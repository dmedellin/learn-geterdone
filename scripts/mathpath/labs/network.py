"""Course 4's drawing kit -- seven modes, one directed network underneath.

Course 4 is the one course on this path that takes TWO kits. `transport` owns
the cost tableau; this one owns the drawing, and serves the seven lessons whose
figure is a directed graph.

  digraph      arcs on <= 8 nodes with typed capacity and cost; a typed flow
               checked node by node and arc by arc, the violated nodes named
  mincost      N, b, u and c written out of the drawing and solved exactly;
               five data sets, one linear programme
  tu           the submatrix determinants of N, the exhaustive sweep to k <= 3,
               and a determinant-2 matrix with the half-integral corner it makes
  bellmanford  the round-by-round labels, the potential check pi_j - pi_i <= c_ij
               on every arc, the tight-arc subgraph, and a negative cycle as
               dual INFEASIBILITY
  maxflow      augmenting paths chosen from the residual network, the reachable
               set as the minimum cut, any other cut shown to be at least as
               large, and the cut exhibited as a 0/1 solution of the dual LP
  matching     a bipartite editor, the maximum matching, and -- when it is
               imperfect -- the deficient set S read off the cut with
               |N(S)| < |S| counted on screen
  cpm          ES, EF, LS, LF and slack for a project, every critical path, and
               the point at which shortening a critical activity stops paying

WHAT THIS KIT DOES NOT CONTAIN, and why that is the design.

  THE AUGMENTING-PATH ALGORITHM. `maxflow` lets a reader push flow along a
  residual path and watch the residual network change, because the theorem
  needs a flow to be a theorem about. It does not teach why backward arcs are
  necessary or what the choice of path costs -- Algorithms owns that, and the
  lesson says so. What is here instead is the duality reading: a cut is a dual
  solution, and the page verifies that solution constraint by constraint.

  DIJKSTRA ALONGSIDE. The shortest-path mode has no Dijkstra panel. "Dijkstra
  usually works" is Algorithms' misconception; this lesson's is that the labels
  are only distances, and the shift control is the answer to it -- add a
  constant to every potential and every reduced cost is unchanged.

  A SUCCESSIVE-SHORTEST-PATHS MODE. There is none, because there is no lesson:
  the algorithm stands on a residual network and a Bellman-Ford this course
  cites rather than proves. `mincost`'s linear programme is the reference
  solution for every instance on the course.

WHY graph.py's GRAPH_JS IS NOT REUSED. It is undirected by construction --
`link(M, i, j)` writes `M[i][j]` and `M[j][i]`, and `edges()` scans `i < j` --
its weights are the function ((7a + 13b) mod 9) + 1 of the endpoints rather
than data a reader types, and it caps N at 8 with no capacities at all. Every
one of those is a thing this kit's first lesson is ABOUT: an arc is ordered,
and (i, j) and (j, i) are two objects with two capacities and two costs.

What GRAPH_JS is good for is checking: `kruskal`, `dijkstra` and `cuts` answer
questions by brute force on graphs this kit can also express, so
scripts/mathcheck.js runs them side by side as independent oracles. That is
recorded where it is done, not here.

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped. or_core's
docstring puts this kit's engine share at 17.6 KB, and that figure assumes one
core for all seven modes; it is not what ships. `cpm` has no linear programme
in it and must not carry a simplex, `tu` has no residual network and must not
carry a cut enumeration, and four of the seven never solve an LP at all. So
the kit's own arithmetic is SEVEN raw strings below rather than one, and each
mode concatenates what it calls and nothing else.

Measured, on a real lesson page rendered by scripts/mathpath/render.py -- page
frame 19.9 KB gzipped, plus the lab:

    bellmanford 35.8 KB   matching 36.1   cpm 36.5   digraph 36.6
    maxflow 41.8   mincost 43.3   tu 47.1

against the 62 KB ceiling. Splitting the kit block was worth about 3 KB on the
heaviest page; re-derive these rather than trusting them, because they go stale
as the engine grows.
"""

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import DUAL_JS, NET_JS, ORFMT_JS, PHASE_JS, TABLEAU_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions only, so scripts/mathcheck.js
# executes the shipped source: nothing here touches the document, and the two
# drawing functions take a layout rather than an element.
# ---------------------------------------------------------------------------

NETKIT_JS = r"""

  /* ================================================ the directed representation

     An arc is {from, to, cap, cost} and both endpoints are strings.  There is
     no adjacency matrix anywhere in this kit and that is deliberate: a matrix
     indexed by (tail, head) holds one cell for the pair, and the whole of the
     first lesson is that (i, j) and (j, i) are two objects with two capacities,
     two costs and two flow variables.  An ARRAY of arcs holds both, holds two
     copies of the same arc if a reader writes one, and indexes the flow vector
     by arc -- which is the column index of the incidence matrix, so the drawing
     and the linear programme are the same object read two ways.

     `cap` is null for an arc with no upper bound.  That is not "a very large
     number": an unbounded arc contributes no row to the linear programme at
     all, which is what u = infinity means and what a big constant would only
     approximate. */

  var NETNODES = 8;              /* the drawing can label eight and no more */
  var NETARCS = 14;

  function netClauses(text) {
    var parts = String(text).split(/[,;\n]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }

  /* One clause is  tail>head  followed by the fields, colon separated:
       s>a 3:4      capacity 3, cost 4
       s>a 4        one field
       s>a *:4      no upper bound, cost 4
     A fraction is a fraction -- 7/2 reads as seven halves, because the field
     separator is a colon and never a slash. */
  function parseNet(text, fields) {
    var cl = netClauses(text), nodes = [], arcs = [], seen = {}, i, k;
    if (!cl.length) return { bad: 'there is no network here yet' };
    if (cl.length > NETARCS) {
      return { bad: 'that is ' + cl.length + ' arcs, and this drawing labels at most ' + NETARCS };
    }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z0-9][A-Za-z0-9]{0,3})\s*(?:->|>)\s*([A-Za-z0-9][A-Za-z0-9]{0,3})\s*(.*)$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not an arc: write the tail, then &gt;, then the head' };
      if (m[1] === m[2]) {
        return { bad: '"' + esc(cl[i]) + '" runs from ' + m[1] + ' back to itself, and a loop carries '
                      + 'no flow anyone can account for' };
      }
      var arc = { from: m[1], to: m[2], cap: null, cost: R0, capped: false };
      var rest = m[3].trim();
      var vals = rest ? rest.split(':') : [];
      if (vals.length > fields.length) {
        return { bad: '"' + esc(cl[i]) + '" gives ' + vals.length + ' numbers; an arc here carries '
                      + fields.join(' and then ') };
      }
      if (vals.length < fields.length) {
        return { bad: '"' + esc(cl[i]) + '" is missing the ' + fields[vals.length]
                      + '; an arc here carries ' + fields.join(' and then ')
                      + ', colon separated' };
      }
      for (k = 0; k < fields.length; k += 1) {
        var raw = vals[k].trim();
        if (fields[k] === 'capacity' && raw === '*') { arc.cap = null; arc.capped = false; continue; }
        var v = Rread(raw);
        if (v === null) return { bad: '"' + esc(raw) + '" in "' + esc(cl[i]) + '" is not a number' };
        if (fields[k] === 'capacity') {
          if (Rsign(v) < 0) return { bad: 'the capacity on "' + esc(cl[i]) + '" is negative' };
          arc.cap = v; arc.capped = true;
        } else { arc.cost = v; }
      }
      arcs.push(arc);
      for (k = 0; k < 2; k += 1) {
        var id = k ? arc.to : arc.from;
        if (!seen[id]) { seen[id] = true; nodes.push(id); }
      }
    }
    if (nodes.length > NETNODES) {
      return { bad: 'that is ' + nodes.length + ' nodes, and this drawing labels at most ' + NETNODES };
    }
    return { nodes: nodes, arcs: arcs };
  }

  /* Supplies, as  node:amount .  A node the reader does not name supplies
     nothing, which is the usual case and should not have to be typed. */
  function parseSupply(text, nodes) {
    var cl = netClauses(text), out = {}, i, j;
    for (j = 0; j < nodes.length; j += 1) out[nodes[j]] = R0;
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z0-9][A-Za-z0-9]{0,3})\s*[:=]\s*(.*)$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not a supply: write the node, a colon, the amount' };
      if (out[m[1]] === undefined) return { bad: 'there is no node called ' + m[1] + ' in this network' };
      var v = Rread(m[2].trim());
      if (v === null) return { bad: '"' + esc(m[2]) + '" is not a number' };
      out[m[1]] = v;
    }
    var total = R0;
    for (j = 0; j < nodes.length; j += 1) total = Radd(total, out[nodes[j]]);
    return { supply: out, total: total };
  }

  /* ================================================================ layout

     Layered left to right: a node's column is the longest chain of arcs that
     reaches it.  A circle is the wrong shape for a network with a source and a
     sink -- the reader cannot see which way anything flows -- and this is why
     the layout is kit-local rather than lifted from the undirected kit. */
  function netLayout(nodes, arcs, width, height) {
    var ix = netIndex(nodes), n = nodes.length, rank = [], i, j;
    for (i = 0; i < n; i += 1) rank.push(0);
    var top = topoOrder(nodes, arcs);
    if (!top.cycle) {
      for (i = 0; i < top.order.length; i += 1) {
        var v = ix[top.order[i]];
        for (j = 0; j < arcs.length; j += 1) {
          if (ix[arcs[j].from] !== v) continue;
          var w = ix[arcs[j].to];
          if (rank[w] < rank[v] + 1) rank[w] = rank[v] + 1;
        }
      }
    } else {
      /* A cycle has no layering, so fall back to distance from the first node
         and let the drawing show the loop as a loop. */
      var dist = [], queue = [0];
      for (i = 0; i < n; i += 1) dist.push(i === 0 ? 0 : -1);
      while (queue.length) {
        var u = queue.shift();
        for (j = 0; j < arcs.length; j += 1) {
          if (ix[arcs[j].from] !== u) continue;
          var z = ix[arcs[j].to];
          if (dist[z] < 0) { dist[z] = dist[u] + 1; queue.push(z); }
        }
      }
      for (i = 0; i < n; i += 1) rank[i] = dist[i] < 0 ? 0 : dist[i];
    }
    var maxRank = 0, counts = {}, placed = {};
    for (i = 0; i < n; i += 1) if (rank[i] > maxRank) maxRank = rank[i];
    for (i = 0; i < n; i += 1) counts[rank[i]] = (counts[rank[i]] || 0) + 1;
    var left = 46, right = width - 46;
    var dx = maxRank > 0 ? (right - left) / maxRank : 0;
    var pos = {};
    for (i = 0; i < n; i += 1) {
      var r = rank[i], c = counts[r], k = placed[r] || 0;
      placed[r] = k + 1;
      var spread = Math.min(76, (height - 72) / Math.max(1, c));
      var y = height / 2 + (k - (c - 1) / 2) * spread;
      pos[nodes[i]] = { x: maxRank > 0 ? left + r * dx : width / 2, y: y, rank: r, index: i };
    }
    return { pos: pos, rank: rank, ranks: maxRank + 1, layered: !top.cycle };
  }

  /* ================================================================ drawing */

  function xy(v) { return Math.round(v * 10) / 10; }

  /* A line with a head on it, trimmed at both ends so the head sits on the
     circle rather than under it. */
  function arcSvg(x1, y1, x2, y2, colour, width, dash, off) {
    var dx = x2 - x1, dy = y2 - y1, len = Math.sqrt(dx * dx + dy * dy) || 1;
    var ux = dx / len, uy = dy / len, px = -uy, py = ux;
    var ax = x1 + ux * 17 + px * off, ay = y1 + uy * 17 + py * off;
    var bx = x2 - ux * 17 + px * off, by = y2 - uy * 17 + py * off;
    var hx = bx - ux * 9, hy = by - uy * 9;
    return '<line x1="' + xy(ax) + '" y1="' + xy(ay) + '" x2="' + xy(hx) + '" y2="' + xy(hy)
      + '" stroke="' + colour + '" stroke-width="' + width + '"'
      + (dash ? ' stroke-dasharray="5 4"' : '') + ' />'
      + '<polygon points="' + xy(bx) + ',' + xy(by) + ' ' + xy(hx + px * 4.6) + ',' + xy(hy + py * 4.6)
      + ' ' + xy(hx - px * 4.6) + ',' + xy(hy - py * 4.6) + '" fill="' + colour + '" />';
  }

  /* The drawing every mode shares.  `opt.label(j)`, `opt.tone(j)`, `opt.dash(j)`
     describe the arcs and `opt.nodeTone(id)`, `opt.nodeRing(id)` the nodes; each
     may be absent.  Antiparallel and parallel arcs are pushed apart
     perpendicular to their own line, which is the only way (i, j) and (j, i)
     can both be seen -- and seeing both is the point of the first lesson. */
  function drawNet(nodes, arcs, layout, opt) {
    opt = opt || {};
    var pos = layout.pos, s = '', i, j;
    var key = function (a) { return a.from < a.to ? a.from + '|' + a.to : a.to + '|' + a.from; };
    var group = {}, slot = [];
    for (j = 0; j < arcs.length; j += 1) {
      var k = key(arcs[j]);
      slot.push(group[k] === undefined ? 0 : group[k]);
      group[k] = slot[j] + 1;
    }
    for (j = 0; j < arcs.length; j += 1) {
      var a = pos[arcs[j].from], b = pos[arcs[j].to];
      if (!a || !b) continue;
      var count = group[key(arcs[j])];
      var off = count > 1 ? (slot[j] - (count - 1) / 2) * 13 : 0;
      var colour = 'var(--' + ((opt.tone && opt.tone(j)) || 'cyan') + ')';
      var width = (opt.wide && opt.wide(j)) ? 3 : 1.6;
      s += arcSvg(a.x, a.y, b.x, b.y, colour, width, opt.dash && opt.dash(j), off);
      var text = opt.label ? opt.label(j) : '';
      if (text) {
        var dx = b.x - a.x, dy = b.y - a.y, len = Math.sqrt(dx * dx + dy * dy) || 1;
        var px = -dy / len, py = dx / len;
        var mx = (a.x + b.x) / 2 + px * (off + 12), my = (a.y + b.y) / 2 + py * (off + 12);
        s += '<text x="' + xy(mx) + '" y="' + xy(my + 4) + '" text-anchor="middle" font-size="11" '
          + 'font-weight="600" fill="' + colour + '">' + text + '</text>';
      }
    }
    for (i = 0; i < nodes.length; i += 1) {
      var p = pos[nodes[i]];
      if (!p) continue;
      var ring = opt.nodeRing && opt.nodeRing(nodes[i]);
      s += '<circle cx="' + xy(p.x) + '" cy="' + xy(p.y) + '" r="16" fill="var(--panel-2)" stroke="var(--'
        + (ring || 'line-strong') + ')" stroke-width="' + (ring ? 3 : 1.5) + '" />'
        + '<text x="' + xy(p.x) + '" y="' + xy(p.y + 4) + '" text-anchor="middle" font-size="12" '
        + 'font-weight="700" fill="var(--' + ((opt.nodeTone && opt.nodeTone(nodes[i])) || 'text') + ')">'
        + ((opt.name && opt.name(nodes[i])) || nodes[i]) + '</text>';
      var under = opt.under && opt.under(nodes[i]);
      if (under) {
        s += '<text x="' + xy(p.x) + '" y="' + xy(p.y + 31) + '" text-anchor="middle" font-size="10" '
          + 'fill="var(--muted)">' + under + '</text>';
      }
    }
    return s;
  }

  /* A caption inside the drawing, so the legend and the picture cannot drift
     apart when a mode changes what it is showing. */
  function netCaption(text, width, height) {
    return '<text x="' + (width / 2) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" '
      + 'fill="var(--muted)">' + text + '</text>';
  }

  function capText(a) { return a.capped ? Rtext(a.cap) : '&#8734;'; }
"""

