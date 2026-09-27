"""Integer Programming -- one kit, nine modes, one engine.

Every mode here is the same linear programme solved again under one more
restriction, which is the course's whole claim, and it is why nothing below
re-implements a solver. What the kit adds is the six things the engine
deliberately does not know: how to draw a lattice, how to read a reader's
inequality, how to cover a set, how to price a big-M, how to improve a tour,
and how to lay out a tree.

THE MODES, AND WHAT EACH COMPUTES

  lattice      the relaxation, every rounding of its optimum tested for
               feasibility with the violated row named, and the integer optimum
               by exhaustive enumeration -- three numbers whose ORDER is the
               lesson
  logic        a condition on binaries evaluated on every 0/1 assignment beside
               the inequality that claims to encode it, with the rows where
               the two disagree named
  knapsack     one capacity, three answers at once: the relaxation with its
               single split item, greed, and the exact optimum by enumeration;
               and a covering instance where `>= 1` and `= 1` differ
  bigm         the relaxation solved exactly at each M from the tightest valid
               value upward, the bound against M with its exact breakpoints,
               the fractional y the relaxation buys with a loose M, and the
               node count that loose M costs
  disjunction  each branch of an either-or pair as its own region, and the
               relaxation's fractional y with the schedule it describes, which
               does not exist
  bb           the tree, growing under the reader's choices of search order,
               branching variable and node budget, with the sub-regions drawn
  gap          the incumbent and the global bound against the node index, and
               depth-first against best-bound on the same instance
  gomory       a reader-picked fractional row, its cut in both coordinate
               systems drawn on the lattice, the dual-simplex re-solve, and the
               cycle repeated to integrality
  tsp          at most seven cities: the exhaustive optimum over all distinct
               tours, the assignment bound with subtour cuts and its tree, and
               a 2-opt tour measured against the bound

SIX DECISIONS RUN THROUGH ALL NINE.

  EACH MODE SHIPS ONLY THE BLOCKS IT CALLS. Nine lessons are nine pages and
  they do not need the same engine; the table `_MODE_JS` below says which gets
  what, and the comment above it carries the measurement that forced it.
  Measured as whole pages, on the heaviest chrome-and-prose baseline in the
  repository, the nine run from 28.2 KB gzipped for the encoding lesson to
  56.1 KB for the cutting-plane one, against a 62 KB ceiling.

  THE TREE IS NEVER HELD IN A CLOSURE. `bbTree` returns the whole node list
  for a given (model, order, maxNodes) and the reader's choices are cfg state
  that redraw() re-derives the tree from. That is what makes the second
  window.redrawLab() call produce the same picture as the first, and it is
  also why the tree can GROW: raising the node budget is a re-derivation, not
  a mutation.

  ONE LATTICE RENDERER, FOUR MODES. `ipLattice` draws the region, the integer
  points in it, any number of extra half-planes, and any number of marked
  points; `lattice`, `disjunction`, `bb` and `gomory` all call it with
  different arguments. This was a page-weight decision before it was a design
  one -- the engine share of this kit is 23.9 KB gzipped measured, against a
  62 KB ceiling for the whole page -- and it is the cut the contract names
  first. What it is NOT is a shared file: the renderer ships inside every page
  that uses it, like everything else here.

  THE TOUR COUNT IS `(n-1)!/2`. At seven cities that is 360 DISTINCT
  UNDIRECTED TOURS -- not 5 040 permutations, not 7!/2 = 2 520, and not
  (n-1)! = 720, which counts each tour once per direction. `tspExact`
  enumerates exactly the 360, `ipTourCount` computes the figure the page
  quotes from `fact`, and the two are held together in scripts/mathcheck.js so
  the prose cannot drift from the enumeration. The Algorithms path states the
  same quantity as (n-1)! for a fixed start; the cap of seven cities is this
  lab's own and exists because 360 tours redraw instantly.

  THE BOUND AGAINST M IS SCANNED, AND ITS BREAKPOINTS ARE SOLVED FOR. In a
  fixed-charge link `x_i <= M y_i` the big-M is a MATRIX coefficient, so it is
  not a right-hand side and `rhsRange` cannot range over it. `ipMBreaks`
  solves the pairwise ties exactly -- the relaxation buys y_i = x_i/M, so the
  effective unit cost is c_i + f_i/M and z is piecewise linear in 1/M -- and
  every breakpoint it returns is CHECKED by re-solving on both sides of it
  with `lpSolve`. `rhsCurve` is used where a right-hand side really is what
  varies: the demand row, whose exact piecewise-linear curve is drawn beside
  the M curve.

  EXACT EVERYWHERE, FLOATS ONLY FOR PIXELS. Every bound, gap, cut coefficient
  and node count is a rational over BigInt. `Number` appears in this file only
  to turn an exact value into an x or a y in an SVG, where the alternative is
  drawing with fractions.
"""

from .algebra_core import RATIONAL_JS
from .algebra_systems import FEAS_JS
from .common import Lab
from .counting import BIGINT_JS
from .logic import PARSER_JS
from .or_core import DUAL_JS, IP_JS, ORFMT_JS, PHASE_JS, RANGE_JS, TABLEAU_JS
from .sysdesign_core import RCEIL_JS


# ---------------------------------------------------------------------------
# The arithmetic and the drawing this kit adds, as top-level functions so
# scripts/mathcheck.js can call every one of them without a DOM. Nothing here
# touches the document; everything that does lives in the per-mode scripts.
#
# TWELVE BLOCKS, NOT ONE, for the reason or_core.py is thirteen: nine lessons
# are nine pages, and the tour lesson should not carry the covering model or
# the tree layout to draw a circle of seven cities. Which mode takes which is
# the table below the blocks.
#
# ONE LATTICE RENDERER, ONE TREE RENDERER, ONE PLOT. `IPLAT_JS` draws the
# region, the integer points in it, extra half-planes and marked points, and
# four modes call it with different arguments; `IPTREE_JS` lays out anything
# with a `parent`, which is the shape both bbTree and tspBranch return.
# ---------------------------------------------------------------------------

IPBASE_JS = r"""
  /* Reader text goes into innerHTML and on this course the reader types < and
     > all day, so it is escaped once at the boundary. Written here rather than
     borrowed from algebra_systems.FORMAT_JS because taking that block for six
     one-line helpers would put 1.3 KB gzipped on all nine pages of this course
     to save forty lines on one of them. */
  function ipEsc(t) {
    return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function ipTd(t, cls) { return '<td' + (cls ? ' class="' + cls + '"' : '') + '>' + t + '</td>'; }
  function ipTdl(t, cls) { return '<td style="text-align:left;"' + (cls ? ' class="' + cls + '"' : '') + '>' + t + '</td>'; }
  function ipTh(t) { return '<th>' + t + '</th>'; }
  function ipTr(cells, cls) { return '<tr' + (cls ? ' class="' + cls + '"' : '') + '>' + cells.join('') + '</tr>'; }
  function ipChip(t, kind) { return '<span class="chip' + (kind ? ' ' + kind : '') + '">' + t + '</span>'; }
  function ipHead(cells) { return '<thead>' + ipTr(cells.map(ipTh)) + '</thead>'; }

  /* Rparse throws on a zero denominator and 1/0 is a thing a reader types, so
     every read of reader input goes through this and a bad fraction becomes a
     sentence in the status banner rather than an exception. */
  function ipRead(text) {
    try { return Rparse(String(text).trim()); } catch (err) { return null; }
  }

  /* Pixels, and only pixels. Nothing downstream reads these back: an exact
     rational becomes an x or a y here and the arithmetic that is REPORTED
     never goes through Number. */
  function ipPx(r) { return Number(r.n) / Number(r.d); }
  function ipAt(v, lo, hi, a, b) { return a + (v - lo) * (b - a) / (hi - lo || 1); }

  function ipEl(tag, attrs, inner) {
    var s = '<' + tag, k;
    for (k in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, k) && attrs[k] !== null && attrs[k] !== undefined) {
        s += ' ' + k + '="' + attrs[k] + '"';
      }
    }
    return inner === undefined ? s + ' />' : s + '>' + inner + '</' + tag + '>';
  }

  function ipLabel(x, y, text, tone, anchor, size) {
    return ipEl('text', { x: x, y: y, 'font-size': size || 10, 'text-anchor': anchor || 'start',
                          fill: 'var(--' + (tone || 'muted') + ')' }, text);
  }
"""


IPMODEL_JS = r"""
  /* ---- models the reader can change, built rather than stored ----------- */

  /* A two-variable instance from plain numbers. `rows` is
     [[a1, a2, rel, b, name], ...] and nothing here is a stored answer: the
     lab solves what this builds. */
  function ipTwoVar(maxim, c1, c2, rows, names) {
    return { max: maxim, names: names || ['x1', 'x2'],
             obj: [R(BigInt(c1), 1n), R(BigInt(c2), 1n)],
             cons: rows.map(function (r) {
               return { a: [R(BigInt(r[0]), 1n), R(BigInt(r[1]), 1n)], rel: r[2],
                        b: R(BigInt(r[3]), 1n), name: r[4] };
             }) };
  }

  /* Every constraint of a two-variable model as a <= half-plane, with the
     x >= 0 and y >= 0 rows added, which is what the picture actually bounds.
     Cfromrow does the >= negation, so there is one direction to reason
     about. */
  function ipHalfPlanes(model) {
    var out = [], i;
    for (i = 0; i < model.cons.length; i += 1) {
      var k = model.cons[i];
      out = out.concat(Cfromrow({ c: [k.a[0], k.a[1]], rel: k.rel || 'le', b: k.b,
                                  src: k.name || ('row ' + (i + 1)) }));
    }
    out.push(Cnew(R(-1n, 1n), R0, R0, false, model.names[0] + ' >= 0'));
    out.push(Cnew(R0, R(-1n, 1n), R0, false, model.names[1] + ' >= 0'));
    return out;
  }

  /* The first row a point breaks, named, or null when it breaks none. This is
     what turns "infeasible" into a sentence: a rounding that fails fails
     somewhere, and the reader should be told where. */
  function ipViolated(model, pt) {
    var i, j;
    for (j = 0; j < pt.length; j += 1) if (Rsign(pt[j]) < 0) return model.names[j] + ' < 0';
    for (i = 0; i < model.cons.length; i += 1) {
      var k = model.cons[i], s = R0;
      for (j = 0; j < pt.length; j += 1) s = Radd(s, Rmul(k.a[j], pt[j]));
      var rel = k.rel || 'le', c = Rcmp(s, k.b);
      var ok = rel === 'le' ? c <= 0 : (rel === 'ge' ? c >= 0 : c === 0);
      if (!ok) return (k.name || ('row ' + (i + 1))) + ' (it wants ' + Rtext(s) + ')';
    }
    return null;
  }

  function ipObjective(model, pt) {
    var s = R0, j;
    for (j = 0; j < pt.length; j += 1) s = Radd(s, Rmul(model.obj[j], pt[j]));
    return s;
  }

  /* The 2^k roundings of a point, every combination of floor and ceiling --
     not "the rounding", because there is no such thing once more than one
     coordinate is fractional, and believing there is is the misconception the
     opening mode exists to break. */
  function ipRoundings(x) {
    var out = [{ pt: [], how: [] }], j, k, next;
    for (j = 0; j < x.length; j += 1) {
      next = [];
      var lo = R(Rfloor(x[j]), 1n), hi = R(Rceil(x[j]), 1n);
      var opts = Requ(lo, hi) ? [[lo, 'exact']] : [[lo, 'down'], [hi, 'up']];
      for (k = 0; k < out.length; k += 1) {
        for (var q = 0; q < opts.length; q += 1) {
          next.push({ pt: out[k].pt.concat([opts[q][0]]), how: out[k].how.concat([opts[q][1]]) });
        }
      }
      out = next;
    }
    return out;
  }

  /* ---- the gap, which is the deliverable -------------------------------- */

  /* STILL OPEN means never expanded: not pruned, and not branched either.
     bbTree sets `prunedBy` on a node it closed and leaves it null on one it
     branched, so "prunedBy is null" alone counts every interior node of a
     finished tree as open. */
  function ipOpen(node) {
    return !node.prunedBy && node.bound !== null && !(node.children && node.children.length);
  }

  /* The global bound WHEN THE SEARCH STOPPED EARLY: the best thing any node it
     never got to still promises. A tree that finished has no such node, and
     then the bound is the incumbent and the gap is nought.

     Not re-derived per step: the honest step-by-step record is `bounds`, which
     bbTree writes as it explores, because exploration order is not node order
     and a trace recomputed from the finished list gets it wrong -- it reported
     a bound of 54 on an instance whose optimum is 55, which is the kind of
     wrong a page must not be. `ipBoundTrace` reads that record instead. */
  function ipOpenBound(nodes, maximise) {
    var best = null, i;
    for (i = 0; i < nodes.length; i += 1) {
      if (!ipOpen(nodes[i])) continue;
      if (best === null || (maximise ? Rcmp(nodes[i].bound, best) > 0 : Rcmp(nodes[i].bound, best) < 0)) {
        best = nodes[i].bound;
      }
    }
    return best;
  }

  /* The incumbent and the global bound after each node, from the two records
     bbTree keeps as it runs -- `bounds` after every branch and `incumbents`
     whenever one improves -- merged, forward-filled and finished off with the
     state the search stopped in. Same tree in, same trace out. */
  function ipBoundTrace(tree, maximise) {
    var marks = [], i;
    for (i = 0; i < tree.bounds.length; i += 1) {
      marks.push({ at: tree.bounds[i].at, bound: tree.bounds[i].bound, incumbent: tree.bounds[i].incumbent });
    }
    for (i = 0; i < tree.incumbents.length; i += 1) {
      marks.push({ at: tree.incumbents[i].at, bound: null, incumbent: tree.incumbents[i].value });
    }
    marks.sort(function (a, b) { return a.at - b.at; });
    var openBound = ipOpenBound(tree.nodes, maximise);
    marks.push({ at: tree.nodes.length,
                 bound: tree.refused ? openBound : tree.best,
                 incumbent: tree.best });
    var out = [], bound = null, inc = null;
    for (i = 0; i < marks.length; i += 1) {
      if (marks[i].bound !== null) bound = marks[i].bound;
      if (marks[i].incumbent !== null && (inc === null || (maximise ? Rcmp(marks[i].incumbent, inc) > 0 : Rcmp(marks[i].incumbent, inc) < 0))) {
        inc = marks[i].incumbent;
      }
      if (out.length && out[out.length - 1].at === marks[i].at) out.pop();
      out.push({ at: marks[i].at, bound: bound, incumbent: inc });
    }
    return out;
  }

  /* Absolute and relative, both exact, and `proved` is the sentence the course
     wants said out loud: a gap is a statement about the BOUND, with no
     probability anywhere in it.

     The relative gap is measured AGAINST THE INCUMBENT -- the value actually in
     hand -- which is the convention every solver reports and the only one that
     is defined before the optimum is known. Every page that prints it says
     which number it is a percentage of, because against the bound instead it is
     a different figure and a reader comparing two pages would have no way to
     tell. */
  function ipGap(bound, incumbent, maximise) {
    if (bound === null || incumbent === null) return { closed: false, abs: null, rel: null, proved: 'nothing is proved yet: there is no incumbent to bound' };
    var abs = Rabs(Rsub(bound, incumbent));
    var rel = Rzero(incumbent) ? null : Rdiv(abs, Rabs(incumbent));
    return { closed: Rzero(abs), abs: abs, rel: rel,
             proved: Rzero(abs)
               ? 'the gap is zero, so the incumbent is optimal and that is a proof'
               : 'nothing beats the incumbent by more than ' + Rtext(abs)
                 + (rel === null ? '' : ' (' + Rpct(rel, 2) + ')')
                 + ', which is a statement about the bound and not about how likely the incumbent is to be best' };
  }
"""


IPINEQ_JS = r"""
  /* ---- a reader's inequality, read exactly ------------------------------ */

  /* `2A + B <= 1` over named binaries, as {a, rel, b} in exact rationals, or
     {error} with a sentence. Written here rather than borrowed because the
     grammar is one line of a linear form over a fixed, known variable list --
     the general expression parser would drag its own block onto every page of
     this course for `yA - yB <= 0`. A leading y or y_ is accepted, because
     that is how the prose writes them. */
  function ipIneq(text, names, prefix) {
    var src = String(text).replace(/\s+/g, '').replace(/−/g, '-')
      .replace(/≤/g, '<=').replace(/≥/g, '>=');
    var m = /(<=|>=|=<|=>|<|>|=)/.exec(src);
    if (!m) return { error: 'there is no &lt;=, &gt;= or = in that, so it is not an inequality' };
    var rel = m[1] === '=<' ? '<=' : (m[1] === '=>' ? '>=' : m[1]);
    var lhs = src.slice(0, m.index), rhs = src.slice(m.index + m[1].length);
    var a = names.map(function () { return R0; }), b = R0, side, sgn, part, i;
    for (side = 0; side < 2; side += 1) {
      var text2 = side === 0 ? lhs : rhs, outer = side === 0 ? 1n : -1n;
      if (text2 === '') return { error: 'one side of that inequality is empty' };
      var re = /([+-]?)(\d+(?:\/\d+)?)?\*?([A-Za-z][A-Za-z0-9_]*)?/g, mm, used = 0;
      while ((mm = re.exec(text2)) !== null) {
        if (mm[0] === '') { re.lastIndex += 1; if (re.lastIndex > text2.length) break; continue; }
        used += mm[0].length;
        sgn = mm[1] === '-' ? -1n : 1n;
        var coef = mm[2] === undefined ? R1 : Rparse(mm[2]);
        if (mm[3] === undefined) { b = Rsub(b, Rmul(R(sgn * outer, 1n), coef)); continue; }
        var nm = prefix ? mm[3].replace(new RegExp('^' + prefix + '_?', 'i'), '') : mm[3];
        var at = -1;
        for (i = 0; i < names.length; i += 1) if (names[i].toLowerCase() === nm.toLowerCase()) at = i;
        if (at < 0) {
          return { error: 'there is no variable called ' + ipEsc(mm[3]) + ' here; the variables are '
                     + (prefix || '') + names.join(', ' + (prefix || '')) };
        }
        a[at] = Radd(a[at], Rmul(R(sgn * outer, 1n), coef));
      }
      if (used !== text2.length) return { error: 'that side does not read as a sum of terms' };
    }
    /* Terms with a variable accumulate into `a` with the sign of the side they
       came from; bare constants accumulate into `b` with the opposite one,
       which is what "move it across" means. */
    return { a: a, rel: rel, b: b, names: names, prefix: prefix || '' };
  }

  function ipIneqValue(ineq, bits) {
    var s = R0, j;
    for (j = 0; j < ineq.a.length; j += 1) if (bits[j]) s = Radd(s, ineq.a[j]);
    return s;
  }

  function ipIneqHolds(ineq, bits) {
    var c = Rcmp(ipIneqValue(ineq, bits), ineq.b);
    if (ineq.rel === '<=') return c <= 0;
    if (ineq.rel === '>=') return c >= 0;
    if (ineq.rel === '<') return c < 0;
    if (ineq.rel === '>') return c > 0;
    return c === 0;
  }

  /* "yA - yB", not "(1)yA + (-1)yB": a coefficient of one is not written and a
     negative one is a minus sign, because that is what the reader typed and
     what the prose shows. */
  function ipIneqText(ineq) {
    var out = '', j;
    for (j = 0; j < ineq.a.length; j += 1) {
      var c = ineq.a[j];
      if (Rzero(c)) continue;
      var neg = Rsign(c) < 0, mag = Rabs(c);
      out += (out === '' ? (neg ? '-' : '') : (neg ? ' - ' : ' + '))
        + (Requ(mag, R1) ? '' : Rtext(mag)) + (ineq.prefix || '') + ineq.names[j];
    }
    var rel = ineq.rel === '<=' ? '&lt;=' : (ineq.rel === '>=' ? '&gt;=' : ipEsc(ineq.rel));
    return (out === '' ? '0' : out) + ' ' + rel + ' ' + Rtext(ineq.b);
  }

  /* The whole comparison in one call: the condition on every assignment, the
     inequality on every assignment, and the rows where they disagree. A wrong
     encoding is refuted by a ROW, which is the habit this mode exists to
     build. */
  function ipEncodingCheck(condSrc, ineqText, names) {
    var tree;
    try { tree = parse(condSrc); } catch (err) { return { error: 'the condition does not parse: ' + err.message }; }
    var ineq = ipIneq(ineqText, names, 'y');
    if (ineq.error) return { error: ineq.error };
    var rows = assignments(names).map(function (env) {
      var bits = names.map(function (nm) { return env[nm] ? 1 : 0; });
      var cond = evalNode(tree, env), holds = ipIneqHolds(ineq, bits);
      return { bits: bits, condition: cond, inequality: holds,
               value: ipIneqValue(ineq, bits), agree: cond === holds };
    });
    var bad = rows.filter(function (r) { return !r.agree; });
    return { rows: rows, ineq: ineq, tree: tree, disagree: bad, valid: bad.length === 0,
             witness: bad.length ? bad[0] : null };
  }
"""


