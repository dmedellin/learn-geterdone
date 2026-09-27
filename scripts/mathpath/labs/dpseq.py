"""Course 7's kit -- nine modes, one recursion filled from the end.

Backward recursion is the half of this subject a reader finds strange, and the
way to make it ordinary is to put the forward answer next to it. Every mode
here computes its value twice: once by the recursion, and once by enumerating
the thing the recursion is a shortcut for -- every path, every allocation,
every order pattern, every policy, every strategy, every accept-set. The two
numbers are printed side by side, and when the enumeration is too big to run
the page says the claim is unchecked rather than making it anyway.

  stages       a staged network solved backwards, with EVERY optimal path kept
               -- "the optimal policy is unique" is what this mode refutes --
               beside the forward enumeration of all of them
  allocation   indivisible units across activities: the state is what is LEFT,
               the network is built from a return table rather than given, and
               every composition is enumerated beside it
  lotsize      Wagner-Whitin, the F(t) table with the argmin in each row, and
               the 2^(T-1) order patterns enumerated
  heuristics   Silver-Meal and least-unit-cost traced against the exact answer,
               with each plan re-priced from scratch rather than trusted
  stochastic   the finite-horizon recursion on exact rationals, against every
               deterministic policy evaluated by pushing a distribution FORWARD
  tree         a payoff table and a prior folded back; EVPI, and EVSI when a
               likelihood is given, with every signal-to-act strategy enumerated
  stopping     sell-or-wait thresholds, against every accept-set in every
               period -- which shows the threshold form rather than assuming it
  secretary    the exact P(r) table, against the rule played out on all n!
               orderings, with n/e beside it and labelled as the limit it is
  discount     value iteration against the exact fixed point (I - gP)^-1 r, the
               residual checked to zero, and the denominators growing on the way

EVERY PRESET PINS WHAT IT PRINTS, AND NO PRESET CARRIES PROSE ANY MORE. Each
of the 27 presets used to carry a `note`, and every mode here RENDERED the
selected one into its side panel, after the words "On this example:". That is
prose about an outcome, no check in this repository could read it, and a
fifteen-kit sweep found 57 such strings false across the library. The notes are
gone, the panel intros now end at the sentence before them, and the slot the
note occupied holds `expect`: {kpi element id: the exact text the page prints}.
scripts/labcheck.js selects the option on the BUILT page, dispatches the menu's
own change handler and compares the tile's textContent.

Writing them turned up one preset whose PAGE and whose NAME disagree:
`secretary/hundred` asks for 100 candidates and the control is a range of
3..60 that redraw() clamps to, so every reader sees n = 60. The expectations
pin what the page prints and the comment beside them says what it would print
at 100, so raising the cap fails this check instead of passing quietly. See
`_expect` below and scripts/mathpath/AGENTS.md for the rule.

WHAT THIS KIT DOES NOT CONTAIN.

  AN INFINITE-HORIZON POLICY ITERATION. `policyIterate` lives in or_core's
  CHAIN_JS and belongs to course 9, where a chain has already been defined.
  `discount` shows the fixed point and the iteration converging to it, which is
  as much of the infinite horizon as a course with no chains behind it can
  honestly claim.

  A CONTINUOUS STATE. Every state here is one of a listed few, and every
  quantity is a rational. A DP over a continuous resource is a different
  subject and the discretisation is the interesting part of it, which this
  course does not have room to do properly.

  A FORWARD RECURSION AS AN ALTERNATIVE ALGORITHM. `everyPath` enumerates; it
  is an ORACLE, not a second method, and it is exponential on purpose. Offering
  it as a way to solve these problems would undo the lesson.

BLOCKS PER MODE. or_core's docstring puts this kit's engine share at 6.1 KB
gzipped, which is the smallest on the path, so the selection here is modest:
only `discount` needs the matrix block, only `secretary` needs the harmonic
sum, and only five modes draw a plot. Measured as whole pages -- rendered by
scripts/mathpath/render.py, frame and prose included, and taking the WORST of
the nine Integer Programming lessons' prose bodies for each mode, because this
course is not authored yet and a mode measured against thin prose is not
measured:

    allocation 38.7 KB   stages 39.0   lotsize 39.7   heuristics 39.9
    tree 41.0   secretary 41.1   stopping 41.2   stochastic 41.3   discount 42.6

against the 62 KB ceiling, so every mode here has at least 19 KB of room.
Re-derive rather than trusting these -- they go stale as the engine grows.
"""

import re

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import DPSEQ_JS, ORFMT_JS
from .sysdesign_core import HARMONIC_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions only, so scripts/mathcheck.js
# executes the shipped source: nothing here touches the document, and every
# drawing function takes data and returns a string.
# ---------------------------------------------------------------------------

DPKIT_JS = r"""

  /* ================================================ a staged network, as text

     Stages are separated by semicolons and nodes by spaces:

         A ; B C ; D E ; F

     and an arc is  tail>head cost .  An arc may skip a stage forward -- the
     recursion handles it, because the value of a node is filled once every
     node it can reach already has one -- but it may never point backwards or
     sideways, and the refusal says which arc did. */

  var DPNODES = 16;      /* nodes the drawing can label */
  var DPARCS = 28;
  var DPPATHS = 4000;    /* paths the enumeration will walk before refusing */

  function dpClauses(text, sep) {
    var parts = String(text).split(sep || /[,;\n]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }

  function parseStages(text) {
    var cols = dpClauses(text, /[;\n]+/), stages = [], seen = {}, total = 0, i, k;
    if (cols.length < 2) return { bad: 'a staged network needs at least two stages, separated by a semicolon' };
    for (i = 0; i < cols.length; i += 1) {
      var names = cols[i].split(/[\s,]+/).filter(function (t) { return t.length; }), col = [];
      if (!names.length) return { bad: 'stage ' + (i + 1) + ' has no nodes in it' };
      for (k = 0; k < names.length; k += 1) {
        if (!/^[A-Za-z0-9][A-Za-z0-9]{0,3}$/.test(names[k])) {
          return { bad: '"' + esc(names[k]) + '" is not a node name: up to four letters or digits' };
        }
        if (seen[names[k]] !== undefined) {
          return { bad: esc(names[k]) + ' is in two stages at once, and a stage is meant to say when' };
        }
        seen[names[k]] = i;
        col.push(names[k]);
        total += 1;
      }
      stages.push(col);
    }
    if (total > DPNODES) {
      return { bad: 'that is ' + total + ' nodes, and this drawing labels at most ' + DPNODES };
    }
    return { stages: stages, stageOf: seen };
  }

  function parseDpArcs(text, stageOf) {
    var cl = dpClauses(text), arcs = [], i;
    if (!cl.length) return { bad: 'there are no arcs here yet' };
    if (cl.length > DPARCS) {
      return { bad: 'that is ' + cl.length + ' arcs, and this drawing labels at most ' + DPARCS };
    }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z0-9][A-Za-z0-9]{0,3})\s*(?:->|>)\s*([A-Za-z0-9][A-Za-z0-9]{0,3})\s+(.*)$/.exec(cl[i]);
      if (!m) {
        return { bad: '"' + esc(cl[i]) + '" is not an arc: write the tail, then &gt;, then the head, then its cost' };
      }
      if (stageOf[m[1]] === undefined) return { bad: 'there is no node called ' + esc(m[1]) + ' in any stage' };
      if (stageOf[m[2]] === undefined) return { bad: 'there is no node called ' + esc(m[2]) + ' in any stage' };
      if (stageOf[m[2]] <= stageOf[m[1]]) {
        return { bad: esc(m[1]) + ' is in stage ' + (stageOf[m[1]] + 1) + ' and ' + esc(m[2])
                      + ' in stage ' + (stageOf[m[2]] + 1) + ', so that arc runs backwards or sideways; '
                      + 'a staged network only ever moves forward' };
      }
      var v = Rread(m[3].trim());
      if (v === null) return { bad: '"' + esc(m[3]) + '" in "' + esc(cl[i]) + '" is not a number' };
      arcs.push({ from: m[1], to: m[2], cost: v });
    }
    return { arcs: arcs };
  }

  /* THE ORACLE.  Every path from a first-stage node to a last-stage one,
     walked forward and priced as it goes.  This shares no line with
     `backwardStages`: it never forms a value for a node, only for a whole
     path, and it is exponential on purpose -- it is what the recursion is a
     shortcut FOR, and the mode prints both numbers. */
  function everyPath(stages, arcs, opts) {
    opts = opts || {};
    var maximise = opts.maximise === true, cap = opts.cap || DPPATHS;
    var last = {}, k, i;
    for (k = 0; k < stages[stages.length - 1].length; k += 1) last[stages[stages.length - 1][k]] = true;
    var out = [], best = null, bestPaths = [], count = 0, truncated = false;
    var walk = function (at, acc, cost) {
      if (truncated) return;
      if (last[at]) {
        count += 1;
        if (count > cap) { truncated = true; return; }
        var end = opts.terminal && opts.terminal[at] !== undefined ? Radd(cost, opts.terminal[at]) : cost;
        out.push({ path: acc.slice(), cost: end });
        if (best === null || (maximise ? Rcmp(end, best) > 0 : Rcmp(end, best) < 0)) {
          best = end; bestPaths = [acc.slice()];
        } else if (Requ(end, best)) bestPaths.push(acc.slice());
        return;
      }
      for (var j = 0; j < arcs.length; j += 1) {
        if (arcs[j].from !== at) continue;
        acc.push(arcs[j].to);
        walk(arcs[j].to, acc, Radd(cost, arcs[j].cost));
        acc.pop();
      }
    };
    for (i = 0; i < stages[0].length; i += 1) walk(stages[0][i], [stages[0][i]], R0);
    return { paths: out, best: best, bestPaths: bestPaths, count: count, truncated: truncated };
  }

  /* A path priced from the arcs, so a path the recursion RETURNS can be
     checked rather than believed. */
  function pathCost(path, arcs) {
    var total = R0, k, j;
    for (k = 0; k + 1 < path.length; k += 1) {
      var hit = -1;
      for (j = 0; j < arcs.length; j += 1) {
        if (arcs[j].from === path[k] && arcs[j].to === path[k + 1]) { hit = j; break; }
      }
      if (hit < 0) return { ok: false, why: 'there is no arc from ' + path[k] + ' to ' + path[k + 1] };
      total = Radd(total, arcs[hit].cost);
    }
    return { ok: true, cost: total };
  }

  /* ============================================================== drawing

     The layered picture the staged modes share: one column per stage, one
     circle per node, arcs labelled with their cost and thickened when they are
     on an optimal path. */
  function dpXY(v) { return Math.round(v * 10) / 10; }

  function dpNet(stages, arcs, opts) {
    opts = opts || {};
    var width = opts.width || 660, height = opts.height || 280;
    var left = 40, right = width - 40, top = 34, bottom = height - 26;
    var pos = {}, s = '', i, k, j;
    var cols = stages.length, dx = cols > 1 ? (right - left) / (cols - 1) : 0;
    for (i = 0; i < cols; i += 1) {
      var m = stages[i].length;
      for (k = 0; k < m; k += 1) {
        var y = m === 1 ? (top + bottom) / 2
          : top + (bottom - top) * (k / (m - 1)) * (m > 1 ? 1 : 0);
        pos[stages[i][k]] = { x: left + i * dx, y: y };
      }
      s += '<text x="' + dpXY(left + i * dx) + '" y="16" text-anchor="middle" font-size="10" '
        + 'fill="var(--muted)">' + (opts.stageName ? opts.stageName(i) : 'stage ' + (i + 1)) + '</text>';
    }
    for (j = 0; j < arcs.length; j += 1) {
      var a = pos[arcs[j].from], b = pos[arcs[j].to];
      if (!a || !b) continue;
      var tone = (opts.tone && opts.tone(j)) || 'line-strong';
      var wide = opts.wide && opts.wide(j);
      var ddx = b.x - a.x, ddy = b.y - a.y, len = Math.sqrt(ddx * ddx + ddy * ddy) || 1;
      var ux = ddx / len, uy = ddy / len;
      s += '<line x1="' + dpXY(a.x + ux * 15) + '" y1="' + dpXY(a.y + uy * 15) + '" x2="'
        + dpXY(b.x - ux * 15) + '" y2="' + dpXY(b.y - uy * 15) + '" stroke="var(--' + tone
        + ')" stroke-width="' + (wide ? 2.6 : 1.1) + '" />';
      var label = opts.label ? opts.label(j) : Rtext(arcs[j].cost);
      if (label) {
        s += '<text x="' + dpXY((a.x + b.x) / 2 - uy * 9) + '" y="' + dpXY((a.y + b.y) / 2 + ux * 9 + 3)
          + '" text-anchor="middle" font-size="9" fill="var(--' + (wide ? tone : 'muted') + ')">'
          + label + '</text>';
      }
    }
    for (i = 0; i < cols; i += 1) {
      for (k = 0; k < stages[i].length; k += 1) {
        var id = stages[i][k], p = pos[id];
        var ring = (opts.nodeTone && opts.nodeTone(id)) || 'line-strong';
        s += '<circle cx="' + dpXY(p.x) + '" cy="' + dpXY(p.y) + '" r="14" fill="var(--panel-2)" '
          + 'stroke="var(--' + ring + ')" stroke-width="1.6" />'
          + '<text x="' + dpXY(p.x) + '" y="' + dpXY(p.y + 4) + '" text-anchor="middle" font-size="11" '
          + 'font-weight="700" fill="var(--text)">' + id + '</text>';
        var under = opts.under && opts.under(id);
        if (under) {
          s += '<text x="' + dpXY(p.x) + '" y="' + dpXY(p.y + 28) + '" text-anchor="middle" '
            + 'font-size="9" fill="var(--cyan)">' + under + '</text>';
        }
      }
    }
    if (opts.caption) {
      s += '<text x="' + dpXY(width / 2) + '" y="' + dpXY(height - 6) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + opts.caption + '</text>';
    }
    return s;
  }

  /* ========================================= allocation, built from a table

     `P 0 5 9 12` is an activity and what it returns for 0, 1, 2, 3 units.  The
     staged network is BUILT from that table rather than typed: a node is
     "how many units are left before this activity decides", which is the thing
     a reader has to see to understand what a state is. */
  function parseReturns(text) {
    var cl = dpClauses(text, /[;\n]+/), acts = [], width = null, i, k;
    if (!cl.length) return { bad: 'there are no activities here yet' };
    if (cl.length > 4) return { bad: 'that is ' + cl.length + ' activities, and this lab allocates across at most 4' };
    for (i = 0; i < cl.length; i += 1) {
      var parts = cl[i].split(/[\s,]+/).filter(function (t) { return t.length; });
      if (parts.length < 2) return { bad: '"' + esc(cl[i]) + '" gives no returns at all' };
      var name = parts[0], vals = [];
      if (!/^[A-Za-z][A-Za-z0-9]{0,3}$/.test(name)) {
        return { bad: '"' + esc(name) + '" is not an activity name' };
      }
      for (k = 1; k < parts.length; k += 1) {
        var v = Rread(parts[k]);
        if (v === null) return { bad: '"' + esc(parts[k]) + '" in "' + esc(cl[i]) + '" is not a number' };
        vals.push(v);
      }
      if (width === null) width = vals.length;
      if (vals.length !== width) {
        return { bad: esc(name) + ' gives ' + vals.length + ' returns where ' + acts[0].id + ' gives '
                      + width + '; every activity has to be priced at the same levels' };
      }
      if (!Rzero(vals[0])) {
        return { bad: 'putting nothing into ' + esc(name) + ' returns ' + Rtext(vals[0])
                      + ', and a table whose first column is not zero is measuring something else' };
      }
      acts.push({ id: name, ret: vals });
    }
    if (width > 7) return { bad: 'that is ' + (width - 1) + ' units, and this lab allocates at most 6' };
    return { acts: acts, levels: width - 1 };
  }

  /* The stages and arcs of the allocation network, from the return table. */
  function allocNetwork(acts, units) {
    var stages = [], arcs = [], i, r, x;
    for (i = 0; i <= acts.length; i += 1) {
      var col = [];
      for (r = units; r >= 0; r -= 1) col.push('s' + i + 'r' + r);
      stages.push(col);
    }
    for (i = 0; i < acts.length; i += 1) {
      for (r = 0; r <= units; r += 1) {
        for (x = 0; x <= r && x < acts[i].ret.length; x += 1) {
          arcs.push({ from: 's' + i + 'r' + r, to: 's' + (i + 1) + 'r' + (r - x),
                      cost: acts[i].ret[x], act: i, take: x });
        }
      }
    }
    return { stages: stages, arcs: arcs, start: 's0r' + units };
  }

  /* THE ORACLE for the allocation.  Every way to split the units, enumerated
     directly from the table with no network anywhere near it. */
  function everyAllocation(acts, units) {
    var best = null, bestAt = [], count = 0, k = acts.length, pick = [];
    var walk = function (i, left) {
      if (i === k) {
        count += 1;
        var total = R0, q;
        for (q = 0; q < k; q += 1) total = Radd(total, acts[q].ret[pick[q]]);
        if (best === null || Rcmp(total, best) > 0) { best = total; bestAt = [pick.slice()]; }
        else if (Requ(total, best)) bestAt.push(pick.slice());
        return;
      }
      for (var x = 0; x <= left && x < acts[i].ret.length; x += 1) {
        pick.push(x); walk(i + 1, left - x); pick.pop();
      }
    };
    walk(0, units);
    return { best: best, at: bestAt, count: count };
  }

  /* ====================================== plans, priced from scratch

     A lot-sizing plan is a list of orders.  Every routine that produces one
     also reports a cost; this prices the plan again from the demand, the setup
     charge and the holding rate, so a heuristic's own bookkeeping is never the
     only witness to what it spent. */
  function planCost(plan, demand, K, h) {
    var total = R0, covered = [], k, t;
    for (k = 0; k < demand.length; k += 1) covered.push(false);
    for (k = 0; k < plan.length; k += 1) {
      var from = plan[k].covers[0], to = plan[k].covers[1], qty = R0, hold = R0;
      for (t = from; t <= to; t += 1) {
        if (t < 1 || t > demand.length) return { ok: false, why: 'the plan covers a period that does not exist' };
        if (covered[t - 1]) return { ok: false, why: 'period ' + t + ' is covered twice' };
        covered[t - 1] = true;
        qty = Radd(qty, demand[t - 1]);
        hold = Radd(hold, Rmul(R(BigInt(t - from), 1n), demand[t - 1]));
      }
      if (!Requ(qty, plan[k].quantity)) {
        return { ok: false, why: 'the order in period ' + from + ' is ' + Rtext(plan[k].quantity)
                                 + ' where the demand it covers is ' + Rtext(qty) };
      }
      total = Radd(total, Radd(K, Rmul(h, hold)));
    }
    for (k = 0; k < demand.length; k += 1) {
      if (!covered[k]) return { ok: false, why: 'period ' + (k + 1) + ' is never covered' };
    }
    return { ok: true, cost: total };
  }

  /* THE ORACLE for lot sizing: every subset of periods to order in.  An
     optimal plan never orders while stock remains, so a plan IS a partition of
     1..T into consecutive intervals, and there are 2^(T-1) of them. */
  function everyOrderPattern(demand, K, h, cap) {
    var T = demand.length, limit = cap || 4096;
    if (T > 13 || (1 << (T - 1)) > limit) {
      return { truncated: true, why: T + ' periods is 2^' + (T - 1)
                                     + ' order patterns, past what this page enumerates' };
    }
    var best = null, bestMask = null, count = 0, mask, k, t;
    for (mask = 0; mask < (1 << (T - 1)); mask += 1) {
      var orders = [0];
      for (k = 1; k < T; k += 1) if (mask & (1 << (k - 1))) orders.push(k);
      var cost = R0;
      for (k = 0; k < orders.length; k += 1) {
        var from = orders[k], to = k + 1 < orders.length ? orders[k + 1] : T;
        cost = Radd(cost, K);
        for (t = from; t < to; t += 1) cost = Radd(cost, Rmul(h, Rmul(R(BigInt(t - from), 1n), demand[t])));
      }
      count += 1;
      if (best === null || Rcmp(cost, best) < 0) { best = cost; bestMask = orders.slice(); }
    }
    return { truncated: false, best: best, orders: bestMask, count: count };
  }

  /* A row of numbers, as a reader types them. */
  function parseRow(text) {
    var parts = String(text).split(/[\s,;]+/).filter(function (t) { return t.length; }), out = [], k;
    if (!parts.length) return null;
    for (k = 0; k < parts.length; k += 1) {
      var v = Rread(parts[k]);
      if (v === null) return null;
      out.push(v);
    }
    return out;
  }

  /* A table a reader types: one row per line, rows separated by semicolons. */
  function parseMatrixRows(text, rows, cols) {
    var lines = dpClauses(text, /[;\n]+/), out = [], i;
    if (rows && lines.length !== rows) {
      return { bad: 'that is ' + lines.length + ' row' + (lines.length === 1 ? '' : 's')
                    + ' where ' + rows + ' were expected' };
    }
    for (i = 0; i < lines.length; i += 1) {
      var vals = parseRow(lines[i]);
      if (vals === null) return { bad: 'row ' + (i + 1) + ' is not a row of numbers' };
      if (cols && vals.length !== cols) {
        return { bad: 'row ' + (i + 1) + ' has ' + vals.length + ' entries where ' + cols + ' were expected' };
      }
      if (i && vals.length !== out[0].length) {
        return { bad: 'row ' + (i + 1) + ' has ' + vals.length + ' entries and row 1 has ' + out[0].length };
      }
      out.push(vals);
    }
    if (!out.length) return { bad: 'there is no table here yet' };
    return { rows: out };
  }

  /* A distribution: value:probability pairs that must sum to one exactly.  A
     page that renormalised silently would be answering a different question
     from the one the reader typed. */
  function parsePmf(text) {
    var cl = dpClauses(text), out = [], total = R0, i;
    if (!cl.length) return { bad: 'there is no distribution here yet' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(-?[0-9/.]+)\s*[:=]\s*(.*)$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not a value and a probability: write 20:1/3' };
      var v = Rread(m[1]), p = Rread(m[2].trim());
      if (v === null) return { bad: '"' + esc(m[1]) + '" is not a number' };
      if (p === null) return { bad: '"' + esc(m[2]) + '" is not a probability' };
      if (Rsign(p) < 0) return { bad: 'a probability of ' + Rtext(p) + ' is negative' };
      total = Radd(total, p);
      out.push([v, p]);
    }
    if (!Requ(total, R1)) {
      return { bad: 'those probabilities add to ' + Rtext(total) + ' rather than 1 — nothing here '
                    + 'renormalises for you, because a distribution that does not add up is a '
                    + 'modelling error rather than a typing one' };
    }
    return { pmf: out };
  }
"""