CHECK_JS = r"""
  /* A typed flow, the two separate tests it has to pass, and the pair of arcs
     whose existence is the first lesson.  Only the conservation mode reads a
     flow the reader typed, so only that page carries this. */
  /* A flow, in the same syntax as the arcs it belongs to, so the reader can see
     the correspondence rather than counting positions in a list.  Repeated
     parallel arcs are filled in order of appearance. */
  function parseFlow(text, arcs) {
    var cl = netClauses(text), flow = [], used = [], i, j;
    for (j = 0; j < arcs.length; j += 1) { flow.push(R0); used.push(false); }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z0-9][A-Za-z0-9]{0,3})\s*(?:->|>)\s*([A-Za-z0-9][A-Za-z0-9]{0,3})\s*:?\s*(.*)$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not an arc with a number on it' };
      var v = Rread(m[3].trim());
      if (v === null) return { bad: '"' + esc(m[3]) + '" in "' + esc(cl[i]) + '" is not a number' };
      var hit = -1;
      for (j = 0; j < arcs.length; j += 1) {
        if (!used[j] && arcs[j].from === m[1] && arcs[j].to === m[2]) { hit = j; break; }
      }
      if (hit < 0) {
        return { bad: 'there is no arc ' + m[1] + ' to ' + m[2] + ' left to carry that; '
                      + 'the flow names an arc the network does not have' };
      }
      flow[hit] = v; used[hit] = true;
    }
    return { flow: flow, given: used };
  }

  /* ---- what conservation does not check ------------------------------- */

  /* The capacity side.  conservation() in the engine answers the node
     question; this answers the arc one, and the lesson needs both because a
     flow can be perfectly conserved at every node and still over-fill an arc. */
  function capacityCheck(arcs, flow) {
    var rows = [], over = [], j;
    for (j = 0; j < arcs.length; j += 1) {
      var f = flow[j] === undefined ? R0 : flow[j];
      var neg = Rsign(f) < 0;
      var slack = arcs[j].capped ? Rsub(arcs[j].cap, f) : null;
      var bad = neg || (slack !== null && Rsign(slack) < 0);
      rows.push({ arc: j, flow: f, cap: arcs[j].cap, slack: slack, negative: neg, ok: !bad });
      if (bad) over.push(j);
    }
    return { rows: rows, over: over, ok: over.length === 0 };
  }

  function flowCost(arcs, flow) {
    var total = R0, j;
    for (j = 0; j < arcs.length; j += 1) {
      total = Radd(total, Rmul(arcs[j].cost, flow[j] === undefined ? R0 : flow[j]));
    }
    return total;
  }

  /* The arcs whose reverse is also present.  Named on the page because the
     named misconception is that they are one edge with an arrow on it. */
  function antiparallel(arcs) {
    var out = [], i, j;
    for (i = 0; i < arcs.length; i += 1) {
      for (j = 0; j < arcs.length; j += 1) {
        if (arcs[i].from === arcs[j].to && arcs[i].to === arcs[j].from) { out.push([i, j]); break; }
      }
    }
    return out;
  }
"""

MODEL_JS = r"""
  /* The linear programme a drawing becomes.  Two modes take this -- the one
     that writes the programme out and the one that shows why its corners are
     whole -- and the other five do not, so it is a block rather than part of
     the core. */

  /* Nx = b, 0 <= x <= u, min c'x -- assembled from the engine's incidence
     matrix and nothing else, so the matrix on the page IS the matrix in the
     programme.  An uncapped arc contributes no bound row. */
  function mcfModel(nodes, arcs, supply) {
    var N = incidence(nodes, arcs), cons = [], names = [], obj = [], i, j;
    for (j = 0; j < arcs.length; j += 1) {
      names.push(arcs[j].from + arcs[j].to);
      obj.push(arcs[j].cost);
    }
    for (i = 0; i < nodes.length; i += 1) {
      cons.push({ a: N[i].slice(), rel: 'eq',
                  b: supply[nodes[i]] === undefined ? R0 : supply[nodes[i]],
                  name: 'node ' + nodes[i] });
    }
    for (j = 0; j < arcs.length; j += 1) {
      if (!arcs[j].capped) continue;
      var row = [];
      for (i = 0; i < arcs.length; i += 1) row.push(i === j ? R1 : R0);
      cons.push({ a: row, rel: 'le', b: arcs[j].cap,
                  name: 'capacity ' + arcs[j].from + '&gt;' + arcs[j].to });
    }
    return { max: false, names: names, obj: obj, cons: cons, N: N };
  }
"""

CUT_JS = r"""
  /* Residual walking, every cut there is, and the maximum-flow programme with
     the 0/1 dual point a cut names.  One mode reads all of it; the other six
     read none of it, and a page that shipped it anyway would be carrying a
     cut enumeration to a reader looking at a project schedule. */

  /* The maximum-flow programme.  Conservation is written IN minus OUT at the
     nodes that are neither source nor sink, and the sign is not arbitrary: an
     equality row may be written either way and its dual variable changes sign
     with it, and written this way the optimal dual potential comes out as the
     INDICATOR of the cut rather than its negative.  The lesson is that a 0/1
     dual solution is a cut, so the 0/1 is worth arranging. */
  function maxflowModel(nodes, arcs, s, t) {
    var cons = [], names = [], obj = [], i, j;
    for (j = 0; j < arcs.length; j += 1) {
      names.push(arcs[j].from + arcs[j].to);
      obj.push(arcs[j].from === s ? R1 : (arcs[j].to === s ? R(-1n, 1n) : R0));
    }
    for (i = 0; i < nodes.length; i += 1) {
      if (nodes[i] === s || nodes[i] === t) continue;
      var row = [];
      for (j = 0; j < arcs.length; j += 1) {
        row.push(arcs[j].to === nodes[i] ? R1 : (arcs[j].from === nodes[i] ? R(-1n, 1n) : R0));
      }
      cons.push({ a: row, rel: 'eq', b: R0, name: 'node ' + nodes[i] });
    }
    for (j = 0; j < arcs.length; j += 1) {
      var cr = [], k;
      for (k = 0; k < arcs.length; k += 1) cr.push(k === j ? R1 : R0);
      cons.push({ a: cr, rel: 'le', b: arcs[j].cap,
                  name: 'capacity ' + arcs[j].from + '&gt;' + arcs[j].to });
    }
    return { max: true, names: names, obj: obj, cons: cons };
  }

  /* The 0/1 point the cut S names, in the dual's own variable order: one
     potential per interior node, then one y per arc. */
  function cutDualPoint(nodes, arcs, S, s, t) {
    var inS = {}, out = [], i, j;
    for (i = 0; i < S.length; i += 1) inS[S[i]] = true;
    for (i = 0; i < nodes.length; i += 1) {
      if (nodes[i] === s || nodes[i] === t) continue;
      out.push(inS[nodes[i]] ? R1 : R0);
    }
    for (j = 0; j < arcs.length; j += 1) {
      out.push(inS[arcs[j].from] && !inS[arcs[j].to] ? R1 : R0);
    }
    return out;
  }

  /* Any model, any point: every row checked against its relation, and the
     objective evaluated.  A primal flow and a dual cut are both points of
     linear programmes, so one function serves both -- and a feasible primal
     and a feasible dual with equal objectives certify BOTH optimal, which is
     the whole of strong duality on an instance. */
  function checkModel(model, x) {
    var rows = [], bad = [], i, j;
    for (i = 0; i < model.cons.length; i += 1) {
      var c = model.cons[i], lhs = R0;
      for (j = 0; j < c.a.length; j += 1) lhs = Radd(lhs, Rmul(c.a[j], x[j]));
      var rel = c.rel || 'le', d = Rcmp(lhs, c.b);
      var ok = rel === 'eq' ? d === 0 : (rel === 'le' ? d <= 0 : d >= 0);
      rows.push({ row: i, name: c.name, rel: rel, lhs: lhs, b: c.b, ok: ok,
                  slack: Rsub(c.b, lhs) });
      if (!ok) bad.push(i);
    }
    var z = R0;
    for (j = 0; j < model.obj.length; j += 1) z = Radd(z, Rmul(model.obj[j], x[j]));
    return { rows: rows, violated: bad, ok: bad.length === 0, value: z };
  }

  /* ---- residual walking, and every cut there is ------------------------ */

  /* Every simple s-t path in a residual network, in the order a depth-first
     walk finds them, capped.  The reader picks one; the kit does not choose,
     because choosing is Algorithms' lesson and not this one. */
  function resPaths(resArcs, s, t, cap) {
    cap = cap || 10;
    var out = [], seen = {};
    seen[s] = true;
    var walk = function (v, path) {
      if (out.length >= cap) return;
      if (v === t) { out.push(path.slice()); return; }
      for (var j = 0; j < resArcs.length; j += 1) {
        if (resArcs[j].from !== v || seen[resArcs[j].to]) continue;
        seen[resArcs[j].to] = true;
        path.push(j);
        walk(resArcs[j].to, path);
        path.pop();
        seen[resArcs[j].to] = false;
      }
    };
    walk(s, []);
    return out;
  }

  function pathBottleneck(resArcs, path) {
    var b = null, i;
    for (i = 0; i < path.length; i += 1) {
      if (b === null || Rcmp(resArcs[path[i]].cap, b) < 0) b = resArcs[path[i]].cap;
    }
    return b;
  }

  /* Push the bottleneck.  A backward residual arc sends flow back down the arc
     it came from, which is why it is a subtraction and not an addition. */
  function augmentFlow(arcs, flow, resArcs, path) {
    var b = pathBottleneck(resArcs, path), f = flow.slice(), i;
    if (b === null) return { flow: f, bottleneck: R0 };
    for (i = 0; i < path.length; i += 1) {
      var ra = resArcs[path[i]];
      f[ra.of] = ra.kind === 'forward' ? Radd(f[ra.of], b) : Rsub(f[ra.of], b);
    }
    return { flow: f, bottleneck: b };
  }

  function flowValue(nodes, arcs, flow, s) {
    var v = R0, j;
    for (j = 0; j < arcs.length; j += 1) {
      var f = flow[j] === undefined ? R0 : flow[j];
      if (arcs[j].from === s) v = Radd(v, f);
      else if (arcs[j].to === s) v = Rsub(v, f);
    }
    return v;
  }

  /* Every cut, not a search for the best one.  With eight nodes there are at
     most 2^6 = 64 of them, and enumerating all of them is what lets the page
     say "this one is minimum" and "there are two of them" as facts rather than
     as the output of a procedure the reader is asked to trust. */
  function allCuts(nodes, arcs, s, t) {
    var mid = [], i, j;
    for (i = 0; i < nodes.length; i += 1) if (nodes[i] !== s && nodes[i] !== t) mid.push(nodes[i]);
    var out = [], total = 1 << mid.length;
    for (i = 0; i < total; i += 1) {
      var S = [s];
      for (j = 0; j < mid.length; j += 1) if (i & (1 << j)) S.push(mid[j]);
      var cc = cutCapacity(nodes, arcs, S);
      out.push({ S: S, capacity: cc.capacity, crossing: cc.crossing, back: cc.back });
    }
    out.sort(function (a, b) { return Rcmp(a.capacity, b.capacity) || (a.S.length - b.S.length); });
    var best = out.length ? out[0].capacity : R0, minimum = [];
    for (i = 0; i < out.length; i += 1) if (Requ(out[i].capacity, best)) minimum.push(i);
    return { cuts: out, min: best, minimum: minimum };
  }
"""

MATCH_JS = r"""
  /* The bipartite editor, the reduction to a flow network, and the cut that
     reduction produces.  The matching mode only. */

  /* `1-a, 2-b` : the left vertex, a dash, the right vertex.  Sides are kept
     apart by position rather than by name, so a graph may use the same letter
     on both sides without the two becoming one vertex. */
  function parseBip(text) {
    var cl = netClauses(text), left = [], right = [], edges = [], ls = {}, rs = {}, i;
    if (!cl.length) return { bad: 'there are no edges here yet' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z0-9][A-Za-z0-9]{0,3})\s*-\s*([A-Za-z0-9][A-Za-z0-9]{0,3})$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not an edge: write a left vertex, a dash, a right one' };
      if (!ls[m[1]]) { ls[m[1]] = true; left.push(m[1]); }
      if (!rs[m[2]]) { rs[m[2]] = true; right.push(m[2]); }
      edges.push([m[1], m[2]]);
    }
    if (left.length > 5 || right.length > 5) {
      return { bad: 'that is ' + left.length + ' on the left and ' + right.length
                    + ' on the right; this drawing takes five a side' };
    }
    return { left: left, right: right, edges: edges };
  }

  /* The reduction, as a function rather than as six lines inside a redraw:
     a unit arc from the source to every applicant, every original edge at
     capacity one, and a unit arc from every job to the sink.  A flow of value
     k is a matching of size k.  It lives here because a helper closed over the
     drawing cannot be checked by scripts/mathcheck.js, and the whole claim of
     the lesson is that the cut of THIS network is Hall's deficient set. */
  function matchingNetwork(left, right, edges) {
    var nodes = ['src'], arcs = [], i;
    for (i = 0; i < left.length; i += 1) {
      nodes.push('L' + left[i]);
      arcs.push({ from: 'src', to: 'L' + left[i], cap: R1, cost: R0, capped: true });
    }
    for (i = 0; i < right.length; i += 1) nodes.push('R' + right[i]);
    for (i = 0; i < edges.length; i += 1) {
      arcs.push({ from: 'L' + edges[i][0], to: 'R' + edges[i][1], cap: R1, cost: R0, capped: true });
    }
    for (i = 0; i < right.length; i += 1) {
      arcs.push({ from: 'R' + right[i], to: 'snk', cap: R1, cost: R0, capped: true });
    }
    nodes.push('snk');
    return { nodes: nodes, arcs: arcs };
  }

  /* The source side of that network's minimum cut: the source, the applicants
     an alternating path reaches from an unmatched one, and the jobs they can
     take.  bipartiteMatch has already computed both halves -- `deficient.S` and
     `deficient.N` ARE that reachable set -- so this names the cut rather than
     searching for it a second time. */
  function matchingCut(match) {
    var S = ['src'], i;
    for (i = 0; i < match.deficient.S.length; i += 1) S.push('L' + match.deficient.S[i]);
    for (i = 0; i < match.deficient.N.length; i += 1) S.push('R' + match.deficient.N[i]);
    return S;
  }
"""