IPCOVER_JS = r"""
  /* ---- set covering: the second atom ------------------------------------ */

  /* inc[i][j] is 1 when set j covers requirement i. The model is built, not
     tabulated, so a reader who edits the incidence sees the LP re-solved. */
  function ipCoverModel(inc, cost, rel) {
    var n = cost.length, m = inc.length, names = [], j, i;
    for (j = 0; j < n; j += 1) names.push('s' + (j + 1));
    var cons = [];
    for (i = 0; i < m; i += 1) {
      var a = [];
      for (j = 0; j < n; j += 1) a.push(R(BigInt(inc[i][j]), 1n));
      cons.push({ a: a, rel: rel || 'ge', b: R1, name: 'requirement ' + (i + 1) });
    }
    for (j = 0; j < n; j += 1) {
      var u = [];
      for (i = 0; i < n; i += 1) u.push(i === j ? R1 : R0);
      cons.push({ a: u, rel: 'le', b: R1, name: names[j] + ' <= 1' });
    }
    return { max: false, names: names, obj: cost.slice(), cons: cons };
  }

  /* Greed on cost per newly covered requirement, and the exact optimum by
     enumeration over subsets -- capped at the same twelve the knapsack uses,
     because 2^12 is the number both atoms can afford. */
  function ipCoverGreedy(inc, cost) {
    var n = cost.length, m = inc.length, left = [], chosen = [], total = R0, steps = [], i, j;
    for (i = 0; i < m; i += 1) left.push(true);
    while (left.indexOf(true) >= 0) {
      var best = -1, bestRatio = null, bestNew = 0;
      for (j = 0; j < n; j += 1) {
        if (chosen.indexOf(j) >= 0) continue;
        var fresh = 0;
        for (i = 0; i < m; i += 1) if (left[i] && inc[i][j]) fresh += 1;
        if (!fresh) continue;
        var ratio = Rdiv(cost[j], R(BigInt(fresh), 1n));
        if (best < 0 || Rcmp(ratio, bestRatio) < 0) { best = j; bestRatio = ratio; bestNew = fresh; }
      }
      if (best < 0) return { feasible: false, chosen: chosen, value: total, steps: steps,
                             why: 'no remaining set covers anything still uncovered, so greed cannot finish and neither can any choice: this instance has a requirement nothing covers' };
      chosen.push(best); total = Radd(total, cost[best]);
      for (i = 0; i < m; i += 1) if (inc[i][best]) left[i] = false;
      steps.push({ set: best, fresh: bestNew, ratio: bestRatio, running: total });
    }
    return { feasible: true, chosen: chosen, value: total, steps: steps };
  }

  function ipCoverExact(inc, cost, rel) {
    var n = cost.length, m = inc.length, limit = 1 << n, mask, i, j;
    if (n > 12) return { exhaustive: false, count: null, value: null, subset: null,
                         why: 'this enumerates every subset and twelve sets is 4096 of them, which is where it stops' };
    var best = null, bestSet = null, feasibleCount = 0;
    for (mask = 0; mask < limit; mask += 1) {
      var ok = true;
      for (i = 0; i < m && ok; i += 1) {
        var hits = 0;
        for (j = 0; j < n; j += 1) if ((mask & (1 << j)) && inc[i][j]) hits += 1;
        ok = rel === 'eq' ? hits === 1 : hits >= 1;
      }
      if (!ok) continue;
      feasibleCount += 1;
      var v = R0;
      for (j = 0; j < n; j += 1) if (mask & (1 << j)) v = Radd(v, cost[j]);
      if (best === null || Rcmp(v, best) < 0) { best = v; bestSet = mask; }
    }
    var subset = [];
    if (bestSet !== null) for (j = 0; j < n; j += 1) if (bestSet & (1 << j)) subset.push(j);
    return { exhaustive: true, count: limit, feasibleCount: feasibleCount,
             value: best, subset: best === null ? null : subset };
  }
"""


IPFIX_JS = r"""
  /* ---- the fixed charge, and what a loose M costs ----------------------- */

  /* A facility-location instance: open facility j for a fixed f_j, ship at
     c_j per unit, meet demand D, and no facility may ship more than its own
     capacity. The link is x_j - M y_j <= 0, and M is the MODELLING DECISION
     the mode is about.

     Variables come out as [x_1 .. x_k, y_1 .. y_k] so the y block is the tail
     and `ipFractionalY` can read it without knowing the instance. */
  function ipFixedCharge(spec, M) {
    var k = spec.fixed.length, names = [], obj = [], cons = [], j, i, a;
    for (j = 0; j < k; j += 1) { names.push('x' + (j + 1)); obj.push(spec.unit[j]); }
    for (j = 0; j < k; j += 1) { names.push('y' + (j + 1)); obj.push(spec.fixed[j]); }
    a = [];
    for (i = 0; i < 2 * k; i += 1) a.push(i < k ? R1 : R0);
    cons.push({ a: a, rel: 'ge', b: spec.demand, name: 'demand met' });
    for (j = 0; j < k; j += 1) {
      a = [];
      for (i = 0; i < 2 * k; i += 1) a.push(i === j ? R1 : (i === k + j ? Rneg(M) : R0));
      cons.push({ a: a, rel: 'le', b: R0, name: 'x' + (j + 1) + ' only if y' + (j + 1) });
      a = [];
      for (i = 0; i < 2 * k; i += 1) a.push(i === k + j ? R1 : R0);
      cons.push({ a: a, rel: 'le', b: R1, name: 'y' + (j + 1) + ' <= 1' });
      a = [];
      for (i = 0; i < 2 * k; i += 1) a.push(i === j ? R1 : R0);
      cons.push({ a: a, rel: 'le', b: spec.cap[j], name: 'capacity ' + (j + 1) });
    }
    return { max: false, names: names, obj: obj, cons: cons, k: k, M: M };
  }

  /* The tightest VALID M: a facility can never ship more than its capacity,
     and never more than the whole demand either, so the smaller of the two is
     valid and nothing smaller is. Saying WHY is the lesson; "a million" is
     not a reason and this returns one. */
  function ipTightM(spec) {
    var best = null, j;
    for (j = 0; j < spec.cap.length; j += 1) {
      if (best === null || Rcmp(spec.cap[j], best) > 0) best = spec.cap[j];
    }
    var tight = Rcmp(spec.demand, best) < 0 ? spec.demand : best;
    return { M: tight,
             why: Rcmp(spec.demand, best) < 0
               ? 'total demand is ' + Rtext(spec.demand) + ' and no facility can ship more than that, so ' + Rtext(spec.demand) + ' is valid and nothing smaller is'
               : 'the largest capacity is ' + Rtext(best) + ' and no facility can ship past its own capacity, so ' + Rtext(best) + ' is valid and nothing smaller is' };
  }

  /* The y block of a solution, which is where a loose M shows up: the
     relaxation sets y_j = x_j/M and buys the facility for a fraction of its
     fixed cost. */
  function ipFractionalY(model, x) {
    var out = [], j;
    for (j = 0; j < model.k; j += 1) out.push(x[model.k + j]);
    return out;
  }

  /* Where the bound against M bends, solved for rather than sampled.

     At the relaxation's optimum y_j = x_j/M, so facility j's effective unit
     cost is c_j + f_j/M: z is piecewise LINEAR in t = 1/M and each breakpoint
     is a tie c_i + t f_i = c_j + t f_j, i.e. t = (c_j - c_i)/(f_i - f_j),
     exact. Every candidate is then CHECKED by re-solving on both sides with
     lpSolve, so a breakpoint this returns is one the solver agrees is there --
     which matters, because the derivation above ignores the capacity rows and
     they can make a tie unreachable. */
  function ipMBreaks(spec, lo, hi) {
    var k = spec.fixed.length, cand = [], i, j;
    for (i = 0; i < k; i += 1) {
      for (j = i + 1; j < k; j += 1) {
        var df = Rsub(spec.fixed[i], spec.fixed[j]);
        if (Rzero(df)) continue;
        var t = Rdiv(Rsub(spec.unit[j], spec.unit[i]), df);
        if (Rsign(t) <= 0) continue;
        var M = Rinv(t);
        if (Rcmp(M, lo) <= 0 || Rcmp(M, hi) >= 0) continue;
        cand.push(M);
      }
    }
    cand.sort(Rcmp);
    var out = [], eps = R(1n, 1000n);
    for (i = 0; i < cand.length; i += 1) {
      if (i && Requ(cand[i], cand[i - 1])) continue;
      var here = ipBound(spec, cand[i]);
      var left = ipBound(spec, Rsub(cand[i], eps)), right = ipBound(spec, Radd(cand[i], eps));
      if (here === null || left === null || right === null) continue;
      var slopeL = Rsub(here, left), slopeR = Rsub(right, here);
      if (!Requ(slopeL, slopeR)) out.push({ M: cand[i], z: here, before: left, after: right });
    }
    return out;
  }

  /* The node count a given M costs, from the SAME branch-and-bound engine the
     search lesson uses. A shared function in the kit rather than a shared
     mode: only the y block is integral -- the shipped quantities stay
     continuous -- which is what a fixed-charge model is. */
  function ipFixedChargeNodes(spec, M, maxNodes) {
    var model = ipFixedCharge(spec, M), ints = [], j;
    for (j = 0; j < model.k; j += 1) ints.push(model.k + j);
    return bbTree(model, { integers: ints, maxNodes: maxNodes || 30 });
  }

  function ipBound(spec, M) {
    if (Rsign(M) <= 0) return null;
    var sol = lpSolve(ipFixedCharge(spec, M));
    return sol.status === 'optimal' ? sol.zOrig : null;
  }
"""


IPDISJ_JS = r"""
  /* ---- the disjunction -------------------------------------------------- */

  /* "A or B", written the only way it can be written: each row relaxed by a
     big-M term that one binary switches off. y = 1 enforces A and makes B
     vacuous; y = 0 does the reverse. Passing y = null leaves y continuous,
     which is the relaxation and the point of the mode.

        rowA:  a.x <= bA + MA (1 - y)      ->   a.x + MA y <= bA + MA
        rowB:  b.x <= bB + MB y            ->   b.x - MB y <= bB

     The two Ms need not be equal and each must be valid for its OWN side; one
     M used for both, unchecked, is how a disjunction quietly becomes an
     implication. */
  function ipDisjunction(spec, MA, MB, yFixed) {
    var cons = [], a, i;
    cons.push({ a: [spec.A[0], spec.A[1], MA], rel: 'le', b: Radd(spec.A[2], MA),
                name: spec.nameA + ' unless y = 0' });
    cons.push({ a: [spec.B[0], spec.B[1], Rneg(MB)], rel: 'le', b: spec.B[2],
                name: spec.nameB + ' unless y = 1' });
    for (i = 0; i < spec.both.length; i += 1) {
      cons.push({ a: [spec.both[i][0], spec.both[i][1], R0], rel: spec.both[i][3] || 'le',
                  b: spec.both[i][2], name: spec.both[i][4] });
    }
    cons.push({ a: [R0, R0, R1], rel: 'le', b: R1, name: 'y <= 1' });
    if (yFixed !== null && yFixed !== undefined) {
      cons.push({ a: [R0, R0, R1], rel: 'eq', b: R(BigInt(yFixed), 1n),
                  name: 'y = ' + yFixed });
    }
    return { max: spec.max !== false, names: [spec.names[0], spec.names[1], 'y'],
             obj: [spec.obj[0], spec.obj[1], R0], cons: cons };
  }

  /* The region one branch of the pair leaves, as half-planes in the reader's
     two variables -- the picture, with y already decided and the vacuous row
     dropped rather than drawn at a meaningless offset. */
  function ipBranchRegion(spec, y, MA, MB) {
    var live = y === 1 ? spec.A : spec.B, name = y === 1 ? spec.nameA : spec.nameB;
    var cons = [Cnew(live[0], live[1], live[2], false, name)], i;
    var dead = y === 1 ? spec.B : spec.A, deadName = y === 1 ? spec.nameB : spec.nameA;
    var deadM = y === 1 ? MB : MA;
    cons = cons.concat([Cnew(dead[0], dead[1], Radd(dead[2], deadM), false, deadName + ', relaxed by its own M')]);
    for (i = 0; i < spec.both.length; i += 1) {
      cons = cons.concat(Cfromrow({ c: [spec.both[i][0], spec.both[i][1]],
                                    rel: spec.both[i][3] || 'le', b: spec.both[i][2],
                                    src: spec.both[i][4] }));
    }
    cons.push(Cnew(R(-1n, 1n), R0, R0, false, spec.names[0] + ' >= 0'));
    cons.push(Cnew(R0, R(-1n, 1n), R0, false, spec.names[1] + ' >= 0'));
    return cons;
  }
"""


IPTOUR_JS = r"""
  /* ---- the tour counts, computed rather than quoted --------------------- */

  /* THE FOUR COUNTS, and which one this is.

     On a SYMMETRIC matrix a tour and its reversal are the same tour, so the
     distinct undirected tours with a fixed start number (n-1)!/2 -- 360 at
     seven cities. On an asymmetric one they are different tours and the count
     is (n-1)! -- 720 at seven. The other two are the ones the misconception
     reaches for: n! counts PERMUTATIONS of the cities (5 040 at seven) and
     n!/2 counts each of those once per direction (2 520). A page that
     computes all four cannot quietly mean a different one in the prose, and
     `tours` is what tspExact actually enumerates. */
  function ipTourCount(n, symmetric) {
    var perms = fact(n), directed = n < 2 ? 1n : fact(n - 1);
    return { tours: symmetric === false ? directed : (n < 3 ? 1n : directed / 2n),
             directed: directed, perms: perms, halfPerms: perms / 2n,
             symmetric: symmetric !== false,
             formula: symmetric === false ? '(n - 1)!' : '(n - 1)! / 2' };
  }

  function ipTourCost(d, tour) {
    var s = R0, k;
    for (k = 0; k + 1 < tour.length; k += 1) s = Radd(s, d[tour[k]][tour[k + 1]]);
    return s;
  }

  /* Nearest neighbour from city 0: the heuristic a reader reaches for, and
     the one the lesson measures rather than praises. */
  function ipNearest(d) {
    var n = d.length, seen = {}, tour = [0], at = 0, k, j;
    seen[0] = true;
    for (k = 1; k < n; k += 1) {
      var best = -1;
      for (j = 0; j < n; j += 1) {
        if (seen[j] || j === at) continue;
        if (best < 0 || Rcmp(d[at][j], d[at][best]) < 0) best = j;
      }
      seen[best] = true; tour.push(best); at = best;
    }
    tour.push(0);
    return { tour: tour, cost: ipTourCost(d, tour) };
  }

  /* 2-opt: reverse a segment whenever doing so shortens the tour, until no
     reversal does. Exact comparisons, so "no improving move" is a fact about
     the tour and not about a tolerance. */
  function ipTwoOpt(d) {
    var start = ipNearest(d), tour = start.tour.slice(), n = d.length;
    var moves = [], improved = true, guard = 0;
    while (improved && guard < 200) {
      improved = false; guard += 1;
      for (var i = 1; i < n - 1 && !improved; i += 1) {
        for (var j = i + 1; j < n && !improved; j += 1) {
          var cand = tour.slice(0, i).concat(tour.slice(i, j + 1).reverse(), tour.slice(j + 1));
          var before = ipTourCost(d, tour), after = ipTourCost(d, cand);
          if (Rcmp(after, before) < 0) {
            moves.push({ i: i, j: j, from: before, to: after });
            tour = cand; improved = true;
          }
        }
      }
    }
    return { tour: tour, cost: ipTourCost(d, tour), moves: moves,
             start: start.tour, startCost: start.cost };
  }

  /* The cities on a circle, with up to two tours over them. Coordinates are
     for the PICTURE only: every cost this mode reports comes from the matrix
     the reader can edit, never from the drawing. */
  function ipTourSvg(n, tours, opts) {
    var w = (opts && opts.width) || 660, h = (opts && opts.height) || 260;
    var cx = w / 2, cy = h / 2, r = Math.min(w, h) / 2 - 34, i, k;
    var at = [];
    for (i = 0; i < n; i += 1) {
      var th = -Math.PI / 2 + (2 * Math.PI * i) / n;
      at.push([cx + r * Math.cos(th), cy + r * Math.sin(th)]);
    }
    var s = '';
    for (k = 0; k < tours.length; k += 1) {
      var t = tours[k], d = '';
      for (i = 0; i < t.tour.length; i += 1) {
        d += (i ? 'L' : 'M') + at[t.tour[i]][0] + ' ' + at[t.tour[i]][1];
      }
      s += ipEl('path', { d: d, fill: 'none', stroke: 'var(--' + t.tone + ')',
                          'stroke-width': t.width || 2, 'stroke-dasharray': t.dashed ? '6 4' : null,
                          'stroke-opacity': t.faint ? '0.65' : '1' });
    }
    for (i = 0; i < n; i += 1) {
      s += ipEl('circle', { cx: at[i][0], cy: at[i][1], r: 11, fill: 'var(--panel-3)',
                            stroke: 'var(--line-strong)', 'stroke-width': 1 });
      s += ipLabel(at[i][0], at[i][1] + 4, String(i + 1), 'text', 'middle', 10);
    }
    return { svg: s, height: h };
  }
"""