DPPLOT_JS = r"""
  /* One plot for the modes that have a curve: a list of series, each a list of
     [x, y] rationals.  Exact in, pixels out -- `Rnum` appears here and nowhere
     else in those modes. */
  function dpPlot(series, opts) {
    opts = opts || {};
    var width = opts.width || 520, height = opts.height || 240;
    var left = 46, right = width - 14, top = 16, bottom = height - 30;
    var xlo = null, xhi = null, ylo = null, yhi = null, i, k;
    for (i = 0; i < series.length; i += 1) {
      for (k = 0; k < series[i].points.length; k += 1) {
        var px = Rnum(series[i].points[k][0]), py = Rnum(series[i].points[k][1]);
        if (xlo === null || px < xlo) xlo = px;
        if (xhi === null || px > xhi) xhi = px;
        if (ylo === null || py < ylo) ylo = py;
        if (yhi === null || py > yhi) yhi = py;
      }
    }
    if (xlo === null) return '';
    if (opts.zero && ylo > 0) ylo = 0;
    if (xhi === xlo) xhi = xlo + 1;
    if (yhi === ylo) yhi = ylo + 1;
    var X = function (v) { return left + (right - left) * ((Rnum(v) - xlo) / (xhi - xlo)); };
    var Y = function (v) { return bottom - (bottom - top) * ((Rnum(v) - ylo) / (yhi - ylo)); };
    var s = '<line x1="' + dpXY(left) + '" y1="' + dpXY(bottom) + '" x2="' + dpXY(right) + '" y2="'
      + dpXY(bottom) + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + dpXY(left) + '" y1="' + dpXY(top) + '" x2="' + dpXY(left) + '" y2="'
      + dpXY(bottom) + '" stroke="var(--line-strong)" stroke-width="1" />';
    for (i = 0; i < series.length; i += 1) {
      var se = series[i], tone = se.tone || 'cyan', d = '';
      for (k = 0; k < se.points.length; k += 1) {
        d += (k ? ' L ' : 'M ') + dpXY(X(se.points[k][0])) + ' ' + dpXY(Y(se.points[k][1]));
      }
      if (se.points.length > 1 && se.line !== false) {
        s += '<path d="' + d + '" fill="none" stroke="var(--' + tone + ')" stroke-width="'
          + (se.wide ? 2.4 : 1.6) + '"' + (se.dash ? ' stroke-dasharray="4 3"' : '') + ' />';
      }
      if (se.dots !== false) {
        for (k = 0; k < se.points.length; k += 1) {
          var mark = se.mark && se.mark(k);
          s += '<circle cx="' + dpXY(X(se.points[k][0])) + '" cy="' + dpXY(Y(se.points[k][1]))
            + '" r="' + (mark ? 4.4 : 2.6) + '" fill="var(--' + (mark ? 'purple' : tone) + ')" />';
        }
      }
      if (se.name) {
        s += '<text x="' + dpXY(right) + '" y="' + dpXY(top + 12 + i * 13) + '" text-anchor="end" '
          + 'font-size="10" fill="var(--' + tone + ')">' + se.name + '</text>';
      }
    }
    s += '<text x="' + dpXY(left) + '" y="' + dpXY(bottom + 15) + '" text-anchor="middle" font-size="10" '
      + 'fill="var(--muted)">' + (opts.xlo === undefined ? xlo : opts.xlo) + '</text>'
      + '<text x="' + dpXY(right) + '" y="' + dpXY(bottom + 15) + '" text-anchor="middle" font-size="10" '
      + 'fill="var(--muted)">' + (opts.xhi === undefined ? xhi : opts.xhi) + '</text>'
      + '<text x="' + dpXY(left - 6) + '" y="' + dpXY(top + 4) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">' + (opts.yhi === undefined ? yhi : opts.yhi) + '</text>'
      + '<text x="' + dpXY(left - 6) + '" y="' + dpXY(bottom) + '" text-anchor="end" font-size="10" '
      + 'fill="var(--muted)">' + (opts.ylo === undefined ? ylo : opts.ylo) + '</text>';
    if (opts.caption) {
      s += '<text x="' + dpXY(width / 2) + '" y="' + dpXY(height - 6) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + opts.caption + '</text>';
    }
    return s;
  }

  /* Bars over a discrete index: demand, an order plan, a threshold per period. */
  function dpBars(items, opts) {
    opts = opts || {};
    var width = opts.width || 660, height = opts.height || 140;
    var left = 36, right = width - 12, top = 18, bottom = height - 26;
    var hi = null, k;
    for (k = 0; k < items.length; k += 1) {
      var v = Rnum(items[k].value);
      if (hi === null || v > hi) hi = v;
    }
    if (!(hi > 0)) hi = 1;
    var step = (right - left) / Math.max(1, items.length), s = '';
    s += '<line x1="' + dpXY(left) + '" y1="' + dpXY(bottom) + '" x2="' + dpXY(right) + '" y2="'
      + dpXY(bottom) + '" stroke="var(--line-strong)" stroke-width="1" />';
    for (k = 0; k < items.length; k += 1) {
      var h = (bottom - top) * (Rnum(items[k].value) / hi), x = left + step * k + step * 0.18;
      var w = step * 0.64, tone = items[k].tone || 'cyan';
      s += '<rect x="' + dpXY(x) + '" y="' + dpXY(bottom - h) + '" width="' + dpXY(w) + '" height="'
        + dpXY(Math.max(1, h)) + '" rx="2" fill="var(--' + tone + ')" fill-opacity="0.32" stroke="var(--'
        + tone + ')" stroke-width="1.2" />'
        + '<text x="' + dpXY(x + w / 2) + '" y="' + dpXY(bottom - h - 4) + '" text-anchor="middle" '
        + 'font-size="9" font-weight="600" fill="var(--' + tone + ')">' + Rtext(items[k].value) + '</text>'
        + '<text x="' + dpXY(x + w / 2) + '" y="' + dpXY(bottom + 13) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">' + items[k].label + '</text>';
    }
    if (opts.caption) {
      s += '<text x="' + dpXY(width / 2) + '" y="' + dpXY(height - 4) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + opts.caption + '</text>';
    }
    return s;
  }
"""


DPPOL_JS = r"""
  /* ======================================= every policy, evaluated FORWARDS

     `stochasticDp` fills a table from the last period back.  This does the
     opposite in both senses: it enumerates the policies one at a time and
     evaluates each by pushing a probability distribution FORWARD from the
     starting state, collecting the reward period by period.  There is no
     value function anywhere in it, so it cannot share a mistake with the
     recursion it is checking.

     |A|^(n * T) policies, which is why there is a cap and why the cap is
     reported rather than silently applied. */
  function evaluateForward(states, P, r, T, policy, start, terminal) {
    var n = states.length, dist = [], i, j, t;
    for (i = 0; i < n; i += 1) dist.push(i === start ? R1 : R0);
    var total = R0;
    for (t = 0; t < T; t += 1) {
      var next = [];
      for (i = 0; i < n; i += 1) next.push(R0);
      for (i = 0; i < n; i += 1) {
        if (Rzero(dist[i])) continue;
        var a = policy[t][i];
        total = Radd(total, Rmul(dist[i], r[a][i]));
        for (j = 0; j < n; j += 1) next[j] = Radd(next[j], Rmul(dist[i], P[a][i][j]));
      }
      dist = next;
    }
    if (terminal) {
      for (i = 0; i < n; i += 1) total = Radd(total, Rmul(dist[i], terminal[i]));
    }
    return { value: total, endDist: dist };
  }

  function everyPolicy(states, acts, P, r, T, opts) {
    opts = opts || {};
    var n = states.length, A = acts.length, slots = n * T, cap = opts.cap || 20000;
    var totalPolicies = Math.pow(A, slots);
    if (totalPolicies > cap) {
      return { truncated: true, count: totalPolicies,
               why: A + '^' + slots + ' = ' + totalPolicies + ' policies, past what this page enumerates' };
    }
    var best = [], bestPol = [], i, t, k;
    for (i = 0; i < n; i += 1) { best.push(null); bestPol.push(null); }
    var digits = [], count = 0;
    for (k = 0; k < slots; k += 1) digits.push(0);
    while (true) {
      var policy = [];
      for (t = 0; t < T; t += 1) {
        var row = [];
        for (i = 0; i < n; i += 1) row.push(digits[t * n + i]);
        policy.push(row);
      }
      count += 1;
      for (i = 0; i < n; i += 1) {
        var v = evaluateForward(states, P, r, T, policy, i, opts.terminal).value;
        var better = best[i] === null
          || (opts.minimise ? Rcmp(v, best[i]) < 0 : Rcmp(v, best[i]) > 0);
        if (better) { best[i] = v; bestPol[i] = policy.map(function (q) { return q.slice(); }); }
      }
      var pnt = slots - 1;
      while (pnt >= 0 && digits[pnt] === A - 1) { digits[pnt] = 0; pnt -= 1; }
      if (pnt < 0) break;
      digits[pnt] += 1;
    }
    return { truncated: false, best: best, policies: bestPol, count: count };
  }

  /* A transition matrix a reader types, one row per state, rows separated by
     semicolons.  Every row must sum to one exactly. */
  function parseStochastic(text, n) {
    var rows = dpClauses(text, /[;\n]+/), out = [], i, j;
    if (rows.length !== n) {
      return { bad: 'that is ' + rows.length + ' rows for ' + n + ' states; one row per state, '
                    + 'separated by semicolons' };
    }
    for (i = 0; i < n; i += 1) {
      var vals = parseRow(rows[i]);
      if (vals === null) return { bad: 'row ' + (i + 1) + ' is not a row of numbers' };
      if (vals.length !== n) {
        return { bad: 'row ' + (i + 1) + ' has ' + vals.length + ' entries and there are ' + n + ' states' };
      }
      var total = R0;
      for (j = 0; j < n; j += 1) {
        if (Rsign(vals[j]) < 0) return { bad: 'row ' + (i + 1) + ' has a negative probability in it' };
        total = Radd(total, vals[j]);
      }
      if (!Requ(total, R1)) {
        return { bad: 'row ' + (i + 1) + ' adds to ' + Rtext(total) + ' rather than 1' };
      }
      out.push(vals);
    }
    return { rows: out };
  }
"""


DPTREE_JS = r"""
  /* ============================= a decision tree, built from a payoff table

     Typing a tree is harder than typing the thing a tree is drawn FROM, so the
     reader gives a payoff matrix, a prior and -- optionally -- a likelihood,
     and the tree is built here.  Without a likelihood it is one decision over
     a chance node per act; with one it is a chance node over signals, and
     inside each of those the same decision again over the posterior.

     THE ORACLE is `everyStrategy`: a strategy is a choice of act for each
     signal, there are |A|^|G| of them, and each is priced directly from the
     joint distribution with no tree involved.  The best of them must equal
     what the tree folds back to. */
  function priorTree(payoff, prior, names, stateNames) {
    var A = payoff.length, S = prior.length, kids = [], a, s;
    for (a = 0; a < A; a += 1) {
      var branches = [];
      for (s = 0; s < S; s += 1) {
        branches.push({ p: prior[s], label: stateNames[s],
                        node: { kind: 'leaf', value: payoff[a][s], label: stateNames[s] } });
      }
      kids.push({ label: names[a], node: { kind: 'chance', children: branches, label: names[a] } });
    }
    return { root: { kind: 'decision', children: kids, label: 'act' }, payoff: payoff, prior: prior };
  }

  function signalTree(payoff, prior, likelihood, names, stateNames, signalNames) {
    var A = payoff.length, S = prior.length, G = likelihood.length, kids = [], g, a, s;
    for (g = 0; g < G; g += 1) {
      var joint = [], pg = R0;
      for (s = 0; s < S; s += 1) {
        var jj = Rmul(prior[s], likelihood[g][s]);
        joint.push(jj); pg = Radd(pg, jj);
      }
      var acts = [];
      for (a = 0; a < A; a += 1) {
        var branches = [];
        for (s = 0; s < S; s += 1) {
          branches.push({ p: Rzero(pg) ? R0 : Rdiv(joint[s], pg), label: stateNames[s],
                          node: { kind: 'leaf', value: payoff[a][s], label: stateNames[s] } });
        }
        acts.push({ label: names[a], node: { kind: 'chance', children: branches, label: names[a] } });
      }
      kids.push({ p: pg, label: signalNames[g],
                  node: { kind: 'decision', children: acts, label: signalNames[g] } });
    }
    return { root: { kind: 'chance', children: kids, label: 'signal' },
             payoff: payoff, prior: prior, likelihood: likelihood };
  }

  /* THE ORACLE.  Every signal-to-act strategy, priced from the joint
     distribution.  No node, no fold, no posterior: just sum over signals and
     states of P(signal, state) times the payoff of the act this strategy uses
     when it sees that signal. */
  function everyStrategy(payoff, prior, likelihood) {
    var A = payoff.length, S = prior.length, G = likelihood ? likelihood.length : 1;
    var best = null, bestPick = null, count = 0, pick = [];
    /* EVERY loop variable here is local to its own call. They used to be
       declared on the line above, shared by every level of the recursion, and
       the inner `for (a = 0; a < A; ...)` left `a === A` behind when it
       returned -- so the caller's own loop ended immediately and this function
       enumerated only the strategies whose earlier signals all map to act 0.
       Measured: 2 of 4, 3 of 9, 2 of 4 on the three shipped presets. The BEST
       value came out right on all three by luck, because the optimum happens
       to assign act 0 to the first signal in each, so the page's agreement
       check passed while the count it printed -- "N ways to map what you see
       to what you do" -- was wrong on every one. */
    var walk = function (i) {
      if (i === G) {
        count += 1;
        var total = R0, g, s;
        for (g = 0; g < G; g += 1) {
          for (s = 0; s < S; s += 1) {
            var pj = likelihood ? Rmul(prior[s], likelihood[g][s]) : prior[s];
            total = Radd(total, Rmul(pj, payoff[pick[g]][s]));
          }
        }
        if (best === null || Rcmp(total, best) > 0) { best = total; bestPick = pick.slice(); }
        return;
      }
      var a;
      for (a = 0; a < A; a += 1) { pick.push(a); walk(i + 1); pick.pop(); }
    };
    walk(0);
    return { best: best, pick: bestPick, count: count };
  }

  /* The tree, drawn.  A decision node is a square, a chance node a circle, and
     the branch the fold chose is thickened -- which is the only part of the
     picture a reader has to trust, so it is the part that is drawn loudest. */
  function dpTree(folded, opts) {
    opts = opts || {};
    var width = opts.width || 660, height = opts.height || 300;
    var left = 26, right = width - 70, top = 20, bottom = height - 22;
    var leaves = [], depth = 0;
    var measure = function (node, d) {
      if (d > depth) depth = d;
      if (node.kind === 'leaf') { leaves.push(node); return 1; }
      var total = 0, k;
      for (k = 0; k < node.children.length; k += 1) total += measure(node.children[k].node, d + 1);
      return total;
    };
    var root = folded.root.node || folded.root;
    var count = measure(root, 0);
    var dx = depth > 0 ? (right - left) / depth : 0;
    var dy = count > 1 ? (bottom - top) / (count - 1) : 0;
    var slot = 0, s = '';
    var place = function (node, d, chosen) {
      var y, k;
      if (node.kind === 'leaf') { y = top + dy * slot; slot += 1; }
      else {
        var ys = [];
        for (k = 0; k < node.children.length; k += 1) {
          ys.push(place(node.children[k].node, d + 1,
                        node.kind === 'decision' ? (node.choiceIndex === k) : true));
        }
        y = (ys[0] + ys[ys.length - 1]) / 2;
        for (k = 0; k < node.children.length; k += 1) {
          var kid = node.children[k];
          var on = node.kind !== 'decision' || node.choiceIndex === k;
          s += '<line x1="' + dpXY(left + d * dx + 9) + '" y1="' + dpXY(y) + '" x2="'
            + dpXY(left + (d + 1) * dx - 9) + '" y2="' + dpXY(ys[k]) + '" stroke="var(--'
            + (on ? 'cyan' : 'line-strong') + ')" stroke-width="' + (on ? 2.2 : 1) + '" />'
            + '<text x="' + dpXY(left + d * dx + 14) + '" y="' + dpXY((y + ys[k]) / 2 - 3)
            + '" font-size="9" fill="var(--muted)">' + (kid.label || '')
            + (kid.p !== undefined ? ' ' + Rtext(kid.p) : '') + '</text>';
        }
      }
      var tone = chosen ? 'cyan' : 'line-strong';
      if (node.kind === 'decision') {
        s += '<rect x="' + dpXY(left + d * dx - 8) + '" y="' + dpXY(y - 8) + '" width="16" height="16" '
          + 'fill="var(--panel-2)" stroke="var(--' + tone + ')" stroke-width="1.6" />';
      } else if (node.kind === 'chance') {
        s += '<circle cx="' + dpXY(left + d * dx) + '" cy="' + dpXY(y) + '" r="8" fill="var(--panel-2)" '
          + 'stroke="var(--' + tone + ')" stroke-width="1.6" />';
      } else {
        s += '<text x="' + dpXY(left + d * dx + 6) + '" y="' + dpXY(y + 4) + '" font-size="10" '
          + 'font-weight="600" fill="var(--' + (chosen ? 'green' : 'muted') + ')">'
          + Rtext(node.value) + '</text>';
      }
      if (node.kind !== 'leaf' && node.folded !== undefined) {
        s += '<text x="' + dpXY(left + d * dx) + '" y="' + dpXY(y - 12) + '" text-anchor="middle" '
          + 'font-size="9" fill="var(--purple)">' + Rtext(node.folded) + '</text>';
      }
      return y;
    };
    place(root, 0, true);
    if (opts.caption) {
      s += '<text x="' + dpXY(width / 2) + '" y="' + dpXY(height - 5) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + opts.caption + '</text>';
    }
    return s;
  }

  /* `foldBack` returns the values in a flat list keyed by path; this hangs
     them back on the nodes so the drawing can print each one where it belongs
     and mark the branch the fold chose. */
  function annotate(folded) {
    var byPath = {}, k;
    for (k = 0; k < folded.values.length; k += 1) byPath[folded.values[k].path] = folded.values[k];
    var walk = function (node, path) {
      var got = byPath[path];
      if (got) {
        node.folded = got.value;
        if (got.choice !== undefined) node.choiceIndex = got.choice;
      }
      if (node.kind === 'leaf') return;
      for (var q = 0; q < node.children.length; q += 1) walk(node.children[q].node, path + '.' + q);
    };
    walk(folded.root.node, '0');
    return folded;
  }
"""