PROJECT_JS = r"""
  /* Activities, precedences, and what shortening one is worth.  The project
     mode only -- and note that nothing here solves a linear programme, which
     is why that page carries no simplex at all. */

  /* `A 3, B 2 after A, D 2 after B C` : an activity, its duration, and the
     activities that must finish first. */
  function parseActs(text) {
    var cl = netClauses(text), acts = [], seen = {}, i, k;
    if (!cl.length) return { bad: 'there are no activities here yet' };
    if (cl.length > 12) return { bad: 'that is ' + cl.length + ' activities, and this table shows twelve' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z][A-Za-z0-9]{0,2})\s+([0-9]+(?:\/[0-9]+)?)\s*(?:after\s+(.*))?$/i.exec(cl[i]);
      if (!m) {
        return { bad: '"' + esc(cl[i]) + '" is not an activity: write its name, its duration, and '
                      + 'then "after" and the activities it waits for' };
      }
      if (seen[m[1]]) return { bad: 'there are two activities called ' + m[1] };
      var dur = Rread(m[2]);
      if (dur === null || Rsign(dur) < 0) return { bad: '"' + esc(m[2]) + '" is not a duration' };
      var preds = [];
      if (m[3]) {
        var ps = m[3].trim().split(/[\s]+/);
        for (k = 0; k < ps.length; k += 1) if (ps[k]) preds.push(ps[k]);
      }
      seen[m[1]] = true;
      acts.push({ id: m[1], dur: dur, pred: preds });
    }
    for (i = 0; i < acts.length; i += 1) {
      for (k = 0; k < acts[i].pred.length; k += 1) {
        if (!seen[acts[i].pred[k]]) {
          return { bad: acts[i].id + ' waits for ' + acts[i].pred[k] + ', which is not an activity here' };
        }
      }
    }
    return { acts: acts };
  }

  /* How far a critical activity can be shortened before it stops paying.  Not
     a formula: the project is recomputed at every length, because the answer
     is "until a SECOND path becomes critical" and which path that is depends
     on the whole network. */
  function crashCurve(acts, id, maxCut) {
    var out = [], k, i;
    for (k = 0; k <= maxCut; k += 1) {
      var trial = [];
      for (i = 0; i < acts.length; i += 1) {
        trial.push(acts[i].id === id
          ? { id: acts[i].id, dur: Rsub(acts[i].dur, R(BigInt(k), 1n)), pred: acts[i].pred }
          : acts[i]);
      }
      if (Rsign(trial[0].dur) < 0) break;
      var pass = cpmPasses(trial);
      if (!pass || pass.cycle) break;
      out.push({ cut: k, makespan: pass.makespan, paths: pass.paths ? pass.paths.length : 0,
                 critical: pass.critical });
    }
    var stops = 0;
    for (k = 1; k < out.length; k += 1) {
      if (Rcmp(out[k].makespan, out[k - 1].makespan) < 0) stops = k; else break;
    }
    return { steps: out, lastUseful: stops };
  }
"""



# ---------------------------------------------------------------------------
# One core per mode, not one for the kit. Each mode names the blocks it calls
# and no others, which is the largest single lever there is on page weight:
# `cpm` has no linear programme in it and must not ship a simplex to a reader,
# and `tu` has no residual network and must not ship a cut enumeration.
# ---------------------------------------------------------------------------

_BASE_JS = RATIONAL_JS + FORMAT_JS + ORFMT_JS + NET_JS + NETKIT_JS
_LPBASE_JS = RATIONAL_JS + FORMAT_JS + ORFMT_JS + TABLEAU_JS + PHASE_JS + NET_JS + NETKIT_JS

_DIGRAPH_JS = _BASE_JS + CHECK_JS
_MINCOST_JS = _LPBASE_JS + MODEL_JS
_TU_CORE_JS = (RATIONAL_JS + FORMAT_JS + MATRIX_JS + ORFMT_JS + TABLEAU_JS + PHASE_JS
               + NET_JS + NETKIT_JS + MODEL_JS)
_BELLMAN_JS = _BASE_JS
_MAXFLOW_JS = RATIONAL_JS + FORMAT_JS + ORFMT_JS + DUAL_JS + NET_JS + NETKIT_JS + CUT_JS
_MATCHING_JS = _BASE_JS + MATCH_JS
_CPM_JS = _BASE_JS + PROJECT_JS


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the rest of the library uses, so a reader
# crossing a course boundary meets the same widgets. Drawings use only the two
# viewBox widths theme.py gives a horizontal-scroll minimum -- 520 and 660 --
# because any other width shrinks the labels to illegibility on a phone
# instead of scrolling.
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

    Every arc a reader types on this course contains a `>`, and a default
    carried in the markup cannot hold one. Escaped as `&gt;` a browser decodes
    it and scripts/labcheck.js does not, so the harness would run all seven of
    these pages against a spec of literal entities and prove nothing; left raw
    it terminates the `<input ...>` match in that harness's own tag scanner and
    the value is lost instead. Either way the one harness that executes these
    labs would be executing the error branch.

    So the value goes in as a string the script assigns before its first
    redraw. `value` is still taken here, and still written into the page -- as
    a placeholder, which carries no `>` -- so the parameter at each call site
    still says what the box is for.
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


def _buttons(items):
    return ('        <div class="btn-row">%s</div>\n'
            % "".join('<button class="btn" id="%s" type="button">%s</button>' % (cid, text)
                      for cid, text in items))


def _hint(cid, text):
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
    """A JavaScript single-quoted string literal for a preset's own text."""
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


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


# ---------------------------------------------------------------------------
# L1 -- digraph: an arc is ordered, and conservation is local
# ---------------------------------------------------------------------------

_DG_PRESETS = [
    {
        "id": "twoway",
        "label": "a lane each way, and a flow that works",
        "spec": "s>a 5:2, a>b 4:2, b>a 3:5, a>t 3:1, b>t 4:3",
        "supply": "s:4, t:-4",
        "flow": "s>a 4, a>b 2, b>a 0, a>t 2, b>t 2",
        "note": "a to b and b to a are two arcs with two capacities and two costs",
    },
    {
        "id": "local",
        "label": "balances in total, fails at two nodes",
        "spec": "s>a 5:2, a>b 4:2, b>a 3:5, a>t 3:1, b>t 4:3",
        "supply": "s:4, t:-4",
        "flow": "s>a 4, a>b 1, b>a 0, a>t 2, b>t 2",
        "note": "the imbalances cancel across the network and the flow is still not a flow",
    },
    {
        "id": "overcap",
        "label": "conserved everywhere, over capacity twice",
        "spec": "s>a 5:2, a>b 4:2, b>a 3:5, a>t 3:1, b>t 4:3",
        "supply": "s:5, t:-5",
        "flow": "s>a 5, a>b 5, b>a 0, a>t 0, b>t 5",
        "note": "every node balances and two arcs are asked to carry more than they can",
    },
    {
        "id": "unbalanced",
        "label": "more supply than demand",
        "spec": "s>a 5:2, a>b 4:2, b>a 3:5, a>t 3:1, b>t 4:3",
        "supply": "s:6, t:-4",
        "flow": "s>a 4, a>b 2, b>a 0, a>t 2, b>t 2",
        "note": "adding the node equations up gives 2 = 0, so nothing can satisfy them",
    },
]


def _digraph(cfg):
    preset = str(cfg.get("preset", _DG_PRESETS[0]["id"]))
    chosen = next((p for p in _DG_PRESETS if p["id"] == preset), _DG_PRESETS[0])

    markup = (
        _toolbar(
            "Arcs, capacities and conservation",
            "an arc is ordered: a to b and b to a are two objects",
            [("cyan", "an arc inside its capacity"), ("red", "over capacity, or a node that fails"),
             ("purple", "an arc whose reverse is also here")],
        )
        + _stage(_svg("dgPlot", "0 0 660 300",
                      "The directed network, each arc labelled with the flow it carries out of its "
                      "capacity and the cost per unit.")
                 + _svg("dgBal", "0 0 660 46",
                        "A strip showing each node's net outflow against the amount it must supply."))
        + _table("dgNodes")
        + _table("dgArcs")
        + _banner("dgStatus")
    )
    controls = (
        _select("dgPreset", "Worked example", _options(_DG_PRESETS), chosen["id"])
        + _text("dgSpec", "Arcs, as tail&gt;head capacity:cost", chosen["spec"])
        + _text("dgSupply", "What each node must supply", chosen["supply"])
        + _text("dgFlow", "The flow to check", chosen["flow"])
        + _kpis(
            [
                ("Total cost of this flow", "dgCost"),
                ("Nodes where conservation fails", "dgViolated"),
                ("Arcs over capacity", "dgOver"),
                ("Supply minus demand, summed", "dgTotal"),
                ("Arcs whose reverse is also here", "dgAnti"),
                ("Is this a flow?", "dgVerdict"),
            ]
        )
        + _hint(
            "dgHint",
            "An arc is <span class=\"tt\">tail&gt;head capacity:cost</span> and the capacity may be "
            "<span class=\"tt\">*</span> for no bound. Write <span class=\"tt\">a&gt;b 4:2</span> and "
            "<span class=\"tt\">b&gt;a 3:5</span> and you have two arcs, not one edge with an arrow: "
            "they carry different amounts at different prices and the flow names each separately.",
        )
    )

    script = _DIGRAPH_JS + r"""
""" + _presets_js("DGP", _DG_PRESETS, ["spec", "supply", "flow", "note"]) + r"""
  var presetIn = document.getElementById('dgPreset');
  var specIn = document.getElementById('dgSpec'), supIn = document.getElementById('dgSupply');
  var flowIn = document.getElementById('dgFlow');
  var plot = document.getElementById('dgPlot'), bal = document.getElementById('dgBal');
  var nodesT = document.getElementById('dgNodes'), arcsT = document.getElementById('dgArcs');
  var status = document.getElementById('dgStatus');
  var KPIS = ['dgCost', 'dgViolated', 'dgOver', 'dgTotal', 'dgAnti', 'dgVerdict'];

  function blank(why) {
    plot.innerHTML = ''; bal.innerHTML = ''; nodesT.innerHTML = ''; arcsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Each clause is a tail, then '
      + '<span class="tone-muted">&gt;</span>, then a head, then the capacity and the cost separated '
      + 'by a colon.';
  }

  function redraw() {
    var net = parseNet(specIn.value, ['capacity', 'cost']);
    if (net.bad) { blank(net.bad); return; }
    var sup = parseSupply(supIn.value, net.nodes);
    if (sup.bad) { blank(sup.bad); return; }
    var fl = parseFlow(flowIn.value, net.arcs);
    if (fl.bad) { blank(fl.bad); return; }

    var cons = conservation(net.nodes, net.arcs, fl.flow, sup.supply);
    var caps = capacityCheck(net.arcs, fl.flow);
    var cost = flowCost(net.arcs, fl.flow);
    var anti = antiparallel(net.arcs), antiSet = {}, i, j;
    for (i = 0; i < anti.length; i += 1) antiSet[anti[i][0]] = true;
    var badNode = {};
    for (i = 0; i < cons.violated.length; i += 1) badNode[cons.violated[i]] = true;
    var badArc = {};
    for (i = 0; i < caps.over.length; i += 1) badArc[caps.over[i]] = true;

    var layout = netLayout(net.nodes, net.arcs, 660, 288);
    plot.innerHTML = drawNet(net.nodes, net.arcs, layout, {
      label: function (k) {
        return Rtext(fl.flow[k]) + ' of ' + capText(net.arcs[k]) + ' at ' + Rtext(net.arcs[k].cost);
      },
      tone: function (k) { return badArc[k] ? 'red' : (antiSet[k] ? 'purple' : 'cyan'); },
      wide: function (k) { return Rsign(fl.flow[k]) > 0; },
      dash: function (k) { return Rzero(fl.flow[k]); },
      nodeRing: function (v) { return badNode[v] ? 'red' : null; },
      under: function (v) {
        var r = null;
        for (var k = 0; k < cons.rows.length; k += 1) if (cons.rows[k].node === v) r = cons.rows[k];
        return r && !Rzero(r.want) ? 'must net ' + Rtext(r.want) : null;
      }
    }) + netCaption('each arc reads  flow of capacity at cost per unit', 660, 300);

    var strip = '', wide = 660 / Math.max(1, cons.rows.length);
    for (i = 0; i < cons.rows.length; i += 1) {
      var r = cons.rows[i], x = wide * (i + 0.5);
      strip += '<text x="' + Math.round(x) + '" y="18" text-anchor="middle" font-size="11" '
        + 'font-weight="700" fill="var(--' + (r.ok ? 'green' : 'red') + ')">' + r.node + ': '
        + Rtext(r.net) + '</text>'
        + '<text x="' + Math.round(x) + '" y="34" text-anchor="middle" font-size="10" '
        + 'fill="var(--muted)">needs ' + Rtext(r.want) + '</text>';
    }
    bal.innerHTML = strip;

    var rows = '';
    for (i = 0; i < cons.rows.length; i += 1) {
      var c = cons.rows[i];
      rows += tr([rowhead(c.node), td(Rtext(c.out)), td(Rtext(c.into)), td(Rtext(c.net)),
                  td(Rtext(c.want)),
                  td(c.ok ? tone('balances', 'green') : tone('off by ' + Rtext(Rsub(c.net, c.want)), 'red'))],
                 c.ok ? null : 'tone-red');
    }
    nodesT.innerHTML = '<caption>Conservation, one equation per node</caption><thead>'
      + tr([th('node'), th('out'), th('in'), th('out &minus; in'), th('must net'), th('verdict')])
      + '</thead><tbody>' + rows + '</tbody><tfoot>' + tr([tdl('Adding every row of this table gives '
      + Rtext(cons.net.reduce(function (a, b) { return Radd(a, b); }, R0)) + ' on the left, because every '
      + 'arc is counted once out of its tail and once into its head. So the supplies must sum to zero '
      + 'before any flow can exist — a test you can run before solving anything.', 'small-copy')
      .replace('<td', '<td colspan="6"')]) + '</tfoot>';

    var arows = '';
    for (j = 0; j < net.arcs.length; j += 1) {
      var a = net.arcs[j], cr = caps.rows[j];
      arows += tr([rowhead(a.from + ' &rarr; ' + a.to), td(Rtext(cr.flow)), td(capText(a)),
                   td(cr.slack === null ? 'no bound' : Rtext(cr.slack)), td(Rtext(a.cost)),
                   td(Rtext(Rmul(a.cost, cr.flow))),
                   td(cr.ok ? tone('fits', 'green') : tone(cr.negative ? 'negative' : 'over', 'red'))],
                  cr.ok ? (antiSet[j] ? 'tone-purple' : null) : 'tone-red');
    }
    arcsT.innerHTML = '<caption>Every arc separately, because every arc is a separate variable</caption>'
      + '<thead>' + tr([th('arc'), th('flow'), th('capacity'), th('spare'), th('cost each'),
                        th('cost here'), th('verdict')]) + '</thead><tbody>' + arows + '</tbody>';

    document.getElementById('dgCost').textContent = Rtext(cost);
    document.getElementById('dgViolated').textContent = cons.violated.length
      ? cons.violated.join(', ') : 'none';
    document.getElementById('dgOver').textContent = caps.over.length ? caps.over.map(function (k) {
      return net.arcs[k].from + '→' + net.arcs[k].to; }).join(', ') : 'none';
    document.getElementById('dgTotal').textContent = Rtext(sup.total)
      + (Rzero(sup.total) ? ' — balanced' : ' — no flow can exist');
    document.getElementById('dgAnti').textContent = anti.length
      ? (anti.length / 2) + ' pair' + plural(anti.length / 2, '', 's') : 'none';
    var good = cons.ok && caps.ok && Rzero(sup.total);
    document.getElementById('dgVerdict').textContent = good ? 'yes' : 'no';

    var parts = [];
    if (!Rzero(sup.total)) {
      parts.push('the supplies add up to ' + tone(Rtext(sup.total), 'red') + ' rather than zero, and '
        + 'adding the node equations together gives that same number on the left of 0 = 0, so this '
        + 'network has no feasible flow at all');
    }
    if (cons.violated.length) {
      var first = null;
      for (i = 0; i < cons.rows.length; i += 1) if (!cons.rows[i].ok && first === null) first = cons.rows[i];
      parts.push('conservation fails at ' + tone(cons.violated.join(' and '), 'red') + ' — ' + first.why);
    }
    if (caps.over.length) {
      var a0 = net.arcs[caps.over[0]];
      parts.push('the flow on ' + tone(a0.from + ' &rarr; ' + a0.to, 'red') + ' is '
        + Rtext(caps.rows[caps.over[0]].flow) + ' where the arc holds ' + capText(a0));
    }
    status.innerHTML = (good
        ? '<strong>' + tone('This is a flow.', 'green') + '</strong> Every node sends out exactly what '
          + 'it takes in plus what it supplies, every arc is inside its capacity, and it costs '
          + tone(Rtext(cost), 'cyan') + '. '
        : '<strong>' + tone('This is not a flow.', 'red') + '</strong> ' + parts.join('; ') + '. ')
      + (anti.length
          ? 'Notice ' + tone(net.arcs[anti[0][0]].from + ' &rarr; ' + net.arcs[anti[0][0]].to
              + ' and ' + net.arcs[anti[0][1]].from + ' &rarr; ' + net.arcs[anti[0][1]].to, 'purple')
            + ': two arcs, two capacities, two costs and two variables. Sending along one does not '
            + 'cancel the other, and the table above prices them apart.'
          : 'Add the reverse of any arc and it appears as a second row with its own capacity and its '
            + 'own price — an arc is ordered, and the pair is not one edge with an arrow drawn on it.');
  }

  function apply() {
    var p = DGP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; supIn.value = p.supply; flowIn.value = p.flow;
    redraw();
  }
  var START = DGP[presetIn.value];
  if (START) {
    if (!specIn.value) specIn.value = START.spec;
    if (!supIn.value) supIn.value = START.supply;
    if (!flowIn.value) flowIn.value = START.flow;
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  supIn.addEventListener('input', redraw);
  flowIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Arcs, capacities and conservation",
        subtitle="Two arcs between the same pair are two variables — and conservation is checked node by node",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the network, the supplies and a flow"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every number below is recomputed from what you type: the net outflow at each node, the "
            "spare capacity on each arc, and the cost. Nothing is stored.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 -- mincost: one linear programme, five data sets
# ---------------------------------------------------------------------------

_MC_PRESETS = [
    {
        "id": "mincost",
        "label": "minimum-cost flow",
        "spec": "s>a 3:2, s>b 3:3, a>b 2:1, a>t 3:5, b>t 3:2",
        "supply": "s:4, t:-4",
        "note": "four units from s to t, every arc bounded and priced",
    },
    {
        "id": "transport",
        "label": "the transportation problem",
        "spec": "S1>D1 *:4, S1>D2 *:6, S1>D3 *:9, S2>D1 *:5, S2>D2 *:3, S2>D3 *:8",
        "supply": "S1:20, S2:30, D1:-10, D2:-25, D3:-15",
        "note": "sources on one side, sinks on the other, and no capacity anywhere",
    },
    {
        "id": "assignment",
        "label": "the assignment problem",
        "spec": ("W1>J1 1:9, W1>J2 1:2, W1>J3 1:7, W2>J1 1:6, W2>J2 1:4, W2>J3 1:3, "
                 "W3>J1 1:5, W3>J2 1:8, W3>J3 1:1"),
        "supply": "W1:1, W2:1, W3:1, J1:-1, J2:-1, J3:-1",
        "note": "transportation with every supply and every demand set to one",
    },
    {
        "id": "shortest",
        "label": "a shortest path",
        "spec": "s>a 1:4, s>b 1:2, b>a 1:1, a>t 1:3, b>t 1:7",
        "supply": "s:1, t:-1",
        "note": "one unit from s to t: the cheapest way to move it is the cheapest path",
    },
    {
        "id": "maxflow",
        "label": "a maximum flow",
        "spec": "s>a 3:0, s>b 2:0, a>b 2:0, a>t 2:0, b>t 3:0, t>s *:-1",
        "supply": "",
        "note": ("every arc free, a return arc from t to s priced at minus one, and nothing supplied "
                 "anywhere, so minimising the cost maximises the flow and the optimum is minus the "
                 "flow value"),
    },
]


def _mincost(cfg):
    preset = str(cfg.get("preset", _MC_PRESETS[0]["id"]))
    chosen = next((p for p in _MC_PRESETS if p["id"] == preset), _MC_PRESETS[0])

    markup = (
        _toolbar(
            "One linear programme, four special cases",
            "N x = b, 0 &#8804; x &#8804; u, minimise c&#8242;x",
            [("cyan", "an arc carrying flow"), ("muted", "an arc left empty"),
             ("amber", "the data that changed")],
        )
        + _stage(_svg("mcPlot", "0 0 660 300",
                      "The network, each arc labelled with the flow the linear programme gives it, "
                      "its capacity and its cost."))
        + _table("mcN")
        + _table("mcData")
        + _table("mcSol")
        + _banner("mcStatus")
    )
    controls = (
        _select("mcCase", "The data set", _options(_MC_PRESETS), chosen["id"])
        + _text("mcSpec", "Arcs, as tail&gt;head capacity:cost", chosen["spec"])
        + _text("mcSupply", "b, as node:amount", chosen["supply"])
        + _kpis(
            [
                ("Which problem this is", "mcKind"),
                ("Shape of N", "mcShape"),
                ("Optimal cost", "mcZ"),
                ("Every flow a whole number?", "mcInt"),
                ("Arcs carrying flow", "mcUsed"),
                ("Simplex pivots", "mcPivots"),
            ]
        )
        + _hint(
            "mcHint",
            "The matrix below is built from the arcs by one rule &mdash; <span class=\"tt\">+1</span> in "
            "the tail's row, <span class=\"tt\">&minus;1</span> in the head's &mdash; and it is the same "
            "matrix for every data set in the list. Change the capacities, the costs or the supplies and "
            "you change the problem; the programme stays where it is.",
        )
    )

    script = _MINCOST_JS + r"""