IPCUT_JS = r"""
  /* ---- cutting to integrality ------------------------------------------- */

  /* The rows whose basic variable came back fractional: the only rows a
     Gomory cut can be derived from, and the choice the reader is given. */
  function ipFracRows(tab) {
    var out = [], i;
    for (i = 0; i < tab.m; i += 1) if (!Rint(tab.T[i][tab.n])) out.push(i);
    return out;
  }

  function ipAllInt(point) {
    for (var i = 0; i < point.length; i += 1) if (!Rint(point[i])) return false;
    return true;
  }

  /* Derive, add, re-solve, repeat. The cut goes in IN THE READER'S VARIABLES
     -- `inOriginal`, the same coefficients the picture draws -- so what is
     added to the tableau and what is drawn on the lattice are one object and
     not two that have to be kept in step. addRow appends it and lets the dual
     simplex restore optimality, which is the whole reason a cut is cheap. */
  function ipCutRounds(model, rounds, firstRow, opts) {
    var sol = lpSolve(model, opts);
    if (sol.status !== 'optimal') return { status: sol.status, steps: [], start: sol };
    var tab = sol.tab, steps = [], point = sol.x, z = sol.zOrig, k;
    for (k = 0; k < rounds; k += 1) {
      if (ipAllInt(point)) break;
      var frac = ipFracRows(tab);
      if (!frac.length) break;
      var row = (k === 0 && frac.indexOf(firstRow) >= 0) ? firstRow : frac[0];
      var cut = gomoryCut(tab, row);
      var added = addRow(tab, { a: cut.inOriginal.a.slice(), rel: 'ge', b: cut.inOriginal.b }, opts);
      if (added.status !== 'optimal') {
        steps.push({ cut: cut, row: row, status: added.status, pivots: 0, x: null, z: null });
        break;
      }
      tab = added.restored;
      var read = tabRead(tab);
      point = stdPoint(tab.std, read.x);
      z = read.zOrig;
      steps.push({ cut: cut, row: row, status: 'optimal', x: point.slice(), z: z,
                   pivots: added.run.pivots, integral: ipAllInt(point) });
    }
    return { status: 'optimal', steps: steps, tab: tab, x: point, z: z,
             integral: ipAllInt(point), start: sol };
  }

  /* A cut is VALID when every integer point of the feasible set satisfies it,
     not when it removes the point you dislike. So the test is over the whole
     lattice, and a cut that fails names the point it killed. */
  function ipCutValid(cut, points) {
    var killed = [], i, j;
    for (i = 0; i < points.length; i += 1) {
      if (!points[i].feasible) continue;
      var v = R0;
      for (j = 0; j < cut.a.length; j += 1) v = Radd(v, Rmul(cut.a[j], points[i].x[j]));
      var c = Rcmp(v, cut.b);
      var holds = cut.rel === '<=' ? c <= 0 : (cut.rel === '>=' ? c >= 0 : c === 0);
      if (!holds) killed.push(points[i]);
    }
    return { valid: killed.length === 0, killed: killed };
  }
"""


IPLAT_JS = r"""
  /* The corners of a region, in the order a polygon needs them rather than the
     order Ccorners hands them back, which is sorted by x. Sorting by angle
     about the centroid is correct here because the region is an intersection
     of half-planes and therefore convex. */
  function ipPolygon(cons) {
    var pts = Ccorners(cons).map(function (p) { return { x: ipPx(p.x), y: ipPx(p.y) }; });
    if (pts.length < 3) return pts;
    var cx = 0, cy = 0, i;
    for (i = 0; i < pts.length; i += 1) { cx += pts[i].x; cy += pts[i].y; }
    cx /= pts.length; cy /= pts.length;
    return pts.slice().sort(function (p, q) {
      return Math.atan2(p.y - cy, p.x - cx) - Math.atan2(q.y - cy, q.x - cx);
    });
  }

  /* THE SHARED LATTICE PICTURE.

     opts: { cons, box: [[x0, x1], [y0, y1]] in integers, points, marks, lines,
             overlay, width, height, names, note }

     `points` is what latticePoints returned, so the dots are the enumeration
     the panel quotes and not a second opinion about it. `lines` draws extra
     half-plane boundaries -- a Gomory cut, a branch bound -- in the reader's
     own coordinates, which is the only place a cut is visible at all. */
  function ipLattice(opts) {
    var w = opts.width || 520, h = opts.height || 300;
    var L = 34, Rm = 12, T = 12, B = 26;
    var x0 = opts.box[0][0], x1 = opts.box[0][1], y0 = opts.box[1][0], y1 = opts.box[1][1];
    var px = function (v) { return ipAt(v, x0, x1, L, w - Rm); };
    var py = function (v) { return ipAt(v, y0, y1, h - B, T); };
    var s = '', i, j;

    /* the region, then any overlay region on top of it */
    var poly = ipPolygon(opts.cons);
    if (poly.length >= 3) {
      s += ipEl('polygon', { points: poly.map(function (p) { return px(p.x) + ',' + py(p.y); }).join(' '),
                             fill: 'var(--cyan)', 'fill-opacity': '0.13',
                             stroke: 'var(--cyan)', 'stroke-width': '1.5' });
    }
    if (opts.overlay) {
      var over = ipPolygon(opts.overlay);
      if (over.length >= 3) {
        s += ipEl('polygon', { points: over.map(function (p) { return px(p.x) + ',' + py(p.y); }).join(' '),
                               fill: 'var(--purple)', 'fill-opacity': '0.18',
                               stroke: 'var(--purple)', 'stroke-width': '1.5',
                               'stroke-dasharray': '4 3' });
      }
    }

    /* the axes last-but-one so the region does not paint over them */
    s += ipEl('line', { x1: L, y1: py(0), x2: w - Rm, y2: py(0), stroke: 'var(--line-strong)', 'stroke-width': 1 });
    s += ipEl('line', { x1: px(0), y1: T, x2: px(0), y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 });
    for (i = Math.ceil(x0); i <= x1; i += 1) {
      s += ipLabel(px(i), h - B + 13, String(i), 'muted', 'middle', 9);
    }
    for (j = Math.ceil(y0); j <= y1; j += 1) {
      s += ipLabel(L - 6, py(j) + 3, String(j), 'muted', 'end', 9);
    }
    s += ipLabel(w - Rm, h - B + 13, (opts.names && opts.names[0]) || 'x1', 'text', 'end', 10);
    s += ipLabel(L - 6, T + 2, (opts.names && opts.names[1]) || 'x2', 'text', 'end', 10);

    /* the lattice itself */
    if (opts.points) {
      for (i = 0; i < opts.points.length; i += 1) {
        var q = opts.points[i], qx = px(ipPx(q.x[0])), qy = py(ipPx(q.x[1]));
        s += ipEl('circle', { cx: qx, cy: qy, r: q.feasible ? 3 : 1.8,
                              fill: q.feasible ? 'var(--green)' : 'var(--line-strong)',
                              'fill-opacity': q.feasible ? '0.95' : '0.6' });
      }
    }

    /* extra half-planes: a cut, a branch bound. Drawn as the boundary line
       clipped to the box, because the half-plane itself is already in cons. */
    for (i = 0; opts.lines && i < opts.lines.length; i += 1) {
      var ln = opts.lines[i], a = ipPx(ln.a), b = ipPx(ln.b), c = ipPx(ln.c);
      var seg = [];
      if (b !== 0) {
        seg.push([x0, (c - a * x0) / b]); seg.push([x1, (c - a * x1) / b]);
      } else if (a !== 0) {
        seg.push([c / a, y0]); seg.push([c / a, y1]);
      }
      if (seg.length === 2) {
        s += ipEl('line', { x1: px(seg[0][0]), y1: py(seg[0][1]), x2: px(seg[1][0]), y2: py(seg[1][1]),
                            stroke: 'var(--' + (ln.tone || 'red') + ')', 'stroke-width': 1.6,
                            'stroke-dasharray': ln.dashed === false ? null : '5 3' });
        if (ln.label) {
          s += ipLabel(px(Math.min(x1, Math.max(x0, seg[1][0]))) - 4,
                       py(Math.min(y1, Math.max(y0, seg[1][1]))) - 5, ln.label, ln.tone || 'red', 'end', 9);
        }
      }
    }

    /* marked points: the LP optimum, the roundings, the integer optimum */
    for (i = 0; opts.marks && i < opts.marks.length; i += 1) {
      var mk = opts.marks[i], mx = px(ipPx(mk.x)), my = py(ipPx(mk.y));
      if (mk.shape === 'square') {
        s += ipEl('rect', { x: mx - 5, y: my - 5, width: 10, height: 10, rx: 1.5,
                            fill: 'none', stroke: 'var(--' + mk.tone + ')', 'stroke-width': 2 });
      } else if (mk.shape === 'cross') {
        s += ipEl('path', { d: 'M' + (mx - 5) + ' ' + (my - 5) + 'L' + (mx + 5) + ' ' + (my + 5)
                              + 'M' + (mx + 5) + ' ' + (my - 5) + 'L' + (mx - 5) + ' ' + (my + 5),
                            stroke: 'var(--' + mk.tone + ')', 'stroke-width': 2, fill: 'none' });
      } else {
        s += ipEl('circle', { cx: mx, cy: my, r: 5.5, fill: 'none',
                              stroke: 'var(--' + mk.tone + ')', 'stroke-width': 2.2 });
      }
      if (mk.label) s += ipLabel(mx + 8, my - 6, mk.label, mk.tone, 'start', 9);
    }
    if (opts.note) s += ipLabel(L, h - 4, opts.note, 'muted', 'start', 9);
    return s;
  }
"""


IPTREE_JS = r"""
  /* THE SHARED TREE. Depth down the page, sibling index across it, each node
     carrying its bound and -- on a leaf -- the reason it closed. Nodes arrive
     as a flat list with `parent`, which is exactly what bbTree and tspBranch
     both return, so neither has to be reshaped to be drawn. */
  function ipTreeSvg(nodes, opts) {
    opts = opts || {};
    var w = opts.width || 660, i, j;
    var maxDepth = 0, byDepth = {};
    for (i = 0; i < nodes.length; i += 1) {
      maxDepth = Math.max(maxDepth, nodes[i].depth);
      byDepth[nodes[i].depth] = (byDepth[nodes[i].depth] || []).concat([i]);
    }
    var rowH = opts.rowH || 46, h = 24 + (maxDepth + 1) * rowH;
    var at = {}, s = '';
    for (var d = 0; d <= maxDepth; d += 1) {
      var row = byDepth[d] || [];
      for (j = 0; j < row.length; j += 1) {
        at[row[j]] = { x: (w * (j + 1)) / (row.length + 1), y: 20 + d * rowH };
      }
    }
    for (i = 0; i < nodes.length; i += 1) {
      var p = nodes[i].parent;
      if (p === null || p === undefined || !at[p]) continue;
      s += ipEl('line', { x1: at[p].x, y1: at[p].y + 11, x2: at[i].x, y2: at[i].y - 11,
                          stroke: 'var(--line-strong)', 'stroke-width': 1 });
    }
    for (i = 0; i < nodes.length; i += 1) {
      var n = nodes[i], tone = opts.tone ? opts.tone(n) : 'cyan';
      var bw = Math.min(96, Math.max(54, (w / Math.max(1, (byDepth[n.depth] || []).length)) - 10));
      s += ipEl('rect', { x: at[i].x - bw / 2, y: at[i].y - 11, width: bw, height: 22, rx: 3,
                          fill: 'var(--' + tone + ')', 'fill-opacity': '0.16',
                          stroke: 'var(--' + tone + ')', 'stroke-width': 1.2 });
      s += ipLabel(at[i].x, at[i].y + 2, opts.top ? opts.top(n) : String(n.id), tone, 'middle', 10);
      var under = opts.bottom ? opts.bottom(n) : '';
      if (under) s += ipLabel(at[i].x, at[i].y + 18, under, 'muted', 'middle', 8.5);
      var over = opts.above ? opts.above(n) : '';
      if (over) s += ipLabel(at[i].x, at[i].y - 14, over, 'muted', 'middle', 8.5);
    }
    return { svg: s, height: h, depth: maxDepth };
  }
"""


IPPLOT_JS = r"""
  /* THE SHARED PLOT: step or straight, several series, exact values turned
     into pixels at the last moment. `bigm` draws a bound against M on it and
     `gap` draws an incumbent and a bound against the node index. */
  function ipPlot(series, opts) {
    var w = opts.width || 660, h = opts.height || 240;
    var L = 46, Rm = 14, T = 14, B = 30, i, k;
    var xs = [], ys = [];
    for (i = 0; i < series.length; i += 1) {
      for (k = 0; k < series[i].pts.length; k += 1) { xs.push(series[i].pts[k][0]); ys.push(series[i].pts[k][1]); }
    }
    if (!xs.length) return { svg: '', height: h };
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    var y0 = opts.y0 !== undefined ? opts.y0 : Math.min.apply(null, ys);
    var y1 = Math.max.apply(null, ys);
    if (y1 === y0) { y1 = y0 + 1; }
    if (x1 === x0) { x1 = x0 + 1; }
    var px = function (v) { return ipAt(v, x0, x1, L, w - Rm); };
    var py = function (v) { return ipAt(v, y0, y1, h - B, T); };
    var s = ipEl('line', { x1: L, y1: h - B, x2: w - Rm, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 })
          + ipEl('line', { x1: L, y1: T, x2: L, y2: h - B, stroke: 'var(--line-strong)', 'stroke-width': 1 });
    for (i = 0; i < 4; i += 1) {
      var gy = y0 + ((y1 - y0) * i) / 3;
      s += ipEl('line', { x1: L, y1: py(gy), x2: w - Rm, y2: py(gy), stroke: 'var(--line)', 'stroke-width': 0.6 });
      s += ipLabel(L - 5, py(gy) + 3, (opts.fmtY ? opts.fmtY(gy) : gy.toFixed(2)), 'muted', 'end', 9);
    }
    for (i = 0; i < series.length; i += 1) {
      var ser = series[i], pts = ser.pts, path = '';
      for (k = 0; k < pts.length; k += 1) {
        if (k === 0) path += 'M' + px(pts[k][0]) + ' ' + py(pts[k][1]);
        else if (ser.step) path += 'L' + px(pts[k][0]) + ' ' + py(pts[k - 1][1]) + 'L' + px(pts[k][0]) + ' ' + py(pts[k][1]);
        else path += 'L' + px(pts[k][0]) + ' ' + py(pts[k][1]);
      }
      s += ipEl('path', { d: path, fill: 'none', stroke: 'var(--' + ser.tone + ')', 'stroke-width': 1.8,
                          'stroke-dasharray': ser.dashed ? '5 3' : null });
      if (ser.dots) {
        for (k = 0; k < pts.length; k += 1) {
          s += ipEl('circle', { cx: px(pts[k][0]), cy: py(pts[k][1]), r: 2.6, fill: 'var(--' + ser.tone + ')' });
        }
      }
    }
    for (i = 0; opts.drops && i < opts.drops.length; i += 1) {
      s += ipEl('line', { x1: px(opts.drops[i].x), y1: T, x2: px(opts.drops[i].x), y2: h - B,
                          stroke: 'var(--amber)', 'stroke-width': 1, 'stroke-dasharray': '3 3' });
      if (opts.drops[i].label) s += ipLabel(px(opts.drops[i].x) + 3, T + 10, opts.drops[i].label, 'amber', 'start', 8.5);
    }
    s += ipLabel(w - Rm, h - 8, opts.xLabel || '', 'text', 'end', 10);
    s += ipLabel(L, h - 8, (opts.fmtX ? opts.fmtX(x0) : String(x0)), 'muted', 'start', 9);
    return { svg: s, height: h, x0: x0, x1: x1 };
  }
"""


IPBARS_JS = r"""
  /* THE SHARED BARS: three numbers whose ORDER is the lesson -- a relaxation,
     a heuristic and an optimum -- drawn so the order is visible rather than
     read out of a table. */
  function ipBars(items, opts) {
    var w = opts.width || 660, rowH = 30, h = 14 + items.length * rowH;
    var L = opts.left || 132, Rm = 92, i;
    var top = null;
    for (i = 0; i < items.length; i += 1) {
      var v = Math.abs(ipPx(items[i].value));
      if (top === null || v > top) top = v;
    }
    if (!top) top = 1;
    var s = '';
    for (i = 0; i < items.length; i += 1) {
      var y = 8 + i * rowH, len = (Math.abs(ipPx(items[i].value)) / top) * (w - L - Rm);
      s += ipLabel(L - 8, y + 14, items[i].label, items[i].tone, 'end', 10);
      s += ipEl('rect', { x: L, y: y + 4, width: Math.max(1, len), height: 14, rx: 2,
                          fill: 'var(--' + items[i].tone + ')', 'fill-opacity': '0.75' });
      s += ipLabel(L + len + 6, y + 15, items[i].text || Rtext(items[i].value), items[i].tone, 'start', 10);
    }
    return { svg: s, height: h };
  }
"""



# ---------------------------------------------------------------------------
# WHICH BLOCKS EACH MODE SHIPS, and why that is a table rather than a constant.
#
# or_core.py's own header says a kit "concatenates only the blocks it needs and
# no others -- this is the single biggest lever on page weight". Nine lessons
# are nine SEPARATE PAGES, and they do not need the same blocks: the tour
# lesson never builds a tableau, the encoding lesson never solves a linear
# programme at all, and only the four that branch or cut need the dual simplex
# and the ranging block behind it.
#
# The measurement that forced this. All of it on one page -- engine, region
# arithmetic, both kit blocks -- is 39.8 KB gzipped, and a real lesson page's
# chrome and prose is 19.7 to 22.8 KB gzipped (measured over the 218 generated
# pages). One mode of this kit, built that way, came to 62.0 KB against a 62 KB
# ceiling, with eight more modes still to add. Selecting per mode is what the
# contract calls a smaller lab, and it is the second cut after the shared
# lattice renderer; the alternative -- one file both paths load -- is the one
# thing this repository does not trade away.
#
# THE RULE FOR EDITING THIS TABLE: a block belongs in a mode's list when that
# mode CALLS something in it. Every block here is top-level function
# declarations only, so a function that is present but never called costs
# bytes and nothing else -- and a function that is called but absent throws on
# the first redraw, which scripts/labcheck.js catches on every published page.
# ---------------------------------------------------------------------------

_BASE = RATIONAL_JS + ORFMT_JS + IPBASE_JS     # every mode prints and escapes
_SOLVE = TABLEAU_JS + PHASE_JS                 # lpSolve and the tableau under it
_RESOLVE = DUAL_JS + RANGE_JS                  # dual simplex, addRow, rhsCurve
_REGION = FEAS_JS + IPMODEL_JS + IPLAT_JS      # the picture four modes share

