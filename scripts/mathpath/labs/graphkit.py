"""Graph Algorithms -- eleven modes over one directed, weighted arc list.

WHAT THE READER TYPES. Every mode here opens on an editor, because every claim
on this course is a claim about all graphs and the fastest way to understand
the root's rule for cut vertices is to try to break it. One clause is

    u>v w        an arc from u to v of weight w      (a directed mode)
    u-v w        an edge between u and v of weight w (an undirected mode)

with 1-based labels, because that is what the prose uses, and w optional and
allowed to be negative -- which is the whole subject of one of these modes and
a thing `graph.py`'s weights, the function ((7i + 13j) mod 9) + 1 of the
endpoints, cannot express at all.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE. `algo_core`'s
GRAPHKIT_JS holds the algorithms; nothing here reimplements one. What this kit
adds is the CHECKING, and there are three kinds of it on these pages:

  an independent oracle       `graph.py`'s GRAPH_JS is undirected, its weights
                              are a function of the endpoints and its N caps at
                              8, so it cannot serve as this kit's engine. But
                              `cuts()` finds bridges by deleting each edge and
                              recounting components, `kruskal()` builds a
                              minimum tree from the cycle property and
                              `dijkstra()` settles vertices by a linear scan --
                              three answers by a different route, and
                              `dgToMatrix` plus `lessonFrom` hand a graph built
                              here to all three. `lowlink`, `kruskal` and
                              `relax` run them live, beside their own answer,
                              on the reader's own graph.
  an exhaustive enumeration   `cutproperty` enumerates EVERY spanning tree at
                              seven or fewer vertices, so "the lightest edge
                              across this cut is in some minimum tree" is read
                              off the list rather than asserted; `topo` counts
                              every valid topological order, which is how the
                              page answers "is it unique" with a number.
  a second algorithm here     `floyd` against Bellman-Ford from every source,
                              `bellmanford` against Floyd's diagonal, `dagsp`
                              against both -- and against Dijkstra's schedule,
                              which on a DAG with a negative weight returns a
                              different answer, printed beside the right one.

THE ONE THING THE ORACLES CANNOT DO, and the page says so where it happens.
GRAPH_JS is a matrix, so it holds one entry per pair. Two arcs between the same
pair -- which this representation allows and which `lowlink` must not call a
bridge -- cannot be handed to it at all. Where the reader's graph has a
parallel pair the check panel reports that the matrix cannot represent the
graph rather than quietly comparing against a different graph.

THE MODES, and the figure each one is for:

  dfstimes     d and f per vertex, every arc classified, the parenthesis
               theorem checked pair by pair, and the same arcs read undirected
               where forward and cross edges cannot occur
  topo         reverse postorder, Kahn's order, the in-degree table, every
               valid order counted, and on a cycle the back edge
  lowlink      d and low per vertex, bridges and cut vertices, against
               delete-and-recount
  scc          both passes, the components against mutual reachability
               computed from the definition, and the condensation
  cutproperty  the crossing set, its lightest arc, and the verdict against
               every spanning tree there is
  prim         the heap at every step, operations against E log V, the weight
  kruskal      union-find state per edge, finds and unions, and the reason each
               rejected edge was rejected
  relax        d[] after each relaxation under three schedules, the upper-bound
               invariant checked after every step, heap operations
  bellmanford  the per-round table, the round each label became final, and a
               negative cycle as the cycle itself
  dagsp        the one-pass table in topological order, longest paths by
               flipping the sign, and per-vertex slack
  floyd        the matrix after each k, and the path rebuilt from next[]

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped. COUNT_JS,
DIGRAPH_JS, GRAPHKIT_JS and this kit's own block are on every page here and
come to about 14 KB gzipped. The rest is added only where it is called:

    ORACLE_JS     topo, cutproperty     -- oracleCap, and nothing else
    GRAPH_JS      lowlink, kruskal, relax -- the three live oracles
    ALGO_JS       prim, relax           -- `ilog2`, for the E log V column.
                  primRun returns the bound as a field, so a page that calls it
                  needs the function whether or not it prints one.

Measured, on a real lesson page rendered by scripts/mathpath/render.py --
gzipped, against the repository's 62 KB ceiling:

    scc 40.1   dfstimes 40.9   floyd 41.4   bellmanford 41.5   dagsp 41.9
    topo 43.1   cutproperty 43.5   kruskal 44.1   prim 44.4   lowlink 44.4
    relax 48.1

Re-derive these rather than trusting them; they go stale as the engine grows.
The spread is the block table above and nothing else: `relax` is the heaviest
because it is the only mode that carries both the Discrete Mathematics graph
block and the logarithm, and `scc` is the lightest because it carries neither.

Nothing on these pages rounds. Distances, weights, low-links, cut capacities
and component counts are integers; the only floating-point arithmetic is the
E log V column, which is a REFERENCE and is labelled as one, and no verdict is
read off it.
"""

from .algo_core import COUNT_JS, DIGRAPH_JS, GRAPHKIT_JS, ORACLE_JS
from .algorithms import ALGO_JS
from .common import Lab
from .graph import GRAPH_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

GKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     One clause is `u>v w` or `u-v w`, 1-based, the weight optional. The
     SEPARATOR IS NOT WHAT DECIDES DIRECTION: the mode does, and it passes
     `directed` in, because a reader who types a hyphen into the strongly-
     connected-components editor means an arc and should get one rather than a
     parse error. What the separator does is let the undirected modes be typed
     the way their prose reads. */
  var GK_MAXN = 12;          /* twelve labels is what the ring drawing can hold */
  var GK_MAXARCS = 26;

  function gkClauses(text) {
    var parts = String(text).split(/[,;\n]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }
  function gkParse(text, directed, maxN) {
    maxN = maxN === undefined ? GK_MAXN : maxN;
    var cl = gkClauses(text), raw = [], n = 0, i;
    if (!cl.length) return { bad: 'write at least one arc' };
    if (cl.length > GK_MAXARCS) return { bad: 'that is more than ' + GK_MAXARCS + ' arcs' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*(?:>|-|to)\s*(\d+)(?:[\s:]+(-?\d+))?$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '"' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10);
      var w = m[3] === undefined ? 1 : parseInt(m[3], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'a loop at ' + u + ': none of these algorithms is about one' };
      if (w < -999 || w > 999) return { bad: 'keep the weight between -999 and 999' };
      raw.push([u, v, w]);
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (n < 2) return { bad: 'two vertices is the smallest graph worth drawing' };
    var G = dgNew(n, directed);
    for (i = 0; i < raw.length; i += 1) dgAdd(G, raw[i][0] - 1, raw[i][1] - 1, raw[i][2], 0);
    return { G: G, n: n, arcs: G.arcs.length };
  }
  /* A vertex set, as the reader writes it: "1, 2, 5". Out-of-range labels are
     reported rather than dropped, because a cut whose set silently lost a
     vertex is a cut the reader did not ask about. */
  function gkParseSet(text, n) {
    var parts = gkClauses(text), out = [], seen = {}, i;
    for (i = 0; i < parts.length; i += 1) {
      var v = parseInt(parts[i], 10);
      if (!isFinite(v)) return { bad: 'cannot read "' + parts[i] + '" as a vertex' };
      if (v < 1 || v > n) return { bad: 'this graph has no vertex ' + v };
      if (!seen[v]) { seen[v] = true; out.push(v - 1); }
    }
    return { set: out.sort(function (a, b) { return a - b; }) };
  }
  function gkLabels(n) {
    var out = [], i;
    for (i = 0; i < n; i += 1) out.push(i + 1);
    return out;
  }
  function gkNames(list) {
    return (list || []).map(function (v) { return v + 1; }).join(', ');
  }
  function gkArcName(a) { return (a.u + 1) + ' → ' + (a.v + 1); }
  function gkEdgeName(a) { return (a.u + 1) + ' – ' + (a.v + 1); }

  /* ----------------------------------------------- handing a graph to GRAPH_JS

     `dgToMatrix` loses two things and the modes that use it say which. A matrix
     holds one entry per pair, so PARALLEL arcs vanish; and GRAPH_JS reads its
     weights through `weight(i, j)`, which consults LESSON keyed on the
     unordered pair, so two arcs between one pair cannot carry two weights.
     gkOracleReady reports both before anything is compared. */
  function gkParallelPairs(G) {
    var seen = {}, dup = [];
    G.arcs.forEach(function (a) {
      var k = Math.min(a.u, a.v) + '-' + Math.max(a.u, a.v);
      if (seen[k] && dup.indexOf(k) === -1) dup.push(k);
      seen[k] = true;
    });
    return dup;
  }
  function gkOracleReady(G) {
    var dup = gkParallelPairs(G);
    return { ok: dup.length === 0, parallel: dup,
             why: dup.length
               ? 'a matrix holds one entry per pair, so it cannot hold '
                 + dup.length + ' parallel pair' + (dup.length === 1 ? '' : 's')
               : null };
  }
  /* The 1-based triples GRAPH_JS.lessonFrom takes, so its `weight(i, j)`
     answers with the reader's number instead of ((7i + 13j) mod 9) + 1. */
  function gkLessonList(G) {
    return G.arcs.map(function (a) { return [a.u + 1, a.v + 1, a.w]; });
  }

  /* -------------------------------------------- the parenthesis theorem, run

     `v is a descendant of u` is computed by WALKING THE PARENT POINTERS, which
     is the definition, and `[d(v), f(v)] subset of [d(u), f(u)]` is computed
     from the timestamps. The theorem is that those two agree on every ordered
     pair, so the page compares them pair by pair rather than restating it. A
     third count matters as much: the number of pairs whose intervals OVERLAP
     without nesting, which the theorem says is zero. */
  function gkAncestors(times) {
    var n = times.d.length, anc = [], v, at;
    for (v = 0; v < n; v += 1) anc.push(new Array(n).fill(false));
    for (v = 0; v < n; v += 1) {
      at = times.parent[v];
      while (at !== -1 && at !== undefined) { anc[at][v] = true; at = times.parent[at]; }
    }
    return anc;
  }
  function parenthesisCheck(times) {
    var anc = gkAncestors(times), n = times.d.length, u, v;
    /* The DESCENT check runs over ordered pairs, because "u contains v" and
       "v contains u" are different statements and each has to match its own
       ancestor entry. The SHAPE count runs over unordered pairs, because
       nesting and disjointness are properties of a PAIR of intervals: counted
       over ordered pairs the two are double-counted unevenly -- one nesting
       appears once and one disjointness twice -- and the three numbers then add
       up to nothing the reader can check. Here they add to exactly C(n, 2). */
    var violations = [];
    for (u = 0; u < n; u += 1) for (v = 0; v < n; v += 1) {
      if (u === v) continue;
      var inside = times.d[u] < times.d[v] && times.f[v] < times.f[u];
      if (inside !== anc[u][v]) violations.push({ u: u, v: v, nested: inside, descendant: anc[u][v] });
    }
    var nested = 0, disjoint = 0, overlapping = 0;
    for (u = 0; u < n; u += 1) for (v = u + 1; v < n; v += 1) {
      var uv = times.d[u] < times.d[v] && times.f[v] < times.f[u];
      var vu = times.d[v] < times.d[u] && times.f[u] < times.f[v];
      var apart = times.f[u] < times.d[v] || times.f[v] < times.d[u];
      if (uv || vu) nested += 1;
      else if (apart) disjoint += 1;
      else overlapping += 1;
    }
    return { nested: nested, disjoint: disjoint, overlapping: overlapping,
             pairs: (n * (n - 1)) / 2, violations: violations,
             holds: violations.length === 0 && overlapping === 0, ancestor: anc };
  }

  /* ------------------------------------------- the same arcs read undirected

     The misconception is that an undirected graph has cross edges. It has only
     tree and back edges, and this computes the classification rather than
     asserting it: an undirected edge is met from whichever end DFS reached
     FIRST, so it is classified from that end -- tree when that end is the
     parent, back when the other end lies inside its interval, and cross
     otherwise. The count of the third is the figure, and it is zero. */
  function gkUndirectedKinds(G, roots) {
    var H = dgNew(G.n, false);
    G.arcs.forEach(function (a) { dgAdd(H, a.u, a.v, a.w, 0); });
    var t = dfsTimes(H, roots).result;
    var counts = { tree: 0, back: 0, forward: 0, cross: 0 }, list = [];
    H.arcs.forEach(function (a, id) {
      var first = t.d[a.u] <= t.d[a.v] ? a.u : a.v, other = first === a.u ? a.v : a.u;
      var kind;
      if (t.parent[other] === first) kind = 'tree';
      else if (t.d[first] < t.d[other] && t.f[other] < t.f[first]) kind = 'back';
      else kind = 'cross';
      counts[kind] += 1;
      list.push({ id: id, u: first, v: other, kind: kind });
    });
    return { counts: counts, edges: list, times: t };
  }

  /* ------------------------------------------------ every topological order

     "The topological order is unique" is answered with a number, so the number
     has to be produced: every order is enumerated by taking every in-degree-
     zero vertex at every step. The cap is the usual refusal -- 8 vertices with
     no arcs is 40 320 orders, which is instant, and 9 is 362 880, which is
     where the tab stops being interactive. Only the first few are kept for the
     panel; all of them are counted. */
  function topoAllOrders(G, cap, keep) {
    cap = cap === undefined ? 8 : cap;
    keep = keep === undefined ? 6 : keep;
    oracleCap('topoAllOrders', G.n, cap);
    var idx = dgIndex(G), indeg = new Array(G.n).fill(0);
    G.arcs.forEach(function (a) { indeg[a.v] += 1; });
    var used = new Array(G.n).fill(false), cur = [], shown = [], total = 0, steps = 0;
    (function walk() {
      if (cur.length === G.n) {
        total += 1;
        if (shown.length < keep) shown.push(cur.slice());
        return;
      }
      for (var v = 0; v < G.n; v += 1) {
        if (used[v] || indeg[v] > 0) continue;
        steps += 1;
        used[v] = true; cur.push(v);
        idx.out[v].forEach(function (id) { indeg[dgOther(G, id, v)] -= 1; });
        walk();
        idx.out[v].forEach(function (id) { indeg[dgOther(G, id, v)] += 1; });
        cur.pop(); used[v] = false;
      }
    })();
    return runOf({ count: total, orders: shown, unique: total === 1 },
                 { nodes: steps }, []);
  }

  /* An order is valid when EVERY arc points forward along it. Both arms of the
     topological mode are checked this way rather than trusted: two orders that
     differ can both be right, and the only thing that makes either right is
     this test. */
  function gkValidOrder(G, order) {
    if (!order || order.length !== G.n) return false;
    var pos = new Array(G.n).fill(-1);
    order.forEach(function (v, i) { pos[v] = i; });
    for (var i = 0; i < G.arcs.length; i += 1) {
      if (pos[G.arcs[i].u] >= pos[G.arcs[i].v]) return false;
    }
    return true;
  }

  /* ------------------------------ strongly connected components, by definition

     u and v are in one component iff each reaches the other. That is a
     traversal from every vertex and a pairwise test, which is O(V(V + E)) and
     has nothing in common with Kosaraju's two passes -- which is exactly why
     it is worth running beside them. */
  function sccBrute(G) {
    var idx = dgIndex(G), reach = [], s, v, u;
    for (s = 0; s < G.n; s += 1) {
      var seen = new Array(G.n).fill(false), stack = [s];
      seen[s] = true;
      while (stack.length) {
        var at = stack.pop();
        idx.out[at].forEach(function (id) {
          var to = dgOther(G, id, at);
          if (!seen[to]) { seen[to] = true; stack.push(to); }
        });
      }
      reach.push(seen);
    }
    var comp = new Array(G.n).fill(-1), comps = [];
    for (v = 0; v < G.n; v += 1) {
      if (comp[v] !== -1) continue;
      var id = comps.length, members = [];
      for (u = 0; u < G.n; u += 1) if (reach[v][u] && reach[u][v]) { comp[u] = id; members.push(u); }
      comps.push(members);
    }
    return { components: comps, componentOf: comp, reaches: reach };
  }
  /* Two component lists agree when they induce the same PARTITION; the names
     the two algorithms give the parts are their own business. */
  function samePartition(a, b) {
    var key = function (list) {
      return list.map(function (c) { return c.slice().sort(function (x, y) { return x - y; }).join('.'); })
        .sort().join('|');
    };
    return key(a) === key(b);
  }

  /* --------------------------------------- the cut property, against every tree

     The lemma says the lightest arc across a cut is in SOME minimum spanning
     tree. That is checked by listing every spanning tree, keeping the minimum-
     weight ones and looking. `inEvery` is the stronger statement and it is
     reported separately, because it holds exactly when that arc is strictly
     lightest across the cut -- and a reader who conflates the two has the
     uniqueness question wrong as well. */
  function cutVerdict(G, S, cap) {
    var cross = crossingEdges(G, S), all = allSpanningTrees(G, cap);
    var min = all.result.minWeight;
    var msts = all.result.trees.filter(function (t) { return t.weight === min; });
    var e = cross.lightest;
    var ties = e ? cross.crossing.filter(function (x) { return x.w === e.w; }).length : 0;
    /* How many of the minimum trees each arc appears in. Zero is the CYCLE
       property on screen: an arc in no minimum tree, which for a strictly
       heaviest arc on a cycle is exactly what the second lemma says. */
    var perArc = G.arcs.map(function (_a, id) {
      return msts.filter(function (t) { return t.arcs.indexOf(id) !== -1; }).length;
    });
    return {
      crossing: cross.crossing, lightest: e, ties: ties, perArc: perArc,
      trees: all.result.count, allTrees: all.result.trees,
      minWeight: min, msts: msts.length, mstList: msts,
      unique: msts.length === 1, examined: all.counts.nodes,
      inSome: e ? msts.some(function (t) { return t.arcs.indexOf(e.id) !== -1; }) : null,
      inEvery: e ? msts.every(function (t) { return t.arcs.indexOf(e.id) !== -1; }) : null
    };
  }
  /* The misconception: "the MST is the set of each vertex's lightest edge."
     Each such edge IS in a minimum tree -- take the cut separating that vertex
     from the rest -- and the set is usually not a spanning tree at all, which
     is a fact about sizes and is therefore computed. */
  function lightestPerVertex(G) {
    var idx = dgIndex(G), picked = {}, ids = [], v;
    for (v = 0; v < G.n; v += 1) {
      var best = -1;
      idx.out[v].concat(idx.inn[v]).forEach(function (id) {
        if (best === -1 || G.arcs[id].w < G.arcs[best].w) best = id;
      });
      if (best !== -1 && !picked[best]) { picked[best] = true; ids.push(best); }
    }
    ids.sort(function (a, b) { return a - b; });
    var H = dgNew(G.n, false);
    ids.forEach(function (id) { dgAdd(H, G.arcs[id].u, G.arcs[id].v, G.arcs[id].w, 0); });
    return { arcs: ids, weight: ids.reduce(function (t, id) { return t + G.arcs[id].w; }, 0),
             pieces: dgComponents(H).length, spans: ids.length === G.n - 1 };
  }

  /* --------------------------------------------- the upper-bound invariant

     d[v] is never below delta(s, v), at any point in any schedule. The truth is
     produced by Bellman-Ford, which is a different algorithm from any schedule
     this mode runs, and every step of the trace is tested against it -- so the
     invariant is checked rather than described. */
  function relaxInvariant(G, source, run) {
    var truth = bellmanFordRounds(G, source).result.dist, bad = [];
    (run.trace || []).forEach(function (step, k) {
      (step.dist || []).forEach(function (d, v) {
        if (d === null) return;
        if (truth[v] === null || d < truth[v]) bad.push({ step: k, v: v, d: d, delta: truth[v] });
      });
    });
    var final = run.result.dist, wrong = [];
    final.forEach(function (d, v) {
      var want = truth[v];
      if ((d === null) !== (want === null) || (d !== null && d !== want)) wrong.push(v);
    });
    return { truth: truth, violations: bad, holds: bad.length === 0,
             exact: wrong.length === 0, wrong: wrong };
  }
  /* E log V as a REFERENCE, not a verdict: `ilog2` is an integer logarithm and
     the product is compared with a measured count of heap operations by eye,
     in a column that says which of the two is a proof. */
  function gkHeapBound(G) { return G.arcs.length * ilog2(Math.max(2, G.n)); }

  /* Every weight negated. The longest-path claim is "negate and run the same
     pass", and the reason it holds only on a DAG is what the negated graph
     looks like when there is a cycle: a cycle of positive total becomes one of
     negative total, and no shortest walk exists. Building it is how the page
     shows that rather than saying it. */
  function gkNegate(G) {
    var H = dgCopy(G);
    H.arcs.forEach(function (a) { a.w = -a.w; });
    return H;
  }
  /* The number of ARCS on the path a parent array records, which is the figure
     Bellman-Ford's round count is compared against: a label settles in round k
     exactly when its shortest path uses k arcs. */
  function gkArcsOnPath(parent, source, v) {
    var path = gkPathTo(parent, source, v);
    return path === null ? null : path.length - 1;
  }

  /* A path from a parent array, as labels, or null when v was never reached. */
  function gkPathTo(parent, source, v) {
    var path = [v], at = v, guard = 0;
    while (at !== source) {
      at = parent[at];
      if (at === -1 || at === undefined || guard > parent.length + 1) return null;
      path.push(at);
      guard += 1;
    }
    return path.reverse();
  }
  function gkPathText(path) {
    return path === null ? 'not reached' : path.map(function (v) { return v + 1; }).join(' → ');
  }
  function gkDistText(d) { return d === null ? 'not reached' : String(d); }
  /* A distance array compared with GRAPH_JS.dijkstra's, whose sentinel is
     Infinity where this one is null. Comparing them requires saying so once. */
  function gkSameDistances(mine, theirs) {
    if (mine.length !== theirs.length) return false;
    for (var v = 0; v < mine.length; v += 1) {
      var a = mine[v] === null ? Infinity : mine[v];
      if (a !== theirs[v]) return false;
    }
    return true;
  }
  function gkPlural(n, one, many) { return n === 1 ? one : many; }
  /* The reader's chosen root FIRST and then every other vertex, so a graph in
     several pieces is still traversed whole. `dfsTimes([r])` alone would leave
     every vertex outside r's piece at d = f = 0, which is not a timestamp and
     would be painted as one. */
  function gkRootsFrom(root, n) {
    var out = [root], i;
    for (i = 0; i < n; i += 1) if (i !== root) out.push(i);
    return out;
  }
  /* A step index a control hands in, clamped into a trace that may have got
     shorter since it was set. Every mode keeps its step in one variable and
     clamps it on every redraw, which is what makes a second redraw safe. */
  function gkStep(want, length) {
    if (!length) return 0;
    var k = parseInt(want, 10);
    if (!isFinite(k) || k < 0) k = 0;
    return Math.min(k, length - 1);
  }
"""


# ---------------------------------------------------------------------------
# One core per mode, not one for the kit -- the largest single lever there is
# on page weight. `floyd` has no oracle enumeration in it and must not ship a
# spanning-tree sweep; `dfstimes` never takes a logarithm and must not carry
# the Discrete Mathematics graph block to avoid one.
# ---------------------------------------------------------------------------

_BASE_JS = COUNT_JS + DIGRAPH_JS + GRAPHKIT_JS + GKIT_JS
_ORACLE_BASE_JS = COUNT_JS + DIGRAPH_JS + ORACLE_JS + GRAPHKIT_JS + GKIT_JS
_CHECKED_JS = COUNT_JS + DIGRAPH_JS + GRAPHKIT_JS + GRAPH_JS + GKIT_JS
# `prim` needs ALGO_JS because primRun returns E log V as a field and therefore
# calls ilog2 whether or not the page prints it; `relax` needs the logarithm for
# the same column AND graph.py's Dijkstra as the oracle beside its own.
_LOG_JS = COUNT_JS + DIGRAPH_JS + GRAPHKIT_JS + ALGO_JS + GKIT_JS
_HEAP_JS = COUNT_JS + DIGRAPH_JS + GRAPHKIT_JS + GRAPH_JS + ALGO_JS + GKIT_JS


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every kit on this path uses, so a reader
# crossing a course boundary meets the same widgets. Drawings take only the two
# viewBox widths theme.py gives a horizontal-scroll minimum -- 520 and 660 --
# because any other width shrinks the labels to illegibility on a phone
# instead of scrolling it.
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

    Every arc a reader types here can contain a `>`, and a default carried in
    the markup cannot hold one: escaped as `&gt;` a browser decodes it and
    scripts/labcheck.js does not, and left raw it terminates that harness's own
    tag scan and the value is lost. network.py met this first and this is the
    same answer -- the value goes in from the script before the first redraw,
    and the placeholder, which carries no `>`, still says what the box is for.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(str(value).replace(">", " to ")))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _buttons(items):
    return ('        <div class="btn-row">%s</div>\n'
            % "".join('<button class="btn small" id="%s" type="button">%s</button>' % (cid, text)
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
    """The preset table as data the script reads, not as branches.

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


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "graphkit: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form. An algorithm run on the graph
# on screen produces a fact about THAT graph; a lemma is a statement about all
# of them. Spelled once so no mode can quietly drop it, and each mode says it
# in its own nouns so no two pages say the same words.
_ONE_GRAPH = (
    "  /* Every number below came from running the algorithm on the graph on\n"
    "     screen. That is one graph. A lemma is a statement about all of them,\n"
    "     and this kit never reads one off a single run: where a page prints a\n"
    "     claim about every graph it either enumerates the whole space at a cap\n"
    "     it states, or it names the proof the lesson gives. */\n"
)


# ---------------------------------------------------------------------------
# dfstimes -- one traversal, and the four things the timestamps say
# ---------------------------------------------------------------------------

_DT_PRESETS = [
    {
        "id": "allfour",
        "label": "one graph with all four edge classes on it",
        "spec": "1>2, 1>4, 2>5, 4>2, 5>4, 3>5, 3>6, 6>3",
        "root": "1",
        "note": "four tree arcs, two back, one forward and one cross, from a single walk",
    },
    {
        "id": "dag",
        "label": "no back edge anywhere, so it is acyclic",
        "spec": "1>2, 2>3, 1>3, 1>4, 4>3",
        "root": "1",
        "note": "1 to 3 is a forward arc: it reaches a vertex already finished inside 1",
    },
    {
        "id": "nested",
        "label": "a long chain, so every interval nests inside the last",
        "spec": "1>2, 2>3, 3>4, 4>5, 5>1, 3>1",
        "root": "1",
        "note": "the intervals are five nested brackets and both back arcs close them",
    },
    {
        "id": "diamond",
        "label": "read it undirected and the forward arc stops existing",
        "spec": "1>2, 1>3, 2>4, 3>4",
        "root": "1",
        "note": "switch the reading below: undirected leaves only tree and back edges",
    },
]


def _dfstimes(cfg):
    chosen = _chosen(_DT_PRESETS, cfg)
    markup = (
        _toolbar(
            "Timestamps, and the four classes they decide",
            "one walk, four different things read off it",
            [("cyan", "the class you asked to see"), ("muted", "every other arc"),
             ("purple", "discovery and finish, as an interval")],
        )
        + _stage(_svg("dtPlot", "0 0 660 300",
                      "The graph, with the arcs of the chosen class drawn heavy.")
                 + _svg("dtBars", "0 0 660 220",
                        "One bar per vertex from its discovery time to its finish time, so "
                        "nesting and disjointness are visible."))
        + _table("dtVerts")
        + _table("dtEdges")
        + _banner("dtStatus")
    )
    controls = (
        _select("dtPreset", "Worked example", _options(_DT_PRESETS), chosen["id"])
        + _text("dtSpec", "Arcs, as tail&gt;head", chosen["spec"])
        + _range("dtRoot", "Start the walk at", 1, 12, chosen["root"])
        + _select("dtRead", "Read the arcs as",
                  [("directed", "directed, as typed"),
                   ("undirected", "undirected, ignoring the arrows")], "directed")
        + _select("dtShow", "Draw heavy the arcs that are",
                  [("tree", "tree arcs"), ("back", "back arcs"),
                   ("forward", "forward arcs"), ("cross", "cross arcs")], "back")
        + _kpis([("Tree arcs", "dtTree"), ("Back arcs", "dtBack"),
                 ("Forward arcs", "dtFwd"), ("Cross arcs", "dtCross"),
                 ("Pairs whose intervals nest", "dtNest"),
                 ("Pairs that overlap without nesting", "dtOver")])
        + _hint(
            "dtHint",
            "An arc is <span class=\"tt\">tail&gt;head</span> and labels start at 1. The class of "
            "an arc is decided by the times at its ends and nothing else: tree when the arc is the "
            "one that discovered its head, back when the head is still open, forward when the head "
            "is a finished descendant, cross otherwise. Switch the reading to undirected and watch "
            "two of the four counts go to zero.",
        )
    )
    script = _BASE_JS + _ONE_GRAPH + _presets_js("DTP", _DT_PRESETS, ["spec", "root", "note"]) + r"""
  var presetIn = document.getElementById('dtPreset'), specIn = document.getElementById('dtSpec');
  var rootIn = document.getElementById('dtRoot'), rootOut = document.getElementById('dtRootOut');
  var readIn = document.getElementById('dtRead'), showIn = document.getElementById('dtShow');
  var plot = document.getElementById('dtPlot'), bars = document.getElementById('dtBars');
  var verts = document.getElementById('dtVerts'), edgesT = document.getElementById('dtEdges');
  var status = document.getElementById('dtStatus');
  var KPIS = ['dtTree', 'dtBack', 'dtFwd', 'dtCross', 'dtNest', 'dtOver'];

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; verts.innerHTML = ''; edgesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> One clause is a tail, then '
      + '<span class="tone-muted">&gt;</span>, then a head: <span class="tt">1&gt;2, 2&gt;3</span>.';
  }

  /* One bar per vertex, from d to f. Two vertices' bars either nest or are
     disjoint, and the drawing is the theorem: there is no third picture. */
  function intervalBars(times, n) {
    var span = 2 * n, rowH = Math.min(18, Math.max(12, Math.floor(200 / n))), s = '', v;
    for (v = 0; v < n; v += 1) {
      var y = 6 + v * rowH;
      var x1 = 30 + ((times.d[v] - 1) / span) * 600;
      var x2 = 30 + (times.f[v] / span) * 600;
      s += '<text x="4" y="' + (y + rowH - 7) + '" font-size="10" font-weight="700" '
        + 'fill="var(--muted)">' + (v + 1) + '</text>';
      s += '<rect x="' + x1.toFixed(1) + '" y="' + y + '" width="' + Math.max(3, x2 - x1).toFixed(1)
        + '" height="' + (rowH - 4) + '" rx="3" fill="var(--purple)" opacity="0.18" '
        + 'stroke="var(--purple)" />';
      s += '<text x="' + (x1 + 4).toFixed(1) + '" y="' + (y + rowH - 8) + '" font-size="9" '
        + 'fill="var(--text)">' + times.d[v] + '</text>';
      s += '<text x="' + (x2 - 4).toFixed(1) + '" y="' + (y + rowH - 8) + '" font-size="9" '
        + 'text-anchor="end" fill="var(--text)">' + times.f[v] + '</text>';
    }
    return s;
  }

  function reasonFor(e, times) {
    var d = times.d, f = times.f;
    if (e.kind === 'tree') return 'this arc discovered ' + (e.v + 1);
    if (e.kind === 'back') return 'd(' + (e.v + 1) + ') = ' + d[e.v] + ' &le; d(' + (e.u + 1)
      + ') = ' + d[e.u] + ' and ' + (e.u + 1) + ' finishes first, so the head is still open';
    if (e.kind === 'forward') return (e.v + 1) + ' is a finished descendant: ' + d[e.u] + ' &lt; '
      + d[e.v] + ' and ' + f[e.v] + ' &lt; ' + f[e.u];
    return 'the two intervals are disjoint, so neither end is an ancestor of the other';
  }

  function redraw() {
    var directed = readIn.value === 'directed';
    var parsed = gkParse(specIn.value, directed);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    rootIn.max = n;
    var root = gkStep(parseInt(rootIn.value, 10) - 1, n);
    rootOut.textContent = String(root + 1);

    var roots = gkRootsFrom(root, n);
    var run = dfsTimes(G, roots), times = run.result;
    var kinds, counts;
    if (directed) {
      kinds = classifyEdges(G, times);
      counts = edgeKindCounts(kinds);
    } else {
      var u = gkUndirectedKinds(G, roots);
      kinds = u.edges; counts = u.counts; times = u.times;
    }
    var paren = parenthesisCheck(times);
    var want = showIn.value;
    var heavy = kinds.filter(function (e) { return e.kind === want; }).map(function (e) { return e.id; });

    var colours = new Array(n).fill(-1);
    times.roots.forEach(function (r) { colours[r] = 3; });
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: heavy, label: 'none', colours: colours });
    bars.innerHTML = intervalBars(times, n);

    var rows = '';
    for (var v = 0; v < n; v += 1) {
      rows += '<tr><th class="rowhead">' + (v + 1) + '</th><td>' + times.d[v] + '</td><td>'
        + times.f[v] + '</td><td>' + (times.parent[v] === -1 ? 'a root of the forest'
            : String(times.parent[v] + 1)) + '</td><td>[' + times.d[v] + ', ' + times.f[v]
        + ']</td><td>' + (times.f[v] - times.d[v] - 1) / 2 + '</td></tr>';
    }
    verts.innerHTML = '<caption>One row per vertex: the two times, the arc that discovered it, '
      + 'and how many other vertices its interval contains</caption><thead><tr><th>vertex</th>'
      + '<th>d</th><th>f</th><th>discovered by</th><th>interval</th><th>descendants</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var TONE = { tree: 'cyan', back: 'red', forward: 'amber', cross: 'purple' };
    var erows = '';
    kinds.forEach(function (e) {
      erows += '<tr' + (e.kind === want ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + (directed ? ((e.u + 1) + ' → ' + (e.v + 1)) : ((e.u + 1) + ' – ' + (e.v + 1)))
        + '</th><td><span class="tone-' + TONE[e.kind] + '">' + e.kind + '</span></td><td>'
        + reasonFor(e, times) + '</td></tr>';
    });
    edgesT.innerHTML = '<caption>Every arc, classified from the times at its ends</caption>'
      + '<thead><tr><th>arc</th><th>class</th><th>why that class and no other</th></tr></thead>'
      + '<tbody>' + erows + '</tbody>';

    document.getElementById('dtTree').textContent = counts.tree;
    document.getElementById('dtBack').textContent = counts.back;
    document.getElementById('dtFwd').textContent = counts.forward;
    document.getElementById('dtCross').textContent = counts.cross;
    document.getElementById('dtNest').textContent = paren.nested;
    document.getElementById('dtOver').textContent = paren.overlapping
      + (paren.overlapping ? ' — the theorem fails' : ' — as the theorem says');

    var acyclic = counts.back === 0;
    status.innerHTML = '<strong>' + counts.tree + ' tree, ' + counts.back + ' back, '
      + counts.forward + ' forward, ' + counts.cross + ' cross</strong> on '
      + G.arcs.length + ' arc' + gkPlural(G.arcs.length, '', 's') + ', from one walk starting at '
      + '<span class="tone-cyan">' + (root + 1) + '</span>. '
      + 'The parenthesis theorem was checked on all ' + paren.pairs + ' pairs of vertices: '
      + '<span class="tone-purple">' + paren.nested + '</span> nest, '
      + '<span class="tone-muted">' + paren.disjoint + '</span> are disjoint, and '
      + '<span class="' + (paren.overlapping ? 'tone-red' : 'tone-green') + '">'
      + paren.overlapping + '</span> overlap without nesting. '
      + (paren.holds
          ? 'Every pair that nests is an ancestor pair and every ancestor pair nests, so on this '
            + 'graph the theorem is not quoted, it is verified. '
          : '<span class="tone-red">This cannot happen: '
            + (paren.violations.length
                ? paren.violations.length + ' pair where nesting and descent disagree'
                : paren.overlapping + ' pair of intervals that overlap without nesting')
            + '.</span> ')
      + (directed
          ? (acyclic
              ? 'No back arc, so this digraph is acyclic and a topological order exists.'
              : 'There are ' + counts.back + ' back arc' + gkPlural(counts.back, '', 's')
                + ', and each one closes a cycle with the tree path above it.')
          : 'Read undirected, forward and cross came out at <span class="tone-green">'
            + counts.forward + '</span> and <span class="tone-green">' + counts.cross
            + '</span>. Both are directed phenomena: an undirected edge to a discovered vertex '
            + 'always reaches an ancestor, because the far end could not have been finished while '
            + 'this end was still open.');
  }

  function apply() {
    var p = DTP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; rootIn.value = p.root;
    redraw();
  }
  var START = DTP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; rootIn.value = START.root; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  rootIn.addEventListener('input', redraw);
  readIn.addEventListener('change', redraw);
  showIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Discovery and finish times, and the four edge classes",
        subtitle="One depth-first walk; the intervals nest exactly when one vertex is inside the other",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a graph, pick where the walk starts"),
        panel_intro=cfg.get(
            "panel_intro",
            "The walk runs in your browser and every class is decided from the two times at the "
            "arc's ends. The parenthesis theorem is checked on every ordered pair of vertices, "
            "not stated.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# topo -- two orders, both right, and a number for "is it unique"
# ---------------------------------------------------------------------------

_TP_PRESETS = [
    {
        "id": "twoways",
        "label": "a task graph whose order is not unique",
        "spec": "1>3, 2>3, 3>4, 3>5, 4>6, 5>6",
        "note": "two independent starts and two independent middles, so the order is a choice",
    },
    {
        "id": "chain",
        "label": "a chain, where the order is forced",
        "spec": "1>2, 2>3, 3>4, 4>5",
        "note": "one valid order in all, which is what uniqueness looks like as a number",
    },
    {
        "id": "diamond",
        "label": "a diamond: exactly two orders",
        "spec": "1>2, 1>3, 2>4, 3>4",
        "note": "the two middles can go in either order and nothing else can move",
    },
    {
        "id": "cycle",
        "label": "a cycle, so no order exists at all",
        "spec": "1>2, 2>3, 3>1, 3>4",
        "note": "the walk finds a back arc and Kahn's queue empties early: two witnesses, one cause",
    },
]

_TP_CAP = 8


def _topo(cfg):
    chosen = _chosen(_TP_PRESETS, cfg)
    markup = (
        _toolbar(
            "Reverse postorder, Kahn's queue, and how many orders there are",
            "two methods, two orders, both valid when either is",
            [("cyan", "placed in order"), ("red", "the back arc, when there is one"),
             ("muted", "still waiting on something")],
        )
        + _stage(_svg("tpPlot", "0 0 660 220",
                      "The vertices laid out left to right in the order found, so every arc "
                      "points forward when an order exists.")
                 + _svg("tpRing", "0 0 520 280",
                        "The same graph drawn as typed, with the back arc drawn heavy when the "
                        "graph has a cycle."))
        + _table("tpSteps")
        + _table("tpOrders")
        + _banner("tpStatus")
    )
    controls = (
        _select("tpPreset", "Worked example", _options(_TP_PRESETS), chosen["id"])
        + _text("tpSpec", "Arcs, as tail&gt;head", chosen["spec"])
        + _select("tpDraw", "Lay the vertices out by",
                  [("dfs", "reverse finishing order"), ("kahn", "Kahn's order")], "dfs")
        + _kpis([("Valid orders in all", "tpCount"),
                 ("Do the two methods agree", "tpAgree"),
                 ("Vertices Kahn placed", "tpPlaced"),
                 ("Sources: in-degree zero", "tpSources"),
                 ("Back arc found by the walk", "tpBack"),
                 ("Every arc points forward", "tpValid")])
        + _hint(
            "tpHint",
            "The two methods are not two implementations of one order. Reverse finishing order "
            "comes out of a depth-first walk; Kahn's comes out of repeatedly taking a vertex "
            "nothing points at. Both are valid orders when the graph is acyclic, and they are "
            "usually different &mdash; which is the answer to whether the order is unique, and the "
            "count beside it is the same answer as a number.",
        )
    )
    script = _ORACLE_BASE_JS + _ONE_GRAPH + _presets_js("TPP", _TP_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('tpPreset'), specIn = document.getElementById('tpSpec');
  var drawIn = document.getElementById('tpDraw');
  var plot = document.getElementById('tpPlot'), ring = document.getElementById('tpRing');
  var steps = document.getElementById('tpSteps'), orders = document.getElementById('tpOrders');
  var status = document.getElementById('tpStatus');
  var KPIS = ['tpCount', 'tpAgree', 'tpPlaced', 'tpSources', 'tpBack', 'tpValid'];
  var CAP = """ + str(_TP_CAP) + r""";

  function blank(why) {
    plot.innerHTML = ''; ring.innerHTML = ''; steps.innerHTML = ''; orders.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Arcs are directed here: '
      + '<span class="tt">1&gt;2</span> means 1 must come before 2.';
  }

  /* Left to right along the order, alternating above and below the axis so a
     long arc does not run through a vertex it has nothing to do with. */
  function orderPoints(order, n) {
    var pts = new Array(n), i;
    (order || []).forEach(function (v, k) {
      pts[v] = [40 + (order.length < 2 ? 290 : (k / (order.length - 1)) * 580),
                110 + (k % 2 ? 58 : -48)];
    });
    for (i = 0; i < n; i += 1) if (!pts[i]) pts[i] = [40 + i * 30, 190];
    return pts;
  }

  function orderText(order) {
    return order === null ? 'none exists' : order.map(function (v) { return v + 1; }).join(' → ');
  }

  function redraw() {
    var parsed = gkParse(specIn.value, true);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var dfsArm = topoDfs(G), kahn = topoKahn(G);
    var acyclic = dfsArm.result.acyclic;
    var dfsOrder = dfsArm.result.order, kahnOrder = kahn.result.order;
    var dfsOk = gkValidOrder(G, dfsOrder), kahnOk = gkValidOrder(G, kahnOrder);

    var total = null, shown = [], refused = null;
    try {
      var every = topoAllOrders(G, CAP, 6);
      total = every.result.count; shown = every.result.orders;
    } catch (err) { refused = err.message; }

    var layout = drawIn.value === 'kahn' ? kahnOrder : dfsOrder;
    var back = dfsArm.result.backEdge;
    plot.innerHTML = dgSvg(G, { points: orderPoints(layout || [], n), label: 'none',
                                highlight: back ? [back.id] : [] });
    ring.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 260, cy: 140, radius: 108 }),
                                label: 'none', highlight: back ? [back.id] : [] });

    var srows = '', sources = 0, i;
    for (i = 0; i < n; i += 1) if (kahn.result.indegree[i] === 0) sources += 1;
    kahn.trace.forEach(function (st) {
      srows += '<tr><th class="rowhead">' + (st.at + 1) + '</th><td class="tone-cyan">'
        + (st.took + 1) + '</td><td>' + st.indeg.map(function (d, v) {
            return (v + 1) + ':' + d; }).join('  ') + '</td><td>'
        + (st.queue.length ? gkNames(st.queue) : 'empty') + '</td></tr>';
    });
    steps.innerHTML = '<caption>Kahn’s method, one row per vertex taken: the in-degree table '
      + 'as it stood, and what was left ready</caption><thead><tr><th>step</th><th>took</th>'
      + '<th>in-degrees before it</th><th>ready afterwards</th></tr></thead><tbody>' + srows
      + '</tbody>';

    var orows = '<tr><th class="rowhead">reverse finishing order</th><td class="tone-'
      + (dfsOk ? 'cyan' : 'red') + '">' + orderText(dfsOrder) + '</td><td>'
      + (dfsOk ? 'every arc points forward along it' : 'not a valid order') + '</td></tr>'
      + '<tr><th class="rowhead">Kahn’s order</th><td class="tone-'
      + (kahnOk ? 'cyan' : 'red') + '">' + orderText(kahnOrder) + '</td><td>'
      + (kahnOk ? 'and so does this one' : 'not a valid order') + '</td></tr>';
    shown.forEach(function (o, k) {
      orows += '<tr><th class="rowhead">order ' + (k + 1) + ' of ' + total + '</th><td>'
        + orderText(o) + '</td><td>' + (gkValidOrder(G, o) ? 'valid' : 'invalid') + '</td></tr>';
    });
    orders.innerHTML = '<caption>The two methods’ answers, then the enumeration they are '
      + 'two of</caption><thead><tr><th>where it came from</th><th>order</th><th>checked</th>'
      + '</tr></thead><tbody>' + orows + '</tbody>';

    document.getElementById('tpCount').textContent = refused ? 'too big to enumerate' : String(total);
    document.getElementById('tpAgree').textContent = !acyclic ? 'neither exists'
      : (orderText(dfsOrder) === orderText(kahnOrder) ? 'same order' : 'different, both valid');
    document.getElementById('tpPlaced').textContent = kahn.result.stuckAt + ' of ' + n;
    document.getElementById('tpSources').textContent = sources;
    document.getElementById('tpBack').textContent = back
      ? ((back.u + 1) + ' → ' + (back.v + 1)) : 'none';
    document.getElementById('tpValid').textContent = acyclic
      ? (dfsOk && kahnOk ? 'yes, for both' : 'no') : 'no order to check';

    if (!acyclic) {
      status.innerHTML = '<strong><span class="tone-red">No topological order exists.</span></strong> '
        + 'The walk found the back arc <span class="tone-red">' + (back.u + 1) + ' → '
        + (back.v + 1) + '</span>, which closes a cycle with the tree path from ' + (back.v + 1)
        + ' down to ' + (back.u + 1) + ': along any order ' + (back.v + 1) + ' would have to come '
        + 'before ' + (back.u + 1) + ' and after it. Kahn’s method says the same thing '
        + 'differently &mdash; it placed <span class="tone-red">' + kahn.result.stuckAt
        + ' of ' + n + '</span> vertices and then every remaining in-degree was positive, because '
        + 'each vertex in the cycle is waiting on another one in it.';
      return;
    }
    status.innerHTML = '<strong>Both orders are valid.</strong> Reverse finishing order gives '
      + '<span class="tone-cyan">' + orderText(dfsOrder) + '</span> and Kahn’s queue gives '
      + '<span class="tone-cyan">' + orderText(kahnOrder) + '</span>'
      + (orderText(dfsOrder) === orderText(kahnOrder)
          ? ' &mdash; the same one, on this graph. '
          : ' &mdash; and they are different, which settles the question: the order is not a '
            + 'property of the graph. ')
      + (refused
          ? 'Counting every order is refused above ' + CAP + ' vertices rather than run slowly: '
            + refused + '.'
          : 'There are <span class="tone-purple">' + total + '</span> valid order'
            + gkPlural(total, '', 's') + ' in all, found by taking every in-degree-zero vertex at '
            + 'every step. ' + (total === 1
                ? 'One: here the order really is forced, and a chain is why.'
                : 'Each of the two methods produces one of them and neither can produce the '
                  + 'others, so neither is "the" order.'));
  }

  function apply() {
    var p = TPP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = TPP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  drawIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Topological order, two ways, and how many there are",
        subtitle="A reverse postorder and an in-degree queue; on a cycle, neither exists and both say so",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the dependencies"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both orders are produced in your browser and both are checked arc by arc. The count "
            "of valid orders is an enumeration, not an estimate, and it is refused rather than "
            "run slowly above the size it states.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# lowlink -- one pass, against deleting each edge and recounting
# ---------------------------------------------------------------------------

_LL_PRESETS = [
    {
        "id": "twoblocks",
        "label": "two triangles joined by one edge",
        "spec": "1-2, 2-3, 3-1, 3-4, 4-5, 5-6, 6-4",
        "note": "one bridge, and both of its ends are cut vertices",
    },
    {
        "id": "rootrule",
        "label": "the root, with two children and no back edge to help",
        "spec": "1-2, 1-3, 2-3, 1-4",
        "note": "the root is a cut vertex here because the walk gave it two children",
    },
    {
        "id": "parallel",
        "label": "two edges between the same pair",
        "spec": "1-2, 1-2, 2-3",
        "note": "a second edge between 1 and 2 stops that pair being a bridge, and a matrix "
                "cannot hold the graph at all",
    },
    {
        "id": "cycle",
        "label": "one cycle: nothing to cut",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-1",
        "note": "every edge lies on a cycle, so no edge is a bridge and no vertex is a cut vertex",
    },
    {
        "id": "path",
        "label": "a path: every interior edge is a bridge",
        "spec": "1-2, 2-3, 3-4, 4-5",
        "note": "four bridges and three cut vertices, and the two ends are neither",
    },
]


def _lowlink(cfg):
    chosen = _chosen(_LL_PRESETS, cfg)
    markup = (
        _toolbar(
            "Low-links, bridges and cut vertices in one pass",
            "and the same answer found again by deleting things",
            [("cyan", "a bridge"), ("red", "a cut vertex"), ("muted", "neither")],
        )
        + _stage(_svg("llPlot", "0 0 660 300",
                      "The graph, with bridges drawn heavy and cut vertices filled.")
                 + _svg("llLow", "0 0 660 120",
                        "For each vertex, its discovery time and the earliest time its subtree "
                        "can reach, drawn as a step down."))
        + _table("llVerts")
        + _table("llEdges")
        + _banner("llStatus")
    )
    controls = (
        _select("llPreset", "Worked example", _options(_LL_PRESETS), chosen["id"])
        + _text("llSpec", "Edges, as one&minus;other", chosen["spec"])
        + _kpis([("Bridges", "llBridges"), ("Cut vertices", "llCuts"),
                 ("Pieces the graph is already in", "llComps"),
                 ("Agrees with delete-and-recount", "llAgree"),
                 ("Edges examined by the brute force", "llWork"),
                 ("Parallel pairs a matrix cannot hold", "llPar")])
        + _hint(
            "llHint",
            "An edge is <span class=\"tt\">1&minus;2</span>. <span class=\"tt\">low(v)</span> is the "
            "earliest discovery time reachable from v's subtree using tree edges and at most one "
            "back edge, and the tree edge into v is a bridge exactly when "
            "<span class=\"tt\">low(v) &gt; d(u)</span> &mdash; nothing in v's subtree can get above "
            "u without it. Write a second edge between the same pair and watch a bridge stop "
            "being one.",
        )
    )
    script = _CHECKED_JS + _ONE_GRAPH + _presets_js("LLP", _LL_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('llPreset'), specIn = document.getElementById('llSpec');
  var plot = document.getElementById('llPlot'), lowPlot = document.getElementById('llLow');
  var verts = document.getElementById('llVerts'), edgesT = document.getElementById('llEdges');
  var status = document.getElementById('llStatus');
  var KPIS = ['llBridges', 'llCuts', 'llComps', 'llAgree', 'llWork', 'llPar'];

  function blank(why) {
    plot.innerHTML = ''; lowPlot.innerHTML = ''; verts.innerHTML = ''; edgesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is two labels with a '
      + 'hyphen between them: <span class="tt">1-2, 2-3</span>.';
  }

  /* d and low side by side, one pair of marks per vertex: where low sits below
     d is exactly where a back edge reached above the vertex. */
  function lowStrip(low, d, n) {
    var span = Math.max(1, 2 * n), s = '', v;
    for (v = 0; v < n; v += 1) {
      var x = 30 + (v / Math.max(1, n - 1)) * 600;
      var yd = 100 - (d[v] / span) * 80, yl = 100 - (low[v] / span) * 80;
      s += '<line x1="' + x.toFixed(1) + '" y1="' + yd.toFixed(1) + '" x2="' + x.toFixed(1)
        + '" y2="' + yl.toFixed(1) + '" stroke="var(--amber)" stroke-width="2" />';
      s += '<circle cx="' + x.toFixed(1) + '" cy="' + yd.toFixed(1)
        + '" r="4" fill="var(--cyan)" />';
      s += '<circle cx="' + x.toFixed(1) + '" cy="' + yl.toFixed(1)
        + '" r="4" fill="var(--purple)" />';
      s += '<text x="' + x.toFixed(1) + '" y="114" text-anchor="middle" font-size="10" '
        + 'fill="var(--muted)">' + (v + 1) + '</text>';
      s += '<text x="' + (x + 7).toFixed(1) + '" y="' + (yl - 4).toFixed(1) + '" font-size="9" '
        + 'fill="var(--purple)">' + low[v] + '</text>';
    }
    s += '<text x="6" y="14" font-size="10" fill="var(--cyan)">d</text>'
      + '<text x="6" y="28" font-size="10" fill="var(--purple)">low</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, false);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;

    var run = lowLink(G), res = run.result;
    /* The DFS tree the low-link pass built, recovered by running the same walk
       through dfsTimes. Both start at the lowest unvisited label and both scan
       a vertex's incident arcs in arc order, so it is the SAME tree -- which is
       what makes the child counts below the counts the root rule is about. A
       root control would break exactly that, which is why there is none: lowLink
       takes no root, and a tree drawn from a different one would put a parent
       beside a low-link computed under another. */
    var tree = dfsTimes(G).result;
    var children = new Array(n).fill(0);
    for (var v = 0; v < n; v += 1) if (tree.parent[v] !== -1) children[tree.parent[v]] += 1;
    var isCut = {}; res.cutVertices.forEach(function (x) { isCut[x] = true; });
    var isBridge = {}; res.bridges.forEach(function (b) { isBridge[b.id] = true; });

    /* THE ORACLE. graph.py's cuts() deletes each edge and recounts the
       components; it is a matrix, so a parallel pair cannot be handed to it and
       the panel says so instead of comparing against a different graph. */
    var ready = gkOracleReady(G), agree = null, theirs = null;
    if (ready.ok) {
      N = n; A = dgToMatrix(G);
      LESSON = lessonFrom(gkLessonList(G)); useLessonWeights = true;
      theirs = cuts();
      var mineB = res.bridges.map(function (b) {
        return Math.min(b.u, b.v) + '-' + Math.max(b.u, b.v); }).sort().join(' ');
      var theirB = theirs.bridges.map(function (b) {
        return Math.min(b.edge[0], b.edge[1]) + '-' + Math.max(b.edge[0], b.edge[1]); }).sort().join(' ');
      agree = mineB === theirB && res.cutVertices.join(',') === theirs.cutVertices.join(',');
    }

    var colours = new Array(n).fill(-1);
    res.cutVertices.forEach(function (x) { colours[x] = 4; });
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: res.bridges.map(function (b) { return b.id; }),
                                label: 'none', colours: colours });
    lowPlot.innerHTML = lowStrip(res.low, res.d, n);

    var rows = '';
    for (v = 0; v < n; v += 1) {
      var why;
      if (tree.parent[v] === -1) {
        why = children[v] > 1
          ? 'a root of the walk with ' + children[v] + ' children, so removing it separates them'
          : 'a root of the walk with ' + children[v] + ' child' + gkPlural(children[v], '', 'ren')
            + ', so it is not one however many back edges it has';
      } else {
        why = isCut[v]
          ? 'some child c has low(c) &ge; d(v), so that child cannot get above v'
          : 'every child reaches strictly above v, so the graph survives without it';
      }
      rows += '<tr' + (isCut[v] ? ' class="tone-red"' : '') + '><th class="rowhead">' + (v + 1)
        + '</th><td>' + res.d[v] + '</td><td>' + res.low[v] + '</td><td>'
        + (tree.parent[v] === -1 ? 'root' : String(tree.parent[v] + 1)) + '</td><td>'
        + children[v] + '</td><td>' + (isCut[v] ? 'cut vertex' : 'no') + '</td><td>' + why
        + '</td></tr>';
    }
    verts.innerHTML = '<caption>One row per vertex: the two numbers, its place in the walk’s '
      + 'tree, and the rule that decided it</caption><thead><tr><th>vertex</th><th>d</th>'
      + '<th>low</th><th>parent</th><th>children</th><th>cut vertex</th><th>by which rule</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var erows = '';
    G.arcs.forEach(function (a, id) {
      var deep = res.d[a.u] > res.d[a.v] ? a.u : a.v, up = deep === a.u ? a.v : a.u;
      erows += '<tr' + (isBridge[id] ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + gkEdgeName(a) + '</th><td>' + (isBridge[id] ? 'bridge' : 'not a bridge') + '</td><td>'
        + 'low(' + (deep + 1) + ') = ' + res.low[deep] + (res.low[deep] > res.d[up] ? ' &gt; ' : ' &le; ')
        + 'd(' + (up + 1) + ') = ' + res.d[up] + '</td><td>'
        + (isBridge[id]
            ? 'deleting it leaves the graph in more pieces'
            : 'something in the deeper side reaches ' + (up + 1) + ' or above without it')
        + '</td></tr>';
    });
    edgesT.innerHTML = '<caption>Every edge, with the comparison that decided it</caption>'
      + '<thead><tr><th>edge</th><th>verdict</th><th>the comparison</th><th>what that means</th>'
      + '</tr></thead><tbody>' + erows + '</tbody>';

    document.getElementById('llBridges').textContent = res.bridges.length
      ? res.bridges.map(function (b) { return (b.u + 1) + '–' + (b.v + 1); }).join(', ') : 'none';
    document.getElementById('llCuts').textContent = res.cutVertices.length
      ? gkNames(res.cutVertices) : 'none';
    document.getElementById('llComps').textContent = dgComponents(G).length;
    document.getElementById('llAgree').textContent = ready.ok
      ? (agree ? 'yes, exactly' : 'no — report it') : 'cannot be asked';
    document.getElementById('llWork').textContent = ready.ok
      ? (G.arcs.length + n) + ' deletions and recounts' : '—';
    document.getElementById('llPar').textContent = ready.parallel.length || 'none';

    var mine = res.bridges.length + ' bridge' + gkPlural(res.bridges.length, '', 's') + ' and '
      + res.cutVertices.length + ' cut vert' + gkPlural(res.cutVertices.length, 'ex', 'ices');
    status.innerHTML = '<strong>' + mine + '</strong>, from one walk of '
      + run.counts.calls + ' calls over ' + G.arcs.length + ' edge'
      + gkPlural(G.arcs.length, '', 's') + '. '
      + (ready.ok
          ? (agree
              ? 'The same graph was handed to the brute force that finds these by <em>deleting '
                + 'each edge and counting the components again</em>, ' + (G.arcs.length + n)
                + ' times over, and it returned <span class="tone-green">the same sets</span>. '
                + 'Two answers from two definitions, and the fast one is a single pass.'
              : '<span class="tone-red">The brute force disagrees, which means one of the two is '
                + 'wrong — that is what this panel is for.</span> ')
          : '<span class="tone-amber">The brute force cannot be asked about this graph: '
            + ready.why + '.</span> That is not a limitation of the check but of the '
            + 'representation it needs &mdash; and it is the reason a bridge here is excluded from a '
            + 'walk by its arc rather than by its two ends. ')
      + (res.bridges.length
          ? 'Each bridge is a tree edge whose deeper end cannot reach above its shallower one: '
            + 'low of the deeper end is strictly greater than d of the other.'
          : 'No edge is a bridge, so every edge lies on a cycle &mdash; there is a second route '
            + 'between its ends and the low-link pass found it.');
  }

  function apply() {
    var p = LLP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = LLP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bridges and cut vertices by low-link",
        subtitle="One pass computes what deleting every edge in turn also computes, and the page runs both",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the graph, then try to break the rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "The low-links come from one depth-first pass. The bridges and cut vertices are then "
            "found again the slow way &mdash; delete each edge, recount the components &mdash; and "
            "the two answers are compared in front of you.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# scc -- two passes, and the condensation they always produce
# ---------------------------------------------------------------------------

_SC_PRESETS = [
    {
        "id": "three",
        "label": "three components, one of them a single vertex",
        "spec": "1>2, 2>3, 3>1, 3>4, 4>5, 5>6, 6>4, 5>7",
        "note": "a triangle, another cycle below it, and a vertex nothing comes back from",
    },
    {
        "id": "onebig",
        "label": "one cycle through everything",
        "spec": "1>2, 2>3, 3>4, 4>1",
        "note": "every vertex reaches every other, so there is one component and the "
                "condensation is a single point",
    },
    {
        "id": "dag",
        "label": "acyclic, so every vertex is its own component",
        "spec": "1>2, 2>3, 1>3, 3>4",
        "note": "the condensation is the graph itself, which is the case the second pass has "
                "nothing to do in",
    },
    {
        "id": "sourcefirst",
        "label": "a source component above a sink component",
        "spec": "1>2, 2>1, 2>3, 3>4, 4>3",
        "note": "the latest finishing vertex is in the SOURCE component, which is why the "
                "second pass runs on the reversed graph",
    },
]


def _scc(cfg):
    chosen = _chosen(_SC_PRESETS, cfg)
    markup = (
        _toolbar(
            "Two passes, and the acyclic graph of components",
            "the finish order names a source, so the second pass is on the transpose",
            [("cyan", "one component"), ("purple", "another"), ("muted", "an arc between two")],
        )
        + _stage(_svg("scPlot", "0 0 660 300",
                      "The graph with each vertex filled by the component it belongs to.")
                 + _svg("scCond", "0 0 520 240",
                        "The condensation: one node per component, one arc where any arc runs "
                        "between two of them."))
        + _table("scFirst")
        + _table("scSecond")
        + _banner("scStatus")
    )
    controls = (
        _select("scPreset", "Worked example", _options(_SC_PRESETS), chosen["id"])
        + _text("scSpec", "Arcs, as tail&gt;head", chosen["spec"])
        + _select("scPass", "Colour the vertices by",
                  [("comp", "the component each is in"),
                   ("finish", "the finishing order of the first pass")], "comp")
        + _kpis([("Components", "scCount"), ("Largest component", "scBig"),
                 ("Arcs in the condensation", "scArcs"),
                 ("Is the condensation acyclic", "scAcyclic"),
                 ("Agrees with mutual reachability", "scAgree"),
                 ("Where the latest finish landed", "scWhere")])
        + _hint(
            "scHint",
            "Two vertices are in one component when each reaches the other. The first pass only "
            "produces finishing times; the second pass takes vertices in decreasing finishing "
            "order on the <em>reversed</em> graph, and peels one component per start. Read the "
            "condensation table: the component holding the latest finish has nothing pointing "
            "into it, which is the fact the method rests on.",
        )
    )
    script = _BASE_JS + _ONE_GRAPH + _presets_js("SCP", _SC_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('scPreset'), specIn = document.getElementById('scSpec');
  var passIn = document.getElementById('scPass');
  var plot = document.getElementById('scPlot'), cond = document.getElementById('scCond');
  var firstT = document.getElementById('scFirst'), secondT = document.getElementById('scSecond');
  var status = document.getElementById('scStatus');
  var KPIS = ['scCount', 'scBig', 'scArcs', 'scAcyclic', 'scAgree', 'scWhere'];

  function blank(why) {
    plot.innerHTML = ''; cond.innerHTML = ''; firstT.innerHTML = ''; secondT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Direction is the whole subject '
      + 'here: <span class="tt">1&gt;2</span> and <span class="tt">2&gt;1</span> are two arcs.';
  }

  function redraw() {
    var parsed = gkParse(specIn.value, true);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var run = kosaraju(G), res = run.result;
    var times = dfsTimes(G).result;
    var brute = sccBrute(G);
    var agree = samePartition(res.components, brute.components);
    var condG = res.condensation;
    var cidx = dgIndex(condG);

    var colours = new Array(n), v;
    for (v = 0; v < n; v += 1) {
      colours[v] = passIn.value === 'comp' ? res.componentOf[v]
        : (res.order.indexOf(v) % 6);
    }
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                label: 'none', colours: colours });
    var clabels = [];
    for (v = 0; v < condG.n; v += 1) clabels.push(v + 1);
    cond.innerHTML = dgSvg(condG, { points: dgLayout(condG.n, { cx: 260, cy: 120, radius: 88 }),
                                    label: 'none', labels: clabels,
                                    colours: clabels.map(function (_x, i) { return i; }) });

    var frows = '';
    res.order.forEach(function (x, k) {
      frows += '<tr><th class="rowhead">' + (k + 1) + '</th><td class="tone-cyan">' + (x + 1)
        + '</td><td>' + times.d[x] + '</td><td>' + times.f[x] + '</td><td>'
        + (res.componentOf[x] + 1) + '</td></tr>';
    });
    firstT.innerHTML = '<caption>The first pass, in DECREASING finishing order &mdash; which is the '
      + 'order the second pass starts from</caption><thead><tr><th>taken</th><th>vertex</th>'
      + '<th>d</th><th>f</th><th>ends up in component</th></tr></thead><tbody>' + frows
      + '</tbody>';

    var srows = '', biggest = 0;
    res.components.forEach(function (members, k) {
      if (members.length > biggest) biggest = members.length;
      srows += '<tr><th class="rowhead">' + (k + 1) + '</th><td class="tone-cyan">'
        + gkNames(members) + '</td><td>' + members.length + '</td><td>'
        + dgIndeg(condG, k, cidx) + '</td><td>' + dgOutdeg(condG, k, cidx) + '</td><td>'
        + (dgIndeg(condG, k, cidx) === 0 ? 'a source of the condensation'
            : dgOutdeg(condG, k, cidx) === 0 ? 'a sink of the condensation' : 'in the middle')
        + '</td></tr>';
    });
    secondT.innerHTML = '<caption>The second pass, one row per component peeled, with its place '
      + 'in the condensation</caption><thead><tr><th>peeled</th><th>members</th><th>size</th>'
      + '<th>arcs in</th><th>arcs out</th><th>what that makes it</th></tr></thead><tbody>'
      + srows + '</tbody>';

    var latest = res.order[0], home = res.componentOf[latest];
    var homeIndeg = dgIndeg(condG, home, cidx);
    document.getElementById('scCount').textContent = res.components.length;
    document.getElementById('scBig').textContent = biggest + ' vert'
      + gkPlural(biggest, 'ex', 'ices');
    document.getElementById('scArcs').textContent = condG.arcs.length;
    document.getElementById('scAcyclic').textContent = res.condensationAcyclic
      ? 'yes, always' : 'no — report it';
    document.getElementById('scAgree').textContent = agree ? 'yes, same partition' : 'no — report it';
    document.getElementById('scWhere').textContent = 'component ' + (home + 1) + ', with '
      + homeIndeg + ' arc' + gkPlural(homeIndeg, '', 's') + ' into it';

    status.innerHTML = '<strong>' + res.components.length + ' component'
      + gkPlural(res.components.length, '', 's') + '</strong> on ' + n + ' vertices, and the '
      + 'condensation has ' + condG.arcs.length + ' arc' + gkPlural(condG.arcs.length, '', 's')
      + ' and <span class="' + (res.condensationAcyclic ? 'tone-green' : 'tone-red') + '">'
      + (res.condensationAcyclic ? 'no cycle' : 'a cycle, which cannot happen')
      + '</span>. The same partition was computed a second way &mdash; a traversal from every '
      + 'vertex, then keeping the pairs that reach each other, straight from the definition &mdash; '
      + 'and it <span class="' + (agree ? 'tone-green">agrees' : 'tone-red">does not agree')
      + '</span>. The latest finishing vertex is <span class="tone-cyan">' + (latest + 1)
      + '</span> at f = ' + times.f[latest] + ', and it lies in component ' + (home + 1)
      + ', which has <span class="tone-purple">' + homeIndeg + '</span> arc'
      + gkPlural(homeIndeg, '', 's') + ' pointing into it. '
      + (homeIndeg === 0
          ? 'That is the fact the method turns on: decreasing finish order names a SOURCE of the '
            + 'condensation, not a sink. A source’s vertices can reach out of it, so a walk on '
            + 'the original graph from there would run past the component; on the reversed graph '
            + 'those arcs point inwards and the walk stops exactly at the component’s edge.'
          : 'On this graph the latest finish is not in a source component, which cannot happen '
            + 'while the condensation is acyclic — report it.');
  }

  function apply() {
    var p = SCP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = SCP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  passIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Strongly connected components, in two passes",
        subtitle="The finish order names a source component, which is why the second pass runs on the transpose",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the arcs; direction is the whole point"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both passes run in your browser, and the partition they produce is compared with the "
            "one you get straight from the definition &mdash; each vertex reaching each other. The "
            "condensation is built from the components and checked for a cycle.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# cutproperty -- the lemma, checked against every spanning tree there is
# ---------------------------------------------------------------------------

_CP_PRESETS = [
    {
        "id": "distinct",
        "label": "all weights different, so the minimum tree is unique",
        "spec": "1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6",
        "set": "1, 2, 3",
        "note": "one minimum tree, and the lightest crossing edge is in it",
    },
    {
        "id": "tie",
        "label": "two crossing edges of equal weight",
        "spec": "1-2 2, 1-3 2, 2-4 3, 3-4 3, 2-3 5",
        "set": "1",
        "note": "in SOME minimum tree, and not in every one: the two lemmas differ exactly here",
    },
    {
        "id": "pervertex",
        "label": "each vertex's own lightest edge is not a tree",
        "spec": "1-2 1, 2-3 5, 3-4 1, 4-5 6, 5-6 1",
        "set": "1, 2",
        "note": "three lightest-per-vertex edges on six vertices: every one is in the tree and "
                "together they are not one",
    },
    {
        "id": "cycle",
        "label": "a cycle with one heaviest edge",
        "spec": "1-2 1, 2-3 2, 3-4 3, 4-1 9, 2-4 4",
        "set": "1, 2",
        "note": "the heaviest edge on the cycle is in no minimum tree at all, which is the "
                "second lemma",
    },
]

_CP_CAP = 7


def _cutproperty(cfg):
    chosen = _chosen(_CP_PRESETS, cfg)
    markup = (
        _toolbar(
            "A cut, its crossing edges, and every spanning tree",
            "the lemma is read off the list, not quoted",
            [("cyan", "the lightest crossing edge"), ("purple", "another crossing edge"),
             ("muted", "inside one side or the other")],
        )
        + _stage(_svg("cpPlot", "0 0 660 300",
                      "The graph with your chosen set filled, the crossing edges drawn heavy.")
                 + _svg("cpBars", "0 0 660 130",
                        "One bar per spanning tree weight, the minimum ones marked."))
        + _table("cpCross")
        + _table("cpArcs")
        + _banner("cpStatus")
    )
    controls = (
        _select("cpPreset", "Worked example", _options(_CP_PRESETS), chosen["id"])
        + _text("cpSpec", "Edges with weights, as one&minus;other w", chosen["spec"])
        + _text("cpSet", "The set on one side of the cut", chosen["set"])
        + _kpis([("Edges crossing the cut", "cpCount"),
                 ("The lightest of them", "cpLight"),
                 ("Spanning trees in all", "cpTrees"),
                 ("Minimum ones, and their weight", "cpMin"),
                 ("In at least one minimum tree", "cpSome"),
                 ("In every minimum tree", "cpEvery")])
        + _hint(
            "cpHint",
            "An edge is <span class=\"tt\">1&minus;2 4</span>: two labels and a weight. The set is a "
            "list of labels, and the cut is that set against everything else. Every spanning tree "
            "is then enumerated exactly, so “in some minimum tree” is a fact read off a "
            "list. Seven vertices is the limit and it is refused above that rather than run slowly.",
        )
    )
    script = _ORACLE_BASE_JS + _ONE_GRAPH + _presets_js("CPP", _CP_PRESETS, ["spec", "set", "note"]) + r"""
  var presetIn = document.getElementById('cpPreset'), specIn = document.getElementById('cpSpec');
  var setIn = document.getElementById('cpSet');
  var plot = document.getElementById('cpPlot'), bars = document.getElementById('cpBars');
  var crossT = document.getElementById('cpCross'), arcsT = document.getElementById('cpArcs');
  var status = document.getElementById('cpStatus');
  var KPIS = ['cpCount', 'cpLight', 'cpTrees', 'cpMin', 'cpSome', 'cpEvery'];
  var CAP = """ + str(_CP_CAP) + r""";

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; crossT.innerHTML = ''; arcsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2 4</span> and the set is a list like <span class="tt">1, 2</span>.';
  }

  /* Every spanning tree as one bar, sorted by weight: the minimum ones are the
     block on the left, and how many of them there are is the uniqueness
     question answered by a picture as well as by a number. */
  function treeBars(trees, min) {
    var sorted = trees.slice().sort(function (a, b) { return a.weight - b.weight; });
    var top = sorted.length ? sorted[sorted.length - 1].weight : 1;
    var w = Math.max(2, Math.min(14, Math.floor(620 / Math.max(1, sorted.length))));
    var s = '', i;
    for (i = 0; i < sorted.length; i += 1) {
      var h = Math.max(3, (sorted[i].weight / Math.max(1, top)) * 96);
      s += '<rect x="' + (28 + i * w).toFixed(1) + '" y="' + (108 - h).toFixed(1) + '" width="'
        + Math.max(1, w - 1) + '" height="' + h.toFixed(1) + '" fill="var('
        + (sorted[i].weight === min ? '--cyan' : '--line-strong') + ')" opacity="'
        + (sorted[i].weight === min ? '0.95' : '0.45') + '" />';
    }
    s += '<line x1="28" y1="108" x2="648" y2="108" stroke="var(--line-strong)" />';
    s += '<text x="28" y="124" font-size="11" fill="var(--muted)">lightest ' + min + '</text>';
    s += '<text x="648" y="124" text-anchor="end" font-size="11" fill="var(--muted)">heaviest '
      + top + '</text>';
    s += '<text x="28" y="16" font-size="11" fill="var(--cyan)">' + sorted.length
      + ' spanning trees, sorted by weight</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, false);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var chosenSet = gkParseSet(setIn.value, n);
    if (chosenSet.bad) { blank(chosenSet.bad); return; }
    var S = chosenSet.set;
    var v;
    if (!S.length || S.length === n) {
      blank('a cut needs something on each side, and this set has ' + (S.length ? 'everything' : 'nothing') + ' on one');
      return;
    }
    var verdict;
    try { verdict = cutVerdict(G, S, CAP); }
    catch (err) { blank(err.message); return; }
    if (verdict.minWeight === null) {
      blank('this graph has no spanning tree: it is in ' + dgComponents(G).length + ' pieces');
      return;
    }
    var perV = lightestPerVertex(G);
    var inS = new Array(n).fill(false);
    S.forEach(function (x) { inS[x] = true; });

    var colours = new Array(n);
    for (v = 0; v < n; v += 1) colours[v] = inS[v] ? 0 : -1;
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: verdict.crossing.map(function (e) { return e.id; }),
                                label: 'w', colours: colours });
    bars.innerHTML = treeBars(verdict.allTrees, verdict.minWeight);

    var crows = '';
    verdict.crossing.forEach(function (e) {
      var isLight = verdict.lightest && e.id === verdict.lightest.id;
      crows += '<tr' + (isLight ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + gkEdgeName(G.arcs[e.id]) + '</th><td>' + e.w + '</td><td>'
        + (isLight ? 'the lightest across this cut' : 'heavier than the lightest by '
            + (e.w - verdict.lightest.w)) + '</td><td>' + verdict.perArc[e.id] + ' of '
        + verdict.msts + '</td></tr>';
    });
    crossT.innerHTML = '<caption>The edges with one end in your set and one end outside it'
      + '</caption><thead><tr><th>edge</th><th>weight</th><th>place across the cut</th>'
      + '<th>in how many minimum trees</th></tr></thead><tbody>' + crows + '</tbody>';

    var arows = '';
    G.arcs.forEach(function (a, id) {
      var count = verdict.perArc[id], crossing = inS[a.u] !== inS[a.v];
      arows += '<tr' + (count === 0 ? ' class="tone-red"' : '') + '><th class="rowhead">'
        + gkEdgeName(a) + '</th><td>' + a.w + '</td><td>' + (crossing ? 'crosses' : 'does not')
        + '</td><td>' + (perV.arcs.indexOf(id) !== -1 ? 'yes' : 'no') + '</td><td>' + count
        + ' of ' + verdict.msts + '</td><td>'
        + (count === 0 ? 'in no minimum tree at all'
            : count === verdict.msts ? 'in every minimum tree' : 'in some but not all')
        + '</td></tr>';
    });
    arcsT.innerHTML = '<caption>Every edge: whether it crosses, whether it is some vertex’s '
      + 'own lightest, and how many minimum trees hold it</caption><thead><tr><th>edge</th>'
      + '<th>weight</th><th>this cut</th><th>lightest at a vertex</th>'
      + '<th>minimum trees holding it</th><th>verdict</th></tr></thead><tbody>' + arows
      + '</tbody>';

    document.getElementById('cpCount').textContent = verdict.crossing.length
      + (verdict.ties > 1 ? ', ' + verdict.ties + ' tied at the lightest' : '');
    document.getElementById('cpLight').textContent = verdict.lightest
      ? gkEdgeName(G.arcs[verdict.lightest.id]) + ' at ' + verdict.lightest.w : 'none';
    document.getElementById('cpTrees').textContent = verdict.trees + ' of '
      + verdict.examined + ' subsets tried';
    document.getElementById('cpMin').textContent = verdict.msts + ' at weight ' + verdict.minWeight;
    document.getElementById('cpSome').textContent = verdict.inSome ? 'yes' : 'no — report it';
    document.getElementById('cpEvery').textContent = verdict.inEvery
      ? 'yes' : 'no, and it need not be';

    var heaviestNone = [];
    G.arcs.forEach(function (a, id) { if (verdict.perArc[id] === 0) heaviestNone.push(id); });
    status.innerHTML = '<strong>' + verdict.crossing.length + ' edge'
      + gkPlural(verdict.crossing.length, '', 's') + ' cross the cut '
      + '{' + gkNames(S) + '}</strong>, the lightest being <span class="tone-cyan">'
      + gkEdgeName(G.arcs[verdict.lightest.id]) + '</span> at weight ' + verdict.lightest.w + '. '
      + 'All ' + verdict.trees + ' spanning tree' + gkPlural(verdict.trees, '', 's')
      + ' of this graph were then listed, ' + verdict.msts + ' of them at the minimum weight '
      + verdict.minWeight + ', and that edge is in <span class="'
      + (verdict.inSome ? 'tone-green">' + verdict.perArc[verdict.lightest.id] + ' of them'
          : 'tone-red">none of them, which would refute the lemma') + '</span>. '
      + (verdict.inEvery
          ? 'Here it is in every one, because it is strictly lighter than every other crossing '
            + 'edge — which is the stronger statement and the one that fails as soon as there '
            + 'is a tie. '
          : 'It is NOT in every one: ' + verdict.ties + ' crossing edges tie at weight '
            + verdict.lightest.w + ', and the lemma promises only that some minimum tree uses this '
            + 'one. ')
      + (heaviestNone.length
          ? 'The other lemma is on the same table: <span class="tone-red">'
            + heaviestNone.map(function (id) { return gkEdgeName(G.arcs[id]); }).join(', ')
            + '</span> appear in no minimum tree at all, each being the heaviest edge on a cycle. '
          : 'On this graph every edge appears in at least one minimum tree, so the cycle lemma has '
            + 'nothing to exclude here — add a heavy edge between two connected vertices and it '
            + 'will. ')
      + 'Each vertex’s own lightest edge gives ' + perV.arcs.length + ' edge'
      + gkPlural(perV.arcs.length, '', 's') + ' of weight ' + perV.weight + ', leaving the graph '
      + 'in ' + perV.pieces + ' piece' + gkPlural(perV.pieces, '', 's') + ' — '
      + (perV.spans
          ? 'which here happens to be a spanning tree, and that is a fact about this graph.'
          : 'so that set is not a spanning tree, though every edge in it is in one.');
  }

  function apply() {
    var p = CPP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; setIn.value = p.set;
    redraw();
  }
  var START = CPP[presetIn.value];
  if (START) {
    if (!specIn.value) specIn.value = START.spec;
    if (!setIn.value) setIn.value = START.set;
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  setIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The cut and cycle properties, against every spanning tree",
        subtitle="Pick a set; the lightest edge leaving it is in a minimum tree, and the page lists them all to show it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the weighted graph and choose a side"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every spanning tree is enumerated exactly, so the verdict on the lightest crossing "
            "edge is read off the list rather than taken from the lemma. The count of minimum "
            "trees is the answer to whether the tree is unique.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# prim -- one tree, one heap, and the cut property applied at every step
# ---------------------------------------------------------------------------

_PM_PRESETS = [
    {
        "id": "classic",
        "label": "seven vertices, all weights different",
        "spec": "1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, 5-7 8, 6-7 2",
        "start": "1",
        "note": "distinct weights, so the minimum tree is unique and both algorithms find it",
    },
    {
        "id": "lazy",
        "label": "a graph that fills the heap with stale entries",
        "spec": "1-2 1, 1-3 1, 1-4 1, 2-3 9, 2-4 9, 3-4 9, 1-5 2, 2-5 3, 3-5 4",
        "start": "1",
        "note": "every heavy edge is pushed and then popped with both ends already in the tree",
    },
    {
        "id": "tie",
        "label": "ties, so the tree is one of several",
        "spec": "1-2 2, 1-3 2, 2-3 2, 3-4 1",
        "start": "1",
        "note": "with equal weights the two algorithms may pick different edges of the same weight",
    },
    {
        "id": "star",
        "label": "a star, where the heap never holds more than a layer",
        "spec": "1-2 5, 1-3 4, 1-4 3, 1-5 2, 1-6 1",
        "start": "1",
        "note": "every candidate is on the boundary at once and the heap empties in one sweep",
    },
]


def _prim(cfg):
    chosen = _chosen(_PM_PRESETS, cfg)
    markup = (
        _toolbar(
            "Grow one tree, always across its own boundary",
            "the heap holds the candidates, and the stale ones are skipped on the way out",
            [("cyan", "in the tree so far"), ("purple", "waiting in the heap"),
             ("red", "popped with both ends already in")],
        )
        + _stage(_svg("pmPlot", "0 0 660 300",
                      "The graph, with the edges the tree has taken up to this step drawn heavy.")
                 + _svg("pmHeap", "0 0 660 120",
                        "The heap's keys at this step, in array order, with the root on the left."))
        + _table("pmSteps")
        + _table("pmCompare")
        + _banner("pmStatus")
    )
    controls = (
        _select("pmPreset", "Worked example", _options(_PM_PRESETS), chosen["id"])
        + _text("pmSpec", "Edges with weights, as one&minus;other w", chosen["spec"])
        + _range("pmStart", "Grow the tree from", 1, 12, chosen["start"])
        + _range("pmStep", "Step", 1, 40, 40)
        + _kpis([("Weight of the tree", "pmWeight"),
                 ("Edges in it", "pmEdges"),
                 ("Heap pushes and pops", "pmOps"),
                 ("Key comparisons in the heap", "pmCmp"),
                 ("E times log2 V, for reference", "pmBound"),
                 ("Same weight as the sorted method", "pmAgree")])
        + _hint(
            "pmHint",
            "The heap holds candidate <em>edges</em>, not vertices, and a better edge to a vertex "
            "is pushed as a second entry rather than found and lowered &mdash; so a pop can come "
            "back with an edge whose two ends are both in the tree already, and it is discarded. "
            "That is lazy deletion, and the operation counts beside "
            "<span class=\"tt\">E log V</span> are what it costs.",
        )
    )
    script = _LOG_JS + _ONE_GRAPH + _presets_js("PMP", _PM_PRESETS, ["spec", "start", "note"]) + r"""
  var presetIn = document.getElementById('pmPreset'), specIn = document.getElementById('pmSpec');
  var startIn = document.getElementById('pmStart'), startOut = document.getElementById('pmStartOut');
  var stepIn = document.getElementById('pmStep'), stepOut = document.getElementById('pmStepOut');
  var plot = document.getElementById('pmPlot'), heapPlot = document.getElementById('pmHeap');
  var stepsT = document.getElementById('pmSteps'), cmpT = document.getElementById('pmCompare');
  var status = document.getElementById('pmStatus');
  var KPIS = ['pmWeight', 'pmEdges', 'pmOps', 'pmCmp', 'pmBound', 'pmAgree'];

  function blank(why) {
    plot.innerHTML = ''; heapPlot.innerHTML = ''; stepsT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2 4</span>: two labels and a weight.';
  }

  /* The heap as its ARRAY, root first, because the array is the structure: a
     drawing of a triangle of circles would hide that a push walks up from the
     end and a pop swaps the end into the front. */
  function heapCells(keys) {
    if (!keys || !keys.length) {
      return '<text x="28" y="60" font-size="12" fill="var(--muted)">the heap is empty</text>';
    }
    var w = Math.max(18, Math.min(46, Math.floor(600 / keys.length))), s = '', i;
    for (i = 0; i < keys.length; i += 1) {
      var x = 28 + i * w;
      s += '<rect x="' + x + '" y="34" width="' + (w - 4) + '" height="42" rx="4" fill="var(--purple)" '
        + 'opacity="' + (i === 0 ? '0.9' : '0.22') + '" stroke="var(--purple)" />';
      s += '<text x="' + (x + (w - 4) / 2) + '" y="60" text-anchor="middle" font-size="13" '
        + 'font-weight="700" fill="var(--' + (i === 0 ? 'on-accent' : 'text') + ')">' + keys[i]
        + '</text>';
      s += '<text x="' + (x + (w - 4) / 2) + '" y="90" text-anchor="middle" font-size="9" '
        + 'fill="var(--muted)">' + i + '</text>';
    }
    s += '<text x="28" y="22" font-size="11" fill="var(--purple)">' + keys.length
      + ' entr' + gkPlural(keys.length, 'y', 'ies') + ' in the heap; the root is the next pop</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, false);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    startIn.max = n;
    var start = gkStep(parseInt(startIn.value, 10) - 1, n);
    startOut.textContent = String(start + 1);

    var run = primRun(G, start), res = run.result;
    var trace = run.trace;
    stepIn.max = Math.max(1, trace.length);
    var k = gkStep(parseInt(stepIn.value, 10) - 1, trace.length);
    stepOut.textContent = trace.length ? (k + 1) + ' of ' + trace.length : 'nothing to step';

    var takenSoFar = [], lastHeap = null, inTree = new Array(n).fill(false);
    inTree[start] = true;
    trace.forEach(function (st, i) {
      if (i > k) return;
      if (st.taken) { takenSoFar.push(st.arc); inTree[st.added] = true; }
      if (st.heap) lastHeap = st.heap;
    });

    var colours = new Array(n);
    for (var v = 0; v < n; v += 1) colours[v] = inTree[v] ? 0 : -1;
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: takenSoFar, label: 'w', colours: colours });
    heapPlot.innerHTML = heapCells(lastHeap);

    var rows = '';
    trace.forEach(function (st, i) {
      var a = G.arcs[st.arc];
      rows += '<tr class="' + (i === k ? 'tone-cyan' : (st.taken ? '' : 'tone-red')) + '">'
        + '<th class="rowhead">' + (i + 1) + '</th><td>' + gkEdgeName(a) + '</td><td>' + st.w
        + '</td><td>' + (st.taken ? 'taken, bringing in ' + (st.added + 1) : 'discarded')
        + '</td><td>' + (st.taken
            ? 'the lightest edge across the tree’s own boundary, which the cut property puts '
              + 'in a minimum tree'
            : st.reason) + '</td><td>'
        + (st.heap ? st.heap.join(' ') : 'unchanged') + '</td></tr>';
    });
    stepsT.innerHTML = '<caption>Every pop, in order: what came out of the heap and what happened '
      + 'to it</caption><thead><tr><th>pop</th><th>edge</th><th>weight</th><th>outcome</th>'
      + '<th>why</th><th>heap keys after</th></tr></thead><tbody>' + rows + '</tbody>';

    /* The independent answer: the same graph run through the sorted, union-find
       method, which never builds a heap and never grows one tree. */
    var kr = kruskalRun(G);
    var same = kr.result.weight === res.weight;
    var sameSet = kr.result.arcs.slice().sort(function (a, b) { return a - b; }).join(',')
      === res.arcs.slice().sort(function (a, b) { return a - b; }).join(',');
    cmpT.innerHTML = '<caption>The same graph, two schedules for the same two lemmas</caption>'
      + '<thead><tr><th>method</th><th>weight</th><th>edges</th><th>what it counted</th>'
      + '</tr></thead><tbody>'
      + '<tr><th class="rowhead">growing one tree with a heap</th><td class="tone-cyan">'
      + res.weight + '</td><td>' + res.arcs.map(function (id) { return gkEdgeName(G.arcs[id]); })
        .join(', ') + '</td><td>' + (run.counts.pushes || 0) + ' pushes, '
      + (run.counts.pops || 0) + ' pops, ' + (run.counts.compares || 0) + ' comparisons</td></tr>'
      + '<tr><th class="rowhead">sorting the edges and asking a find</th><td class="tone-cyan">'
      + kr.result.weight + '</td><td>' + kr.result.arcs.map(function (id) { return gkEdgeName(G.arcs[id]); })
        .join(', ') + '</td><td>' + (kr.counts.finds || 0) + ' finds, '
      + (kr.counts.unions || 0) + ' unions</td></tr></tbody>';

    document.getElementById('pmWeight').textContent = res.weight
      + (res.spanning ? '' : ' — not spanning');
    document.getElementById('pmEdges').textContent = res.arcs.length + ' of ' + (n - 1);
    document.getElementById('pmOps').textContent = (run.counts.pushes || 0) + ' and '
      + (run.counts.pops || 0);
    document.getElementById('pmCmp').textContent = run.counts.compares || 0;
    document.getElementById('pmBound').textContent = res.bound;
    document.getElementById('pmAgree').textContent = same
      ? (sameSet ? 'same weight, same edges' : 'same weight, different edges') : 'no — report it';

    var stale = trace.filter(function (st) { return !st.taken; }).length;
    status.innerHTML = '<strong>Weight ' + res.weight + '</strong> on ' + res.arcs.length
      + ' edge' + gkPlural(res.arcs.length, '', 's') + ', from ' + (run.counts.pops || 0)
      + ' pops of which <span class="tone-red">' + stale + '</span> came back with both ends '
      + 'already in the tree and were discarded. '
      + 'The heap cost <span class="tone-purple">' + (run.counts.compares || 0)
      + '</span> key comparisons, against <span class="tone-amber">' + res.bound
      + '</span> for E log' + '₂' + ' V on this graph &mdash; and those two numbers are not the '
      + 'same kind of thing: the first is a measurement on one graph and the second is a bound on '
      + 'all of them, drawn here so the shape can be seen rather than the constant. '
      + (same
          ? (sameSet
              ? 'Sorting the edges and asking a find instead produced <span class="tone-green">the '
                + 'same tree</span>, edge for edge: with these weights the minimum tree is unique '
                + 'and a schedule cannot change it.'
              : 'Sorting the edges instead produced a <span class="tone-amber">different set of '
                + 'edges at the same weight ' + res.weight + '</span>. Both are minimum trees; the '
                + 'weights tie, so the tree is not unique and the two schedules broke the tie '
                + 'differently.')
          : '<span class="tone-red">The two methods disagree on the weight, which cannot happen '
            + 'on a connected graph.</span>');
  }

  function apply() {
    var p = PMP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; startIn.value = p.start; stepIn.value = stepIn.max;
    redraw();
  }
  var START = PMP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; startIn.value = START.start; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  startIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Prim's algorithm, with the heap on screen",
        subtitle="Lazy deletion instead of decrease-key, so a pop can bring back an edge with nowhere to go",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the graph and step the heap"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every pop is a row: what came out, whether it was used, and the heap's keys "
            "afterwards. The same graph is run through the sorted, union-find method as well, so "
            "the two answers sit side by side.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# kruskal -- sorted edges, and a find for every cycle question
# ---------------------------------------------------------------------------

_KR_PRESETS = [
    {
        "id": "classic",
        "label": "seven vertices, all weights different",
        "spec": "1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, 5-7 8, 6-7 2",
        "note": "three edges rejected, each by a find that returned the same root twice",
    },
    {
        "id": "chain",
        "label": "unions in a line, so a find walks far",
        "spec": "1-2 1, 2-3 2, 3-4 3, 4-5 4, 5-6 5, 1-6 9",
        "note": "no rank rule and no compression here, so the last find walks the whole chain",
    },
    {
        "id": "manycycles",
        "label": "a complete graph on five, so most edges are rejected",
        "spec": "1-2 1, 1-3 2, 1-4 3, 1-5 4, 2-3 5, 2-4 6, 2-5 7, 3-4 8, 3-5 9, 4-5 1",
        "note": "ten edges, four taken: every rejection is the cycle property and not the algorithm",
    },
    {
        "id": "forest",
        "label": "a graph in two pieces",
        "spec": "1-2 1, 2-3 2, 4-5 3, 5-6 4",
        "note": "it never spans, and the panel says so rather than reporting a tree",
    },
]


def _kruskal(cfg):
    chosen = _chosen(_KR_PRESETS, cfg)
    markup = (
        _toolbar(
            "Sorted edges, and one find per cycle question",
            "each rejection is justified by the cycle property, not by the algorithm",
            [("cyan", "taken into the forest"), ("red", "rejected: both ends already joined"),
             ("purple", "a parent pointer in the union-find forest")],
        )
        + _stage(_svg("krPlot", "0 0 660 300",
                      "The graph, with the edges taken so far drawn heavy.")
                 + _svg("krSets", "0 0 520 240",
                        "The union-find forest at this step: each vertex drawn with an arrow to "
                        "its parent."))
        + _table("krSteps")
        + _table("krCheck")
        + _banner("krStatus")
    )
    controls = (
        _select("krPreset", "Worked example", _options(_KR_PRESETS), chosen["id"])
        + _text("krSpec", "Edges with weights, as one&minus;other w", chosen["spec"])
        + _range("krStep", "Step", 1, 40, 40)
        + _kpis([("Weight of the forest", "krWeight"),
                 ("Edges taken, and needed", "krEdges"),
                 ("Finds and unions", "krOps"),
                 ("Pointer hops inside the finds", "krHops"),
                 ("Edges rejected", "krReject"),
                 ("Agrees with the by-hand baseline", "krAgree")])
        + _hint(
            "krHint",
            "The edges are sorted once, and then the only question per edge is whether its two ends "
            "are already in the same set &mdash; which is two finds, not a traversal. A rejected "
            "edge is the heaviest on the cycle it would close, so the cycle property says no "
            "minimum tree wants it; the forest below is the state those finds walk.",
        )
    )
    script = _CHECKED_JS + _ONE_GRAPH + _presets_js("KRP", _KR_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('krPreset'), specIn = document.getElementById('krSpec');
  var stepIn = document.getElementById('krStep'), stepOut = document.getElementById('krStepOut');
  var plot = document.getElementById('krPlot'), sets = document.getElementById('krSets');
  var stepsT = document.getElementById('krSteps'), checkT = document.getElementById('krCheck');
  var status = document.getElementById('krStatus');
  var KPIS = ['krWeight', 'krEdges', 'krOps', 'krHops', 'krReject', 'krAgree'];

  function blank(why) {
    plot.innerHTML = ''; sets.innerHTML = ''; stepsT.innerHTML = ''; checkT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2 4</span>: two labels and a weight.';
  }

  /* The union-find state is a FOREST, so it is drawn with the graph renderer:
     one arc from each vertex to its parent. Reusing the drawing rather than
     writing a second one is the point -- a parent array is a digraph. */
  function forestOf(parent, n) {
    var F = dgNew(n, true), v;
    for (v = 0; v < n; v += 1) if (parent[v] !== v) dgAdd(F, v, parent[v], 1, 0);
    return F;
  }
  function rootOf(parent, x) {
    var guard = 0;
    while (parent[x] !== x && guard <= parent.length) { x = parent[x]; guard += 1; }
    return x;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, false);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var run = kruskalRun(G), res = run.result, trace = run.trace;
    stepIn.max = Math.max(1, trace.length);
    var k = gkStep(parseInt(stepIn.value, 10) - 1, trace.length);
    stepOut.textContent = trace.length ? (k + 1) + ' of ' + trace.length : 'nothing to step';

    var takenSoFar = [], parent = [], i, v;
    for (v = 0; v < n; v += 1) parent.push(v);
    trace.forEach(function (st, idx) {
      if (idx > k) return;
      if (st.taken) takenSoFar.push(st.arc);
      parent = st.parent.slice();
    });
    var roots = {}, pieces = 0;
    for (v = 0; v < n; v += 1) { var r = rootOf(parent, v); if (!roots[r]) { roots[r] = true; pieces += 1; } }
    var colour = {}, next = 0;
    for (v = 0; v < n; v += 1) {
      var rr = rootOf(parent, v);
      if (colour[rr] === undefined) { colour[rr] = next; next += 1; }
    }
    var colours = [];
    for (v = 0; v < n; v += 1) colours.push(colour[rootOf(parent, v)]);

    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: takenSoFar, label: 'w', colours: colours });
    var F = forestOf(parent, n);
    sets.innerHTML = F.arcs.length
      ? dgSvg(F, { points: dgLayout(n, { cx: 260, cy: 120, radius: 92 }), label: 'none',
                   colours: colours })
      : '<text x="24" y="120" font-size="12" fill="var(--muted)">every vertex is still its own '
        + 'root: no union has happened yet</text>';

    var rows = '';
    trace.forEach(function (st, idx) {
      var a = G.arcs[st.arc];
      var before = idx === 0 ? null : trace[idx - 1].parent;
      rows += '<tr class="' + (idx === k ? 'tone-cyan' : (st.taken ? '' : 'tone-red')) + '">'
        + '<th class="rowhead">' + (idx + 1) + '</th><td>' + gkEdgeName(a) + '</td><td>' + st.w
        + '</td><td>' + (before === null ? (a.u + 1) + ' and ' + (a.v + 1) + ' are their own roots'
            : 'find(' + (a.u + 1) + ') = ' + (rootOf(before, a.u) + 1) + ', find(' + (a.v + 1)
              + ') = ' + (rootOf(before, a.v) + 1)) + '</td><td>'
        + (st.taken ? 'taken' : 'rejected') + '</td><td>'
        + (st.taken
            ? 'two different sets, so this edge joins them and closes no cycle'
            : st.reason + ', so it is the heaviest edge on the cycle it would close')
        + '</td></tr>';
    });
    stepsT.innerHTML = '<caption>Every edge in sorted order, with the two finds that decided it'
      + '</caption><thead><tr><th>step</th><th>edge</th><th>weight</th><th>the finds</th>'
      + '<th>outcome</th><th>why</th></tr></thead><tbody>' + rows + '</tbody>';

    /* THE ORACLE. graph.py's kruskal() sorts the same edges and uses a find
       with path halving, written for another course; it has never heard of this
       one. Where a matrix cannot hold the graph the panel says so. */
    var ready = gkOracleReady(G), theirs = null, agree = null;
    if (ready.ok) {
      N = n; A = dgToMatrix(G);
      LESSON = lessonFrom(gkLessonList(G)); useLessonWeights = true;
      theirs = kruskal();
      agree = theirs.total === res.weight;
    }
    checkT.innerHTML = '<caption>The same edges, sorted and unioned by a different '
      + 'implementation</caption><thead><tr><th>where it came from</th><th>weight</th>'
      + '<th>edges taken</th></tr></thead><tbody>'
      + '<tr><th class="rowhead">this page</th><td class="tone-cyan">' + res.weight + '</td><td>'
      + res.arcs.map(function (id) { return gkEdgeName(G.arcs[id]); }).join(', ') + '</td></tr>'
      + (ready.ok
          ? '<tr><th class="rowhead">the by-hand baseline</th><td class="tone-cyan">' + theirs.total
            + '</td><td>' + theirs.chosen.map(function (e) {
                return (e[0] + 1) + '–' + (e[1] + 1); }).join(', ') + '</td></tr>'
          : '<tr><th class="rowhead">the by-hand baseline</th><td class="tone-amber">cannot be '
            + 'asked</td><td>' + ready.why + '</td></tr>')
      + '</tbody>';

    var rejected = trace.filter(function (st) { return !st.taken; }).length;
    document.getElementById('krWeight').textContent = res.weight
      + (res.spanning ? '' : ' — a forest, not a tree');
    document.getElementById('krEdges').textContent = res.arcs.length + ' of ' + (n - 1);
    document.getElementById('krOps').textContent = (run.counts.finds || 0) + ' and '
      + (run.counts.unions || 0);
    document.getElementById('krHops').textContent = run.counts.hops || 0;
    document.getElementById('krReject').textContent = rejected + ' of ' + G.arcs.length;
    document.getElementById('krAgree').textContent = ready.ok
      ? (agree ? 'yes, same weight' : 'no — report it') : 'cannot be asked';

    status.innerHTML = '<strong>' + res.arcs.length + ' edge'
      + gkPlural(res.arcs.length, '', 's') + ' at weight ' + res.weight + '</strong> from '
      + G.arcs.length + ' considered in sorted order, with <span class="tone-red">' + rejected
      + '</span> rejected. '
      + (res.spanning
          ? ''
          : '<span class="tone-amber">It never spans: the graph is in ' + dgComponents(G).length
            + ' pieces, so ' + (n - 1) + ' edges cannot be found and what came out is a minimum '
            + 'spanning FOREST.</span> ')
      + 'The cycle questions cost <span class="tone-purple">' + (run.counts.finds || 0)
      + '</span> finds and <span class="tone-purple">' + (run.counts.hops || 0)
      + '</span> pointer hops inside them &mdash; no traversal of the graph at all, which is the '
      + 'whole reason the sort dominates the cost. '
      + (ready.ok
          ? (agree
              ? 'A different implementation of the same idea, written for another course and '
                + 'reused here as it ships, returned <span class="tone-green">the same weight</span> '
                + 'on the same edges.'
              : '<span class="tone-red">The baseline disagrees, which means one of the two is '
                + 'wrong.</span>')
          : '<span class="tone-amber">The baseline cannot be asked about this graph: ' + ready.why
            + '.</span>');
  }

  function apply() {
    var p = KRP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; stepIn.value = stepIn.max;
    redraw();
  }
  var START = KRP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Kruskal's algorithm, with the union-find state visible",
        subtitle="Every rejection is the cycle property, and the cost is the sort plus two finds an edge",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the graph and step the sorted edges"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each row is one edge in sorted order, the two finds it made, and the reason it was "
            "taken or rejected. The forest beside the graph is the union-find state those finds "
            "walk, and the pointer hops are counted.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# relax -- one step, three schedules, one answer
# ---------------------------------------------------------------------------

_RX_PRESETS = [
    {
        "id": "classic",
        "label": "six vertices, weights all different",
        "spec": "1-2 7, 1-3 9, 1-6 14, 2-3 10, 2-4 15, 3-4 11, 3-6 2, 4-5 6, 5-6 9",
        "source": "1",
        "note": "the schedule changes how much work happens and not one distance",
    },
    {
        "id": "stale",
        "label": "a graph that fills the heap with stale entries",
        "spec": "1-2 10, 1-3 9, 3-2 1, 3-4 8, 2-4 1, 1-4 30",
        "source": "1",
        "note": "2 is pushed twice and the first entry is skipped when it comes out",
    },
    {
        "id": "far",
        "label": "a long chain, so the frontier is always one vertex",
        "spec": "1-2 1, 2-3 1, 3-4 1, 4-5 1, 5-6 1, 6-7 1",
        "source": "1",
        "note": "every schedule does the same thing here, which is what makes the dense case "
                "interesting instead",
    },
    {
        "id": "dense",
        "label": "a complete graph on five, where scanning is the cheaper order",
        "spec": "1-2 3, 1-3 8, 1-4 2, 1-5 9, 2-3 4, 2-4 6, 2-5 5, 3-4 7, 3-5 1, 4-5 4",
        "source": "1",
        "note": "ten edges on five vertices: the heap pays for structure the scan does without",
    },
]


def _relax(cfg):
    chosen = _chosen(_RX_PRESETS, cfg)
    markup = (
        _toolbar(
            "One relaxation step under three schedules",
            "the answer is the same; the work is not",
            [("cyan", "settled"), ("purple", "reached but not settled"),
             ("muted", "no label yet")],
        )
        + _stage(_svg("rxPlot", "0 0 660 300",
                      "The graph, with the tree of shortest paths found so far drawn heavy.")
                 + _svg("rxBars", "0 0 660 140",
                        "One bar per vertex for its label at this step, so an improvement is a "
                        "bar getting shorter."))
        + _table("rxSteps")
        + _table("rxFinal")
        + _banner("rxStatus")
    )
    controls = (
        _select("rxPreset", "Worked example", _options(_RX_PRESETS), chosen["id"])
        + _text("rxSpec", "Edges with weights, as one&minus;other w", chosen["spec"])
        + _range("rxSource", "Shortest paths from", 1, 12, chosen["source"])
        + _select("rxSched", "Relaxation schedule",
                  [("heap", "nearest unsettled first, from a heap"),
                   ("scan", "nearest unsettled first, by scanning every vertex"),
                   ("insertion", "every edge, in the order you typed, over and over")], "heap")
        + _range("rxStep", "Step", 1, 60, 60)
        + _kpis([("Relaxations performed", "rxRelax"),
                 ("Heap pushes and pops", "rxOps"),
                 ("E times log2 V, for reference", "rxBound"),
                 ("The upper-bound invariant", "rxInv"),
                 ("Labels equal to the true distances", "rxExact"),
                 ("Agrees with the by-hand baseline", "rxAgree")])
        + _hint(
            "rxHint",
            "The step is always the same: if <span class=\"tt\">d[u] + w</span> beats "
            "<span class=\"tt\">d[v]</span>, write it down. What changes is the order the step is "
            "applied in. <span class=\"tt\">d[v]</span> is never below the true distance under any "
            "of the three &mdash; that is checked after every step against an answer computed a "
            "different way &mdash; and the counts show what each order costs.",
        )
    )
    script = _HEAP_JS + _ONE_GRAPH + _presets_js("RXP", _RX_PRESETS, ["spec", "source", "note"]) + r"""
  var presetIn = document.getElementById('rxPreset'), specIn = document.getElementById('rxSpec');
  var srcIn = document.getElementById('rxSource'), srcOut = document.getElementById('rxSourceOut');
  var schedIn = document.getElementById('rxSched');
  var stepIn = document.getElementById('rxStep'), stepOut = document.getElementById('rxStepOut');
  var plot = document.getElementById('rxPlot'), bars = document.getElementById('rxBars');
  var stepsT = document.getElementById('rxSteps'), finalT = document.getElementById('rxFinal');
  var status = document.getElementById('rxStatus');
  var KPIS = ['rxRelax', 'rxOps', 'rxBound', 'rxInv', 'rxExact', 'rxAgree'];

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; stepsT.innerHTML = ''; finalT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2 7</span>: two labels and a weight.';
  }

  /* One bar per vertex for its current label. An unreached vertex is an OUTLINE
     rather than a zero-height bar: null is not a small distance. */
  function labelBars(dist, n, truth) {
    var top = 1, v;
    for (v = 0; v < n; v += 1) if (dist[v] !== null && dist[v] > top) top = dist[v];
    for (v = 0; v < n; v += 1) if (truth[v] !== null && truth[v] > top) top = truth[v];
    var w = Math.max(20, Math.min(60, Math.floor(600 / n))), s = '';
    for (v = 0; v < n; v += 1) {
      var x = 28 + v * w, d = dist[v];
      if (d === null) {
        s += '<rect x="' + x + '" y="24" width="' + (w - 6) + '" height="88" rx="4" fill="none" '
          + 'stroke="var(--line-strong)" stroke-dasharray="4 4" />';
        s += '<text x="' + (x + (w - 6) / 2) + '" y="74" text-anchor="middle" font-size="10" '
          + 'fill="var(--muted)">none</text>';
      } else {
        var h = Math.max(3, (Math.abs(d) / top) * 88);
        s += '<rect x="' + x + '" y="' + (112 - h).toFixed(1) + '" width="' + (w - 6) + '" height="'
          + h.toFixed(1) + '" rx="4" fill="var(--cyan)" opacity="0.8" />';
        s += '<text x="' + (x + (w - 6) / 2) + '" y="' + Math.max(20, 106 - h).toFixed(1)
          + '" text-anchor="middle" font-size="11" font-weight="700" fill="var(--text)">' + d
          + '</text>';
      }
      s += '<text x="' + (x + (w - 6) / 2) + '" y="128" text-anchor="middle" font-size="10" '
        + 'fill="var(--muted)">' + (v + 1) + '</text>';
    }
    s += '<line x1="28" y1="112" x2="648" y2="112" stroke="var(--line-strong)" />';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, false);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    srcIn.max = n;
    var source = gkStep(parseInt(srcIn.value, 10) - 1, n);
    srcOut.textContent = String(source + 1);
    var sched = schedIn.value;

    var run = relaxRun(G, source, sched), res = run.result, trace = run.trace;
    var inv = relaxInvariant(G, source, run);
    stepIn.max = Math.max(1, trace.length);
    var k = gkStep(parseInt(stepIn.value, 10) - 1, trace.length);
    stepOut.textContent = trace.length ? (k + 1) + ' of ' + trace.length : 'nothing to step';

    var atStep = trace.length ? trace[k].dist : res.dist;
    var settled = {}, v;
    trace.forEach(function (st, i) { if (i <= k && st.settled !== undefined) settled[st.settled] = true; });

    var treeArcs = [];
    for (v = 0; v < n; v += 1) {
      if (res.parent[v] === -1) continue;
      var id = dgFind(G, res.parent[v], v);
      if (id !== -1) treeArcs.push(id);
    }
    var colours = new Array(n);
    for (v = 0; v < n; v += 1) {
      colours[v] = settled[v] ? 0 : (atStep[v] !== null ? 1 : -1);
    }
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: treeArcs, label: 'w', colours: colours });
    bars.innerHTML = labelBars(atStep, n, inv.truth);

    var rows = '';
    trace.forEach(function (st, i) {
      var what = st.settled !== undefined
        ? 'settled ' + (st.settled + 1) + ' at d = ' + gkDistText(st.d)
        : 'relaxed ' + gkEdgeName(G.arcs[st.arc]) + ', improving ' + (st.to + 1);
      rows += '<tr class="' + (i === k ? 'tone-cyan' : '') + '"><th class="rowhead">' + (i + 1)
        + '</th><td>' + (st.round === undefined ? '—' : st.round) + '</td><td>' + what
        + '</td><td>' + st.dist.map(function (d, x) {
            return (x + 1) + ':' + (d === null ? '—' : d); }).join('  ') + '</td></tr>';
    });
    stepsT.innerHTML = '<caption>Every step of this schedule, with d[] after it</caption>'
      + '<thead><tr><th>step</th><th>round</th><th>what happened</th><th>d[] afterwards</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    /* THE ORACLE. graph.py's dijkstra() settles by a linear scan and returns
       Infinity where this one returns null; it was written for another course.
       It is only asked where it can answer: its weights come from the
       unordered pair, and negative weights break the schedule it implements. */
    var ready = gkOracleReady(G), theirs = null, agree = null;
    if (ready.ok && !res.negativeWeights) {
      N = n; A = dgToMatrix(G);
      LESSON = lessonFrom(gkLessonList(G)); useLessonWeights = true;
      theirs = dijkstra(source);
      agree = gkSameDistances(res.dist, theirs.dist);
    }

    var frows = '';
    for (v = 0; v < n; v += 1) {
      frows += '<tr' + (inv.wrong.indexOf(v) !== -1 ? ' class="tone-red"' : '')
        + '><th class="rowhead">' + (v + 1) + '</th><td>' + gkDistText(res.dist[v]) + '</td><td>'
        + gkDistText(inv.truth[v]) + '</td><td>'
        + (theirs ? (theirs.dist[v] === Infinity ? 'not reached' : String(theirs.dist[v]))
            : 'not asked') + '</td><td>' + gkPathText(gkPathTo(res.parent, source, v))
        + '</td><td>' + (inv.wrong.indexOf(v) !== -1
            ? 'this schedule left it above the true distance'
            : 'agrees with the true distance') + '</td></tr>';
    }
    finalT.innerHTML = '<caption>Each vertex: this schedule’s label, the true distance from a '
      + 'different algorithm, the by-hand baseline, and the path</caption><thead><tr>'
      + '<th>vertex</th><th>label</th><th>true distance</th><th>baseline</th><th>path</th>'
      + '<th>verdict</th></tr></thead><tbody>' + frows + '</tbody>';

    document.getElementById('rxRelax').textContent = run.counts.relaxations || 0;
    document.getElementById('rxOps').textContent = sched === 'heap'
      ? (run.counts.pushes || 0) + ' and ' + (run.counts.pops || 0)
      : 'no heap in this schedule';
    document.getElementById('rxBound').textContent = gkHeapBound(G);
    document.getElementById('rxInv').textContent = inv.holds
      ? 'never violated' : inv.violations.length + ' violations — report it';
    document.getElementById('rxExact').textContent = inv.exact
      ? 'all ' + n : (n - inv.wrong.length) + ' of ' + n;
    document.getElementById('rxAgree').textContent = theirs
      ? (agree ? 'yes, every distance' : 'no — report it')
      : (res.negativeWeights ? 'not asked: a weight is negative' : 'cannot be asked');

    var schedName = sched === 'heap' ? 'nearest unsettled first, from a heap'
      : sched === 'scan' ? 'nearest unsettled first, by scanning' : 'every edge in order, repeatedly';
    status.innerHTML = '<strong>' + (run.counts.relaxations || 0) + ' relaxation'
      + gkPlural(run.counts.relaxations || 0, '', 's') + '</strong> under <em>' + schedName
      + '</em>, against <span class="tone-amber">' + gkHeapBound(G) + '</span> for E log'
      + '₂ V on this graph. The invariant d[v] &ge; the true distance was tested after every '
      + 'one of the ' + trace.length + ' steps against labels from a different algorithm, and it '
      + 'was <span class="' + (inv.holds ? 'tone-green">never violated' : 'tone-red">violated '
          + inv.violations.length + ' times, which cannot happen') + '</span>. '
      + (res.negativeWeights
          ? '<span class="tone-red">This graph has a negative weight, and these edges point both '
            + 'ways.</span> An edge of negative weight that can be walked in either direction IS a '
            + 'negative cycle: go along it and back, and the total falls by twice its weight, so '
            + 'there is no shortest walk for a label to converge to and nothing on this page is a '
            + 'distance. Negative weights want arcs that point one way, and rounds rather than a '
            + 'settled set. '
          : (theirs
              ? (agree
                  ? 'The same graph was handed to a Dijkstra written for another course, which '
                    + 'settles by scanning every vertex rather than by a heap, and it returned '
                    + '<span class="tone-green">the same distances</span>. '
                  : '<span class="tone-red">The baseline disagrees on some distance.</span> ')
              : '<span class="tone-amber">The baseline cannot be asked: ' + ready.why + '.</span> '))
      + (sched === 'heap'
          ? 'A better route to a vertex is pushed as a second entry rather than lowered in place, '
            + 'so ' + (run.counts.pushes || 0) + ' pushes answered ' + (run.counts.pops || 0)
            + ' pops and the stale ones were skipped on the way out.'
          : sched === 'scan'
            ? 'With no heap at all the scan cost ' + (run.counts.reads || 0) + ' reads to find the '
              + 'nearest unsettled vertex, which is the dense-graph trade: fewer structures, more '
              + 'looking.'
            : 'Relaxing every edge in the order typed took ' + res.rounds + ' round'
              + gkPlural(res.rounds, '', 's') + ' to stop changing anything, and reached the same '
              + 'labels by doing more work in a simpler order.');
  }

  function apply() {
    var p = RXP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; srcIn.value = p.source; stepIn.value = stepIn.max;
    redraw();
  }
  var START = RXP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; srcIn.value = START.source; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  schedIn.addEventListener('change', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Relaxation, and Dijkstra as one schedule for it",
        subtitle="Three orders for the same step; the labels never drop below the true distance and the page checks it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the graph, choose the schedule"),
        panel_intro=cfg.get(
            "panel_intro",
            "The relaxation step is one line of arithmetic. Each schedule applies it in a "
            "different order, and after every step the labels are checked against distances "
            "computed by a different algorithm entirely.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# bellmanford -- rounds, and the round each label stopped moving
# ---------------------------------------------------------------------------

_BF_PRESETS = [
    {
        "id": "negative",
        "label": "negative arcs, and no negative cycle",
        "spec": "1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, 4>2 -2, 5>1 2, 5>4 7",
        "source": "1",
        "note": "four negative arcs and every shortest path still exists, which is the point",
    },
    {
        "id": "negcycle",
        "label": "a negative cycle, certified",
        "spec": "1>2 1, 2>3 -3, 3>4 1, 4>2 1",
        "source": "1",
        "note": "something still improves in the last round, and the parent pointers close a loop",
    },
    {
        "id": "worstorder",
        "label": "the arcs typed in the worst possible order",
        "spec": "5>6 1, 4>5 1, 3>4 1, 2>3 1, 1>2 1",
        "source": "1",
        "note": "one label becomes final per round, so all of the rounds are needed",
    },
    {
        "id": "bestorder",
        "label": "the same chain, typed the other way round",
        "spec": "1>2 1, 2>3 1, 3>4 1, 4>5 1, 5>6 1",
        "source": "1",
        "note": "one round settles everything and the next changes nothing, so it stops",
    },
]


def _bellmanford(cfg):
    chosen = _chosen(_BF_PRESETS, cfg)
    markup = (
        _toolbar(
            "Rounds of relaxing every arc, and what a round buys",
            "after round k, every shortest path of at most k arcs is exact",
            [("cyan", "the arc that set this label"), ("red", "a negative cycle"),
             ("purple", "the round a label became final")],
        )
        + _stage(_svg("bfPlot", "0 0 660 300",
                      "The graph, with the arcs of the shortest-path tree drawn heavy, or the "
                      "negative cycle when there is one.")
                 + _svg("bfFinal", "0 0 660 130",
                        "One mark per vertex at the round its label stopped changing."))
        + _table("bfRounds")
        + _table("bfVerts")
        + _banner("bfStatus")
    )
    controls = (
        _select("bfPreset", "Worked example", _options(_BF_PRESETS), chosen["id"])
        + _text("bfSpec", "Arcs with weights, as tail&gt;head w", chosen["spec"])
        + _range("bfSource", "Labels from", 1, 12, chosen["source"])
        + _range("bfRound", "Show the table up to round", 1, 12, 12)
        + _kpis([("Rounds actually run", "bfRan"),
                 ("Relaxations performed", "bfRelax"),
                 ("Most arcs on any shortest path", "bfArcs"),
                 ("Final no later than its arc count", "bfMatch"),
                 ("Negative cycle", "bfCycle"),
                 ("Agrees with the all-pairs matrix", "bfAgree")])
        + _hint(
            "bfHint",
            "An arc is <span class=\"tt\">1&gt;2 6</span> and the weight may be negative. A shortest "
            "path uses at most one arc fewer than there are vertices, so that many rounds of "
            "relaxing every arc is enough &mdash; and a further round that still improves something "
            "cannot be explained by any path, which is the certificate. The negative arcs are the "
            "subject here; negative <em>cycles</em> are the thing that has no answer.",
        )
    )
    script = _BASE_JS + _ONE_GRAPH + _presets_js("BFP", _BF_PRESETS, ["spec", "source", "note"]) + r"""
  var presetIn = document.getElementById('bfPreset'), specIn = document.getElementById('bfSpec');
  var srcIn = document.getElementById('bfSource'), srcOut = document.getElementById('bfSourceOut');
  var roundIn = document.getElementById('bfRound'), roundOut = document.getElementById('bfRoundOut');
  var plot = document.getElementById('bfPlot'), finalPlot = document.getElementById('bfFinal');
  var roundsT = document.getElementById('bfRounds'), vertsT = document.getElementById('bfVerts');
  var status = document.getElementById('bfStatus');
  var KPIS = ['bfRan', 'bfRelax', 'bfArcs', 'bfMatch', 'bfCycle', 'bfAgree'];

  function blank(why) {
    plot.innerHTML = ''; finalPlot.innerHTML = ''; roundsT.innerHTML = ''; vertsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 6</span>, and <span class="tt">1&gt;2 -6</span> is allowed.';
  }

  /* One mark per vertex at the round its label last changed. The shape of this
     strip IS the induction: nothing is ever final before the number of arcs on
     its own shortest path. */
  function finalStrip(finalAt, arcsOn, n, rounds) {
    var span = Math.max(1, rounds), s = '', v;
    for (v = 0; v < n; v += 1) {
      var y = 18 + (v / Math.max(1, n - 1)) * 92;
      s += '<text x="6" y="' + (y + 4).toFixed(1) + '" font-size="10" font-weight="700" '
        + 'fill="var(--muted)">' + (v + 1) + '</text>';
      s += '<line x1="28" y1="' + y.toFixed(1) + '" x2="648" y2="' + y.toFixed(1)
        + '" stroke="var(--line)" />';
      if (finalAt[v] < 0) {
        s += '<text x="34" y="' + (y + 4).toFixed(1) + '" font-size="10" fill="var(--muted)">'
          + 'never reached</text>';
        continue;
      }
      var x = 28 + (finalAt[v] / span) * 610;
      s += '<circle cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="5" fill="var(--purple)" />';
      s += '<text x="' + (x + 9).toFixed(1) + '" y="' + (y + 4).toFixed(1) + '" font-size="10" '
        + 'fill="var(--text)">round ' + finalAt[v] + ', and its path uses '
        + (arcsOn[v] === null ? '?' : arcsOn[v]) + ' arc'
        + (arcsOn[v] === 1 ? '' : 's') + '</text>';
    }
    s += '<text x="28" y="126" font-size="11" fill="var(--muted)">round 0 on the left, round '
      + rounds + ' on the right</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, true);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    srcIn.max = n;
    var source = gkStep(parseInt(srcIn.value, 10) - 1, n);
    srcOut.textContent = String(source + 1);

    var run = bellmanFordRounds(G, source), res = run.result;
    var rounds = res.rounds;
    roundIn.max = Math.max(1, rounds.length);
    var k = gkStep(parseInt(roundIn.value, 10) - 1, rounds.length);
    roundOut.textContent = 'round ' + rounds[k].round + ' of ' + rounds.length;

    var cycle = res.negativeCycle;
    var cycleArcs = [];
    if (cycle) {
      for (var c = 0; c + 1 < cycle.length; c += 1) {
        var id = dgFind(G, cycle[c], cycle[c + 1]);
        if (id !== -1) cycleArcs.push(id);
      }
    }
    var treeArcs = [], v;
    for (v = 0; v < n; v += 1) {
      if (res.parent[v] === -1) continue;
      var tid = dgFind(G, res.parent[v], v);
      if (tid !== -1) treeArcs.push(tid);
    }
    var colours = new Array(n);
    for (v = 0; v < n; v += 1) colours[v] = res.dist[v] === null ? -1 : (v === source ? 3 : 1);
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                highlight: cycle ? cycleArcs : treeArcs, label: 'w',
                                colours: colours });

    var arcsOn = [];
    for (v = 0; v < n; v += 1) arcsOn.push(gkArcsOnPath(res.parent, source, v));
    finalPlot.innerHTML = finalStrip(res.finalAt, arcsOn, n, rounds.length);

    /* The rounds table is a matrix, so it is painted with the shared matrix
       printer rather than a second one written here. */
    var M = rounds.slice(0, k + 1).map(function (r) { return r.dist.slice(); });
    var changed = rounds.map(function (r) {
      var set = {};
      r.changed.forEach(function (x) { set[x] = true; });
      return set;
    });
    roundsT.innerHTML = paintMatrix(null, M, {
      caption: 'One row per round, one column per vertex: the labels after relaxing every arc',
      cols: gkLabels(n),
      rows: rounds.slice(0, k + 1).map(function (r) { return 'round ' + r.round; }),
      cell: function (i, j, val) { return val === null ? '&mdash;' : String(val); },
      on: function (i, j) { return !!changed[i][j]; }
    });

    var floyd = floydSteps(dgWeightMatrix(G));
    var theirs = floyd.result.dist[source];
    var agree = gkSameDistances(res.dist, theirs.map(function (d) { return d === null ? Infinity : d; }));
    /* WHAT THE INDUCTION ACTUALLY CLAIMS. After round k every shortest path of
       at most k arcs is exact, so a label is final NO LATER than the number of
       arcs on its own path -- `within`. It can be final much earlier: relax the
       arcs of a path in path order inside one round and the whole path settles
       at once, which is what the two chain examples here differ by. So the two
       counts are kept apart: one is the bound and must hold for every vertex,
       the other is a fact about the order that was typed. */
    var within = 0, exactly = 0, checkable = 0;
    for (v = 0; v < n; v += 1) {
      if (res.finalAt[v] < 0 || arcsOn[v] === null) continue;
      checkable += 1;
      if (res.finalAt[v] <= arcsOn[v]) within += 1;
      if (res.finalAt[v] === arcsOn[v]) exactly += 1;
    }

    var vrows = '';
    for (v = 0; v < n; v += 1) {
      vrows += '<tr><th class="rowhead">' + (v + 1) + '</th><td>' + gkDistText(res.dist[v])
        + '</td><td>' + (res.finalAt[v] < 0 ? 'never' : String(res.finalAt[v])) + '</td><td>'
        + (arcsOn[v] === null ? '—' : String(arcsOn[v])) + '</td><td>'
        + gkPathText(gkPathTo(res.parent, source, v)) + '</td><td>'
        + (theirs[v] === null ? 'not reached' : String(theirs[v])) + '</td></tr>';
    }
    vertsT.innerHTML = '<caption>Each label, the round it stopped moving, and the same distance '
      + 'from the all-pairs matrix</caption><thead><tr><th>vertex</th><th>label</th>'
      + '<th>final in round</th><th>arcs on its path</th><th>path</th><th>all-pairs</th>'
      + '</tr></thead><tbody>' + vrows + '</tbody>';

    var most = 0;
    for (v = 0; v < n; v += 1) if (arcsOn[v] !== null && arcsOn[v] > most) most = arcsOn[v];
    document.getElementById('bfRan').textContent = rounds.length + ' of the ' + n + ' allowed';
    document.getElementById('bfRelax').textContent = run.counts.relaxations || 0;
    document.getElementById('bfArcs').textContent = most;
    document.getElementById('bfMatch').textContent = cycle ? 'no path to compare'
      : (within === checkable
          ? 'never later than its arc count; ' + exactly + ' of ' + checkable + ' exactly at it'
          : (checkable - within) + ' later than the arc count — report it');
    document.getElementById('bfCycle').textContent = cycle
      ? cycle.map(function (x) { return x + 1; }).join(' → ') : 'none';
    document.getElementById('bfAgree').textContent = cycle ? 'not asked: no distances exist'
      : (agree ? 'yes, every distance' : 'no — report it');

    if (cycle) {
      var total = 0;
      cycleArcs.forEach(function (id) { total += G.arcs[id].w; });
      status.innerHTML = '<strong><span class="tone-red">A negative cycle.</span></strong> '
        + 'Something still improved in round ' + rounds.length + ', and no path can explain that: '
        + 'a shortest path uses at most ' + (n - 1) + ' arc' + gkPlural(n - 1, '', 's')
        + ', so every label that could be explained by one was already exact. Following the parent '
        + 'pointers back from a vertex that moved lands inside the loop, and the loop is '
        + '<span class="tone-red">' + cycle.map(function (x) { return x + 1; }).join(' → ')
        + '</span> at total weight <span class="tone-red">' + total + '</span>. Go round it again '
        + 'and the walk is ' + total + ' cheaper, so there is no shortest walk at all &mdash; not a '
        + 'large one, none. The certificate is the cycle, and it is the object itself rather than a '
        + 'flag saying one exists.';
      return;
    }
    status.innerHTML = '<strong>' + rounds.length + ' round'
      + gkPlural(rounds.length, '', 's') + ' and ' + (run.counts.relaxations || 0)
      + ' relaxations</strong>, where ' + n + ' were allowed. The longest shortest path here uses '
      + '<span class="tone-purple">' + most + '</span> arc' + gkPlural(most, '', 's')
      + ', and <span class="' + (within === checkable ? 'tone-green' : 'tone-red') + '">'
      + within + ' of ' + checkable + '</span> labels became final no later than the number of '
      + 'arcs on their own path &mdash; which is exactly what the induction promises, and it '
      + (within === checkable ? 'holds here. ' : 'has failed, which cannot happen. ')
      + 'Of those, <span class="tone-purple">' + exactly + '</span> became final in precisely that '
      + 'round and the rest earlier: the promise is an upper bound, and relaxing the arcs of a path '
      + 'in path order inside one round settles the whole path at once. '
      + (rounds.length < n
          ? 'Round ' + rounds.length + ' changed nothing, so the algorithm stopped there rather '
            + 'than running all ' + n + ' &mdash; the bound is a worst case and the arc order you '
            + 'typed decides how close to it this graph comes.'
          : 'All ' + n + ' rounds ran, which is what the arc order forces here: each round can only '
            + 'extend a shortest path by the one arc it happens to relax after the arc before it.')
      + (agree
          ? ' The same distances come out of the all-pairs matrix, computed by filling in one '
            + 'interior vertex at a time and never mentioning a round: <span class="tone-green">'
            + 'they agree</span>.'
          : ' <span class="tone-red">The all-pairs matrix disagrees, which means one of the two is '
            + 'wrong.</span>');
  }

  function apply() {
    var p = BFP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; srcIn.value = p.source; roundIn.value = roundIn.max;
    redraw();
  }
  var START = BFP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; srcIn.value = START.source; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  roundIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bellman–Ford, round by round",
        subtitle="One round per arc on a shortest path, and a round that still improves something is a negative cycle",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the arcs; negative weights are the subject"),
        panel_intro=cfg.get(
            "panel_intro",
            "The table is one row per round. The round each label became final is compared with "
            "the number of arcs on its own shortest path, and the distances are compared with an "
            "all-pairs matrix that never mentions a round.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# dagsp -- one pass, and the sign that turns it into longest
# ---------------------------------------------------------------------------

_DS_PRESETS = [
    {
        "id": "project",
        "label": "a small project, so the longest path is the critical one",
        "spec": "1>2 3, 1>3 2, 2>4 4, 3>4 1, 4>5 2, 3>5 7, 5>6 1",
        "source": "1",
        "note": "the critical path is the longest one, and everything off it has slack",
    },
    {
        "id": "settled",
        "label": "a negative arc, where settling once goes wrong",
        "spec": "1>2 2, 1>3 3, 3>2 -2, 2>4 1",
        "source": "1",
        "note": "nearest-first settles 2 at 2, relaxes 2 to 4 from it, and only then finds the "
                "cheaper route into 2",
    },
    {
        "id": "cyclic",
        "label": "a cycle, where neither pass exists",
        "spec": "1>2 3, 2>3 2, 3>1 1, 3>4 5",
        "note": "negate the weights and the cycle is negative, which is why the trick needs a DAG",
        "source": "1",
    },
    {
        "id": "wide",
        "label": "two long parallel routes, nearly the same length",
        "spec": "1>2 5, 2>3 5, 3>6 5, 1>4 7, 4>5 4, 5>6 3, 1>6 2",
        "source": "1",
        "note": "shortening the critical route by enough makes the other one critical instead",
    },
]


def _dagsp(cfg):
    chosen = _chosen(_DS_PRESETS, cfg)
    markup = (
        _toolbar(
            "One pass in topological order, and the same pass for longest",
            "negating the weights keeps the order, which is the whole reason it works",
            [("cyan", "on the extreme path"), ("purple", "has slack"),
             ("red", "no order exists")],
        )
        + _stage(_svg("dsPlot", "0 0 660 220",
                      "The vertices in topological order, left to right, with the extreme path "
                      "drawn heavy.")
                 + _svg("dsSlack", "0 0 660 140",
                        "For each vertex, the earliest and latest it can sit, and the gap between "
                        "them."))
        + _table("dsPass")
        + _table("dsCompare")
        + _banner("dsStatus")
    )
    controls = (
        _select("dsPreset", "Worked example", _options(_DS_PRESETS), chosen["id"])
        + _text("dsSpec", "Arcs with weights, as tail&gt;head w", chosen["spec"])
        + _range("dsSource", "Start from", 1, 12, chosen["source"])
        + _select("dsSign", "Take the",
                  [("1", "shortest path"), ("-1", "longest path")], "1")
        + _kpis([("The far end, and what it costs", "dsValue"),
                 ("The path it came along", "dsPath"),
                 ("Vertices with no slack", "dsTight"),
                 ("Relaxations: one per arc", "dsRelax"),
                 ("Agrees with the rounds method", "dsAgree"),
                 ("Nearest-first schedule agrees", "dsDij")])
        + _hint(
            "dsHint",
            "In topological order a vertex is relaxed only after everything that points at it, so "
            "one pass over each arc is enough and negative weights are no trouble at all. Flip the "
            "sign and the same pass returns the longest path &mdash; which on a graph with a cycle "
            "is not merely hard but undefined, because negating a positive cycle makes it negative. "
            "Try the cyclic example and read what the page refuses to answer.",
        )
    )
    script = _BASE_JS + _ONE_GRAPH + _presets_js("DSP", _DS_PRESETS, ["spec", "source", "note"]) + r"""
  var presetIn = document.getElementById('dsPreset'), specIn = document.getElementById('dsSpec');
  var srcIn = document.getElementById('dsSource'), srcOut = document.getElementById('dsSourceOut');
  var signIn = document.getElementById('dsSign');
  var plot = document.getElementById('dsPlot'), slack = document.getElementById('dsSlack');
  var passT = document.getElementById('dsPass'), cmpT = document.getElementById('dsCompare');
  var status = document.getElementById('dsStatus');
  var KPIS = ['dsValue', 'dsPath', 'dsTight', 'dsRelax', 'dsAgree', 'dsDij'];

  function reset(fields) {
    plot.innerHTML = ''; slack.innerHTML = ''; passT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) {
      document.getElementById(KPIS[i]).textContent = fields || '—';
    }
  }
  function blank(why) {
    reset(null);
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 3</span> and it points one way.';
  }

  function orderPoints(order, n) {
    var pts = new Array(n), i;
    (order || []).forEach(function (v, k) {
      pts[v] = [40 + (order.length < 2 ? 290 : (k / (order.length - 1)) * 580),
                110 + (k % 2 ? 58 : -48)];
    });
    for (i = 0; i < n; i += 1) if (!pts[i]) pts[i] = [40 + i * 30, 190];
    return pts;
  }

  /* Earliest as a filled bar, latest as an outline: where they coincide the
     vertex cannot move, and those are the ones on every extreme path. */
  function slackBars(dist, latest, slk, n) {
    var lo = 0, hi = 1, v;
    for (v = 0; v < n; v += 1) {
      if (dist[v] === null) continue;
      if (dist[v] < lo) lo = dist[v];
      if (dist[v] > hi) hi = dist[v];
      if (latest[v] !== null) { if (latest[v] < lo) lo = latest[v]; if (latest[v] > hi) hi = latest[v]; }
    }
    var span = Math.max(1, hi - lo), s = '';
    for (v = 0; v < n; v += 1) {
      var y = 14 + (v / Math.max(1, n - 1)) * 98;
      s += '<text x="6" y="' + (y + 4).toFixed(1) + '" font-size="10" font-weight="700" '
        + 'fill="var(--muted)">' + (v + 1) + '</text>';
      if (dist[v] === null) {
        s += '<text x="30" y="' + (y + 4).toFixed(1) + '" font-size="10" fill="var(--muted)">'
          + 'not reached from here</text>';
        continue;
      }
      var x1 = 30 + ((dist[v] - lo) / span) * 560;
      var x2 = 30 + (((latest[v] === null ? dist[v] : latest[v]) - lo) / span) * 560;
      var tight = slk[v] === 0;
      s += '<circle cx="' + x1.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="5" fill="var('
        + (tight ? '--cyan' : '--purple') + ')" />';
      if (!tight) {
        s += '<line x1="' + x1.toFixed(1) + '" y1="' + y.toFixed(1) + '" x2="' + x2.toFixed(1)
          + '" y2="' + y.toFixed(1) + '" stroke="var(--purple)" stroke-width="3" opacity="0.6" />';
        s += '<circle cx="' + x2.toFixed(1) + '" cy="' + y.toFixed(1)
          + '" r="4" fill="none" stroke="var(--purple)" />';
      }
      s += '<text x="' + (Math.max(x1, x2) + 9).toFixed(1) + '" y="' + (y + 4).toFixed(1)
        + '" font-size="10" fill="var(--text)">' + dist[v]
        + (tight ? ', no slack' : ' to ' + latest[v] + ', slack ' + slk[v]) + '</text>';
    }
    s += '<text x="30" y="132" font-size="11" fill="var(--muted)">earliest filled, latest '
      + 'outlined</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, true);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    srcIn.max = n;
    var source = gkStep(parseInt(srcIn.value, 10) - 1, n);
    srcOut.textContent = String(source + 1);
    var sign = signIn.value === '-1' ? -1 : 1;

    var topo = topoDfs(G);
    if (!topo.result.acyclic) {
      var back = topo.result.backEdge;
      var neg = gkNegate(G), cyc = bellmanFordRounds(neg, source).result.negativeCycle;
      reset('no order');
      plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 110, radius: 86 }),
                                  label: 'w', highlight: back ? [back.id] : [] });
      status.innerHTML = '<strong><span class="tone-red">This graph has a cycle, so there is no '
        + 'topological order and no pass to make.</span></strong> The walk found the back arc '
        + '<span class="tone-red">' + (back.u + 1) + ' → ' + (back.v + 1) + '</span>. '
        + 'That is not only an obstacle to the method: with the weights negated the cycle has '
        + (cyc
            ? 'total weight below zero, and the rounds method returns it as a certificate — '
              + '<span class="tone-red">' + cyc.map(function (x) { return x + 1; }).join(' → ')
              + '</span> — so there is no longest walk to find, however it is looked for. '
            : 'no reachable negative total from this start, so nothing is certified from here; move '
              + 'the start onto the cycle and it will be. ')
        + 'Longest path is shortest path with the sign flipped ONLY on a graph with no cycle, and '
        + 'the reason is exactly this: the negation preserves the arcs and destroys the bound.';
      return;
    }

    var run = dagRelax(G, source, sign), res = run.result;
    var truth = bellmanFordRounds(sign === 1 ? G : gkNegate(G), source).result.dist;
    var agree = true, v;
    for (v = 0; v < n; v += 1) {
      var want = truth[v] === null ? null : (sign === 1 ? truth[v] : -truth[v]);
      if ((res.dist[v] === null) !== (want === null)) { agree = false; break; }
      if (res.dist[v] !== null && res.dist[v] !== want) { agree = false; break; }
    }
    var dij = relaxRun(G, source, 'heap').result.dist;
    var dijAgrees = sign === 1 && gkSameDistances(res.dist, dij.map(function (d) {
      return d === null ? Infinity : d; }));

    var pathArcs = [], tight = [];
    for (v = 0; v < n; v += 1) {
      if (res.slack[v] === 0) tight.push(v);
      if (res.parent[v] === -1) continue;
      var id = dgFind(G, res.parent[v], v);
      if (id !== -1 && res.slack[v] === 0 && res.slack[res.parent[v]] === 0) pathArcs.push(id);
    }
    plot.innerHTML = dgSvg(G, { points: orderPoints(res.order, n), label: 'w',
                                highlight: pathArcs,
                                colours: res.dist.map(function (d, x) {
                                  return d === null ? -1 : (res.slack[x] === 0 ? 0 : 1); }) });
    slack.innerHTML = slackBars(res.dist, res.latest, res.slack, n);

    var prows = '';
    res.order.forEach(function (x, k) {
      prows += '<tr' + (res.slack[x] === 0 ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + (k + 1) + '</th><td>' + (x + 1) + '</td><td>' + gkDistText(res.dist[x]) + '</td><td>'
        + (res.latest[x] === null ? '—' : String(res.latest[x])) + '</td><td>'
        + (res.slack[x] === null ? '—' : String(res.slack[x])) + '</td><td>'
        + gkPathText(gkPathTo(res.parent, source, x)) + '</td></tr>';
    });
    passT.innerHTML = '<caption>The single pass, in topological order: each vertex is finished '
      + 'when it is reached</caption><thead><tr><th>position</th><th>vertex</th><th>earliest</th>'
      + '<th>latest</th><th>slack</th><th>path from the start</th></tr></thead><tbody>' + prows
      + '</tbody>';

    cmpT.innerHTML = '<caption>The same question, three schedules</caption><thead><tr>'
      + '<th>method</th><th>what it needs</th><th>value at the far end</th><th>work</th>'
      + '</tr></thead><tbody>'
      + '<tr><th class="rowhead">one pass in topological order</th><td>no cycle</td>'
      + '<td class="tone-cyan">' + gkDistText(res.extreme === null ? null : res.dist[res.extreme])
      + '</td><td>' + (run.counts.relaxations || 0) + ' relaxations, one per arc</td></tr>'
      + '<tr><th class="rowhead">rounds of relaxing every arc</th><td>no negative cycle</td><td>'
      + (res.extreme === null ? '—'
          : gkDistText(truth[res.extreme] === null ? null
              : (sign === 1 ? truth[res.extreme] : -truth[res.extreme])))
      + '</td><td>' + n + ' rounds over ' + G.arcs.length + ' arcs</td></tr>'
      + '<tr><th class="rowhead">nearest unsettled first</th><td>no negative weight</td><td>'
      + (sign === 1
          ? (res.extreme === null ? '—' : gkDistText(dij[res.extreme]))
          : 'cannot be asked for a longest path')
      + '</td><td>' + (sign === 1 ? 'a heap, and a settled set' : '—') + '</td></tr></tbody>';

    var negArcs = G.arcs.filter(function (a) { return a.w < 0; }).length;
    document.getElementById('dsValue').textContent = res.extreme === null ? 'nothing reached'
      : 'vertex ' + (res.extreme + 1) + ', at ' + gkDistText(res.dist[res.extreme]);
    document.getElementById('dsPath').textContent = res.extreme === null ? '—'
      : gkPathText(gkPathTo(res.parent, source, res.extreme));
    document.getElementById('dsTight').textContent = gkNames(tight) || 'none';
    document.getElementById('dsRelax').textContent = (run.counts.relaxations || 0) + ' for '
      + G.arcs.length + ' arcs';
    document.getElementById('dsAgree').textContent = agree ? 'yes, every value' : 'no — report it';
    document.getElementById('dsDij').textContent = sign === -1 ? 'not applicable to longest'
      : (dijAgrees ? 'yes' : 'no, and here is why');

    status.innerHTML = '<strong>' + (res.extreme === null
          ? 'Nothing is reachable from ' + (source + 1)
          : (sign === 1
              ? 'The farthest vertex from ' + (source + 1) + ' is ' + (res.extreme + 1)
                + ', at ' + gkDistText(res.dist[res.extreme])
              : 'The longest path from ' + (source + 1) + ' ends at ' + (res.extreme + 1)
                + ', at ' + gkDistText(res.dist[res.extreme])))
      + '</strong>, in <span class="tone-cyan">' + (run.counts.relaxations || 0)
      + '</span> relaxations for ' + G.arcs.length + ' arc' + gkPlural(G.arcs.length, '', 's')
      + ' &mdash; one each, because in topological order a vertex is never relaxed again after it is '
      + 'passed. ' + (negArcs
          ? 'There ' + (negArcs === 1 ? 'is 1 negative arc' : 'are ' + negArcs + ' negative arcs')
            + ' and the pass does not care: order, not sign, is what it needs. '
          : 'Every arc here is non-negative, so try one that is not &mdash; the pass is unchanged. ')
      + '<span class="tone-purple">' + tight.length + '</span> vert'
      + gkPlural(tight.length, 'ex', 'ices') + ' ha' + gkPlural(tight.length, 's', 've')
      + ' no slack &mdash; slack being how far a vertex could move off its earliest time without '
      + 'moving the far end, and zero meaning it cannot move at all. '
      + (sign === 1 ? 'Those are the ones on a shortest route to the far end. '
          : 'Those are the critical ones: shortening anything else changes nothing. ')
      + (agree
          ? 'The rounds method, run on ' + (sign === 1 ? 'the same graph' : 'the graph with every '
              + 'weight negated') + ', <span class="tone-green">reaches the same values</span>. '
          : '<span class="tone-red">The rounds method disagrees, which means one of the two is '
            + 'wrong.</span> ')
      + (sign === -1
          ? 'That negated graph is the whole trick, and it is only safe here: negate a graph with a '
            + 'cycle and the cycle can go negative, at which point no algorithm has a longest walk '
            + 'to return.'
          : (dijAgrees
              ? 'Nearest-unsettled-first agrees on this instance too.'
              : '<span class="tone-amber">Nearest-unsettled-first does NOT agree here.</span> It '
                + 'settles a vertex when it first comes off the heap and relaxes that vertex’s '
                + 'arcs from the label it had then; a negative arc found later improves the label '
                + 'and nothing goes back to re-relax what was sent onward from it. One pass in '
                + 'topological order cannot make that mistake, because nothing is passed until '
                + 'everything pointing at it has been.'));
  }

  function apply() {
    var p = DSP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; srcIn.value = p.source;
    redraw();
  }
  var START = DSP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; srcIn.value = START.source; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  signIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Shortest and longest paths in a graph with no cycle",
        subtitle="One pass in topological order, negative weights allowed, and the sign flip that gives the critical path",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the arcs and choose shortest or longest"),
        panel_intro=cfg.get(
            "panel_intro",
            "One relaxation per arc, in topological order. The values are checked against the "
            "rounds method, and against the nearest-unsettled-first schedule as well &mdash; which "
            "on a graph with a negative arc returns something different, printed beside them.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# floyd -- one matrix, one interior vertex at a time
# ---------------------------------------------------------------------------

_FW_PRESETS = [
    {
        "id": "interior",
        "label": "a route that needs two interior vertices",
        "spec": "1>2 6, 2>4 9, 3>2 2, 4>3 8",
        "from": "1", "to": "3",
        "note": "1 to 3 is 23 through 2 and 4, which only appears once both are allowed inside",
    },
    {
        "id": "negative",
        "label": "negative arcs, which the all-pairs matrix does not mind",
        "spec": "1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, 4>2 -2, 5>1 2, 5>4 7",
        "from": "1", "to": "5",
        "note": "the same negative weights the rounds method handles, in one matrix",
    },
    {
        "id": "negcycle",
        "label": "a negative cycle, visible on the diagonal",
        "spec": "1>2 1, 2>3 -3, 3>4 1, 4>2 1, 1>4 7",
        "from": "1", "to": "3",
        "note": "a diagonal entry goes below zero, which is a walk from a vertex back to itself "
                "that costs less than nothing",
    },
    {
        "id": "sparse",
        "label": "sparse and wide, where the one-source method wins",
        "spec": "1>2 1, 2>3 1, 3>4 1, 4>5 1, 5>6 1, 6>7 1, 7>8 1",
        "from": "1", "to": "8",
        "note": "eight vertices and seven arcs: filling a whole matrix does far more work than "
                "one pass per source",
    },
]


def _floyd(cfg):
    chosen = _chosen(_FW_PRESETS, cfg)
    markup = (
        _toolbar(
            "One matrix, one interior vertex at a time",
            "the outer loop says which vertices a route is allowed to pass through",
            [("cyan", "improved at this step"), ("purple", "on the rebuilt path"),
             ("red", "a negative diagonal")],
        )
        + _stage(_svg("fwPlot", "0 0 660 300",
                      "The graph, with the arcs of the rebuilt path drawn heavy.")
                 + _svg("fwGrid", "0 0 520 200",
                        "The matrix as a grid of cells, darker where the distance is smaller."))
        + _table("fwMatrix")
        + _table("fwCheck")
        + _banner("fwStatus")
    )
    controls = (
        _select("fwPreset", "Worked example", _options(_FW_PRESETS), chosen["id"])
        + _text("fwSpec", "Arcs with weights, as tail&gt;head w", chosen["spec"])
        + _range("fwK", "Allow interior vertices up to", 1, 12, 12)
        + _range("fwFrom", "Rebuild the path from", 1, 12, chosen["from"])
        + _range("fwTo", "to", 1, 12, chosen["to"])
        + _kpis([("The distance between them", "fwDist"),
                 ("The path, from next", "fwPath"),
                 ("Relaxations: one per cell per step", "fwWork"),
                 ("Compared with one source at a time", "fwAlt"),
                 ("Negative diagonal", "fwNeg"),
                 ("Agrees with the rounds method", "fwAgree")])
        + _hint(
            "fwHint",
            "The subproblem is the whole content: after step k, the cell "
            "<span class=\"tt\">D[i][j]</span> is the best route from i to j whose interior "
            "vertices are all among the first k. That is why the k loop is the outer one &mdash; "
            "write the loops in another order and you compute something else that often looks "
            "right. Step k below and watch which cells move.",
        )
    )
    script = _BASE_JS + _ONE_GRAPH + _presets_js("FWP", _FW_PRESETS, ["spec", "from", "to", "note"]) + r"""
  var presetIn = document.getElementById('fwPreset'), specIn = document.getElementById('fwSpec');
  var kIn = document.getElementById('fwK'), kOut = document.getElementById('fwKOut');
  var fromIn = document.getElementById('fwFrom'), fromOut = document.getElementById('fwFromOut');
  var toIn = document.getElementById('fwTo'), toOut = document.getElementById('fwToOut');
  var plot = document.getElementById('fwPlot'), grid = document.getElementById('fwGrid');
  var matrixT = document.getElementById('fwMatrix'), checkT = document.getElementById('fwCheck');
  var status = document.getElementById('fwStatus');
  var KPIS = ['fwDist', 'fwPath', 'fwWork', 'fwAlt', 'fwNeg', 'fwAgree'];

  function blank(why) {
    plot.innerHTML = ''; grid.innerHTML = ''; matrixT.innerHTML = ''; checkT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 6</span> and it points one way.';
  }

  /* The matrix as cells, so the shape of the answer is visible before any
     number is read: the diagonal, the unreachable pairs, and where the small
     distances live. */
  function gridOf(M, n) {
    var lo = null, hi = null, i, j;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) {
      var v = M[i][j];
      if (v === null) continue;
      if (lo === null || v < lo) lo = v;
      if (hi === null || v > hi) hi = v;
    }
    if (lo === null) { lo = 0; hi = 1; }
    var span = Math.max(1, hi - lo);
    var cell = Math.max(12, Math.min(28, Math.floor(170 / n))), s = '';
    for (i = 0; i < n; i += 1) {
      s += '<text x="' + (24 + i * cell + cell / 2).toFixed(1) + '" y="14" text-anchor="middle" '
        + 'font-size="9" fill="var(--muted)">' + (i + 1) + '</text>';
      s += '<text x="16" y="' + (22 + i * cell + cell / 2 + 3).toFixed(1) + '" text-anchor="end" '
        + 'font-size="9" fill="var(--muted)">' + (i + 1) + '</text>';
      for (j = 0; j < n; j += 1) {
        var val = M[i][j];
        var fill = val === null ? 'var(--panel-3)'
          : (val < 0 ? 'var(--red)' : 'var(--cyan)');
        var op = val === null ? '0.5' : (val < 0 ? '0.85'
          : (0.85 - 0.6 * ((val - lo) / span)).toFixed(2));
        s += '<rect x="' + (24 + j * cell) + '" y="' + (22 + i * cell) + '" width="' + (cell - 2)
          + '" height="' + (cell - 2) + '" rx="2" fill="' + fill + '" opacity="' + op + '" />';
      }
    }
    s += '<text x="24" y="' + (36 + n * cell) + '" font-size="11" fill="var(--muted)">'
      + 'darker is smaller; the palest cells are pairs with no route yet</text>';
    return s;
  }

  function redraw() {
    var parsed = gkParse(specIn.value, true);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var W = dgWeightMatrix(G);
    var run = floydSteps(W), res = run.result;
    kIn.max = n; fromIn.max = n; toIn.max = n;
    var k = gkStep(parseInt(kIn.value, 10) - 1, res.steps.length);
    var from = gkStep(parseInt(fromIn.value, 10) - 1, n);
    var to = gkStep(parseInt(toIn.value, 10) - 1, n);
    kOut.textContent = 'through ' + (k + 1) + ' of ' + n;
    fromOut.textContent = String(from + 1);
    toOut.textContent = String(to + 1);

    var atK = res.steps[k].matrix;
    var before = k === 0 ? W : res.steps[k - 1].matrix;
    var path = floydPath(res.next, from, to);
    var pathArcs = [], i;
    if (path) {
      for (i = 0; i + 1 < path.length; i += 1) {
        var id = dgFind(G, path[i], path[i + 1]);
        if (id !== -1) pathArcs.push(id);
      }
    }
    var onPath = {};
    (path || []).forEach(function (v) { onPath[v] = true; });

    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                label: 'w', highlight: pathArcs,
                                colours: gkLabels(n).map(function (_x, v) {
                                  return v === from ? 3 : (v === to ? 4 : (onPath[v] ? 1 : -1)); }) });
    grid.innerHTML = gridOf(atK, n);

    matrixT.innerHTML = paintMatrix(null, atK, {
      caption: 'The matrix after allowing interior vertices up to ' + (k + 1)
        + ': the cells that moved at this step are marked',
      cols: gkLabels(n), rows: gkLabels(n),
      cell: function (a, b, val) { return val === null ? '&mdash;' : String(val); },
      on: function (a, b) {
        return before[a][b] !== atK[a][b];
      }
    });

    /* The independent answer: the rounds method from every source, which never
       builds a matrix and never mentions an interior vertex. */
    var agree = true, worst = null;
    for (i = 0; i < n; i += 1) {
      var bf = bellmanFordRounds(G, i).result;
      if (bf.negativeCycle) { agree = null; break; }
      for (var j = 0; j < n; j += 1) {
        var mineV = res.dist[i][j], theirV = bf.dist[j];
        if ((mineV === null) !== (theirV === null) || (mineV !== null && mineV !== theirV)) {
          agree = false; worst = (i + 1) + ' to ' + (j + 1);
        }
      }
      if (agree === false) break;
    }
    var cells = n * n * n;
    var oneSource = n * G.arcs.length * Math.max(1, Math.ceil(Math.log(Math.max(2, n)) / Math.LN2));
    checkT.innerHTML = '<caption>The same all-pairs question, two ways, and what each one '
      + 'costs</caption><thead><tr><th>method</th><th>this instance</th><th>steps it takes</th>'
      + '<th>what it needs of the graph</th></tr></thead><tbody>'
      + '<tr><th class="rowhead">one matrix, one interior vertex at a time</th>'
      + '<td class="tone-cyan">' + (run.counts.relaxations || 0) + ' relaxations</td><td>'
      + n + ' cubed, which is ' + cells + '</td><td>no negative cycle</td></tr>'
      + '<tr><th class="rowhead">one pass per source, from a heap</th><td class="tone-cyan">'
      + oneSource + ' as a reference</td><td>V times E log' + '₂' + ' V</td>'
      + '<td>no negative weight at all</td></tr>'
      + '<tr><th class="rowhead">rounds, once per source</th><td class="tone-cyan">'
      + (n * n * G.arcs.length) + ' as a reference</td><td>V times V times E</td>'
      + '<td>no negative cycle</td></tr></tbody>';

    document.getElementById('fwDist').textContent = res.dist[from][to] === null
      ? 'no route at all' : String(res.dist[from][to]);
    document.getElementById('fwPath').textContent = path === null
      ? 'none' : gkPathText(path);
    document.getElementById('fwWork').textContent = (run.counts.relaxations || 0) + ' for '
      + cells + ' cell visits';
    document.getElementById('fwAlt').textContent = oneSource + ' against ' + cells;
    document.getElementById('fwNeg').textContent = res.negativeCycleAt.length
      ? gkNames(res.negativeCycleAt) : 'none';
    document.getElementById('fwAgree').textContent = agree === null
      ? 'not asked: a negative cycle' : (agree ? 'yes, every pair' : 'no at ' + worst);

    if (res.negativeCycleAt.length) {
      var v0 = res.negativeCycleAt[0];
      status.innerHTML = '<strong><span class="tone-red">A negative cycle.</span></strong> '
        + 'The diagonal entry for vertex ' + (v0 + 1) + ' came out at <span class="tone-red">'
        + res.dist[v0][v0] + '</span>, and a diagonal entry is the cost of a walk from a vertex '
        + 'back to itself: below zero it can be gone round again for less than nothing, so no '
        + 'shortest walk exists between any pair that can reach it. The matrix is where this shows '
        + 'up for free &mdash; there is no separate check, only a number on the diagonal that '
        + 'should have stayed at 0.';
      return;
    }
    var moved = 0;
    for (i = 0; i < n; i += 1) for (var b = 0; b < n; b += 1) if (before[i][b] !== atK[i][b]) moved += 1;
    status.innerHTML = '<strong>' + (path === null
        ? 'There is no route from ' + (from + 1) + ' to ' + (to + 1)
        : (from + 1) + ' to ' + (to + 1) + ' is ' + res.dist[from][to] + ' along '
          + gkPathText(path)) + '</strong>, rebuilt by following next[] one hop at a time rather '
      + 'than by storing the path. Allowing interior vertices up to ' + (k + 1) + ' moved '
      + '<span class="tone-cyan">' + moved + '</span> cell' + gkPlural(moved, '', 's')
      + ' of the ' + (n * n) + ' in the matrix. '
      + 'The whole fill took <span class="tone-purple">' + (run.counts.relaxations || 0)
      + '</span> relaxations, which is ' + n + ' cubed exactly, and one pass per source from a heap '
      + 'would be about <span class="tone-amber">' + oneSource + '</span> on this graph &mdash; '
      + (oneSource < cells
          ? 'less, because this graph is sparse. The matrix is not always the cheaper choice; it '
            + 'wins when the graph is dense, or when a weight is negative and the heap cannot be '
            + 'used at all.'
          : 'more, because this graph is dense enough that the matrix does less work than V '
            + 'separate searches. That is the comparison, and it moves with the graph.')
      + (agree
          ? ' Every one of the ' + (n * n) + ' distances was checked against the rounds method run '
            + 'from each source in turn, which never builds a matrix: <span class="tone-green">'
            + 'they all agree</span>.'
          : ' <span class="tone-red">The rounds method disagrees at ' + worst + '.</span>');
  }

  function apply() {
    var p = FWP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; fromIn.value = p.from; toIn.value = p.to; kIn.value = kIn.max;
    redraw();
  }
  var START = FWP[presetIn.value];
  if (START && !specIn.value) {
    specIn.value = START.spec; fromIn.value = START.from; toIn.value = START.to;
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  fromIn.addEventListener('input', redraw);
  toIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Floyd–Warshall, one interior vertex at a time",
        subtitle="The outer loop is the subproblem, and the path comes back out of next rather than being stored",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the arcs, then let more vertices inside"),
        panel_intro=cfg.get(
            "panel_intro",
            "The matrix is filled in your browser and kept after every step, so you can see which "
            "cells each interior vertex improves. Every distance is checked against the rounds "
            "method run from each source in turn.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice -- the markup assertions
# pass, labcheck passes, and a reader is shown a topological order under the
# heading about minimum cuts.
# ---------------------------------------------------------------------------

_MODES = {
    "dfstimes": _dfstimes,
    "topo": _topo,
    "lowlink": _lowlink,
    "scc": _scc,
    "cutproperty": _cutproperty,
    "prim": _prim,
    "kruskal": _kruskal,
    "relax": _relax,
    "bellmanford": _bellmanford,
    "dagsp": _dagsp,
    "floyd": _floyd,
}

MODES = tuple(sorted(_MODES))


def graphkit_lab(cfg):
    """The graph course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "graphkit_lab: unknown mode %r; the eleven modes of the graph course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["graphkit_lab", "GKIT_JS", "MODES"]