DPSTOP_JS = r"""
  /* ======================================= every accept-set, in every period

     `stopThresholds` computes a threshold per period and takes an offer when
     it beats the threshold.  That is a claim with a shape in it -- that the
     optimal rule is a threshold -- and a page can prove the shape rather than
     assume it: enumerate, for each period, EVERY subset of the offer values
     that the rule might accept, and evaluate the resulting rule exactly.
     2^(|S| * T) of them, which is small for a page-sized problem, and the best
     of them turns out to be a threshold rule every time.

     A rule is `sets[t][k] = true` meaning "with t periods left, accept offer
     k".  It is evaluated backwards over the DISTRIBUTION, which is not the
     same computation as the threshold recursion: that one asks what carrying
     on is worth, this one asks what THIS rule is worth. */
  function ruleValue(pmf, sets, c) {
    var T = sets.length, v = R0, t, k;
    for (t = 0; t < T; t += 1) {
      var e = R0;
      for (k = 0; k < pmf.length; k += 1) {
        e = Radd(e, Rmul(pmf[k][1], sets[t][k] ? pmf[k][0] : v));
      }
      v = Rsub(e, c);
    }
    return v;
  }

  function everyStoppingRule(pmf, T, c, opts) {
    opts = opts || {};
    var S = pmf.length, slots = S * T, cap = opts.cap || 8192;
    if (Math.pow(2, slots) > cap) {
      return { truncated: true, count: Math.pow(2, slots),
               why: '2^' + slots + ' accept-sets, past what this page enumerates' };
    }
    var best = null, bestSets = null, count = 0, bits = [], k, t;
    for (k = 0; k < slots; k += 1) bits.push(0);
    while (true) {
      var sets = [];
      for (t = 0; t < T; t += 1) {
        var row = [];
        for (k = 0; k < S; k += 1) row.push(!!bits[t * S + k]);
        sets.push(row);
      }
      var v = ruleValue(pmf, sets, c);
      count += 1;
      if (best === null || Rcmp(v, best) > 0) {
        best = v;
        bestSets = sets.map(function (q) { return q.slice(); });
      }
      var p = slots - 1;
      while (p >= 0 && bits[p] === 1) { bits[p] = 0; p -= 1; }
      if (p < 0) break;
      bits[p] = 1;
    }
    /* is the winner a threshold rule?  accepting x implies accepting anything
       larger, in every period. */
    var isThreshold = true, sorted = pmf.map(function (q, i) { return i; }).sort(function (a, b) {
      return Rcmp(pmf[a][0], pmf[b][0]);
    });
    for (t = 0; t < T; t += 1) {
      var seenAccept = false;
      for (k = 0; k < sorted.length; k += 1) {
        if (bestSets[t][sorted[k]]) seenAccept = true;
        else if (seenAccept) isThreshold = false;
      }
    }
    return { truncated: false, best: best, sets: bestSets, count: count,
             threshold: isThreshold, order: sorted };
  }

  /* The accept-sets the THRESHOLD rule describes, so the two can be compared
     set by set rather than only by their values. */
  function thresholdSets(pmf, rows) {
    var sets = [], t, k;
    for (t = rows.length - 1; t >= 0; t -= 1) {
      var row = [];
      for (k = 0; k < pmf.length; k += 1) row.push(Rcmp(pmf[k][0], rows[t].threshold) > 0);
      sets.push(row);
    }
    return sets;
  }

  /* 1/e, as the exact partial sum of  sum (-1)^k / k!  taken far enough that
     the next term is below the last digit anyone prints.  The secretary
     problem's "look at n/e of them" is a LIMIT, and this is that limit shown
     as what it is -- a rounding of an irrational number -- beside an exact
     P(r) table that never needed it. */
  function invE(terms) {
    var total = R0, fact = 1n, k, upto = terms || 20;
    for (k = 0; k <= upto; k += 1) {
      if (k) fact *= BigInt(k);
      total = Radd(total, R(k % 2 === 0 ? 1n : -1n, fact));
    }
    return total;
  }

  /* THE ORACLE for the secretary problem: the rule played out on every one of
     the n! orderings of the ranks.  `secretaryExact` sums a harmonic series;
     this one counts, and the two have no line in common. */
  function secretaryBrute(n, cap) {
    if (n > (cap || 7)) {
      return { truncated: true, why: n + '! orderings is past what this page walks' };
    }
    var counts = [], r, k;
    for (r = 0; r <= n; r += 1) counts.push(0);
    var perm = [], used = [], total = 0;
    var walk = function () {
      if (perm.length === n) {
        total += 1;
        for (r = 1; r <= n; r += 1) {
          /* look at the first r - 1, then take the first one better than all of them */
          var bestSeen = 0, took = -1;
          for (k = 0; k < r - 1; k += 1) if (perm[k] > bestSeen) bestSeen = perm[k];
          for (k = r - 1; k < n; k += 1) {
            if (perm[k] > bestSeen) { took = perm[k]; break; }
          }
          if (took === n) counts[r] += 1;
        }
        return;
      }
      for (var v = 1; v <= n; v += 1) {
        if (used[v]) continue;
        used[v] = true; perm.push(v); walk(); perm.pop(); used[v] = false;
      }
    };
    walk();
    var probs = [];
    for (r = 1; r <= n; r += 1) probs.push({ r: r, p: R(BigInt(counts[r]), BigInt(total)) });
    return { truncated: false, probs: probs, total: total, counts: counts };
  }
"""


# ---------------------------------------------------------------------------
# WHICH BLOCKS EACH MODE SHIPS. The rule is integer.py's: a block belongs in a
# mode's list when that mode CALLS something in it. DPSEQ_JS is one block and
# every mode takes it whole, but the things hanging off it are selected --
# `discount` is the only mode that reaches Mrref, `secretary` the only one that
# reaches the harmonic sum, and the tree layout and the stopping oracles belong
# to one mode each.
#
# DPSTOP_JS carries both optimal-stopping oracles: `everyStoppingRule` for the
# sell-or-wait mode and `secretaryBrute` for the secretary one. They are one
# block because they are one idea -- play the rule out rather than reason about
# it -- and neither mode is heavy enough for the split to pay.
# ---------------------------------------------------------------------------

_BASE = RATIONAL_JS + FORMAT_JS + ORFMT_JS + DPSEQ_JS + DPKIT_JS

_MODE_JS = {
    "stages": _BASE,
    "allocation": _BASE,
    "lotsize": _BASE + DPPLOT_JS,
    "heuristics": _BASE + DPPLOT_JS,
    "stochastic": _BASE + DPPLOT_JS + DPPOL_JS,
    "tree": _BASE + DPTREE_JS,
    "stopping": _BASE + DPPLOT_JS + DPSTOP_JS,
    "secretary": (RATIONAL_JS + FORMAT_JS + ORFMT_JS + HARMONIC_JS + DPSEQ_JS + DPKIT_JS
                  + DPPLOT_JS + DPSTOP_JS),
    "discount": (RATIONAL_JS + FORMAT_JS + MATRIX_JS + ORFMT_JS + DPSEQ_JS + DPKIT_JS + DPPLOT_JS),
}


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the rest of the library uses.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


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
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    """A text box that starts EMPTY, and is filled by the script at startup.

    One field on this kit -- the arc list -- contains a `>` in every clause,
    and a default carried in the markup cannot hold one: escaped as `&gt;` a
    browser decodes it and scripts/labcheck.js does not, so the harness would
    run the page against a spec of literal entities; left raw it terminates the
    `<input ...>` match in that harness's own tag scanner and the value is lost
    instead. Either way the one harness that executes these labs would be
    executing the error branch. network.py hit this first and this is its fix.

    Every text box in this kit uses it rather than only the arc one, so there
    is a single rule here instead of a trap waiting for whoever adds a field
    with a `>` in it. `value` is still written into the page as a placeholder,
    with any `>` spelled out, so the markup still says what the box is for.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(str(value).replace(">", " to ")))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n' % (label, cid)
        for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    # The `x` math shorthand, converted here the way render.inline() converts it
    # everywhere else. A hint is raw markup like every other panel string, so
    # the marks do NOT convert themselves -- two hints in this kit shipped
    # sixteen literal backtick characters to the reader before anything looked.
    # Kept local rather than imported, because labs/ does not depend on render.
    text = re.sub(r"`([^`]+)`", r'<span class="math">\1</span>', text)
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)
        for tone, text in legend
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


def _js(text):
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
    """The preset table, as data the script reads -- not as branches.

    Every preset goes through the same parser the reader's own typing does, so
    a preset cannot show a number the typed version would not.
    """
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _fill_js(name, fields):
    """The startup fill for the script-filled text boxes.

    Written once here rather than in nine scripts, because forgetting it in one
    of them gives a page whose controls are empty until the reader types --
    which looks like a styling problem and is not.
    """
    lines = ["  var START = %s[%sIn.value] || %s[Object.keys(%s)[0]];" % (name, "preset", name, name)]
    for cid, key in fields:
        lines.append("  if (START && !%s.value) %s.value = START.%s;" % (cid, cid, key))
    return "\n".join(lines) + "\n"


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _expect(presets):
    """{preset id: {kpi element id: the exact text the page prints}}.

    A preset's `label` is prose about an instance and no check in this
    repository can read it. This is the other half of the same claim, and it is
    the half a machine can hold: what the page PRINTS once the preset is
    selected. scripts/labcheck.js selects the option on the BUILT page,
    dispatches the menu's own change handler and compares
    getElementById(kpi).textContent with the string here. Every figure below
    was read off the running kit with `node scripts/labcheck.js --observe
    <page>`, never copied out of the code that computes it.

    Tiles are read with every OTHER control at the value the markup ships, so a
    claim that only becomes visible once another control moves cannot be pinned
    here; those are named in a comment beside the preset that makes them.
    """
    return {p["id"]: dict(p.get("expect") or {}) for p in presets}


def _choose(cfg, mode, presets, default):
    """The preset this lesson opens on, or a refusal.

    A preset that fell back to a default would render the right lesson's widget
    opened on someone else's worked example -- the panel's numbers would not be
    the prose's numbers -- and nothing in the suite would notice, because the
    lab still builds and still draws.
    """
    name = str(cfg.get("preset", default))
    for p in presets:
        if p["id"] == name:
            return p
    raise ValueError(
        "dpseq_lab: mode %r has no preset %r; its presets are %s"
        % (mode, name, ", ".join(sorted(p["id"] for p in presets)))
    )


# ---------------------------------------------------------------------------
# L1 -- stages: the recursion, and every path it stands for
# ---------------------------------------------------------------------------

_ST_PRESETS = [
    {
        "id": "tie",
        "label": "one optimal route, and a tie that is not on it",
        "stages": "A; B C; D E; F",
        "arcs": "A>B 2, A>C 4, B>D 7, B>E 4, C>D 3, C>E 2, D>F 1, E>F 4",
        "expect": {
            "stValue": "8",
            "stRoutes": "1 of 4",
            "stTies": "B",
        },
    },
    {
        "id": "several",
        "label": "three routes, all optimal",
        "stages": "A; B C; D E; F",
        "arcs": "A>B 0, A>C 4, B>D 7, B>E 4, C>D 3, C>E 2, D>F 1, E>F 4",
        "expect": {
            "stValue": "8",
            "stRoutes": "3 of 4",
            "stTies": "B, A",
        },
    },
    {
        "id": "skip",
        "label": "an arc that skips a stage",
        "stages": "A; B C; D E; F",
        "arcs": "A>B 2, A>C 4, A>E 3, B>D 7, B>E 4, C>D 3, C>E 2, D>F 1, E>F 4",
        "expect": {
            "stValue": "7",
            "stCount": "5",
        },
    },
]


def _stages(cfg):
    chosen = _choose(cfg, "stages", _ST_PRESETS, "tie")

    markup = (
        _toolbar(
            "Filling the table from the end",
            "the value of being somewhere is the step plus the value of where it leads",
            [("cyan", "an arc the recursion chose"), ("purple", "a tie, kept rather than resolved"),
             ("green", "the value of each node"), ("line-strong", "an arc it did not choose")],
        )
        + _stage(_svg("stNet", "0 0 660 280",
                      "The staged network, each node carrying the value the recursion gave it and "
                      "each chosen arc drawn thick."))
        + _table("stTable")
        + _table("stPaths")
        + _banner("stStatus")
    )
    controls = (
        _select("stPreset", "Worked example", _options(_ST_PRESETS), chosen["id"])
        + _text("stStages", "The stages, separated by semicolons", chosen["stages"])
        + _text("stArcs", "The arcs, as tail&gt;head cost", chosen["arcs"])
        + _select("stDir", "The recursion",
                  [("min", "take the cheapest continuation"), ("max", "take the richest continuation")],
                  "min")
        + _kpis([
            ("The value at the start", "stValue"),
            ("By enumerating every path", "stForward"),
            ("Do the two agree?", "stAgree"),
            ("Paths there are", "stCount"),
            ("Optimal routes", "stRoutes"),
            ("Nodes with a tie", "stTies"),
        ])
        + _hint(
            "stHint",
            "The table is filled from the last stage backwards, and a node's value never changes once "
            "it is written &mdash; that is the whole reason the recursion is cheaper than the "
            "enumeration beside it. Every argmin is kept, not the first one found, because "
            "&ldquo;the optimal policy is unique&rdquo; is false and the ties are where it is false.",
        )
    )

    script = _MODE_JS["stages"] + r"""