_MODE_JS = {
    # the lattice picture: solve, enumerate, round
    "lattice": _BASE + RCEIL_JS + _SOLVE + IP_JS + _REGION,
    # a condition and an inequality on 2^n assignments: no linear programme at all
    "logic": RATIONAL_JS + IPBASE_JS + PARSER_JS + IPINEQ_JS,
    # one capacity three ways, and a covering LP beside it
    "knapsack": _BASE + BIGINT_JS + _SOLVE + IP_JS + IPMODEL_JS + IPCOVER_JS + IPBARS_JS,
    # the bound against M, its breakpoints, and what a loose M costs in nodes
    "bigm": _BASE + RCEIL_JS + _SOLVE + _RESOLVE + IP_JS + IPMODEL_JS + IPFIX_JS + IPPLOT_JS,
    # two regions, one binary, and the fractional y between them
    "disjunction": _BASE + _SOLVE + _REGION + IPDISJ_JS,
    # the tree, growing, with the sub-regions drawn
    "bb": _BASE + RCEIL_JS + _SOLVE + _RESOLVE + IP_JS + _REGION + IPTREE_JS,
    # the incumbent and the bound against the node index
    "gap": _BASE + RCEIL_JS + _SOLVE + _RESOLVE + IP_JS + IPMODEL_JS + IPPLOT_JS,
    # a cut, drawn in the reader's coordinates, then added and re-solved
    "gomory": _BASE + RCEIL_JS + _SOLVE + _RESOLVE + IP_JS + _REGION + IPINEQ_JS + IPCUT_JS,
    # every distinct tour, the assignment bound, and a heuristic measured
    "tsp": _BASE + BIGINT_JS + IP_JS + IPMODEL_JS + IPTOUR_JS + IPTREE_JS,
}


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every lab on the library uses, so a reader
# moving between courses moves between the same widgets.
# ---------------------------------------------------------------------------


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


def _table(cid):
    return '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%s"></table></div>\n' % cid


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _preset(cfg, mode, table, default):
    """The preset this lesson opens on, or a refusal.

    A preset that fell back to a default would render the WRONG worked example
    under the right lesson's prose -- the panel's numbers would not be the
    prose's numbers -- and nothing in the suite would notice, because the lab
    builds and draws. So an unknown one raises, the same way an unknown mode
    does. Every lesson opens on its own worked example by naming it here.
    """
    name = cfg.get("preset", default)
    if name not in table:
        raise ValueError(
            "integer_lab: mode %r has no preset %r; its presets are %s"
            % (mode, name, ", ".join(sorted(table)))
        )
    return name, table[name]


# ---------------------------------------------------------------------------
# lattice -- when rounding fails
# ---------------------------------------------------------------------------

# Each preset is a two-variable integer programme, its bounding box, and the
# one sentence that says what it is for. The opening one is the one whose
# integer optimum sits at the far end of the region from the LP optimum,
# because the misconception the mode exists to break is "the integer answer is
# near the fractional one".
_LATTICE = {
    "far": (
        "max 3x1 + 4x2 subject to 2x1 + x2 &lt;= 6 and 2x1 + 3x2 &lt;= 9",
        "true, 3, 4, [[2,1,'le',6,'assembly'],[2,3,'le',9,'finishing']], 0, 5, 0, 4",
    ),
    "rounddown": (
        "min 5x1 + 4x2 subject to 3x1 + 2x2 &gt;= 7 and x1 + 4x2 &gt;= 6",
        "false, 5, 4, [[3,2,'ge',7,'protein'],[1,4,'ge',6,'fibre'],[1,0,'le',4,'x1 cap'],[0,1,'le',4,'x2 cap']], 0, 4, 0, 4",
    ),
    "integral": (
        "max 2x1 + 3x2 subject to x1 + x2 &lt;= 4, x1 &lt;= 2 and x2 &lt;= 3",
        "true, 2, 3, [[1,1,'le',4,'people'],[1,0,'le',2,'x1 cap'],[0,1,'le',3,'x2 cap']], 0, 4, 0, 4",
    ),
}