""" + _presets_js("MCP", _MC_PRESETS, ["spec", "supply", "note", "label"]) + r"""
  var caseIn = document.getElementById('mcCase');
  var specIn = document.getElementById('mcSpec'), supIn = document.getElementById('mcSupply');
  var plot = document.getElementById('mcPlot');
  var matT = document.getElementById('mcN'), dataT = document.getElementById('mcData');
  var solT = document.getElementById('mcSol'), status = document.getElementById('mcStatus');
  var KPIS = ['mcKind', 'mcShape', 'mcZ', 'mcInt', 'mcUsed', 'mcPivots'];

  function blank(why) {
    plot.innerHTML = ''; matT.innerHTML = ''; dataT.innerHTML = ''; solT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tone-muted">tail&gt;head capacity:cost</span>, and a capacity of '
      + '<span class="tone-muted">*</span> means the arc has no upper bound at all.';
  }

  function redraw() {
    var net = parseNet(specIn.value, ['capacity', 'cost']);
    if (net.bad) { blank(net.bad); return; }
    var sup = parseSupply(supIn.value, net.nodes);
    if (sup.bad) { blank(sup.bad); return; }
    var model = mcfModel(net.nodes, net.arcs, sup.supply);
    var solved = lpSolve(model);
    var i, j;

    var flow = [];
    for (j = 0; j < net.arcs.length; j += 1) {
      flow.push(solved.x && solved.x[j] !== undefined ? solved.x[j] : R0);
    }
    var integral = true, used = 0;
    for (j = 0; j < flow.length; j += 1) {
      if (!Rint(flow[j])) integral = false;
      if (!Rzero(flow[j])) used += 1;
    }
    var feasible = solved.status === 'optimal';

    var layout = netLayout(net.nodes, net.arcs, 660, 288);
    plot.innerHTML = drawNet(net.nodes, net.arcs, layout, {
      label: function (k) {
        return (feasible ? Rtext(flow[k]) + ' of ' : '') + capText(net.arcs[k])
          + ' at ' + Rtext(net.arcs[k].cost);
      },
      tone: function (k) { return feasible && !Rzero(flow[k]) ? 'cyan' : 'muted'; },
      wide: function (k) { return feasible && !Rzero(flow[k]); },
      dash: function (k) { return !feasible || Rzero(flow[k]); },
      under: function (v) {
        return Rzero(sup.supply[v]) ? null : 'b = ' + Rtext(sup.supply[v]);
      }
    }) + netCaption(feasible ? 'each arc reads  flow of capacity at cost per unit'
                             : 'no flow satisfies these supplies', 660, 300);

    var heads = [th('node')], rows = '';
    for (j = 0; j < net.arcs.length; j += 1) {
      heads.push(th(net.arcs[j].from + '&rarr;' + net.arcs[j].to));
    }
    heads.push(th('b'));
    for (i = 0; i < net.nodes.length; i += 1) {
      var cells = [rowhead(net.nodes[i])];
      for (j = 0; j < net.arcs.length; j += 1) {
        var v = model.N[i][j];
        cells.push(td(Rzero(v) ? '<span class="tone-muted">0</span>'
          : tone(Rsign(v) > 0 ? '+1' : '&minus;1', Rsign(v) > 0 ? 'cyan' : 'purple')));
      }
      cells.push(td(tone(Rtext(sup.supply[net.nodes[i]]), 'amber')));
      rows += tr(cells);
    }
    matT.innerHTML = '<caption>N, the node&ndash;arc incidence matrix, and b</caption><thead>'
      + tr(heads) + '</thead><tbody>' + rows + '</tbody>';

    var capsText = [], costText = [];
    for (j = 0; j < net.arcs.length; j += 1) {
      capsText.push(capText(net.arcs[j]));
      costText.push(Rtext(net.arcs[j].cost));
    }
    var bText = [];
    for (i = 0; i < net.nodes.length; i += 1) {
      bText.push(net.nodes[i] + ' ' + Rtext(sup.supply[net.nodes[i]]));
    }
    dataT.innerHTML = '<caption>What the programme is, and what the data are</caption><tbody>'
      + tr([rowhead('the model'), tdl('minimise c&#8242;x subject to N x = b and 0 &#8804; x &#8804; u '
          + '&mdash; identical in every data set on this list')])
      + tr([rowhead('N'), tdl(net.nodes.length + ' by ' + net.arcs.length
          + ', built from the arcs and from nothing else')])
      + tr([rowhead('b'), tdl(tone(bText.join(', '), 'amber'))])
      + tr([rowhead('u'), tdl(tone(capsText.join(', '), 'amber'))])
      + tr([rowhead('c'), tdl(tone(costText.join(', '), 'amber'))])
      + '</tbody>';

    var srows = '';
    for (j = 0; j < net.arcs.length; j += 1) {
      srows += tr([rowhead(net.arcs[j].from + ' &rarr; ' + net.arcs[j].to),
                   td(capText(net.arcs[j])), td(Rtext(net.arcs[j].cost)),
                   td(feasible ? Rtext(flow[j]) : '&mdash;'),
                   td(feasible ? Rtext(Rmul(net.arcs[j].cost, flow[j])) : '&mdash;')],
                  feasible && !Rzero(flow[j]) ? 'tone-cyan' : 'tone-muted');
    }
    solT.innerHTML = '<caption>The solution, arc by arc</caption><thead>'
      + tr([th('arc'), th('u'), th('c'), th('x'), th('c x')]) + '</thead><tbody>' + srows
      + '</tbody>';

    document.getElementById('mcKind').textContent = MCP[caseIn.value]
      ? MCP[caseIn.value].label : 'a network you typed';
    document.getElementById('mcShape').textContent = net.nodes.length + ' rows by '
      + net.arcs.length + ' columns';
    document.getElementById('mcZ').textContent = feasible ? Rtext(solved.zOrig) : solved.status;
    document.getElementById('mcInt').textContent = feasible
      ? (integral ? 'yes, every one' : 'no') : '—';
    document.getElementById('mcUsed').textContent = feasible ? used + ' of ' + net.arcs.length : '—';
    document.getElementById('mcPivots').textContent = solved.run ? solved.run.pivots : '—';

    if (!feasible) {
      status.innerHTML = '<strong>' + tone('No flow exists.', 'red') + '</strong> The simplex reports '
        + solved.status + '. Adding the rows of N together gives zero on the left, because every arc '
        + 'leaves one node and enters another, so the supplies must sum to zero before anything else '
        + 'can be true &mdash; and here they sum to ' + tone(Rtext(sup.total), 'red') + '.';
      return;
    }
    status.innerHTML = '<strong>' + tone('Optimal cost ' + Rtext(solved.zOrig) + '.', 'cyan')
      + '</strong> ' + (MCP[caseIn.value] ? 'This is ' + MCP[caseIn.value].label + ': '
          + MCP[caseIn.value].note + '. ' : '')
      + 'Nothing about the programme changed to get it &mdash; the matrix is still N, the constraint is '
      + 'still N x = b, and the objective is still c&#8242;x. '
      + (integral
          ? 'Every flow came out a whole number, on integer data, with no rounding and no integrality '
            + 'constraint anywhere in the programme. That is a property of N, and the integrality '
            + 'lesson is where it is proved.'
          : 'Some flow came out fractional, which on a network is worth investigating: the supplies or '
            + 'the capacities here are not whole numbers.')
      + ' Minimum-cost flow also has an algorithm of its own &mdash; augment along the cheapest path in '
      + 'the residual network, which keeps the flow cheapest for its value &mdash; and this programme is '
      + 'the reference solution that settles every instance on this course exactly.';
  }

  function apply() {
    var p = MCP[caseIn.value];
    if (!p) return;
    specIn.value = p.spec; supIn.value = p.supply;
    redraw();
  }
  var START = MCP[caseIn.value];
  if (START) {
    if (!specIn.value) specIn.value = START.spec;
    if (!supIn.value) supIn.value = START.supply;
  }
  caseIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  supIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The minimum-cost flow model",
        subtitle="Transportation, assignment, shortest path and maximum flow are this programme with different data",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Change the data, not the model"),
        panel_intro=cfg.get(
            "panel_intro",
            "N is built from the arcs you type and the exact simplex solves the programme in rationals. "
            "Switching the data set changes b, u and c and nothing else.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 -- tu: the determinants that make the corners whole
# ---------------------------------------------------------------------------

# Two rules for building an incidence matrix from the same drawing, and the
# determinant is the whole difference between them. This is the one block only
# `tu` ships, because it is the one mode that takes Mdet.
TU_JS = r"""
  /* The OTHER incidence matrix: +1 at BOTH endpoints, which is what an
     undirected edge gives you.  This is not an alternative convention -- it is
     a different matrix with different determinants, and on an odd cycle its
     determinant is 2.  A reader arriving from an undirected graph kit has been
     handed this matrix all along, which is exactly why the rule is a control
     here rather than a footnote. */
  function incidenceUndirected(nodes, arcs) {
    var ix = netIndex(nodes), M = [], i, j;
    for (i = 0; i < nodes.length; i += 1) {
      var row = [];
      for (j = 0; j < arcs.length; j += 1) {
        row.push((ix[arcs[j].from] === i || ix[arcs[j].to] === i) ? R1 : R0);
      }
      M.push(row);
    }
    return M;
  }

  /* max 1'x subject to Mx <= 1, x >= 0 : the fractional relaxation whose
     corners are half-integral exactly when M is not unimodular.  On an odd
     cycle every basic solution has denominator 2 and the optimum is 3/2. */
  function packingModel(M, names) {
    var m = M.length, n = m ? M[0].length : 0, obj = [], cons = [], i, j;
    for (j = 0; j < n; j += 1) obj.push(R1);
    for (i = 0; i < m; i += 1) cons.push({ a: M[i].slice(), rel: 'le', b: R1, name: 'row ' + (i + 1) });
    return { max: true, names: names, obj: obj, cons: cons };
  }

  /* "1,3,4" as zero-based indices into something of length n, refusing what is
     out of range rather than silently clamping it -- a clamped pick is a
     determinant of a submatrix the reader did not choose. */
  function pickIndices(text, n, what) {
    var parts = String(text).split(/[,\s]+/), out = [], seen = {}, i;
    for (i = 0; i < parts.length; i += 1) {
      if (!parts[i]) continue;
      if (!/^[0-9]+$/.test(parts[i])) return { bad: '"' + esc(parts[i]) + '" is not a ' + what + ' number' };
      var v = Number(parts[i]);
      if (v < 1 || v > n) return { bad: 'there is no ' + what + ' ' + v + '; there are ' + n };
      if (seen[v]) return { bad: what + ' ' + v + ' is named twice, and a matrix with a repeated '
                                 + what + ' has determinant zero for a reason that is not about networks' };
      seen[v] = true;
      out.push(v - 1);
    }
    if (!out.length) return { bad: 'name at least one ' + what };
    return { pick: out };
  }
"""

_TU_PRESETS = [
    {
        "id": "network",
        "label": "a network, +1 at the tail and −1 at the head",
        "spec": "s>a 3:2, s>b 3:3, a>b 2:1, a>t 3:5, b>t 3:2",
        "supply": "s:4, t:-4",
        "rule": "directed",
        "rows": "1,2,3",
        "cols": "1,3,4",
    },
    {
        "id": "triangle",
        "label": "a triangle, +1 at both ends",
        "spec": "1>2 1:1, 2>3 1:1, 3>1 1:1",
        "supply": "",
        "rule": "undirected",
        "rows": "1,2,3",
        "cols": "1,2,3",
    },
    {
        "id": "square",
        "label": "a four-cycle, +1 at both ends",
        "spec": "1>2 1:1, 2>3 1:1, 3>4 1:1, 4>1 1:1",
        "supply": "",
        "rule": "undirected",
        "rows": "1,2,3,4",
        "cols": "1,2,3,4",
    },
]


def _tu(cfg):
    preset = str(cfg.get("preset", _TU_PRESETS[0]["id"]))
    chosen = next((p for p in _TU_PRESETS if p["id"] == preset), _TU_PRESETS[0])

    markup = (
        _toolbar(
            "Every square submatrix, and what its determinant costs",
            "det B = &plusmn;1 makes B&#8315;&#185;b whole; det B = 2 makes it halves",
            [("cyan", "a determinant in {0, +1, −1}"), ("red", "a determinant outside it"),
             ("purple", "the rows and columns you picked")],
        )
        + _stage(_svg("tuPlot", "0 0 520 250",
                      "The graph the matrix is built from, with the picked columns marked."))
        + _table("tuMatrix")
        + _table("tuSweep")
        + _table("tuCorner")
        + _banner("tuStatus")
    )
    controls = (
        _select("tuCase", "Worked example", _options(_TU_PRESETS), chosen["id"])
        + _text("tuSpec", "The graph, as tail&gt;head capacity:cost", chosen["spec"])
        + _select("tuRule", "How the matrix is built",
                  [("directed", "+1 at the tail, −1 at the head"),
                   ("undirected", "+1 at both ends")], chosen["rule"])
        + _text("tuRows", "Rows to take", chosen["rows"])
        + _text("tuCols", "Columns to take", chosen["cols"])
        + _range("tuK", "Sweep every submatrix up to order", 1, 3, 3)
        + _kpis(
            [
                ("Shape", "tuShape"),
                ("Determinants checked", "tuChecked"),
                ("Any outside {0, +1, −1}?", "tuBad"),
                ("The picked determinant", "tuPick"),
                ("What the corner comes out as", "tuCorner2"),
                ("Denominator of the corner", "tuDenom"),
            ]
        )
        + _hint(
            "tuHint",
            "The sweep is exhaustive up to the order the slider sets, and stops at three because the "
            "count grows as the product of two binomial coefficients &mdash; eight nodes and twelve arcs "
            "give 12&nbsp;320 determinants at order three and 34&nbsp;650 at order four. Above three, "
            "pick the rows and columns yourself and the lab says which it did.",
        )
    )

    script = _TU_CORE_JS + TU_JS + r"""
""" + _presets_js("TUP", _TU_PRESETS, ["spec", "supply", "rule", "rows", "cols", "label"]) + r"""
  var caseIn = document.getElementById('tuCase'), specIn = document.getElementById('tuSpec');
  var ruleIn = document.getElementById('tuRule'), rowsIn = document.getElementById('tuRows');
  var colsIn = document.getElementById('tuCols'), kIn = document.getElementById('tuK');
  var plot = document.getElementById('tuPlot'), matT = document.getElementById('tuMatrix');
  var sweepT = document.getElementById('tuSweep'), cornT = document.getElementById('tuCorner');
  var status = document.getElementById('tuStatus');
  var KPIS = ['tuShape', 'tuChecked', 'tuBad', 'tuPick', 'tuCorner2', 'tuDenom'];
  /* The supplies belong to the preset rather than to a box of their own: the
     directed rule solves a flow programme and needs them, and the undirected
     rule solves a packing programme and has no use for them at all. */
  var TUSUP = '';

  function blank(why) {
    plot.innerHTML = ''; matT.innerHTML = ''; sweepT.innerHTML = ''; cornT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    document.getElementById('tuKOut').textContent = kIn.value;
    var net = parseNet(specIn.value, ['capacity', 'cost']);
    if (net.bad) { blank(net.bad); return; }
    var directed = ruleIn.value === 'directed';
    var M = directed ? incidence(net.nodes, net.arcs) : incidenceUndirected(net.nodes, net.arcs);
    var names = [], i, j;
    for (j = 0; j < net.arcs.length; j += 1) {
      names.push(net.arcs[j].from + (directed ? '&rarr;' : '&ndash;') + net.arcs[j].to);
    }
    var rp = pickIndices(rowsIn.value, net.nodes.length, 'row');
    if (rp.bad) { blank(rp.bad); return; }
    var cp = pickIndices(colsIn.value, net.arcs.length, 'column');
    if (cp.bad) { blank(cp.bad); return; }
    var square = rp.pick.length === cp.pick.length;
    var det = square ? submatrixDet(M, rp.pick, cp.pick) : null;
    var sweep = unimodularSweep(M, Number(kIn.value));
    var rowSet = {}, colSet = {};
    for (i = 0; i < rp.pick.length; i += 1) rowSet[rp.pick[i]] = true;
    for (i = 0; i < cp.pick.length; i += 1) colSet[cp.pick[i]] = true;

    var layout = netLayout(net.nodes, net.arcs, 520, 238);
    plot.innerHTML = drawNet(net.nodes, net.arcs, layout, {
      label: function (k) { return 'x' + (k + 1); },
      tone: function (k) { return colSet[k] ? 'purple' : 'muted'; },
      wide: function (k) { return !!colSet[k]; },
      nodeRing: function (v) {
        for (var k = 0; k < net.nodes.length; k += 1) if (net.nodes[k] === v && rowSet[k]) return 'purple';
        return null;
      }
    }) + netCaption(directed ? 'one column per arc: +1 in the tail row, −1 in the head row'
                             : 'one column per edge: +1 in both endpoint rows', 520, 250);

    var heads = [th('')], rows = '';
    for (j = 0; j < names.length; j += 1) heads.push(th(names[j]));
    for (i = 0; i < net.nodes.length; i += 1) {
      var cells = [rowhead(net.nodes[i])];
      for (j = 0; j < names.length; j += 1) {
        var v = M[i][j], text = Rzero(v) ? '0' : (Rsign(v) > 0 ? '+1' : '&minus;1');
        var hot = rowSet[i] && colSet[j];
        cells.push(td(hot ? tone(text, 'purple') : (Rzero(v) ? '<span class="tone-muted">0</span>' : text)));
      }
      rows += tr(cells, rowSet[i] ? 'tone-purple' : null);
    }
    matT.innerHTML = '<caption>' + (directed ? 'N, with +1 at each arc&rsquo;s tail and &minus;1 at its head'
      : 'the undirected incidence matrix, with +1 at both ends of every edge') + '</caption><thead>'
      + tr(heads) + '</thead><tbody>' + rows + '</tbody>';

    var srows = '', checked = 0;
    for (i = 0; i < sweep.counts.length; i += 1) {
      var c = sweep.counts[i], bad = 0;
      for (j = 0; j < sweep.bad.length; j += 1) if (sweep.bad[j].k === c.k) bad += 1;
      checked += c.checked;
      srows += tr([rowhead('order ' + c.k), td(String(c.checked)),
                   td(bad ? tone(String(bad), 'red') : tone('none', 'green')),
                   tdl(bad ? 'the first is ' + Rtext(sweep.bad[0].det) + ', on rows '
                       + sweep.bad[0].rows.map(function (r) { return r + 1; }).join(', ')
                       + ' and columns ' + sweep.bad[0].cols.map(function (r) { return r + 1; }).join(', ')
                       : 'every determinant landed in {0, +1, &minus;1}')],
                  bad ? 'tone-red' : null);
    }
    sweepT.innerHTML = '<caption>The exhaustive sweep, order by order</caption><thead>'
      + tr([th('order'), th('determinants computed'), th('outside {0, +1, −1}'), th('what was found')])
      + '</thead><tbody>' + srows + '</tbody>';

    var model = null, solved = null, corner = '&mdash;', denom = '&mdash;';
    if (directed) {
      var sup = parseSupply(TUSUP, net.nodes);
      if (!sup.bad) {
        model = mcfModel(net.nodes, net.arcs, sup.supply);
        solved = lpSolve(model);
      }
    } else {
      model = packingModel(M, names);
      solved = lpSolve(model);
    }
    var crows = '';
    if (solved && solved.status === 'optimal') {
      var worst = 1n, whole = true;
      for (j = 0; j < solved.x.length; j += 1) {
        if (!Rint(solved.x[j])) whole = false;
        if (solved.x[j].d > worst) worst = solved.x[j].d;
      }
      for (j = 0; j < solved.x.length; j += 1) {
        crows += tr([rowhead(names[j]), td(Rtext(solved.x[j]))], Rint(solved.x[j]) ? null : 'tone-red');
      }
      crows += tr([rowhead('objective'), td(tone(Rtext(solved.zOrig), whole ? 'green' : 'red'))]);
      corner = whole ? 'every entry whole' : 'fractional';
      denom = String(worst);
      cornT.innerHTML = '<caption>' + (directed
          ? 'The corner this matrix produces: minimise c&#8242;x on N x = b, 0 &#8804; x &#8804; u'
          : 'The corner this matrix produces: maximise the sum of x subject to M x &#8804; 1')
        + '</caption><tbody>' + crows + '</tbody>';
    } else {
      cornT.innerHTML = '<caption>The corner this matrix produces</caption><tbody>'
        + tr([tdl('the programme on this matrix is ' + (solved ? solved.status : 'not set up')
             + ', so there is no corner to read')]) + '</tbody>';
    }

    document.getElementById('tuShape').textContent = net.nodes.length + ' by ' + net.arcs.length;
    document.getElementById('tuChecked').textContent = checked
      + (sweep.truncated ? ' (stopped at the cap)' : '');
    document.getElementById('tuBad').textContent = sweep.bad.length
      ? sweep.bad.length + ' of them' : 'none, up to order ' + kIn.value;
    document.getElementById('tuPick').textContent = square
      ? Rtext(det) : rp.pick.length + ' rows and ' + cp.pick.length + ' columns is not square';
    document.getElementById('tuCorner2').textContent = corner;
    document.getElementById('tuDenom').textContent = denom;

    var picked = square
      ? 'The submatrix you picked has determinant ' + tone(Rtext(det),
          (Rzero(det) || Requ(det, R1) || Requ(det, R(-1n, 1n))) ? 'green' : 'red') + '. '
      : 'Pick as many rows as columns and the lab will take the determinant. ';
    status.innerHTML = picked + 'The sweep computed ' + tone(String(checked), 'cyan')
      + ' determinants exhaustively up to order ' + kIn.value + ' &mdash; it did not sample them &mdash; '
      + (sweep.bad.length
          ? 'and ' + tone(sweep.bad.length + ' of them '
                + plural(sweep.bad.length, 'lies', 'lie') + ' outside {0, +1, −1}', 'red')
            + '. A basis with determinant ' + Rtext(sweep.bad[0].det) + ' inverts to a matrix with that '
            + 'number underneath every entry, so B&#8315;&#185;b is fractional even when b is whole. '
            + 'That is why integrality is a property of the MATRIX and not of the data, and why a '
            + 'method that works on a network stops working the moment the matrix stops being this one.'
          : 'and every one landed in {0, +1, −1}. So every basis B has det B = ±1, B&#8315;&#185; is an '
            + 'integer matrix, and B&#8315;&#185;b is an integer vector whenever b is &mdash; the corners '
            + 'come out whole because of the matrix, not because the numbers happened to be tidy.')
      + ' Order four and above is not swept here: eight nodes and twelve arcs have 34 650 square '
      + 'submatrices of order four, so above three you name the rows and columns and the determinant '
      + 'above is the one you asked for.';
  }


  function apply() {
    var p = TUP[caseIn.value];
    if (!p) return;
    specIn.value = p.spec; ruleIn.value = p.rule;
    rowsIn.value = p.rows; colsIn.value = p.cols;
    TUSUP = p.supply;
    redraw();
  }
  var START = TUP[caseIn.value];
  if (START) {
    TUSUP = START.supply;
    if (!specIn.value) specIn.value = START.spec;
    if (!rowsIn.value) rowsIn.value = START.rows;
    if (!colsIn.value) colsIn.value = START.cols;
  }
  caseIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  ruleIn.addEventListener('change', redraw);
  rowsIn.addEventListener('input', redraw);
  colsIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Why the corners are integers",
        subtitle="Every square submatrix of a node–arc incidence matrix has determinant 0, +1 or −1 — and an odd cycle does not",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick rows and columns, or sweep all of them"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every determinant here is computed exactly by cofactor expansion over rationals. Switch the "
            "rule that builds the matrix and the same drawing produces a different answer.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 -- bellmanford: the labels are prices
# ---------------------------------------------------------------------------

_BF_PRESETS = [
    {
        "id": "prices",
        "label": "five nodes, every cost positive",
        "spec": "s>a 4, s>b 2, b>a 1, a>t 3, b>t 7",
        "note": "the labels settle after two rounds and price every arc",
    },
    {
        "id": "negative",
        "label": "a negative arc, and no negative cycle",
        "spec": "s>a 4, s>b 2, a>b -3, b>t 2, a>t 6",
        "note": "a negative cost is not a problem; a negative cycle is",
    },
    {
        "id": "cycle",
        "label": "a negative cycle: no potentials exist",
        "spec": "x>y 1, y>z -3, z>x 1, x>z 5",
        "note": "adding the dual inequalities around the loop gives 0 ≤ −1",
    },
]


def _bellmanford(cfg):
    preset = str(cfg.get("preset", _BF_PRESETS[0]["id"]))
    chosen = next((p for p in _BF_PRESETS if p["id"] == preset), _BF_PRESETS[0])

    markup = (
        _toolbar(
            "Distance labels are prices",
            "the dual of the shortest-path programme: max &pi;&#8348; &minus; &pi;&#8347; with &pi;&#8332; &minus; &pi;&#8336; &#8804; c&#8336;&#8332;",
            [("green", "a tight arc: the inequality holds with equality"),
             ("cyan", "an arc with slack"), ("red", "an arc the potentials violate")],
        )
        + _stage(_svg("bfPlot", "0 0 660 290",
                      "The network with each node's potential printed under it and the tight arcs drawn "
                      "heavily."))
        + _table("bfRounds")
        + _table("bfArcs")
        + _banner("bfStatus")
    )
    controls = (
        _select("bfPreset", "Worked example", _options(_BF_PRESETS), chosen["id"])
        + _text("bfSpec", "Arcs, as tail&gt;head cost", chosen["spec"])
        + _range("bfShift", "Add this to every potential", -6, 6, 0)
        + _kpis(
            [
                ("Rounds before nothing moved", "bfRounds2"),
                ("The dual objective", "bfValue"),
                ("Arcs violating the dual constraint", "bfViol"),
                ("Tight arcs", "bfTight"),
                ("Are the labels dual feasible?", "bfFeas"),
                ("Cost around the cycle", "bfCycle"),
            ]
        )
        + _hint(
            "bfHint",
            "Relax every arc, as many times as there are nodes. A round that still improves something "
            "after that certifies a negative cycle. Move the shift and watch every potential change and "
            "every reduced cost stay exactly where it was &mdash; that is what makes these prices rather "
            "than distances.",
        )
    )

    script = _BELLMAN_JS + r"""
""" + _presets_js("BFP", _BF_PRESETS, ["spec", "note", "label"]) + r"""
  var presetIn = document.getElementById('bfPreset'), specIn = document.getElementById('bfSpec');
  var shiftIn = document.getElementById('bfShift');
  var plot = document.getElementById('bfPlot'), roundT = document.getElementById('bfRounds');
  var arcT = document.getElementById('bfArcs'), status = document.getElementById('bfStatus');
  var KPIS = ['bfRounds2', 'bfValue', 'bfViol', 'bfTight', 'bfFeas', 'bfCycle'];

  function blank(why) {
    plot.innerHTML = ''; roundT.innerHTML = ''; arcT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc here is '
      + '<span class="tone-muted">tail&gt;head cost</span>, and the cost may be negative.';
  }

  function redraw() {
    document.getElementById('bfShiftOut').textContent = shiftIn.value;
    var net = parseNet(specIn.value, ['cost']);
    if (net.bad) { blank(net.bad); return; }
    var s = net.nodes[0], t = net.nodes[net.nodes.length - 1];
    var bf = bellmanRounds(net.nodes, net.arcs, s);
    var shift = R(BigInt(shiftIn.value), 1n), pi = [], i, j;
    for (i = 0; i < net.nodes.length; i += 1) {
      pi.push(bf.dist[i] === null ? null : Radd(bf.dist[i], shift));
    }
    var reachedAll = true;
    for (i = 0; i < pi.length; i += 1) if (pi[i] === null) { reachedAll = false; pi[i] = shift; }
    var pot = potentialCheck(net.nodes, net.arcs, pi, s, t);
    var tight = {}, viol = {};
    for (i = 0; i < pot.tight.length; i += 1) tight[pot.tight[i]] = true;
    for (i = 0; i < pot.violated.length; i += 1) viol[pot.violated[i]] = true;
    var cycleArc = {};
    if (bf.cycleArcs) for (i = 0; i < bf.cycleArcs.length; i += 1) cycleArc[bf.cycleArcs[i]] = true;

    var layout = netLayout(net.nodes, net.arcs, 660, 278);
    plot.innerHTML = drawNet(net.nodes, net.arcs, layout, {
      label: function (k) { return Rtext(net.arcs[k].cost); },
      tone: function (k) {
        return viol[k] ? 'red' : (cycleArc[k] ? 'amber' : (tight[k] ? 'green' : 'cyan'));
      },
      wide: function (k) { return !!tight[k] || !!viol[k]; },
      dash: function (k) { return !tight[k] && !viol[k]; },
      nodeRing: function (v) { return v === s || v === t ? 'purple' : null; },
      under: function (v) {
        for (var k = 0; k < net.nodes.length; k += 1) {
          if (net.nodes[k] === v) return 'π = ' + Rtext(pi[k]);
        }
        return null;
      }
    }) + netCaption('the number on an arc is its cost; the number under a node is its potential',
                    660, 290);

    var heads = [th('round')], rrows = '';
    for (i = 0; i < net.nodes.length; i += 1) heads.push(th(net.nodes[i]));
    heads.push(th('what moved'));
    for (i = 0; i < bf.rounds.length; i += 1) {
      var r = bf.rounds[i], cells = [rowhead(String(r.round))];
      for (j = 0; j < net.nodes.length; j += 1) {
        cells.push(td(r.dist[j] === null ? '<span class="tone-muted">&mdash;</span>' : Rtext(r.dist[j])));
      }
      cells.push(tdl(r.changed.length ? r.changed.join(', ') : 'nothing'));
      rrows += tr(cells, (bf.negative && i === bf.rounds.length - 1) ? 'tone-red' : null);
    }
    roundT.innerHTML = '<caption>Every arc relaxed, round by round, starting from ' + s
      + '</caption><thead>' + tr(heads) + '</thead><tbody>' + rrows + '</tbody>';

    var arows = '';
    for (j = 0; j < pot.rows.length; j += 1) {
      var p = pot.rows[j];
      arows += tr([rowhead(p.from + ' &rarr; ' + p.to), td(Rtext(p.cost)), td(Rtext(p.gap)),
                   td(Rtext(p.slack)),
                   td(p.ok ? (p.tight ? tone('tight', 'green') : tone('slack', 'cyan'))
                           : tone('violated', 'red')),
                   tdl(p.why)],
                  p.ok ? (p.tight ? 'tone-green' : null) : 'tone-red');
    }
    arcT.innerHTML = '<caption>The dual constraint, on every arc: &pi;&#8332; &minus; &pi;&#8336; '
      + '&#8804; c&#8336;&#8332;</caption><thead>'
      + tr([th('arc'), th('c'), th('π head − π tail'), th('reduced cost'), th('verdict'), th('the check')])
      + '</thead><tbody>' + arows + '</tbody>';

    document.getElementById('bfRounds2').textContent = (bf.rounds.length - 1)
      + ' of ' + net.nodes.length;
    document.getElementById('bfValue').textContent = pot.value === null ? '—'
      : Rtext(pot.value) + ' = π(' + t + ') − π(' + s + ')';
    document.getElementById('bfViol').textContent = pot.violated.length || 'none';
    document.getElementById('bfTight').textContent = pot.tight.length;
    document.getElementById('bfFeas').textContent = pot.ok ? 'yes' : 'no — none exist here';
    document.getElementById('bfCycle').textContent = bf.negative ? Rtext(bf.cycleCost) : 'no cycle';

    if (bf.negative) {
      status.innerHTML = '<strong>' + tone('There are no feasible potentials at all.', 'red')
        + '</strong> Relaxation improved something in round ' + (bf.rounds.length - 1)
        + ', which certifies the cycle ' + tone(bf.cycle.join(' → '), 'amber') + '. Add the dual '
        + 'inequality π head − π tail ≤ c around that loop and every potential appears once with a plus '
        + 'and once with a minus, so the left side is 0 and the right side is '
        + tone(Rtext(bf.cycleCost), 'red') + ': the requirement is 0 ≤ ' + Rtext(bf.cycleCost)
        + ', which nothing satisfies. A negative cycle is not a numerical accident and not a failure of '
        + 'the relaxation &mdash; it is the dual programme being infeasible, which is the same thing as '
        + 'the primal being unbounded below: go round the loop again and the cost drops again.';
      return;
    }
    status.innerHTML = '<strong>' + (pot.ok
        ? tone('The labels are a feasible dual solution.', 'green')
        : tone('These potentials violate ' + pot.violated.length + ' arcs.', 'red'))
      + '</strong> ' + (pot.ok
          ? 'Every arc satisfies π head − π tail ≤ c, so the labels are prices: they are a feasible point '
            + 'of the dual programme, and its objective π(' + t + ') − π(' + s + ') = '
            + tone(Rtext(pot.value), 'cyan') + ' is exactly what it costs to send one unit from ' + s
            + ' to ' + t + '. The ' + pot.tight.length + ' tight arcs &mdash; the ones where the '
            + 'inequality holds with equality &mdash; are where complementary slackness allows flow, '
            + 'and a cheapest path lies inside them. '
          : 'Shift the potentials back, or fix the arcs the table marks in red. ')
      + 'The shift is the point of the control: adding ' + shiftIn.value + ' to every potential changed '
      + 'every label and changed no reduced cost, because each one is a DIFFERENCE of two potentials. '
      + 'Distances happen to be one feasible set of prices, normalised so that the source is worth '
      + 'nothing; they are not the only one, and nothing on this page depends on which you pick.'
      + (reachedAll ? '' : ' Some node is not reachable from ' + s
          + ', and its potential is the shift alone &mdash; there is no path to price.');
  }

  function apply() {
    var p = BFP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = BFP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  shiftIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Shortest paths as a linear programme",
        subtitle="The labels are dual variables — prices on the nodes — and a negative cycle is dual infeasibility",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Relax the arcs, then check the prices"),
        panel_intro=cfg.get(
            "panel_intro",
            "The rounds, the per-arc dual check and the tight-arc subgraph are all recomputed from the "
            "costs you type. Costs may be negative.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 -- maxflow: the theorem as strong duality
# ---------------------------------------------------------------------------

_MF_PRESETS = [
    {
        "id": "twocuts",
        "label": "five arcs, and two different minimum cuts",
        "spec": "s>a 3, s>b 2, a>b 2, a>t 2, b>t 3",
        "note": "the reachable-set cut is one of two of the same capacity",
    },
    {
        "id": "unique",
        "label": "one minimum cut, and only one",
        "spec": "s>a 2, s>b 5, a>t 5, b>t 3",
        "note": "here the minimum cut really is unique",
    },
    {
        "id": "wider",
        "label": "six nodes, a longer network",
        "spec": "s>a 4, s>b 3, a>c 3, a>b 2, b>d 4, c>t 3, d>t 4, c>d 1",
        "note": "more cuts to compare, and the reachable set still names the smallest",
    },
]


def _maxflow(cfg):
    preset = str(cfg.get("preset", _MF_PRESETS[0]["id"]))
    chosen = next((p for p in _MF_PRESETS if p["id"] == preset), _MF_PRESETS[0])

    markup = (
        _toolbar(
            "Maximum flow and minimum cut, as one programme and its dual",
            "a 0/1 dual solution is a cut, and any cut bounds any flow",
            [("cyan", "an arc with spare capacity"), ("red", "an arc crossing the cut"),
             ("purple", "the source side S")],
        )
        + _stage(_svg("mfPlot", "0 0 660 290",
                      "The network with the flow on each arc out of its capacity, the source side of "
                      "the cut ringed and the crossing arcs marked.")
                 + _svg("mfRes", "0 0 660 260",
                        "The residual network: what is left forward on each arc and what can be undone."))
        + _table("mfCuts")
        + _table("mfDual")
        + _banner("mfStatus")
    )
    controls = (
        _select("mfPreset", "Worked example", _options(_MF_PRESETS), chosen["id"])
        + _text("mfSpec", "Arcs, as tail&gt;head capacity", chosen["spec"])
        + _select("mfPath", "An augmenting path in the residual network", [("0", "—")], "0")
        + _buttons([("mfPush", "Push the bottleneck"), ("mfAuto", "Push until none is left"),
                    ("mfReset", "Start again from nothing")])
        + _select("mfCut", "Compare another cut", [("", "—")], "")
        + _kpis(
            [
                ("Flow value", "mfValue"),
                ("The cut the residual network names", "mfCut2"),
                ("The cut you selected", "mfOther"),
                ("How many cuts are minimum", "mfCount"),
                ("Dual objective at that 0/1 point", "mfDualZ"),
                ("Dual objective minus flow value", "mfDualOk"),
            ]
        )
        + _hint(
            "mfHint",
            "The augmenting loop, in one line: find any path from the source to the sink in the residual "
            "network &mdash; forward arcs with spare capacity, backward arcs carrying flow already sent "
            "&mdash; and push the bottleneck. When no such path is left, the set reachable from the "
            "source is a minimum cut. Why the backward arcs are necessary, and what choosing the path "
            "well is worth, are not argued here.",
        )
    )

    script = _MAXFLOW_JS + r"""
""" + _presets_js("MFP", _MF_PRESETS, ["spec", "note", "label"]) + r"""
  var presetIn = document.getElementById('mfPreset'), specIn = document.getElementById('mfSpec');
  var pathIn = document.getElementById('mfPath'), cutIn = document.getElementById('mfCut');
  var plot = document.getElementById('mfPlot'), resPlot = document.getElementById('mfRes');
  var cutT = document.getElementById('mfCuts'), dualT = document.getElementById('mfDual');
  var status = document.getElementById('mfStatus');
  var KPIS = ['mfValue', 'mfCut2', 'mfOther', 'mfCount', 'mfDualZ', 'mfDualOk'];
  var FLOW = null, SEEN = null, PATH = 0, CUT = '';

  function blank(why) {
    plot.innerHTML = ''; resPlot.innerHTML = ''; cutT.innerHTML = ''; dualT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc here is '
      + '<span class="tone-muted">tail&gt;head capacity</span>; the first node named is the source and '
      + 'the last is the sink.';
  }

  function state() {
    var net = parseNet(specIn.value, ['capacity']);
    if (net.bad) return net;
    var j;
    for (j = 0; j < net.arcs.length; j += 1) {
      if (!net.arcs[j].capped) return { bad: 'every arc needs a capacity here; * is not a flow anyone '
        + 'can bound' };
    }
    if (net.nodes.length < 2) return { bad: 'a flow needs a source and a sink' };
    if (SEEN !== specIn.value || FLOW === null || FLOW.length !== net.arcs.length) {
      FLOW = []; SEEN = specIn.value;
      for (j = 0; j < net.arcs.length; j += 1) FLOW.push(R0);
    }
    return net;
  }

  function redraw() {
    var net = state();
    if (net.bad) { blank(net.bad); return; }
    var s = net.nodes[0], t = net.nodes[net.nodes.length - 1], i, j;
    var res = residual(net.arcs, FLOW);
    var paths = resPaths(res, s, t, 8);
    var reach = reachable(net.nodes, res, s);
    var mine = cutCapacity(net.nodes, net.arcs, reach.set);
    var every = allCuts(net.nodes, net.arcs, s, t);
    var value = flowValue(net.nodes, net.arcs, FLOW, s);

    var opts = '';
    for (i = 0; i < paths.length; i += 1) {
      var names = [s];
      for (j = 0; j < paths[i].length; j += 1) names.push(res[paths[i][j]].to);
      opts += '<option value="' + i + '">' + names.join(' → ') + ', bottleneck '
        + Rtext(pathBottleneck(res, paths[i])) + '</option>';
    }
    if (!paths.length) opts = '<option value="0">none is left — this flow is maximum</option>';
    pathIn.innerHTML = opts;
    if (PATH >= paths.length) PATH = 0;
    pathIn.value = String(PATH);

    var copts = '';
    for (i = 0; i < every.cuts.length; i += 1) {
      copts += '<option value="' + every.cuts[i].S.join('+') + '">S = {' + every.cuts[i].S.join(', ')
        + '}, capacity ' + Rtext(every.cuts[i].capacity) + '</option>';
    }
    cutIn.innerHTML = copts;
    var pick = null;
    for (i = 0; i < every.cuts.length; i += 1) if (every.cuts[i].S.join('+') === CUT) pick = every.cuts[i];
    if (pick === null) { pick = every.cuts[0]; CUT = pick.S.join('+'); }
    cutIn.value = CUT;
    /* Whether the residual network has named a cut yet.  Before the flow is
       maximum the set reachable from the source still contains the sink, and a
       set containing both ends is not a cut of anything. */
    var named = !reach.inSet[t];

    var crossing = {}, inS = reach.inSet;
    for (i = 0; i < mine.crossing.length; i += 1) crossing[mine.crossing[i]] = true;
    var layout = netLayout(net.nodes, net.arcs, 660, 278);
    plot.innerHTML = drawNet(net.nodes, net.arcs, layout, {
      label: function (k) { return Rtext(FLOW[k]) + ' of ' + Rtext(net.arcs[k].cap); },
      tone: function (k) { return crossing[k] ? 'red' : (Rzero(FLOW[k]) ? 'muted' : 'cyan'); },
      wide: function (k) { return !!crossing[k]; },
      dash: function (k) { return Rzero(FLOW[k]); },
      nodeRing: function (v) { return inS[v] ? 'purple' : null; },
      under: function (v) { return v === s ? 'source' : (v === t ? 'sink' : null); }
    }) + netCaption('ringed nodes are the set reachable from the source in the residual network',
                    660, 290);

    var rnodes = net.nodes.slice();
    resPlot.innerHTML = res.length
      ? drawNet(rnodes, res, netLayout(rnodes, net.arcs, 660, 248), {
          label: function (k) { return Rtext(res[k].cap); },
          tone: function (k) { return res[k].kind === 'backward' ? 'amber' : 'cyan'; },
          dash: function (k) { return res[k].kind === 'backward'; },
          nodeRing: function (v) { return inS[v] ? 'purple' : null; }
        }) + netCaption('the residual network: solid forward, dashed amber undoes flow already sent',
                        660, 260)
      : netCaption('the residual network is empty', 660, 260);

    var crows = '';
    for (i = 0; i < every.cuts.length && i < 10; i += 1) {
      /* The reachable set comes back in walk order and a cut in node order, so
         both are sorted before they are compared; and before the flow is
         maximum it is not a cut at all, so no row claims to be it. */
      var c = every.cuts[i];
      var isMine = named && c.S.slice().sort().join('+') === reach.set.slice().sort().join('+');
      crows += tr([rowhead('{' + c.S.join(', ') + '}'), td(Rtext(c.capacity)),
                   td(c.crossing.map(function (k) {
                     return net.arcs[k].from + '→' + net.arcs[k].to; }).join(', ') || 'none'),
                   td(Rcmp(c.capacity, value) >= 0 ? tone('≥ ' + Rtext(value), 'green')
                                                   : tone('< ' + Rtext(value), 'red')),
                   tdl(isMine ? 'the one the residual network names' : '')],
                  Requ(c.capacity, every.min) ? 'tone-cyan' : null);
    }
    cutT.innerHTML = '<caption>Every cut, smallest first — ' + every.cuts.length + ' of them, '
      + 'enumerated rather than searched for</caption><thead>'
      + tr([th('S'), th('capacity'), th('arcs leaving S'), th('against the flow'), th('')])
      + '</thead><tbody>' + crows + '</tbody>'
      + (every.cuts.length > 10 ? '<tfoot>' + tr([tdl('the ' + (every.cuts.length - 10)
          + ' larger cuts are not listed', 'small-copy').replace('<td', '<td colspan="5"')])
        + '</tfoot>' : '');

    var model = maxflowModel(net.nodes, net.arcs, s, t);
    var dual = dualModel(model);
    var point = cutDualPoint(net.nodes, net.arcs, pick.S, s, t);
    var inPick = {};
    for (i = 0; i < pick.S.length; i += 1) inPick[pick.S[i]] = true;
    var check = checkModel(dual, point);
    var drows = '', k = 0;
    for (i = 0; i < net.nodes.length; i += 1) {
      if (net.nodes[i] === s || net.nodes[i] === t) continue;
      drows += tr([rowhead('π ' + net.nodes[i]), td(Rtext(point[k])), td('free'),
                   tdl(inPick[net.nodes[i]] ? net.nodes[i] + ' is on the source side of S'
                                            : net.nodes[i] + ' is on the sink side of S')]);
      k += 1;
    }
    for (j = 0; j < net.arcs.length; j += 1) {
      drows += tr([rowhead('y ' + net.arcs[j].from + '→' + net.arcs[j].to), td(Rtext(point[k])),
                   td('≥ 0'),
                   tdl(Rzero(point[k]) ? 'not cut' : 'cut, and it pays ' + Rtext(net.arcs[j].cap))],
                  Rzero(point[k]) ? null : 'tone-red');
      k += 1;
    }
    dualT.innerHTML = '<caption>The dual programme, at the 0/1 point the cut S = {' + pick.S.join(', ')
      + '} names: minimise the sum of u y, one π per interior node and one y per arc</caption><thead>'
      + tr([th('dual variable'), th('value here'), th('sign'), th('what it means')])
      + '</thead><tbody>' + drows + '</tbody><tfoot>'
      + tr([rowhead('objective'), td(tone(Rtext(check.value), 'cyan')),
            tdl(check.ok ? 'every one of the ' + check.rows.length + ' dual constraints is satisfied'
                         : check.violated.length + ' dual constraints fail', 'small-copy')
              .replace('<td', '<td colspan="2"')])
      + '</tfoot>';

    document.getElementById('mfValue').textContent = Rtext(value);
    document.getElementById('mfCut2').textContent = named
      ? Rtext(mine.capacity) + ' at {' + reach.set.join(', ') + '}'
      : 'not a cut yet — the sink is still reachable';
    document.getElementById('mfOther').textContent = Rtext(pick.capacity) + ' at {'
      + pick.S.join(', ') + '}';
    document.getElementById('mfCount').textContent = every.minimum.length + ' of '
      + every.cuts.length;
    document.getElementById('mfDualZ').textContent = Rtext(check.value);
    document.getElementById('mfDualOk').textContent = Rtext(Rsub(check.value, value))
      + (check.ok ? '' : ' — and the point is not dual feasible, which this page would be wrong about');

    var done = paths.length === 0;
    status.innerHTML = '<strong>' + (done
        ? tone('This flow is maximum, and here is the certificate.', 'green')
        : tone('There is still an augmenting path.', 'amber'))
      + '</strong> The flow is worth ' + tone(Rtext(value), 'cyan') + ' and the cut you selected has '
      + 'capacity ' + tone(Rtext(pick.capacity), 'purple') + ' — at least as large, and that is not a '
      + 'coincidence: every unit that reaches the sink must cross every cut, so any cut bounds any flow. '
      + 'That is weak duality, and the table above exhibits it on all ' + every.cuts.length + ' of them. '
      + (done
          ? 'With no augmenting path left, the reachable set is a cut of capacity '
            + tone(Rtext(mine.capacity), 'red') + ', which equals the flow — so neither can improve and '
            + 'both are optimal. '
          : 'Push along a path and watch the residual network change. ')
      + 'The dual table writes the selected cut as a point of the dual programme: π is 1 on the source '
      + 'side and 0 on the sink side, y is 1 on the arcs that cross, and '
      + (check.ok ? 'every one of its ' + check.rows.length + ' constraints holds'
                  : tone('some constraint fails, which would mean this page is wrong', 'red'))
      + ' at objective ' + tone(Rtext(check.value), 'purple') + '. That is what makes a cut a bound: a '
      + 'feasible dual point bounds every primal one, whichever cut you pick. '
      + (Requ(check.value, value)
          ? 'Here the two are equal, and a feasible primal and a feasible dual of equal value certify '
            + 'each other — which is what the theorem says, and why the minimum cut is not a separate '
            + 'combinatorial object that happens to match. '
          : 'The gap is ' + Rtext(Rsub(check.value, value)) + ': either the flow can still grow or the '
            + 'cut is not a minimum one. ')
      + (every.minimum.length > 1
          ? 'Note that ' + tone(every.minimum.length + ' different cuts', 'red') + ' have that same '
            + 'minimum capacity here. Minimum cuts are not unique; the reachable set is only the one '
            + 'this construction happens to produce.'
          : 'On this network the minimum cut happens to be unique — switch the worked example and it '
            + 'is not.');
  }

  function apply() {
    var p = MFP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; FLOW = null; SEEN = null; PATH = 0; CUT = '';
    redraw();
  }
  function pushOnce() {
    var net = state();
    if (net.bad) return false;
    var s = net.nodes[0], t = net.nodes[net.nodes.length - 1];
    var res = residual(net.arcs, FLOW), paths = resPaths(res, s, t, 8);
    if (!paths.length) return false;
    var idx = PATH < paths.length ? PATH : 0;
    FLOW = augmentFlow(net.arcs, FLOW, res, paths[idx]).flow;
    PATH = 0;
    return true;
  }
  var START = MFP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', function () { FLOW = null; SEEN = null; redraw(); });
  pathIn.addEventListener('change', function () { PATH = Number(pathIn.value) || 0; redraw(); });
  cutIn.addEventListener('change', function () { CUT = cutIn.value; redraw(); });
  document.getElementById('mfPush').addEventListener('click', function () { pushOnce(); redraw(); });
  document.getElementById('mfAuto').addEventListener('click', function () {
    for (var i = 0; i < 40; i += 1) if (!pushOnce()) break;
    redraw();
  });
  document.getElementById('mfReset').addEventListener('click', function () {
    FLOW = null; SEEN = null; PATH = 0; redraw();
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The max-flow min-cut theorem as duality",
        subtitle="Any cut bounds any flow; the minimum cut is the optimal dual solution, and it is 0/1 because the matrix is",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Push flow, then read the cut off the residual network"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every cut of the network you type is enumerated and priced, so the minimum is a fact rather "
            "than the output of a search you are asked to trust.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 -- matching: Hall's condition, proved from the cut
# ---------------------------------------------------------------------------

_MT_PRESETS = [
    {
        "id": "three-two",
        "label": "three applicants, two jobs between them",
        "spec": "1-a, 1-b, 2-a, 2-b, 3-a, 3-b",
        "note": "all three want the same two jobs",
    },
    {
        "id": "subset",
        "label": "a deficient set that is not all of X",
        "spec": "1-a, 2-a, 3-a, 4-b, 4-c, 4-d",
        "note": "three applicants share one job while a fourth has three of its own",
    },
    {
        "id": "perfect",
        "label": "a perfect matching",
        "spec": "1-a, 1-b, 2-b, 2-c, 3-c, 3-d, 4-d, 4-a",
        "note": "every applicant placed, and Hall's condition holds on every subset",
    },
]


def _matching(cfg):
    preset = str(cfg.get("preset", _MT_PRESETS[0]["id"]))
    chosen = next((p for p in _MT_PRESETS if p["id"] == preset), _MT_PRESETS[0])

    markup = (
        _toolbar(
            "Hall's condition, read off the cut",
            "if a maximum matching misses a vertex, the cut hands you S with |N(S)| &lt; |S|",
            [("green", "an edge in the matching"), ("purple", "the source side of the cut"),
             ("red", "an arc crossing the cut")],
        )
        + _stage(_svg("mtPlot", "0 0 660 300",
                      "The matching network: a unit arc from the source to each applicant, each original "
                      "edge, and a unit arc from each job to the sink."))
        + _table("mtLeft")
        + _table("mtCut")
        + _banner("mtStatus")
    )
    controls = (
        _select("mtPreset", "Worked example", _options(_MT_PRESETS), chosen["id"])
        + _text("mtSpec", "Edges, as left&minus;right", chosen["spec"])
        + _kpis(
            [
                ("Applicants and jobs", "mtSize"),
                ("Maximum matching", "mtMatch"),
                ("Minimum cut of the network", "mtCutCap"),
                ("The deficient set S", "mtS"),
                ("Its neighbourhood N(S)", "mtNS"),
                ("Hall's condition", "mtHall"),
            ]
        )
        + _hint(
            "mtHint",
            "The reduction, in two lines: a unit-capacity arc from the source to every applicant, every "
            "original edge with capacity one, and a unit-capacity arc from every job to the sink. A flow "
            "of value k is a matching of size k, and it comes out whole because the matrix is the one "
            "the integrality lesson swept.",
        )
    )

    script = _MATCHING_JS + r"""
""" + _presets_js("MTP", _MT_PRESETS, ["spec", "note", "label"]) + r"""
  var presetIn = document.getElementById('mtPreset'), specIn = document.getElementById('mtSpec');
  var plot = document.getElementById('mtPlot'), leftT = document.getElementById('mtLeft');
  var cutT = document.getElementById('mtCut'), status = document.getElementById('mtStatus');
  var KPIS = ['mtSize', 'mtMatch', 'mtCutCap', 'mtS', 'mtNS', 'mtHall'];

  function blank(why) {
    plot.innerHTML = ''; leftT.innerHTML = ''; cutT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tone-muted">1-a</span>: an applicant, a dash, a job.';
  }

  function redraw() {
    var bip = parseBip(specIn.value);
    if (bip.bad) { blank(bip.bad); return; }
    var m = bipartiteMatch(bip.left, bip.right, bip.edges), i, j;

    /* The flow network the reduction names, and the cut of it -- both from
       top-level functions, so the numbers on this page are the ones
       scripts/mathcheck.js checks. */
    var built = matchingNetwork(bip.left, bip.right, bip.edges);
    var nodes = built.nodes, arcs = built.arcs;
    var S = matchingCut(m), inS = {};
    for (i = 0; i < S.length; i += 1) inS[S[i]] = true;
    var cut = cutCapacity(nodes, arcs, S), crossing = {};
    for (i = 0; i < cut.crossing.length; i += 1) crossing[cut.crossing[i]] = true;
    var matched = {};
    for (i = 0; i < m.matching.length; i += 1) {
      matched['L' + m.matching[i].left + '|R' + m.matching[i].right] = true;
    }

    var layout = netLayout(nodes, arcs, 660, 288);
    plot.innerHTML = drawNet(nodes, arcs, layout, {
      name: function (v) { return v === 'src' ? 'source' : (v === 'snk' ? 'sink' : v.slice(1)); },
      label: function (k) { return ''; },
      tone: function (k) {
        if (crossing[k]) return 'red';
        return matched[arcs[k].from + '|' + arcs[k].to] ? 'green' : 'muted';
      },
      wide: function (k) { return !!matched[arcs[k].from + '|' + arcs[k].to] || !!crossing[k]; },
      dash: function (k) { return !matched[arcs[k].from + '|' + arcs[k].to] && !crossing[k]; },
      nodeRing: function (v) { return inS[v] ? 'purple' : null; }
    }) + netCaption('every arc has capacity one; ringed nodes are the source side of the minimum cut',
                    660, 300);

    var rows = '';
    for (i = 0; i < bip.left.length; i += 1) {
      var nb = [];
      for (j = 0; j < bip.edges.length; j += 1) {
        if (bip.edges[j][0] === bip.left[i]) nb.push(bip.edges[j][1]);
      }
      var to = m.matchL[i] >= 0 ? bip.right[m.matchL[i]] : null;
      var inDef = m.deficient.S.indexOf(bip.left[i]) >= 0;
      rows += tr([rowhead(bip.left[i]), tdl(nb.join(', ')), td(nb.length),
                  td(to === null ? tone('unmatched', 'red') : tone(to, 'green')),
                  td(inDef ? tone('yes', 'purple') : '')],
                 inDef ? 'tone-purple' : null);
    }
    leftT.innerHTML = '<caption>Every applicant, what they can take, and what they got</caption><thead>'
      + tr([th('applicant'), th('jobs open to them'), th('how many'), th('matched to'), th('in S?')])
      + '</thead><tbody>' + rows + '</tbody>';

    var perfect = m.matching.length === bip.left.length;
    cutT.innerHTML = '<caption>The cut, and what it certifies</caption><tbody>'
      + tr([rowhead('minimum cut'), tdl('{' + S.map(function (v) {
            return v === 'src' ? 'source' : v.slice(1); }).join(', ') + '}, capacity '
          + tone(Rtext(cut.capacity), 'cyan'))])
      + tr([rowhead('maximum matching'), tdl(m.matching.map(function (p) {
            return p.left + '&ndash;' + p.right; }).join(', ') || 'nothing can be matched')])
      + tr([rowhead('minimum vertex cover'), tdl('{' + m.cover.left.concat(m.cover.right).join(', ')
          + '}, size ' + m.cover.size + ' &mdash; equal to the matching, which is what K&ouml;nig&rsquo;s '
          + 'theorem says and what the Hungarian method&rsquo;s line count was really asking for')])
      + tr([rowhead('S'), tdl('{' + m.deficient.S.join(', ') + '}, size ' + m.deficient.S.length)])
      + tr([rowhead('N(S)'), tdl('{' + m.deficient.N.join(', ') + '}, size ' + m.deficient.N.length)])
      + tr([rowhead('|N(S)| − |S|'), tdl(tone(String(m.deficient.N.length - m.deficient.S.length),
          m.deficient.violated ? 'red' : 'green'))])
      + '</tbody>';

    document.getElementById('mtSize').textContent = bip.left.length + ' and ' + bip.right.length;
    document.getElementById('mtMatch').textContent = m.size + ' of ' + bip.left.length;
    document.getElementById('mtCutCap').textContent = Rtext(cut.capacity);
    document.getElementById('mtS').textContent = '{' + m.deficient.S.join(', ') + '}, size '
      + m.deficient.S.length;
    document.getElementById('mtNS').textContent = '{' + m.deficient.N.join(', ') + '}, size '
      + m.deficient.N.length;
    document.getElementById('mtHall').textContent = m.deficient.violated
      ? 'fails on S' : 'holds on every subset';

    status.innerHTML = (perfect
        ? '<strong>' + tone('Every applicant is placed.', 'green') + '</strong> The matching has '
          + m.size + ' edges, the minimum cut has capacity ' + Rtext(cut.capacity) + ', and the two are '
          + 'equal because a matching is a flow and this is that flow&rsquo;s theorem. There is no '
          + 'deficient set to find: Hall&rsquo;s condition holds on every subset of the applicants, and '
          + 'the alternating search from the unmatched side found nothing because there is no unmatched '
          + 'side. Remove an edge and the certificate appears.'
        : '<strong>' + tone('The matching is imperfect, and here is why.', 'red') + '</strong> '
          + 'It has ' + m.size + ' edges for ' + bip.left.length + ' applicants. Take S = '
          + tone('{' + m.deficient.S.join(', ') + '}', 'purple') + ', the applicants on the source side '
          + 'of the minimum cut. Their jobs between them are N(S) = '
          + tone('{' + m.deficient.N.join(', ') + '}', 'purple') + ': '
          + tone(String(m.deficient.N.length), 'red') + ' job'
          + plural(m.deficient.N.length, '', 's') + ' for '
          + tone(String(m.deficient.S.length), 'red') + ' applicant'
          + plural(m.deficient.S.length, '', 's') + '. That is Hall&rsquo;s condition '
          + 'failing, and it is a certificate you can hand to somebody &mdash; count the two sets and '
          + 'the claim is settled without running anything. '
          + 'The direction that needed proving is this one: the condition is not merely necessary, and '
          + 'whenever a matching falls short the cut produces the violating set.')
      + ' The flow came out whole rather than fractional because the constraint matrix of this network '
      + 'is the one whose square submatrices all have determinant 0, +1 or &minus;1 &mdash; half an '
      + 'applicant is not ruled out by the algorithm, it is ruled out by the matrix.';
  }

  function apply() {
    var p = MTP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = MTP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bipartite matching and Hall's theorem",
        subtitle="When the matching falls short, the minimum cut hands you the set with too few neighbours",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Edit the bipartite graph"),
        panel_intro=cfg.get(
            "panel_intro",
            "The matching, the cover and the deficient set are all computed from the edges you type; the "
            "cut is taken of the flow network drawn above, not asserted.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L10 -- cpm: the project length is a longest path
# ---------------------------------------------------------------------------

_CP_PRESETS = [
    {
        "id": "nine",
        "label": "nine activities, one critical path",
        "spec": ("A 3, B 2 after A, C 4 after A, G 5 after A, D 2 after B, E 3 after C, "
                 "H 2 after G, F 1 after D E, I 1 after F H"),
        "crash": "C",
        "note": "shorten C by one and a second path draws level",
    },
    {
        "id": "twopaths",
        "label": "two critical paths from the start",
        "spec": "A 3, B 2 after A, C 2 after A, D 2 after B, E 2 after C, F 1 after D E",
        "crash": "B",
        "note": "shortening either one alone buys nothing at all",
    },
    {
        "id": "cycle",
        "label": "a precedence loop, and therefore no schedule",
        "spec": "A 3 after C, B 2 after A, C 4 after B",
        "crash": "A",
        "note": "no order exists, so there is nothing to compute",
    },
]


def _cpm(cfg):
    preset = str(cfg.get("preset", _CP_PRESETS[0]["id"]))
    chosen = next((p for p in _CP_PRESETS if p["id"] == preset), _CP_PRESETS[0])

    markup = (
        _toolbar(
            "Earliest, latest and slack",
            "the project length is a longest path, and criticality belongs to the path",
            [("red", "a critical activity: zero slack"), ("cyan", "an activity with slack"),
             ("amber", "the activity being shortened")],
        )
        + _stage(_svg("cpPlot", "0 0 660 300",
                      "The precedence network, one node per activity, with the critical chain drawn "
                      "heavily."))
        + _table("cpTable")
        + _table("cpCrash")
        + _banner("cpStatus")
    )
    controls = (
        _select("cpPreset", "Worked example", _options(_CP_PRESETS), chosen["id"])
        + _text("cpSpec", "Activities, as name duration after predecessors", chosen["spec"])
        + _select("cpAct", "Shorten this activity", [(chosen["crash"], chosen["crash"])],
                  chosen["crash"])
        + _range("cpCut", "By this much", 0, 6, 0)
        + _kpis(
            [
                ("Project length", "cpLen"),
                ("Critical activities", "cpCrit"),
                ("Distinct critical paths", "cpPaths"),
                ("Slack on the chosen activity", "cpSlack"),
                ("Shortening it is worth", "cpGain"),
                ("It stops paying after", "cpStop"),
            ]
        )
        + _hint(
            "cpHint",
            "Write <span class=\"tt\">D 2 after B C</span> for an activity of length two that waits for "
            "both B and C. Listing the activities so that every predecessor comes first is possible "
            "exactly when the precedence graph has no cycle; the method for producing such an order, and "
            "the proof that it exists, are not this lab&rsquo;s.",
        )
    )

    script = _CPM_JS + r"""
""" + _presets_js("CPP", _CP_PRESETS, ["spec", "crash", "note", "label"]) + r"""
  var presetIn = document.getElementById('cpPreset'), specIn = document.getElementById('cpSpec');
  var actIn = document.getElementById('cpAct'), cutIn = document.getElementById('cpCut');
  var plot = document.getElementById('cpPlot'), tableT = document.getElementById('cpTable');
  var crashT = document.getElementById('cpCrash'), status = document.getElementById('cpStatus');
  var KPIS = ['cpLen', 'cpCrit', 'cpPaths', 'cpSlack', 'cpGain', 'cpStop'];
  var PICK = '';

  function blank(why) {
    plot.innerHTML = ''; tableT.innerHTML = ''; crashT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    document.getElementById('cpCutOut').textContent = cutIn.value;
    var parsed = parseActs(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var acts = parsed.acts, i, j;
    var ids = acts.map(function (a) { return a.id; });

    var opts = '';
    for (i = 0; i < ids.length; i += 1) opts += '<option value="' + ids[i] + '">' + ids[i] + '</option>';
    actIn.innerHTML = opts;
    if (ids.indexOf(PICK) < 0) PICK = ids[0];
    actIn.value = PICK;

    var cut = Number(cutIn.value) || 0;
    var chosen = null;
    for (i = 0; i < acts.length; i += 1) if (acts[i].id === PICK) chosen = acts[i];
    var maxCut = chosen ? Number(chosen.dur.n / chosen.dur.d) : 0;
    if (cut > maxCut) cut = maxCut;
    var shortened = [];
    for (i = 0; i < acts.length; i += 1) {
      shortened.push(acts[i].id === PICK
        ? { id: acts[i].id, dur: Rsub(acts[i].dur, R(BigInt(cut), 1n)), pred: acts[i].pred }
        : acts[i]);
    }
    var base = cpmPasses(acts), pass = cpmPasses(shortened);
    if (pass.cycle) {
      plot.innerHTML = '';
      tableT.innerHTML = ''; crashT.innerHTML = '';
      for (i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
      status.innerHTML = '<strong>' + tone('This project has no schedule.', 'red') + '</strong> '
        + 'The precedences run in a loop: ' + tone(pass.cycle.join(' → ') + ' → ' + pass.cycle[0], 'amber')
        + '. No listing of the activities can put every predecessor before the activity that waits for '
        + 'it, so there is no forward pass to run and no earliest start to compute. Such an order exists '
        + 'exactly when the precedence graph is acyclic; break the loop and the table comes back.';
      return;
    }

    var ix = {}, nodes = [], arcs = [];
    for (i = 0; i < shortened.length; i += 1) { ix[shortened[i].id] = i; nodes.push(shortened[i].id); }
    for (i = 0; i < shortened.length; i += 1) {
      for (j = 0; j < shortened[i].pred.length; j += 1) {
        arcs.push({ from: shortened[i].pred[j], to: shortened[i].id, cap: null, cost: R0,
                    capped: false });
      }
    }
    var critical = {};
    for (i = 0; i < pass.critical.length; i += 1) critical[pass.critical[i]] = true;

    var layout = netLayout(nodes, arcs, 660, 288);
    plot.innerHTML = drawNet(nodes, arcs, layout, {
      label: function () { return ''; },
      tone: function (k) {
        return critical[arcs[k].from] && critical[arcs[k].to] ? 'red' : 'muted';
      },
      wide: function (k) { return critical[arcs[k].from] && critical[arcs[k].to]; },
      dash: function (k) { return !(critical[arcs[k].from] && critical[arcs[k].to]); },
      nodeRing: function (v) { return v === PICK ? 'amber' : (critical[v] ? 'red' : null); },
      under: function (v) { return Rtext(shortened[ix[v]].dur); }
    }) + netCaption('one node per activity; the number under it is its duration', 660, 300);

    var rows = '';
    for (i = 0; i < shortened.length; i += 1) {
      rows += tr([rowhead(shortened[i].id), tdl(shortened[i].pred.join(' ') || '&mdash;'),
                  td(Rtext(shortened[i].dur)), td(Rtext(pass.ES[i])), td(Rtext(pass.EF[i])),
                  td(Rtext(pass.LS[i])), td(Rtext(pass.LF[i])),
                  td(Rzero(pass.slack[i]) ? tone('0', 'red') : Rtext(pass.slack[i])),
                  td(Rzero(pass.slack[i]) ? tone('critical', 'red') : '')],
                 Rzero(pass.slack[i]) ? 'tone-red' : (shortened[i].id === PICK ? 'tone-amber' : null));
    }
    tableT.innerHTML = '<caption>Forward pass, backward pass, and the difference between them'
      + '</caption><thead>'
      + tr([th('activity'), th('after'), th('duration'), th('ES'), th('EF'), th('LS'), th('LF'),
            th('slack'), th('')]) + '</thead><tbody>' + rows + '</tbody>'
      + '<tfoot>' + tr([tdl('Every critical path: ' + (pass.paths.length
          ? pass.paths.map(function (p) { return p.join(' → '); }).join('; ')
          : 'none'), 'small-copy').replace('<td', '<td colspan="9"')]) + '</tfoot>';

    var curve = crashCurve(acts, PICK, maxCut), crows = '';
    for (i = 0; i < curve.steps.length; i += 1) {
      var st = curve.steps[i];
      crows += tr([rowhead(PICK + ' shortened by ' + st.cut), td(Rtext(st.makespan)),
                   td(i === 0 ? '&mdash;' : Rtext(Rsub(curve.steps[i - 1].makespan, st.makespan))),
                   td(String(st.paths)), tdl(st.critical.join(' '))],
                  i === cut ? 'tone-amber' : (i > curve.lastUseful ? 'tone-muted' : null));
    }
    crashT.innerHTML = '<caption>What shortening ' + PICK + ' buys, one unit at a time'
      + '</caption><thead>'
      + tr([th('cut'), th('project length'), th('bought'), th('critical paths'), th('critical')])
      + '</thead><tbody>' + crows + '</tbody>';

    var slack = Rtext(pass.slack[ix[PICK]]);
    var gain = Rsub(base.makespan, pass.makespan);
    document.getElementById('cpLen').textContent = Rtext(pass.makespan)
      + (cut ? ' (was ' + Rtext(base.makespan) + ')' : '');
    document.getElementById('cpCrit').textContent = pass.critical.join(' ') || 'none';
    document.getElementById('cpPaths').textContent = pass.paths.length;
    document.getElementById('cpSlack').textContent = slack;
    document.getElementById('cpGain').textContent = Rtext(gain) + ' shorter, for ' + cut
      + ' unit' + plural(cut, '', 's') + ' cut';
    document.getElementById('cpStop').textContent = curve.lastUseful + ' unit'
      + plural(curve.lastUseful, '', 's');

    status.innerHTML = '<strong>The project takes ' + tone(Rtext(pass.makespan), 'cyan')
      + '.</strong> That is the longest path through the precedences, not the sum of the longest '
      + 'activities and not the length of any one chain you can see: ' + pass.paths.length
      + ' distinct path' + plural(pass.paths.length, '', 's') + ' through the network '
      + plural(pass.paths.length, 'has', 'have') + ' zero slack, and slack is LS − ES computed by two '
      + 'passes over every activity. '
      + (Rzero(pass.slack[ix[PICK]])
          ? tone(PICK, 'amber') + ' is critical, so shortening it moves the project &mdash; '
            + (curve.lastUseful > 0
                ? 'for ' + tone(curve.lastUseful + ' unit' + plural(curve.lastUseful, '', 's'), 'amber')
                  + ', and then it stops. After that a second path is critical too and the length is '
                  + 'held by a chain ' + PICK + ' is not on, so every further unit spent on it buys '
                  + 'exactly nothing.'
                : 'or it would, except that another path is already level with it: '
                  + tone('the first unit buys nothing at all', 'red') + ', because two paths are '
                  + 'critical and shortening one leaves the other holding the length.')
          : tone(PICK, 'amber') + ' has ' + slack + ' unit' + plural(Number(slack), '', 's')
            + ' of slack, so shortening it moves nothing: '
            + 'it is not on a critical path, and the project length is a property of the path rather '
            + 'than of any activity on it.');
  }

  function apply() {
    var p = CPP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; PICK = p.crash; cutIn.value = '0';
    redraw();
  }
  var START = CPP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  actIn.addEventListener('change', function () { PICK = actIn.value; redraw(); });
  cutIn.addEventListener('input', redraw);
  PICK = actIn.value;
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Project networks and the critical path",
        subtitle="Shortening a critical activity helps — until a second path becomes critical, and then it does nothing",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the project, then shorten something"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both passes and every critical path are recomputed from the activities you type, and the "
            "crash table recomputes the whole project at each length rather than extrapolating.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. `sspath` is deliberately absent: the lesson that used it was
# cut, because it stood on a residual network and a Bellman-Ford that belong to
# another subject, and lesson `mincost`'s programme solves every instance of it
# on this course exactly.
# ---------------------------------------------------------------------------

_MODES = {
    "digraph": _digraph,
    "mincost": _mincost,
    "tu": _tu,
    "bellmanford": _bellmanford,
    "maxflow": _maxflow,
    "matching": _matching,
    "cpm": _cpm,
}

MODES = tuple(sorted(_MODES))


def network_lab(cfg):
    """Course 4's drawing kit. `cfg["mode"]` chooses the lesson; unknown raises.

    The raise is the contract and not defensiveness. A kit that fell back to a
    default would render a finished-looking page carrying another lesson's
    widget, and nothing downstream would notice: the markup assertions pass,
    labcheck passes, and a reader is shown a critical path under the heading
    about minimum cuts.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "network_lab: unknown mode %r; the seven modes of the network course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["network_lab", "NETKIT_JS", "CHECK_JS", "MODEL_JS", "CUT_JS",
           "MATCH_JS", "PROJECT_JS", "TU_JS", "MODES"]