""" + _presets_js("STP", _ST_PRESETS, ["stages", "arcs"]) + r"""
  var presetIn = document.getElementById('stPreset');
  var stagesIn = document.getElementById('stStages'), arcsIn = document.getElementById('stArcs');
  var dirIn = document.getElementById('stDir');
  var net = document.getElementById('stNet');
  var tableT = document.getElementById('stTable'), pathsT = document.getElementById('stPaths');
  var status = document.getElementById('stStatus');
  var KPIS = ['stValue', 'stForward', 'stAgree', 'stCount', 'stRoutes', 'stTies'];

  function blank(why) {
    net.innerHTML = ''; tableT.innerHTML = ''; pathsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Stages are separated by semicolons '
      + 'and an arc is a tail, then <span class="tone-muted">&gt;</span>, then a head, then its cost.';
  }

  function redraw() {
    var sp = parseStages(stagesIn.value);
    if (sp.bad) { blank(sp.bad); return; }
    var ap = parseDpArcs(arcsIn.value, sp.stageOf);
    if (ap.bad) { blank(ap.bad); return; }
    var stages = sp.stages, arcs = ap.arcs, maximise = dirIn.value === 'max', i, k, j;
    if (stages[0].length !== 1) { blank('this mode wants one node in the first stage, so the value at the start is one number'); return; }
    var back = backwardStages(stages, arcs, { maximise: maximise });
    var fwd = everyPath(stages, arcs, { maximise: maximise });
    if (fwd.truncated) { blank(fwd.why || 'there are too many paths here to enumerate them all'); return; }
    if (fwd.best === null) { blank('no path reaches the last stage at all'); return; }
    var agree = back.value !== null && Requ(back.value, fwd.best);

    var chosen = {};
    for (var node in back.argmin) {
      if (!Object.prototype.hasOwnProperty.call(back.argmin, node)) continue;
      for (k = 0; k < back.argmin[node].length; k += 1) chosen[back.argmin[node][k].arc] = back.argmin[node].length;
    }
    net.innerHTML = dpNet(stages, arcs, {
      width: 660, height: 280,
      tone: function (q) { return chosen[q] ? (chosen[q] > 1 ? 'purple' : 'cyan') : 'line-strong'; },
      wide: function (q) { return !!chosen[q]; },
      under: function (id) { return back.f[id] === undefined || back.f[id] === null ? null : Rtext(back.f[id]); },
      nodeTone: function (id) { return back.ties.some(function (t) { return t.node === id; }) ? 'purple' : 'line-strong'; },
      caption: 'the number under each node is what it is worth from there on'
    });

    var rows = '';
    for (i = stages.length - 1; i >= 0; i -= 1) {
      for (k = 0; k < stages[i].length; k += 1) {
        var id = stages[i][k], picks = back.argmin[id] || [];
        var opts = [];
        for (j = 0; j < arcs.length; j += 1) {
          if (arcs[j].from !== id || back.f[arcs[j].to] === undefined) continue;
          opts.push(arcs[j].to + ': ' + Rtext(arcs[j].cost) + ' + ' + Rtext(back.f[arcs[j].to])
                    + ' = ' + Rtext(Radd(arcs[j].cost, back.f[arcs[j].to])));
        }
        rows += tr([rowhead('stage ' + (i + 1) + ', ' + id),
                    td(back.f[id] === null || back.f[id] === undefined ? '—' : Rtext(back.f[id])),
                    tdl(opts.length ? opts.join(' &nbsp;|&nbsp; ') : 'nothing left to do'),
                    td(picks.length
                        ? (picks.length > 1
                            ? tone(picks.map(function (q) { return q.to; }).join(' or '), 'purple')
                            : picks[0].to)
                        : '—')],
                   picks.length > 1 ? 'tone-purple' : null);
      }
    }
    tableT.innerHTML = '<caption>The table, filled from the last stage back</caption><thead>'
      + tr([th('node'), th('its value'), th('each continuation, priced'), th('which it takes')])
      + '</thead><tbody>' + rows + '</tbody>';

    var sorted = fwd.paths.slice().sort(function (a, b) { return Rcmp(a.cost, b.cost) * (maximise ? -1 : 1); });
    var prows = '', limit = Math.min(sorted.length, 14), ok = true;
    for (i = 0; i < limit; i += 1) {
      var best = Requ(sorted[i].cost, fwd.best);
      var priced = pathCost(sorted[i].path, arcs);
      if (!priced.ok || !Requ(priced.cost, sorted[i].cost)) ok = false;
      prows += tr([rowhead(sorted[i].path.join(' → ')), td(Rtext(sorted[i].cost)),
                   td(best ? tone('optimal', 'green') : '')], best ? 'tone-green' : null);
    }
    if (sorted.length > limit) {
      prows += tr([tdl('and ' + (sorted.length - limit) + ' more, all of them priced', 'small-copy')
                   .replace('<td', '<td colspan="3"')]);
    }
    pathsT.innerHTML = '<caption>Every path from the first stage to the last, walked forwards</caption>'
      + '<thead>' + tr([th('path'), th('total cost'), th('')]) + '</thead><tbody>' + prows + '</tbody>';

    var recon = true, badPath = null;
    for (i = 0; i < back.policy.length; i += 1) {
      var pc = pathCost(back.policy[i], arcs);
      if (!pc.ok || !Requ(pc.cost, back.value)) { recon = false; badPath = back.policy[i].join(' → '); }
    }

    document.getElementById('stValue').textContent = back.value === null ? '—' : Rtext(back.value);
    document.getElementById('stForward').textContent = Rtext(fwd.best);
    document.getElementById('stAgree').textContent = agree && recon && ok ? 'yes' : 'NO';
    document.getElementById('stCount').textContent = String(fwd.count);
    document.getElementById('stRoutes').textContent = back.policy.length + ' of ' + fwd.count;
    document.getElementById('stTies').textContent = back.ties.length
      ? back.ties.map(function (t) { return t.node; }).join(', ') : 'none';

    if (!agree || !recon || !ok) {
      status.innerHTML = '<strong>' + tone('These two do not agree, so neither is shown as an answer.', 'red')
        + '</strong> The recursion says ' + (back.value === null ? 'nothing' : Rtext(back.value))
        + ' and walking every path says ' + Rtext(fwd.best)
        + (recon ? '' : '; and the route it reconstructed, ' + badPath + ', does not cost what it claims')
        + '. That is a defect in the kit and not in your network.';
      return;
    }
    status.innerHTML = '<strong>The recursion fills ' + tone(String(fwd.count === 0 ? 0
        : Object.keys(back.f).length), 'cyan') + ' values and stops at '
      + tone(Rtext(back.value), 'green') + '.</strong> Walking all ' + fwd.count
      + ' paths forwards reaches the same number, and each of the '
      + tone(back.policy.length + ' optimal route' + plural(back.policy.length, '', 's'), 'green')
      + ' it reconstructed was priced again from the arcs before it was printed: '
      + back.policy.map(function (q) { return q.join(' → '); }).join(', ') + '. '
      + (back.ties.length
          ? 'There ' + (back.ties.length === 1 ? 'is a tie at ' : 'are ties at ')
            + tone(back.ties.map(function (t) { return t.node; }).join(' and '), 'purple')
            + ' — two continuations worth exactly the same. '
            + (back.policy.length > 1
                ? 'They are on an optimal route, so there really are '
                  + back.policy.length + ' best answers and a page that printed one would be wrong.'
                : 'Neither is on an optimal route, so the answer is still unique — but the tie is kept '
                  + 'rather than quietly resolved, because one changed cost puts it on the route.')
          : 'No node has a tie here, so the optimal route is unique — which is a fact about this '
            + 'instance and not about dynamic programming. Open the second example.');
  }

  function apply() {
    var p = STP[presetIn.value];
    if (!p) return;
    stagesIn.value = p.stages; arcsIn.value = p.arcs;
    redraw();
  }