def _lattice(cfg):
    name, (label, spec) = _preset(cfg, "lattice", _LATTICE, "far")

    markup = (
        _toolbar(
            "The lattice and the relaxation",
            "the integer optimum is not the rounded one, and it need not be anywhere near it",
            [("cyan", "the relaxed region"), ("green", "integer points"),
             ("amber", "the relaxation"), ("red", "its roundings"), ("purple", "the integer optimum")],
        )
        + _stage(_svg("ltGrid", "0 0 520 300",
                      "Every integer point of the region, the relaxation's optimum, its roundings and the integer optimum."))
        + _table("ltTable")
        + _banner("ltStatus")
    )
    controls = (
        _select("ltPreset", "Instance",
                [("far", "the integer optimum at the far end"),
                 ("rounddown", "rounding down is infeasible"),
                 ("integral", "a relaxation that lands integral by itself")], name)
        + _range("ltShift", "Move the first row's right-hand side", -3, 3, 0)
        + _select("ltShow", "Draw",
                  [("all", "every lattice point"), ("feasible", "only the feasible ones")], "all")
        + _kpis([
            ("The relaxation, z_LP", "ltZlp"),
            ("The integer optimum, z_IP", "ltZip"),
            ("The gap it leaves", "ltGap"),
            ("Best feasible rounding", "ltBest"),
            ("Roundings that are feasible", "ltFeas"),
            ("Integer points in the region", "ltCount"),
        ])
        + _hint("ltHint",
                "Every figure here is the exact fraction. The relaxation is solved by the same "
                "simplex the earlier courses used; the integer optimum is found by testing every "
                "lattice point in the box, which is honest at this size and hopeless at any other.")
    )

    script = _MODE_JS["lattice"] + r"""
  var SPEC = { far: [""" + _LATTICE["far"][1] + r"""],
               rounddown: [""" + _LATTICE["rounddown"][1] + r"""],
               integral: [""" + _LATTICE["integral"][1] + r"""] };
  var preSel = document.getElementById('ltPreset'), shiftS = document.getElementById('ltShift');
  var showSel = document.getElementById('ltShow'), grid = document.getElementById('ltGrid');
  var table = document.getElementById('ltTable'), status = document.getElementById('ltStatus');

  function build() {
    var p = SPEC[preSel.value], shift = +shiftS.value;
    var rows = p[3].map(function (r, i) { return i === 0 ? [r[0], r[1], r[2], r[3] + shift, r[4]] : r.slice(); });
    document.getElementById('ltShiftOut').textContent = (shift >= 0 ? '+' : '') + shift;
    return { model: ipTwoVar(p[0], p[1], p[2], rows),
             box: [[BigInt(p[4]), BigInt(p[5])], [BigInt(p[6]), BigInt(p[7])]],
             view: [[p[4], p[5]], [p[6], p[7]]] };
  }

  function redraw() {
    var b = build(), model = b.model, maximise = model.max !== false;
    var lp = lpSolve(model);
    var lat = latticePoints(model, b.box);
    var best = lat.best;
    var rows = '', marks = [], feasRoundings = 0, bestRound = null;

    if (lp.status === 'optimal') {
      marks.push({ x: lp.x[0], y: lp.x[1], tone: 'amber', shape: 'cross', label: 'LP' });
      var rr = ipRoundings(lp.x);
      for (var i = 0; i < rr.length; i += 1) {
        var pt = rr[i].pt, bad = ipViolated(model, pt), obj = ipObjective(model, pt);
        if (!bad) {
          feasRoundings += 1;
          if (bestRound === null || (maximise ? Rcmp(obj, bestRound) > 0 : Rcmp(obj, bestRound) < 0)) bestRound = obj;
        }
        marks.push({ x: pt[0], y: pt[1], tone: bad ? 'red' : 'amber', shape: 'square' });
        rows += ipTr([ipTd('(' + Rtext(pt[0]) + ', ' + Rtext(pt[1]) + ')'),
                      ipTd(rr[i].how.join(' / ')),
                      ipTd(bad ? ipChip('infeasible', 'no') : ipChip('feasible', 'ok')),
                      ipTdl(bad ? 'it breaks ' + bad : 'objective ' + Rtext(obj))]);
      }
    }
    if (best) marks.push({ x: best.x[0], y: best.x[1], tone: 'purple', label: 'integer best' });

    var pts = lat.points;
    if (showSel.value === 'feasible') pts = pts.filter(function (q) { return q.feasible; });
    grid.innerHTML = ipLattice({
      cons: ipHalfPlanes(model), box: b.view, points: pts, marks: marks,
      width: 520, height: 300, names: model.names,
      note: 'every dot is a whole-number plan; the filled ones satisfy every row'
    });

    table.innerHTML = ipHead(['rounding of the relaxation', 'how', 'verdict', 'why'])
      + '<tbody>' + (rows || ipTr([ipTdl('the relaxation has no optimum to round')])) + '</tbody>';

    var zlp = lp.status === 'optimal' ? lp.zOrig : null;
    document.getElementById('ltZlp').textContent = zlp === null ? lp.status : Rtext(zlp);
    document.getElementById('ltZip').textContent = best ? Rtext(best.objective) : 'no integer point';
    document.getElementById('ltGap').textContent = (zlp !== null && best) ? Rtext(Rabs(Rsub(zlp, best.objective))) : '—';
    document.getElementById('ltBest').textContent = bestRound === null ? 'none is feasible' : Rtext(bestRound);
    document.getElementById('ltFeas').textContent = feasRoundings + ' of ' + (lp.status === 'optimal' ? ipRoundings(lp.x).length : 0);
    document.getElementById('ltCount').textContent = String(lat.feasibleCount);

    if (lp.status !== 'optimal' || !best) {
      status.innerHTML = 'This instance has no optimum to compare: the relaxation says <strong>'
        + ipEsc(lp.status) + '</strong> and the enumeration found '
        + (best ? 'an integer point' : '<strong>no feasible integer point at all</strong>')
        + '. Move the right-hand side back.';
      return;
    }
    var slack = Rabs(Rsub(zlp, best.objective));
    var far = Rabs(Rsub(best.x[0], lp.x[0])), far2 = Rabs(Rsub(best.x[1], lp.x[1]));
    var all = ipRoundings(lp.x), whole = Rint(lp.x[0]) && Rint(lp.x[1]);
    var isRounding = false;
    for (var q = 0; q < all.length; q += 1) {
      if (Requ(all[q].pt[0], best.x[0]) && Requ(all[q].pt[1], best.x[1])) isRounding = true;
    }
    status.innerHTML = 'The relaxation stops at <strong>' + Rtext(zlp) + '</strong> at ('
      + Rtext(lp.x[0]) + ', ' + Rtext(lp.x[1]) + ')'
      + (whole ? ', which is already a whole-number plan &mdash; there is nothing to round. '
               : ', which no whole-number plan can do. ')
      + (whole ? ''
          : (feasRoundings === 0
              ? 'Not one of its ' + all.length + ' roundings is even feasible: rounding a corner off the region '
                + 'does not land in it. '
              : 'Of its ' + all.length + ' roundings, ' + (all.length - feasRoundings)
                + (all.length - feasRoundings === 1 ? ' is infeasible' : ' are infeasible')
                + ' and the best of the rest is worth <strong>' + Rtext(bestRound) + '</strong>. '))
      + 'The best whole-number plan is <strong>' + Rtext(best.objective) + '</strong> at ('
      + Rtext(best.x[0]) + ', ' + Rtext(best.x[1]) + ') &mdash; '
      + (Rzero(slack)
          ? 'the same number. That happens, and it is worth noticing rather than assuming: this relaxation '
            + 'landed on a whole corner by itself, and only a check can tell you so.'
          : Rtext(far) + ' and ' + Rtext(far2) + ' away from the relaxation in the two coordinates, so the gap of '
            + Rtext(slack) + ' is not a rounding error. '
            + (isRounding
                ? 'On this instance it happens to be one of the roundings &mdash; but which one, only the check '
                  + 'told you, and the instance next door has its answer nowhere near them.'
                : 'It is a different point, and no amount of rounding reaches it.'));
  }

  [preSel, showSel].forEach(function (el) { el.addEventListener('change', redraw); });
  shiftS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Rounding is not an answer",
        subtitle="The relaxation bounds the integer optimum; the rounded point is a different object",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Solve it, round it, then look at every whole-number plan"),
        panel_intro=cfg.get(
            "panel_intro",
            "The relaxation is solved exactly, each rounding of its optimum is tested against every "
            "row, and the best whole-number plan is found by trying all of them. On this instance: "
            + label + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# logic -- binary variables and logical constraints
# ---------------------------------------------------------------------------

# (condition in the parser's syntax, what it says in words, the encoding that
# is right, the encoding readers reach for instead). The wrong column is not
# decoration: a reader who has seen the ROW that refutes it does not make the
# mistake again, and a mode that could only show right answers could not show
# that row at all.
_CONDITIONS = {
    "ifthen": ("A -> B", "if project A is chosen then project B must be too",
               "yA - yB <= 0", "yB - yA <= 0"),
    "atmost": ("!(A & B & C)", "at most two of the three projects",
               "yA + yB + yC <= 2", "yA + yB + yC <= 3"),
    "either": ("A | B", "at least one of A and B",
               "yA + yB >= 1", "yA + yB <= 1"),
    "exactly": ("(A & !B & !C) | (!A & B & !C) | (!A & !B & C)",
                "exactly one of the three",
                "yA + yB + yC = 1", "yA + yB + yC <= 1"),
    "both": ("A & B", "both A and B",
             "yA + yB >= 2", "yA + yB >= 1"),
}


def _js_conditions():
    """The condition table as a JS literal, so the page has the data the panel
    describes and not a transcription of it."""
    import json
    return json.dumps({
        k: {"cond": v[0], "words": v[1], "right": v[2], "wrong": v[3]}
        for k, v in _CONDITIONS.items()
    }).replace("</", "<\\/")


def _logic(cfg):
    name, (cond, words, right, wrong) = _preset(cfg, "logic", _CONDITIONS, "ifthen")

    markup = (
        _toolbar(
            "An encoding, checked",
            "an inequality either agrees with the condition on every assignment or it is refuted by one",
            [("green", "the two agree"), ("red", "they disagree"),
             ("cyan", "the condition holds"), ("muted", "it does not")],
        )
        + _stage(_svg("lgGrid", "0 0 520 190",
                      "The condition and the inequality on every 0/1 assignment, with the rows where they disagree marked."))
        + _table("lgTable")
        + _banner("lgStatus")
    )
    controls = (
        _select("lgCond", "The condition",
                [(k, _CONDITIONS[k][1]) for k in sorted(_CONDITIONS)], name)
        + _select("lgTry", "The inequality to test",
                  [("right", "the encoding that is right"),
                   ("wrong", "the one readers reach for"),
                   ("typed", "whatever is typed below")], "right")
        + _text("lgIneq", "Inequality on the binaries", right)
        + _kpis([
            ("Assignments checked", "lgRows"),
            ("Rows where they agree", "lgAgree"),
            ("Rows that refute it", "lgBad"),
            ("The first refuting row", "lgWitness"),
            ("Verdict", "lgVerdict"),
        ])
        + _hint("lgHint",
                "Type any linear inequality on yA, yB and yC &mdash; coefficients may be "
                "fractions. It is evaluated on all eight assignments beside the condition, and "
                "a disagreement is a refutation: one row is enough, and an argument is not.")
    )

    script = _MODE_JS["logic"] + r"""
  var COND = """ + _js_conditions() + r""";
  var condSel = document.getElementById('lgCond'), trySel = document.getElementById('lgTry');
  var box = document.getElementById('lgIneq'), grid = document.getElementById('lgGrid');
  var table = document.getElementById('lgTable'), status = document.getElementById('lgStatus');
  var NAMES = ['A', 'B', 'C'];

  function redraw() {
    var spec = COND[condSel.value];
    if (trySel.value !== 'typed') box.value = trySel.value === 'right' ? spec.right : spec.wrong;
    var res = ipEncodingCheck(spec.cond, box.value, NAMES);
    if (res.error) {
      grid.innerHTML = '';
      table.innerHTML = '';
      ['lgRows', 'lgAgree', 'lgBad', 'lgWitness'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      document.getElementById('lgVerdict').textContent = 'unreadable';
      status.innerHTML = 'That is not an inequality this page can read: <strong>' + res.error
        + '</strong>. The variables are yA, yB and yC, and the relation is one of &lt;=, &gt;= or =.';
      return;
    }

    var rows = '', cells = '', i, w = 520, cw = w / res.rows.length;
    for (i = 0; i < res.rows.length; i += 1) {
      var r = res.rows[i], bits = r.bits.join('');
      rows += ipTr([ipTd(bits.split('').join(' ')),
                    ipTd(r.condition ? ipChip('holds', 'hi') : ipChip('fails', 'no')),
                    ipTd(Rtext(r.value) + ' ' + (res.ineq.rel === '<=' ? '&lt;=' : (res.ineq.rel === '>=' ? '&gt;=' : '=')) + ' ' + Rtext(res.ineq.b)),
                    ipTd(r.inequality ? ipChip('holds', 'hi') : ipChip('fails', 'no')),
                    ipTdl(r.agree ? 'they agree' : 'REFUTED: the condition ' + (r.condition ? 'holds' : 'does not') + ' and the inequality ' + (r.inequality ? 'does' : 'does not'))],
                   r.agree ? null : 'tone-red');
      var x = i * cw;
      cells += ipEl('rect', { x: x + 1, y: 30, width: cw - 2, height: 34, rx: 2,
                              fill: 'var(--' + (r.condition ? 'cyan' : 'muted') + ')',
                              'fill-opacity': r.condition ? '0.5' : '0.16' });
      cells += ipEl('rect', { x: x + 1, y: 74, width: cw - 2, height: 34, rx: 2,
                              fill: 'var(--' + (r.inequality ? 'cyan' : 'muted') + ')',
                              'fill-opacity': r.inequality ? '0.5' : '0.16' });
      cells += ipEl('rect', { x: x + 1, y: 118, width: cw - 2, height: 12, rx: 2,
                              fill: 'var(--' + (r.agree ? 'green' : 'red') + ')', 'fill-opacity': '0.85' });
      cells += ipLabel(x + cw / 2, 145, bits, r.agree ? 'muted' : 'red', 'middle', 9);
    }
    grid.innerHTML = ipLabel(0, 14, 'the condition: ' + ipEsc(spec.words), 'text', 'start', 11)
      + cells
      + ipLabel(0, 24, '', 'muted', 'start', 9)
      + ipLabel(0, 162, 'top band: the condition. middle: the inequality. bottom: do they agree. '
                + 'Each column is one assignment of yA yB yC.', 'muted', 'start', 9)
      + ipLabel(0, 176, 'the inequality: ' + ipIneqText(res.ineq), 'text', 'start', 10);

    table.innerHTML = ipHead(['yA yB yC', 'the condition', 'the inequality evaluates to', 'it holds', 'verdict'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('lgRows').textContent = String(res.rows.length);
    document.getElementById('lgAgree').textContent = (res.rows.length - res.disagree.length) + ' of ' + res.rows.length;
    document.getElementById('lgBad').textContent = String(res.disagree.length);
    document.getElementById('lgWitness').textContent = res.witness ? res.witness.bits.join(' ') : 'there is none';
    document.getElementById('lgVerdict').textContent = res.valid ? 'it encodes the condition' : 'it does not';

    status.innerHTML = res.valid
      ? 'On all ' + res.rows.length + ' assignments <strong>' + ipIneqText(res.ineq)
        + '</strong> holds exactly when &ldquo;' + ipEsc(spec.words) + '&rdquo; does, so it encodes the '
        + 'condition. That is a check, not an opinion: every assignment was tried.'
      : 'Refuted. At <strong>yA yB yC = ' + res.witness.bits.join(' ') + '</strong> the condition '
        + (res.witness.condition ? 'HOLDS' : 'FAILS') + ' and the inequality '
        + (res.witness.inequality ? 'HOLDS' : 'FAILS')
        + ', so <strong>' + ipIneqText(res.ineq) + '</strong> does not encode &ldquo;'
        + ipEsc(spec.words) + '&rdquo;. One row settles it; there '
        + (res.disagree.length === 1 ? 'is one such row' : 'are ' + res.disagree.length + ' such rows') + '.';
  }

  [condSel, trySel].forEach(function (el) { el.addEventListener('change', redraw); });
  box.addEventListener('input', function () { trySel.value = 'typed'; redraw(); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Logic as inequalities",
        subtitle="An encoding is checked on every assignment, and a wrong one is refuted by a row",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick a condition, then test an inequality against it"),
        panel_intro=cfg.get(
            "panel_intro",
            "The condition is evaluated on every assignment of the binaries and so is the "
            "inequality; the rows where they disagree are marked. This one says: " + words + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# knapsack -- the two atoms of binary modelling
# ---------------------------------------------------------------------------

# Both atoms live in one mode because the lesson is the pair: one capacity with
# chosen items, and every requirement covered by at least one chosen set. The
# covering instance ships with the `= 1` partitioning variant that turns it
# infeasible, because "covering and partitioning are the same problem stated
# twice" is the misconception and an instance is the only honest refutation.
_KNAPSACKS = {
    "classic": ("60,10; 100,20; 120,30", 50,
                "three items where greed, the relaxation and the optimum are three different numbers"),
    "split": ("9,6; 11,1; 9,3; 19,7; 5,3; 17,5", 14,
              "six items, where the relaxation, greed and the optimum are three different numbers"),
    "dense": ("7,3; 7,3; 7,3; 7,3; 20,10; 20,10; 3,1", 14,
              "ties in the density order, which is where the value-per-weight rule stops deciding"),
}

_COVERS = {
    "cycle": ("1,1,0,0,0; 0,1,1,0,0; 0,0,1,1,0; 0,0,0,1,1; 1,0,0,0,1", "2,2,2,2,2",
              "five regions in a ring, each reachable from two depots"),
    "depots": ("1,1,0,0; 0,1,1,0; 1,0,1,0; 0,0,1,1; 1,0,0,1", "5,4,3,6",
               "four depots whose relaxation happens to land whole"),
    "odd": ("1,1,0; 0,1,1; 1,0,1", "2,2,2",
            "three sets, pairwise overlapping, the smallest ring there is"),
}


def _js_map(table, keys):
    """A preset table as a JS literal, keyed the way the script reads it."""
    import json
    return json.dumps({
        name: {k: v for k, v in zip(keys, values)} for name, values in table.items()
    }).replace("</", "<\\/")


def _knapsack(cfg):
    name, (items, cap, blurb) = _preset(cfg, "knapsack", _KNAPSACKS, "classic")
    cover_name = cfg.get("cover", "cycle")
    if cover_name not in _COVERS:
        raise ValueError("integer_lab: mode 'knapsack' has no covering preset %r; they are %s"
                         % (cover_name, ", ".join(sorted(_COVERS))))
    inc, costs, _ = _COVERS[cover_name]

    markup = (
        _toolbar(
            "One capacity, three answers",
            "a relaxation is a bound, greed is a guess, and only one of the three is the optimum",
            [("amber", "the relaxation"), ("cyan", "greed"), ("green", "the exact optimum")],
        )
        + _stage(_svg("knBars", "0 0 660 130",
                      "The relaxation, the greedy answer and the exact optimum drawn against each other."))
        + _table("knTable")
        + _banner("knStatus")
    )
    controls = (
        _select("knView", "Model",
                [("knapsack", "one capacity, chosen items"),
                 ("cover", "every requirement covered by a chosen set")], "knapsack")
        + _select("knPreset", "Knapsack instance",
                  [(k, _KNAPSACKS[k][2]) for k in sorted(_KNAPSACKS)], name)
        + _range("knCap", "Capacity", 1, 60, cap)
        + _text("knItems", "Items as value,weight pairs", items)
        + _select("knCover", "Covering instance",
                  [(k, _COVERS[k][2]) for k in sorted(_COVERS)], cover_name)
        + _select("knRel", "Each requirement must be covered",
                  [("ge", "at least once"), ("eq", "exactly once")], "ge")
        + _kpis([
            ("The relaxation, a bound", "knLp"),
            ("What greed gets", "knGreedy"),
            ("The exact optimum", "knOpt"),
            ("Gap the relaxation leaves", "knGapLp"),
            ("Gap greed leaves", "knGapGreedy"),
            ("Subsets enumerated", "knCount"),
        ])
        + _hint("knHint",
                "Edit the items as value,weight pairs separated by semicolons, or the incidence "
                "rows as 0/1 lists. The relaxation, greed and the exact optimum are all recomputed "
                "from what is typed; nothing here is a stored answer.")
    )

    script = _MODE_JS["knapsack"] + r"""
  var viewSel = document.getElementById('knView'), preSel = document.getElementById('knPreset');
  var capS = document.getElementById('knCap'), itemBox = document.getElementById('knItems');
  var coverSel = document.getElementById('knCover'), relSel = document.getElementById('knRel');
  var bars = document.getElementById('knBars'), table = document.getElementById('knTable');
  var status = document.getElementById('knStatus');
  var KNAP = """ + _js_map(_KNAPSACKS, ("items", "cap", "words")) + r""";
  var COVER = """ + _js_map(_COVERS, ("inc", "cost", "words")) + r""";
  var lastPreset = null, lastCover = null;

  function readItems(text) {
    var out = [], bits = String(text).split(';'), i;
    for (i = 0; i < bits.length; i += 1) {
      var t = bits[i].trim();
      if (!t) continue;
      var pair = t.split(',');
      if (pair.length !== 2) return { error: 'each item is value,weight &mdash; ' + ipEsc(t) + ' is not' };
      var v = ipRead(pair[0]), w = ipRead(pair[1]);
      if (v === null || w === null || Rsign(w) <= 0) return { error: 'item ' + (i + 1) + ' has no readable value and positive weight' };
      out.push({ name: 'item ' + (i + 1), value: v, weight: w });
    }
    if (!out.length) return { error: 'there are no items to choose from' };
    if (out.length > 12) return { error: 'this enumerates every subset and stops at twelve items, which is 4096 of them' };
    return { items: out };
  }

  function readInc(text) {
    var rows = String(text).split(';'), out = [], i, j;
    for (i = 0; i < rows.length; i += 1) {
      var t = rows[i].trim();
      if (!t) continue;
      var cells = t.split(',').map(function (c) { return c.trim() === '1' ? 1 : 0; });
      out.push(cells);
    }
    if (!out.length) return null;
    for (i = 1; i < out.length; i += 1) if (out[i].length !== out[0].length) return null;
    return out;
  }

  function drawKnapsack() {
    if (preSel.value !== lastPreset) {
      lastPreset = preSel.value;
      itemBox.value = KNAP[preSel.value].items;
      capS.value = KNAP[preSel.value].cap;
    }
    document.getElementById('knCapOut').textContent = capS.value;
    var parsed = readItems(itemBox.value);
    if (parsed.error) {
      bars.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'Nothing to solve: <strong>' + parsed.error + '</strong>.';
      return null;
    }
    var cap = R(BigInt(+capS.value), 1n), k = knapsackExact(parsed.items, cap);
    var drawn = ipBars([
      { label: 'relaxation', value: k.relaxation, tone: 'amber' },
      { label: 'greed', value: k.greedy, tone: 'cyan' },
      { label: 'exact optimum', value: k.optimum, tone: 'green' }], { width: 660 });
    bars.innerHTML = drawn.svg;

    var rows = '', i;
    for (i = 0; i < k.ratios.length; i += 1) {
      var it = parsed.items[k.ratios[i].item];
      var inRelax = k.take.filter(function (t) { return t.item === k.ratios[i].item; })[0];
      var split = k.fractionalItem && k.fractionalItem.item === k.ratios[i].item;
      rows += ipTr([ipTd('item ' + (k.ratios[i].item + 1)), ipTd(Rtext(it.value)), ipTd(Rtext(it.weight)),
                    ipTd(Rshort(k.ratios[i].ratio, 3)),
                    ipTd(inRelax ? (split ? ipChip(Rtext(inRelax.part) + ' of it', 'hi') : ipChip('all of it', 'ok')) : ipChip('none', null)),
                    ipTd(k.greedySet.indexOf(k.ratios[i].item) >= 0 ? ipChip('taken', 'ok') : ipChip('left', null)),
                    ipTd(k.subset.indexOf(k.ratios[i].item) >= 0 ? ipChip('taken', 'ok') : ipChip('left', null))]);
    }
    table.innerHTML = ipHead(['in density order', 'value', 'weight', 'value per weight',
                              'the relaxation takes', 'greed takes', 'the optimum takes'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('knLp').textContent = Rshort(k.relaxation, 3);
    document.getElementById('knGreedy').textContent = Rtext(k.greedy);
    document.getElementById('knOpt').textContent = Rtext(k.optimum);
    document.getElementById('knGapLp').textContent = Rshort(Rsub(k.relaxation, k.optimum), 3);
    document.getElementById('knGapGreedy').textContent = Rtext(Rsub(k.optimum, k.greedy));
    document.getElementById('knCount').textContent = k.exhaustive ? group(String(k.count)) : 'too many';

    status.innerHTML = 'The relaxation is worth <strong>' + Rshort(k.relaxation, 3) + '</strong> and '
      + (k.fractionalItem
          ? 'gets there by splitting <strong>item ' + (k.fractionalItem.item + 1) + '</strong> &mdash; it takes '
            + Rtext(k.fractionalItem.part) + ' of it, which no reader can do. '
          : 'happens to be integral here, so on this instance it is not merely a bound. ')
      + 'Greed by value per weight gets <strong>' + Rtext(k.greedy) + '</strong>; the best whole choice is <strong>'
      + Rtext(k.optimum) + '</strong>, found by trying all ' + group(String(k.count)) + ' subsets. '
      + 'The order ' + Rshort(k.relaxation, 3) + ' &gt;= ' + Rtext(k.optimum) + ' &gt;= ' + Rtext(k.greedy)
      + ' is the point: the first is a bound and the last is a guess.';
    return k;
  }

  function drawCover() {
    if (coverSel.value !== lastCover) { lastCover = coverSel.value; }
    var spec = COVER[coverSel.value];
    var inc = readInc(spec.inc), cost = spec.cost.split(',').map(function (c) { return ipRead(c.trim()); });
    var rel = relSel.value;
    var relaxed = lpSolve(ipCoverModel(inc, cost, rel));
    var greedy = ipCoverGreedy(inc, cost);
    var exact = ipCoverExact(inc, cost, rel);
    var lp = relaxed.status === 'optimal' ? relaxed.zOrig : null;

    var items = [];
    if (lp !== null) items.push({ label: 'relaxation', value: lp, tone: 'amber', text: Rshort(lp, 3) });
    if (greedy.feasible && rel === 'ge') items.push({ label: 'greed', value: greedy.value, tone: 'cyan' });
    if (exact.value !== null) items.push({ label: 'exact optimum', value: exact.value, tone: 'green' });
    bars.innerHTML = items.length ? ipBars(items, { width: 660 }).svg
      : ipLabel(10, 40, 'there is nothing to draw: this instance has no feasible choice of sets at all', 'red', 'start', 12);

    var rows = '', i, j;
    for (i = 0; i < inc.length; i += 1) {
      var cells = [ipTd('requirement ' + (i + 1))];
      for (j = 0; j < cost.length; j += 1) cells.push(ipTd(inc[i][j] ? ipChip('covers', 'hi') : '&middot;'));
      rows += ipTr(cells);
    }
    var costRow = [ipTd('cost')];
    for (j = 0; j < cost.length; j += 1) {
      costRow.push(ipTd(Rtext(cost[j]) + (relaxed.status === 'optimal' ? ' &middot; ' + Rtext(relaxed.x[j]) : '')));
    }
    rows += ipTr(costRow);
    var heads = ['requirement'];
    for (j = 0; j < cost.length; j += 1) heads.push('set ' + (j + 1));
    table.innerHTML = ipHead(heads) + '<tbody>' + rows + '</tbody>';

    document.getElementById('knLp').textContent = lp === null ? relaxed.status : Rshort(lp, 3);
    document.getElementById('knGreedy').textContent = greedy.feasible ? Rtext(greedy.value) : 'greed cannot finish';
    document.getElementById('knOpt').textContent = exact.value === null ? 'no feasible choice' : Rtext(exact.value);
    document.getElementById('knGapLp').textContent = (lp !== null && exact.value !== null) ? Rshort(Rsub(exact.value, lp), 3) : '—';
    document.getElementById('knGapGreedy').textContent = (greedy.feasible && exact.value !== null) ? Rtext(Rsub(greedy.value, exact.value)) : '—';
    document.getElementById('knCount').textContent = group(String(exact.count));

    var frac = [];
    if (relaxed.status === 'optimal') {
      for (j = 0; j < cost.length; j += 1) if (!Rint(relaxed.x[j])) frac.push('set ' + (j + 1) + ' at ' + Rtext(relaxed.x[j]));
    }
    status.innerHTML = (rel === 'eq' ? 'Covered <strong>exactly once</strong>: ' : 'Covered <strong>at least once</strong>: ')
      + (exact.value === null
          ? 'there is <strong>no feasible choice of sets at all</strong>, and the instance did not change &mdash; only the relation did. '
            + 'Covering and partitioning are not the same problem stated twice.'
          : 'the cheapest choice costs <strong>' + Rtext(exact.value) + '</strong>, of ' + exact.feasibleCount
            + ' feasible choices among ' + group(String(exact.count)) + ' subsets. '
            + (lp === null ? 'The relaxation has no optimum here. '
                : 'The relaxation stops at <strong>' + Rshort(lp, 3) + '</strong>'
                  + (frac.length ? ', spreading halves across ' + frac.join(', ') + ' &mdash; which is the shape of a covering relaxation'
                                 : ', integral on this instance') + '. ')
            + (greedy.feasible && rel === 'ge'
                ? 'Greed on cost per newly covered requirement pays ' + Rtext(greedy.value) + '.' : ''));
  }

  function redraw() {
    var cover = viewSel.value === 'cover';
    document.getElementById('knPreset').disabled = cover;
    document.getElementById('knCap').disabled = cover;
    document.getElementById('knItems').disabled = cover;
    document.getElementById('knCover').disabled = !cover;
    document.getElementById('knRel').disabled = !cover;
    if (cover) drawCover(); else drawKnapsack();
  }

  [viewSel, preSel, coverSel, relSel].forEach(function (el) { el.addEventListener('change', redraw); });
  capS.addEventListener('input', redraw);
  itemBox.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Knapsack and set covering",
        subtitle="Two atoms of binary modelling, and the characteristic shape of each relaxation",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the instance; the bound, the guess and the optimum all move"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every number is recomputed from the items or the incidence rows as typed: the "
            "relaxation by simplex, greed by the density rule, the optimum by enumerating every "
            "subset. This knapsack is " + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# tsp -- the travelling salesman at lesson size
# ---------------------------------------------------------------------------

# SEVEN CITIES IS THIS LAB'S OWN CAP, and the reason is a count rather than a
# feeling: the distinct undirected tours on n cities with a fixed start number
# (n-1)!/2, which is 360 at seven and 2 520 at eight. 360 redraw instantly.
# The Discrete Mathematics graph lab's Hamilton cap of eight is about 8! = 40
# 320 PERMUTATIONS, a different quantity, and the two caps are unrelated.
_TSP = {
    "plants": ("0,32,40,32,8,40,32; 32,0,24,16,32,24,32; 40,24,0,16,8,16,40; "
               "32,16,16,0,40,8,24; 8,32,8,40,0,16,32; 40,24,16,8,16,0,8; "
               "32,32,40,24,32,8,0",
               "symmetric, with a loose assignment bound and a heuristic that misses"),
    "clustered": ("0,3,93,13,33,9,20; 4,0,77,42,21,16,30; 45,17,0,36,16,28,50; "
                  "39,90,80,0,56,7,44; 28,46,88,33,0,25,17; 3,88,18,46,92,0,11; "
                  "22,35,41,19,27,14,0",
                  "an asymmetric instance, where a tour and its reversal are different tours"),
    "metric": ("0,10,15,20,25,30,35; 10,0,35,25,20,15,30; 15,35,0,30,10,25,20; "
               "20,25,30,0,15,35,10; 25,20,10,15,0,30,15; 30,15,25,35,30,0,20; "
               "35,30,20,10,15,20,0",
               "a symmetric instance where nearest neighbour happens to do well"),
}


def _tsp(cfg):
    name, (matrix, blurb) = _preset(cfg, "tsp", _TSP, "plants")

    markup = (
        _toolbar(
            "Every tour, and a bound instead",
            "the assignment relaxation drops the one-cycle rule, and the subtours it leaves are the branching",
            [("green", "the optimal tour"), ("amber", "the heuristic tour"),
             ("cyan", "a node still open"), ("red", "closed by the bound")],
        )
        + _stage(_svg("tsRing", "0 0 660 260",
                      "The cities with the optimal tour and the heuristic tour drawn over them."))
        + _stage(_svg("tsTree", "0 0 660 200",
                      "The branch and bound tree, each node carrying its assignment bound and the subtour it cut."))
        + _table("tsTable")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Instance", [(k, _TSP[k][1]) for k in sorted(_TSP)], name)
        + _range("tsN", "Cities", 4, 7, 6)
        + _select("tsHeur", "Heuristic tour",
                  [("twoopt", "nearest neighbour, then 2-opt"),
                   ("nearest", "nearest neighbour alone")], "twoopt")
        + _text("tsCost", "Cost matrix, rows separated by semicolons", matrix)
        + _kpis([
            ("Distinct tours at this size", "tsCount"),
            ("The optimum, by enumeration", "tsOpt"),
            ("The assignment bound at the root", "tsRoot"),
            ("Nodes the tree explored", "tsNodes"),
            ("The heuristic tour costs", "tsHeurCost"),
            ("Its gap, against its own length", "tsGap"),
        ])
        + _hint("tsHint",
                "Distinct undirected tours on n cities with a fixed start number (n &minus; 1)! / 2 "
                "&mdash; which is why this stops at seven cities. Every cost is an integer or a "
                "fraction, so every tour length, bound and gap here is exact.")
    )

    script = _MODE_JS["tsp"] + r"""
  var preSel = document.getElementById('tsPreset'), nS = document.getElementById('tsN');
  var heurSel = document.getElementById('tsHeur'), box = document.getElementById('tsCost');
  var ring = document.getElementById('tsRing'), treeSvg = document.getElementById('tsTree');
  var table = document.getElementById('tsTable'), status = document.getElementById('tsStatus');
  var MATRIX = """ + _js_map(_TSP, ("matrix", "words")) + r""";
  var lastPreset = null;

  function readMatrix(text, n) {
    var rows = String(text).split(';'), out = [], i, j;
    for (i = 0; i < rows.length && out.length < n; i += 1) {
      var t = rows[i].trim();
      if (!t) continue;
      var cells = t.split(','), row = [];
      for (j = 0; j < cells.length && row.length < n; j += 1) {
        var v = ipRead(cells[j]);
        if (v === null) return { error: 'row ' + (i + 1) + ' has an entry this page cannot read' };
        row.push(v);
      }
      if (row.length < n) return { error: 'row ' + (i + 1) + ' is shorter than ' + n + ' cities' };
      out.push(row);
    }
    if (out.length < n) return { error: 'there are fewer than ' + n + ' rows' };
    return { d: out };
  }

  function redraw() {
    if (preSel.value !== lastPreset) { lastPreset = preSel.value; box.value = MATRIX[preSel.value].matrix; }
    var n = +nS.value;
    document.getElementById('tsNOut').textContent = n + ' cities';
    var parsed = readMatrix(box.value, n);
    if (parsed.error) {
      ring.innerHTML = ''; treeSvg.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'The matrix does not read: <strong>' + parsed.error + '</strong>.';
      return;
    }
    var d = parsed.d;
    var exact = tspExact(d, { maxCities: 7 });
    var counts = ipTourCount(n, exact.symmetric);
    var branch = tspBranch(d, { maxNodes: 60 });
    var heur = heurSel.value === 'nearest' ? ipNearest(d) : ipTwoOpt(d);

    var tours = [];
    if (heur.tour) tours.push({ tour: heur.tour, tone: 'amber', dashed: true, faint: true, width: 2 });
    if (exact.best) tours.push({ tour: exact.best.tour, tone: 'green', width: 2.4 });
    ring.innerHTML = ipTourSvg(n, tours, { width: 660, height: 260 }).svg;

    var drawn = ipTreeSvg(branch.nodes, {
      width: 660, rowH: 44,
      tone: function (node) {
        return node.tour ? 'green' : (node.prunedBy === 'bound' ? 'red' : (node.prunedBy === 'infeasible' ? 'muted' : 'cyan'));
      },
      top: function (node) { return Rtext(node.bound); },
      bottom: function (node) {
        return node.tour ? 'a tour' : (node.prunedBy === 'bound' ? 'cut off by the bound'
          : (node.cut ? node.cut.length + '-city subtour' : (node.prunedBy || '')));
      }
    });
    treeSvg.innerHTML = drawn.svg;

    var rows = '', i;
    for (i = 0; i < branch.nodes.length && i < 14; i += 1) {
      var nd = branch.nodes[i];
      rows += ipTr([ipTd(String(nd.id)), ipTd(nd.parent === null ? 'root' : String(nd.parent)),
                    ipTd(ipEsc(nd.label)), ipTd(Rtext(nd.bound)),
                    ipTd(nd.cycles.length === 1 ? ipChip('one cycle: a tour', 'ok')
                         : nd.cycles.map(function (c) { return c.length; }).join(' + ') + ' cities'),
                    ipTdl(nd.prunedBy || 'branched on its shortest subtour')]);
    }
    table.innerHTML = ipHead(['node', 'parent', 'what it forbids', 'assignment bound',
                              'the relaxation gives', 'what happened'])
      + '<tbody>' + rows + '</tbody>';

    var root = branch.nodes.length ? branch.nodes[0].bound : null;
    var gap = exact.best ? ipGap(exact.best.cost, heur.cost, false) : { abs: null, rel: null, proved: '' };
    document.getElementById('tsCount').textContent = group(String(counts.tours)) + ' distinct';
    document.getElementById('tsOpt').textContent = exact.best ? Rtext(exact.best.cost) : 'too many to enumerate';
    document.getElementById('tsRoot').textContent = root === null ? '—' : Rtext(root);
    document.getElementById('tsNodes').textContent = String(branch.counts.explored);
    document.getElementById('tsHeurCost').textContent = Rtext(heur.cost);
    document.getElementById('tsGap').textContent = gap.abs === null ? '—'
      : Rtext(gap.abs) + (gap.rel === null ? '' : ' (' + Rpct(gap.rel, 1) + ')');

    status.innerHTML = 'At <strong>' + n + ' cities</strong> this instance has <strong>'
      + group(String(counts.tours)) + '</strong> distinct tours &mdash; '
      + (counts.symmetric
          ? '(n &minus; 1)! / 2, because the cost from one city to another is the same both ways, so a tour '
            + 'and its reversal are one tour. Not ' + group(String(counts.perms)) + ', which counts permutations '
            + 'of the cities, and not ' + group(String(counts.halfPerms)) + ' or ' + group(String(counts.directed)) + '. '
          : '(n &minus; 1)!, because the costs are not symmetric here and a tour driven backwards is a '
            + 'different tour with a different length. On a symmetric instance the same n gives '
            + group(String(counts.directed / 2n)) + '. ')
      + 'The enumeration found ' + group(String(exact.count)) + ' of them, which is that number, and the best is <strong>'
      + (exact.best ? Rtext(exact.best.cost) : '&mdash;') + '</strong>. '
      + 'Branch and bound reaches the same answer from the assignment relaxation, which starts at <strong>'
      + (root === null ? '&mdash;' : Rtext(root)) + '</strong> and leaves subtours rather than a tour, '
      + 'forbidding one arc of the shortest of them at each branch: <strong>' + branch.counts.explored
      + ' nodes</strong>' + (branch.refused ? ', and it stopped at the node cap rather than claim an unproved optimum' : '')
      + '. The heuristic tour costs <strong>' + Rtext(heur.cost) + '</strong>, so '
      + (gap.abs === null ? 'there is nothing to measure it against yet'
          : (Rzero(gap.abs) ? 'it is optimal on this instance &mdash; which happens, and is worth knowing rather than assuming'
              : 'it is <strong>' + Rtext(gap.abs) + '</strong> worse, a measured ' + Rpct(gap.rel, 1)
                + '. Without a bound, "near-optimal" is a word with nothing behind it.'));
  }

  [preSel, heurSel].forEach(function (el) { el.addEventListener('change', redraw); });
  nS.addEventListener('input', redraw);
  box.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The travelling salesman",
        subtitle="A relaxation that leaves subtours, the cuts that forbid them, and a heuristic with a number attached",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the costs; the bound, the tree and the gap all move"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every distinct tour is enumerated, the assignment relaxation is solved and branched "
            "on its subtours, and a heuristic tour is measured against the result. This instance is "
            + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# bb -- the tree, growing under the reader's choices
# ---------------------------------------------------------------------------

# The tree is NOT held anywhere. `bbTree` is called fresh on every redraw with
# the order, the branching order and the node budget the controls currently
# say, so raising the budget re-derives a larger tree rather than mutating a
# stored one -- which is what makes the second redrawLab() call draw the same
# picture as the first, and what makes the picture grow at all.
_BB = {
    "mixed": ("true, 5, 4, [[6,4,'le',25,'machine hours'],[3,5,'le',22,'inspection']], 0, 5, 0, 5",
              "two rows whose corner is fractional in both variables"),
    "tall": ("true, 3, 2, [[5,4,'le',37,'kiln'],[4,7,'le',43,'glaze']], 0, 8, 0, 7",
             "a relaxation whose corner is only just fractional, so the tree goes deep before it closes"),
    "wide": ("true, 7, 9, [[3,4,'le',22,'fabric'],[5,3,'le',26,'labour']], 0, 6, 0, 6",
             "an objective that keeps several nodes alive at once"),
}


def _bb(cfg):
    name, (spec, blurb) = _preset(cfg, "bb", _BB, "mixed")

    markup = (
        _toolbar(
            "Branch and bound",
            "two children, no integer point lost, and each one re-solved from its parent's tableau",
            [("cyan", "still open"), ("green", "integral, an incumbent"),
             ("red", "closed by the bound"), ("muted", "infeasible"), ("purple", "the node you picked")],
        )
        + _stage(_svg("bbTree", "0 0 660 260",
                      "The search tree, each node showing its bound and why it closed."))
        + _stage(_svg("bbRegion", "0 0 520 280",
                      "The chosen node's sub-region drawn over the lattice of the whole problem."))
        + _table("bbTable")
        + '      <p class="small-copy" id="bbWhy" style="margin:10px 0 0;"></p>\n'
        + _banner("bbStatus")
    )
    controls = (
        _select("bbPreset", "Instance", [(k, _BB[k][1]) for k in sorted(_BB)], name)
        + _select("bbOrder", "Take the next node",
                  [("depthFirst", "depth first: the newest open node"),
                   ("bestBound", "best bound: the most promising open node")], "depthFirst")
        + _select("bbVar", "Branch on",
                  [("first", "the first fractional variable"),
                   ("second", "the second variable first")], "first")
        + _range("bbBudget", "Nodes the tree may explore", 1, 40, 3)
        + _range("bbNode", "Draw the sub-region of node", 0, 39, 0)
        + _kpis([
            ("Nodes explored", "bbNodes"),
            ("The incumbent", "bbInc"),
            ("The global bound", "bbBound"),
            ("The gap, which is what is proved", "bbGap"),
            ("The chosen node's bound", "bbNodeBound"),
            ("Why that node closed", "bbNodeWhy"),
        ])
        + _hint("bbHint",
                "Raise the node budget one at a time and watch the tree grow. Nothing is stored "
                "between redraws: the whole tree is re-derived from the instance and these three "
                "settings, which is why it is the same tree every time you come back to a setting.")
    )

    script = _MODE_JS["bb"] + r"""
  var SPEC = { mixed: [""" + _BB["mixed"][0] + r"""],
               tall: [""" + _BB["tall"][0] + r"""],
               wide: [""" + _BB["wide"][0] + r"""] };
  var preSel = document.getElementById('bbPreset'), orderSel = document.getElementById('bbOrder');
  var varSel = document.getElementById('bbVar'), budS = document.getElementById('bbBudget');
  var nodeS = document.getElementById('bbNode');
  var treeSvg = document.getElementById('bbTree'), regionSvg = document.getElementById('bbRegion');
  var table = document.getElementById('bbTable'), status = document.getElementById('bbStatus');

  function build() {
    var p = SPEC[preSel.value];
    return { model: ipTwoVar(p[0], p[1], p[2], p[3]), view: [[p[4], p[5]], [p[6], p[7]]],
             box: [[BigInt(p[4]), BigInt(p[5])], [BigInt(p[6]), BigInt(p[7])]] };
  }

  function redraw() {
    var b = build(), model = b.model;
    var budget = +budS.value;
    document.getElementById('bbBudgetOut').textContent = budget;
    var tree = bbTree(model, { order: orderSel.value, maxNodes: budget,
                               integers: varSel.value === 'second' ? [1, 0] : [0, 1] });
    var pick = Math.max(0, Math.min(+nodeS.value, tree.nodes.length - 1));
    document.getElementById('bbNodeOut').textContent = tree.nodes.length ? ('node ' + pick) : 'no nodes';

    var drawn = ipTreeSvg(tree.nodes, {
      width: 660, rowH: 46,
      tone: function (node) {
        if (node.id === pick) return 'purple';
        if (node.prunedBy === 'integral') return 'green';
        if (node.prunedBy === 'bound') return 'red';
        if (node.prunedBy === 'infeasible') return 'muted';
        return 'cyan';
      },
      top: function (node) { return node.bound === null ? 'none' : Rshort(node.bound, 2); },
      bottom: function (node) { return node.prunedBy || 'still open'; },
      above: function (node) { return node.depth === 0 ? '' : ipEsc(node.label); }
    });
    treeSvg.innerHTML = drawn.svg;

    var lat = latticePoints(model, b.box);
    var node = tree.nodes[pick] || null;
    var marks = [], lines = [];
    if (node && node.relaxation) {
      marks.push({ x: node.relaxation[0], y: node.relaxation[1], tone: 'amber', shape: 'cross',
                   label: 'this node stops here' });
    }
    if (tree.x) marks.push({ x: tree.x[0], y: tree.x[1], tone: 'green', label: 'incumbent' });
    regionSvg.innerHTML = ipLattice({
      cons: ipHalfPlanes(model),
      overlay: node && node.model ? ipHalfPlanes(node.model) : null,
      box: b.view, points: lat.points, marks: marks, lines: lines,
      width: 520, height: 280, names: model.names,
      note: 'the dashed region is the node you picked; every whole-number plan of the parent is still in one of its children'
    });

    var rows = '', i;
    for (i = 0; i < tree.nodes.length; i += 1) {
      var nd = tree.nodes[i];
      rows += ipTr([ipTd(String(nd.id)), ipTd(nd.parent === null ? 'root' : String(nd.parent)),
                    ipTd(ipEsc(nd.label)),
                    ipTd(nd.bound === null ? 'infeasible' : Rtext(nd.bound)),
                    ipTd(nd.relaxation ? '(' + Rtext(nd.relaxation[0]) + ', ' + Rtext(nd.relaxation[1]) + ')' : '&mdash;'),
                    ipTd(nd.prunedBy ? ipChip(nd.prunedBy, nd.prunedBy === 'integral' ? 'ok' : 'no') : ipChip('open', 'hi')),
                    ipTdl(nd.sol && nd.sol.from ? nd.sol.from : 'the first solve')],
                   nd.id === pick ? 'tone-purple' : null);
    }
    table.innerHTML = ipHead(['node', 'parent', 'the branch that made it', 'its bound',
                              'where its relaxation stops', 'status', 'how it was solved'])
      + '<tbody>' + rows + '</tbody>';

    var openBound = ipOpenBound(tree.nodes, true);
    var global = openBound === null ? tree.best : openBound;
    var gap = ipGap(global, tree.best, true);
    document.getElementById('bbNodes').textContent = String(tree.counts.explored);
    document.getElementById('bbInc').textContent = tree.best === null ? 'none yet' : Rtext(tree.best);
    document.getElementById('bbBound').textContent = global === null ? '—' : Rshort(global, 3);
    document.getElementById('bbGap').textContent = gap.abs === null ? 'nothing yet' : Rshort(gap.abs, 3);
    document.getElementById('bbNodeBound').textContent = node && node.bound !== null ? Rtext(node.bound) : 'infeasible';
    document.getElementById('bbNodeWhy').textContent = node ? (node.prunedBy || 'it is still open') : '—';
    document.getElementById('bbWhy').innerHTML = node && node.branch
      ? node.branch.why
      : (node && node.prunedBy
          ? 'This node was closed because it came back ' + ipEsc(node.prunedBy)
            + ', so there was nothing to split.'
          : 'Pick a node that was branched to see why its two children are the two children.');

    var reasons = { integral: 0, bound: 0, infeasible: 0 };
    for (i = 0; i < tree.nodes.length; i += 1) if (tree.nodes[i].prunedBy) reasons[tree.nodes[i].prunedBy] += 1;
    status.innerHTML = (tree.refused
        ? 'The tree passed its budget of <strong>' + budget + ' nodes</strong> and stopped, saying so rather than '
          + 'reporting an optimum it has not proved. '
        : 'The tree closed in <strong>' + tree.counts.explored + ' nodes</strong>. ')
      + (tree.best === null
          ? 'There is no incumbent yet, so nothing at all is proved. '
          : 'The incumbent is <strong>' + Rtext(tree.best) + '</strong> and '
            + (openBound === null
                ? 'no node is still open, so the bound is the incumbent itself: ' + gap.proved
                : 'the best bound over the nodes still open is <strong>' + Rshort(global, 3)
                  + '</strong>, so ' + gap.proved) + '. ')
      + 'Closed so far: ' + reasons.integral + ' because the relaxation came back whole, '
      + reasons.bound + ' because the bound could not beat the incumbent, and '
      + reasons.infeasible + ' because there was nothing in them. '
      + 'A branch is an inequality and not an assignment &mdash; the child with x &lt;= 2 still permits x = 0 &mdash; '
      + 'which is the only reason no whole-number plan is lost.';
  }

  [preSel, orderSel, varSel].forEach(function (el) { el.addEventListener('change', redraw); });
  [budS, nodeS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The tree, and what closes a node",
        subtitle="Branch on a fractional variable, bound each child, and prune for one of three reasons",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Grow the tree one node at a time"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every node is a linear programme and every child is re-solved from its parent's final "
            "tableau by the dual simplex, which the last column of the table names. This instance has "
            + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# gap -- the incumbent, the bound, and what is actually proved
# ---------------------------------------------------------------------------

_GAP = {
    "slow": ("true, 9, 5, [[7,4,'le',43,'press'],[4,9,'le',47,'anneal']], 0, 7, 0, 6",
             "a bound that comes down slowly, so the gap is visible for several nodes"),
    "early": ("true, 4, 3, [[3,2,'le',17,'weld'],[2,5,'le',23,'paint']], 0, 6, 0, 5",
              "an incumbent found early and proved optimal much later"),
    "even": ("true, 6, 6, [[5,3,'le',28,'cut'],[2,7,'le',31,'sew']], 0, 6, 0, 5",
             "an objective that treats the two variables alike, so the orders separate"),
}


def _gap(cfg):
    name, (spec, blurb) = _preset(cfg, "gap", _GAP, "early")

    markup = (
        _toolbar(
            "The gap is the deliverable",
            "any feasible point bounds one side and any relaxation the other; the space between them is what is proved",
            [("green", "the incumbent"), ("amber", "the global bound"),
             ("purple", "the gap between them"), ("muted", "the other search order")],
        )
        + _stage(_svg("gpPlot", "0 0 660 240",
                      "The incumbent and the global bound drawn against the node index as the tree grows."))
        + _table("gpTable")
        + _banner("gpStatus")
    )
    controls = (
        _select("gpPreset", "Instance", [(k, _GAP[k][1]) for k in sorted(_GAP)], name)
        + _select("gpOrder", "Draw the run that takes",
                  [("depthFirst", "the newest open node, depth first"),
                   ("bestBound", "the most promising open node")], "depthFirst")
        + _range("gpBudget", "Nodes explored so far", 1, 40, 40)
        + _kpis([
            ("The incumbent, a lower bound", "gpInc"),
            ("The global bound, an upper one", "gpBound"),
            ("Absolute gap", "gpAbs"),
            ("Relative gap", "gpRel"),
            ("Nodes, depth first", "gpDf"),
            ("Nodes, best bound", "gpBb"),
        ])
        + _hint("gpHint",
                "A small gap is not a probability. It says nothing beats the incumbent by more than "
                "that much &mdash; a statement about the bound. The incumbent is often optimal long "
                "before the gap closes, and the gap is what has been proved, not what is likely.")
    )

    script = _MODE_JS["gap"] + r"""
  var SPEC = { slow: [""" + _GAP["slow"][0] + r"""],
               early: [""" + _GAP["early"][0] + r"""],
               even: [""" + _GAP["even"][0] + r"""] };
  var preSel = document.getElementById('gpPreset'), orderSel = document.getElementById('gpOrder');
  var budS = document.getElementById('gpBudget');
  var plot = document.getElementById('gpPlot'), table = document.getElementById('gpTable');
  var status = document.getElementById('gpStatus');

  function run(order, budget) {
    var p = SPEC[preSel.value];
    var model = ipTwoVar(p[0], p[1], p[2], p[3]);
    return bbTree(model, { order: order, maxNodes: budget });
  }

  function redraw() {
    var budget = +budS.value;
    document.getElementById('gpBudgetOut').textContent = budget;
    var here = run(orderSel.value, budget);
    var other = run(orderSel.value === 'depthFirst' ? 'bestBound' : 'depthFirst', budget);
    var full = { df: run('depthFirst', 60), bb: run('bestBound', 60) };
    var t = ipBoundTrace(here, true), tOther = ipBoundTrace(other, true);

    var incPts = [], bndPts = [], otherPts = [], i;
    for (i = 0; i < t.length; i += 1) {
      if (t[i].incumbent !== null) incPts.push([t[i].at, ipPx(t[i].incumbent)]);
      if (t[i].bound !== null) bndPts.push([t[i].at, ipPx(t[i].bound)]);
    }
    for (i = 0; i < tOther.length; i += 1) {
      if (tOther[i].bound !== null) otherPts.push([tOther[i].at, ipPx(tOther[i].bound)]);
    }
    var series = [];
    if (otherPts.length) series.push({ pts: otherPts, tone: 'muted', step: true, dashed: true });
    if (bndPts.length) series.push({ pts: bndPts, tone: 'amber', step: true, dots: true });
    if (incPts.length) series.push({ pts: incPts, tone: 'green', step: true, dots: true });
    var drawn = ipPlot(series, { width: 660, height: 240, xLabel: 'nodes explored',
                                 fmtY: function (v) { return v.toFixed(1); },
                                 fmtX: function () { return 'node 0'; } });
    plot.innerHTML = drawn.svg
      + ipLabel(52, 26, 'green: the incumbent. amber: the global bound. dashed: the other search order.', 'muted', 'start', 9);

    var rows = '';
    for (i = 0; i < t.length; i += 1) {
      var g = ipGap(t[i].bound, t[i].incumbent, true);
      rows += ipTr([ipTd(String(t[i].at)),
                    ipTd(t[i].incumbent === null ? 'none yet' : Rtext(t[i].incumbent)),
                    ipTd(t[i].bound === null ? '&mdash;' : Rshort(t[i].bound, 3)),
                    ipTd(g.abs === null ? '&mdash;' : Rshort(g.abs, 3)),
                    ipTd(g.rel === null ? '&mdash;' : Rpct(g.rel, 1)),
                    ipTdl(g.abs === null ? 'nothing is proved yet'
                          : (Rzero(g.abs) ? 'the incumbent is optimal, and that is proved'
                             : 'nothing beats the incumbent by more than ' + Rshort(g.abs, 3)))]);
    }
    table.innerHTML = ipHead(['after node', 'incumbent', 'global bound', 'gap', 'relative', 'what is proved'])
      + '<tbody>' + rows + '</tbody>';

    var last = t.length ? t[t.length - 1] : { incumbent: null, bound: null };
    var gap = ipGap(last.bound, last.incumbent, true);
    document.getElementById('gpInc').textContent = last.incumbent === null ? 'none yet' : Rtext(last.incumbent);
    document.getElementById('gpBound').textContent = last.bound === null ? '—' : Rshort(last.bound, 3);
    document.getElementById('gpAbs').textContent = gap.abs === null ? '—' : Rshort(gap.abs, 3);
    document.getElementById('gpRel').textContent = gap.rel === null ? '—' : Rpct(gap.rel, 2);
    document.getElementById('gpDf').textContent = full.df.refused ? 'over 60' : String(full.df.counts.explored);
    document.getElementById('gpBb').textContent = full.bb.refused ? 'over 60' : String(full.bb.counts.explored);

    var firstInc = null;
    for (i = 0; i < t.length; i += 1) if (t[i].incumbent !== null) { firstInc = t[i].at; break; }
    var closed = null;
    for (i = 0; i < t.length; i += 1) {
      var gi = ipGap(t[i].bound, t[i].incumbent, true);
      if (gi.abs !== null && Rzero(gi.abs)) { closed = t[i].at; break; }
    }
    status.innerHTML = 'After <strong>' + here.counts.explored + ' nodes</strong> the incumbent is <strong>'
      + (last.incumbent === null ? 'still nothing' : Rtext(last.incumbent)) + '</strong> and the global bound is <strong>'
      + (last.bound === null ? '&mdash;' : Rshort(last.bound, 3)) + '</strong>, so ' + gap.proved + '. '
      + (firstInc === null ? ''
          : 'The incumbent that wins was found at node ' + firstInc
            + (closed === null ? ' and the gap has not closed yet, which is the whole difference: a value in hand is not a proof.'
               : ' and the gap closed at node ' + closed + ' &mdash; '
                 + (closed > firstInc ? (closed - firstInc) + ' nodes of work after the answer was already in hand, spent entirely on proving it.'
                    : 'in the same step.')) + ' ')
      + 'On this instance depth first explores <strong>' + (full.df.refused ? 'more than 60' : full.df.counts.explored)
      + '</strong> nodes and best bound <strong>' + (full.bb.refused ? 'more than 60' : full.bb.counts.explored)
      + '</strong>, for the same answer.';
  }

  [preSel, orderSel].forEach(function (el) { el.addEventListener('change', redraw); });
  budS.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Incumbents, bounds and the gap",
        subtitle="Two numbers that squeeze the optimum, and the only thing proved at any moment",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Watch the two bounds close on each other"),
        panel_intro=cfg.get(
            "panel_intro",
            "The incumbent comes from any feasible point and the bound from the relaxation; both "
            "are re-derived from the node list, so the same tree gives the same trace. This instance has "
            + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# gomory -- a cut, drawn where a reader can see it
# ---------------------------------------------------------------------------

_GOMORY = {
    "corner": ("true, 1, 1, [[2,5,'le',16,'kiln'],[6,5,'le',30,'glaze']], 0, 6, 0, 4",
               "a corner fractional in both variables, so the first cut has something to bite on"),
    "sliver": ("true, 4, 5, [[3,2,'le',13,'cutting'],[1,4,'le',15,'joining']], 0, 5, 0, 4",
               "a thin region where the cuts take several rounds to reach a whole corner"),
    "flat": ("true, 2, 1, [[4,3,'le',19,'press'],[1,3,'le',13,'dry']], 0, 5, 0, 5",
             "a nearly flat objective, so the cut moves the optimum without moving its value much"),
}


def _gomory(cfg):
    name, (spec, blurb) = _preset(cfg, "gomory", _GOMORY, "corner")

    markup = (
        _toolbar(
            "Cutting planes",
            "round every coefficient of a fractional row down, and the leftovers are an inequality no integer point breaks",
            [("cyan", "the relaxed region"), ("green", "integer points"),
             ("red", "the cuts"), ("amber", "where the relaxation stops"), ("purple", "a cut you typed")],
        )
        + _stage(_svg("goGrid", "0 0 520 300",
                      "The region with every cut drawn on it, and the point the relaxation now stops at."))
        + _table("goTable")
        + _banner("goStatus")
    )
    controls = (
        _select("goPreset", "Instance", [(k, _GOMORY[k][1]) for k in sorted(_GOMORY)], name)
        + _range("goRounds", "Cuts added", 0, 6, 1)
        + _range("goRow", "Derive the first cut from row", 1, 4, 1)
        + _text("goOwn", "Or test a cut of your own", "x1 + x2 <= 4")
        + _kpis([
            ("Where the relaxation stops now", "goPoint"),
            ("Its value", "goZ"),
            ("Cuts actually added", "goAdded"),
            ("Dual-simplex pivots they cost", "goPivots"),
            ("Integer points the cuts removed", "goKept"),
            ("Your cut", "goOwnVerdict"),
        ])
        + _hint("goHint",
                "Validity is a claim about every integer point, not about the one you dislike. "
                "Type a cut and the lab tests it on every lattice point in the box; if it kills one, "
                "the point it killed is named.")
    )

    script = _MODE_JS["gomory"] + r"""
  var SPEC = { corner: [""" + _GOMORY["corner"][0] + r"""],
               sliver: [""" + _GOMORY["sliver"][0] + r"""],
               flat: [""" + _GOMORY["flat"][0] + r"""] };
  var preSel = document.getElementById('goPreset'), roundS = document.getElementById('goRounds');
  var rowS = document.getElementById('goRow'), ownBox = document.getElementById('goOwn');
  var grid = document.getElementById('goGrid'), table = document.getElementById('goTable');
  var status = document.getElementById('goStatus');

  function redraw() {
    var p = SPEC[preSel.value];
    var model = ipTwoVar(p[0], p[1], p[2], p[3]);
    var view = [[p[4], p[5]], [p[6], p[7]]];
    var box = [[BigInt(p[4]), BigInt(p[5])], [BigInt(p[6]), BigInt(p[7])]];
    var rounds = +roundS.value, row = +rowS.value - 1;
    document.getElementById('goRoundsOut').textContent = rounds === 1 ? 'one cut' : rounds + ' cuts';
    document.getElementById('goRowOut').textContent = 'row ' + (row + 1);

    var lat = latticePoints(model, box);
    var run = ipCutRounds(model, rounds, row);
    if (run.status !== 'optimal') {
      grid.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'The relaxation of this instance is <strong>' + ipEsc(run.status)
        + '</strong>, so there is no fractional corner to cut.';
      return;
    }

    var lines = [], rows = '', pivots = 0, killed = 0, i;
    for (i = 0; i < run.steps.length; i += 1) {
      var st = run.steps[i], co = st.cut.inOriginal;
      /* drawn as  -a.x <= -b , which is the >= cut as a half-plane */
      lines.push({ a: Rneg(co.a[0]), b: Rneg(co.a[1]), c: Rneg(co.b), tone: 'red',
                   label: 'cut ' + (i + 1) });
      var check = ipCutValid({ a: co.a, b: co.b, rel: '>=' }, lat.points);
      killed += check.killed.length;
      pivots += st.pivots || 0;
      rows += ipTr([ipTd('cut ' + (i + 1)), ipTd('row ' + (st.row + 1) + ', ' + ipEsc(st.cut.basicName)),
                    ipTdl(st.cut.inTableau.text), ipTdl(co.text),
                    ipTd(st.x ? '(' + Rtext(st.x[0]) + ', ' + Rtext(st.x[1]) + ')' : ipEsc(st.status)),
                    ipTd(st.z === null ? '&mdash;' : Rtext(st.z)),
                    ipTd(check.valid ? ipChip('keeps every integer point', 'ok')
                                     : ipChip('removes ' + check.killed.length, 'no'))]);
    }

    var own = ipIneq(ownBox.value, model.names), ownCheck = null;
    if (!own.error) {
      ownCheck = ipCutValid({ a: own.a, b: own.b, rel: own.rel }, lat.points);
      lines.push({ a: own.rel === '>=' ? Rneg(own.a[0]) : own.a[0],
                   b: own.rel === '>=' ? Rneg(own.a[1]) : own.a[1],
                   c: own.rel === '>=' ? Rneg(own.b) : own.b,
                   tone: 'purple', label: 'yours' });
    }

    var marks = [{ x: run.start.x[0], y: run.start.x[1], tone: 'muted', shape: 'square',
                   label: 'before any cut' }];
    if (run.x) marks.push({ x: run.x[0], y: run.x[1], tone: 'amber', shape: 'cross', label: 'now' });
    grid.innerHTML = ipLattice({
      cons: ipHalfPlanes(model), box: view, points: lat.points, marks: marks, lines: lines,
      width: 520, height: 300, names: model.names,
      note: 'a cut is valid when no filled dot falls on the wrong side of it'
    });

    table.innerHTML = ipHead(['cut', 'derived from', "in the tableau's variables",
                              "in the reader's variables", 'the relaxation then stops at',
                              'its value', 'validity, tested on every lattice point'])
      + '<tbody>' + (rows || ipTr([ipTdl('no cut has been added yet')])) + '</tbody>';

    document.getElementById('goPoint').textContent = '(' + Rtext(run.x[0]) + ', ' + Rtext(run.x[1]) + ')';
    document.getElementById('goZ').textContent = Rtext(run.z);
    document.getElementById('goAdded').textContent = String(run.steps.length);
    document.getElementById('goPivots').textContent = String(pivots);
    document.getElementById('goKept').textContent = killed === 0
      ? 'none, on all ' + run.steps.length + ' of them' : String(killed);
    document.getElementById('goOwnVerdict').textContent = own.error ? 'unreadable'
      : (ownCheck.valid ? 'valid' : 'it kills ' + ownCheck.killed.length);

    var before = run.start;
    status.innerHTML = 'The relaxation alone stops at <strong>(' + Rtext(before.x[0]) + ', ' + Rtext(before.x[1])
      + ')</strong> worth ' + Rtext(before.zOrig) + '. '
      + (run.steps.length === 0
          ? 'No cut has been added yet.'
          : 'After <strong>' + run.steps.length + (run.steps.length === 1 ? ' cut' : ' cuts')
            + '</strong> it stops at <strong>(' + Rtext(run.x[0]) + ', ' + Rtext(run.x[1]) + ')</strong> worth '
            + Rtext(run.z) + ', and the dual simplex needed ' + pivots + ' pivot'
            + (pivots === 1 ? '' : 's') + ' to get there &mdash; the tableau was already optimal, only infeasible. ')
      + (run.integral ? 'That point is whole, so the relaxation has been driven to the integer optimum. '
                      : 'It is still fractional, so there is another row to cut from. ')
      + 'Every cut so far keeps every one of the ' + lat.feasibleCount
      + ' integer points of the region' + (killed ? ' &mdash; except that ' + killed + ' were removed, which would be a bug' : '')
      + '. '
      + (own.error
          ? 'The cut you typed does not read: ' + own.error + '.'
          : (ownCheck.valid
              ? '<strong>' + ipIneqText(own)
                + '</strong> is valid: no integer point of the region breaks it.'
              : '<strong>' + ipIneqText(own)
                + '</strong> is <strong>not</strong> a valid cut. It removes ('
                + Rtext(ownCheck.killed[0].x[0]) + ', ' + Rtext(ownCheck.killed[0].x[1])
                + '), which is a whole-number plan satisfying every row &mdash; cutting off the fractional optimum is not enough.'));
  }

  preSel.addEventListener('change', redraw);
  [roundS, rowS].forEach(function (el) { el.addEventListener('input', redraw); });
  ownBox.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Cuts that lose no integer point",
        subtitle="Fractional parts of a tableau row, added as a constraint, and the dual simplex puts it back",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Add cuts one at a time, and test one of your own"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each cut is derived from a fractional row, drawn in the reader's own coordinates, added "
            "to the tableau and re-solved by the dual simplex; every one is tested against every "
            "lattice point in the box. This instance has " + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# bigm -- sizing a big-M, and paying for getting it wrong
# ---------------------------------------------------------------------------

# fixed costs, unit costs, capacities, demand. The tightest valid M is the
# smaller of the largest capacity and the whole demand, and the instance is
# chosen so that a genuine breakpoint -- where the relaxation changes which
# facility it half-opens -- sits ABOVE that value and can be reached by the
# slider.
_BIGM = {
    "two": ("200,60", "2,6", "40,40", 30,
            "a cheap facility with a large fixed cost against a dear one with a small fixed cost"),
    "three": ("240,150,90", "2,4,7", "30,30,30", 40,
              "three facilities, so the relaxation has more than one way to spread a fraction"),
    "equal": ("150,150", "3,5", "50,50", 45,
              "equal fixed costs, so the relaxation never changes its mind and the curve has no bend"),
}


def _bigm(cfg):
    name, (fixed, unit, cap, demand, blurb) = _preset(cfg, "bigm", _BIGM, "two")

    markup = (
        _toolbar(
            "The price of a loose M",
            "every unit of M past the smallest valid one weakens the bound and buys nothing",
            [("amber", "the bound against M"), ("purple", "a breakpoint"),
             ("cyan", "the bound against demand"), ("green", "the integer answer")],
        )
        + _stage(_svg("bmPlot", "0 0 660 240",
                      "The relaxation's bound plotted against M, with the exact breakpoints marked."))
        + _table("bmTable")
        + _banner("bmStatus")
    )
    controls = (
        _select("bmPreset", "Instance", [(k, _BIGM[k][4]) for k in sorted(_BIGM)], name)
        + _range("bmM", "M, as a multiple of the tightest valid value", 10, 400, 10)
        + _range("bmDemand", "Demand", 5, 60, demand)
        + _select("bmDraw", "Draw",
                  [("m", "the bound against M"), ("demand", "the bound against demand, at this M")], "m")
        + _kpis([
            ("The tightest valid M", "bmTight"),
            ("M as chosen", "bmMUsed"),
            ("The bound at this M", "bmBound"),
            ("The bound at the tightest M", "bmTightBound"),
            ("The fractional y it buys", "bmY"),
            ("Nodes at this M, against the tightest", "bmNodes"),
        ])
        + _hint("bmHint",
                "The tightest valid M is a reason, not a habit: a facility can ship no more than its "
                "own capacity and no more than the whole demand, so the smaller of those two is "
                "valid and nothing smaller is. Every unit above it is paid for in the bound.")
    )

    script = _MODE_JS["bigm"] + r"""
  var SPEC = """ + _js_map(_BIGM, ("fixed", "unit", "cap", "demand", "words")) + r""";
  var preSel = document.getElementById('bmPreset'), mS = document.getElementById('bmM');
  var demS = document.getElementById('bmDemand'), drawSel = document.getElementById('bmDraw');
  var plot = document.getElementById('bmPlot'), table = document.getElementById('bmTable');
  var status = document.getElementById('bmStatus');
  var lastPreset = null;

  function nums(text) { return String(text).split(',').map(function (t) { return ipRead(t); }); }

  function build() {
    var p = SPEC[preSel.value];
    if (preSel.value !== lastPreset) { lastPreset = preSel.value; demS.value = p.demand; }
    return { fixed: nums(p.fixed), unit: nums(p.unit), cap: nums(p.cap),
             demand: R(BigInt(+demS.value), 1n) };
  }

  function redraw() {
    var spec = build();
    var tight = ipTightM(spec);
    var mult = +mS.value / 10;
    var M = Rmul(tight.M, R(BigInt(+mS.value), 10n));
    document.getElementById('bmMOut').textContent = mult.toFixed(1) + ' times';
    document.getElementById('bmDemandOut').textContent = demS.value;

    var here = lpSolve(ipFixedCharge(spec, M));
    var atTight = lpSolve(ipFixedCharge(spec, tight.M));
    var hi = Rmul(tight.M, R(40n, 1n));
    var breaks = ipMBreaks(spec, tight.M, hi);
    var treeHere = ipFixedChargeNodes(spec, M, 30);
    var treeTight = Requ(M, tight.M) ? treeHere : ipFixedChargeNodes(spec, tight.M, 30);

    /* Sixteen samples plus every exact breakpoint. The samples are only the
       shape of the curve; the bends are solved for, so more samples would buy
       nothing and cost a re-solve each. */
    var pts = [], i;
    var steps = 16;
    for (i = 0; i <= steps; i += 1) {
      var Mi = Radd(tight.M, Rmul(Rsub(hi, tight.M), R(BigInt(i), BigInt(steps))));
      var z = ipBound(spec, Mi);
      if (z !== null) pts.push([ipPx(Mi), ipPx(z)]);
    }
    for (i = 0; i < breaks.length; i += 1) pts.push([ipPx(breaks[i].M), ipPx(breaks[i].z)]);
    pts.sort(function (a, b) { return a[0] - b[0]; });

    var drops = breaks.map(function (b) {
      return { x: ipPx(b.M), label: 'M = ' + Rshort(b.M, 2) };
    });

    if (drawSel.value === 'demand') {
      var model = ipFixedCharge(spec, M);
      var curve = rhsCurve(model, 0, R(5n, 1n), R(60n, 1n));
      var dpts = [];
      for (i = 0; i < curve.pieces.length; i += 1) {
        dpts.push([ipPx(curve.pieces[i].from), ipPx(curve.pieces[i].z)]);
        dpts.push([ipPx(curve.pieces[i].to), ipPx(curve.pieces[i].zTo === undefined ? curve.pieces[i].z : curve.pieces[i].zTo)]);
      }
      var drawn = ipPlot([{ pts: dpts, tone: 'cyan', dots: true }],
                         { width: 660, height: 240, xLabel: 'demand',
                           fmtY: function (v) { return v.toFixed(0); } });
      plot.innerHTML = drawn.svg
        + ipLabel(52, 26, 'the bound against the demand right-hand side, at this M: '
                  + curve.breakpoints.length + ' exact breakpoints', 'cyan', 'start', 9);
    } else {
      var drawn2 = ipPlot([{ pts: pts, tone: 'amber', dots: false }],
                          { width: 660, height: 240, xLabel: 'M', drops: drops,
                            fmtY: function (v) { return v.toFixed(0); },
                            fmtX: function (v) { return 'M = ' + v.toFixed(0); } });
      plot.innerHTML = drawn2.svg
        + ipLabel(52, 26, 'the relaxation\'s bound as M grows: it falls away from the answer and never comes back',
                  'amber', 'start', 9);
    }

    var rows = '', j;
    var ys = here.status === 'optimal' ? ipFractionalY(ipFixedCharge(spec, M), here.x) : [];
    var yt = atTight.status === 'optimal' ? ipFractionalY(ipFixedCharge(spec, tight.M), atTight.x) : [];
    for (j = 0; j < spec.fixed.length; j += 1) {
      rows += ipTr([ipTd('facility ' + (j + 1)), ipTd(Rtext(spec.fixed[j])), ipTd(Rtext(spec.unit[j])),
                    ipTd(Rtext(spec.cap[j])),
                    ipTd(yt.length ? Rtext(yt[j]) : '&mdash;'),
                    ipTd(ys.length ? Rtext(ys[j]) : '&mdash;'),
                    ipTdl(ys.length && !Rzero(ys[j]) && !Requ(ys[j], R1)
                          ? 'open for ' + Rpct(ys[j], 1) + ' of its fixed cost, which is not a thing that can be done'
                          : 'whole')]);
    }
    for (j = 0; j < breaks.length; j += 1) {
      rows += ipTr([ipTd('breakpoint'), ipTdl('M = ' + Rtext(breaks[j].M)), ipTd(Rtext(breaks[j].z)),
                    ipTd('&mdash;'), ipTd('&mdash;'), ipTd('&mdash;'),
                    ipTdl('the relaxation changes which facility it half-opens here, and the curve bends')],
                  'tone-purple');
    }
    table.innerHTML = ipHead(['', 'fixed cost', 'unit cost', 'capacity',
                              'y at the tightest M', 'y at this M', 'what that means'])
      + '<tbody>' + rows + '</tbody>';

    var zHere = here.status === 'optimal' ? here.zOrig : null;
    var zTight = atTight.status === 'optimal' ? atTight.zOrig : null;
    document.getElementById('bmTight').textContent = Rtext(tight.M);
    document.getElementById('bmMUsed').textContent = Rshort(M, 2);
    document.getElementById('bmBound').textContent = zHere === null ? here.status : Rshort(zHere, 2);
    document.getElementById('bmTightBound').textContent = zTight === null ? atTight.status : Rshort(zTight, 2);
    document.getElementById('bmY').textContent = ys.length
      ? ys.map(function (v) { return Rshort(v, 2); }).join(', ') : '&mdash;';
    document.getElementById('bmNodes').textContent = (treeHere.refused ? 'over 30' : treeHere.counts.explored)
      + ' against ' + (treeTight.refused ? 'over 30' : treeTight.counts.explored);

    status.innerHTML = 'The tightest valid M here is <strong>' + Rtext(tight.M) + '</strong>, because '
      + tight.why + '. At that value the relaxation is worth <strong>'
      + (zTight === null ? atTight.status : Rshort(zTight, 2)) + '</strong>. '
      + 'At <strong>M = ' + Rshort(M, 2) + '</strong> it is worth <strong>'
      + (zHere === null ? here.status : Rshort(zHere, 2)) + '</strong>'
      + (zHere !== null && zTight !== null && !Requ(zHere, zTight)
          ? ' &mdash; ' + Rshort(Rabs(Rsub(zTight, zHere)), 2) + ' weaker, for no change in the answer'
          : ' &mdash; the same bound, so this much slack costs nothing yet')
      + '. The tree needs <strong>' + (treeHere.refused ? 'more than 30' : treeHere.counts.explored)
      + '</strong> nodes at this M against <strong>' + (treeTight.refused ? 'more than 30' : treeTight.counts.explored)
      + '</strong> at the tightest, and both finish at '
      + (treeTight.best === null ? 'no integer answer' : Rtext(treeTight.best)) + '. '
      + (breaks.length
          ? 'The curve bends at ' + breaks.map(function (b) { return 'M = ' + Rtext(b.M); }).join(' and ')
            + ', where the relaxation swaps which facility it half-opens; those values are solved for and then '
            + 'checked by re-solving on both sides, not read off the drawing.'
          : 'There is no bend in this range: the relaxation never changes which facility it prefers, '
            + 'so the bound simply decays.')
      + ' Replacing the binary by x/M and rounding up is not a constraint at all &mdash; it is the rounding '
      + 'fallacy one level up.';
  }

  preSel.addEventListener('change', redraw);
  drawSel.addEventListener('change', redraw);
  [mS, demS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Fixed charges and the size of M",
        subtitle="A binary linked to an activity, and the bound you pay for every unit of slack in the link",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Make M larger and watch the bound fall away"),
        panel_intro=cfg.get(
            "panel_intro",
            "The relaxation is re-solved exactly at each value of M, the breakpoints are solved for "
            "and then checked, and the node count comes from the same branch-and-bound engine the "
            "search lesson uses. This instance is " + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# disjunction -- either-or, and the schedule half a binary describes
# ---------------------------------------------------------------------------

# Two jobs and one machine: either job one finishes before job two starts or
# the other way round. The pair is the smallest honest either-or there is, and
# it is also why the scheduling course's job shop is an integer programme --
# which this mode says out loud.
#
# Each row is (coefficient on x1, coefficient on x2, right-hand side) as a
# `<=`, so A is x1 - x2 <= -p1 and B is -x1 + x2 <= -p2.
_DISJUNCTIONS = {
    "machine": (4, 3, 10, 10, 1, 1,
                "two jobs of four and three hours competing for one machine"),
    "uneven": (7, 2, 12, 12, 1, 2,
               "a long job and a short one, where the order matters a great deal"),
    "tight": (5, 5, 9, 9, 2, 1,
              "equal jobs and a deadline that only just fits one order"),
}


def _disjunction(cfg):
    name, (p1, p2, d1, d2, c1, c2, blurb) = _preset(cfg, "disjunction", _DISJUNCTIONS, "machine")

    markup = (
        _toolbar(
            "Either, or",
            "writing both constraints writes the conjunction, and on a sequencing pair that is infeasible",
            [("cyan", "the branch y = 1 allows"), ("purple", "the branch y = 0 allows"),
             ("amber", "where the relaxation stops"), ("red", "writing both")],
        )
        + _stage(_svg("djGrid", "0 0 520 300",
                      "The region each branch of the disjunction leaves, drawn over the other."))
        + _table("djTable")
        + _banner("djStatus")
    )
    controls = (
        _select("djPreset", "Instance", [(k, _DISJUNCTIONS[k][6]) for k in sorted(_DISJUNCTIONS)], name)
        + _select("djY", "The binary",
                  [("1", "y = 1: the first job goes first"),
                   ("0", "y = 0: the second job goes first"),
                   ("free", "leave y continuous, which is the relaxation"),
                   ("both", "write both constraints, which is the mistake")], "1")
        + _range("djMA", "M for the first row, as a multiple of the tightest", 10, 60, 10)
        + _range("djMB", "M for the second row, as a multiple of the tightest", 10, 60, 10)
        + _kpis([
            ("y", "djYval"),
            ("Where the schedule starts", "djPoint"),
            ("Its cost", "djZ"),
            ("The tightest M for the first row", "djTightA"),
            ("The tightest M for the second row", "djTightB"),
            ("What the binary describes", "djMeaning"),
        ])
        + _hint("djHint",
                "The two values of M need not be equal and each must be valid for its own row. One "
                "M used for both, unchecked, is how a disjunction quietly becomes an implication &mdash; "
                "and the two sliders here are deliberately separate for that reason.")
    )

    script = _MODE_JS["disjunction"] + r"""
  var SPEC = """ + _js_map(_DISJUNCTIONS, ("p1", "p2", "d1", "d2", "c1", "c2", "words")) + r""";
  var preSel = document.getElementById('djPreset'), ySel = document.getElementById('djY');
  var maS = document.getElementById('djMA'), mbS = document.getElementById('djMB');
  var grid = document.getElementById('djGrid'), table = document.getElementById('djTable');
  var status = document.getElementById('djStatus');

  function build() {
    var p = SPEC[preSel.value];
    var ri = function (v) { return R(BigInt(v), 1n); };
    /* x1 - x2 <= -p1  is "job one finishes before job two starts";
       -x1 + x2 <= -p2 is the other order. Both deadlines hold either way. */
    return { names: ['start of job one', 'start of job two'], max: false,
             obj: [ri(p.c1), ri(p.c2)],
             A: [R1, R(-1n, 1n), ri(-p.p1)], nameA: 'job one before job two',
             B: [R(-1n, 1n), R1, ri(-p.p2)], nameB: 'job two before job one',
             both: [[R1, R0, ri(p.d1), 'le', 'job one starts by its deadline'],
                    [R0, R1, ri(p.d2), 'le', 'job two starts by its deadline']],
             p1: ri(p.p1), p2: ri(p.p2), d1: ri(p.d1), d2: ri(p.d2) };
  }

  /* The tightest valid M for a row is the most that row's left-hand side can
     exceed its right-hand side anywhere in the box the other constraints
     allow: enough to make the row vacuous, and not one unit more. */
  function tightM(spec, which) {
    var row = which === 'A' ? spec.A : spec.B;
    /* Row A is x1 - x2 <= -p1, worst at x1 at its deadline and x2 at zero;
       row B is the mirror of that. */
    var x = which === 'A' ? spec.d1 : R0, y = which === 'A' ? R0 : spec.d2;
    return Rsub(Radd(Rmul(row[0], x), Rmul(row[1], y)), row[2]);
  }

  function redraw() {
    var spec = build();
    var tA = tightM(spec, 'A'), tB = tightM(spec, 'B');
    var MA = Rmul(tA, R(BigInt(+maS.value), 10n)), MB = Rmul(tB, R(BigInt(+mbS.value), 10n));
    document.getElementById('djMAOut').textContent = (+maS.value / 10).toFixed(1) + ' times';
    document.getElementById('djMBOut').textContent = (+mbS.value / 10).toFixed(1) + ' times';

    var mode = ySel.value;
    var model;
    if (mode === 'both') {
      model = { max: false, names: [spec.names[0], spec.names[1]], obj: spec.obj,
                cons: [{ a: [spec.A[0], spec.A[1]], rel: 'le', b: spec.A[2], name: spec.nameA },
                       { a: [spec.B[0], spec.B[1]], rel: 'le', b: spec.B[2], name: spec.nameB }]
                  .concat(spec.both.map(function (r) {
                    return { a: [r[0], r[1]], rel: r[3], b: r[2], name: r[4] };
                  })) };
    } else {
      model = ipDisjunction(spec, MA, MB, mode === 'free' ? null : +mode);
    }
    var sol = lpSolve(model);
    var yVal = (mode === 'both') ? null : (sol.status === 'optimal' ? sol.x[2] : null);

    var regionOne = ipBranchRegion(spec, 1, MA, MB);
    var regionZero = ipBranchRegion(spec, 0, MA, MB);
    var marks = [];
    if (sol.status === 'optimal') {
      marks.push({ x: sol.x[0], y: sol.x[1], tone: 'amber', shape: 'cross',
                   label: 'the schedule it picks' });
    }
    var span = Math.max(Number(spec.d1.n), Number(spec.d2.n)) + 2;
    grid.innerHTML = ipLattice({
      cons: regionOne, overlay: regionZero, box: [[0, span], [0, span]],
      points: null, marks: marks, width: 520, height: 300,
      names: ['start of job one', 'start of job two'],
      note: mode === 'both'
        ? 'the two rows written together leave nothing at all: their intersection is empty'
        : 'solid: what y = 1 allows. dashed: what y = 0 allows. They do not overlap, and that is the point'
    });

    var rows = '';
    rows += ipTr([ipTdl(spec.nameA), ipTdl('x1 - x2 &lt;= -' + Rtext(spec.p1)),
                  ipTd(Rtext(tA)), ipTd(Rshort(MA, 2)),
                  ipTdl('at y = 1 it binds; at y = 0 it becomes x1 - x2 &lt;= ' + Rshort(Rsub(MA, spec.p1), 2) + ', which nothing in the box breaks')]);
    rows += ipTr([ipTdl(spec.nameB), ipTdl('-x1 + x2 &lt;= -' + Rtext(spec.p2)),
                  ipTd(Rtext(tB)), ipTd(Rshort(MB, 2)),
                  ipTdl('at y = 0 it binds; at y = 1 it becomes -x1 + x2 &lt;= ' + Rshort(Rsub(MB, spec.p2), 2) + ', which nothing in the box breaks')]);
    for (var q = 0; q < 2; q += 1) {
      var branch = lpSolve(ipDisjunction(spec, MA, MB, q));
      rows += ipTr([ipTdl('fix y = ' + q), ipTdl(q ? spec.nameA : spec.nameB),
                    ipTd('&mdash;'), ipTd('&mdash;'),
                    ipTdl(branch.status === 'optimal'
                          ? 'starts at (' + Rtext(branch.x[0]) + ', ' + Rtext(branch.x[1]) + '), costing ' + Rtext(branch.zOrig)
                          : 'that branch is ' + ipEsc(branch.status))]);
    }
    table.innerHTML = ipHead(['row', 'as written', 'tightest valid M', 'M in use', 'what the binary does to it'])
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('djYval').textContent = mode === 'both' ? 'there is none'
      : (yVal === null ? '&mdash;' : Rtext(yVal));
    document.getElementById('djPoint').textContent = sol.status === 'optimal'
      ? '(' + Rtext(sol.x[0]) + ', ' + Rtext(sol.x[1]) + ')' : ipEsc(sol.status);
    document.getElementById('djZ').textContent = sol.status === 'optimal' ? Rtext(sol.zOrig) : '—';
    document.getElementById('djTightA').textContent = Rtext(tA);
    document.getElementById('djTightB').textContent = Rtext(tB);
    var meaning = 'both jobs run, one after the other';
    if (mode === 'both') meaning = 'nothing: there is no schedule';
    else if (yVal !== null && !Rint(yVal)) meaning = 'a schedule that does not exist';
    document.getElementById('djMeaning').textContent = meaning;

    if (mode === 'both') {
      status.innerHTML = 'Writing <strong>both</strong> rows is the conjunction, not the disjunction: it asks '
        + 'that job one finish before job two starts <em>and</em> that job two finish before job one starts. '
        + 'Adding the two gives 0 &lt;= -' + Rtext(Radd(spec.p1, spec.p2))
        + ', so the model is <strong>' + ipEsc(sol.status) + '</strong> &mdash; and a reader who wrote it this way '
        + 'usually goes looking for a data error. The relaxation of each row by a big-M term that one binary '
        + 'switches off is what "or" actually costs.';
      return;
    }
    if (sol.status !== 'optimal') {
      status.innerHTML = 'At this setting the model is <strong>' + ipEsc(sol.status)
        + '</strong>. An M below the tightest valid value does that: it does not merely weaken the bound, '
        + 'it cuts off schedules that exist.';
      return;
    }
    var frac = !Rint(yVal);
    status.innerHTML = (mode === 'free'
        ? 'Left continuous, the relaxation sets <strong>y = ' + Rtext(yVal) + '</strong>'
        : 'With <strong>y = ' + mode + '</strong> the model enforces ' + (mode === '1' ? spec.nameA : spec.nameB))
      + ' and starts the jobs at <strong>(' + Rtext(sol.x[0]) + ', ' + Rtext(sol.x[1]) + ')</strong>, costing '
      + Rtext(sol.zOrig) + '. '
      + (frac
          ? 'That y is not 0 and not 1: it says job one is <strong>' + Rpct(yVal, 0) + ' before</strong> job two '
            + 'and the rest of it after, which is not a schedule. Both rows are half-relaxed at once, so both jobs '
            + 'may start at the same moment on one machine &mdash; the relaxation has bought a plan that cannot be run, '
            + 'and its cost is a bound and nothing else.'
          : 'Each branch is a genuine schedule, and the better of the two is what the integer problem wants. '
            + 'Sequencing two jobs on one machine IS this pair of constraints, which is why a job shop is an '
            + 'integer programme rather than a linear one.');
  }

  [preSel, ySel].forEach(function (el) { el.addEventListener('change', redraw); });
  [maS, mbS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Either-or constraints",
        subtitle="One binary relaxes one row and enforces the other, and a fractional y describes nothing",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fix the binary either way, then let it go"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each branch is solved exactly and drawn as its own region, and the relaxation is solved "
            "with the binary left continuous so its value can be read for what it is. This instance is "
            + blurb + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "lattice": _lattice,
    "logic": _logic,
    "knapsack": _knapsack,
    "bigm": _bigm,
    "disjunction": _disjunction,
    "bb": _bb,
    "gap": _gap,
    "gomory": _gomory,
    "tsp": _tsp,
}

MODES = tuple(sorted(_MODES))


def integer_lab(cfg):
    """The integer programming kit. `cfg["mode"]` chooses the lesson.

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
            "integer_lab: unknown mode %r; the nine modes of this course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["integer_lab", "MODES", "IPBASE_JS", "IPMODEL_JS", "IPINEQ_JS",
           "IPCOVER_JS", "IPFIX_JS", "IPDISJ_JS", "IPTOUR_JS", "IPCUT_JS",
           "IPLAT_JS", "IPTREE_JS", "IPPLOT_JS", "IPBARS_JS"]