""" + _fill_js("STP", [("stagesIn", "stages"), ("arcsIn", "arcs")]) + r"""
  presetIn.addEventListener('change', apply);
  dirIn.addEventListener('change', redraw);
  stagesIn.addEventListener('input', redraw);
  arcsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Filling the table from the end",
        subtitle="Every value the recursion writes, beside every path it stands for",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a staged network and watch it fill backwards"),
        panel_intro=cfg.get(
            "panel_intro",
            "The recursion runs from the last stage back; every path is then walked forwards and "
            "priced independently, and nothing is shown unless the two agree.",
        ),
        script=script,
        expect={"stPreset": _expect(_ST_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L2 -- allocation: the state is what is LEFT
# ---------------------------------------------------------------------------

_AL_PRESETS = [
    {
        "id": "diminishing",
        "label": "three activities with diminishing returns",
        "returns": "P 0 5 9 12 14; Q 0 4 8 11 13; R 0 6 9 11 12",
        "units": "4",
        # Two different splits reach 19 and the tile names the one the recursion took;
        # the count of splits that tie is in the enumeration table, not in a tile.
        "expect": {
            "alBestV": "19",
            "alForward": "19",
            "alPick": "P=1, Q=2, R=1",
        },
    },
    {
        "id": "lumpy",
        "label": "a return that jumps",
        "returns": "P 0 2 4 15 16; Q 0 6 8 9 10; R 0 3 7 8 9",
        "units": "4",
        "expect": {
            "alBestV": "21",
            "alPick": "P=3, Q=1, R=0",
        },
    },
    {
        "id": "twoway",
        "label": "two activities, so the table can be read across",
        "returns": "P 0 7 11 14 15; Q 0 5 10 13 16",
        "units": "4",
        "expect": {
            "alBestV": "21",
            "alCount": "15",
        },
    },
]


def _allocation(cfg):
    chosen = _choose(cfg, "allocation", _AL_PRESETS, "diminishing")

    markup = (
        _toolbar(
            "Allocating indivisible units",
            "the state is how much is left, and the network is built from the table rather than given",
            [("cyan", "an allocation the recursion chose"), ("purple", "a tie"),
             ("green", "the value of each state"), ("line-strong", "an allocation it did not take")],
        )
        + _stage(_svg("alNet", "0 0 660 300",
                      "The allocation network: one column per activity, one node per amount still unspent."))
        + _table("alTable")
        + _table("alBest")
        + _banner("alStatus")
    )
    controls = (
        _select("alPreset", "Worked example", _options(_AL_PRESETS), chosen["id"])
        + _text("alReturns", "Each activity and what it returns for 0, 1, 2, ... units",
                chosen["returns"])
        + _range("alUnits", "Units to allocate", 1, 6, int(chosen["units"]))
        + _kpis([
            ("The best total return", "alBestV"),
            ("By enumerating every split", "alForward"),
            ("Do the two agree?", "alAgree"),
            ("The allocation it chose", "alPick"),
            ("States the recursion visited", "alStates"),
            ("Splits there are", "alCount"),
        ])
        + _hint(
            "alHint",
            "There is no network to type here: the nodes are the amounts that could still be "
            "unspent when an activity has to decide, and the arcs are the amounts it could take. "
            "Building that network is the lesson &mdash; once it exists, this is the previous page "
            "again.",
        )
    )

    script = _MODE_JS["allocation"] + r"""
""" + _presets_js("ALP", _AL_PRESETS, ["returns", "units"]) + r"""
  var presetIn = document.getElementById('alPreset'), retIn = document.getElementById('alReturns');
  var unitsIn = document.getElementById('alUnits');
  var net = document.getElementById('alNet');
  var tableT = document.getElementById('alTable'), bestT = document.getElementById('alBest');
  var status = document.getElementById('alStatus');
  var KPIS = ['alBestV', 'alForward', 'alAgree', 'alPick', 'alStates', 'alCount'];

  function blank(why) {
    net.innerHTML = ''; tableT.innerHTML = ''; bestT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An activity is a name and then '
      + 'what it returns for nothing, one unit, two units and so on, with activities separated by '
      + 'semicolons.';
  }

  function redraw() {
    var parsed = parseReturns(retIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var acts = parsed.acts, i, k, r, x;
    var units = Math.max(1, Math.min(Math.min(6, parsed.levels), Math.round(+unitsIn.value)));
    document.getElementById('alUnitsOut').textContent = units
      + (units < Math.round(+unitsIn.value) ? ' (the table only prices ' + parsed.levels + ')' : '');
    var netw = allocNetwork(acts, units);
    var back = backwardStages(netw.stages, netw.arcs, { maximise: true });
    var brute = everyAllocation(acts, units);
    var agree = back.f[netw.start] !== undefined && Requ(back.f[netw.start], brute.best);

    var chosen = {};
    for (var node in back.argmin) {
      if (!Object.prototype.hasOwnProperty.call(back.argmin, node)) continue;
      for (k = 0; k < back.argmin[node].length; k += 1) chosen[back.argmin[node][k].arc] = back.argmin[node].length;
    }
    net.innerHTML = dpNet(netw.stages, netw.arcs, {
      width: 660, height: 300,
      stageName: function (q) { return q < acts.length ? acts[q].id : 'done'; },
      label: function (q) { return netw.arcs[q].take + 'u'; },
      tone: function (q) { return chosen[q] ? (chosen[q] > 1 ? 'purple' : 'cyan') : 'line-strong'; },
      wide: function (q) { return !!chosen[q]; },
      under: function (id) { return back.f[id] === undefined || back.f[id] === null ? null : Rtext(back.f[id]); },
      caption: 'a node is how many units are still unspent; an arc is how many this activity takes'
    });

    var rows = '';
    for (i = acts.length - 1; i >= 0; i -= 1) {
      for (r = units; r >= 0; r -= 1) {
        var id = 's' + i + 'r' + r, picks = back.argmin[id] || [], opts = [];
        for (k = 0; k < netw.arcs.length; k += 1) {
          if (netw.arcs[k].from !== id) continue;
          var to = netw.arcs[k].to;
          if (back.f[to] === undefined) continue;
          opts.push(netw.arcs[k].take + ' → ' + Rtext(netw.arcs[k].cost) + ' + ' + Rtext(back.f[to])
                    + ' = ' + Rtext(Radd(netw.arcs[k].cost, back.f[to])));
        }
        rows += tr([rowhead(acts[i].id + ', ' + r + ' left'),
                    td(back.f[id] === undefined || back.f[id] === null ? '—' : Rtext(back.f[id])),
                    tdl(opts.join(' &nbsp;|&nbsp; ')),
                    td(picks.length
                        ? picks.map(function (q) { return netw.arcs[q.arc].take + 'u'; }).join(' or ')
                        : '—')],
                   picks.length > 1 ? 'tone-purple' : null);
      }
    }
    tableT.innerHTML = '<caption>What each state is worth, filled from the last activity back</caption>'
      + '<thead>' + tr([th('state'), th('its value'), th('each amount it could take, priced'),
                        th('which it takes')]) + '</thead><tbody>' + rows + '</tbody>';

    var routes = back.policy.filter(function (q) { return q[0] === netw.start; });
    var brows = '', picks = [];
    for (i = 0; i < routes.length && i < 8; i += 1) {
      var take = [], total = R0;
      for (k = 0; k + 1 < routes[i].length; k += 1) {
        for (x = 0; x < netw.arcs.length; x += 1) {
          if (netw.arcs[x].from === routes[i][k] && netw.arcs[x].to === routes[i][k + 1]) {
            take.push(acts[netw.arcs[x].act].id + '=' + netw.arcs[x].take);
            total = Radd(total, netw.arcs[x].cost);
            break;
          }
        }
      }
      picks.push(take.join(', '));
      brows += tr([rowhead(take.join(', ')), td(Rtext(total)),
                   td(Requ(total, brute.best) ? tone('matches the enumeration', 'green')
                      : tone('does NOT match the enumeration', 'red'))],
                  Requ(total, brute.best) ? 'tone-green' : 'tone-red');
    }
    for (i = 0; i < brute.at.length && i < 8; i += 1) {
      var names = [];
      for (k = 0; k < acts.length; k += 1) names.push(acts[k].id + '=' + brute.at[i][k]);
      brows += tr([rowhead(names.join(', ')), td(Rtext(brute.best)),
                   td(tone('found by trying all ' + brute.count + ' splits', 'purple'))], 'tone-purple');
    }
    bestT.innerHTML = '<caption>What the recursion reconstructed, and what the enumeration found</caption>'
      + '<thead>' + tr([th('allocation'), th('returns'), th('where it came from')]) + '</thead>'
      + '<tbody>' + brows + '</tbody>';

    document.getElementById('alBestV').textContent = back.f[netw.start] === undefined ? '—'
      : Rtext(back.f[netw.start]);
    document.getElementById('alForward').textContent = Rtext(brute.best);
    document.getElementById('alAgree').textContent = agree ? 'yes' : 'NO';
    document.getElementById('alPick').textContent = picks.length ? picks[0] : '—';
    document.getElementById('alStates').textContent = String(Object.keys(back.f).length);
    document.getElementById('alCount').textContent = String(brute.count);

    if (!agree) {
      status.innerHTML = '<strong>' + tone('The recursion and the enumeration disagree.', 'red')
        + '</strong> Nothing here is an answer until they do not.';
      return;
    }
    var states = Object.keys(back.f).length;
    status.innerHTML = '<strong>The best split returns ' + tone(Rtext(brute.best), 'green')
      + '</strong> — ' + picks.join(' or ') + '. The recursion reached it by writing '
      + tone(states + ' state values', 'cyan') + '; the enumeration reached it by pricing all '
      + tone(brute.count + ' splits', 'purple') + ', and the two numbers are the same. '
      + 'The saving is small at ' + units + ' units and three activities and it is the whole point: '
      + 'the states grow with the units and the splits grow with the units to the power of the '
      + 'activities. '
      + (brute.at.length > 1
          ? 'There are ' + brute.at.length + ' splits that all return the best, so the answer is a '
            + 'set and not a plan.'
          : 'Only one split returns the best here.');
  }

  function apply() {
    var p = ALP[presetIn.value];
    if (!p) return;
    retIn.value = p.returns; unitsIn.value = p.units;
    redraw();
  }
""" + _fill_js("ALP", [("retIn", "returns")]) + r"""
  presetIn.addEventListener('change', apply);
  retIn.addEventListener('input', redraw);
  unitsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Allocating indivisible units",
        subtitle="The state is what is left, and the network has to be built before it can be solved",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Split the units, and check the split against every other one"),
        panel_intro=cfg.get(
            "panel_intro",
            "The return table is turned into a staged network, solved backwards, and then checked "
            "against every possible split enumerated directly from the table.",
        ),
        script=script,
        expect={"alPreset": _expect(_AL_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L3 -- lotsize: Wagner-Whitin, and every order pattern there is
# ---------------------------------------------------------------------------

_LS_PRESETS = [
    {
        "id": "classic",
        "label": "six periods, demand that ramps",
        "demand": "10 62 12 130 154 129",
        "K": "54",
        "h": "2",
        # Which periods share an order -- 2 and 3, and no others -- is the plan table;
        # the number of orders it places is a tile.
        "expect": {
            "wwCost": "294",
            "wwOrders1": "5",
            "wwRepriced": "294 — agrees",
        },
    },
    {
        "id": "flat",
        "label": "steady demand, so the intervals are even",
        "demand": "40 40 40 40 40 40",
        "K": "90",
        "h": "1",
        "expect": {
            "wwCost": "390",
            "wwOrders1": "3",
        },
    },
    {
        "id": "spike",
        "label": "one period that dwarfs the rest",
        "demand": "8 6 200 7 9 5",
        "K": "60",
        "h": "3",
        "expect": {
            "wwCost": "234",
            "wwOrders1": "3",
        },
    },
]


def _lotsize(cfg):
    chosen = _choose(cfg, "lotsize", _LS_PRESETS, "classic")

    markup = (
        _toolbar(
            "Wagner-Whitin: when to order",
            "an optimal plan never orders while stock remains, so a plan is a partition into intervals",
            [("cyan", "demand"), ("green", "a period an order is placed in"),
             ("purple", "the interval that order covers"), ("amber", "holding cost")],
        )
        + _stage(_svg("wwDemand", "0 0 660 140",
                      "Demand period by period.")
                 + _svg("wwOrders", "0 0 660 140",
                        "The quantity ordered in each period under the exact plan."))
        + _table("wwTable")
        + _table("wwPlan")
        + _banner("wwStatus")
    )
    controls = (
        _select("wwPreset", "Worked example", _options(_LS_PRESETS), chosen["id"])
        + _text("wwDemandIn", "Demand, period by period", chosen["demand"])
        + _range("wwK", "The charge for placing an order", 10, 200, int(chosen["K"]), 2)
        + _range("wwH", "Holding cost, per unit per period", 1, 10, int(chosen["h"]))
        + _kpis([
            ("The cheapest plan costs", "wwCost"),
            ("By enumerating every pattern", "wwBrute"),
            ("Do the two agree?", "wwAgree"),
            ("Orders it places", "wwOrders1"),
            ("Patterns there are", "wwPatterns"),
            ("The plan, priced again from scratch", "wwRepriced"),
        ])
        + _hint(
            "wwHint",
            "F(t) is the cheapest way to cover periods 1 to t, and the recursion is over the period "
            "the LAST order was placed in. That works because an optimal plan never orders while "
            "stock remains &mdash; so every plan is a partition of the periods into consecutive "
            "intervals, and there are 2<sup>T&minus;1</sup> of them, all of which are priced here "
            "as a check.",
        )
    )

    script = _MODE_JS["lotsize"] + r"""
""" + _presets_js("LSP", _LS_PRESETS, ["demand", "K", "h"]) + r"""
  var presetIn = document.getElementById('wwPreset'), demIn = document.getElementById('wwDemandIn');
  var kIn = document.getElementById('wwK'), hIn = document.getElementById('wwH');
  var demSvg = document.getElementById('wwDemand'), ordSvg = document.getElementById('wwOrders');
  var tableT = document.getElementById('wwTable'), planT = document.getElementById('wwPlan');
  var status = document.getElementById('wwStatus');
  var KPIS = ['wwCost', 'wwBrute', 'wwAgree', 'wwOrders1', 'wwPatterns', 'wwRepriced'];

  function blank(why) {
    demSvg.innerHTML = ''; ordSvg.innerHTML = ''; tableT.innerHTML = ''; planT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Demand is a row of numbers, one '
      + 'for each period.';
  }

  function redraw() {
    var demand = parseRow(demIn.value);
    if (demand === null) { blank('that is not a row of numbers'); return; }
    if (demand.length < 2) { blank('there is only one period here, and nothing to decide'); return; }
    if (demand.length > 10) { blank('that is ' + demand.length + ' periods, and this lab plans at most 10'); return; }
    var i, t;
    for (i = 0; i < demand.length; i += 1) {
      if (Rsign(demand[i]) < 0) { blank('period ' + (i + 1) + ' has negative demand in it'); return; }
    }
    var K = R(BigInt(Math.round(+kIn.value)), 1n), h = R(BigInt(Math.round(+hIn.value)), 1n);
    document.getElementById('wwKOut').textContent = Rtext(K);
    document.getElementById('wwHOut').textContent = Rtext(h);
    var ww = wagnerWhitin(demand, K, h);
    var repriced = planCost(ww.plan, demand, K, h);
    var brute = everyOrderPattern(demand, K, h);
    var agree = !brute.truncated && Requ(ww.cost, brute.best);

    var orderAt = {};
    for (i = 0; i < ww.plan.length; i += 1) orderAt[ww.plan[i].period] = ww.plan[i];
    demSvg.innerHTML = dpBars(demand.map(function (d, k) {
      return { label: 't' + (k + 1), value: d, tone: orderAt[k + 1] ? 'green' : 'cyan' };
    }), { width: 660, height: 140, caption: 'demand, with the periods an order is placed in in green' });
    ordSvg.innerHTML = dpBars(demand.map(function (d, k) {
      return { label: 't' + (k + 1), value: orderAt[k + 1] ? orderAt[k + 1].quantity : R0,
               tone: orderAt[k + 1] ? 'purple' : 'cyan' };
    }), { width: 660, height: 140, caption: 'what each order buys — nothing in the periods it covers' });

    var rows = '';
    for (t = 0; t < ww.detail.length; t += 1) {
      var d = ww.detail[t], opts = [];
      for (i = 0; i < d.options.length; i += 1) {
        var o = d.options[i];
        opts.push((o.orderAt === d.orderAt ? '<strong>' : '') + 'order at ' + o.orderAt + ': '
                  + Rtext(o.before) + ' + ' + Rtext(K) + ' + ' + Rtext(o.holding) + ' = ' + Rtext(o.value)
                  + (o.orderAt === d.orderAt ? '</strong>' : ''));
      }
      rows += tr([rowhead('F(' + d.t + ')'), td(Rtext(d.value)), td(String(d.orderAt)),
                  tdl(opts.join(' &nbsp;|&nbsp; '))]);
    }
    tableT.innerHTML = '<caption>F(t), the cheapest way to cover periods 1 to t</caption><thead>'
      + tr([th('t'), th('F(t)'), th('last order at'), th('each candidate, priced')]) + '</thead>'
      + '<tbody>' + rows + '</tbody>';

    var prows = '';
    for (i = 0; i < ww.plan.length; i += 1) {
      var p = ww.plan[i], hold = R0;
      for (t = p.covers[0]; t <= p.covers[1]; t += 1) {
        hold = Radd(hold, Rmul(R(BigInt(t - p.covers[0]), 1n), demand[t - 1]));
      }
      prows += tr([rowhead('period ' + p.period), td(Rtext(p.quantity)),
                   td(p.covers[0] === p.covers[1] ? 'period ' + p.covers[0]
                      : 'periods ' + p.covers[0] + ' to ' + p.covers[1]),
                   td(Rtext(K)), td(Rtext(Rmul(h, hold))),
                   td(Rtext(Radd(K, Rmul(h, hold))))]);
    }
    prows += tr([rowhead('in all'), td('—'), td('—'), td(Rtext(Rmul(K, R(BigInt(ww.orders), 1n)))),
                 td(Rtext(Rsub(ww.cost, Rmul(K, R(BigInt(ww.orders), 1n))))),
                 td(tone(Rtext(ww.cost), 'green'))], 'tone-green');
    planT.innerHTML = '<caption>The plan, and what each order costs</caption><thead>'
      + tr([th('ordered in'), th('quantity'), th('covering'), th('setup'), th('holding'), th('total')])
      + '</thead><tbody>' + prows + '</tbody>';

    document.getElementById('wwCost').textContent = Rtext(ww.cost);
    document.getElementById('wwBrute').textContent = brute.truncated ? 'not enumerated' : Rtext(brute.best);
    document.getElementById('wwAgree').textContent = brute.truncated ? 'not checked' : (agree ? 'yes' : 'NO');
    document.getElementById('wwOrders1').textContent = String(ww.orders);
    document.getElementById('wwPatterns').textContent = brute.truncated ? '—' : String(brute.count);
    document.getElementById('wwRepriced').textContent = repriced.ok
      ? Rtext(repriced.cost) + (Requ(repriced.cost, ww.cost) ? ' — agrees' : ' — DISAGREES')
      : repriced.why;

    if (!repriced.ok || !Requ(repriced.cost, ww.cost) || (!brute.truncated && !agree)) {
      status.innerHTML = '<strong>' + tone('The three routes to this number do not agree.', 'red')
        + '</strong> The recursion says ' + Rtext(ww.cost) + ', pricing the plan it returned says '
        + (repriced.ok ? Rtext(repriced.cost) : repriced.why)
        + (brute.truncated ? '' : ', and the enumeration says ' + Rtext(brute.best))
        + '. Nothing here is an answer until they do.';
      return;
    }
    status.innerHTML = '<strong>' + tone(ww.orders + ' order' + plural(ww.orders, '', 's'), 'green')
      + ', costing ' + tone(Rtext(ww.cost), 'green') + ' in all.</strong> The recursion filled '
      + ww.detail.length + ' values of F; the plan it returned was priced again from the demand, the '
      + Rtext(K) + ' charge and the ' + Rtext(h) + '-per-unit holding rate and came to the same '
      + 'number; and ' + (brute.truncated ? brute.why
          : 'all ' + brute.count + ' order patterns were priced and none of them beat it')
      + '. Raise the order charge and the intervals get longer; raise the holding cost and they get '
      + 'shorter — the plan is the balance of the two, and neither alone decides it.';
  }

  function apply() {
    var p = LSP[presetIn.value];
    if (!p) return;
    demIn.value = p.demand; kIn.value = p.K; hIn.value = p.h;
    redraw();
  }
""" + _fill_js("LSP", [("demIn", "demand")]) + r"""
  presetIn.addEventListener('change', apply);
  demIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  hIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Wagner-Whitin: when to order",
        subtitle="A plan is a partition into intervals, and every one of them is priced here",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the charges and watch the intervals move"),
        panel_intro=cfg.get(
            "panel_intro",
            "The recursion is over the period the last order was placed in; the plan it returns is "
            "then priced again from scratch, and the whole thing is checked against every order "
            "pattern.",
        ),
        script=script,
        expect={"wwPreset": _expect(_LS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L4 -- heuristics: two rules of thumb, measured
# ---------------------------------------------------------------------------

_HE_PRESETS = [
    {
        "id": "split",
        "label": "the two heuristics disagree with each other",
        "demand": "10 62 12 130 154 129",
        "K": "54",
        "h": "2",
        "expect": {
            "heExact": "294",
            "heSM": "294",
            "heLUC": "600",
        },
    },
    {
        "id": "both",
        "label": "both of them miss, and by different amounts",
        "demand": "17 25 73 113 89",
        "K": "116",
        "h": "1",
        # How many orders each heuristic places -- three and two -- is in the two
        # traces; what each one gives away is a tile.
        "expect": {
            "heExact": "462",
            "heGapSM": "24 (5.19%)",
            "heGapLUC": "30 (6.49%)",
        },
    },
    {
        "id": "agree",
        "label": "steady demand, and everything agrees",
        "demand": "30 30 30 30 30 30",
        "K": "80",
        "h": "1",
        "expect": {
            "heExact": "330",
            "heSM": "330",
            "heLUC": "330",
        },
    },
]


def _heuristics(cfg):
    chosen = _choose(cfg, "heuristics", _HE_PRESETS, "split")

    markup = (
        _toolbar(
            "Two rules of thumb, against the exact answer",
            "a heuristic that stops when the average turns up can stop in the wrong place",
            [("green", "the exact plan"), ("cyan", "Silver-Meal"),
             ("amber", "least unit cost"), ("red", "what the rule left on the table")],
        )
        + _stage(_svg("heDemand", "0 0 660 140",
                      "Demand period by period, with the exact plan's order periods marked.")
                 + _svg("heCost", "0 0 520 220",
                        "The cost of each plan, against the number of orders it places."))
        + _table("heTrail")
        + _table("heCompare")
        + _banner("heStatus")
    )
    controls = (
        _select("hePreset", "Worked example", _options(_HE_PRESETS), chosen["id"])
        + _text("heDemandIn", "Demand, period by period", chosen["demand"])
        + _range("heK", "The charge for placing an order", 10, 200, int(chosen["K"]), 2)
        + _range("heH", "Holding cost, per unit per period", 1, 10, int(chosen["h"]))
        + _kpis([
            ("The exact cost", "heExact"),
            ("Silver-Meal costs", "heSM"),
            ("Least unit cost costs", "heLUC"),
            ("What Silver-Meal gives away", "heGapSM"),
            ("What least unit cost gives away", "heGapLUC"),
            ("Every plan priced again?", "heRepriced"),
        ])
        + _hint(
            "heHint",
            "Silver-Meal extends an interval while the average cost per PERIOD is falling; "
            "least-unit-cost extends it while the average cost per UNIT is falling. They are "
            "different questions, they stop in different places, and neither of them can see past "
            "the first turn &mdash; which is the failure mode, not the cost.",
        )
    )

    script = _MODE_JS["heuristics"] + r"""
""" + _presets_js("HEP", _HE_PRESETS, ["demand", "K", "h"]) + r"""
  var presetIn = document.getElementById('hePreset'), demIn = document.getElementById('heDemandIn');
  var kIn = document.getElementById('heK'), hIn = document.getElementById('heH');
  var demSvg = document.getElementById('heDemand'), costSvg = document.getElementById('heCost');
  var trailT = document.getElementById('heTrail'), cmpT = document.getElementById('heCompare');
  var status = document.getElementById('heStatus');
  var KPIS = ['heExact', 'heSM', 'heLUC', 'heGapSM', 'heGapLUC', 'heRepriced'];

  function blank(why) {
    demSvg.innerHTML = ''; costSvg.innerHTML = ''; trailT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Demand is a row of numbers, one '
      + 'for each period.';
  }

  function redraw() {
    var demand = parseRow(demIn.value);
    if (demand === null) { blank('that is not a row of numbers'); return; }
    if (demand.length < 2 || demand.length > 10) {
      blank('this lab plans between 2 and 10 periods, and that is ' + (demand ? demand.length : 0));
      return;
    }
    var i, k;
    for (i = 0; i < demand.length; i += 1) {
      if (Rsign(demand[i]) < 0) { blank('period ' + (i + 1) + ' has negative demand in it'); return; }
    }
    var K = R(BigInt(Math.round(+kIn.value)), 1n), h = R(BigInt(Math.round(+hIn.value)), 1n);
    document.getElementById('heKOut').textContent = Rtext(K);
    document.getElementById('heHOut').textContent = Rtext(h);
    var hr = lotsizeHeuristics(demand, K, h);
    var plans = [['the exact plan', hr.exact.plan, hr.exact.cost, 'green'],
                 ['Silver-Meal', hr.silverMeal.plan, hr.silverMeal.cost, 'cyan'],
                 ['least unit cost', hr.leastUnitCost.plan, hr.leastUnitCost.cost, 'amber']];
    var repriced = true, why = '';
    for (i = 0; i < plans.length; i += 1) {
      var pc = planCost(plans[i][1], demand, K, h);
      if (!pc.ok) { repriced = false; why = plans[i][0] + ': ' + pc.why; break; }
      if (!Requ(pc.cost, plans[i][2])) {
        repriced = false;
        why = plans[i][0] + ' reports ' + Rtext(plans[i][2]) + ' and its plan costs ' + Rtext(pc.cost);
        break;
      }
    }
    if (!repriced) { blank('a plan does not cost what it says it costs — ' + why); return; }

    var exactAt = {};
    for (i = 0; i < hr.exact.plan.length; i += 1) exactAt[hr.exact.plan[i].period] = true;
    demSvg.innerHTML = dpBars(demand.map(function (d, q) {
      return { label: 't' + (q + 1), value: d, tone: exactAt[q + 1] ? 'green' : 'cyan' };
    }), { width: 660, height: 140, caption: 'demand, with the exact plan\'s order periods in green' });
    costSvg.innerHTML = dpPlot([{ name: 'cost against orders placed', tone: 'purple', line: false,
        points: plans.map(function (p) { return [R(BigInt(p[1].length), 1n), p[2]]; }),
        mark: function (q) { return q === 0; } }],
      { width: 520, height: 220, zero: false, caption: 'orders placed, against what the plan costs' });

    var rows = '';
    var trails = [['Silver-Meal', hr.silverMeal, 'per period'], ['least unit cost', hr.leastUnitCost, 'per unit']];
    for (i = 0; i < trails.length; i += 1) {
      var st = trails[i][1].steps;
      for (k = 0; k < st.length; k += 1) {
        var cells = st[k].trail.map(function (q) {
          return q.periods + ' period' + plural(q.periods, '', 's') + ': ' + Rtext(q.total) + ' / '
                 + (trails[i][2] === 'per unit' ? Rtext(q.quantity) : q.periods) + ' = '
                 + (q.average === null ? '—' : Rtext(q.average));
        });
        rows += tr([rowhead(trails[i][0]), td('from period ' + st[k].from),
                    td(st[k].span + ' period' + plural(st[k].span, '', 's')),
                    tdl(cells.join(' &nbsp;|&nbsp; '))],
                   i === 0 ? 'tone-cyan' : 'tone-amber');
      }
    }
    trailT.innerHTML = '<caption>Each rule, interval by interval, with the average it watched</caption>'
      + '<thead>' + tr([th('rule'), th('starting at'), th('it took'), th('the averages it saw')])
      + '</thead><tbody>' + rows + '</tbody>';

    var crows = '';
    for (i = 0; i < plans.length; i += 1) {
      var periods = plans[i][1].map(function (q) { return q.period; }).join(', ');
      var gap = Rsub(plans[i][2], hr.exact.cost);
      crows += tr([rowhead(plans[i][0]), td(String(plans[i][1].length)), td(periods),
                   td(Rtext(plans[i][2])),
                   td(Rzero(gap) ? tone('optimal', 'green') : tone('+' + Rtext(gap), 'red'))],
                  Rzero(gap) ? 'tone-green' : 'tone-red');
    }
    cmpT.innerHTML = '<caption>Three plans on the same demand</caption><thead>'
      + tr([th('plan'), th('orders'), th('placed in periods'), th('costs'), th('over the exact answer')])
      + '</thead><tbody>' + crows + '</tbody>';

    document.getElementById('heExact').textContent = Rtext(hr.exact.cost);
    document.getElementById('heSM').textContent = Rtext(hr.silverMeal.cost);
    document.getElementById('heLUC').textContent = Rtext(hr.leastUnitCost.cost);
    document.getElementById('heGapSM').textContent = Rtext(hr.silverMeal.gap)
      + (hr.silverMeal.excess === null ? '' : ' (' + Rpct(hr.silverMeal.excess, 2) + ')');
    document.getElementById('heGapLUC').textContent = Rtext(hr.leastUnitCost.gap)
      + (hr.leastUnitCost.excess === null ? '' : ' (' + Rpct(hr.leastUnitCost.excess, 2) + ')');
    document.getElementById('heRepriced').textContent = 'yes — all three';

    var same = Requ(hr.silverMeal.cost, hr.leastUnitCost.cost);
    status.innerHTML = '<strong>The exact plan costs ' + tone(Rtext(hr.exact.cost), 'green')
      + '; Silver-Meal ' + tone(Rtext(hr.silverMeal.cost), 'cyan') + ' and least-unit-cost '
      + tone(Rtext(hr.leastUnitCost.cost), 'amber') + '.</strong> '
      + (same ? 'The two heuristics agree with each other here — which is not the same as being right. '
              : 'The two heuristics do not even agree with each other, which is worth more than either '
                + 'of their answers: a rule of thumb is a rule, and two rules are two answers. ')
      + (Rzero(hr.silverMeal.gap) && Rzero(hr.leastUnitCost.gap)
          ? 'On this instance both of them happen to find the optimum. Change the order charge and '
            + 'watch how quickly that stops being true.'
          : 'Each rule stops extending an interval the first time its average turns up, and neither '
            + 'can see that the average turns back down again one period later. That is the whole of '
            + 'the failure, and it costs '
            + Rtext(Rcmp(hr.silverMeal.gap, hr.leastUnitCost.gap) > 0 ? hr.silverMeal.gap : hr.leastUnitCost.gap)
            + ' at worst here.')
      + ' Every plan above was priced again from the demand before it was compared, so a rule cannot '
      + 'look good by mis-reporting its own bill.';
  }

  function apply() {
    var p = HEP[presetIn.value];
    if (!p) return;
    demIn.value = p.demand; kIn.value = p.K; hIn.value = p.h;
    redraw();
  }
""" + _fill_js("HEP", [("demIn", "demand")]) + r"""
  presetIn.addEventListener('change', apply);
  demIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  hIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two rules of thumb, against the exact answer",
        subtitle="Silver-Meal and least-unit-cost watch different averages and stop in different places",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Trace both heuristics and price what they produce"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each rule is traced interval by interval with the averages it was watching, and each "
            "plan it produces is priced again from the demand rather than taken on trust.",
        ),
        script=script,
        expect={"hePreset": _expect(_HE_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L5 -- stochastic: the recursion, against every policy pushed forwards
# ---------------------------------------------------------------------------

_SD_PRESETS = [
    {
        "id": "twoact",
        "label": "two states, two actions, three periods",
        "states": "calm rough",
        "acts": "hold act",
        "p0": "1/2 1/2; 1/4 3/4",
        "p1": "3/4 1/4; 1/2 1/2",
        "r": "1 3; 2 1",
        "T": "3",
        # That the optimal policy is the same in all three periods is the policy table,
        # row by row, and not a tile.
        "expect": {
            "sdV1": "53/8",
            "sdB1": "53/8",
            "sdCount": "64",
        },
    },
    {
        "id": "absorb",
        "label": "an action that ends the game",
        "states": "owned sold",
        "acts": "keep sell",
        "p0": "4/5 1/5; 0 1",
        "p1": "0 1; 0 1",
        "r": "3 0; 7 0",
        "T": "3",
        "expect": {
            "sdV1": "247/25",
            "sdV2": "0",
        },
    },
    {
        "id": "flip",
        "label": "the best action changes with how long is left",
        "states": "small large",
        "acts": "grow harvest",
        "p0": "1/4 3/4; 0 1",
        "p1": "1 0; 3/4 1/4",
        "r": "0 1; 3 9",
        "T": "4",
        # The act that changes with the horizon is read off the policy table; what the
        # tiles hold is the value it achieves and how many policies were enumerated
        # against it.
        "expect": {
            "sdV1": "33/2",
            "sdV2": "45/2",
            "sdCount": "256",
        },
    },
]


def _stochastic(cfg):
    chosen = _choose(cfg, "stochastic", _SD_PRESETS, "twoact")

    markup = (
        _toolbar(
            "The stochastic recursion, and every policy there is",
            "a value is an expectation, and the action that maximises it can change with the horizon",
            [("cyan", "the first state"), ("purple", "the second"),
             ("green", "the action the recursion chose"), ("amber", "an action it rejected")],
        )
        + _stage(_svg("sdPlot", "0 0 520 230",
                      "The value of each state against how many periods are left."))
        + _table("sdTable")
        + _table("sdPolicy")
        + _banner("sdStatus")
    )
    controls = (
        _select("sdPreset", "Worked example", _options(_SD_PRESETS), chosen["id"])
        + _text("sdStates", "The states", chosen["states"])
        + _text("sdActs", "The actions", chosen["acts"])
        + _text("sdP0", "Where the first action sends you, row per state", chosen["p0"])
        + _text("sdP1", "Where the second action sends you", chosen["p1"])
        + _text("sdR", "What each action pays in each state, row per action", chosen["r"])
        + _range("sdT", "Periods to go", 1, 4, int(chosen["T"]))
        + _kpis([
            ("The value at the start, state 1", "sdV1"),
            ("By enumerating every policy", "sdB1"),
            ("The value at the start, state 2", "sdV2"),
            ("By enumerating every policy", "sdB2"),
            ("Policies there are", "sdCount"),
            ("Does the chosen policy achieve it?", "sdAchieves"),
        ])
        + _hint(
            "sdHint",
            "The recursion fills one column of values per period, backwards, and takes the best "
            "action in each cell. The check beside it never forms a value at all: it lists every "
            "deterministic policy, pushes a probability distribution forward through each one "
            "collecting reward as it goes, and reports the best. Two computations with no line in "
            "common.",
        )
    )

    script = _MODE_JS["stochastic"] + r"""
""" + _presets_js("SDP", _SD_PRESETS, ["states", "acts", "p0", "p1", "r", "T"]) + r"""
  var presetIn = document.getElementById('sdPreset');
  var statesIn = document.getElementById('sdStates'), actsIn = document.getElementById('sdActs');
  var p0In = document.getElementById('sdP0'), p1In = document.getElementById('sdP1');
  var rIn = document.getElementById('sdR'), tIn = document.getElementById('sdT');
  var plot = document.getElementById('sdPlot');
  var tableT = document.getElementById('sdTable'), polT = document.getElementById('sdPolicy');
  var status = document.getElementById('sdStatus');
  var KPIS = ['sdV1', 'sdB1', 'sdV2', 'sdB2', 'sdCount', 'sdAchieves'];

  function blank(why) {
    plot.innerHTML = ''; tableT.innerHTML = ''; polT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Each row of a transition table is '
      + 'where one state goes, and it has to add to 1.';
  }

  function nameRow(text) {
    return String(text).split(/[\s,;]+/).filter(function (t) { return t.length; });
  }

  function redraw() {
    var states = nameRow(statesIn.value), acts = nameRow(actsIn.value);
    if (states.length !== 2) { blank('this mode takes exactly two states'); return; }
    if (acts.length !== 2) { blank('this mode takes exactly two actions'); return; }
    var n = 2, A = 2, i, k, t, a;
    var m0 = parseStochastic(p0In.value, n);
    if (m0.bad) { blank(acts[0] + ': ' + m0.bad); return; }
    var m1 = parseStochastic(p1In.value, n);
    if (m1.bad) { blank(acts[1] + ': ' + m1.bad); return; }
    var rm = parseMatrixRows(rIn.value, A, n);
    if (rm.bad) { blank('the reward table: ' + rm.bad); return; }
    var P = [m0.rows, m1.rows], r = rm.rows;
    var T = Math.max(1, Math.min(4, Math.round(+tIn.value)));
    document.getElementById('sdTOut').textContent = String(T);

    var dp = stochasticDp(states, acts, P, r, T);
    var brute = everyPolicy(states, acts, P, r, T, {});
    var agree = !brute.truncated && Requ(dp.V[0][0], brute.best[0]) && Requ(dp.V[0][1], brute.best[1]);

    /* the reconstructed policy, evaluated forwards -- "the table says 53/8" and
       "the plan the table describes is worth 53/8" are two claims */
    var policy = [];
    for (t = 0; t < T; t += 1) policy.push(dp.policy[t].slice());
    var achieves = true, got = [];
    for (i = 0; i < n; i += 1) {
      var v = evaluateForward(states, P, r, T, policy, i);
      got.push(v.value);
      if (!Requ(v.value, dp.V[0][i])) achieves = false;
    }

    var series = [];
    for (i = 0; i < n; i += 1) {
      var pts = [];
      for (t = T; t >= 0; t -= 1) pts.push([R(BigInt(T - t), 1n), dp.V[t][i]]);
      series.push({ name: states[i], tone: i ? 'purple' : 'cyan', points: pts });
    }
    plot.innerHTML = dpPlot(series, { width: 520, height: 230, zero: true,
      caption: 'periods left, against what the state is worth with that many to go' });

    var rows = '';
    for (t = T - 1; t >= 0; t -= 1) {
      for (i = 0; i < n; i += 1) {
        var d = dp.table[t][i], opts = [];
        for (a = 0; a < A; a += 1) {
          var o = d.options[a];
          opts.push((a === dp.policy[t][i] ? '<strong>' : '') + acts[a] + ': ' + Rtext(r[a][i]) + ' + '
                    + P[a][i].map(function (q, j) { return Rtext(q) + '·' + Rtext(dp.V[t + 1][j]); }).join(' + ')
                    + ' = ' + Rtext(o.value) + (a === dp.policy[t][i] ? '</strong>' : ''));
        }
        rows += tr([rowhead((T - t) + ' to go, ' + states[i]), td(Rtext(dp.V[t][i])),
                    td(tone(acts[dp.policy[t][i]], 'green')), tdl(opts.join(' &nbsp;|&nbsp; '))]);
      }
    }
    tableT.innerHTML = '<caption>The recursion, one column per period, filled from the end</caption>'
      + '<thead>' + tr([th('state, and how long is left'), th('its value'), th('best action'),
                        th('each action, priced')]) + '</thead><tbody>' + rows + '</tbody>';

    var prows = '';
    for (i = 0; i < n; i += 1) {
      prows += tr([rowhead('starting in ' + states[i]), td(Rtext(dp.V[0][i])),
                   td(Rtext(got[i])),
                   td(brute.truncated ? 'not enumerated' : Rtext(brute.best[i])),
                   td(Requ(got[i], dp.V[0][i]) && (brute.truncated || Requ(dp.V[0][i], brute.best[i]))
                      ? tone('all three agree', 'green') : tone('THEY DISAGREE', 'red'))],
                  Requ(got[i], dp.V[0][i]) ? 'tone-green' : 'tone-red');
    }
    var plan = [];
    for (t = 0; t < T; t += 1) {
      plan.push((T - t) + ' to go: ' + states.map(function (s, q) { return s + '→' + acts[policy[t][q]]; }).join(', '));
    }
    prows += tr([tdl('The policy itself: ' + plan.join(' &nbsp;|&nbsp; '), 'small-copy')
                 .replace('<td', '<td colspan="5"')]);
    polT.innerHTML = '<caption>Three routes to the same number</caption><thead>'
      + tr([th('start'), th('the recursion'), th('its own policy, pushed forwards'),
            th('the best of every policy'), th('verdict')]) + '</thead><tbody>' + prows + '</tbody>';

    document.getElementById('sdV1').textContent = Rtext(dp.V[0][0]);
    document.getElementById('sdB1').textContent = brute.truncated ? 'not enumerated' : Rtext(brute.best[0]);
    document.getElementById('sdV2').textContent = Rtext(dp.V[0][1]);
    document.getElementById('sdB2').textContent = brute.truncated ? 'not enumerated' : Rtext(brute.best[1]);
    document.getElementById('sdCount').textContent = brute.truncated ? brute.why : String(brute.count);
    document.getElementById('sdAchieves').textContent = achieves ? 'yes' : 'NO';

    if (!achieves || (!brute.truncated && !agree)) {
      status.innerHTML = '<strong>' + tone('These do not agree, so none of them is shown as an answer.', 'red')
        + '</strong> The table says ' + Rtext(dp.V[0][0]) + ' and ' + Rtext(dp.V[0][1])
        + ', the policy it describes is worth ' + got.map(Rtext).join(' and ')
        + (brute.truncated ? '' : ', and the best of every policy is ' + brute.best.map(Rtext).join(' and '))
        + '.';
      return;
    }
    var changes = [];
    for (i = 0; i < n; i += 1) {
      var first = dp.policy[T - 1][i], flipped = false;
      for (t = 0; t < T; t += 1) if (dp.policy[t][i] !== first) flipped = true;
      if (flipped) changes.push(states[i]);
    }
    status.innerHTML = '<strong>Three periods from the end, ' + states[0] + ' is worth '
      + tone(Rtext(dp.V[0][0]), 'cyan') + ' and ' + states[1] + ' '
      + tone(Rtext(dp.V[0][1]), 'purple') + '</strong> — exactly, as fractions, because an '
      + 'expectation of an expectation of an expectation is still a rational number. '
      + (brute.truncated ? brute.why + '. '
          : 'All ' + brute.count + ' deterministic policies were evaluated by pushing a distribution '
            + 'forward through each one, and none of them beats the table. ')
      + 'The policy the table describes was then pushed forward itself and came to the same number, '
      + 'which is the claim a value table does not make on its own. '
      + (changes.length
          ? 'Notice ' + tone(changes.join(' and '), 'amber') + ': the best action there is not the same '
            + 'with one period left as with ' + T + '. A policy in a finite horizon is a function of '
            + 'time as well as of state, and that is why the table has columns.'
          : 'The best action in each state is the same however long is left here, so the policy happens '
            + 'to be stationary — which is a fact about this instance and not a rule.');
  }

  function apply() {
    var p = SDP[presetIn.value];
    if (!p) return;
    statesIn.value = p.states; actsIn.value = p.acts; p0In.value = p.p0; p1In.value = p.p1;
    rIn.value = p.r; tIn.value = p.T;
    redraw();
  }
""" + _fill_js("SDP", [("statesIn", "states"), ("actsIn", "acts"), ("p0In", "p0"),
                       ("p1In", "p1"), ("rIn", "r")]) + r"""
  presetIn.addEventListener('change', apply);
  [statesIn, actsIn, p0In, p1In, rIn].forEach(function (el) { el.addEventListener('input', redraw); });
  tIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The stochastic recursion, and every policy there is",
        subtitle="A value table is a claim; the policy it describes, evaluated forwards, is the evidence",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fill the table backwards, then check it forwards"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every deterministic policy is evaluated by pushing a probability distribution forward "
            "through it, and the recursion's own policy is evaluated the same way, so the table's "
            "number has two independent witnesses.",
        ),
        script=script,
        expect={"sdPreset": _expect(_SD_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L6 -- tree: folding back, and what information is worth
# ---------------------------------------------------------------------------

_TR_PRESETS = [
    {
        "id": "build",
        "label": "build or wait, with a survey you could buy",
        "acts": "build wait",
        "states": "good poor",
        "payoff": "100 -20; 0 0",
        "prior": "3/10 7/10",
        "lik": "4/5 1/4; 1/5 3/4",
        "expect": {
            "trAct": "build",
            "trEvpi": "14",
            "trEvsi": "9/2",
        },
    },
    {
        "id": "three",
        "label": "three acts, three states",
        "acts": "small medium large",
        "states": "weak mid strong",
        "payoff": "20 20 20; 0 40 45; -30 20 80",
        "prior": "1/4 1/2 1/4",
        "lik": "7/10 1/5 1/10; 3/10 4/5 9/10",
        "expect": {
            "trAct": "medium",
            "trEvpi": "55/4",
            "trEvsi": "7/8",
        },
    },
    {
        "id": "useless",
        "label": "a signal that tells you nothing",
        "acts": "go stop",
        "states": "up down",
        "payoff": "60 -40; 0 0",
        "prior": "1/2 1/2",
        "lik": "1/2 1/2; 1/2 1/2",
        "expect": {
            "trEvsi": "0",
            "trEvpi": "20",
        },
    },
]


def _tree(cfg):
    chosen = _choose(cfg, "tree", _TR_PRESETS, "build")

    markup = (
        _toolbar(
            "Folding a decision tree back",
            "a chance node is an expectation and a decision node is a maximum, and the order matters",
            [("cyan", "the branch the fold chose"), ("purple", "what each node is worth"),
             ("green", "a payoff on the chosen path"), ("line-strong", "a branch not taken")],
        )
        + _stage(_svg("trTree", "0 0 660 320",
                      "The decision tree, with the value each node folds to and the branch chosen at "
                      "each decision drawn thick."))
        + _table("trPayoff")
        + _table("trValue")
        + _banner("trStatus")
    )
    controls = (
        _select("trPreset", "Worked example", _options(_TR_PRESETS), chosen["id"])
        + _text("trActs", "The acts", chosen["acts"])
        + _text("trStates", "The states of the world", chosen["states"])
        + _text("trPay", "What each act pays in each state, row per act", chosen["payoff"])
        + _text("trPrior", "How likely each state is", chosen["prior"])
        + _text("trLik", "The signal, row per signal: how likely it is in each state", chosen["lik"])
        + _select("trUse", "The tree to fold",
                  [("prior", "decide now, on the prior"), ("signal", "see the signal, then decide")],
                  "prior")
        + _kpis([
            ("Best act on the prior", "trAct"),
            ("What it is worth", "trPriorV"),
            ("With perfect information", "trPerfect"),
            ("EVPI", "trEvpi"),
            ("With the signal", "trWith"),
            ("EVSI", "trEvsi"),
        ])
        + _hint(
            "trHint",
            "EVPI is what you would pay to be told the state before deciding, and it is an upper "
            "bound on what any signal can be worth. EVSI is what this particular signal is worth, and "
            "it is computed from the joint distribution rather than from the shape of the tree &mdash; "
            "which is why a tree with no likelihood in it reports EVSI as nothing rather than as a "
            "number.",
        )
    )

    script = _MODE_JS["tree"] + r"""
""" + _presets_js("TRP", _TR_PRESETS, ["acts", "states", "payoff", "prior", "lik"]) + r"""
  var presetIn = document.getElementById('trPreset');
  var actsIn = document.getElementById('trActs'), statesIn = document.getElementById('trStates');
  var payIn = document.getElementById('trPay'), priorIn = document.getElementById('trPrior');
  var likIn = document.getElementById('trLik'), useIn = document.getElementById('trUse');
  var treeSvg = document.getElementById('trTree');
  var payT = document.getElementById('trPayoff'), valT = document.getElementById('trValue');
  var status = document.getElementById('trStatus');
  var KPIS = ['trAct', 'trPriorV', 'trPerfect', 'trEvpi', 'trWith', 'trEvsi'];

  function blank(why) {
    treeSvg.innerHTML = ''; payT.innerHTML = ''; valT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> The payoff table has one row per '
      + 'act and one column per state, rows separated by semicolons.';
  }

  function nameRow(text) {
    return String(text).split(/[\s,;]+/).filter(function (t) { return t.length; });
  }

  function redraw() {
    var acts = nameRow(actsIn.value), states = nameRow(statesIn.value), i, s, a, g;
    if (acts.length < 2 || acts.length > 4) { blank('this lab folds between two and four acts'); return; }
    if (states.length < 2 || states.length > 4) { blank('this lab folds between two and four states'); return; }
    var pm = parseMatrixRows(payIn.value, acts.length, states.length);
    if (pm.bad) { blank('the payoff table: ' + pm.bad); return; }
    var prior = parseRow(priorIn.value);
    if (prior === null || prior.length !== states.length) {
      blank('the prior needs one probability for each of the ' + states.length + ' states'); return;
    }
    var total = R0;
    for (s = 0; s < prior.length; s += 1) {
      if (Rsign(prior[s]) < 0) { blank('a prior probability is negative'); return; }
      total = Radd(total, prior[s]);
    }
    if (!Requ(total, R1)) { blank('the prior adds to ' + Rtext(total) + ' rather than 1'); return; }
    var lik = null, useSignal = useIn.value === 'signal';
    if (String(likIn.value).trim()) {
      var lm = parseMatrixRows(likIn.value, null, states.length);
      if (lm.bad) { blank('the signal table: ' + lm.bad); return; }
      lik = lm.rows;
      for (g = 0; g < states.length; g += 1) {
        var col = R0;
        for (i = 0; i < lik.length; i += 1) col = Radd(col, lik[i][g]);
        if (!Requ(col, R1)) {
          blank('in state ' + states[g] + ' the signal probabilities add to ' + Rtext(col)
                + ' rather than 1 — a column of a likelihood is a distribution over what you might see');
          return;
        }
      }
    }
    if (useSignal && !lik) { blank('there is no signal table to fold, so there is nothing to see first'); return; }
    var signals = [];
    if (lik) for (i = 0; i < lik.length; i += 1) signals.push('G' + (i + 1));

    var tree = useSignal ? signalTree(pm.rows, prior, lik, acts, states, signals)
                         : priorTree(pm.rows, prior, acts, states);
    if (lik) tree.likelihood = lik;
    var folded = annotate(foldBack(tree));
    var oracle = everyStrategy(pm.rows, prior, useSignal ? lik : null);
    var agree = Requ(folded.value, oracle.best);

    treeSvg.innerHTML = dpTree(folded, { width: 660, height: 320,
      caption: useSignal ? 'the signal comes first, and the decision is taken inside each branch of it'
                         : 'one decision, and a chance node under each act' });

    var rows = '';
    for (a = 0; a < acts.length; a += 1) {
      var cells = [rowhead(acts[a])], ev = R0;
      for (s = 0; s < states.length; s += 1) {
        cells.push(td(Rtext(pm.rows[a][s])));
        ev = Radd(ev, Rmul(prior[s], pm.rows[a][s]));
      }
      cells.push(td(Rtext(ev)));
      rows += tr(cells, Requ(ev, folded.prior) ? 'tone-green' : null);
    }
    var head = [th('act')];
    for (s = 0; s < states.length; s += 1) head.push(th(states[s] + ' (' + Rtext(prior[s]) + ')'));
    head.push(th('on the prior'));
    payT.innerHTML = '<caption>The payoff table, and what each act is worth before anything is seen</caption>'
      + '<thead>' + tr(head) + '</thead><tbody>' + rows + '</tbody>';

    var vrows = '';
    vrows += tr([rowhead('decide now'), td(Rtext(folded.prior)),
                 tdl('the best act under the prior, which is what the first tree folds to')]);
    vrows += tr([rowhead('know the state first'), td(Rtext(folded.perfect)),
                 tdl('the best act in each state, weighted by how likely the state is')]);
    vrows += tr([rowhead('EVPI'), td(tone(Rtext(folded.evpi), 'purple')),
                 tdl('the difference, and an upper bound on what any signal can be worth')], 'tone-purple');
    if (folded.evsi !== null) {
      vrows += tr([rowhead('see the signal first'),
                   td(Rtext(Radd(folded.prior, folded.evsi))),
                   tdl('decide separately after each signal, weighted by how likely the signal is')]);
      vrows += tr([rowhead('EVSI'), td(tone(Rtext(folded.evsi), 'cyan')),
                   tdl('what this signal is worth — never more than EVPI, and here '
                       + (Rzero(folded.evsi) ? 'nothing at all' : Rtext(folded.evsi)))], 'tone-cyan');
    } else {
      vrows += tr([rowhead('EVSI'), td(tone('not computed', 'muted')),
                   tdl('there is no likelihood here, and the shape of a tree cannot be made to '
                       + 'produce one')]);
    }
    vrows += tr([rowhead('every strategy, enumerated'), td(Rtext(oracle.best)),
                 tdl(oracle.count + ' way' + plural(oracle.count, '', 's') + ' to map what you see to '
                     + 'what you do, each priced straight from the joint distribution')],
                agree ? 'tone-green' : 'tone-red');
    valT.innerHTML = '<caption>What each kind of knowing is worth</caption><thead>'
      + tr([th('what you know when you decide'), th('worth'), th('how it is computed')])
      + '</thead><tbody>' + vrows + '</tbody>';

    var bestAct = folded.root.choiceLabel;
    document.getElementById('trAct').textContent = useSignal
      ? 'depends on the signal' : (bestAct || '—');
    document.getElementById('trPriorV').textContent = Rtext(folded.prior);
    document.getElementById('trPerfect').textContent = Rtext(folded.perfect);
    document.getElementById('trEvpi').textContent = Rtext(folded.evpi);
    document.getElementById('trWith').textContent = folded.evsi === null ? '—'
      : Rtext(Radd(folded.prior, folded.evsi));
    document.getElementById('trEvsi').textContent = folded.evsi === null ? 'no likelihood given'
      : Rtext(folded.evsi);

    if (!agree) {
      status.innerHTML = '<strong>' + tone('The fold and the enumeration disagree.', 'red')
        + '</strong> The tree folds to ' + Rtext(folded.value) + ' and the best of the '
        + oracle.count + ' strategies is worth ' + Rtext(oracle.best) + '.';
      return;
    }
    status.innerHTML = '<strong>This tree folds to ' + tone(Rtext(folded.value), 'green') + '</strong>'
      + (useSignal
          ? ', and the strategy it describes was checked against all ' + oracle.count
            + ' ways of mapping a signal to an act — each priced from the joint distribution with no '
            + 'tree involved. '
          : ' — the best act under the prior is ' + tone(bestAct, 'green') + ', worth '
            + Rtext(folded.prior) + '. ')
      + 'Knowing the state before deciding would be worth ' + tone(Rtext(folded.perfect), 'purple')
      + ', so perfect information is worth ' + tone(Rtext(folded.evpi), 'purple') + '. '
      + (folded.evsi === null
          ? 'This tree carries no likelihood, so EVSI is reported as absent rather than guessed from '
            + 'the shape of the branches.'
          : (Rzero(folded.evsi)
              ? tone('This signal is worth nothing at all', 'red') + ': its probabilities are the same '
                + 'in every state, so seeing it leaves the posterior equal to the prior and no '
                + 'decision changes. A signal has to DISCRIMINATE to be worth anything, and being '
                + 'informative-looking is not the same thing.'
              : 'This signal is worth ' + tone(Rtext(folded.evsi), 'cyan') + ', which is '
                + Rtext(Rdiv(folded.evsi, folded.evpi)) + ' of EVPI — less than perfect information, '
                + 'as it must be, because it is a noisy view of the same state.'));
  }

  function apply() {
    var p = TRP[presetIn.value];
    if (!p) return;
    actsIn.value = p.acts; statesIn.value = p.states; payIn.value = p.payoff;
    priorIn.value = p.prior; likIn.value = p.lik;
    redraw();
  }
""" + _fill_js("TRP", [("actsIn", "acts"), ("statesIn", "states"), ("payIn", "payoff"),
                       ("priorIn", "prior"), ("likIn", "lik")]) + r"""
  presetIn.addEventListener('change', apply);
  useIn.addEventListener('change', redraw);
  [actsIn, statesIn, payIn, priorIn, likIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Folding a decision tree back",
        subtitle="EVPI bounds what any signal can be worth; EVSI says what this one is worth",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fold the tree, then price every strategy it could have chosen"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tree is built from the payoff table rather than typed, folded back node by node, and "
            "checked against every mapping from what you see to what you do.",
        ),
        script=script,
        expect={"trPreset": _expect(_TR_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L7 -- stopping: the threshold, and every rule it is competing with
# ---------------------------------------------------------------------------

_SP_PRESETS = [
    {
        "id": "three",
        "label": "three offers, equally likely, and a cost to carry on",
        "pmf": "10:1/3, 20:1/3, 30:1/3",
        "T": "3",
        "c": "1",
        "expect": {
            "spValue": "71/3",
            "spShape": "yes",
            "spLast": "0",
        },
    },
    {
        "id": "skew",
        "label": "a rare high offer",
        "pmf": "8:3/5, 14:3/10, 40:1/10",
        "T": "4",
        "c": "1",
        "expect": {
            "spValue": "4341/250",
            "spCount": "4096",
        },
    },
    {
        "id": "costly",
        "label": "searching is expensive",
        "pmf": "10:1/2, 30:1/2",
        "T": "4",
        "c": "5",
        "expect": {
            "spValue": "155/8",
            "spCount": "256",
        },
    },
]


def _stopping(cfg):
    chosen = _choose(cfg, "stopping", _SP_PRESETS, "three")

    markup = (
        _toolbar(
            "When to stop looking",
            "the threshold is what carrying on is worth, and it falls as the chances run out",
            [("cyan", "the threshold"), ("green", "an offer this period would accept"),
             ("purple", "the best rule of any shape"), ("amber", "the cost of one more look")],
        )
        + _stage(_svg("spPlot", "0 0 520 230",
                      "The threshold against how many periods are left."))
        + _table("spRows")
        + _table("spRules")
        + _banner("spStatus")
    )
    controls = (
        _select("spPreset", "Worked example", _options(_SP_PRESETS), chosen["id"])
        + _text("spPmf", "The offers, as value:probability", chosen["pmf"])
        + _range("spT", "Periods you have", 1, 4, int(chosen["T"]))
        + _range("spC", "What one more look costs", 0, 6, int(chosen["c"]))
        + _kpis([
            ("The whole search is worth", "spValue"),
            ("The best rule of any shape", "spBest"),
            ("Do the two agree?", "spAgree"),
            ("Accept-sets there are", "spCount"),
            ("Is the best rule a threshold?", "spShape"),
            ("The threshold with one period left", "spLast"),
        ])
        + _hint(
            "spHint",
            "That the best rule is a threshold is a claim about its SHAPE, and it is usually asserted. "
            "Here it is measured: every way of choosing which offers to accept in each period is "
            "enumerated and evaluated, and the winner is then tested for whether accepting an offer "
            "implies accepting every larger one.",
        )
    )

    script = _MODE_JS["stopping"] + r"""
""" + _presets_js("SPP", _SP_PRESETS, ["pmf", "T", "c"]) + r"""
  var presetIn = document.getElementById('spPreset'), pmfIn = document.getElementById('spPmf');
  var tIn = document.getElementById('spT'), cIn = document.getElementById('spC');
  var plot = document.getElementById('spPlot');
  var rowsT = document.getElementById('spRows'), rulesT = document.getElementById('spRules');
  var status = document.getElementById('spStatus');
  var KPIS = ['spValue', 'spBest', 'spAgree', 'spCount', 'spShape', 'spLast'];

  function blank(why) {
    plot.innerHTML = ''; rowsT.innerHTML = ''; rulesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An offer is a value, a colon and a '
      + 'probability, and the probabilities have to add to 1.';
  }

  function redraw() {
    var pp = parsePmf(pmfIn.value);
    if (pp.bad) { blank(pp.bad); return; }
    var pmf = pp.pmf, i, k, t;
    if (pmf.length > 4) { blank('that is ' + pmf.length + ' offers, and this lab enumerates at most 4'); return; }
    var T = Math.max(1, Math.min(4, Math.round(+tIn.value)));
    var c = R(BigInt(Math.round(+cIn.value)), 1n);
    document.getElementById('spTOut').textContent = String(T);
    document.getElementById('spCOut').textContent = Rtext(c);

    var st = stopThresholds(pmf, T, c);
    var sets = thresholdSets(pmf, st.rows);
    var mine = ruleValue(pmf, sets, c);
    var brute = everyStoppingRule(pmf, T, c);
    var agree = !brute.truncated && Requ(st.value, brute.best);
    if (!Requ(mine, st.value)) {
      blank('the accept-sets the thresholds describe are worth ' + Rtext(mine)
            + ' and the recursion says ' + Rtext(st.value));
      return;
    }

    plot.innerHTML = dpPlot([{ name: 'threshold', tone: 'cyan',
        points: st.rows.map(function (q) { return [R(BigInt(q.left), 1n), q.threshold]; }) },
      { name: 'worth carrying on', tone: 'purple', dash: true,
        points: st.rows.map(function (q) { return [R(BigInt(q.left), 1n), q.continuation]; }) }],
      { width: 520, height: 230, zero: true,
        caption: 'periods left, against the offer you would need to see to stop' });

    var rows = '';
    for (i = 0; i < st.rows.length; i += 1) {
      var r = st.rows[i];
      rows += tr([rowhead(r.left + ' left'), td(Rtext(r.threshold)),
                  td(r.accept.length ? r.accept.map(Rtext).join(', ') : 'nothing'),
                  td(Rtext(r.continuation)), tdl(r.why)]);
    }
    rowsT.innerHTML = '<caption>The threshold, period by period</caption><thead>'
      + tr([th('periods left'), th('accept above'), th('which offers that is'),
            th('worth carrying on'), th('why')]) + '</thead><tbody>' + rows + '</tbody>';

    var srows = '';
    var describe = function (ss) {
      var out = [];
      for (t = ss.length - 1; t >= 0; t -= 1) {
        var take = [];
        for (k = 0; k < pmf.length; k += 1) if (ss[t][k]) take.push(Rtext(pmf[k][0]));
        out.push((t + 1) + ' left: ' + (take.length ? take.join(' ') : 'nothing'));
      }
      return out.join(' &nbsp;|&nbsp; ');
    };
    srows += tr([rowhead('the threshold rule'), td(Rtext(mine)), tdl(describe(sets))], 'tone-cyan');
    if (!brute.truncated) {
      srows += tr([rowhead('the best of every accept-set'), td(Rtext(brute.best)),
                   tdl(describe(brute.sets))], 'tone-purple');
      srows += tr([rowhead('is that a threshold rule?'),
                   td(brute.threshold ? tone('yes', 'green') : tone('no', 'red')),
                   tdl(brute.threshold
                       ? 'accepting an offer implies accepting every larger one, in every period — '
                         + 'which is the shape the recursion assumed, measured rather than asserted'
                       : 'the best rule accepts an offer and rejects a larger one, which would make '
                         + 'the threshold form wrong here')],
                  brute.threshold ? 'tone-green' : 'tone-red');
    } else {
      srows += tr([rowhead('every accept-set'), td('not enumerated'), tdl(brute.why)]);
    }
    rulesT.innerHTML = '<caption>The rule the recursion found, against every rule there is</caption>'
      + '<thead>' + tr([th('rule'), th('worth'), th('what it does')]) + '</thead>'
      + '<tbody>' + srows + '</tbody>';

    document.getElementById('spValue').textContent = Rtext(st.value);
    document.getElementById('spBest').textContent = brute.truncated ? 'not enumerated' : Rtext(brute.best);
    document.getElementById('spAgree').textContent = brute.truncated ? 'not checked' : (agree ? 'yes' : 'NO');
    document.getElementById('spCount').textContent = brute.truncated ? brute.why : String(brute.count);
    document.getElementById('spShape').textContent = brute.truncated ? 'not checked'
      : (brute.threshold ? 'yes' : 'NO');
    document.getElementById('spLast').textContent = Rtext(st.rows[st.rows.length - 1].threshold);

    if (!brute.truncated && !agree) {
      status.innerHTML = '<strong>' + tone('The recursion is beaten by a rule it did not consider.', 'red')
        + '</strong> It reaches ' + Rtext(st.value) + ' and the best accept-set is worth '
        + Rtext(brute.best) + '.';
      return;
    }
    var falls = Rcmp(st.rows[0].threshold, st.rows[st.rows.length - 1].threshold) > 0;
    status.innerHTML = '<strong>The whole search is worth ' + tone(Rtext(st.value), 'green')
      + '</strong> with ' + T + ' period' + plural(T, '', 's') + ' and a look costing ' + Rtext(c)
      + '. The threshold ' + (falls ? tone('falls', 'cyan') + ' as the deadline nears — '
          + st.rows.map(function (q) { return Rtext(q.threshold); }).join(', then ')
          + ' — because there is less left to wait for'
        : 'does not fall here, which is worth looking at: with a cost this high, carrying on is worth '
          + 'so little that the rule barely changes')
      + '. With one period left the threshold is '
      + tone(Rtext(st.rows[st.rows.length - 1].threshold), 'cyan')
      + ', so any offer at all is taken — there is nothing to carry on to. '
      + (brute.truncated ? brute.why + '. '
          : 'All ' + brute.count + ' ways of choosing which offers to accept in which period were '
            + 'evaluated, and the threshold rule is the best of them. '
            + (brute.threshold
                ? 'The winner is a threshold rule, which the recursion assumed and this measured.'
                : tone('The winner is NOT a threshold rule, which would break the recursion.', 'red')));
  }

  function apply() {
    var p = SPP[presetIn.value];
    if (!p) return;
    pmfIn.value = p.pmf; tIn.value = p.T; cIn.value = p.c;
    redraw();
  }
""" + _fill_js("SPP", [("pmfIn", "pmf")]) + r"""
  presetIn.addEventListener('change', apply);
  pmfIn.addEventListener('input', redraw);
  tIn.addEventListener('input', redraw);
  cIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="When to stop looking",
        subtitle="The threshold is the value of carrying on, and its shape is measured rather than assumed",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the offers and the search cost, and watch the rule change"),
        panel_intro=cfg.get(
            "panel_intro",
            "The recursion gives a threshold per period; every possible accept-set in every period is "
            "then enumerated and evaluated, so the claim that the best rule is a threshold is a "
            "measurement.",
        ),
        script=script,
        expect={"spPreset": _expect(_SP_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L8 -- secretary: the exact table, and the rule played out on every ordering
# ---------------------------------------------------------------------------

_SE_PRESETS = [
    {
        "id": "small",
        "label": "four candidates, small enough to count by hand",
        "n": "4",
        "expect": {
            "seBestR": "1",
            "seBestP": "11/24",
            "seWalked": "24",
        },
    },
    {
        "id": "seven",
        "label": "seven, the largest this page enumerates",
        "n": "7",
        "expect": {
            "seBestR": "2",
            "seBestP": "29/70",
            "seWalked": "5040",
        },
    },
    {
        "id": "hundred",
        "label": "sixty, where the limit starts to look like the answer",
        "n": "100",
        # THIS PRESET ASKS FOR 100 AND THE PAGE RENDERS 60. The control below is a range
        # 3..60 and redraw() clamps to it, so the figures pinned here are n = 60's:
        # reject 22, win with probability 0.373210, against a limit of 60/e. At the n =
        # 100 this preset names they would be 37 and 0.371043. Raise the cap rather than
        # retuning the strings -- and when it is raised, these three expectations fail
        # and point here.
        "expect": {
            "seBestR": "22",
            "seBestP": "0.373210",
            "seLimit": "22.0728 — rounded",
        },
    },
]


def _secretary(cfg):
    chosen = _choose(cfg, "secretary", _SE_PRESETS, "small")

    markup = (
        _toolbar(
            "Look, then leap",
            "reject the first r − 1 whatever they are, then take the first one better than all of them",
            [("cyan", "the chance of success at each r"), ("purple", "the best r"),
             ("green", "the same figure, counted over every ordering"), ("amber", "the n/e limit")],
        )
        + _stage(_svg("sePlot", "0 0 520 240",
                      "The probability of ending with the best candidate, against how many are rejected first."))
        + _table("seTable")
        + _table("seCheck")
        + _banner("seStatus")
    )
    controls = (
        _select("sePreset", "Worked example", _options(_SE_PRESETS), chosen["id"])
        + _range("seN", "Candidates", 3, 60, int(chosen["n"]))
        + _kpis([
            ("Reject this many first", "seBestR"),
            ("Then you win with probability", "seBestP"),
            ("As a decimal", "seBestD"),
            ("n / e, rounded", "seLimit"),
            ("Orderings walked as a check", "seWalked"),
            ("Does the closed form match?", "seAgree"),
        ])
        + _hint(
            "seHint",
            "The exact probability is `((r−1)/n) · Σ 1/(i−1)` over `i` from `r` to `n`, and every "
            "entry below is that fraction rather than a decimal. The `n/e` a textbook quotes is the "
            "LIMIT of the best `r`, not the answer &mdash; it is printed here rounded and labelled, "
            "beside the exact table that never needs it.",
        )
    )

    script = _MODE_JS["secretary"] + r"""
""" + _presets_js("SEP", _SE_PRESETS, ["n"]) + r"""
  var presetIn = document.getElementById('sePreset'), nIn = document.getElementById('seN');
  var plot = document.getElementById('sePlot');
  var tableT = document.getElementById('seTable'), checkT = document.getElementById('seCheck');
  var status = document.getElementById('seStatus');

  function redraw() {
    var n = Math.max(3, Math.min(60, Math.round(+nIn.value))), i;
    document.getElementById('seNOut').textContent = String(n);
    var ex = secretaryExact(n);
    var brute = secretaryBrute(n, 7);
    var agree = true, mismatch = null;
    if (!brute.truncated) {
      for (i = 0; i < ex.probs.length; i += 1) {
        if (!Requ(ex.probs[i].p, brute.probs[i].p)) { agree = false; mismatch = ex.probs[i].r; }
      }
    }
    var limit = Rmul(R(BigInt(n), 1n), invE());

    plot.innerHTML = dpPlot([
      { name: 'exact P(r)', tone: 'cyan',
        points: ex.probs.map(function (q) { return [R(BigInt(q.r), 1n), q.p]; }),
        mark: function (k) { return ex.probs[k].r === ex.best; } }
    ].concat(brute.truncated ? [] : [{ name: 'counted over every ordering', tone: 'green', dash: true,
        dots: false, points: brute.probs.map(function (q) { return [R(BigInt(q.r), 1n), q.p]; }) }]),
      { width: 520, height: 240, zero: true,
        caption: 'how many to reject first, against the chance of ending with the best' });

    var rows = '', step = Math.max(1, Math.ceil(n / 14));
    for (i = 0; i < ex.probs.length; i += 1) {
      var q = ex.probs[i];
      if (q.r !== ex.best && (q.r - 1) % step !== 0 && q.r !== n) continue;
      rows += tr([rowhead('r = ' + q.r), td(Rshort(q.p, 6, 20)), td(Rfixed(q.p, 6)),
                  td(q.r === ex.best ? tone('the best r', 'purple') : '')],
                 q.r === ex.best ? 'tone-purple' : null);
    }
    tableT.innerHTML = '<caption>The chance of success, exactly, for each number rejected first'
      + (step > 1 ? ' (every ' + step + 'th row, and the best)' : '') + '</caption><thead>'
      + tr([th('r'), th('P(r), exactly'), th('as a decimal'), th('')]) + '</thead>'
      + '<tbody>' + rows + '</tbody>';

    var crows = '';
    if (brute.truncated) {
      crows += tr([tdl('At n = ' + n + ' there are too many orderings to walk, so the table above is '
        + 'the closed form alone. Drop to 7 or fewer and every entry is checked by counting.',
        'small-copy').replace('<td', '<td colspan="4"')]);
    } else {
      for (i = 0; i < ex.probs.length; i += 1) {
        crows += tr([rowhead('r = ' + ex.probs[i].r), td(Rshort(ex.probs[i].p, 6, 20)),
                     td(brute.counts[ex.probs[i].r] + ' of ' + brute.total),
                     td(Requ(ex.probs[i].p, brute.probs[i].p) ? tone('the same', 'green')
                        : tone('DIFFERENT', 'red'))],
                    Requ(ex.probs[i].p, brute.probs[i].p) ? null : 'tone-red');
      }
    }
    checkT.innerHTML = '<caption>The closed form against the count'
      + (brute.truncated ? '' : ', over all ' + brute.total + ' orderings') + '</caption><thead>'
      + tr([th('r'), th('the harmonic sum'), th('orderings it wins'), th('verdict')]) + '</thead>'
      + '<tbody>' + crows + '</tbody>';

    document.getElementById('seBestR').textContent = String(ex.best - 1);
    document.getElementById('seBestP').textContent = Rshort(ex.bestP, 6, 20);
    document.getElementById('seBestD').textContent = Rfixed(ex.bestP, 6);
    document.getElementById('seLimit').textContent = Rfixed(limit, 4) + ' — rounded';
    document.getElementById('seWalked').textContent = brute.truncated ? 'none — too many' : String(brute.total);
    document.getElementById('seAgree').textContent = brute.truncated ? 'not checked' : (agree ? 'yes' : 'NO');

    if (!agree) {
      status.innerHTML = '<strong>' + tone('The closed form and the count disagree at r = ' + mismatch
        + '.', 'red') + '</strong> Neither is shown as an answer.';
      return;
    }
    status.innerHTML = '<strong>Reject the first ' + tone(String(ex.best - 1), 'purple')
      + ' and then take the first one better than all of them.</strong> That wins with probability '
      + tone(Rshort(ex.bestP, 6, 20), 'purple') + ', which is ' + Rfixed(ex.bestP, 6)
      + ' — an exact fraction, printed as a decimal once it runs past twenty digits, '
      + 'not a simulation. '
      + (brute.truncated
          ? 'At n = ' + n + ' there are too many orderings to walk; drop to seven or fewer and every '
            + 'entry of the table above is checked by playing the rule out on all of them. '
          : 'Every entry was checked by playing the rule out on all ' + brute.total
            + ' orderings and counting the wins, which shares no arithmetic with the harmonic sum. ')
      + 'The <span class="tone-amber">n/e</span> a textbook quotes is ' + Rfixed(limit, 4)
      + ' here, and it is the LIMIT of the best r rather than the answer: at n = ' + n
      + ' the best r is ' + ex.best + ', and 1/e is irrational so that figure is rounded and this is '
      + 'the only rounded number on the page.';
  }

  function apply() {
    var p = SEP[presetIn.value];
    if (!p) return;
    nIn.value = p.n;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  nIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Look, then leap",
        subtitle="An exact harmonic sum, checked by playing the rule out on every ordering",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose how many to reject, and see what it costs you"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every probability here is an exact fraction, and for seven candidates or fewer each one "
            "is checked by walking all n! orderings and counting.",
        ),
        script=script,
        expect={"sePreset": _expect(_SE_PRESETS)},
    )


# ---------------------------------------------------------------------------
# L9 -- discount: value iteration, and the fixed point it is approaching
# ---------------------------------------------------------------------------

_DC_PRESETS = [
    {
        "id": "two",
        "label": "two states, and a discount of a half",
        "P": "1/2 1/2; 1/4 3/4",
        "r": "1 3",
        "gamma": "1/2",
        "expect": {
            "dcV1": "22/7",
            "dcV2": "38/7",
            "dcIterV": "3.14171782",
        },
    },
    {
        "id": "patient",
        "label": "a discount of nine tenths",
        "P": "1/2 1/2; 1/4 3/4",
        "r": "1 3",
        "gamma": "9/10",
        "expect": {
            "dcV1": "670/31",
            "dcV2": "750/31",
        },
    },
    {
        "id": "three",
        "label": "three states",
        "P": "1/2 1/4 1/4; 0 2/3 1/3; 1/5 1/5 3/5",
        "r": "2 0 5",
        "gamma": "3/4",
        "expect": {
            "dcV1": "1508/163",
            "dcV2": "1096/163",
        },
    },
]


def _discount(cfg):
    chosen = _choose(cfg, "discount", _DC_PRESETS, "two")

    markup = (
        _toolbar(
            "Value iteration, and the fixed point under it",
            "the iteration approaches the answer; row reduction lands on it",
            [("cyan", "the first state"), ("purple", "the second"),
             ("green", "the exact fixed point"), ("amber", "the gap still left")],
        )
        + _stage(_svg("dcPlot", "0 0 520 240",
                      "Each state's value at each iteration, against the exact fixed point."))
        + _table("dcIter")
        + _table("dcFixed")
        + _banner("dcStatus")
    )
    controls = (
        _select("dcPreset", "Worked example", _options(_DC_PRESETS), chosen["id"])
        + _text("dcP", "Where each state goes, row per state", chosen["P"])
        + _text("dcR", "What each state pays", chosen["r"])
        + _select("dcG", "The discount",
                  [("1/2", "a half"), ("2/3", "two thirds"), ("3/4", "three quarters"),
                   ("9/10", "nine tenths"), ("99/100", "ninety-nine hundredths")], chosen["gamma"])
        + _range("dcT", "Iterations", 1, 24, 12)
        + _kpis([
            ("The fixed point, state 1", "dcV1"),
            ("The fixed point, state 2", "dcV2"),
            ("After the iterations shown", "dcIterV"),
            ("The gap still left", "dcGap"),
            ("Does r + gPv = v exactly?", "dcResidual"),
            ("Digits in the last denominator", "dcDigits"),
        ])
        + _hint(
            "dcHint",
            "`v = r + gPv` is a linear system, so it has an exact solution and row reduction finds "
            "it: `(I − gP)v = r`. Value iteration is the other way round &mdash; start at zero and "
            "apply the map &mdash; and it never arrives, which is visible in the denominators: each "
            "step multiplies by one more power of the discount's denominator.",
        )
    )

    script = _MODE_JS["discount"] + r"""
""" + _presets_js("DCP", _DC_PRESETS, ["P", "r", "gamma"]) + r"""
  var presetIn = document.getElementById('dcPreset'), pIn = document.getElementById('dcP');
  var rIn = document.getElementById('dcR'), gIn = document.getElementById('dcG');
  var tIn = document.getElementById('dcT');
  var plot = document.getElementById('dcPlot');
  var iterT = document.getElementById('dcIter'), fixT = document.getElementById('dcFixed');
  var status = document.getElementById('dcStatus');
  var KPIS = ['dcV1', 'dcV2', 'dcIterV', 'dcGap', 'dcResidual', 'dcDigits'];

  function blank(why) {
    plot.innerHTML = ''; iterT.innerHTML = ''; fixT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Each row of the transition table '
      + 'says where one state goes, and it has to add to 1.';
  }

  function redraw() {
    var pm = parseMatrixRows(pIn.value, null, null);
    if (pm.bad) { blank(pm.bad); return; }
    var P = pm.rows, n = P.length, i, j, k;
    if (n < 2 || n > 4) { blank('this lab takes between two and four states'); return; }
    for (i = 0; i < n; i += 1) {
      if (P[i].length !== n) { blank('row ' + (i + 1) + ' has ' + P[i].length + ' entries and there are ' + n + ' states'); return; }
      var total = R0;
      for (j = 0; j < n; j += 1) {
        if (Rsign(P[i][j]) < 0) { blank('row ' + (i + 1) + ' has a negative probability in it'); return; }
        total = Radd(total, P[i][j]);
      }
      if (!Requ(total, R1)) { blank('row ' + (i + 1) + ' adds to ' + Rtext(total) + ' rather than 1'); return; }
    }
    var r = parseRow(rIn.value);
    if (r === null || r.length !== n) { blank('there needs to be one reward for each of the ' + n + ' states'); return; }
    var gamma = Rread(gIn.value);
    if (gamma === null) { blank('that is not a discount'); return; }
    var T = Math.max(1, Math.min(24, Math.round(+tIn.value)));
    document.getElementById('dcTOut').textContent = String(T);

    var dv = discountedValue(P, r, gamma, T);
    if (dv.singular) { blank('I − gP is singular at this discount, so there is no fixed point to find'); return; }

    /* the residual: the fixed point put back into the equation it solves */
    var residual = [], exact = true;
    for (i = 0; i < n; i += 1) {
      var s = r[i];
      for (j = 0; j < n; j += 1) s = Radd(s, Rmul(gamma, Rmul(P[i][j], dv.v[j])));
      var res = Rsub(s, dv.v[i]);
      residual.push(res);
      if (!Rzero(res)) exact = false;
    }

    var series = [], tones = ['cyan', 'purple', 'blue', 'amber'];
    for (i = 0; i < n; i += 1) {
      series.push({ name: 'state ' + (i + 1), tone: tones[i % tones.length],
                    points: dv.iterations.map(function (v, q) { return [R(BigInt(q), 1n), v[i]]; }) });
      series.push({ name: '', tone: 'green', dash: true, dots: false,
                    points: [[R0, dv.v[i]], [R(BigInt(T), 1n), dv.v[i]]] });
    }
    plot.innerHTML = dpPlot(series, { width: 520, height: 240, zero: true,
      caption: 'iterations, against the value of each state — the dashed lines are the fixed point' });

    var rows = '', step = Math.max(1, Math.ceil(T / 10));
    for (k = 0; k <= T; k += 1) {
      if (k % step !== 0 && k !== T) continue;
      var cells = [rowhead('v' + k)];
      for (i = 0; i < n; i += 1) cells.push(td(Rshort(dv.iterations[k][i], 6, 12)));
      cells.push(td(String(String(dv.iterations[k][0].d).length)));
      var gapHere = Rsub(dv.iterations[k][0], dv.v[0]);
      cells.push(td(Rzero(gapHere) ? tone('exactly there', 'green') : Rfixed(Rabs(gapHere), 8)));
      rows += tr(cells, k === T ? 'tone-cyan' : null);
    }
    var head = [th('iteration')];
    for (i = 0; i < n; i += 1) head.push(th('state ' + (i + 1)));
    head.push(th('digits in the denominator'));
    head.push(th('gap at state 1'));
    iterT.innerHTML = '<caption>Value iteration from zero, and what it costs to carry the exact value</caption>'
      + '<thead>' + tr(head) + '</thead><tbody>' + rows + '</tbody>';

    var frows = '';
    for (i = 0; i < n; i += 1) {
      var eq = [];
      for (j = 0; j < n; j += 1) {
        eq.push(Rtext(Rsub(i === j ? R1 : R0, Rmul(gamma, P[i][j]))) + '·v' + (j + 1));
      }
      frows += tr([rowhead('state ' + (i + 1)), tdl(eq.join(' + ') + ' = ' + Rtext(r[i])),
                   td(Rtext(dv.v[i])), td(Rfixed(dv.v[i], 6)),
                   td(Rzero(residual[i]) ? tone('0', 'green') : tone(Rtext(residual[i]), 'red'))],
                  Rzero(residual[i]) ? null : 'tone-red');
    }
    fixT.innerHTML = '<caption>(I − gP)v = r, solved by row reduction in ' + dv.ops.length
      + ' operations</caption><thead>'
      + tr([th('row'), th('the equation'), th('v, exactly'), th('as a decimal'),
            th('r + gPv − v')]) + '</thead><tbody>' + frows + '</tbody>';

    document.getElementById('dcV1').textContent = Rtext(dv.v[0]);
    document.getElementById('dcV2').textContent = Rtext(dv.v[1]);
    document.getElementById('dcIterV').textContent = Rfixed(dv.vT[0], 8);
    document.getElementById('dcGap').textContent = Rzero(dv.gap[0]) ? '0 — exactly there'
      : Rfixed(Rabs(dv.gap[0]), 10);
    document.getElementById('dcResidual').textContent = exact ? 'yes — every entry is exactly zero' : 'NO';
    document.getElementById('dcDigits').textContent = String(String(dv.iterations[T][0].d).length)
      + ' (it started at ' + String(dv.iterations[0][0].d).length + ')';

    if (!exact) {
      status.innerHTML = '<strong>' + tone('The fixed point does not satisfy its own equation.', 'red')
        + '</strong> r + gPv − v comes to ' + residual.map(Rtext).join(', ')
        + ' rather than zero, so nothing here is an answer.';
      return;
    }
    var grew = String(dv.iterations[T][0].d).length - String(dv.iterations[0][0].d).length;
    status.innerHTML = '<strong>The exact values are ' + tone(dv.v.map(Rtext).join(' and '), 'green')
      + '</strong>, found by row reduction on (I − gP)v = r and then put straight back into that '
      + 'equation: r + gPv − v is exactly zero in every row, which is a check a decimal could not '
      + 'make. Value iteration from zero reaches ' + tone(Rfixed(dv.vT[0], 8), 'cyan')
      + ' after ' + T + ' step' + plural(T, '', 's') + ', leaving '
      + (Rzero(dv.gap[0]) ? 'nothing' : tone(Rfixed(Rabs(dv.gap[0]), 10), 'amber')) + ' to go — and it '
      + 'never arrives, because each step multiplies by one more power of the discount. That is '
      + 'visible rather than asserted: the denominator has grown by '
      + tone(grew + ' digit' + plural(grew, '', 's'), 'purple') + ' over those ' + T
      + ' steps. A float would have hidden both facts — the exactness of the fixed point and the cost '
      + 'of getting near it — behind the same fifteen digits.';
  }

  function apply() {
    var p = DCP[presetIn.value];
    if (!p) return;
    pIn.value = p.P; rIn.value = p.r; gIn.value = p.gamma;
    redraw();
  }
""" + _fill_js("DCP", [("pIn", "P"), ("rIn", "r")]) + r"""
  presetIn.addEventListener('change', apply);
  gIn.addEventListener('change', redraw);
  pIn.addEventListener('input', redraw);
  rIn.addEventListener('input', redraw);
  tIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Value iteration, and the fixed point under it",
        subtitle="One method approaches the answer and the other lands on it; both are exact here",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Iterate, and solve, and watch the gap between them"),
        panel_intro=cfg.get(
            "panel_intro",
            "The fixed point is found by row reduction and then put back into the equation it "
            "solves, so the residual is shown rather than assumed; the iteration is drawn beside it "
            "with the denominators it is accumulating.",
        ),
        script=script,
        expect={"dcPreset": _expect(_DC_PRESETS)},
    )


# ---------------------------------------------------------------------------
# The dispatch. `policy iteration` is deliberately absent: it belongs to course
# 9, where a chain has already been defined, and `discount` shows as much of
# the infinite horizon as a course with no chains behind it can honestly claim.
# ---------------------------------------------------------------------------

_MODES = {
    "stages": _stages,
    "allocation": _allocation,
    "lotsize": _lotsize,
    "heuristics": _heuristics,
    "stochastic": _stochastic,
    "tree": _tree,
    "stopping": _stopping,
    "secretary": _secretary,
    "discount": _discount,
}

MODES = tuple(sorted(_MODES))


def dpseq_lab(cfg):
    """Course 7's kit. `cfg["mode"]` chooses the lesson.

    An unknown mode raises, and so does an unknown preset. The raise is the
    contract rather than defensiveness: a kit that fell back to a default would
    render a finished-looking page carrying another lesson's widget, or the
    right lesson's widget opened on someone else's worked example. Both pass
    every markup assertion in the suite and both pass labcheck, because the lab
    builds and draws; the reader is simply shown the wrong arithmetic under the
    right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "dpseq_lab: unknown mode %r; the nine modes of the sequential-decisions course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["dpseq_lab", "MODES", "DPKIT_JS", "DPPLOT_JS", "DPPOL_JS", "DPTREE_JS", "DPSTOP_JS"]
