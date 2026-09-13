"""The exact engine the Algorithms labs share.

Every figure on an Algorithms page is a COUNT -- comparisons, swaps, probes,
pointer hops, relaxations, nodes expanded -- produced by running the algorithm
in the reader's browser and incrementing a counter, never by quoting a
complexity class. A count of integers is exact in any representation, so most
of this module returns plain integers; the places that are not integers are
probabilities, expectations, charges and ratios, and those are `RATIONAL_JS`
from algebra_core -- BigInt over BigInt -- so a page prints `39/20`, not
`1.9500000000000002`.

WHAT IS NOT EXACT ON THIS PATH. Course §2's footer promises the reader exactly
four, and this module is where all four live:

  knuthProbeApprox(alpha)        HASH_JS.  Linear probing's clustering curve,
                                 (1 + 1/(1-a)^2)/2 for an unsuccessful search
                                 and (1 + 1/(1-a))/2 for a successful one. The
                                 arithmetic is a double -- relative error under
                                 1e-15, negligible -- and the MODEL is the
                                 approximation: it assumes a uniform hash and
                                 an idealised cluster distribution, and the
                                 lesson compares it against probes the page
                                 actually measured. Above a = 0.98 it is not
                                 quoted at all: the curve is vertical there and
                                 a number off it means nothing.
  randomBstDepthApprox(n)        TREE_JS. 2 ln n, the asymptotic mean root-to-
                                 node depth of a tree built from a uniformly
                                 random insertion order. Asymptotic: at n = 15
                                 it reads 5.42 against a true mean near 4.6, so
                                 it is drawn as a reference curve and labelled,
                                 never as the answer. Math.log is correctly
                                 rounded, so the number is the asymptote to
                                 ~1e-15 and wrong about the tree by ~15%.
  sysdesign_core.bloomApprox     HASH_JS's `bloom` mode prints it BESIDE
                                 bloomExact(m, n, k), which is exact and a
                                 rational. The gap between them is the
                                 independent-hash idealisation, and showing
                                 both is the lesson.
  sysdesign_core.logApprox       The maximum-load asymptotics: log n / log log n
                                 for one choice and ln ln n for two. STATED AND
                                 PROVED NOWHERE IN THIS LIBRARY -- their proofs
                                 need Chernoff bounds, which no Subject here
                                 teaches. Every mode that prints one says so in
                                 those words and puts the load it MEASURED in
                                 the next column.

Everything else rounds only where a drawing does. A reference curve on a plot
(n log2 n, n^2/2, E log V, 2^n) is sampled through Math.log2 or Math.pow at
double precision; it is a drawing, not a claim, and no verdict is ever read off
one. Where a count and a curve disagree the lesson says why.

THE COUNTER CONVENTION, fixed here before the first kit is written. 109 modes
built on 14 conventions is the failure `labs/__init__.py` warns about, so there
is one:

    a routine that RUNS an algorithm returns  { result, counts, trace }
    a routine that COMPUTES a quantity returns that quantity

`result` is the answer (an array, a tree, a number, a rational). `counts` is a
flat object of integers, from a fixed vocabulary so two kits' panels line up:

    compares  swaps  moves  probes  hops  finds  unions  pushes  pops
    relaxations  nodes  calls  reads  writes  cells  rounds

`trace` is the array of steps a panel steps through, each step a plain object
whose `at` field says where it happened. `runOf` in COUNT_JS builds the shape
and is the only place it is spelled, so a kit cannot drift from it by accident.

HOW THIS RELATES TO THE TWO SHIPPED BLOCKS. `algorithms.ALGO_JS` and
`graph.GRAPH_JS` stay exactly where they are; the Discrete Mathematics pages
that render through them are not touched by anything here.

  Reused from ALGO_JS as it ships: `mergeSort`, whose comparison total is the
  baseline `heap.heapsort` and `sortkit.select` are measured against, and
  `ilog2`, in four blocks.

  NOT reused, and two of these were claimed in the design:
    `drawSeries`   is not in the pure block at all. It is inside
                   `algorithm_lab`, closed over the `alPlot` element, so it
                   cannot be concatenated. SERIES_JS below is its replacement,
                   with the element passed in.
    `makeArray`'s  'shuffle' is ONE fixed permutation, produced by
                   idx = (idx + 7) % length, and takes no seed. The five modes
                   that need a seeded stream take it from SEEDED_JS over
                   `sysdesign_core.lcgStream`.
    `binarySearch` returns the NUMBER OF COMPARISONS an exact-match search
                   made -- not an index, and nothing at all when the target is
                   absent. `dpkit.wis`'s p(j) and `dpkit.lis`'s tails both need
                   the insertion POSITION of a value that is not in the array,
                   which is a different function. Both are written out in
                   DP_JS, counted where the comparisons happen. This is the
                   same shape of defect as the `drawSeries` claim and it was
                   found the same way: by trying to call it.
    `insertionSort` likewise returns a total and no sorted output, so it cannot
                   serve as a hybrid sort's cutoff arm. SORT_JS has its own.

  Reused from GRAPH_JS as it ships, as INDEPENDENT ORACLES rather than as
  machinery: `cuts()` finds bridges and cut vertices by deleting each edge and
  recounting components, which is the right thing to check `lowLink` against;
  `kruskal()`, `dijkstra()` and `hamilton()` answer the same questions as
  `kruskalRun`, `relaxRun` and `hamiltonBrute` by a different route. Where a
  routine here and one there answer the same question, mathcheck asserts they
  agree.

  NOT reused: the representation. `GRAPH_JS.link(M, i, j)` writes both `M[i][j]`
  and `M[j][i]` and `edges()` scans `i < j`, so it is undirected BY
  CONSTRUCTION; its weight is a function of the endpoints, `((7i + 13j) mod 9)
  + 1`, so it is never negative and never reader-set; it carries no capacity;
  and N is capped at 8. DFS edge classification, topological order, strongly
  connected components, Bellman-Ford and every flow network need all four of
  those to be false. DIGRAPH_JS is the representation that makes them true, and
  `dgFromMatrix` reads a GRAPH_JS preset into it so a lesson can open on a graph
  the reader already met in Discrete Mathematics.

THE BLOCKS. Seven shared, then fourteen -- one per kit, in the order of the
design's §4.1-§4.14. A kit concatenates only the blocks it needs, which is why
they are separate: a page that shipped the whole core would carry twelve
courses of algorithms to show one heap, and 62 KB gzipped is this repository's
measured ceiling (AGENTS.md).

    COUNT_JS     the { result, counts, trace } shape and a counter
    RFIXED_JS    a rational as a decimal, by BigInt long division. Several
                 quantities here -- the exact Bloom rate, the all-distinct
                 product, a contraction probability -- have denominators past
                 10^300, where algebra_core's Rdec returns NaN
    SERIES_JS    measured against predicted, as SVG, element passed in
    DIGRAPH_JS   directed, weighted (negative allowed), capacitated graphs,
                 their renderer, and the GRAPH_JS adapter
    TREEDRAW_JS  a tree renderer, generic over the node type. Six kinds of tree
                 are drawn on this path and each was about to be a helper
                 closed over its own lab's element
    SEEDED_JS    the seeded stream, over sysdesign_core's lcgStream: MINSTD
                 parameters and a splitmix64-mixed seed, for the five modes
                 whose draws are consumed as x % n
    ORACLE_JS    exhaustive optima, each with its instance cap as a parameter
                 and a refusal above it. Only the ones more than one kit needs
                 are here; a single-kit oracle lives in its kit and calls
                 `oracleCap` from this block, so the refusal is spelled once.

    SEQ_JS  HEAP_JS  HASH_JS  TREE_JS  SORT_JS  GRAPHKIT_JS  FLOW_JS
    GREEDY_JS  DP_JS  STRINGS_JS  GEOM_JS  RANDOM_JS  REDUCTION_JS  COPING_JS

Dependencies a kit must concatenate alongside:

    every block            COUNT_JS
    SEQ_JS, SORT_JS,
    GRAPHKIT_JS, GEOM_JS   ALGO_JS's `ilog2`
    HEAP_JS                RATIONAL_JS
    HASH_JS                RATIONAL_JS, RFIXED_JS, and sysdesign_core's
                           bloomApprox, logApprox, lcgStream for the labelled
                           columns
    TREE_JS                RATIONAL_JS, TREEDRAW_JS, and sysdesign_core's
                           logApprox for the 2 ln n reference curve
    SORT_JS                RATIONAL_JS, SEEDED_JS, ALGO_JS's mergeSort and
                           ilog2, and sysdesign_core.HARMONIC_JS -- quickExpected
                           is 2(n+1)H_n - 4n and H_n is `harmonic(n, 1)`, exact,
                           not rebuilt here
    GRAPHKIT_JS            DIGRAPH_JS, ORACLE_JS, ALGO_JS's ilog2
    FLOW_JS                DIGRAPH_JS
    GREEDY_JS              RATIONAL_JS, ORACLE_JS, TREEDRAW_JS, and
                           sysdesign_core.REPLAY_JS -- `caching` is
                           replayPolicy and nothing else
    DP_JS                  ORACLE_JS and counting.BIGINT_JS
    STRINGS_JS             nothing, though a kit drawing the trie wants
                           TREEDRAW_JS and `trieKids` from this block
    GEOM_JS                nothing (every figure is a BigInt integer)
    RANDOM_JS              RATIONAL_JS, RFIXED_JS, SEEDED_JS, DIGRAPH_JS,
                           ORACLE_JS
    REDUCTION_JS           DIGRAPH_JS and ORACLE_JS
    COPING_JS              RATIONAL_JS, DIGRAPH_JS, ORACLE_JS, GRAPHKIT_JS (for
                           primRun), GREEDY_JS (for fractionalKnapsack),
                           sysdesign_core's HARMONIC_JS for the H_n * OPT bound
                           and the charges, and RCEIL_JS for the FPTAS's floor

The blocks are raw strings so `scripts/mathcheck.js` executes the SHIPPED
source rather than a transcription of it. Anything mathcheck needs to call is a
top-level function that takes what it works on as an argument -- including the
three drawing blocks, whose entire reason for existing is that the repository's
previous drawing helpers were closed over a DOM element and therefore could
not be tested, reused, or shown to be right. The rule that makes them shared is
narrow and worth stating: the function that BUILDS the markup takes the thing
it draws and returns a string, and the function that installs it takes the
element as its FIRST argument and may be handed null.
"""

# ------------------------------------------------------------ the convention

COUNT_JS = r"""
  /* The one shape. See the module docstring: a routine that RUNS an algorithm
     returns { result, counts, trace }, and this is the only place that object
     is spelled, so a kit cannot invent a second convention by accident. */
  function runOf(result, counts, trace) {
    return { result: result, counts: counts || {}, trace: trace || [] };
  }
  /* A counter with a fixed vocabulary. bump() on an unknown key still works --
     refusing would turn a panel into a crash -- but the vocabulary is what the
     panels are laid out from, so a new key is a decision, not a typo. */
  var COUNT_KEYS = ['compares', 'swaps', 'moves', 'probes', 'hops', 'finds',
    'unions', 'pushes', 'pops', 'relaxations', 'nodes', 'calls', 'reads',
    'writes', 'cells', 'rounds'];
  function counter() {
    var c = {};
    for (var i = 0; i < COUNT_KEYS.length; i += 1) c[COUNT_KEYS[i]] = 0;
    return c;
  }
  /* Drop the keys that stayed zero: a panel showing "swaps 0" for an algorithm
     that cannot swap is noise, and the reader cannot tell it from a bug. */
  function usedCounts(c) {
    var out = {};
    Object.keys(c).forEach(function (k) { if (c[k]) out[k] = c[k]; });
    return out;
  }
"""


# ------------------------------------------------------ printing a rational

RFIXED_JS = r"""
  /* A rational as a decimal string, by BigInt long division.

     algebra_core's Rdec goes through Rnum, which is Number(a.n) / Number(a.d),
     and several quantities on this path do not survive that: the exact Bloom
     rate at m = 1000, n = 100, k = 7 is a fraction whose denominator is
     1000^700, so both halves become Infinity and the page prints NaN. Karger's
     exact success probability and the all-distinct product in ballsExact have
     the same shape. So the decimal is produced by dividing the BigInts, which
     works at any size, and it ROUNDS HALF UP at the last place kept -- the only
     rounding in this block, and it is a rounding of the PRINTING, not of the
     number: Rtext still gives the exact fraction and the lesson prints both
     where the fraction is short enough to read.

     The System Design kits each carry their own copy of this function. This is
     the Algorithms path's one copy, and it is deliberately the same name and
     the same behaviour, so a reader moving between subjects reads one format. */
  function Rfixed(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }
  /* A rational too small to read as a decimal, as "1 in N" -- which is how a
     false-positive rate and a failure probability are quoted in practice. */
  function RoneIn(a) {
    if (Rzero(a)) return 'never';
    var inv = Rinv(a);
    return '1 in ' + Rfixed(inv, inv.d === 1n ? 0 : 1);
  }
"""


# ------------------------------------------------------- measured vs predicted

SERIES_JS = r"""
  /* Measured against predicted, drawn.

     This is `drawSeries` from algorithms.py, lifted out of `algorithm_lab` and
     given the element as an argument. The original assigned to `plot`, an
     element it had closed over, so it could not be called from another lab, and
     could not be called from a test at all. Here the function that BUILDS the
     markup and the function that installs it are separate: seriesSvg returns a
     string and touches nothing, drawSeries hands that string to an element.
     Every assertion mathcheck makes about a drawing is an assertion about the
     string.

     A series is { label, values, colour, dashed, points }. `dashed` is for a
     predicted bound and `points` marks the measured samples, because the whole
     figure on this path is one measured curve against one predicted one, and
     two solid lines of different colours do not say which is which.

     The geometry is the shipped one -- x from 26 to 496, baseline at 200, 180
     tall -- so a page that swaps this in for the old helper draws the same
     picture. */
  var SERIES_BOX = { left: 26, right: 496, base: 200, top: 14 };

  function seriesMax(series) {
    var m = 0;
    series.forEach(function (s) {
      s.values.forEach(function (v) { if (isFinite(v) && v > m) m = v; });
    });
    return m > 0 ? m : 1;
  }

  /* The scale, returned as functions so a kit can place its own annotations on
     the same axes rather than guessing at them. */
  function seriesScale(series, xs, opts) {
    opts = opts || {};
    var box = opts.box || SERIES_BOX;
    var maxY = opts.maxY || seriesMax(series);
    var log = !!opts.log;
    var span = box.base - box.top;
    return {
      box: box, maxY: maxY, log: log, n: xs.length,
      x: function (i) {
        return box.left + (i / Math.max(1, xs.length - 1)) * (box.right - box.left);
      },
      y: function (v) {
        if (!isFinite(v)) return box.top - 8;          /* off the top, deliberately */
        if (log) {
          var lv = Math.log10(Math.max(v, 1)), lm = Math.log10(Math.max(maxY, 10));
          return box.base - (lv / lm) * span;
        }
        return box.base - (v / maxY) * span;
      }
    };
  }

  function seriesPath(sc, values) {
    return values.map(function (v, i) {
      return (i ? 'L' : 'M') + sc.x(i).toFixed(1) + ' ' + sc.y(v).toFixed(1);
    }).join(' ');
  }

  /* Endpoint labels, separated so two curves that end close together are both
     readable. Lifted with the shipped helper's logic intact: sort by where the
     curve ends, push each down to clear the one above, then pull the tail back
     up so the last one stays inside the box. */
  function seriesLabelRows(series, sc) {
    var rows = series.map(function (ser, i) {
      var last = ser.values[ser.values.length - 1];
      return { series: ser, order: i,
               baseline: Math.max(20, Math.min(sc.box.base - 12, sc.y(last) - 6)) };
    }).sort(function (a, b) { return a.baseline - b.baseline || a.order - b.order; });
    rows.forEach(function (r, i) {
      if (i) r.baseline = Math.max(r.baseline, rows[i - 1].baseline + 18);
    });
    for (var i = rows.length - 1; i >= 0; i -= 1) {
      rows[i].baseline = Math.min(rows[i].baseline,
        i === rows.length - 1 ? sc.box.base - 12 : rows[i + 1].baseline - 18);
    }
    return rows;
  }

  function seriesSvg(series, xs, opts) {
    opts = opts || {};
    var sc = seriesScale(series, xs, opts), b = sc.box;
    var s = '<line x1="' + b.left + '" y1="' + b.base + '" x2="' + (b.right + 4) + '" y2="' + b.base
          + '" stroke="var(--line-strong)" />'
          + '<line x1="' + b.left + '" y1="' + b.top + '" x2="' + b.left + '" y2="' + b.base
          + '" stroke="var(--line-strong)" />';
    series.forEach(function (ser) {
      s += '<path d="' + seriesPath(sc, ser.values) + '" fill="none" stroke="' + ser.colour
        + '" stroke-width="' + (ser.dashed ? 2 : 2.4) + '" opacity="0.9"'
        + (ser.dashed ? ' stroke-dasharray="6 4"' : '') + ' />';
      if (ser.points) {
        ser.values.forEach(function (v, i) {
          if (!isFinite(v)) return;
          s += '<circle cx="' + sc.x(i).toFixed(1) + '" cy="' + sc.y(v).toFixed(1)
            + '" r="2.6" fill="' + ser.colour + '" />';
        });
      }
    });
    seriesLabelRows(series, sc).forEach(function (row) {
      s += '<text x="' + (sc.x(xs.length - 1) - 6).toFixed(1) + '" y="' + row.baseline.toFixed(1)
        + '" text-anchor="end" font-size="12" font-weight="700" fill="' + row.series.colour
        + '">' + row.series.label + '</text>';
    });
    var tag = opts.xlabel === undefined ? 'n' : opts.xlabel;
    s += '<text x="' + b.left + '" y="' + (b.base + 16) + '" font-size="12" fill="var(--muted)">'
      + tag + ' = ' + xs[0] + '</text>';
    s += '<text x="' + (b.right + 4) + '" y="' + (b.base + 16)
      + '" text-anchor="end" font-size="12" fill="var(--muted)">' + tag + ' = ' + xs[xs.length - 1] + '</text>';
    if (sc.log) s += '<text x="' + (b.left + 4) + '" y="' + (b.top + 10)
      + '" font-size="12" fill="var(--muted)">log scale</text>';
    return s;
  }

  /* The element is the FIRST argument and may be null, which is what makes the
     helper shared. Returns the markup either way. */
  function drawSeries(el, series, xs, opts) {
    var s = seriesSvg(series, xs, opts);
    if (el) el.innerHTML = s;
    return s;
  }

  /* Sample a predicted curve on the same x values as a measured one. The curve
     is a drawing: it is evaluated at double precision and nothing is decided
     from it. */
  function predicted(xs, f) { return xs.map(function (n) { return f(n); }); }
"""


# ------------------------------------------- directed, weighted, capacitated

DIGRAPH_JS = r"""
  /* THE REPRESENTATION, and why it is an arc LIST and not a matrix.

     `GRAPH_JS` is a symmetric 0/1 matrix whose weight is a function of the
     endpoints. Four courses here need something it cannot express, and each of
     the four is a different failure of the same choice:

       direction    link(M,i,j) writes M[i][j] AND M[j][i]; edges() scans i<j.
                    A tree edge and a back edge are the same entry, so DFS edge
                    classification, topological order and SCCs have nothing to
                    read.
       sign         w(i,j) = ((7i+13j) mod 9) + 1 is never negative and never
                    the reader's. Bellman-Ford's whole subject is the weight
                    the reader makes negative.
       capacity     there is no second number on an edge at all.
       multiplicity a matrix holds one entry per pair, and a flow network holds
                    u->v and v->u at once, a gadget's vertex split produces two
                    arcs between the same pair, and a residual graph is built
                    by pairing each arc with its reverse.

     So: an ARC LIST with an index built on demand. An arc is
     { u, v, w, cap } and its id is its position in G.arcs. Identity is the
     point -- the residual network names an arc's reverse by id, which a triple
     [i, j, w] cannot do once two arcs share endpoints -- and the honest E that
     every "operations against E log V" panel prints is G.arcs.length.

     G = { n, directed, arcs: [{u, v, w, cap}] }. `directed: false` means each
     arc is traversable both ways but STORED ONCE, so |E| is arcs.length and
     Kruskal iterates arcs rather than half a matrix.

     WEIGHTS ARE NUMBERS, NOT BIGINT, AND THAT IS EXACT. Every weight is an
     integer the reader typed and every distance is a sum of at most n of them:
     at this path's caps (n <= 16, |w| <= 9999) no quantity here exceeds 160000,
     which a double holds exactly, and integer addition of exactly-held integers
     is exact. BigInt would buy nothing and would make the unreachable sentinel
     awkward -- which is `null`, not Infinity, because `Infinity + w` compares
     as reachable and that defect is how a Bellman-Ford lab reports a path
     through a vertex it never reached.

     An arc id is stable for the life of the graph. dgRemove is the one
     exception and it says so; nothing that keeps ids across a call (flow,
     residual, augmenting) ever edits. */

  function dgNew(n, directed) {
    return { n: n, directed: directed === undefined ? true : !!directed, arcs: [] };
  }
  function dgAdd(G, u, v, w, cap) {
    G.arcs.push({ u: u, v: v, w: w === undefined ? 1 : w, cap: cap === undefined ? 0 : cap });
    return G.arcs.length - 1;
  }
  function dgSetWeight(G, id, w) { G.arcs[id].w = w; return G; }
  function dgSetCap(G, id, cap) { G.arcs[id].cap = cap; return G; }
  /* Splices, so ids after `id` shift down by one. The only mutator that does. */
  function dgRemove(G, id) { G.arcs.splice(id, 1); return G; }
  function dgCopy(G) {
    return { n: G.n, directed: G.directed,
             arcs: G.arcs.map(function (a) { return { u: a.u, v: a.v, w: a.w, cap: a.cap }; }) };
  }

  /* out[v] and inn[v] are arrays of arc ids. On an undirected graph an arc is
     in both lists of both endpoints, which is what "traversable both ways,
     stored once" means. */
  function dgIndex(G) {
    var out = [], inn = [], i;
    for (i = 0; i < G.n; i += 1) { out.push([]); inn.push([]); }
    for (i = 0; i < G.arcs.length; i += 1) {
      var a = G.arcs[i];
      out[a.u].push(i); inn[a.v].push(i);
      if (!G.directed) { out[a.v].push(i); inn[a.u].push(i); }
    }
    return { out: out, inn: inn };
  }
  /* The endpoint reached from `from` along arc id. */
  function dgOther(G, id, from) {
    var a = G.arcs[id];
    return a.u === from ? a.v : a.u;
  }
  /* Neighbours as {id, to, w, cap, forward}, in arc order -- deterministic, so
     two readers at the same graph see the same traversal. */
  function dgOut(G, v, idx) {
    idx = idx || dgIndex(G);
    return idx.out[v].map(function (id) {
      var a = G.arcs[id];
      return { id: id, to: dgOther(G, id, v), w: a.w, cap: a.cap, forward: a.u === v };
    });
  }
  function dgOutdeg(G, v, idx) { return (idx || dgIndex(G)).out[v].length; }
  function dgIndeg(G, v, idx) { return (idx || dgIndex(G)).inn[v].length; }
  function dgFind(G, u, v) {
    for (var i = 0; i < G.arcs.length; i += 1) {
      var a = G.arcs[i];
      if (a.u === u && a.v === v) return i;
      if (!G.directed && a.u === v && a.v === u) return i;
    }
    return -1;
  }
  /* Every arc flipped: Kosaraju's second pass, and nothing else. */
  function dgReverse(G) {
    var H = dgNew(G.n, G.directed);
    G.arcs.forEach(function (a) { dgAdd(H, a.v, a.u, a.w, a.cap); });
    return H;
  }
  /* The weight matrix Floyd-Warshall fills: null off the graph, 0 on the
     diagonal, the LIGHTEST arc where several run between the same pair. */
  function dgWeightMatrix(G) {
    var W = [], i, j;
    for (i = 0; i < G.n; i += 1) { W.push([]); for (j = 0; j < G.n; j += 1) W[i].push(i === j ? 0 : null); }
    G.arcs.forEach(function (a) {
      if (W[a.u][a.v] === null || a.w < W[a.u][a.v]) W[a.u][a.v] = a.w;
      if (!G.directed && (W[a.v][a.u] === null || a.w < W[a.v][a.u])) W[a.v][a.u] = a.w;
    });
    return W;
  }
  /* THE ADAPTER, both ways.

     dgFromMatrix reads a GRAPH_JS adjacency matrix -- any of its eight presets,
     or a lesson's own example through PRESETS.lesson -- into this
     representation, so a lesson can open on a graph the reader already met in
     Discrete Mathematics. `wfn(i, j)` is GRAPH_JS's `weight` when the formula
     weights are wanted and the reader's own function when they are not.
     `directed: true` orients each edge i -> j with i < j, which is the
     orientation the DFS-classification lesson opens on.

     dgToMatrix goes the other way, and exists for exactly one reason: it hands
     a graph built here to GRAPH_JS's brute-force routines, so `cuts()`,
     `kruskal()`, `dijkstra()` and `hamilton()` can answer the same question by
     a different route and the two answers can be asserted equal. */
  function dgFromMatrix(M, n, wfn, directed) {
    var G = dgNew(n, directed), i, j;
    for (i = 0; i < n; i += 1) for (j = i + 1; j < n; j += 1) {
      if (M[i][j]) dgAdd(G, i, j, wfn ? wfn(i, j) : 1, 0);
    }
    return G;
  }
  function dgToMatrix(G) {
    var M = [], i, j;
    for (i = 0; i < G.n; i += 1) { M.push([]); for (j = 0; j < G.n; j += 1) M[i].push(0); }
    G.arcs.forEach(function (a) { if (a.u !== a.v) { M[a.u][a.v] = 1; M[a.v][a.u] = 1; } });
    return M;
  }
  /* A lesson's worked example, in the 1-BASED labels the prose uses, exactly as
     GRAPH_JS.lessonFrom takes them: [u, v] or [u, v, w] or [u, v, w, cap]. */
  function dgFromLesson(n, list, directed) {
    var G = dgNew(n, directed);
    (list || []).forEach(function (e) {
      dgAdd(G, e[0] - 1, e[1] - 1, e.length > 2 ? e[2] : 1, e.length > 3 ? e[3] : 0);
    });
    return G;
  }
  /* Undirected components, by arc traversal. Used by the spanning-tree oracle
     and by every "is it still connected" question. */
  function dgComponents(G, skipArc) {
    var idx = dgIndex(G), seen = new Array(G.n).fill(false), comps = [], s;
    for (s = 0; s < G.n; s += 1) {
      if (seen[s]) continue;
      var stack = [s], comp = [];
      seen[s] = true;
      while (stack.length) {
        var v = stack.pop();
        comp.push(v);
        idx.out[v].concat(idx.inn[v]).forEach(function (id) {
          if (skipArc !== undefined && id === skipArc) return;
          var u = dgOther(G, id, v);
          if (!seen[u]) { seen[u] = true; stack.push(u); }
        });
      }
      comps.push(comp.sort(function (a, b) { return a - b; }));
    }
    return comps;
  }

  /* ------------------------------------------------------- the drawing.

     GRAPH_JS's renderer is `positions`, `draw` and `paintMatrix` inside
     `graph_lab`, closed over the gPlot and gMatrix elements. Six modes across
     two kits here draw a graph, so this is the single largest piece of shared
     UI the Subject needs, and it is built the way SERIES_JS is: the function
     that makes the markup takes a graph and returns a string, and the function
     that installs it takes the element first.

     Two things the undirected renderer never had to do. An arc needs an
     ARROWHEAD, placed at the node's rim rather than its centre, or the reader
     cannot see which way a back edge points. And ANTIPARALLEL arcs -- which a
     residual network has at every augmentation -- must both be visible, so
     when u->v and v->u both exist each is bowed to its own side. Drawn
     straight they would lie on top of each other and the reverse arc, which is
     the entire idea of the residual network, would be invisible. */
  var DG_R = 17;
  function dgLayout(n, opts) {
    opts = opts || {};
    var cx = opts.cx === undefined ? 230 : opts.cx, cy = opts.cy === undefined ? 150 : opts.cy;
    var rad = opts.radius === undefined ? 105 : opts.radius, pts = [];
    for (var i = 0; i < n; i += 1) {
      var ang = -Math.PI / 2 + (2 * Math.PI * i) / n;
      pts.push([cx + rad * Math.cos(ang), cy + rad * Math.sin(ang)]);
    }
    return pts;
  }
  /* Left column / right column, for a bipartite matching or a flow network
     where source and sink belong at the ends. */
  function dgLayered(n, layers, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 460 : opts.width, h = opts.height === undefined ? 280 : opts.height;
    var cols = [], pts = new Array(n), i;
    layers.forEach(function (L, k) { cols[k] = L; });
    cols.forEach(function (L, k) {
      L.forEach(function (v, j) {
        pts[v] = [30 + (cols.length === 1 ? w / 2 : (k / (cols.length - 1)) * (w - 60)),
                  30 + (L.length === 1 ? (h - 60) / 2 : (j / (L.length - 1)) * (h - 60))];
      });
    });
    for (i = 0; i < n; i += 1) if (!pts[i]) pts[i] = [30, 30];
    return pts;
  }
  var DG_PALETTE = ['var(--cyan)', 'var(--purple)', 'var(--amber)', 'var(--green)',
                    'var(--red)', 'var(--blue)'];

  function dgArrow(x1, y1, x2, y2, colour) {
    var dx = x2 - x1, dy = y2 - y1, len = Math.sqrt(dx * dx + dy * dy) || 1;
    var ux = dx / len, uy = dy / len;
    var tipx = x2 - ux * DG_R, tipy = y2 - uy * DG_R;
    var bx = tipx - ux * 9, by = tipy - uy * 9;
    return '<polygon points="' + tipx.toFixed(1) + ',' + tipy.toFixed(1) + ' '
      + (bx - uy * 4.2).toFixed(1) + ',' + (by + ux * 4.2).toFixed(1) + ' '
      + (bx + uy * 4.2).toFixed(1) + ',' + (by - ux * 4.2).toFixed(1)
      + '" fill="' + colour + '" />';
  }

  /* opts: { points, highlight: [arc ids], colours: [per vertex], labels,
             label: 'w' | 'cap' | 'flow' | 'none', flow: [per arc] } */
  function dgSvg(G, opts) {
    opts = opts || {};
    var pts = opts.points || dgLayout(G.n, opts);
    var hi = {};
    (opts.highlight || []).forEach(function (id) { hi[id] = true; });
    var mode = opts.label === undefined ? (G.arcs.some(function (a) { return a.cap; }) ? 'cap' : 'w') : opts.label;
    var pairs = {}, s = '';
    G.arcs.forEach(function (a) { pairs[a.u + '>' + a.v] = true; });
    G.arcs.forEach(function (a, id) {
      var p = pts[a.u], q = pts[a.v];
      var on = hi[id], colour = on ? 'var(--cyan)' : 'var(--line-strong)';
      /* bow when the reverse arc exists too, so neither hides the other */
      var bow = G.directed && pairs[a.v + '>' + a.u] ? 1 : 0;
      var mx = (p[0] + q[0]) / 2, my = (p[1] + q[1]) / 2;
      if (bow) {
        var dx = q[0] - p[0], dy = q[1] - p[1], L = Math.sqrt(dx * dx + dy * dy) || 1;
        mx -= (dy / L) * 22; my += (dx / L) * 22;
        s += '<path d="M' + p[0].toFixed(1) + ' ' + p[1].toFixed(1) + ' Q' + mx.toFixed(1) + ' '
          + my.toFixed(1) + ' ' + q[0].toFixed(1) + ' ' + q[1].toFixed(1) + '" fill="none" stroke="'
          + colour + '" stroke-width="' + (on ? 3.4 : 1.8) + '" />';
      } else {
        s += '<line x1="' + p[0].toFixed(1) + '" y1="' + p[1].toFixed(1) + '" x2="' + q[0].toFixed(1)
          + '" y2="' + q[1].toFixed(1) + '" stroke="' + colour + '" stroke-width="'
          + (on ? 3.4 : 1.8) + '" />';
      }
      if (G.directed) {
        var fromx = bow ? mx : p[0], fromy = bow ? my : p[1];
        s += dgArrow(fromx, fromy, q[0], q[1], colour);
      }
      if (mode !== 'none') {
        var text = mode === 'cap' ? String(a.cap)
          : mode === 'flow' ? ((opts.flow ? opts.flow[id] : 0) + '/' + a.cap)
          : String(a.w);
        var lx = bow ? (p[0] + 2 * mx + q[0]) / 4 : mx, ly = bow ? (p[1] + 2 * my + q[1]) / 4 : my;
        s += '<circle cx="' + lx.toFixed(1) + '" cy="' + ly.toFixed(1)
          + '" r="' + (text.length > 3 ? 12 : 9) + '" fill="var(--panel-solid)" stroke="var(--line)" />';
        s += '<text x="' + lx.toFixed(1) + '" y="' + (ly + 4).toFixed(1)
          + '" text-anchor="middle" font-size="10" font-weight="700" fill="'
          + (on ? 'var(--cyan)' : 'var(--muted)') + '">' + text + '</text>';
      }
    });
    for (var i = 0; i < G.n; i += 1) {
      var c = opts.colours && opts.colours[i] !== undefined && opts.colours[i] !== -1
        ? DG_PALETTE[opts.colours[i] % DG_PALETTE.length] : 'var(--panel-3)';
      s += '<circle cx="' + pts[i][0].toFixed(1) + '" cy="' + pts[i][1].toFixed(1) + '" r="' + DG_R
        + '" fill="' + c + '" stroke="var(--line-strong)" stroke-width="2" />';
      var label = opts.labels && opts.labels[i] !== undefined ? opts.labels[i] : (i + 1);
      s += '<text x="' + pts[i][0].toFixed(1) + '" y="' + (pts[i][1] + 5).toFixed(1)
        + '" text-anchor="middle" font-size="13" font-weight="800" fill="'
        + (opts.colours && opts.colours[i] !== undefined && opts.colours[i] !== -1
            ? 'var(--on-accent)' : 'var(--text)') + '">' + label + '</text>';
    }
    return s;
  }
  function drawGraph(el, G, opts) {
    var s = dgSvg(G, opts);
    if (el) el.innerHTML = s;
    return s;
  }

  /* A matrix as a table, for the adjacency, the Floyd tables and the DP grids.
     cell(i, j, v) may return a string, so a lesson can put its own mark in a
     cell without a second painter. */
  function matrixHtml(M, opts) {
    opts = opts || {};
    var head = opts.cols || M[0].map(function (_, j) { return j + 1; });
    var side = opts.rows || M.map(function (_, i) { return i + 1; });
    var h = (opts.caption ? '<caption>' + opts.caption + '</caption>' : '') + '<thead><tr><th></th>';
    head.forEach(function (c) { h += '<th>' + c + '</th>'; });
    h += '</tr></thead><tbody>';
    M.forEach(function (row, i) {
      h += '<tr><th class="rowhead">' + side[i] + '</th>';
      row.forEach(function (v, j) {
        var text = opts.cell ? opts.cell(i, j, v) : (v === null ? '&mdash;' : String(v));
        h += '<td class="' + (opts.on && opts.on(i, j, v) ? 'on' : '') + '" data-i="' + i
          + '" data-j="' + j + '">' + text + '</td>';
      });
      h += '</tr>';
    });
    return h + '</tbody>';
  }
  function paintMatrix(el, M, opts) {
    var h = matrixHtml(M, opts);
    if (el) el.innerHTML = h;
    return h;
  }
"""


# ------------------------------------------------- exhaustive, with a cap

ORACLE_JS = r"""
  /* Brute force, with the instance cap as a parameter and a REFUSAL above it.

     Nearly every mode in courses 4, 9 and the reduction course compares an
     algorithm against the true optimum, and the true optimum is an exhaustive
     search. A silent slow path is the wrong shape for that: at n = 22 a subset
     enumeration is forty seconds of a frozen tab, and the reader's conclusion
     is that the lesson is broken rather than that the instance is too big --
     which is itself the lesson of the course. So every routine here throws, the
     kit catches, and the panel says how big an instance it can answer for.

     Only the oracles MORE THAN ONE kit needs live here; a single-kit oracle
     lives in its own block and calls `oracleCap`, so the refusal is spelled
     once and a kit does not ship eight enumerations to use one.

         bruteOptimal            subsets, cap 16     greedy, coping
         knapsackBrute           items,   cap 12     greedy, coping
         tspBrute                cities,  cap 8      reduction, coping
         satBrute                vars,    cap 16     reduction, coping
         independentSetBrute     vertices,cap 16     reduction, coping
         vertexCoverBrute        vertices,cap 16     reduction, coping
         hamiltonBrute           vertices,cap 8      reduction

     The caps are the design's, and they are not arbitrary: 2^16 = 65 536
     assignments and 8! = 40 320 tours are each a few milliseconds, and the next
     step up is a second. */
  function oracleCap(what, size, cap) {
    if (size > cap) {
      throw new Error(what + ': ' + size + ' exceeds the exhaustive cap of ' + cap);
    }
    return size;
  }
  /* Every subset of {0..n-1} as a bitmask, in increasing mask order so the
     first optimum found is the lexicographically smallest -- a tie broken the
     same way twice is a tie a reader can reproduce. */
  function forEachSubset(n, fn) {
    var total = 1 << n;
    for (var mask = 0; mask < total; mask += 1) fn(mask);
  }
  function maskMembers(mask, n) {
    var out = [];
    for (var i = 0; i < n; i += 1) if (mask & (1 << i)) out.push(i);
    return out;
  }
  function popcount(mask) { var c = 0; while (mask) { mask &= mask - 1; c += 1; } return c; }

  /* The generic one: `objective(members)` returns null for an infeasible set
     and a number to MAXIMISE otherwise. Counts the subsets examined, because
     "2^n of them" is the figure the panel prints beside the greedy run's n. */
  function bruteOptimal(items, objective, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('bruteOptimal', items.length, cap);
    var best = null, bestSet = [], examined = 0, feasible = 0;
    forEachSubset(items.length, function (mask) {
      var members = maskMembers(mask, items.length);
      examined += 1;
      var v = objective(members);
      if (v === null || v === undefined) return;
      feasible += 1;
      if (best === null || v > best) { best = v; bestSet = members; }
    });
    return runOf({ value: best, members: bestSet },
                 { nodes: examined, calls: feasible }, []);
  }

  /* 0/1 knapsack, exactly. items are { w, v }. */
  function knapsackBrute(items, W, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('knapsackBrute', items.length, cap);
    var best = 0, bestSet = [], examined = 0;
    forEachSubset(items.length, function (mask) {
      var members = maskMembers(mask, items.length), wt = 0, val = 0;
      examined += 1;
      for (var i = 0; i < members.length; i += 1) { wt += items[members[i]].w; val += items[members[i]].v; }
      if (wt <= W && val > best) { best = val; bestSet = members; }
    });
    return runOf({ value: best, members: bestSet }, { nodes: examined }, []);
  }

  /* The shortest tour visiting every city once and returning to 0. D may be
     asymmetric; nothing here assumes the triangle inequality, which is what
     lets `coping.tsp` break its own 2-approximation on a non-metric instance. */
  function tspBrute(D, budget, cap) {
    cap = cap === undefined ? 8 : cap;
    var n = D.length;
    oracleCap('tspBrute', n, cap);
    var best = null, bestTour = null, examined = 0;
    var used = new Array(n).fill(false), tour = [0];
    used[0] = true;
    (function walk(at, len) {
      if (tour.length === n) {
        examined += 1;
        var total = len + D[at][0];
        if (best === null || total < best) { best = total; bestTour = tour.slice(); }
        return;
      }
      for (var v = 1; v < n; v += 1) {
        if (used[v]) continue;
        used[v] = true; tour.push(v);
        walk(v, len + D[at][v]);
        tour.pop(); used[v] = false;
      }
    })(0, 0);
    return runOf({ length: best, tour: bestTour,
                   withinBudget: budget === undefined ? null : (best !== null && best <= budget) },
                 { nodes: examined }, []);
  }

  /* CNF: { n, clauses: [[lit, ...]] }, a literal being a signed 1-based
     variable index -- 3 is x3, -3 is NOT x3. An assignment is an array of
     booleans indexed from 0. */
  function satEval(formula, assign) {
    var sat = 0;
    for (var c = 0; c < formula.clauses.length; c += 1) {
      var cl = formula.clauses[c], ok = false;
      for (var k = 0; k < cl.length; k += 1) {
        var lit = cl[k], v = assign[Math.abs(lit) - 1];
        if (lit > 0 ? v : !v) { ok = true; break; }
      }
      if (ok) sat += 1;
    }
    return sat;
  }
  function maskAssign(mask, n) {
    var a = [];
    for (var i = 0; i < n; i += 1) a.push(!!(mask & (1 << i)));
    return a;
  }
  function satBrute(formula, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('satBrute', formula.n, cap);
    var models = [], examined = 0, first = null;
    forEachSubset(formula.n, function (mask) {
      examined += 1;
      var a = maskAssign(mask, formula.n);
      if (satEval(formula, a) === formula.clauses.length) {
        models.push(mask);
        if (first === null) first = a;
      }
    });
    return runOf({ satisfiable: models.length > 0, model: first, models: models.length },
                 { nodes: examined }, []);
  }

  /* Independent sets and vertex covers on a DIGRAPH_JS graph, read
     undirected -- both problems ignore direction, and the reduction course
     needs them to agree with each other on the same instance, which is the
     complement identity |S| + |C| = V it is there to show. */
  function dgAdjacency(G) {
    var adj = [], i;
    for (i = 0; i < G.n; i += 1) adj.push(new Array(G.n).fill(false));
    G.arcs.forEach(function (a) { if (a.u !== a.v) { adj[a.u][a.v] = true; adj[a.v][a.u] = true; } });
    return adj;
  }
  function independentSetBrute(G, k, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('independentSetBrute', G.n, cap);
    var adj = dgAdjacency(G), best = [], examined = 0, atK = null;
    forEachSubset(G.n, function (mask) {
      examined += 1;
      var m = maskMembers(mask, G.n), ok = true, i, j;
      for (i = 0; ok && i < m.length; i += 1)
        for (j = i + 1; j < m.length; j += 1) if (adj[m[i]][m[j]]) { ok = false; break; }
      if (!ok) return;
      if (m.length > best.length) best = m;
      if (k !== undefined && m.length >= k && atK === null) atK = m;
    });
    return runOf({ size: best.length, members: best, atLeastK: atK },
                 { nodes: examined }, []);
  }
  /* The largest set of MUTUALLY ADJACENT vertices -- written separately rather
     than as "an independent set in the complement", because the point of the
     complement lesson is that those two answers agree, and a check in which one
     routine is defined as the other checks nothing. GRAPH_JS.cliqueNumber()
     answers the same question a third way, and mathcheck asserts all three. */
  function cliqueBrute(G, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('cliqueBrute', G.n, cap);
    var adj = dgAdjacency(G), best = [], examined = 0;
    forEachSubset(G.n, function (mask) {
      examined += 1;
      var m = maskMembers(mask, G.n);
      if (m.length <= best.length) return;
      var ok = true, i, j;
      for (i = 0; ok && i < m.length; i += 1)
        for (j = i + 1; j < m.length; j += 1) if (!adj[m[i]][m[j]]) { ok = false; break; }
      if (ok) best = m;
    });
    return runOf({ size: best.length, members: best }, { nodes: examined }, []);
  }
  function vertexCoverBrute(G, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('vertexCoverBrute', G.n, cap);
    var adj = dgAdjacency(G), best = null, examined = 0;
    forEachSubset(G.n, function (mask) {
      examined += 1;
      if (best !== null && popcount(mask) >= best.length) return;
      var m = maskMembers(mask, G.n), inSet = new Array(G.n).fill(false), ok = true;
      m.forEach(function (v) { inSet[v] = true; });
      for (var i = 0; ok && i < G.arcs.length; i += 1) {
        var a = G.arcs[i];
        if (a.u !== a.v && !inSet[a.u] && !inSet[a.v]) ok = false;
      }
      if (ok && (best === null || m.length < best.length)) best = m;
    });
    return runOf({ size: best ? best.length : 0, members: best || [] }, { nodes: examined }, []);
  }

  /* A Hamilton path and circuit on a digraph, by exhaustive search -- the
     directed case GRAPH_JS.hamilton cannot answer. On an undirected graph the
     two must agree, and mathcheck asserts that they do. */
  function hamiltonBrute(G, cap) {
    cap = cap === undefined ? 8 : cap;
    oracleCap('hamiltonBrute', G.n, cap);
    var adj = [], i;
    for (i = 0; i < G.n; i += 1) adj.push(new Array(G.n).fill(false));
    G.arcs.forEach(function (a) {
      adj[a.u][a.v] = true;
      if (!G.directed) adj[a.v][a.u] = true;
    });
    var path = null, circuit = null, examined = 0;
    var used = new Array(G.n).fill(false), cur = [];
    (function walk() {
      if (cur.length === G.n) {
        examined += 1;
        if (!path) path = cur.slice();
        if (adj[cur[cur.length - 1]][cur[0]] && !circuit) circuit = cur.slice();
        return;
      }
      for (var v = 0; v < G.n; v += 1) {
        if (used[v]) continue;
        if (cur.length && !adj[cur[cur.length - 1]][v]) continue;
        used[v] = true; cur.push(v);
        walk();
        cur.pop(); used[v] = false;
        if (path && circuit) return;
      }
    })();
    return runOf({ path: path, circuit: circuit }, { nodes: examined }, []);
  }
"""


# --------------------------------------------------- 4.1 seqkit (course 1)

SEQ_JS = r"""
  /* Course 1's cost model, in the word RAM the lesson states: an array index
     costs 1 and reaching the i-th node of a list costs i + 1 hops. Every cost
     here is that model executed, not a complexity class quoted, which is why
     the table can disagree with the reader's expectation and be right.

     One vocabulary of operations serves all four modes, and a structure that
     cannot do an operation returns null rather than a large number. "Not
     supported" and "expensive" are different answers and a lab that conflated
     them would teach that a stack is a slow array. */
  var SEQ_OPS = ['index', 'search', 'insertFront', 'insertEnd', 'deleteAt', 'min'];
  var SEQ_STRUCTURES = {
    array: {
      label: 'dynamic array',
      index: function (n, at) { return 1; },
      search: function (n, at) { return n; },                    /* worst case: scan */
      insertFront: function (n, at) { return n + 1; },           /* shift every element */
      insertEnd: function (n, at) { return 1; },                 /* amortised; see ALGO_JS.dynamicArray */
      deleteAt: function (n, at) { return n - at; },
      min: function (n, at) { return n; }
    },
    sortedArray: {
      label: 'sorted array',
      index: function (n, at) { return 1; },
      search: function (n, at) { return ilog2(n) + 1; },         /* binary search */
      insertFront: null,                                          /* position is not the caller's to choose */
      insertEnd: null,
      deleteAt: function (n, at) { return n - at; },
      min: function (n, at) { return 1; }                        /* it is at the front */
    },
    list: {
      label: 'doubly-linked list',
      index: function (n, at) { return at + 1; },
      search: function (n, at) { return n; },
      insertFront: function (n, at) { return 1; },
      insertEnd: function (n, at) { return 1; },                 /* a tail pointer */
      deleteAt: function (n, at) { return at + 2; },             /* walk, then splice */
      min: function (n, at) { return n; }
    },
    stack: {
      label: 'stack',
      index: null, search: null,
      insertFront: null,
      insertEnd: function (n, at) { return 1; },                 /* push */
      deleteAt: null,
      min: null
    },
    queue: {
      label: 'queue (two stacks)',
      index: null, search: null,
      insertFront: null,
      insertEnd: function (n, at) { return 1; },
      deleteAt: null,
      min: null
    }
  };

  /* One operation sequence on one representation. ops are
     { op, at, key }; `at` is a 0-based position and defaults to the middle,
     which is the position the lesson's worked example uses. */
  function seqRun(ops, rep, n0) {
    var spec = SEQ_STRUCTURES[rep];
    if (!spec) throw new Error('unknown representation: ' + rep);
    var n = n0 === undefined ? 8 : n0, c = counter(), trace = [], total = 0;
    ops.forEach(function (o, i) {
      var at = o.at === undefined ? Math.floor(n / 2) : o.at;
      var f = spec[o.op];
      if (f === null || f === undefined) {
        trace.push({ at: i, op: o.op, cost: null, n: n, supported: false });
        return;
      }
      var cost = f(n, Math.min(at, Math.max(0, n - 1)));
      total += cost;
      if (o.op === 'index' || o.op === 'search' || o.op === 'min') c.reads += cost;
      else if (rep === 'list') c.hops += cost;
      else c.moves += cost;
      if (o.op.indexOf('insert') === 0) n += 1;
      if (o.op === 'deleteAt') n -= 1;
      trace.push({ at: i, op: o.op, cost: cost, n: n, supported: true });
    });
    return runOf({ total: total, size: n, label: spec.label }, usedCounts(c), trace);
  }
  function sortedArrayRun(ops, n0) { return seqRun(ops, 'sortedArray', n0); }

  /* The whole mix on all five, ranked, with "not supported" kept as its own
     answer. `mix` is { op: repetitions }. */
  function workloadRun(mix, n) {
    var ops = [];
    Object.keys(mix).forEach(function (op) {
      for (var i = 0; i < mix[op]; i += 1) ops.push({ op: op });
    });
    var rows = Object.keys(SEQ_STRUCTURES).map(function (rep) {
      var r = seqRun(ops, rep, n);
      var missing = ops.filter(function (o) { return !SEQ_STRUCTURES[rep][o.op]; })
                       .map(function (o) { return o.op; });
      var uniq = missing.filter(function (m, i) { return missing.indexOf(m) === i; });
      return { rep: rep, label: SEQ_STRUCTURES[rep].label, total: r.result.total,
               unsupported: uniq, usable: uniq.length === 0 };
    });
    var ranked = rows.filter(function (r) { return r.usable; })
                     .sort(function (a, b) { return a.total - b.total; });
    return runOf({ rows: rows, ranked: ranked, best: ranked.length ? ranked[0].rep : null },
                 { calls: ops.length }, []);
  }

  /* A queue from two stacks, and the CREDIT argument that bounds it.

     The unit of cost is one element touched: a push is 1, a transfer from the
     in stack to the out stack is 1, a pop is 1. So an element costs exactly 3
     over its whole life, no matter how the operations interleave, and the total
     is at most 3m for m enqueues -- which is the bound, evaluated rather than
     asserted. Each enqueue is charged 3 and spends 1, leaving 2 on the element
     to pay for its own transfer and its own pop; the balance in the trace is
     that bank, and the claim the lesson makes is that it never goes negative.

     Counting a transfer as 2 (a pop and a push) would be just as defensible and
     would make the bound 4m. The lesson states the 3, so this counts the 3. */
  function twoStackRun(ops) {
    var inS = [], outS = [], c = counter(), trace = [], total = 0, credits = 0, m = 0, out = [];
    ops.forEach(function (o, i) {
      var cost = 0, moved = 0, took = null;
      if (o.op === 'enqueue') {
        inS.push(o.key); cost = 1; c.pushes += 1; m += 1;
        credits += 3 - cost;
      } else {
        if (!outS.length) {
          while (inS.length) { outS.push(inS.pop()); moved += 1; c.moves += 1; }
          cost += moved;
        }
        if (outS.length) { took = outS.pop(); out.push(took); cost += 1; c.pops += 1; }
        credits -= cost;
      }
      total += cost;
      trace.push({ at: i, op: o.op, key: o.key, took: took, cost: cost, moved: moved,
                   total: total, credits: credits, bound: 3 * m });
    });
    return runOf({ total: total, bound: 3 * m, enqueues: m, order: out,
                   withinBound: total <= 3 * m,
                   creditsNeverNegative: trace.every(function (t) { return t.credits >= 0; }) },
                 usedCounts(c), trace);
  }

  /* Union-find, with the two improvements as independent switches, because the
     lesson's point is that either one alone is already good and the pair is
     what makes the bound flat. `rules` is { rank: bool, compress: bool }.
     Hops are counted per find, which is the figure the panel plots against
     the 2^r bound on a rank-r tree. */
  function unionFindRun(ops, rules, n) {
    rules = rules || {};
    var parent = [], rank = [], size = [], c = counter(), trace = [], i;
    for (i = 0; i < n; i += 1) { parent.push(i); rank.push(0); size.push(1); }
    function findWith(x) {
      var hops = 0, root = x;
      while (parent[root] !== root) { root = parent[root]; hops += 1; }
      if (rules.compress) {
        var cur = x;
        while (parent[cur] !== cur) { var next = parent[cur]; parent[cur] = root; cur = next; c.writes += 1; }
      }
      c.hops += hops; c.finds += 1;
      return { root: root, hops: hops };
    }
    ops.forEach(function (o, k) {
      if (o.op === 'find') {
        var f = findWith(o.a);
        trace.push({ at: k, op: 'find', a: o.a, root: f.root, hops: f.hops, parent: parent.slice() });
        return;
      }
      var ra = findWith(o.a), rb = findWith(o.b);
      if (ra.root === rb.root) {
        trace.push({ at: k, op: 'union', a: o.a, b: o.b, merged: false,
                     hops: ra.hops + rb.hops, parent: parent.slice() });
        return;
      }
      var x = ra.root, y = rb.root;
      if (rules.rank && rank[x] > rank[y]) { var t = x; x = y; y = t; }
      parent[x] = y; size[y] += size[x]; c.unions += 1; c.writes += 1;
      if (rules.rank && rank[x] === rank[y]) rank[y] += 1;
      else if (!rules.rank) rank[y] = Math.max(rank[y], rank[x] + 1);
      trace.push({ at: k, op: 'union', a: o.a, b: o.b, merged: true, root: y,
                   hops: ra.hops + rb.hops, parent: parent.slice() });
    });
    var maxRank = 0, maxSize = 0;
    for (i = 0; i < n; i += 1) {
      if (parent[i] === i) { maxRank = Math.max(maxRank, rank[i]); maxSize = Math.max(maxSize, size[i]); }
    }
    var worst = 0;
    trace.forEach(function (t) { if (t.hops > worst) worst = t.hops; });
    return runOf({ parent: parent, rank: rank, maxRank: maxRank, maxSize: maxSize,
                   bound: Math.pow(2, maxRank), worstHops: worst,
                   rankBoundHolds: maxSize >= Math.pow(2, maxRank) },
                 usedCounts(c), trace);
  }
"""


# ------------------------------------------ 4.2 heap (courses 1 and 2)

HEAP_JS = r"""
  /* Binary heaps as an array, 0-based: children of i are 2i+1 and 2i+2.

     Every routine takes the array and returns a NEW one, so a panel can show
     before and after side by side without a copy of its own. `max` selects a
     max-heap; heapsort wants one (it sorts ascending in place) and a k-way
     merge wants a min-heap, and having both is cheaper than explaining why the
     lesson's heap is upside down.

     Comparisons are counted where they happen -- one per sift step against the
     parent, one per child pair plus one against the winner on the way down --
     because the figure the lesson plots is that count against floor(log2 n),
     and an implementation that compared twice where it could compare once
     would draw a curve above the bound and teach that the bound is wrong. */
  function heapCmp(a, b, max) { return max ? a > b : a < b; }

  function heapInsert(heap, key, max) {
    var h = heap.slice(), c = counter(), trace = [];
    h.push(key);
    var i = h.length - 1;
    while (i > 0) {
      var p = (i - 1) >> 1;
      c.compares += 1;
      if (!heapCmp(h[i], h[p], max)) break;
      var t = h[i]; h[i] = h[p]; h[p] = t;
      c.swaps += 1;
      trace.push({ at: trace.length, from: i, to: p, heap: h.slice() });
      i = p;
    }
    return runOf({ heap: h, depth: trace.length }, usedCounts(c), trace);
  }

  function heapSiftDown(h, i, size, c, trace, max) {
    while (true) {
      var l = 2 * i + 1, r = l + 1, best = i;
      if (l < size) { c.compares += 1; if (heapCmp(h[l], h[best], max)) best = l; }
      if (r < size) { c.compares += 1; if (heapCmp(h[r], h[best], max)) best = r; }
      if (best === i) return;
      var t = h[i]; h[i] = h[best]; h[best] = t;
      c.swaps += 1;
      if (trace) trace.push({ at: trace.length, from: i, to: best, heap: h.slice(0, size) });
      i = best;
    }
  }
  function heapExtract(heap, max) {
    var h = heap.slice(), c = counter(), trace = [];
    if (!h.length) return runOf({ key: null, heap: h }, usedCounts(c), trace);
    var top = h[0], last = h.pop();
    if (h.length) { h[0] = last; heapSiftDown(h, 0, h.length, c, trace, max); }
    return runOf({ key: top, heap: h, depth: trace.length }, usedCounts(c), trace);
  }

  /* Floyd's build: sift down from the last internal node. The lesson's claim is
     that this is linear where n inserts are n log n, and both counts come from
     running both, on the same array. */
  function floydBuild(a, max) {
    var h = a.slice(), c = counter(), trace = [];
    for (var i = (h.length >> 1) - 1; i >= 0; i -= 1) {
      trace.push({ at: trace.length, root: i, heap: h.slice() });
      heapSiftDown(h, i, h.length, c, null, max);
    }
    return runOf({ heap: h }, usedCounts(c), trace);
  }
  function insertBuild(a, max) {
    var h = [], c = counter();
    a.forEach(function (k) {
      var r = heapInsert(h, k, max);
      h = r.result.heap;
      c.compares += r.counts.compares || 0;
      c.swaps += r.counts.swaps || 0;
    });
    return runOf({ heap: h }, usedCounts(c), []);
  }

  /* Floyd's bound, evaluated rather than asserted: the number of swaps is at
     most sum over h of ceil(n / 2^(h+1)) * h, and that sum is under n. Exact
     (it is a sum of integers) and returned as a rational so the panel can
     divide it by n and print a fraction under 1 without a decimal. */
  function buildSumExact(n) {
    var terms = [], total = 0n, top = 0, h;
    while ((1 << (top + 1)) <= n) top += 1;        /* top = floor(log2 n) */
    for (h = 0; h <= top; h += 1) {
      var nodes = Math.ceil(n / Math.pow(2, h + 1));
      terms.push({ h: h, nodes: nodes, product: nodes * h });
      total += BigInt(nodes * h);
    }
    return { terms: terms, height: top, total: R(total, 1n),
             perElement: R(total, BigInt(n || 1)) };
  }

  function heapsortRun(a, opts) {
    var h = a.slice(), c = counter(), trace = [], i;
    var b = floydBuild(h, true);
    h = b.result.heap;
    c.compares += b.counts.compares || 0;
    c.swaps += b.counts.swaps || 0;
    var built = h.slice();
    for (i = h.length - 1; i > 0; i -= 1) {
      var t = h[0]; h[0] = h[i]; h[i] = t;
      c.swaps += 1;
      heapSiftDown(h, 0, i, c, null, true);
      trace.push({ at: trace.length, placed: h[i], size: i, heap: h.slice() });
    }
    return runOf({ sorted: h, built: built,
                   buildCompares: b.counts.compares || 0 }, usedCounts(c), trace);
  }

  /* k-way merge two ways, on the same runs, because the comparison IS the
     lesson: a heap of k run heads does one extract and one insert per element,
     and k - 1 pairwise passes re-read the accumulated prefix every time. */
  function kwayMerge(runs) {
    /* The heap holds { key, run } rather than keys, because the merge has to
       know which run to refill from -- which is why this cannot just call
       heapInsert. The sift helpers below are the same two loops with the
       comparison on `.key`, counted identically. */
    var c = counter(), heap = [], out = [], trace = [];
    var cursor = runs.map(function () { return 0; });
    var items = [];
    runs.forEach(function (r, i) { if (r.length) items.push({ key: r[0], run: i }); });
    function siftUpItems(arr) {
      var i = arr.length - 1;
      while (i > 0) {
        var p = (i - 1) >> 1;
        c.compares += 1;
        if (arr[i].key >= arr[p].key) break;
        var t = arr[i]; arr[i] = arr[p]; arr[p] = t;
        c.swaps += 1;
        i = p;
      }
    }
    function siftDownItems(arr) {
      var i = 0;
      while (true) {
        var l = 2 * i + 1, r = l + 1, best = i;
        if (l < arr.length) { c.compares += 1; if (arr[l].key < arr[best].key) best = l; }
        if (r < arr.length) { c.compares += 1; if (arr[r].key < arr[best].key) best = r; }
        if (best === i) return;
        var t = arr[i]; arr[i] = arr[best]; arr[best] = t;
        c.swaps += 1;
        i = best;
      }
    }
    items.forEach(function (it) { heap.push(it); siftUpItems(heap); });
    while (heap.length) {
      var top = heap[0], last = heap.pop();
      if (heap.length) { heap[0] = last; siftDownItems(heap); }
      out.push(top.key);
      c.pops += 1;
      cursor[top.run] += 1;
      trace.push({ at: trace.length, took: top.key, run: top.run, heapSize: heap.length });
      if (cursor[top.run] < runs[top.run].length) {
        heap.push({ key: runs[top.run][cursor[top.run]], run: top.run });
        siftUpItems(heap);
        c.pushes += 1;
      }
    }
    return runOf({ merged: out, k: runs.length }, usedCounts(c), trace);
  }
  function pairwiseMerge(runs) {
    var c = counter(), trace = [], cur = runs.map(function (r) { return r.slice(); });
    function merge2(A, B) {
      var out = [], i = 0, j = 0;
      while (i < A.length && j < B.length) { c.compares += 1; out.push(A[i] <= B[j] ? A[i++] : B[j++]); }
      while (i < A.length) out.push(A[i++]);
      while (j < B.length) out.push(B[j++]);
      return out;
    }
    while (cur.length > 1) {
      var A = cur.shift(), B = cur.shift(), m = merge2(A, B);
      trace.push({ at: trace.length, sizes: [A.length, B.length], produced: m.length });
      cur.push(m);
    }
    return runOf({ merged: cur[0] || [], passes: trace.length }, usedCounts(c), trace);
  }
"""


# ------------------------------------------ 4.3 hash (courses 1 and 8)

HASH_JS = r"""
  /* Hash tables. Load factors, expected chain lengths, collision and
     false-positive probabilities are exact rationals; probe counts are
     measured by running the probes.

     THE ONE APPROXIMATION IN THIS BLOCK is knuthProbeApprox, and it is one of
     the four the path's footer names. Everything else -- including the Bloom
     rate, which most libraries only ever print in its e^-kn/m form -- has an
     exact closed form here, and `bloom` prints both.

     hashOf is exact integer arithmetic in both rules. The multiplicative rule
     is usually written floor(m * frac(k * A)) with A irrational, which cannot
     be exact; the form used here is the integer one Knuth actually recommends,
     floor(m * ((k * w) mod 2^32) / 2^32) with w = 2654435769, the nearest
     integer to 2^32/phi. Every step is an integer, so two readers at the same
     key get the same slot on every machine. */
  var HASH_W = 2654435769n;
  function hashOf(key, m, rule) {
    var k = BigInt(key);
    if (rule === 'multiply') {
      var frac = (k * HASH_W) % 4294967296n;
      if (frac < 0n) frac += 4294967296n;
      return Number((BigInt(m) * frac) / 4294967296n);
    }
    var v = k % BigInt(m);
    return Number(v < 0n ? v + BigInt(m) : v);
  }

  /* Separate chaining. alpha = n/m exactly. The expected number of elements
     examined is 1 + alpha/2 - alpha/(2m) for a successful search and alpha for
     an unsuccessful one, under the simple-uniform-hashing assumption the
     lesson states -- both exact rationals here, and the panel puts the MEAN
     the page measured by running all n searches beside them. */
  function chainRun(keys, m, rule) {
    var chains = [], c = counter(), i;
    for (i = 0; i < m; i += 1) chains.push([]);
    keys.forEach(function (k) { chains[hashOf(k, m, rule)].push(k); c.writes += 1; });
    var probes = 0;
    keys.forEach(function (k) {
      var ch = chains[hashOf(k, m, rule)];
      for (i = 0; i < ch.length; i += 1) { probes += 1; c.probes += 1; if (ch[i] === k) break; }
    });
    var n = keys.length, longest = 0, empty = 0;
    chains.forEach(function (ch) { if (ch.length > longest) longest = ch.length; if (!ch.length) empty += 1; });
    var alpha = R(BigInt(n), BigInt(m));
    var succ = Radd(R(1n, 1n), Rsub(Rdiv(alpha, R(2n, 1n)),
                                    Rdiv(alpha, R(BigInt(2 * m), 1n))));
    return runOf({
      chains: chains, longest: longest, empty: empty, alpha: alpha,
      expectedSuccessful: succ, expectedUnsuccessful: alpha,
      measuredMean: n ? R(BigInt(probes), BigInt(n)) : R(0n, 1n)
    }, usedCounts(c), []);
  }

  /* Open addressing. rule: 'linear', 'quadratic' (i + i^2 mod m), 'double'
     (a second hash, odd so it is coprime with a power-of-two m).

     Tombstones are the point of the delete case: a deleted slot must not stop a
     probe sequence, so it is marked rather than emptied, and the clusters the
     panel counts are runs of NON-EMPTY slots -- a tombstone is as bad as an
     occupant for probing and as good as empty for insertion. */
  function probeSlot(key, m, rule, i) {
    var h = hashOf(key, m, 'division');
    if (rule === 'quadratic') return (h + i + i * i) % m;
    if (rule === 'double') {
      var h2 = 1 + 2 * (hashOf(key, m, 'multiply') % Math.max(1, Math.floor(m / 2)));
      return (h + i * h2) % m;
    }
    return (h + i) % m;
  }
  function probeRun(ops, m, rule) {
    var slots = new Array(m).fill(null), dead = new Array(m).fill(false);
    var c = counter(), trace = [], n = 0;
    ops.forEach(function (o, step) {
      var i, at = -1, probes = 0, found = false;
      for (i = 0; i < m; i += 1) {
        at = probeSlot(o.key, m, rule, i);
        probes += 1; c.probes += 1;
        if (o.op === 'insert') {
          if (slots[at] === null || dead[at]) { slots[at] = o.key; dead[at] = false; n += 1; found = true; break; }
          if (slots[at] === o.key) { found = true; break; }
        } else {
          if (slots[at] === o.key) {
            found = true;
            if (o.op === 'delete') { slots[at] = null; dead[at] = true; n -= 1; }
            break;
          }
          if (slots[at] === null && !dead[at]) break;      /* a true empty ends the search */
        }
      }
      trace.push({ at: step, op: o.op, key: o.key, slot: found ? at : null, probes: probes, found: found });
    });
    var clusters = [], run = 0, longest = 0, tombs = 0;
    for (var s = 0; s < m; s += 1) {
      if (slots[s] !== null || dead[s]) { run += 1; if (dead[s]) tombs += 1; }
      else { if (run) clusters.push(run); longest = Math.max(longest, run); run = 0; }
    }
    if (run) { clusters.push(run); longest = Math.max(longest, run); }
    var totalProbes = trace.reduce(function (t, r) { return t + r.probes; }, 0);
    return runOf({
      slots: slots, dead: dead, size: n, alpha: R(BigInt(n), BigInt(m)),
      clusters: clusters, longestCluster: longest, tombstones: tombs,
      measuredMean: trace.length ? R(BigInt(totalProbes), BigInt(trace.length)) : R(0n, 1n)
    }, usedCounts(c), trace);
  }

  /* KNUTH'S CLUSTERING CURVES -- an approximation, and one of the four this
     path's footer names.

     (1 + 1/(1-a)^2)/2 probes for an unsuccessful search and (1 + 1/(1-a))/2 for
     a successful one, under linear probing. The arithmetic is a double and its
     error is under 1e-15 relative, which is not the point: the MODEL is the
     approximation. It assumes a uniform hash and the idealised cluster
     distribution that analysis derives, and this library proves neither.
     Returns null above alpha = 0.98 rather than a number -- the curve is
     effectively vertical there (2501 probes at 0.98, 5001 at 0.99) and a figure
     read off it says nothing about a real table. */
  function knuthProbeApprox(alpha) {
    var a = typeof alpha === 'number' ? alpha : Rnum(alpha);
    if (!(a >= 0) || a > 0.98) return null;
    return {
      unsuccessful: (1 + 1 / ((1 - a) * (1 - a))) / 2,
      successful: (1 + 1 / (1 - a)) / 2,
      alpha: a,
      stated: 'Knuth, under uniform hashing -- an approximation, not a count'
    };
  }

  /* Growing at one threshold and SHRINKING AT A LOWER ONE. The hysteresis is
     the lesson: grow at alpha >= growAt, shrink at alpha <= shrinkAt, and if
     the two are set too close together a mixed sequence rehashes on nearly
     every operation. ALGO_JS.dynamicArray cannot show this -- it only ever
     grows, takes no thresholds and has no deletions.

     growAt and shrinkAt are rationals, so 3/4 is 3/4. */
  function resizeRun(ops, growAt, shrinkAt, m0) {
    var m = m0 === undefined ? 4 : m0, n = 0, c = counter(), trace = [], moved = 0, total = 0;
    ops.forEach(function (o, i) {
      var cost = 1, event = null;
      if (o.op === 'insert') n += 1; else n = Math.max(0, n - 1);
      c.writes += 1;
      var alpha = R(BigInt(n), BigInt(m));
      if (Rcmp(alpha, growAt) >= 0) {
        event = { from: m, to: m * 2, keys: n };
        cost += n; moved += n; m *= 2; c.moves += n;
      } else if (m > 4 && Rcmp(alpha, shrinkAt) <= 0) {
        event = { from: m, to: Math.max(4, Math.floor(m / 2)), keys: n };
        cost += n; moved += n; m = Math.max(4, Math.floor(m / 2)); c.moves += n;
      }
      total += cost;
      trace.push({ at: i, op: o.op, n: n, m: m, alpha: alpha, cost: cost, total: total, event: event });
    });
    /* Thrashing: a rehash on each of three consecutive operations means the two
       thresholds are too close for this mix, which is the failure the lesson
       asks the reader to reproduce. */
    var thrash = null;
    for (var k = 2; k < trace.length; k += 1) {
      if (trace[k].event && trace[k - 1].event && trace[k - 2].event) { thrash = k - 2; break; }
    }
    return runOf({ table: m, size: n, moved: moved, total: total, bound: 3 * ops.length,
                   amortised: ops.length ? R(BigInt(total), BigInt(ops.length)) : R(0n, 1n),
                   thrashAt: thrash }, usedCounts(c), trace);
  }

  /* The universal family h_{a,b}(x) = ((a x + b) mod p) mod m, counted over
     EVERY (a, b) with a in 1..p-1 and b in 0..p-1 -- p(p-1) of them. The
     collision fraction for a fixed pair x != y is exact and the lesson's claim
     is that it is at most 1/m; the count is what shows it. */
  function universalCount(p, m, x, y) {
    var collisions = 0, total = 0;
    for (var a = 1; a < p; a += 1) {
      for (var b = 0; b < p; b += 1) {
        total += 1;
        var hx = ((a * x + b) % p) % m, hy = ((a * y + b) % p) % m;
        if (hx === hy) collisions += 1;
      }
    }
    return { collisions: collisions, total: total,
             rate: R(BigInt(collisions), BigInt(total)), bound: R(1n, BigInt(m)),
             withinBound: Rcmp(R(BigInt(collisions), BigInt(total)), R(1n, BigInt(m))) <= 0 };
  }

  /* Balls in bins, exactly. The expected number of colliding PAIRS is
     n(n-1)/2m and the expected number of empty bins is m(1 - 1/m)^n; both are
     rationals with no approximation anywhere. birthdayN is the smallest n for
     which the probability that all n land in distinct bins drops below 1/2,
     found by multiplying the exact product out, not by the sqrt(2m ln 2)
     estimate. */
  function ballsExact(n, m) {
    var M = BigInt(m), N = BigInt(n);
    var pairs = Rdiv(R(N * (N - 1n), 2n), R(M, 1n));
    var empty = Rmul(R(M, 1n), Rpow(Rsub(R(1n, 1n), R(1n, M)), n));
    var distinct = R(1n, 1n), birthday = null;
    for (var k = 1; k <= n; k += 1) {
      distinct = Rmul(distinct, R(M - BigInt(k - 1), M));
      if (birthday === null && Rcmp(distinct, R(1n, 2n)) < 0) birthday = k;
    }
    return { expectedPairs: pairs, expectedEmpty: empty,
             allDistinct: distinct, birthdayN: birthday };
  }
  /* The smallest n whose all-distinct probability falls below 1/2, searched
     upward so a lesson can ask for it at an m where n is not yet known. */
  function birthdayExact(m) {
    var M = BigInt(m), p = R(1n, 1n);
    for (var k = 1; k <= 4 * m; k += 1) {
      p = Rmul(p, R(M - BigInt(k - 1), M));
      if (Rcmp(p, R(1n, 2n)) < 0) return { n: k, probability: Rsub(R(1n, 1n), p) };
    }
    return { n: null, probability: null };
  }

  /* A Bloom filter's false-positive rate, EXACTLY: (1 - (1 - 1/m)^(kn))^k.
     sysdesign_core.bloomApprox is the (1 - e^(-kn/m))^k idealisation, and the
     `bloom` mode prints them side by side -- the gap between them is the
     independence assumption, which is the lesson, and printing only the
     approximation would hide it. kStar is found by scanning k exactly, not
     from the m/n * ln 2 rule of thumb. */
  function bloomExact(m, n, k) {
    var one = R(1n, 1n);
    var perBit = Rpow(Rsub(one, R(1n, BigInt(m))), k * n);
    return Rpow(Rsub(one, perBit), k);
  }
  function bloomKStar(m, n, kmax) {
    var best = null, bestK = null, rows = [];
    for (var k = 1; k <= (kmax || 20); k += 1) {
      var p = bloomExact(m, n, k);
      rows.push({ k: k, rate: p });
      if (best === null || Rcmp(p, best) < 0) { best = p; bestK = k; }
    }
    return { k: bestK, rate: best, rows: rows };
  }

  /* Count-Min. The estimate is the minimum over d rows, and the guarantee the
     panel states is the MARKOV one, because that is the only one this library
     proves: each row's overcount has mean F1/w, so P(overcount >= eps*F1) <=
     1/(eps*w), and d independent rows make it (1/(eps*w))^d. At eps = 2/w that
     is exactly 2^-d. Both numbers are rationals.

     The textbook e/w and e^-d are sharper and need a bound course 8 does not
     teach; quoting them would have put a fifth approximation on a path whose
     footer promises four. */
  function countMinRun(stream, w, d, seedRow) {
    var sketch = [], truth = {}, c = counter(), i, j;
    for (i = 0; i < d; i += 1) sketch.push(new Array(w).fill(0));
    var rows = [];
    for (i = 0; i < d; i += 1) rows.push((seedRow ? seedRow(i) : (2 * i + 1)));
    function cell(row, key) { return hashOf(key * rows[row] + row, w, 'multiply'); }
    stream.forEach(function (key) {
      truth[key] = (truth[key] || 0) + 1;
      for (i = 0; i < d; i += 1) { sketch[i][cell(i, key)] += 1; c.writes += 1; }
    });
    var keys = Object.keys(truth).map(Number).sort(function (a, b) { return a - b; });
    var estimates = keys.map(function (key) {
      var est = null;
      for (i = 0; i < d; i += 1) {
        var v = sketch[i][cell(i, key)];
        c.reads += 1;
        if (est === null || v < est) est = v;
      }
      return { key: key, truth: truth[key], estimate: est, over: est - truth[key] };
    });
    var worst = estimates.reduce(function (t, e) { return Math.max(t, e.over); }, 0);
    return runOf({
      sketch: sketch, estimates: estimates, worstOver: worst,
      neverUnder: estimates.every(function (e) { return e.estimate >= e.truth; }),
      total: stream.length,
      eps: R(2n, BigInt(w)), delta: R(1n, 2n ** BigInt(d))
    }, usedCounts(c), []);
  }
"""


# ------------------------------------------------------- the seeded stream

SEEDED_JS = r"""
  /* The seeded input five modes need -- sortkit's `quick` and `expected`,
     tree's `orders` and `skiplist`, random's `karger` -- and the two traps that
     come with it. Built on sysdesign_core.STREAM_JS's lcgStream, which is
     reused exactly as it ships; only the parameters and the seed handling are
     here.

     ALGO_JS.makeArray's 'shuffle' cannot serve. It is ONE fixed permutation,
     produced by idx = (idx + 7) % length, and it takes no seed -- which is
     right for the Discrete Mathematics lesson that wanted two readers to see
     the same array, and useless for a mode whose whole content is what happens
     over many different inputs.

     TRAP ONE: THE MODULUS. Every draw here is consumed as x % n -- a pivot
     index, a vertex to contract, a coin. lcgStream takes its modulus as a
     parameter, and under the glibc parameters the rest of this library uses
     (1103515245, 12345, 2^31) the modulus is a power of two, so the low bits
     are a short cycle: x % 4 runs 0, 1, 2, 3, 0, 1, 2, 3 forever, and 1200 keys
     dealt into 4, 8 or 16 bins come out perfectly level. Measured on this path
     today, not imagined. So the parameters here are MINSTD -- a = 16807, c = 0,
     m = 2^31 - 1, which is PRIME, so no bit of the state is worse than any
     other. A draw consumed as x/m uses the high bits and would have been fine
     either way; a draw consumed as x % n would not.

     TRAP TWO: THE SEED. An LCG's k-th value is an affine function of its seed,
     and under a purely multiplicative one it is literally seed * (a^k mod m).
     So consecutive seeds -- which is exactly what a slider hands out -- produce
     correlated streams, and a mode that asks the reader to reseed and compare
     would be comparing a straight line. The seed is therefore run through the
     splitmix64 finaliser before it becomes the state: multiply, xor-shift,
     multiply, xor-shift, which is nonlinear over the integers and breaks the
     affinity. shard.py's shardSeedState is the same function for the same
     reason; this is the Algorithms path's copy of it. */
  function algoMultiplier() { return 16807; }
  function algoModulus() { return 2147483647; }
  function algoSeedState(seed) {
    var mask = 0xFFFFFFFFFFFFFFFFn;
    var x = (BigInt(seed) + 1n) * 0x9E3779B97F4A7C15n & mask;
    x = ((x ^ (x >> 30n)) * 0xBF58476D1CE4E5B9n) & mask;
    x = ((x ^ (x >> 27n)) * 0x94D049BB133111EBn) & mask;
    x = x ^ (x >> 31n);
    return Number(x % BigInt(algoModulus() - 1)) + 1;    /* never the fixed point 0 */
  }
  function algoStream(seed, count) {
    return lcgStream(algoMultiplier(), 0, algoModulus(), algoSeedState(seed), count);
  }
  /* Exact rationals in (0, 1) over the modulus, for anything that compares a
     draw against a probability rather than indexing with it. */
  function algoUniform(seed, count) {
    var m = BigInt(algoModulus());
    return algoStream(seed, count).map(function (x) { return R(BigInt(x), m); });
  }
  /* A uniformly random permutation of 0..n-1 from one stream, by Fisher-Yates
     taking draw i modulo the shrinking suffix. */
  function algoPermutation(n, seed) {
    var draws = algoStream(seed, n), a = [], i;
    for (i = 0; i < n; i += 1) a.push(i);
    for (i = n - 1; i > 0; i -= 1) {
      var j = draws[n - 1 - i] % (i + 1), t = a[i];
      a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  /* A tape of coin flips. The low bit of a prime-modulus stream is a coin; the
     low bit of a power-of-two modulus is not, which is trap one again. */
  function algoCoins(seed, count) {
    return algoStream(seed, count).map(function (x) { return x % 2; });
  }
"""


# ------------------------------------------------------------ drawing a tree

TREEDRAW_JS = r"""
  /* A tree renderer, shared for the same reason the graph one is: six kinds of
     tree are drawn on this path -- search trees, AVL and treaps, Huffman codes,
     tries, DP subproblem trees, branch-and-bound search trees -- and every one
     of them was about to be a helper closed over its own lab's element.

     It is generic over the node type: `kids(node)` returns the children (nulls
     included, so a BST's missing left child still leaves a gap where it
     belongs) and `label(node)` returns what goes in the circle. x is the
     in-order position, y is the depth, which is the layout that makes a search
     tree's in-order sequence readable straight off the drawing. */
  function treeLayout(root, kids, label, opts) {
    opts = opts || {};
    var nodes = [], links = [], next = 0, maxDepth = 0;
    (function place(node, depth, parent) {
      if (!node) { next += opts.gaps === false ? 0 : 0.5; return null; }
      var children = kids(node) || [];
      var left = children.length ? place(children[0], depth + 1, null) : null;
      var me = { node: node, label: label(node), depth: depth, order: next, id: nodes.length };
      next += 1;
      nodes.push(me);
      if (left) links.push({ from: me.id, to: left.id, side: 0 });
      for (var k = 1; k < children.length; k += 1) {
        var c = place(children[k], depth + 1, null);
        if (c) links.push({ from: me.id, to: c.id, side: k });
      }
      if (depth > maxDepth) maxDepth = depth;
      return me;
    })(root, 0, null);
    var w = opts.width === undefined ? 460 : opts.width;
    var h = opts.height === undefined ? 210 : opts.height;
    var cols = Math.max(1, next - 1), rows = Math.max(1, maxDepth);
    nodes.forEach(function (n) {
      n.x = 26 + (n.order / cols) * (w - 52);
      n.y = 22 + (n.depth / rows) * (h - 44);
    });
    return { nodes: nodes, links: links, depth: maxDepth, count: nodes.length };
  }
  function treeSvg(layout, opts) {
    opts = opts || {};
    var hi = {};
    (opts.highlight || []).forEach(function (i) { hi[i] = true; });
    var s = '', r = opts.radius === undefined ? 14 : opts.radius;
    layout.links.forEach(function (l) {
      var a = layout.nodes[l.from], b = layout.nodes[l.to];
      s += '<line x1="' + a.x.toFixed(1) + '" y1="' + a.y.toFixed(1) + '" x2="' + b.x.toFixed(1)
        + '" y2="' + b.y.toFixed(1) + '" stroke="'
        + (hi[l.to] ? 'var(--cyan)' : 'var(--line-strong)') + '" stroke-width="'
        + (hi[l.to] ? 3 : 1.6) + '" />';
    });
    layout.nodes.forEach(function (n) {
      var fill = opts.fill ? opts.fill(n) : (hi[n.id] ? 'var(--cyan)' : 'var(--panel-3)');
      s += '<circle cx="' + n.x.toFixed(1) + '" cy="' + n.y.toFixed(1) + '" r="' + r
        + '" fill="' + fill + '" stroke="var(--line-strong)" stroke-width="1.8" />';
      s += '<text x="' + n.x.toFixed(1) + '" y="' + (n.y + 4).toFixed(1)
        + '" text-anchor="middle" font-size="11" font-weight="800" fill="'
        + (hi[n.id] ? 'var(--on-accent)' : 'var(--text)') + '">' + n.label + '</text>';
      if (opts.note) {
        var note = opts.note(n);
        if (note) s += '<text x="' + n.x.toFixed(1) + '" y="' + (n.y - r - 4).toFixed(1)
          + '" text-anchor="middle" font-size="9" fill="var(--muted)">' + note + '</text>';
      }
    });
    return s;
  }
  function drawTree(el, root, kids, label, opts) {
    var s = treeSvg(treeLayout(root, kids, label, opts), opts);
    if (el) el.innerHTML = s;
    return s;
  }
"""


# ------------------------------------------ 4.4 tree (courses 1 and 8)

TREE_JS = r"""
  /* Search trees. A node is { key, l, r, size, height, priority }; an empty
     subtree is null. Every routine returns a NEW tree rather than mutating the
     one it was given, so a mode can draw before and after without keeping its
     own copy, and so a trace step can hold the actual tree it describes.

     The one approximation in this block is randomBstDepthApprox, and it is one
     of the four the path's footer names. */
  function bstNode(key) { return { key: key, l: null, r: null, size: 1, height: 0, priority: 0 }; }
  function bstCopy(t) {
    if (!t) return null;
    return { key: t.key, l: bstCopy(t.l), r: bstCopy(t.r), size: t.size,
             height: t.height, priority: t.priority };
  }
  function bstFix(t) {
    if (!t) return null;
    t.size = 1 + (t.l ? t.l.size : 0) + (t.r ? t.r.size : 0);
    t.height = 1 + Math.max(t.l ? t.l.height : -1, t.r ? t.r.height : -1);
    return t;
  }
  function bstKids(t) { return [t.l, t.r]; }
  function bstInorder(t) {
    var out = [];
    (function walk(n) { if (!n) return; walk(n.l); out.push(n.key); walk(n.r); })(t);
    return out;
  }
  function bstHeight(t) { return t ? t.height : -1; }
  function bstDepths(t) {
    var out = [];
    (function walk(n, d) { if (!n) return; out.push(d); walk(n.l, d + 1); walk(n.r, d + 1); })(t, 0);
    return out;
  }

  /* THE GLOBAL CHECK AND THE LOCAL ONE, which is why bstValid takes bounds.
     Checking only that each node sits between its two children passes trees
     that are not search trees at all -- the classic wrong answer -- so both
     verdicts are returned and the lesson shows an instance where they differ. */
  function bstValid(t, lo, hi) {
    if (!t) return true;
    if (lo !== null && lo !== undefined && t.key <= lo) return false;
    if (hi !== null && hi !== undefined && t.key >= hi) return false;
    return bstValid(t.l, lo, t.key) && bstValid(t.r, t.key, hi);
  }
  function bstLocallyValid(t) {
    if (!t) return true;
    if (t.l && t.l.key >= t.key) return false;
    if (t.r && t.r.key <= t.key) return false;
    return bstLocallyValid(t.l) && bstLocallyValid(t.r);
  }

  function bstInsert(root, key, c) {
    var made = false;
    function go(t) {
      if (!t) { made = true; if (c) c.writes += 1; return bstNode(key); }
      if (c) c.compares += 1;
      if (key < t.key) t.l = go(t.l);
      else if (key > t.key) t.r = go(t.r);
      else return t;
      return bstFix(t);
    }
    var out = go(root);
    return { root: bstFix(out), inserted: made };
  }
  function bstSearch(root, key, c) {
    var path = [], t = root;
    while (t) {
      path.push(t.key);
      if (c) c.compares += 1;
      if (key === t.key) return { found: true, path: path };
      t = key < t.key ? t.l : t.r;
    }
    return { found: false, path: path };
  }
  /* Deletion, with the two-child case the lesson animates: the node's key is
     replaced by its in-order SUCCESSOR -- the minimum of the right subtree --
     and that successor, which has no left child by construction, is deleted
     from there. `replaced` is what the animation steps through. */
  function bstDelete(root, key, c) {
    var replaced = null, removed = false;
    function minOf(t) { while (t.l) t = t.l; return t; }
    function go(t) {
      if (!t) return null;
      if (c) c.compares += 1;
      if (key < t.key) { t.l = go(t.l); return bstFix(t); }
      if (key > t.key) { t.r = go(t.r); return bstFix(t); }
      removed = true;
      if (!t.l) return t.r;
      if (!t.r) return t.l;
      var s = minOf(t.r);
      replaced = { from: t.key, to: s.key };
      t.key = s.key;
      var k = key; key = s.key;
      t.r = go(t.r);
      key = k;
      return bstFix(t);
    }
    var out = go(root);
    return { root: out, removed: removed, replaced: replaced };
  }

  /* One operation sequence, with the tree after each step. ops are
     { op: 'insert' | 'delete' | 'search', key }. */
  function bstRun(ops) {
    var root = null, c = counter(), trace = [];
    ops.forEach(function (o, i) {
      var note = null;
      if (o.op === 'insert') { var r = bstInsert(root, o.key, c); root = r.root; note = r.inserted ? 'inserted' : 'already present'; }
      else if (o.op === 'delete') { var d = bstDelete(root, o.key, c); root = d.root; note = d.replaced ? ('successor ' + d.replaced.to + ' moved up') : (d.removed ? 'removed' : 'absent'); }
      else { var s = bstSearch(root, o.key, c); note = s.found ? ('found via ' + s.path.join(' -> ')) : 'not found'; }
      trace.push({ at: i, op: o.op, key: o.key, note: note, tree: bstCopy(root),
                   inorder: bstInorder(root), valid: bstValid(root, null, null) });
    });
    return runOf({ root: root, inorder: bstInorder(root), height: bstHeight(root),
                   valid: bstValid(root, null, null), locallyValid: bstLocallyValid(root) },
                 usedCounts(c), trace);
  }

  /* Height and mean depth under one insertion order. The panel plots the mean
     against 2 ln n, which is an ASYMPTOTIC statement about a uniformly random
     order and is drawn as a labelled reference curve, never as the answer. */
  function bstFromOrder(order) {
    var root = null, c = counter();
    order.forEach(function (k) { root = bstInsert(root, k, c).root; });
    var depths = bstDepths(root), total = depths.reduce(function (a, b) { return a + b; }, 0);
    return runOf({ root: root, height: bstHeight(root), depths: depths,
                   meanDepth: R(BigInt(total), BigInt(depths.length || 1)) },
                 usedCounts(c), []);
  }
  /* 2 ln n -- APPROXIMATE, and one of the four this path's footer names. It is
     the asymptotic mean root-to-node depth of a tree built from a uniformly
     random insertion order. At n = 15 it reads 5.42 against a true mean nearer
     4.6: the arithmetic is a double and correct to ~1e-15, and the STATEMENT is
     an asymptote, which is a different kind of wrong from a rounding. */
  function randomBstDepthApprox(n) { return n > 0 ? 2 * logApprox(n) : 0; }

  /* Rotation. dir 'right' lifts the left child, dir 'left' lifts the right one.
     The in-order sequence is unchanged by construction and the panel checks it,
     because "a rotation preserves the search order" is the claim on which every
     balanced tree rests. */
  function rotate(t, dir) {
    if (!t) return null;
    var out;
    if (dir === 'right') {
      if (!t.l) return t;
      out = t.l; t.l = out.r; out.r = t;
    } else {
      if (!t.r) return t;
      out = t.r; t.r = out.l; out.l = t;
    }
    bstFix(t); bstFix(out);
    return out;
  }
  /* N(h): the fewest nodes an AVL tree of height h can hold, N(h) = N(h-1) +
     N(h-2) + 1. The table is the bound on an AVL tree's height, and it is a
     recurrence evaluated, not a log quoted. */
  function minAvlNodes(h) {
    var rows = [{ h: 0, n: 1 }, { h: 1, n: 2 }];
    for (var k = 2; k <= h; k += 1) rows.push({ h: k, n: rows[k - 1].n + rows[k - 2].n + 1 });
    return { rows: rows.slice(0, Math.max(1, h + 1)), n: rows[Math.min(h, rows.length - 1)].n };
  }
  function bstBalance(t) { return t ? bstHeight(t.l) - bstHeight(t.r) : 0; }
  /* AVL insertion, with the case NAMED at each rebalance -- LL, LR, RR, RL --
     because the case is what the reader has to learn to recognise. */
  function avlInsert(keys) {
    var c = counter(), trace = [], root = null;
    function fixUp(t, key) {
      bstFix(t);
      var bal = bstBalance(t), which = null;
      if (bal > 1 && key < t.l.key) { which = 'LL'; t = rotate(t, 'right'); }
      else if (bal < -1 && key > t.r.key) { which = 'RR'; t = rotate(t, 'left'); }
      else if (bal > 1) { which = 'LR'; t.l = rotate(t.l, 'left'); t = rotate(t, 'right'); }
      else if (bal < -1) { which = 'RL'; t.r = rotate(t.r, 'right'); t = rotate(t, 'left'); }
      if (which) { c.swaps += 1; trace.push({ at: trace.length, key: key, rebalance: which, root: t.key }); }
      return t;
    }
    keys.forEach(function (key) {
      root = (function go(t) {
        if (!t) { c.writes += 1; return bstNode(key); }
        c.compares += 1;
        if (key < t.key) t.l = go(t.l);
        else if (key > t.key) t.r = go(t.r);
        else return t;
        return fixUp(t, key);
      })(root);
    });
    var plain = bstFromOrder(keys);
    return runOf({ root: root, height: bstHeight(root), inorder: bstInorder(root),
                   plainHeight: plain.result.height, rebalances: trace.length,
                   minNodesForHeight: minAvlNodes(bstHeight(root)).n },
                 usedCounts(c), trace);
  }

  /* An order-statistic tree: every node carries the size of its subtree, so
     rank, select and a range count are walks rather than scans. The walk is
     traced because the subtraction at each right turn is the step readers get
     wrong. */
  function augmentWalk(root, query) {
    var c = counter(), trace = [], t = root, result = null;
    if (query.op === 'select') {
      var i = query.i;
      while (t) {
        var left = t.l ? t.l.size : 0;
        c.compares += 1;
        trace.push({ at: trace.length, node: t.key, leftSize: left, want: i });
        if (i === left + 1) { result = t.key; break; }
        if (i <= left) t = t.l;
        else { i -= left + 1; t = t.r; }
      }
    } else if (query.op === 'rank') {
      var rank = 0;
      while (t) {
        var l2 = t.l ? t.l.size : 0;
        c.compares += 1;
        trace.push({ at: trace.length, node: t.key, leftSize: l2, running: rank });
        if (query.key === t.key) { rank += l2 + 1; result = rank; break; }
        if (query.key < t.key) t = t.l;
        else { rank += l2 + 1; t = t.r; }
      }
    } else {
      /* rangeCount(lo, hi) as TWO WALKS and not a scan: the keys at most hi
         minus the keys below lo, each counted by adding a subtree size at every
         right turn. Scanning the in-order list would give the same number and
         would not be the lesson, which is that the augmentation makes this
         O(height). */
      var hiCount = bstCountAtMost(root, query.hi, c, trace);
      var loCount = bstCountBelow(root, query.lo, c, trace);
      result = hiCount - loCount;
    }
    return runOf({ value: result }, usedCounts(c), trace);
  }
  function bstCountAtMost(root, key, c, trace) {
    var n = 0, t = root;
    while (t) {
      var l = t.l ? t.l.size : 0;
      if (c) c.compares += 1;
      if (trace) trace.push({ at: trace.length, node: t.key, leftSize: l, running: n, want: '<= ' + key });
      if (key < t.key) t = t.l;
      else { n += l + 1; t = t.r; }
    }
    return n;
  }
  function bstCountBelow(root, key, c, trace) {
    var n = 0, t = root;
    while (t) {
      var l = t.l ? t.l.size : 0;
      if (c) c.compares += 1;
      if (trace) trace.push({ at: trace.length, node: t.key, leftSize: l, running: n, want: '< ' + key });
      if (key <= t.key) t = t.l;
      else { n += l + 1; t = t.r; }
    }
    return n;
  }

  /* A treap: a search tree on the keys and a heap on the priorities. Two
     insertion orders of the same (key, priority) set give the SAME tree, which
     is the mode's point, so the rotations are counted and the shape returned. */
  function treapInsert(keys, priorities) {
    var c = counter(), trace = [], root = null;
    keys.forEach(function (key, i) {
      var pri = priorities[i];
      root = (function go(t) {
        if (!t) { var n = bstNode(key); n.priority = pri; c.writes += 1; return n; }
        c.compares += 1;
        if (key < t.key) {
          t.l = go(t.l);
          if (t.l.priority < t.priority) {
            t = rotate(t, 'right'); c.swaps += 1;
            trace.push({ at: trace.length, key: key, rotation: 'right', root: t.key });
          }
        } else if (key > t.key) {
          t.r = go(t.r);
          if (t.r.priority < t.priority) {
            t = rotate(t, 'left'); c.swaps += 1;
            trace.push({ at: trace.length, key: key, rotation: 'left', root: t.key });
          }
        }
        return bstFix(t);
      })(root);
    });
    var depths = bstDepths(root), total = depths.reduce(function (a, b) { return a + b; }, 0);
    return runOf({ root: root, height: bstHeight(root), inorder: bstInorder(root),
                   meanDepth: R(BigInt(total), BigInt(depths.length || 1)),
                   heapOrdered: (function ok(t) {
                     if (!t) return true;
                     if (t.l && t.l.priority < t.priority) return false;
                     if (t.r && t.r.priority < t.priority) return false;
                     return ok(t.l) && ok(t.r);
                   })(root) },
                 usedCounts(c), trace);
  }

  /* A skip list from a COIN TAPE, so the levels are the reader's seed rather
     than a hidden random source. A key's level is the run of heads at its place
     on the tape; the search drops a level whenever the next node overshoots,
     and the hops are what the panel plots against 2 log2 n. */
  function skipBuild(keys, tape) {
    var levels = [], c = counter(), at = 0, maxLevel = 0;
    keys.forEach(function () {
      var lvl = 0;
      while (at < tape.length && tape[at] === 1 && lvl < 8) { lvl += 1; at += 1; }
      at += 1;
      levels.push(lvl);
      if (lvl > maxLevel) maxLevel = lvl;
    });
    var sorted = keys.map(function (k, i) { return { key: k, level: levels[i] }; })
                     .sort(function (a, b) { return a.key - b.key; });
    function search(target) {
      var lvl = maxLevel, i = -1, hops = 0, path = [];
      while (lvl >= 0) {
        var j = i + 1;
        while (j < sorted.length) {
          if (sorted[j].level < lvl) { j += 1; continue; }
          hops += 1;
          if (sorted[j].key > target) break;
          path.push({ level: lvl, key: sorted[j].key });
          i = j;
          if (sorted[j].key === target) return { hops: hops, found: true, path: path };
          j += 1;
        }
        lvl -= 1;
      }
      return { hops: hops, found: i >= 0 && sorted[i].key === target, path: path };
    }
    var totalHops = 0, worst = 0;
    sorted.forEach(function (e) {
      var r = search(e.key);
      totalHops += r.hops; c.hops += r.hops;
      if (r.hops > worst) worst = r.hops;
    });
    return runOf({ levels: levels, sorted: sorted, maxLevel: maxLevel, worstHops: worst,
                   meanHops: R(BigInt(totalHops), BigInt(sorted.length || 1)),
                   search: search },
                 usedCounts(c), []);
  }
"""


# ------------------------------------------------------ 4.5 sortkit (course 2)

SORT_JS = r"""
  /* Sorting. Every comparison count comes from running the sort on the array
     on screen. The only exact expectation here, 2(n+1)H_n - 4n, is a rational
     over an exact H_n, which is sysdesign_core.harmonic(n, 1) reused as it
     ships -- the point of computing it exactly is that the measured mean over
     seeds and the expectation can be compared as NUMBERS rather than as two
     decimals that nearly agree.

     ALGO_JS's mergeSort and insertionSort are reused as they ship wherever a
     baseline total is all that is wanted. Everything this kit SHOWS -- the
     partition invariant, the pivot rule, the stability tags -- is here, because
     those routines return a total and nothing else. */

  /* Records are { key, tag }; the tag is the input position, which is what
     makes a stability violation visible. */
  function stableRecords(keys) {
    return keys.map(function (k, i) { return { key: k, tag: i + 1 }; });
  }
  function stabilityViolations(input, output) {
    var v = [], i, j;
    for (i = 0; i < output.length; i += 1) {
      for (j = i + 1; j < output.length; j += 1) {
        if (output[i].key === output[j].key && output[i].tag > output[j].tag) {
          v.push([output[i], output[j]]);
        }
      }
    }
    return v;
  }
  function stableRun(records, algo) {
    var a = records.map(function (r) { return { key: r.key, tag: r.tag }; }), c = counter(), i, j;
    if (algo === 'insertion') {
      for (i = 1; i < a.length; i += 1) {
        var key = a[i];
        j = i - 1;
        while (j >= 0) { c.compares += 1; if (a[j].key <= key.key) break; a[j + 1] = a[j]; c.moves += 1; j -= 1; }
        a[j + 1] = key;
      }
    } else if (algo === 'selection') {
      /* Unstable, and the lesson wants to SEE why: the long-range swap that
         puts the minimum in place jumps an equal key over its twin. */
      for (i = 0; i < a.length; i += 1) {
        var m = i;
        for (j = i + 1; j < a.length; j += 1) { c.compares += 1; if (a[j].key < a[m].key) m = j; }
        if (m !== i) { var t = a[i]; a[i] = a[m]; a[m] = t; c.swaps += 1; }
      }
    } else if (algo === 'merge') {
      a = (function sort(arr) {
        if (arr.length <= 1) return arr;
        var mid = arr.length >> 1, L = sort(arr.slice(0, mid)), Rt = sort(arr.slice(mid)), out = [];
        i = 0; j = 0;
        while (i < L.length && j < Rt.length) { c.compares += 1; out.push(L[i].key <= Rt[j].key ? L[i++] : Rt[j++]); }
        while (i < L.length) out.push(L[i++]);
        while (j < Rt.length) out.push(Rt[j++]);
        return out;
      })(a);
    } else if (algo === 'quick') {
      a = (function sort(arr) {
        if (arr.length <= 1) return arr;
        var p = arr[arr.length - 1], lo = [], hi = [];
        for (i = 0; i < arr.length - 1; i += 1) {
          c.compares += 1;
          (arr[i].key <= p.key ? lo : hi).push(arr[i]);
        }
        /* The in-place Lomuto partition this stands for swaps equal keys past
           each other; the split below reproduces the same output order. */
        return sort(hi).concat([p], sort(lo)).reverse();
      })(a);
    } else {
      throw new Error('unknown sort: ' + algo);
    }
    var viol = stabilityViolations(records, a);
    return runOf({ output: a, stable: viol.length === 0, violations: viol }, usedCounts(c), []);
  }
  /* A two-key sort by successive stable passes. The misconception the lesson
     names is the order: with stable passes the LEAST significant key is sorted
     first, and doing it the other way round loses the primary order. */
  function twoKeyPasses(records, first, second) {
    function pass(list, key) {
      var out = list.slice();
      out.sort(function (x, y) { return x[key] - y[key]; });     /* stable in every engine since ES2019 */
      return out;
    }
    var right = pass(pass(records, second), first);
    var wrong = pass(pass(records, first), second);
    return { correct: right, wrong: wrong,
             same: right.map(function (r) { return r.tag; }).join(',')
                   === wrong.map(function (r) { return r.tag; }).join(',') };
  }

  /* Partitioning, the two schemes, with the invariant checked after EVERY
     step -- which is the mode, and the reason the region boundaries are in the
     trace rather than only the final split. */
  function partitionRun(a, pivotIndex, scheme) {
    var arr = a.slice(), c = counter(), trace = [], lo = 0, hi = arr.length - 1, ok = true;
    if (scheme === 'hoare') {
      var p = arr[pivotIndex === undefined ? lo : pivotIndex];
      var i = lo - 1, j = hi + 1;
      while (true) {
        do { i += 1; c.compares += 1; } while (arr[i] < p);
        do { j -= 1; c.compares += 1; } while (arr[j] > p);
        if (i >= j) break;
        var t = arr[i]; arr[i] = arr[j]; arr[j] = t; c.swaps += 1;
        trace.push({ at: trace.length, i: i, j: j, array: arr.slice(), pivot: p });
      }
      return runOf({ array: arr, split: j, pivot: p, scheme: 'hoare',
                     invariant: arr.slice(0, j + 1).every(function (v) { return v <= p; })
                                && arr.slice(j + 1).every(function (v) { return v >= p; }) },
                   usedCounts(c), trace);
    }
    /* Lomuto: a[lo..i] <= pivot < a[i+1..j-1], a[j..hi-1] not yet seen. */
    var pi = pivotIndex === undefined ? hi : pivotIndex;
    if (pi !== hi) { var s = arr[pi]; arr[pi] = arr[hi]; arr[hi] = s; c.swaps += 1; }
    var pivot = arr[hi], k = lo - 1;
    for (var j2 = lo; j2 < hi; j2 += 1) {
      c.compares += 1;
      if (arr[j2] <= pivot) {
        k += 1;
        if (k !== j2) { var t2 = arr[k]; arr[k] = arr[j2]; arr[j2] = t2; c.swaps += 1; }
      }
      var less = arr.slice(lo, k + 1).every(function (v) { return v <= pivot; });
      var more = arr.slice(k + 1, j2 + 1).every(function (v) { return v > pivot; });
      if (!(less && more)) ok = false;
      trace.push({ at: trace.length, i: k, j: j2, array: arr.slice(), pivot: pivot,
                   regions: { le: [lo, k], gt: [k + 1, j2], unseen: [j2 + 1, hi - 1] },
                   invariant: less && more });
    }
    var t3 = arr[k + 1]; arr[k + 1] = arr[hi]; arr[hi] = t3; c.swaps += 1;
    return runOf({ array: arr, split: k + 1, pivot: pivot, scheme: 'lomuto', invariant: ok },
                 usedCounts(c), trace);
  }

  /* Quicksort under a pivot rule. 'random' draws from the seeded stream, which
     is MINSTD with a mixed seed -- see SEEDED_JS for why a pivot index taken
     modulo the subarray length may not come off a power-of-two modulus. */
  function pivotFor(arr, lo, hi, rule, draws, drawAt, c) {
    if (rule === 'first') return lo;
    if (rule === 'middle') return (lo + hi) >> 1;
    if (rule === 'median3') {
      var m = (lo + hi) >> 1, x = arr[lo], y = arr[m], z = arr[hi];
      c.compares += 3;
      if ((x <= y && y <= z) || (z <= y && y <= x)) return m;
      if ((y <= x && x <= z) || (z <= x && x <= y)) return lo;
      return hi;
    }
    if (rule === 'random') return lo + (draws[drawAt.i++ % draws.length] % (hi - lo + 1));
    return hi;
  }
  function quickRun(a, rule, seed) {
    var arr = a.slice(), c = counter(), trace = [], maxDepth = 0;
    var draws = rule === 'random' ? algoStream(seed === undefined ? 1 : seed, Math.max(8, a.length * 2)) : [];
    var drawAt = { i: 0 };
    (function sort(lo, hi, depth) {
      if (lo >= hi) return;
      if (depth > maxDepth) maxDepth = depth;
      c.calls += 1;
      var pi = pivotFor(arr, lo, hi, rule, draws, drawAt, c);
      if (pi !== hi) { var s = arr[pi]; arr[pi] = arr[hi]; arr[hi] = s; c.swaps += 1; }
      var pivot = arr[hi], k = lo - 1;
      for (var j = lo; j < hi; j += 1) {
        c.compares += 1;
        if (arr[j] <= pivot) { k += 1; if (k !== j) { var t = arr[k]; arr[k] = arr[j]; arr[j] = t; c.swaps += 1; } }
      }
      var t2 = arr[k + 1]; arr[k + 1] = arr[hi]; arr[hi] = t2; c.swaps += 1;
      trace.push({ at: trace.length, lo: lo, hi: hi, pivot: pivot, split: k + 1, depth: depth,
                   left: k - lo, right: hi - k - 1 });
      sort(lo, k, depth + 1);
      sort(k + 2, hi, depth + 1);
    })(0, arr.length - 1, 1);
    return runOf({ sorted: arr, depth: maxDepth, rule: rule }, usedCounts(c), trace);
  }
  /* The exact expectation: 2(n+1)H_n - 4n comparisons for a random pivot.
     H_n is sysdesign_core.harmonic(n, 1), exact, so this is a fraction. */
  function quickExpected(n) {
    if (n < 2) return R(0n, 1n);
    var H = harmonic(n, 1);
    return Rsub(Rmul(R(BigInt(2 * (n + 1)), 1n), H), R(BigInt(4 * n), 1n));
  }
  /* The mean over many seeds, as a rational, so it can sit beside the
     expectation without either becoming a decimal. */
  function quickMeanOverSeeds(a, seeds) {
    var total = 0n;
    seeds.forEach(function (s) { total += BigInt(quickRun(a, 'random', s).counts.compares || 0); });
    return R(total, BigInt(seeds.length));
  }

  function countingSortRun(keys, k) {
    var c = counter(), count = new Array(k).fill(0), i;
    keys.forEach(function (v) { count[v] += 1; c.reads += 1; });
    var counts0 = count.slice();
    for (i = 1; i < k; i += 1) count[i] += count[i - 1];
    var prefix = count.slice(), out = new Array(keys.length).fill(null);
    /* Backwards, which is what makes it stable -- and the mode's toggle runs it
       forwards to show the same algorithm losing the property. */
    for (i = keys.length - 1; i >= 0; i -= 1) {
      count[keys[i]] -= 1;
      out[count[keys[i]]] = keys[i];
      c.writes += 1;
    }
    return runOf({ sorted: out, counts: counts0, prefix: prefix,
                   work: keys.length + k, comparisonBound: keys.length * ilog2(Math.max(2, keys.length)) },
                 usedCounts(c), []);
  }
  /* LSD radix. `stable: false` reverses each bucket on distribution, which
     breaks the sort visibly -- the point being that radix is correct only
     BECAUSE its per-digit pass is stable. */
  function radixRun(keys, base, stable) {
    var c = counter(), cur = keys.slice(), passes = [], maxKey = Math.max.apply(null, keys.concat([0]));
    var digits = 0, v = maxKey;
    while (v > 0) { digits += 1; v = Math.floor(v / base); }
    digits = Math.max(1, digits);
    for (var d = 0; d < digits; d += 1) {
      var buckets = [], i;
      for (i = 0; i < base; i += 1) buckets.push([]);
      cur.forEach(function (key) {
        buckets[Math.floor(key / Math.pow(base, d)) % base].push(key);
        c.moves += 1;
      });
      if (!stable) buckets.forEach(function (b) { b.reverse(); });
      cur = [].concat.apply([], buckets);
      passes.push({ digit: d, buckets: buckets.map(function (b) { return b.slice(); }), after: cur.slice() });
    }
    var want = keys.slice().sort(function (x, y) { return x - y; });
    return runOf({ sorted: cur, digits: digits, passes: passes,
                   correct: cur.join(',') === want.join(',') }, usedCounts(c), passes);
  }
  /* Bucket sort: distribute by value, insertion-sort each bucket. The work is
     quadratic IN THE BUCKET, so a skewed distribution and a uniform one on the
     same n are the mode's two arms. */
  function bucketRun(keys, buckets, top) {
    var c = counter(), lim = top === undefined ? (Math.max.apply(null, keys.concat([1])) + 1) : top;
    var bs = [], i;
    for (i = 0; i < buckets; i += 1) bs.push([]);
    keys.forEach(function (k) {
      var b = Math.min(buckets - 1, Math.floor((k * buckets) / lim));
      bs[b].push(k); c.moves += 1;
    });
    var out = [], work = [];
    bs.forEach(function (b, bi) {
      var inner = 0;
      for (i = 1; i < b.length; i += 1) {
        var key = b[i], j = i - 1;
        while (j >= 0) { c.compares += 1; inner += 1; if (b[j] <= key) break; b[j + 1] = b[j]; j -= 1; }
        b[j + 1] = key;
      }
      work.push({ bucket: bi, size: b.length, compares: inner });
      out = out.concat(b);
    });
    return runOf({ sorted: out, buckets: bs, work: work, n: keys.length }, usedCounts(c), []);
  }

  function quickselectRun(a, k, rule, seed) {
    var arr = a.slice(), c = counter(), trace = [], lo = 0, hi = arr.length - 1;
    var draws = rule === 'random' ? algoStream(seed === undefined ? 1 : seed, Math.max(8, a.length * 2)) : [];
    var drawAt = { i: 0 }, answer = null;
    while (lo <= hi) {
      c.calls += 1;
      var pi = pivotFor(arr, lo, hi, rule, draws, drawAt, c);
      if (pi !== hi) { var s = arr[pi]; arr[pi] = arr[hi]; arr[hi] = s; c.swaps += 1; }
      var pivot = arr[hi], p = lo - 1;
      for (var j = lo; j < hi; j += 1) {
        c.compares += 1;
        if (arr[j] <= pivot) { p += 1; if (p !== j) { var t = arr[p]; arr[p] = arr[j]; arr[j] = t; c.swaps += 1; } }
      }
      var t2 = arr[p + 1]; arr[p + 1] = arr[hi]; arr[hi] = t2; c.swaps += 1;
      var rank = p + 2;                       /* 1-based rank of the pivot */
      trace.push({ at: trace.length, lo: lo, hi: hi, pivot: pivot, rank: rank, want: k });
      if (rank === k) { answer = pivot; break; }
      if (k < rank) hi = p; else lo = p + 2;
    }
    var sortCompares = mergeSort(a.slice());
    return runOf({ value: answer, sortThenIndex: sortCompares }, usedCounts(c), trace);
  }

  /* Median of medians. The guarantee is what the mode shows: with groups of
     five, the pivot is at least as large as three elements in each of half the
     groups, so at least 3n/10 fall on each side and the recursion cannot
     degenerate the way quickselect's can. */
  function momRun(a, k, group) {
    group = group || 5;
    var c = counter(), trace = [];
    function medianOf(list) {
      var s = list.slice().sort(function (x, y) { return x - y; });
      c.compares += Math.max(0, list.length * (list.length - 1) / 2);
      return s[(s.length - 1) >> 1];
    }
    function select(list, want, depth) {
      c.calls += 1;
      if (list.length <= group) {
        var s = list.slice().sort(function (x, y) { return x - y; });
        c.compares += Math.max(0, list.length * (list.length - 1) / 2);
        return s[want - 1];
      }
      var groups = [], i;
      for (i = 0; i < list.length; i += group) groups.push(list.slice(i, i + group));
      var medians = groups.map(medianOf);
      var pivot = select(medians, Math.ceil(medians.length / 2), depth + 1);
      var lo = [], eq = [], hi = [];
      list.forEach(function (v) { c.compares += 1; (v < pivot ? lo : v > pivot ? hi : eq).push(v); });
      trace.push({ at: trace.length, depth: depth, n: list.length, groups: groups.length,
                   pivot: pivot, less: lo.length, equal: eq.length, greater: hi.length,
                   guarantee: Math.floor(3 * list.length / 10) });
      if (want <= lo.length) return select(lo, want, depth + 1);
      if (want <= lo.length + eq.length) return pivot;
      return select(hi, want - lo.length - eq.length, depth + 1);
    }
    var value = select(a.slice(), k, 0);
    var qs = quickselectRun(a, k, 'last');
    return runOf({ value: value, quickselectValue: qs.result.value,
                   quickselectCompares: qs.counts.compares || 0,
                   agrees: value === qs.result.value }, usedCounts(c), trace);
  }
  /* The recursion tree of T(n) = T(f1 n) + T(f2 n) + n, level by level, as
     exact rationals. The level sum is (f1 + f2)^i * n, so the tree is geometric
     and the total is n / (1 - (f1 + f2)) when the sum is under 1 -- which is
     the median-of-medians recurrence's whole argument, at f1 = 1/5, f2 = 7/10. */
  function levelSums(f1, f2, n, levels) {
    var ratio = Radd(f1, f2), rows = [], cur = R(BigInt(n), 1n), total = R(0n, 1n);
    for (var i = 0; i < (levels || 8); i += 1) {
      rows.push({ level: i, sum: cur });
      total = Radd(total, cur);
      cur = Rmul(cur, ratio);
    }
    var one = R(1n, 1n), geometric = Rcmp(ratio, one) < 0
      ? Rdiv(R(BigInt(n), 1n), Rsub(one, ratio)) : null;
    return { ratio: ratio, rows: rows, partial: total, geometric: geometric,
             converges: Rcmp(ratio, one) < 0 };
  }

  /* The adversary that forces n - 1 comparisons for the maximum: every element
     except one must LOSE at least once, and the adversary answers so that no
     comparison makes two elements lose at the same time. */
  function adversaryMax(n) {
    var lost = new Array(n).fill(false), compares = 0, trace = [];
    return {
      ask: function (i, j) {
        compares += 1;
        var winner;
        if (lost[i] && !lost[j]) winner = j;
        else if (lost[j] && !lost[i]) winner = i;
        else winner = Math.min(i, j);          /* deterministic, so a reader can replay it */
        var loser = winner === i ? j : i;
        var newInfo = !lost[loser];
        lost[loser] = true;
        trace.push({ at: trace.length, i: i, j: j, winner: winner, newInfo: newInfo });
        return winner;
      },
      state: function () {
        var unbeaten = [];
        for (var v = 0; v < n; v += 1) if (!lost[v]) unbeaten.push(v);
        return { compares: compares, unbeaten: unbeaten, lower: n - 1,
                 settled: unbeaten.length === 1, trace: trace };
      }
    };
  }
  /* Second largest by a tournament: n - 1 comparisons to find the winner, then
     the second is the best of the ceil(log2 n) elements that lost to it. */
  function tournament(a) {
    var c = counter(), round = a.map(function (v, i) { return { value: v, beatenBy: [], id: i }; });
    var rounds = [];
    while (round.length > 1) {
      var next = [], i;
      for (i = 0; i + 1 < round.length; i += 2) {
        c.compares += 1;
        var win = round[i].value >= round[i + 1].value ? round[i] : round[i + 1];
        var lose = win === round[i] ? round[i + 1] : round[i];
        win.beatenBy.push(lose);
        next.push(win);
      }
      if (round.length % 2) next.push(round[round.length - 1]);
      rounds.push(next.map(function (x) { return x.value; }));
      round = next;
    }
    var champ = round[0], second = null;
    champ.beatenBy.forEach(function (x) {
      /* k candidates need k - 1 comparisons, not k: the first one is taken,
         not compared. Counting it would put the total one over the bound the
         lesson asks the reader to check it against. */
      if (second === null) { second = x.value; return; }
      c.compares += 1;
      if (x.value > second) second = x.value;
    });
    var bound = a.length - 1 + Math.ceil(Math.log2(Math.max(2, a.length))) - 1;
    return runOf({ max: champ.value, second: second, rounds: rounds,
                   candidates: champ.beatenBy.length, bound: bound },
                 usedCounts(c), []);
  }
"""


# ---------------------------------------------- 4.6 graphkit (course 3)

GRAPHKIT_JS = r"""
  /* Traversal, trees and shortest paths on a DIGRAPH_JS graph.

     Four of these answer a question GRAPH_JS already answers by brute force,
     and that is deliberate: `lowLink` against `cuts()`, which deletes each edge
     and recounts components; `kruskalRun` against `kruskal()`; `relaxRun`
     against `dijkstra()`; and the tour oracles against `hamilton()`. Where two
     routines answer the same question, mathcheck asserts they agree -- which is
     worth more than either test alone, because the two are written from
     different definitions.

     An arc is excluded from a traversal by ID, not by endpoint. On a multigraph
     -- which this representation allows and GRAPH_JS's matrix cannot -- "do not
     go back the way you came" is a statement about the arc, and a lowlink that
     compared endpoints would call a genuine parallel edge a bridge. */

  function dfsTimes(G, roots) {
    var idx = dgIndex(G), c = counter(), n = G.n;
    var d = new Array(n).fill(0), f = new Array(n).fill(0), parent = new Array(n).fill(-1);
    var colour = new Array(n).fill('white'), order = [], time = 0, forest = [];
    function visit(v) {
      c.calls += 1;
      time += 1; d[v] = time; colour[v] = 'grey'; order.push(v);
      idx.out[v].forEach(function (id) {
        var u = dgOther(G, id, v);
        c.reads += 1;
        if (colour[u] === 'white') { parent[u] = v; visit(u); }
      });
      colour[v] = 'black';
      time += 1; f[v] = time;
    }
    var starts = roots && roots.length ? roots : (function () {
      var a = [];
      for (var i = 0; i < n; i += 1) a.push(i);
      return a;
    })();
    starts.forEach(function (s) { if (colour[s] === 'white') { forest.push(s); visit(s); } });
    return runOf({ d: d, f: f, parent: parent, order: order, roots: forest },
                 usedCounts(c), []);
  }
  /* Every arc classified from the discovery and finish times, which is the
     definition the lesson gives: tree if the arc is the one that discovered its
     head; back if the head is a grey ancestor (d[u] < d[v] < f[v] < f[u]);
     forward if the head is a finished descendant; cross otherwise. */
  function classifyEdges(G, times) {
    var d = times.d, f = times.f, parent = times.parent;
    return G.arcs.map(function (a, id) {
      var u = a.u, v = a.v, kind;
      if (parent[v] === u && d[v] > d[u]) kind = 'tree';
      else if (d[v] <= d[u] && f[u] <= f[v]) kind = 'back';
      else if (d[u] < d[v] && f[v] < f[u]) kind = 'forward';
      else kind = 'cross';
      return { id: id, u: u, v: v, kind: kind };
    });
  }
  function edgeKindCounts(list) {
    var out = { tree: 0, back: 0, forward: 0, cross: 0 };
    list.forEach(function (e) { out[e.kind] += 1; });
    return out;
  }

  /* Topological order two ways. The DFS one is the reverse of the finishing
     order; Kahn's is the in-degree queue. They can differ and both be right,
     which is the lesson -- and if there is a cycle neither exists, so the DFS
     arm returns the back edge as the certificate. */
  function topoDfs(G) {
    var t = dfsTimes(G);
    var kinds = classifyEdges(G, t.result);
    var back = kinds.filter(function (e) { return e.kind === 'back'; });
    var order = G.arcs.length >= 0 ? (function () {
      var vs = [];
      for (var i = 0; i < G.n; i += 1) vs.push(i);
      return vs.sort(function (a, b) { return t.result.f[b] - t.result.f[a]; });
    })() : [];
    return runOf({ order: back.length ? null : order, backEdge: back.length ? back[0] : null,
                   acyclic: back.length === 0, finish: t.result.f },
                 t.counts, []);
  }
  function topoKahn(G) {
    var idx = dgIndex(G), c = counter(), indeg = new Array(G.n).fill(0), i;
    G.arcs.forEach(function (a) { indeg[a.v] += 1; });
    var start = indeg.slice(), queue = [], order = [], trace = [];
    for (i = 0; i < G.n; i += 1) if (!indeg[i]) queue.push(i);
    while (queue.length) {
      queue.sort(function (a, b) { return a - b; });    /* deterministic ties */
      var v = queue.shift();
      order.push(v); c.pops += 1;
      trace.push({ at: trace.length, took: v, indeg: indeg.slice(), queue: queue.slice() });
      idx.out[v].forEach(function (id) {
        var u = dgOther(G, id, v);
        indeg[u] -= 1; c.reads += 1;
        if (!indeg[u]) { queue.push(u); c.pushes += 1; }
      });
    }
    return runOf({ order: order.length === G.n ? order : null, indegree: start,
                   acyclic: order.length === G.n, stuckAt: order.length },
                 usedCounts(c), trace);
  }

  /* Tarjan's low-link, on the UNDIRECTED reading of the graph: bridges and cut
     vertices in one pass, against GRAPH_JS.cuts()'s delete-and-recount. */
  function lowLink(G) {
    var idx = dgIndex(G), c = counter(), n = G.n;
    var d = new Array(n).fill(-1), low = new Array(n).fill(-1), parentArc = new Array(n).fill(-1);
    var time = 0, bridges = [], cutVertices = [], trace = [];
    function visit(v, fromArc) {
      c.calls += 1;
      time += 1; d[v] = time; low[v] = time;
      var children = 0, isCut = false;
      idx.out[v].concat(idx.inn[v]).forEach(function (id) {
        if (id === fromArc) return;               /* by ARC, not by endpoint */
        var u = dgOther(G, id, v);
        if (u === v) return;
        c.reads += 1;
        if (d[u] === -1) {
          children += 1;
          parentArc[u] = id;
          visit(u, id);
          if (low[u] < low[v]) low[v] = low[u];
          if (low[u] > d[v]) bridges.push({ id: id, u: v, v: u });
          if (fromArc !== -1 && low[u] >= d[v]) isCut = true;
        } else if (d[u] < low[v]) low[v] = d[u];
      });
      if (fromArc === -1 && children > 1) isCut = true;
      if (isCut) cutVertices.push(v);
      trace.push({ at: trace.length, v: v, d: d[v], low: low[v] });
    }
    for (var s = 0; s < n; s += 1) if (d[s] === -1) visit(s, -1);
    return runOf({ d: d, low: low, bridges: bridges,
                   cutVertices: cutVertices.sort(function (a, b) { return a - b; }) },
                 usedCounts(c), trace);
  }

  /* Kosaraju: finishing order on G, then components on the reverse. Both passes
     are returned because the mode steps through them, and so is the
     condensation, which is the acyclic graph the lesson says always results. */
  function kosaraju(G) {
    var c = counter(), first = dfsTimes(G), n = G.n, i;
    var order = [];
    for (i = 0; i < n; i += 1) order.push(i);
    order.sort(function (a, b) { return first.result.f[b] - first.result.f[a]; });
    var Gr = dgReverse(G), idx = dgIndex(Gr);
    var comp = new Array(n).fill(-1), comps = [];
    order.forEach(function (s) {
      if (comp[s] !== -1) return;
      var id = comps.length, stack = [s], members = [];
      comp[s] = id;
      while (stack.length) {
        var v = stack.pop();
        members.push(v); c.calls += 1;
        idx.out[v].forEach(function (aid) {
          var u = dgOther(Gr, aid, v);
          c.reads += 1;
          if (comp[u] === -1) { comp[u] = id; stack.push(u); }
        });
      }
      comps.push(members.sort(function (a, b) { return a - b; }));
    });
    var cond = dgNew(comps.length, true), seen = {};
    G.arcs.forEach(function (a) {
      if (comp[a.u] === comp[a.v]) return;
      var key = comp[a.u] + '>' + comp[a.v];
      if (seen[key]) return;
      seen[key] = true;
      dgAdd(cond, comp[a.u], comp[a.v], 1, 0);
    });
    return runOf({ components: comps, componentOf: comp, order: order, condensation: cond,
                   condensationAcyclic: topoDfs(cond).result.acyclic },
                 usedCounts(c), []);
  }

  /* The cut property, checked rather than asserted: the arcs crossing (S, V-S)
     and the lightest of them, which must be in every minimum spanning tree. */
  function crossingEdges(G, S) {
    var inS = new Array(G.n).fill(false);
    S.forEach(function (v) { inS[v] = true; });
    var crossing = [];
    G.arcs.forEach(function (a, id) {
      if (inS[a.u] !== inS[a.v]) crossing.push({ id: id, u: a.u, v: a.v, w: a.w });
    });
    var lightest = null;
    crossing.forEach(function (e) { if (!lightest || e.w < lightest.w) lightest = e; });
    return { crossing: crossing, lightest: lightest };
  }
  /* EVERY spanning tree, so the cut property's "in every MST" can be checked by
     looking at every one of them. V <= 7 -- C(21, 6) is 54 264 subsets at V = 7
     and 735 471 at V = 8, which is where the tab stops being interactive. */
  function allSpanningTrees(G, cap) {
    cap = cap === undefined ? 7 : cap;
    oracleCap('allSpanningTrees', G.n, cap);
    var m = G.arcs.length, need = G.n - 1, trees = [], examined = 0;
    var chosen = [];
    (function pick(start) {
      if (chosen.length === need) {
        examined += 1;
        var H = dgNew(G.n, false);
        chosen.forEach(function (id) { dgAdd(H, G.arcs[id].u, G.arcs[id].v, G.arcs[id].w, 0); });
        if (dgComponents(H).length === 1) {
          trees.push({ arcs: chosen.slice(),
                       weight: chosen.reduce(function (t, id) { return t + G.arcs[id].w; }, 0) });
        }
        return;
      }
      for (var id = start; id < m; id += 1) {
        if (m - id < need - chosen.length) break;
        chosen.push(id);
        pick(id + 1);
        chosen.pop();
      }
    })(0);
    var best = null;
    trees.forEach(function (t) { if (best === null || t.weight < best) best = t.weight; });
    return runOf({ trees: trees, count: trees.length, minWeight: best },
                 { nodes: examined }, []);
  }

  /* A binary heap keyed on a number, for the two mode panels that show the heap
     contents. Lazy: a decrease-key is a second push, and the stale entry is
     skipped on the way out, which is what a real implementation does and what
     makes "operations against E log V" the right comparison. */
  function pqNew() { return { items: [] }; }
  function pqPush(q, key, v, c) {
    q.items.push({ key: key, v: v });
    var i = q.items.length - 1;
    while (i > 0) {
      var p = (i - 1) >> 1;
      if (c) c.compares += 1;
      if (q.items[i].key >= q.items[p].key) break;
      var t = q.items[i]; q.items[i] = q.items[p]; q.items[p] = t;
      i = p;
    }
    if (c) c.pushes += 1;
  }
  function pqPop(q, c) {
    if (!q.items.length) return null;
    var top = q.items[0], last = q.items.pop();
    if (q.items.length) {
      q.items[0] = last;
      var i = 0;
      while (true) {
        var l = 2 * i + 1, r = l + 1, best = i;
        if (l < q.items.length) { if (c) c.compares += 1; if (q.items[l].key < q.items[best].key) best = l; }
        if (r < q.items.length) { if (c) c.compares += 1; if (q.items[r].key < q.items[best].key) best = r; }
        if (best === i) break;
        var t = q.items[i]; q.items[i] = q.items[best]; q.items[best] = t;
        i = best;
      }
    }
    if (c) c.pops += 1;
    return top;
  }

  function primRun(G, start) {
    var idx = dgIndex(G), c = counter(), s = start || 0;
    var inTree = new Array(G.n).fill(false), q = pqNew(), chosen = [], total = 0, trace = [];
    inTree[s] = true;
    idx.out[s].forEach(function (id) { pqPush(q, G.arcs[id].w, id, c); });
    while (q.items.length && chosen.length < G.n - 1) {
      var top = pqPop(q, c);
      var a = G.arcs[top.v];
      var u = inTree[a.u] ? a.v : a.u;
      if (inTree[a.u] && inTree[a.v]) {
        trace.push({ at: trace.length, arc: top.v, w: top.key, taken: false, reason: 'both ends already in the tree' });
        continue;
      }
      inTree[u] = true;
      chosen.push(top.v); total += top.key;
      trace.push({ at: trace.length, arc: top.v, w: top.key, taken: true, added: u,
                   heap: q.items.map(function (it) { return it.key; }) });
      idx.out[u].forEach(function (id) {
        var other = dgOther(G, id, u);
        if (!inTree[other]) pqPush(q, G.arcs[id].w, id, c);
      });
    }
    return runOf({ arcs: chosen, weight: total, spanning: chosen.length === G.n - 1,
                   bound: G.arcs.length * ilog2(Math.max(2, G.n)) },
                 usedCounts(c), trace);
  }

  /* Kruskal with the union-find state per edge and the REASON an edge was
     rejected, which is the panel's content. Checked against GRAPH_JS.kruskal()
     on the same weights. */
  function kruskalRun(G) {
    var c = counter(), order = G.arcs.map(function (a, id) { return id; }).sort(function (x, y) {
      var a = G.arcs[x], b = G.arcs[y];
      return a.w - b.w || a.u - b.u || a.v - b.v;
    });
    var parent = [], i;
    for (i = 0; i < G.n; i += 1) parent.push(i);
    function find(x) { var hops = 0; while (parent[x] !== x) { x = parent[x]; hops += 1; } c.hops += hops; c.finds += 1; return x; }
    var chosen = [], total = 0, trace = [];
    order.forEach(function (id) {
      var a = G.arcs[id], ra = find(a.u), rb = find(a.v);
      if (ra === rb) {
        trace.push({ at: trace.length, arc: id, w: a.w, taken: false,
                     reason: 'both ends are already connected', parent: parent.slice() });
        return;
      }
      parent[ra] = rb; c.unions += 1;
      chosen.push(id); total += a.w;
      trace.push({ at: trace.length, arc: id, w: a.w, taken: true, parent: parent.slice() });
    });
    return runOf({ arcs: chosen, weight: total, order: order,
                   spanning: chosen.length === G.n - 1 }, usedCounts(c), trace);
  }

  /* Dijkstra, with the relaxation SCHEDULE as a parameter, because the mode's
     content is that the schedule changes the work and not the answer:
     'heap' takes the closest unfinished vertex, 'scan' takes the lowest index,
     'insertion' relaxes arcs in arc order over and over. All three must reach
     the same distances on a non-negative graph. */
  function relaxRun(G, source, schedule) {
    var idx = dgIndex(G), c = counter(), n = G.n;
    var dist = new Array(n).fill(null), parent = new Array(n).fill(-1), done = new Array(n).fill(false);
    var trace = [], negative = G.arcs.some(function (a) { return a.w < 0; });
    dist[source] = 0;
    if (schedule === 'insertion') {
      var changed = true, round = 0;
      while (changed && round <= n) {
        changed = false; round += 1;
        G.arcs.forEach(function (a, id) {
          var ends = G.directed ? [[a.u, a.v]] : [[a.u, a.v], [a.v, a.u]];
          ends.forEach(function (e) {
            if (dist[e[0]] === null) return;
            c.relaxations += 1;
            if (dist[e[1]] === null || dist[e[0]] + a.w < dist[e[1]]) {
              dist[e[1]] = dist[e[0]] + a.w; parent[e[1]] = e[0]; changed = true;
              trace.push({ at: trace.length, round: round, arc: id, to: e[1], dist: dist.slice() });
            }
          });
        });
      }
      return runOf({ dist: dist, parent: parent, negativeWeights: negative, rounds: round },
                   usedCounts(c), trace);
    }
    var q = pqNew();
    pqPush(q, 0, source, c);
    for (var it = 0; it < 4 * n + 4 * G.arcs.length; it += 1) {
      var v = -1;
      if (schedule === 'scan') {
        for (var k = 0; k < n; k += 1) {
          c.reads += 1;
          if (!done[k] && dist[k] !== null && (v === -1 || dist[k] < dist[v])) v = k;
        }
        if (v === -1) break;
      } else {
        var top = pqPop(q, c);
        if (!top) break;
        if (done[top.v]) continue;
        v = top.v;
      }
      done[v] = true;
      trace.push({ at: trace.length, settled: v, d: dist[v], dist: dist.slice() });
      idx.out[v].forEach(function (id) {
        var a = G.arcs[id], u = dgOther(G, id, v);
        c.relaxations += 1;
        if (dist[u] === null || dist[v] + a.w < dist[u]) {
          dist[u] = dist[v] + a.w; parent[u] = v;
          if (schedule !== 'scan') pqPush(q, dist[u], u, c);
        }
      });
    }
    return runOf({ dist: dist, parent: parent, settled: done, negativeWeights: negative },
                 usedCounts(c), trace);
  }

  /* Bellman-Ford, round by round, which is the table the mode steps through.
     Round i holds every shortest path of at most i arcs, so the round a label
     stops changing is the number of arcs on its shortest path -- and a label
     that still improves in round n is the negative-cycle certificate, returned
     as the cycle itself rather than as a boolean. */
  function bellmanFordRounds(G, source) {
    var c = counter(), n = G.n;
    var dist = new Array(n).fill(null), parent = new Array(n).fill(-1);
    var rounds = [], finalAt = new Array(n).fill(-1);
    dist[source] = 0; finalAt[source] = 0;
    for (var i = 1; i <= n; i += 1) {
      var changed = [];
      G.arcs.forEach(function (a, id) {
        var ends = G.directed ? [[a.u, a.v]] : [[a.u, a.v], [a.v, a.u]];
        ends.forEach(function (e) {
          if (dist[e[0]] === null) return;
          c.relaxations += 1;
          if (dist[e[1]] === null || dist[e[0]] + a.w < dist[e[1]]) {
            dist[e[1]] = dist[e[0]] + a.w; parent[e[1]] = e[0];
            changed.push(e[1]); finalAt[e[1]] = i;
          }
        });
      });
      rounds.push({ round: i, dist: dist.slice(), changed: changed.slice() });
      if (!changed.length && i < n) break;
    }
    var last = rounds[rounds.length - 1];
    var cycle = null;
    if (rounds.length === n && last.changed.length) {
      /* Walk the parent pointers back n times from a vertex that still moved:
         that lands inside the cycle, and following it round closes it. */
      var v = last.changed[0];
      for (var k = 0; k < n; k += 1) v = parent[v];
      var loop = [v], at = parent[v];
      while (at !== v && at !== -1 && loop.length <= n + 1) { loop.push(at); at = parent[at]; }
      loop.push(v);
      cycle = loop.reverse();
    }
    return runOf({ dist: dist, parent: parent, rounds: rounds, finalAt: finalAt,
                   negativeCycle: cycle },
                 usedCounts(c), rounds);
  }

  /* One pass in topological order, which is all a DAG needs -- and with the
     sign flipped it is the LONGEST path, which no algorithm here can do on a
     general graph. Slack is the difference between the earliest and the latest
     a vertex can be scheduled, which is the critical-path reading of it. */
  function dagRelax(G, source, sign) {
    var topo = topoDfs(G);
    if (!topo.result.order) return runOf({ dist: null, acyclic: false }, {}, []);
    var s = sign === undefined ? 1 : sign, idx = dgIndex(G), c = counter();
    var dist = new Array(G.n).fill(null), parent = new Array(G.n).fill(-1), trace = [];
    dist[source] = 0;
    topo.result.order.forEach(function (v) {
      if (dist[v] === null) return;
      idx.out[v].forEach(function (id) {
        var a = G.arcs[id], u = dgOther(G, id, v);
        c.relaxations += 1;
        if (dist[u] === null || s * (dist[v] + a.w) < s * dist[u]) {
          dist[u] = dist[v] + a.w; parent[u] = v;
          trace.push({ at: trace.length, from: v, to: u, dist: dist.slice() });
        }
      });
    });
    /* Latest start: relax backwards from the finish under the same sign. */
    var latest = dist.slice(), order = topo.result.order.slice().reverse();
    var finish = null;
    dist.forEach(function (d, v) { if (d !== null && (finish === null || s * d > s * dist[finish])) finish = v; });
    order.forEach(function (v) {
      idx.out[v].forEach(function (id) {
        var a = G.arcs[id], u = dgOther(G, id, v);
        if (latest[u] === null) return;
        var cand = latest[u] - a.w;
        if (latest[v] === null || s * cand < s * latest[v]) latest[v] = cand;
      });
    });
    var slack = dist.map(function (d, v) { return d === null ? null : latest[v] - d; });
    return runOf({ dist: dist, parent: parent, latest: latest, slack: slack,
                   acyclic: true, extreme: finish, order: topo.result.order },
                 usedCounts(c), trace);
  }

  /* Floyd-Warshall, with the matrix kept after every k so the mode can step
     through them, and next[] for the path. The k loop OUTSIDE is the whole
     content: it says "paths whose interior lies in {0..k}", and writing the
     loops in any other order computes something else that often looks right. */
  function floydSteps(W) {
    var n = W.length, c = counter(), i, j, k;
    var D = W.map(function (r) { return r.slice(); });
    var next = [];
    for (i = 0; i < n; i += 1) {
      next.push([]);
      for (j = 0; j < n; j += 1) next[i].push(D[i][j] === null ? null : j);
    }
    var steps = [];
    for (k = 0; k < n; k += 1) {
      for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) {
        c.relaxations += 1;
        if (D[i][k] === null || D[k][j] === null) continue;
        var via = D[i][k] + D[k][j];
        if (D[i][j] === null || via < D[i][j]) { D[i][j] = via; next[i][j] = next[i][k]; }
      }
      steps.push({ k: k, matrix: D.map(function (r) { return r.slice(); }) });
    }
    var negative = [];
    for (i = 0; i < n; i += 1) if (D[i][i] !== null && D[i][i] < 0) negative.push(i);
    return runOf({ dist: D, next: next, steps: steps, negativeCycleAt: negative },
                 usedCounts(c), steps);
  }
  function floydPath(next, i, j) {
    if (next[i][j] === null) return null;
    var path = [i];
    while (i !== j) { i = next[i][j]; path.push(i); if (path.length > next.length + 1) return null; }
    return path;
  }
"""


# ------------------------------------------------ 4.7 flowkit (course 3)

FLOW_JS = r"""
  /* Maximum flow on a DIGRAPH_JS network. A flow is an array parallel to
     G.arcs, so `f[id]` is the flow on arc id -- which is why the
     representation had to carry arc identity: a residual network has an arc in
     each direction between the same pair, and a triple [u, v, w] cannot say
     which original arc a reverse arc undoes.

     THE REVERSE ARC IS THE SUBJECT. Every residual arc here records the arc it
     came from and whether it is the forward or the backward one, and
     `maxflow(G, s, t, { reverse: false })` builds the residual network WITHOUT
     the backward arcs, which is the failure the lesson wants on screen: the
     forward-only search gets stuck at a flow that is not maximum, and the
     reader sees that undoing an earlier choice is not an optimisation but the
     reason the algorithm is correct. */

  function zeroFlow(G) { return new Array(G.arcs.length).fill(0); }

  /* The residual network as a graph in its own right, so every routine that
     takes a graph works on it. Each residual arc carries { from, forward }. */
  function residual(G, f, opts) {
    opts = opts || {};
    var Rg = dgNew(G.n, true), meta = [];
    G.arcs.forEach(function (a, id) {
      var left = a.cap - f[id];
      if (left > 0) { dgAdd(Rg, a.u, a.v, a.w, left); meta.push({ from: id, forward: true, residual: left }); }
      if (opts.reverse !== false && f[id] > 0) {
        dgAdd(Rg, a.v, a.u, -a.w, f[id]);
        meta.push({ from: id, forward: false, residual: f[id] });
      }
    });
    return { graph: Rg, meta: meta };
  }
  /* The SHORTEST augmenting path, in arcs -- Edmonds-Karp, so the number of
     augmentations is bounded by VE/2 and the mode can print it. */
  function bfsPath(res, s, t) {
    var G = res.graph, idx = dgIndex(G), prev = new Array(G.n).fill(-1);
    var seen = new Array(G.n).fill(false), queue = [s], order = [];
    seen[s] = true;
    while (queue.length) {
      var v = queue.shift();
      order.push(v);
      if (v === t) break;
      idx.out[v].forEach(function (id) {
        var u = G.arcs[id].v;
        if (seen[u] || G.arcs[id].cap <= 0) return;
        seen[u] = true; prev[u] = id; queue.push(u);
      });
    }
    if (!seen[t]) return { path: null, reachable: order };
    var path = [], at = t;
    while (at !== s) { path.push(prev[at]); at = G.arcs[prev[at]].u; }
    return { path: path.reverse(), reachable: order };
  }
  /* Push the bottleneck along one residual path, forward arcs up and backward
     arcs DOWN -- which is the line that makes the algorithm correct. */
  function augment(G, f, res, path) {
    var bottleneck = null;
    path.forEach(function (rid) {
      var left = res.graph.arcs[rid].cap;
      if (bottleneck === null || left < bottleneck) bottleneck = left;
    });
    var out = f.slice();
    path.forEach(function (rid) {
      var m = res.meta[rid];
      out[m.from] += m.forward ? bottleneck : -bottleneck;
    });
    return { flow: out, bottleneck: bottleneck };
  }
  function flowValue(G, f, s) {
    var v = 0;
    G.arcs.forEach(function (a, id) {
      if (a.u === s) v += f[id];
      if (a.v === s) v -= f[id];
    });
    return v;
  }
  function maxflow(G, s, t, opts) {
    opts = opts || {};
    var f = zeroFlow(G), c = counter(), trace = [], guard = 0;
    while (guard < 10000) {
      guard += 1;
      var res = residual(G, f, opts);
      var found = bfsPath(res, s, t);
      if (!found.path) {
        trace.push({ at: trace.length, done: true, reachable: found.reachable });
        break;
      }
      var a = augment(G, f, res, found.path);
      f = a.flow;
      c.rounds += 1;
      trace.push({ at: trace.length, path: found.path.map(function (rid) {
                     return { u: res.graph.arcs[rid].u, v: res.graph.arcs[rid].v,
                              forward: res.meta[rid].forward };
                   }), bottleneck: a.bottleneck, value: flowValue(G, f, s) });
    }
    var conserved = true;
    for (var v = 0; v < G.n; v += 1) {
      if (v === s || v === t) continue;
      var net = 0;
      G.arcs.forEach(function (arc, id) {
        if (arc.u === v) net -= f[id];
        if (arc.v === v) net += f[id];
      });
      if (net !== 0) conserved = false;
    }
    return runOf({ flow: f, value: flowValue(G, f, s), conserved: conserved,
                   augmentations: c.rounds, residual: residual(G, f, opts) },
                 usedCounts(c), trace);
  }
  /* The minimum cut, read off the final residual network: everything reachable
     from s. The panel's check is that its capacity EQUALS the flow value, which
     is the theorem, and that every crossing arc is saturated -- and the mode
     also shows a set of saturated arcs that is not a cut, because "saturated"
     and "a cut" are different properties and conflating them is the
     misconception. */
  function minCutFrom(G, f, s) {
    var res = residual(G, f), idx = dgIndex(res.graph);
    var seen = new Array(G.n).fill(false), stack = [s];
    seen[s] = true;
    while (stack.length) {
      var v = stack.pop();
      idx.out[v].forEach(function (id) {
        var u = res.graph.arcs[id].v;
        if (!seen[u] && res.graph.arcs[id].cap > 0) { seen[u] = true; stack.push(u); }
      });
    }
    var S = [], T = [], arcs = [], capacity = 0;
    for (var i = 0; i < G.n; i += 1) (seen[i] ? S : T).push(i);
    G.arcs.forEach(function (a, id) {
      if (seen[a.u] && !seen[a.v]) { arcs.push({ id: id, u: a.u, v: a.v, cap: a.cap, flow: f[id] }); capacity += a.cap; }
    });
    return { S: S, T: T, arcs: arcs, capacity: capacity,
             allSaturated: arcs.every(function (e) { return e.flow === e.cap; }) };
  }

  /* Bipartite matching as a flow: a unit-capacity arc from the source to every
     left vertex, from every left vertex to each of its right neighbours, and
     from every right vertex to the sink. The matching is the saturated middle
     layer, and the cut read back is a vertex cover of the same size -- which is
     Konig's theorem, on the page as two numbers that agree. */
  function matchingNetwork(left, right, pairs) {
    var n = left + right + 2, s = left + right, t = s + 1;
    var G = dgNew(n, true), middle = [];
    for (var i = 0; i < left; i += 1) dgAdd(G, s, i, 0, 1);
    pairs.forEach(function (p) { middle.push(dgAdd(G, p[0], left + p[1], 0, 1)); });
    for (var j = 0; j < right; j += 1) dgAdd(G, left + j, t, 0, 1);
    return { graph: G, s: s, t: t, left: left, right: right, middle: middle };
  }
  function matchingFrom(net, f) {
    var out = [];
    net.middle.forEach(function (id) {
      if (f[id] > 0) out.push({ left: net.graph.arcs[id].u, right: net.graph.arcs[id].v - net.left });
    });
    return out;
  }
  /* Konig: from the minimum cut, the cover is (left vertices NOT reachable)
     together with (right vertices reachable). */
  function konigCover(net, f) {
    var cut = minCutFrom(net.graph, f, net.s), inS = {};
    cut.S.forEach(function (v) { inS[v] = true; });
    var cover = [];
    for (var i = 0; i < net.left; i += 1) if (!inS[i]) cover.push({ side: 'left', v: i });
    for (var j = 0; j < net.right; j += 1) if (inS[net.left + j]) cover.push({ side: 'right', v: j });
    return { cover: cover, size: cover.length, cut: cut };
  }

  /* The three transformations course 3 asks the reader to build, each returning
     the new network beside the correspondence that makes the answer readable
     back on the original.
       'split'       a vertex capacity becomes an arc from v_in to v_out
       'unit'        every capacity set to 1, for a disjoint-paths question
       'supersource' several sources and sinks become one of each */
  function gadgetBuild(kind, spec) {
    if (kind === 'split') {
      var n = spec.graph.n, G = dgNew(2 * n, true), map = [];
      for (var v = 0; v < n; v += 1) {
        map.push({ v: v, inV: v, outV: n + v });
        dgAdd(G, v, n + v, 0, spec.vertexCap[v] === undefined ? Infinity : spec.vertexCap[v]);
      }
      spec.graph.arcs.forEach(function (a) { dgAdd(G, n + a.u, a.v, a.w, a.cap); });
      return { graph: G, map: map, s: spec.s, t: n + spec.t,
               note: 'each vertex became an in-copy and an out-copy joined by its capacity' };
    }
    if (kind === 'unit') {
      var U = dgCopy(spec.graph);
      U.arcs.forEach(function (a) { a.cap = 1; });
      return { graph: U, s: spec.s, t: spec.t,
               note: 'every capacity is 1, so the flow value counts arc-disjoint paths' };
    }
    if (kind === 'supersource') {
      var H = dgCopy(spec.graph), S = H.n, T = H.n + 1;
      H.n += 2;
      spec.sources.forEach(function (v) { dgAdd(H, S, v, 0, spec.sourceCap ? spec.sourceCap[v] : Infinity); });
      spec.sinks.forEach(function (v) { dgAdd(H, v, T, 0, spec.sinkCap ? spec.sinkCap[v] : Infinity); });
      return { graph: H, s: S, t: T,
               note: 'one super-source and one super-sink, so a many-to-many flow is a single s-t flow' };
    }
    throw new Error('unknown gadget: ' + kind);
  }
"""


# ------------------------------------------------- 4.8 greedy (course 4)

GREEDY_JS = r"""
  /* Greedy algorithms, each run beside the optimum it claims to reach.

     The kit's whole method is that "greedy is optimal here" is checked and not
     asserted, so every mode has a brute-force arm -- ORACLE_JS's bruteOptimal
     and knapsackBrute, and this block's allFullBinaryTrees and
     independenceEnumerate, which only this kit needs.

     `caching` has no code here at all: sysdesign_core.replayPolicy(trace, k,
     policy) already implements FIFO, LRU and farthest-in-future on a reference
     trace and returns the exact hit rate, and its own comment says
     farthest-in-future belongs in a core because it is the BOUND the lesson
     rests on. It is reused as it ships. */

  /* Interval scheduling. Intervals are { s, f, label }. */
  var INTERVAL_RULES = {
    earliestFinish: function (a, b) { return a.f - b.f || a.s - b.s; },
    earliestStart: function (a, b) { return a.s - b.s || a.f - b.f; },
    shortest: function (a, b) { return (a.f - a.s) - (b.f - b.s) || a.s - b.s; },
    fewestConflicts: null
  };
  function conflictCount(items, x) {
    var n = 0;
    items.forEach(function (y) { if (y !== x && y.s < x.f && x.s < y.f) n += 1; });
    return n;
  }
  function greedyIntervals(items, rule) {
    var order = items.slice(), c = counter(), chosen = [], trace = [];
    if (rule === 'fewestConflicts') {
      order.sort(function (a, b) { return conflictCount(items, a) - conflictCount(items, b) || a.s - b.s; });
    } else {
      var cmp = INTERVAL_RULES[rule];
      if (!cmp) throw new Error('unknown rule: ' + rule);
      order.sort(cmp);
    }
    var lastFinish = -Infinity;
    order.forEach(function (x) {
      c.compares += 1;
      var ok = x.s >= lastFinish;
      if (ok) { chosen.push(x); lastFinish = x.f; }
      trace.push({ at: trace.length, item: x, taken: ok, finishSoFar: lastFinish });
    });
    return { chosen: chosen, trace: trace, counts: usedCounts(c) };
  }
  /* STAYS AHEAD, step by step: g_i is the finish time of greedy's i-th
     interval, o_i the optimum's, and the claim is g_i <= o_i for every i. The
     optimum comes from ORACLE_JS.bruteOptimal over every subset, so the wrong
     rules can be shown FALLING BEHIND at a named step rather than merely
     ending smaller. */
  function greedyTrace(items, rule) {
    var g = greedyIntervals(items, rule);
    var opt = bruteOptimal(items, function (members) {
      var sel = members.map(function (i) { return items[i]; })
                       .sort(function (a, b) { return a.s - b.s; });
      for (var i = 1; i < sel.length; i += 1) if (sel[i].s < sel[i - 1].f) return null;
      return sel.length;
    });
    var best = opt.result.members.map(function (i) { return items[i]; })
                                 .sort(function (a, b) { return a.f - b.f; });
    var rows = [], fellBehind = null;
    for (var i = 0; i < Math.max(g.chosen.length, best.length); i += 1) {
      var gi = i < g.chosen.length ? g.chosen[i].f : null;
      var oi = i < best.length ? best[i].f : null;
      var ahead = gi !== null && oi !== null ? gi <= oi : null;
      if (ahead === false && fellBehind === null) fellBehind = i;
      rows.push({ i: i + 1, g: gi, o: oi, ahead: ahead });
    }
    return runOf({ chosen: g.chosen, optimum: opt.result.value, optimal: best,
                   size: g.chosen.length, matchesOptimum: g.chosen.length === opt.result.value,
                   rows: rows, fellBehindAt: fellBehind },
                 g.counts, g.trace);
  }

  /* Interval partitioning: the depth is the most intervals live at any one
     point, and the claim is that the greedy by start time uses exactly that
     many rooms -- so the lab prints the point that attains the depth, which is
     the certificate that no fewer will do. */
  function depthOf(intervals) {
    var points = [], best = 0, at = null;
    intervals.forEach(function (x) { points.push(x.s); });
    points.sort(function (a, b) { return a - b; });
    points.forEach(function (t) {
      var live = intervals.filter(function (x) { return x.s <= t && t < x.f; });
      if (live.length > best) { best = live.length; at = t; }
    });
    return { depth: best, at: at };
  }
  function partitionRooms(intervals, order) {
    var list = intervals.slice(), c = counter(), rooms = [], trace = [];
    list.sort(order === 'finish' ? function (a, b) { return a.f - b.f; }
                                 : function (a, b) { return a.s - b.s; });
    list.forEach(function (x) {
      var put = -1;
      for (var r = 0; r < rooms.length; r += 1) {
        c.compares += 1;
        if (rooms[r][rooms[r].length - 1].f <= x.s) { put = r; break; }
      }
      if (put === -1) { rooms.push([x]); put = rooms.length - 1; }
      else rooms[put].push(x);
      trace.push({ at: trace.length, item: x, room: put + 1, rooms: rooms.length });
    });
    var d = depthOf(intervals);
    return runOf({ rooms: rooms, used: rooms.length, depth: d.depth, at: d.at,
                   optimal: rooms.length === d.depth }, usedCounts(c), trace);
  }

  /* Huffman. The merge sequence IS the lesson, so it is the trace; the tree is
     built from it and the expected codeword length is an exact rational. */
  function huffmanBuild(freqs) {
    var c = counter(), nodes = freqs.map(function (f, i) {
      return { symbol: f.symbol === undefined ? String(i) : f.symbol, weight: f.weight, l: null, r: null };
    });
    var live = nodes.slice(), trace = [];
    while (live.length > 1) {
      live.sort(function (a, b) { return a.weight - b.weight || String(a.symbol).localeCompare(String(b.symbol)); });
      c.compares += live.length;
      var x = live.shift(), y = live.shift();
      var merged = { symbol: null, weight: x.weight + y.weight, l: x, r: y };
      trace.push({ at: trace.length, took: [x.symbol, y.symbol], weights: [x.weight, y.weight],
                   made: merged.weight, remaining: live.length + 1 });
      live.push(merged);
      c.calls += 1;
    }
    var root = live[0] || null, codes = {};
    (function walk(n, prefix) {
      if (!n) return;
      if (!n.l && !n.r) { codes[n.symbol] = prefix || '0'; return; }
      walk(n.l, prefix + '0');
      walk(n.r, prefix + '1');
    })(root, '');
    return runOf({ root: root, codes: codes }, usedCounts(c), trace);
  }
  function huffKids(n) { return [n.l, n.r]; }
  /* Expected codeword length as an exact fraction, and the fixed-length code
     it is compared against -- which is ceil(log2 of the alphabet) bits. */
  function codeCost(codes, freqs) {
    var total = 0n, bits = 0n;
    freqs.forEach(function (f) {
      var sym = f.symbol === undefined ? null : f.symbol;
      var code = codes[sym];
      total += BigInt(f.weight);
      bits += BigInt(f.weight) * BigInt(code ? code.length : 0);
    });
    var fixed = Math.max(1, Math.ceil(Math.log2(Math.max(2, freqs.length))));
    return { bits: bits, total: total, expected: R(bits, total),
             fixed: R(BigInt(fixed), 1n),
             saving: Rsub(R(BigInt(fixed), 1n), R(bits, total)) };
  }
  /* EVERY full binary tree on n leaves, so Huffman's can be shown at the
     minimum rather than asserted to be. Catalan(n-1) of them: 14 at n = 5,
     42 at n = 6, 132 at n = 7 -- and the shapes stop being readable long
     before the count stops being computable, so the cap is 5 leaves. */
  function allFullBinaryTrees(n, cap) {
    cap = cap === undefined ? 5 : cap;
    oracleCap('allFullBinaryTrees', n, cap);
    function shapes(k) {
      if (k === 1) return [{ leaf: true }];
      var out = [];
      for (var i = 1; i < k; i += 1) {
        shapes(i).forEach(function (L) {
          shapes(k - i).forEach(function (Rt) { out.push({ leaf: false, l: L, r: Rt }); });
        });
      }
      return out;
    }
    return shapes(n);
  }
  /* Cost a shape against a weight assignment, over every assignment of the
     weights to its leaves -- which is what makes "Huffman is optimal" a
     statement the page can check. */
  function shapeCost(shape, weights) {
    var depths = [];
    (function walk(n, d) {
      if (n.leaf) { depths.push(d); return; }
      walk(n.l, d + 1); walk(n.r, d + 1);
    })(shape, 0);
    depths.sort(function (a, b) { return b - a; });
    var w = weights.slice().sort(function (a, b) { return a - b; });
    var total = 0n;
    for (var i = 0; i < depths.length; i += 1) total += BigInt(depths[i]) * BigInt(w[i]);
    return total;                    /* heaviest weight on the shallowest leaf */
  }

  /* Fractional knapsack, exactly: sort by value density -- a RATIO, so the
     comparison is Rcmp on fractions and not a float -- take whole items while
     they fit, then the fraction of the next that does. The optimum is a
     rational and the 0/1 optimum beside it is ORACLE_JS.knapsackBrute. */
  function fractionalKnapsack(items, W) {
    var order = items.map(function (it, i) { return { i: i, w: it.w, v: it.v, d: R(BigInt(it.v), BigInt(it.w)) }; });
    order.sort(function (a, b) { return -Rcmp(a.d, b.d) || a.i - b.i; });
    var left = W, value = R(0n, 1n), picks = [], c = counter();
    order.forEach(function (it) {
      c.compares += 1;
      if (left <= 0) return;
      if (it.w <= left) {
        left -= it.w; value = Radd(value, R(BigInt(it.v), 1n));
        picks.push({ i: it.i, take: R(1n, 1n) });
      } else {
        var frac = R(BigInt(left), BigInt(it.w));
        value = Radd(value, Rmul(frac, R(BigInt(it.v), 1n)));
        picks.push({ i: it.i, take: frac });
        left = 0;
      }
    });
    var whole = knapsackBrute(items, W);
    return runOf({ value: value, picks: picks, order: order,
                   integralValue: whole.result.value, integralPicks: whole.result.members,
                   gap: Rsub(value, R(BigInt(whole.result.value), 1n)) },
                 usedCounts(c), []);
  }

  /* Matroids. A family is given by an INDEPENDENCE ORACLE -- a function on a
     subset -- because that is the definition, and enumerating the family from
     the oracle is what lets the exchange property be tested pair by pair
     instead of assumed. |E| <= 10 is 1024 subsets. */
  function independenceEnumerate(ground, oracle, cap) {
    cap = cap === undefined ? 10 : cap;
    oracleCap('independenceEnumerate', ground.length, cap);
    var family = [], examined = 0;
    forEachSubset(ground.length, function (mask) {
      examined += 1;
      var m = maskMembers(mask, ground.length);
      if (oracle(m)) family.push(m);
    });
    var bases = [], maxSize = 0;
    family.forEach(function (s) { if (s.length > maxSize) maxSize = s.length; });
    family.forEach(function (s) { if (s.length === maxSize) bases.push(s); });
    return runOf({ family: family, bases: bases, rank: maxSize },
                 { nodes: examined }, []);
  }
  /* The exchange property, tested on EVERY ordered pair of the family: if
     |A| < |B| then some element of B - A can join A. The failures are returned,
     because the mode's second arm is a family that is not a matroid and the
     failing pair is the reason. */
  function exchangeTest(family) {
    var failures = [], tested = 0;
    var key = family.map(function (s) { return s.join(','); });
    family.forEach(function (A, ai) {
      family.forEach(function (B, bi) {
        if (A.length >= B.length) return;
        tested += 1;
        var ok = B.some(function (x) {
          if (A.indexOf(x) !== -1) return false;
          return key.indexOf(A.concat([x]).sort(function (p, q) { return p - q; }).join(',')) !== -1;
        });
        if (!ok) failures.push({ A: A, B: B });
      });
    });
    return { tested: tested, failures: failures, isMatroid: failures.length === 0 };
  }
  /* Greedy over the family by weight, and the optimum over the same family.
     They are equal exactly when the family is a matroid, which is the mode. */
  function matroidGreedy(family, weights, ground) {
    var c = counter(), order = ground.map(function (_, i) { return i; })
      .sort(function (a, b) { return weights[b] - weights[a] || a - b; });
    var key = {};
    family.forEach(function (s) { key[s.join(',')] = true; });
    var chosen = [], trace = [];
    order.forEach(function (x) {
      c.compares += 1;
      var next = chosen.concat([x]).sort(function (p, q) { return p - q; });
      var ok = !!key[next.join(',')];
      if (ok) chosen = next;
      trace.push({ at: trace.length, element: x, weight: weights[x], taken: ok });
    });
    var greedyValue = chosen.reduce(function (t, x) { return t + weights[x]; }, 0);
    var best = null, bestSet = null;
    family.forEach(function (s) {
      var v = s.reduce(function (t, x) { return t + weights[x]; }, 0);
      if (best === null || v > best) { best = v; bestSet = s; }
    });
    return runOf({ chosen: chosen, value: greedyValue, optimum: best, optimal: bestSet,
                   matches: greedyValue === best }, usedCounts(c), trace);
  }

  /* Gale-Shapley. prefsA[i] and prefsB[j] are full ranking arrays. The mode's
     content is the proposal sequence and the EMPTY blocking-pair list, plus
     each side's average rank under the two runs -- proposers do better, which
     is the asymmetry readers do not expect. */
  function galeShapley(prefsA, prefsB) {
    var n = prefsA.length, c = counter(), trace = [];
    var next = new Array(n).fill(0), matchB = new Array(n).fill(-1), matchA = new Array(n).fill(-1);
    var rankB = prefsB.map(function (row) {
      var r = new Array(n).fill(0);
      row.forEach(function (a, k) { r[a] = k; });
      return r;
    });
    var free = [];
    for (var i = 0; i < n; i += 1) free.push(i);
    var guard = 0;
    while (free.length && guard < n * n + n) {
      guard += 1;
      var a = free.shift(), b = prefsA[a][next[a]];
      next[a] += 1; c.calls += 1;
      if (matchB[b] === -1) {
        matchB[b] = a; matchA[a] = b;
        trace.push({ at: trace.length, proposer: a, to: b, outcome: 'accepted' });
      } else {
        var rival = matchB[b];
        c.compares += 1;
        if (rankB[b][a] < rankB[b][rival]) {
          matchB[b] = a; matchA[a] = b; matchA[rival] = -1; free.push(rival);
          trace.push({ at: trace.length, proposer: a, to: b, outcome: 'accepted, ' + rival + ' rejected' });
        } else {
          free.push(a);
          trace.push({ at: trace.length, proposer: a, to: b, outcome: 'rejected' });
        }
      }
    }
    var ranks = { proposers: 0, receivers: 0 };
    for (i = 0; i < n; i += 1) {
      ranks.proposers += prefsA[i].indexOf(matchA[i]) + 1;
      ranks.receivers += rankB[i][matchB[i]] + 1;
    }
    return runOf({ matchA: matchA, matchB: matchB, proposals: c.calls,
                   meanProposerRank: R(BigInt(ranks.proposers), BigInt(n)),
                   meanReceiverRank: R(BigInt(ranks.receivers), BigInt(n)) },
                 usedCounts(c), trace);
  }
  /* Every pair that would rather have each other than their partners. On a
     Gale-Shapley matching this list is empty, and printing the empty list is
     the lesson -- an assertion of stability is not one. */
  function blockingPairs(matchA, prefsA, prefsB) {
    var n = prefsA.length, out = [], matchB = new Array(n).fill(-1);
    matchA.forEach(function (b, a) { if (b >= 0) matchB[b] = a; });
    for (var a = 0; a < n; a += 1) {
      for (var b = 0; b < n; b += 1) {
        if (matchA[a] === b) continue;
        var aPrefers = prefsA[a].indexOf(b) < prefsA[a].indexOf(matchA[a]);
        var bPrefers = prefsB[b].indexOf(a) < prefsB[b].indexOf(matchB[b]);
        if (aPrefers && bPrefers) out.push([a, b]);
      }
    }
    return { pairs: out, stable: out.length === 0 };
  }
"""


# -------------------------------------------------- 4.9 dpkit (course 5)

DP_JS = r"""
  /* One table-stepping grammar for twelve modes.

     A dynamic program is a table, a fill ORDER and a recurrence, and the thing
     readers get wrong is never the recurrence -- it is which cells a cell reads
     and whether they are filled yet. So dpFill records, for every cell, the
     cells it READ while it was being computed, and the mode paints them. That
     dependency list is not a description of the recurrence written by hand; it
     is collected by the `get` the recurrence itself calls, so it cannot
     disagree with what the code did.

     spec = {
       rows, cols,          the table's shape
       base(i, j)           a value for cells that have one, else undefined
       cell(i, j, get)      the recurrence; returns a value or { v, from }
       order                'rowmajor' | 'colmajor' | 'bylength'
     }
     'bylength' fills by j - i ascending, which is the interval order matrix
     chain needs and the order a row-major fill gets wrong. */
  function dpOrder(spec) {
    var out = [], i, j;
    if (spec.order === 'colmajor') {
      for (j = 0; j < spec.cols; j += 1) for (i = 0; i < spec.rows; i += 1) out.push([i, j]);
    } else if (spec.order === 'bylength') {
      for (var len = 0; len < spec.cols; len += 1) {
        for (i = 0; i + len < spec.rows; i += 1) out.push([i, i + len]);
      }
    } else {
      for (i = 0; i < spec.rows; i += 1) for (j = 0; j < spec.cols; j += 1) out.push([i, j]);
    }
    return out;
  }
  function dpFill(spec) {
    var c = counter(), table = [], deps = [], from = [], i, j;
    for (i = 0; i < spec.rows; i += 1) {
      table.push(new Array(spec.cols).fill(null));
      deps.push([]); from.push([]);
      for (j = 0; j < spec.cols; j += 1) { deps[i].push([]); from[i].push(null); }
    }
    var order = dpOrder(spec), reads = [];
    order.forEach(function (rc) {
      var r = rc[0], k = rc[1];
      reads = [];
      function get(a, b) {
        c.reads += 1;
        reads.push([a, b]);
        if (a < 0 || b < 0 || a >= spec.rows || b >= spec.cols) return null;
        return table[a][b];
      }
      var base = spec.base ? spec.base(r, k) : undefined;
      var v = base === undefined ? spec.cell(r, k, get) : base;
      if (v !== null && typeof v === 'object' && v.v !== undefined) {
        from[r][k] = v.from === undefined ? null : v.from;
        v = v.v;
      }
      table[r][k] = v;
      deps[r][k] = reads.slice();
      c.cells += 1;
      c.writes += 1;
    });
    return runOf({ table: table, deps: deps, from: from, order: order },
                 usedCounts(c), []);
  }
  /* Walk `from` back from a cell. The tie-break is a parameter because the mode
     shows two different optimal answers reached by two tie-breaks, which is the
     point that an optimum need not be unique. */
  function reconstruct(filled, start, tieBreak) {
    var path = [start], at = start, guard = 0;
    while (guard < filled.table.length * filled.table[0].length + 4) {
      guard += 1;
      var f = filled.from[at[0]][at[1]];
      if (!f) break;
      var next = Array.isArray(f[0]) ? (tieBreak === 'last' ? f[f.length - 1] : f[0]) : f;
      if (!next) break;
      path.push(next);
      at = next;
    }
    return path;
  }

  /* Longest increasing subsequence, both ways, because the mode shows them
     side by side: the n^2 table and the tails array.

     THE BINARY SEARCH IS WRITTEN OUT HERE AND NOT REUSED, and the design said
     it would be. `ALGO_JS.binarySearch(a, target)` returns the NUMBER OF
     COMPARISONS an exact-match search made and nothing else -- no index, and
     no answer at all when the target is absent. The tails array needs the
     insertion POSITION of a value that is not there, which is a different
     function, so it is the six lines below, with its comparisons counted where
     they happen. The same is true of dpkit's p(j).

     The tails array is NOT the subsequence: it has the right LENGTH and
     usually the wrong contents, which is the misconception, so the
     subsequence comes from predecessors. */
  function lisTails(a) {
    var c = counter(), tails = [], idx = [], prev = new Array(a.length).fill(-1), steps = [];
    a.forEach(function (x, i) {
      var lo = 0, hi = tails.length;
      while (lo < hi) {
        var mid = (lo + hi) >> 1;
        c.compares += 1;
        if (tails[mid] < x) lo = mid + 1; else hi = mid;
      }
      if (lo > 0) prev[i] = idx[lo - 1];
      tails[lo] = x; idx[lo] = i;
      steps.push({ at: i, value: x, position: lo, tails: tails.slice() });
    });
    var out = [], at = tails.length ? idx[tails.length - 1] : -1;
    while (at !== -1) { out.push(a[at]); at = prev[at]; }
    out.reverse();
    return runOf({ length: tails.length, tails: tails, subsequence: out },
                 usedCounts(c), steps);
  }

  /* Weighted independent set on a TREE, by one postorder pass: for each node,
     the best with it and the best without it. Checked against brute force over
     every subset, which is this kit's one capped oracle. */
  function treeDp(tree, w) {
    var c = counter(), withV = {}, without = {}, order = [];
    (function post(v, parent) {
      c.calls += 1;
      var a = w[v], b = 0;
      (tree[v] || []).forEach(function (u) {
        if (u === parent) return;
        post(u, v);
        a += without[u];
        b += Math.max(withV[u], without[u]);
        c.reads += 2;
      });
      withV[v] = a; without[v] = b;
      order.push(v);
    })(0, -1);
    var chosen = [];
    (function pick(v, parent, allowed) {
      var take = allowed && withV[v] >= without[v];
      if (take) chosen.push(v);
      (tree[v] || []).forEach(function (u) { if (u !== parent) pick(u, v, !take); });
    })(0, -1, true);
    return runOf({ value: Math.max(withV[0], without[0]), withV: withV, without: without,
                   order: order, chosen: chosen.sort(function (a, b) { return a - b; }) },
                 usedCounts(c), []);
  }
  function misBrute(tree, w, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('misBrute', w.length, cap);
    var edges = [];
    Object.keys(tree).forEach(function (v) {
      (tree[v] || []).forEach(function (u) { if (Number(v) < u) edges.push([Number(v), u]); });
    });
    var best = 0, bestSet = [], examined = 0;
    forEachSubset(w.length, function (mask) {
      examined += 1;
      var ok = edges.every(function (e) { return !((mask >> e[0]) & 1) || !((mask >> e[1]) & 1); });
      if (!ok) return;
      var m = maskMembers(mask, w.length);
      var v = m.reduce(function (t, x) { return t + w[x]; }, 0);
      if (v > best) { best = v; bestSet = m; }
    });
    return runOf({ value: best, members: bestSet }, { nodes: examined }, []);
  }

  /* Counting, where the ORDER OF THE LOOPS is the answer: items outside counts
     combinations, amounts outside counts ordered sequences, and readers write
     the second while meaning the first. Both are computed, and the objects
     themselves are listed for small amounts so the difference is visible and
     not merely numeric. */
  function countWays(coins, amount, order) {
    var c = counter(), i, v;
    var dp = new Array(amount + 1).fill(0n);
    dp[0] = 1n;
    var rows = [];
    if (order === 'permutations') {
      for (v = 1; v <= amount; v += 1) {
        coins.forEach(function (coin) { if (coin <= v) { dp[v] += dp[v - coin]; c.reads += 1; } });
      }
    } else {
      coins.forEach(function (coin) {
        for (v = coin; v <= amount; v += 1) { dp[v] += dp[v - coin]; c.reads += 1; }
        rows.push({ coin: coin, row: dp.slice() });
      });
    }
    return runOf({ count: dp[amount], table: dp, rows: rows, order: order || 'combinations' },
                 usedCounts(c), rows);
  }
  function listCombinations(coins, amount, cap) {
    cap = cap === undefined ? 40 : cap;
    oracleCap('listCombinations', amount, cap);
    var out = [];
    (function pick(i, left, acc) {
      if (left === 0) { out.push(acc.slice()); return; }
      if (i >= coins.length || left < 0) return;
      pick(i + 1, left, acc);
      acc.push(coins[i]);
      pick(i, left - coins[i], acc);
      acc.pop();
    })(0, amount, []);
    return out;
  }
  /* The unbounded knapsack in ONE ROW, and the direction that makes it
     unbounded: forward reuses the item within the same row, backward does not.
     Both are run, which is the mode. */
  function oneRow(items, W, direction) {
    var row = new Array(W + 1).fill(0), c = counter(), snapshots = [];
    items.forEach(function (it) {
      if (direction === 'backward') {
        for (var w = W; w >= it.w; w -= 1) { c.reads += 1; row[w] = Math.max(row[w], row[w - it.w] + it.v); }
      } else {
        for (var w2 = it.w; w2 <= W; w2 += 1) { c.reads += 1; row[w2] = Math.max(row[w2], row[w2 - it.w] + it.v); }
      }
      snapshots.push({ item: it, row: row.slice() });
    });
    return runOf({ value: row[W], row: row, direction: direction || 'forward' },
                 usedCounts(c), snapshots);
  }

  /* Combinatorial game positions: a position is LOSING exactly when every move
     leads to a winning one. `moves` is a function from a position to its
     options, and the labels are computed over the reachable set, so the period
     a reader is asked to spot is a fact about the table rather than a claim. */
  function gameLabels(moves, positions) {
    var label = {}, c = counter();
    positions.forEach(function (p) {
      var opts = moves(p);
      c.calls += 1;
      label[p] = opts.some(function (q) { return label[q] === 'L'; }) ? 'W' : 'L';
      if (!opts.length) label[p] = 'L';
    });
    var losing = positions.filter(function (p) { return label[p] === 'L'; });
    var period = null;
    for (var k = 1; k <= positions.length && period === null; k += 1) {
      var ok = positions.every(function (p, i) {
        return i + k >= positions.length || label[positions[i]] === label[positions[i + k]];
      });
      if (ok && losing.length) period = k;
    }
    return runOf({ label: label, losing: losing, period: period }, usedCounts(c), []);
  }

  /* Held-Karp: the exact TSP by subsets, and the reason the mode exists is the
     comparison it prints -- n^2 2^n against (n-1)!, both as BigInts, with the
     brute-force tour count beside them. */
  function heldKarp(D) {
    var n = D.length, c = counter(), full = 1 << (n - 1);
    var dp = [], parent = [], mask, j;
    for (mask = 0; mask < full; mask += 1) {
      dp.push(new Array(n - 1).fill(null));
      parent.push(new Array(n - 1).fill(-1));
    }
    for (j = 0; j < n - 1; j += 1) dp[1 << j][j] = D[0][j + 1];
    var bySize = [];
    for (mask = 1; mask < full; mask += 1) {
      for (j = 0; j < n - 1; j += 1) {
        if (!(mask & (1 << j)) || dp[mask][j] === null) continue;
        for (var k = 0; k < n - 1; k += 1) {
          if (mask & (1 << k)) continue;
          var next = mask | (1 << k), cand = dp[mask][j] + D[j + 1][k + 1];
          c.reads += 1;
          if (dp[next][k] === null || cand < dp[next][k]) { dp[next][k] = cand; parent[next][k] = j; }
        }
      }
      bySize.push({ mask: mask, size: popcount(mask), row: dp[mask].slice() });
    }
    var best = null, last = -1;
    for (j = 0; j < n - 1; j += 1) {
      if (dp[full - 1][j] === null) continue;
      var total = dp[full - 1][j] + D[j + 1][0];
      if (best === null || total < best) { best = total; last = j; }
    }
    var tour = [], mask2 = full - 1, at = last;
    while (at !== -1) { tour.push(at + 1); var p = parent[mask2][at]; mask2 ^= (1 << at); at = p; }
    tour.push(0); tour.reverse();
    var N = BigInt(n);
    return runOf({ length: best, tour: tour, table: bySize,
                   heldKarpWork: N * N * (2n ** N), bruteWork: fact(n - 1) },
                 usedCounts(c), bySize);
  }
"""


# ------------------------------------------------ 4.10 strings (course 6)

STRINGS_JS = r"""
  /* String matching. Every count is a character comparison actually made, and
     the hashes are BigInt so a rolling hash is the same number on every
     machine -- a lesson whose subject is that two windows collide cannot have
     the collision depend on the reader's browser. */

  function naiveRun(t, p) {
    var c = counter(), trace = [], hits = [];
    for (var i = 0; i + p.length <= t.length; i += 1) {
      var k = 0;
      while (k < p.length) { c.compares += 1; if (t[i + k] !== p[k]) break; k += 1; }
      if (k === p.length) hits.push(i);
      trace.push({ at: i, compares: k === p.length ? k : k + 1, matched: k, hit: k === p.length });
    }
    return runOf({ hits: hits, alignments: trace.length }, usedCounts(c), trace);
  }
  /* The expected characters compared per alignment over a uniform alphabet of
     size sigma: sum_{k>=1} k * (1/sigma)^(k-1) * ((sigma-1)/sigma) = sigma /
     (sigma - 1), exactly. Which is why naive matching is fast on ordinary text
     and quadratic only on the contrived pair the mode builds in one click. */
  function expectedPerAlignment(sigma) {
    return R(BigInt(sigma), BigInt(sigma - 1));
  }
  function naiveWorstPair(m, n, letter) {
    var a = letter || 'a';
    return { text: new Array(n + 1).join(a), pattern: new Array(m).join(a) + 'b' };
  }

  /* Rabin-Karp, with every window's hash exact. A HIT IS NOT A MATCH: the
     lesson's whole content is that an equal hash must be verified, so spurious
     hits are counted separately from real ones. */
  function rollingHash(t, p, b, mod) {
    var B = BigInt(b), M = BigInt(mod), c = counter(), trace = [];
    function hash(s) {
      var h = 0n;
      for (var i = 0; i < s.length; i += 1) h = (h * B + BigInt(s.charCodeAt(i))) % M;
      return h;
    }
    var m = p.length, target = hash(p), high = 1n;
    for (var i = 1; i < m; i += 1) high = (high * B) % M;
    var h = m <= t.length ? hash(t.slice(0, m)) : null;
    var hits = [], spurious = 0, verified = 0;
    for (var s = 0; s + m <= t.length; s += 1) {
      if (s > 0) {
        h = (h - BigInt(t.charCodeAt(s - 1)) * high % M + M) % M;
        h = (h * B + BigInt(t.charCodeAt(s + m - 1))) % M;
      }
      var equal = h === target, real = false;
      if (equal) {
        verified += 1;
        real = t.slice(s, s + m) === p;
        c.compares += m;
        if (real) hits.push(s); else spurious += 1;
      }
      trace.push({ at: s, hash: h, equal: equal, match: real });
    }
    return runOf({ hits: hits, target: target, spurious: spurious, verifications: verified,
                   base: b, modulus: mod }, usedCounts(c), trace);
  }

  /* KMP's failure function: fail[k] is the length of the longest proper border
     of the first k characters. The inner loop's total iterations are bounded by
     2m, and the panel plots them against it, because "amortised" is the claim
     and a count is the only honest evidence for it. */
  function failureFn(p) {
    var c = counter(), fail = new Array(p.length + 1).fill(0), k = 0, inner = 0;
    fail[0] = -1;
    for (var i = 1; i < p.length; i += 1) {
      while (k > 0 && p[i] !== p[k]) { k = fail[k] > 0 ? fail[k] : 0; inner += 1; c.compares += 1; if (k === 0) break; }
      c.compares += 1;
      if (p[i] === p[k]) k += 1; else k = 0;
      fail[i + 1] = k;
    }
    var chain = [];
    var at = p.length;
    while (at > 0) { chain.push(at); at = fail[at] > 0 ? fail[at] : 0; }
    return runOf({ fail: fail, borders: chain, inner: inner, bound: 2 * p.length },
                 usedCounts(c), []);
  }
  function kmpRun(t, p) {
    var f = failureFn(p).result.fail, c = counter(), trace = [], hits = [], k = 0;
    for (var i = 0; i < t.length; i += 1) {
      while (k > 0 && t[i] !== p[k]) { k = Math.max(0, f[k]); c.compares += 1; }
      c.compares += 1;
      if (t[i] === p[k]) k += 1;
      trace.push({ at: i, matched: k, text: i });
      if (k === p.length) { hits.push(i - p.length + 1); k = Math.max(0, f[k]); }
    }
    var naive = naiveRun(t, p);
    return runOf({ hits: hits, naiveCompares: naive.counts.compares || 0,
                   textPointerMonotone: true, bound: 2 * t.length },
                 usedCounts(c), trace);
  }

  /* Horspool: the shift table is the LAST occurrence of each character in the
     pattern's first m-1 positions, so a mismatch jumps rather than sliding by
     one. Characters skipped is the figure. */
  function horspoolRun(t, p) {
    var c = counter(), shift = {}, m = p.length, i;
    for (i = 0; i < m - 1; i += 1) shift[p[i]] = m - 1 - i;
    var hits = [], trace = [], s = 0, skipped = 0;
    while (s + m <= t.length) {
      var k = m - 1;
      while (k >= 0) { c.compares += 1; if (t[s + k] !== p[k]) break; k -= 1; }
      if (k < 0) hits.push(s);
      var step = shift[t[s + m - 1]] === undefined ? m : shift[t[s + m - 1]];
      trace.push({ at: s, matchedFromRight: m - 1 - k, shift: step });
      skipped += step - 1;
      s += step;
    }
    var kmp = kmpRun(t, p);
    return runOf({ hits: hits, table: shift, skipped: skipped,
                   kmpCompares: kmp.counts.compares || 0 }, usedCounts(c), trace);
  }

  /* A trie. `slots` counts the array cells an array-per-node implementation
     would allocate, beside the `nodes` a map-per-node one uses -- the space
     question the lesson asks, answered with two numbers rather than a word. */
  function trieBuild(words, sigma) {
    var root = { ch: '', kids: {}, end: false, id: 0 }, nodes = [root], c = counter();
    words.forEach(function (w) {
      var at = root;
      for (var i = 0; i < w.length; i += 1) {
        if (!at.kids[w[i]]) {
          var made = { ch: w[i], kids: {}, end: false, id: nodes.length };
          nodes.push(made); at.kids[w[i]] = made; c.writes += 1;
        }
        at = at.kids[w[i]];
        c.reads += 1;
      }
      at.end = true;
    });
    return { root: root, nodes: nodes, count: nodes.length,
             slots: nodes.length * (sigma || 26),
             counts: usedCounts(c) };
  }
  function trieKids(n) {
    return Object.keys(n.kids).sort().map(function (k) { return n.kids[k]; });
  }
  function triePrefix(trie, prefix) {
    var at = trie.root;
    for (var i = 0; i < prefix.length; i += 1) {
      at = at.kids[prefix[i]];
      if (!at) return [];
    }
    var out = [];
    (function walk(n, acc) {
      if (n.end) out.push(acc);
      trieKids(n).forEach(function (k) { walk(k, acc + k.ch); });
    })(at, prefix);
    return out;
  }
  /* Aho-Corasick failure links by BFS, then ONE pass over the text reporting
     every match of every pattern -- against k separate KMP runs, which is the
     comparison the mode draws. */
  function ahoLinks(trie) {
    var root = trie.root, queue = [];
    root.fail = root; root.out = [];
    trieKids(root).forEach(function (k) { k.fail = root; queue.push(k); });
    while (queue.length) {
      var v = queue.shift();
      v.out = (v.end ? [v] : []).concat(v.fail.out || []);
      trieKids(v).forEach(function (k) {
        var f = v.fail;
        while (f !== root && !f.kids[k.ch]) f = f.fail;
        k.fail = (f.kids[k.ch] && f.kids[k.ch] !== k) ? f.kids[k.ch] : root;
        queue.push(k);
      });
    }
    return trie;
  }
  function ahoRun(t, trie) {
    var root = trie.root, at = root, c = counter(), hits = [], trace = [];
    for (var i = 0; i < t.length; i += 1) {
      while (at !== root && !at.kids[t[i]]) { at = at.fail; c.compares += 1; }
      c.compares += 1;
      if (at.kids[t[i]]) at = at.kids[t[i]];
      (at.out || []).forEach(function (n) { hits.push({ at: i, node: n.id }); });
      trace.push({ at: i, state: at.id, outputs: (at.out || []).length });
    }
    return runOf({ hits: hits, states: trie.count }, usedCounts(c), trace);
  }

  /* The suffix array by PREFIX DOUBLING: sort by the first character, then use
     the previous ranks to sort by 2, 4, 8 characters at a time, so each round
     is a sort on pairs of ranks rather than on strings. The rounds are the
     mode. */
  function suffixArray(s) {
    var n = s.length, c = counter(), rank = [], sa = [], i, rounds = [];
    for (i = 0; i < n; i += 1) { sa.push(i); rank.push(s.charCodeAt(i)); }
    var k = 1, tmp = new Array(n).fill(0);
    while (true) {
      var cmp = function (a, b) {
        if (rank[a] !== rank[b]) return rank[a] - rank[b];
        var ra = a + k < n ? rank[a + k] : -1, rb = b + k < n ? rank[b + k] : -1;
        return ra - rb;
      };
      sa.sort(function (a, b) { c.compares += 1; return cmp(a, b); });
      tmp[sa[0]] = 0;
      for (i = 1; i < n; i += 1) tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) < 0 ? 1 : 0);
      for (i = 0; i < n; i += 1) rank[i] = tmp[i];
      rounds.push({ k: k, order: sa.slice(), rank: rank.slice() });
      if (rank[sa[n - 1]] === n - 1) break;
      k *= 2;
      if (k > 2 * n) break;
    }
    return runOf({ sa: sa, rounds: rounds, suffixes: sa.map(function (i) { return s.slice(i); }) },
                 usedCounts(c), rounds);
  }
  /* Kasai: the LCP array in one pass, because the suffix one place earlier in
     the TEXT has an lcp at least one less -- which is the trick, and the
     counter shows the total work is linear. */
  function kasai(s, sa) {
    var n = s.length, rank = new Array(n).fill(0), lcp = new Array(n).fill(0), c = counter();
    sa.forEach(function (p, i) { rank[p] = i; });
    var h = 0;
    for (var i = 0; i < n; i += 1) {
      if (rank[i] > 0) {
        var j = sa[rank[i] - 1];
        while (i + h < n && j + h < n && s[i + h] === s[j + h]) { h += 1; c.compares += 1; }
        lcp[rank[i]] = h;
        if (h > 0) h -= 1;
      } else h = 0;
    }
    var longest = 0, at = -1;
    lcp.forEach(function (v, i) { if (v > longest) { longest = v; at = sa[i]; } });
    var distinct = 0n, N = BigInt(n);
    for (var k = 0; k < n; k += 1) distinct += N - BigInt(sa[k]) - BigInt(lcp[k]);
    return runOf({ lcp: lcp, longestRepeat: longest, repeatAt: at,
                   distinctSubstrings: distinct }, usedCounts(c), []);
  }

  /* The KMP automaton written out in full: m * sigma transitions, and then the
     run takes EXACTLY n steps with no back-up at all. The trade is the table's
     size, which is why both numbers are printed. */
  function dfaTable(p, alphabet) {
    var m = p.length, table = [], c = counter();
    for (var i = 0; i <= m; i += 1) {
      var row = {};
      alphabet.forEach(function (ch) {
        var k = Math.min(m, i + 1);
        while (k > 0 && (p.slice(0, i) + ch).slice(-k) !== p.slice(0, k)) k -= 1;
        row[ch] = k;
        c.writes += 1;
      });
      table.push(row);
    }
    return { table: table, states: m + 1, cells: (m + 1) * alphabet.length, counts: usedCounts(c) };
  }
  function dfaRun(t, table, m) {
    var state = 0, hits = [], c = counter(), trace = [];
    for (var i = 0; i < t.length; i += 1) {
      state = table[state][t[i]] === undefined ? 0 : table[state][t[i]];
      c.reads += 1;
      trace.push({ at: i, state: state });
      if (state === m) hits.push(i - m + 1);
    }
    return runOf({ hits: hits, steps: t.length }, usedCounts(c), trace);
  }
"""


# ----------------------------------------------- 4.11 geometry (course 7)

GEOM_JS = r"""
  /* Computational geometry in EXACT INTEGERS. No distance on this course is
     square-rooted: a comparison of distances is a comparison of squared
     distances, and the answer to every question the course asks -- which side,
     do they cross, which is closer, what is the area -- is a determinant, a
     sign, or a doubled area, all of them integers.

     BigInt, and not Number, for the determinants. orient2 on coordinates near
     10^8 produces cross products near 10^16, which is past 2^53, and a double
     there returns a WRONG SIGN. Measured, not asserted: at a = (0, 0),
     b = (134217729, 134217728), c = (134217728, 134217727) the exact
     determinant is -1 -- a right turn -- and the double gives 0, which reads as
     three collinear points. A hull built on that answer has a vertex missing
     and a point-in-polygon test on it flips. The mode prints the float beside
     the exact value for exactly that reason, and it is the one deliberate
     float in this block. */
  function orient2(a, b, c) {
    var d = (BigInt(b[0]) - BigInt(a[0])) * (BigInt(c[1]) - BigInt(a[1]))
          - (BigInt(b[1]) - BigInt(a[1])) * (BigInt(c[0]) - BigInt(a[0]));
    return d;
  }
  function orientSign(a, b, c) {
    var d = orient2(a, b, c);
    return d > 0n ? 1 : (d < 0n ? -1 : 0);
  }
  /* The same determinant in double arithmetic, for the column the lesson puts
     beside the exact one. It is here to be WRONG in front of the reader. */
  function orient2Float(a, b, c) {
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  }
  function boxOverlap(p1, p2, q1, q2) {
    return Math.min(p1[0], p2[0]) <= Math.max(q1[0], q2[0])
        && Math.min(q1[0], q2[0]) <= Math.max(p1[0], p2[0])
        && Math.min(p1[1], p2[1]) <= Math.max(q1[1], q2[1])
        && Math.min(q1[1], q2[1]) <= Math.max(p1[1], p2[1]);
  }
  function onSegment(a, b, q) {
    return orientSign(a, b, q) === 0
      && Math.min(a[0], b[0]) <= q[0] && q[0] <= Math.max(a[0], b[0])
      && Math.min(a[1], b[1]) <= q[1] && q[1] <= Math.max(a[1], b[1]);
  }
  /* Four orientations and the verdict, collinear cases included -- which is
     where a segment-intersection test is usually wrong. */
  function straddle(p1, p2, q1, q2) {
    var d1 = orientSign(q1, q2, p1), d2 = orientSign(q1, q2, p2);
    var d3 = orientSign(p1, p2, q1), d4 = orientSign(p1, p2, q2);
    var proper = ((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0))
              && ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0));
    var touching = onSegment(q1, q2, p1) || onSegment(q1, q2, p2)
                || onSegment(p1, p2, q1) || onSegment(p1, p2, q2);
    return { d: [d1, d2, d3, d4], proper: proper, touching: touching,
             intersect: proper || touching, boxes: boxOverlap(p1, p2, q1, q2) };
  }

  function lexSort(points) {
    return points.slice().sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
  }
  /* Jarvis's march: wrap the hull one vertex at a time, so the work is n per
     hull vertex -- n*h, which beats n log n exactly when h is small, and the
     mode plots both. */
  function jarvis(points) {
    var c = counter(), pts = lexSort(points), hull = [], start = 0, i;
    if (pts.length < 3) return runOf({ hull: pts, h: pts.length }, usedCounts(c), []);
    var at = 0, trace = [];
    do {
      hull.push(pts[at]);
      var next = (at + 1) % pts.length;
      for (i = 0; i < pts.length; i += 1) {
        c.compares += 1;
        var o = orientSign(pts[at], pts[i], pts[next]);
        if (o > 0) next = i;
      }
      trace.push({ at: trace.length, from: pts[at], to: pts[next] });
      at = next;
    } while (at !== 0 && hull.length <= pts.length);
    return runOf({ hull: hull, h: hull.length, work: pts.length * hull.length,
                   nlogn: pts.length * ilog2(Math.max(2, pts.length)) },
                 usedCounts(c), trace);
  }
  /* Andrew's monotone chain. The stack is the mode: pushes and pops against
     2n, which is the amortised argument -- a point is pushed once and popped
     at most once. */
  function monotoneChain(points) {
    var c = counter(), pts = lexSort(points), trace = [], i;
    function half(list) {
      var stack = [];
      list.forEach(function (p) {
        while (stack.length >= 2) {
          c.compares += 1;
          if (orientSign(stack[stack.length - 2], stack[stack.length - 1], p) > 0) break;
          stack.pop(); c.pops += 1;
          trace.push({ at: trace.length, action: 'pop', stack: stack.slice() });
        }
        stack.push(p); c.pushes += 1;
        trace.push({ at: trace.length, action: 'push', point: p, stack: stack.slice() });
      });
      return stack;
    }
    var lower = half(pts), upper = half(pts.slice().reverse());
    var hull = lower.slice(0, -1).concat(upper.slice(0, -1));
    return runOf({ hull: hull, h: hull.length, lower: lower, upper: upper,
                   bound: 2 * pts.length }, usedCounts(c), trace);
  }
  /* Lift x to (x, x^2): the hull of the lifted points reads back the sorted
     order, which is the reduction that puts an n log n LOWER bound under every
     convex hull algorithm. */
  function liftParabola(xs) {
    return xs.map(function (x) { return [x, x * x]; });
  }

  function dist2(a, b) {
    var dx = BigInt(a[0]) - BigInt(b[0]), dy = BigInt(a[1]) - BigInt(b[1]);
    return dx * dx + dy * dy;
  }
  /* Closest pair by divide and conquer, with the STRIP comparisons counted --
     the claim being that each point is compared with at most seven others, and
     the panel plots the measured total against 7n. Squared distances, so
     nothing is rounded. */
  function closestPair(points) {
    var c = counter(), pts = lexSort(points), levels = [], stripTotal = 0;
    function rec(list, depth) {
      c.calls += 1;
      if (list.length <= 3) {
        var best = null, pair = null;
        for (var i = 0; i < list.length; i += 1) for (var j = i + 1; j < list.length; j += 1) {
          c.compares += 1;
          var d = dist2(list[i], list[j]);
          if (best === null || d < best) { best = d; pair = [list[i], list[j]]; }
        }
        return { d: best, pair: pair };
      }
      var mid = list.length >> 1, midX = list[mid][0];
      var L = rec(list.slice(0, mid), depth + 1), Rr = rec(list.slice(mid), depth + 1);
      var best2 = L.d === null ? Rr.d : (Rr.d === null ? L.d : (L.d < Rr.d ? L.d : Rr.d));
      var pair2 = (L.d !== null && (Rr.d === null || L.d <= Rr.d)) ? L.pair : Rr.pair;
      var strip = list.filter(function (p) {
        var dx = BigInt(p[0]) - BigInt(midX);
        return best2 === null || dx * dx < best2;
      }).sort(function (a, b) { return a[1] - b[1]; });
      var here = 0;
      for (var k = 0; k < strip.length; k += 1) {
        for (var t = k + 1; t < strip.length && t <= k + 7; t += 1) {
          var dy = BigInt(strip[t][1]) - BigInt(strip[k][1]);
          if (best2 !== null && dy * dy >= best2) break;
          c.compares += 1; here += 1;
          var dd = dist2(strip[k], strip[t]);
          if (best2 === null || dd < best2) { best2 = dd; pair2 = [strip[k], strip[t]]; }
        }
      }
      stripTotal += here;
      levels.push({ depth: depth, n: list.length, strip: strip.length, compares: here });
      return { d: best2, pair: pair2 };
    }
    var out = rec(pts, 0);
    return runOf({ d2: out.d, pair: out.pair, levels: levels, stripCompares: stripTotal,
                   bound: 7 * pts.length }, usedCounts(c), levels);
  }

  /* The sweep: events sorted by x, with the status structure holding the
     segments currently crossed by the sweep line. The status structure IS
     TREE_JS's bstRun in the lesson, which is the point -- a data structure met
     in course 1 turns up as the engine of a geometry algorithm. */
  function sweepEvents(segments) {
    var events = [];
    segments.forEach(function (s, i) {
      var a = s[0], b = s[1];
      if (a[0] > b[0]) { var t = a; a = b; b = t; }
      events.push({ x: a[0], y: a[1], kind: 'start', seg: i });
      events.push({ x: b[0], y: b[1], kind: 'end', seg: i });
    });
    events.sort(function (p, q) { return p.x - q.x || (p.kind === 'start' ? -1 : 1) || p.y - q.y; });
    var active = [], c = counter(), crossings = [], trace = [];
    events.forEach(function (e) {
      if (e.kind === 'start') {
        active.forEach(function (j) {
          c.compares += 1;
          var r = straddle(segments[e.seg][0], segments[e.seg][1], segments[j][0], segments[j][1]);
          if (r.intersect) crossings.push([e.seg, j]);
        });
        active.push(e.seg);
      } else {
        active = active.filter(function (j) { return j !== e.seg; });
      }
      trace.push({ at: trace.length, x: e.x, kind: e.kind, seg: e.seg, active: active.slice() });
    });
    var allPairs = segments.length * (segments.length - 1) / 2;
    return runOf({ events: events, crossings: crossings, tests: c.compares || 0,
                   allPairs: allPairs }, usedCounts(c), trace);
  }

  /* The doubled signed area, exactly -- doubled so it stays an integer, which
     is why the lesson works with 2A and halves only at the end. The sign is the
     orientation, which is information a magnitude would throw away. */
  function shoelace2(poly) {
    var s = 0n;
    for (var i = 0; i < poly.length; i += 1) {
      var a = poly[i], b = poly[(i + 1) % poly.length];
      s += BigInt(a[0]) * BigInt(b[1]) - BigInt(b[0]) * BigInt(a[1]);
    }
    return s;
  }
  /* Point in polygon by ray crossing, INCLUDING the vertex case -- a ray
     through a vertex is the bug every implementation has, and the fix is the
     half-open rule below: count an edge only when one endpoint is strictly
     above the ray and the other is not. */
  function rayParity(poly, q) {
    var crossings = 0, onEdge = false, detail = [];
    for (var i = 0; i < poly.length; i += 1) {
      var a = poly[i], b = poly[(i + 1) % poly.length];
      if (onSegment(a, b, q)) onEdge = true;
      var above = (a[1] > q[1]) !== (b[1] > q[1]);
      if (above) {
        var side = orientSign(a, b, q) * (b[1] > a[1] ? 1 : -1);
        if (side > 0) crossings += 1;
        detail.push({ edge: i, counted: side > 0 });
      }
    }
    return { crossings: crossings, inside: !onEdge && crossings % 2 === 1,
             onBoundary: onEdge, detail: detail };
  }

  /* A 2-d tree, split on x then y by depth, and a range query that reports how
     many NODES it visited -- which is the figure, because the whole claim of a
     k-d tree is that the visit count is far under n. */
  function kdBuild(points, depth) {
    if (!points.length) return null;
    depth = depth || 0;
    var axis = depth % 2;
    var sorted = points.slice().sort(function (a, b) { return a[axis] - b[axis] || a[1 - axis] - b[1 - axis]; });
    var mid = sorted.length >> 1;
    return { point: sorted[mid], axis: axis, depth: depth,
             l: kdBuild(sorted.slice(0, mid), depth + 1),
             r: kdBuild(sorted.slice(mid + 1), depth + 1) };
  }
  function kdKids(n) { return [n.l, n.r]; }
  function kdRange(tree, rect) {
    var c = counter(), found = [];
    (function visit(n) {
      if (!n) return;
      c.nodes += 1;
      var p = n.point;
      if (p[0] >= rect[0] && p[0] <= rect[2] && p[1] >= rect[1] && p[1] <= rect[3]) found.push(p);
      var lo = n.axis === 0 ? rect[0] : rect[1], hi = n.axis === 0 ? rect[2] : rect[3];
      if (lo <= p[n.axis]) visit(n.l);
      if (hi >= p[n.axis]) visit(n.r);
    })(tree);
    return runOf({ found: found, visited: c.nodes }, usedCounts(c), []);
  }

  /* Rotating calipers: the diameter of a convex polygon is between an
     ANTIPODAL pair, so the squared diameter comes from h pairs rather than
     n^2 -- and it is exact, because it is never square-rooted. */
  function calipers(hull) {
    var c = counter(), n = hull.length, best = 0n, pair = null, pairs = [];
    if (n < 2) return runOf({ d2: 0n, pair: null, pairs: [] }, usedCounts(c), []);
    var j = 1;
    for (var i = 0; i < n; i += 1) {
      var ni = (i + 1) % n;
      while (true) {
        var area1 = orient2(hull[i], hull[ni], hull[(j + 1) % n]);
        var area0 = orient2(hull[i], hull[ni], hull[j]);
        c.compares += 1;
        if (area1 > area0) j = (j + 1) % n; else break;
      }
      pairs.push([i, j]);
      var d = dist2(hull[i], hull[j]);
      if (d > best) { best = d; pair = [hull[i], hull[j]]; }
      var d2b = dist2(hull[ni], hull[j]);
      if (d2b > best) { best = d2b; pair = [hull[ni], hull[j]]; }
    }
    return runOf({ d2: best, pair: pair, pairs: pairs }, usedCounts(c), []);
  }
  /* The brute-force diameter, for the mode to agree with. n^2/2 pairs. */
  function diameterBrute(points) {
    var best = 0n, pair = null;
    for (var i = 0; i < points.length; i += 1) for (var j = i + 1; j < points.length; j += 1) {
      var d = dist2(points[i], points[j]);
      if (d > best) { best = d; pair = [points[i], points[j]]; }
    }
    return { d2: best, pair: pair };
  }
"""


# ------------------------------------------------- 4.12 random (course 8)

RANDOM_JS = r"""
  /* Randomised algorithms, with every probability an exact fraction.

     Two things in this block are the reason it exists. kargerExact is a
     memoised recursion over CONTRACTION STATES and not a sample, for the reason
     given at the function. And strongTest follows ALGO_JS.powerTrace's shape --
     repeated squaring with the invariant checked exactly after every step --
     with a modulus added, which powerTrace does not have. */

  /* A pmf is [value, rational] pairs, as in sysdesign_core.PMF_JS. */
  function pmfExpect(pairs) {
    var m = R(0n, 1n);
    pairs.forEach(function (p) { m = Radd(m, Rmul(R(BigInt(p[0]), 1n), p[1])); });
    return m;
  }
  function pmfVariance(pairs) {
    var mu = pmfExpect(pairs), v = R(0n, 1n);
    pairs.forEach(function (p) {
      var d = Rsub(R(BigInt(p[0]), 1n), mu);
      v = Radd(v, Rmul(Rmul(d, d), p[1]));
    });
    return v;
  }
  /* Markov: P(X >= a) <= E[X]/a, for a non-negative X. Exact, and the mode's
     content is how far above the true tail it sits. */
  function markovBound(pairs, a) {
    return { bound: Rdiv(pmfExpect(pairs), R(BigInt(a), 1n)), mean: pmfExpect(pairs) };
  }
  /* Chebyshev: P(|X - mu| >= t) <= Var/t^2. */
  function chebyshevBound(pairs, t) {
    var v = pmfVariance(pairs);
    return { bound: Rdiv(v, R(BigInt(t) * BigInt(t), 1n)), variance: v, mean: pmfExpect(pairs) };
  }
  function exactTail(pairs, t) {
    var s = R(0n, 1n);
    pairs.forEach(function (p) { if (p[0] >= t) s = Radd(s, p[1]); });
    return s;
  }
  function exactDeviation(pairs, t) {
    var mu = pmfExpect(pairs), s = R(0n, 1n);
    pairs.forEach(function (p) {
      var d = Rsub(R(BigInt(p[0]), 1n), mu);
      if (Rcmp(Rabs(d), R(BigInt(t), 1n)) >= 0) s = Radd(s, p[1]);
    });
    return s;
  }

  /* EVERY tape, for both shuffles, at n <= 4. Fisher-Yates draws j in [0..i]
     going down, so it has n! tapes and produces each permutation exactly once;
     the naive version draws j in [0..n-1] every time, so it has n^n tapes --
     and n^n is not divisible by n! for n >= 3, which is the proof that it
     CANNOT be uniform, printed as two frequencies that differ. */
  function allTapes(n, kind) {
    var sizes = [];
    if (kind === 'naive') { for (var i = 0; i < n; i += 1) sizes.push(n); }
    else { for (var k = n - 1; k >= 1; k -= 1) sizes.push(k + 1); }
    var out = [[]];
    sizes.forEach(function (s) {
      var next = [];
      out.forEach(function (prefix) {
        for (var v = 0; v < s; v += 1) next.push(prefix.concat([v]));
      });
      out = next;
    });
    return out;
  }
  function fisherYates(n, tape) {
    var a = [], i;
    for (i = 0; i < n; i += 1) a.push(i);
    var at = 0;
    for (i = n - 1; i >= 1; i -= 1) {
      var j = tape[at++] % (i + 1), t = a[i];
      a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function naiveShuffle(n, tape) {
    var a = [], i;
    for (i = 0; i < n; i += 1) a.push(i);
    for (i = 0; i < n; i += 1) {
      var j = tape[i] % n, t = a[i];
      a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function shuffleFrequencies(n, kind) {
    var tapes = allTapes(n, kind), freq = {};
    tapes.forEach(function (tape) {
      var perm = (kind === 'naive' ? naiveShuffle : fisherYates)(n, tape).join('');
      freq[perm] = (freq[perm] || 0) + 1;
    });
    var keys = Object.keys(freq).sort();
    var total = tapes.length;
    var rows = keys.map(function (k) {
      return { perm: k, count: freq[k], probability: R(BigInt(freq[k]), BigInt(total)) };
    });
    var uniform = keys.every(function (k) { return freq[k] === freq[keys[0]]; });
    return { rows: rows, tapes: total, distinct: keys.length, uniform: uniform };
  }
  /* Reservoir sampling: after the whole stream, every item is in the reservoir
     with probability exactly k/n, which is the claim. The draws are integers;
     item i (0-based, i >= k) is kept if draw % (i + 1) < k. */
  function reservoir(n, k, draws) {
    var res = [], i;
    for (i = 0; i < Math.min(k, n); i += 1) res.push(i);
    for (i = k; i < n; i += 1) {
      var j = draws[i - k] % (i + 1);
      if (j < k) res[j] = i;
    }
    return { sample: res, retention: R(BigInt(k), BigInt(n)) };
  }

  /* KARGER'S CONTRACTION, EXACTLY.

     The success probability CANNOT be obtained by enumerating edge orders: that
     is |E|! and it is wrong as well as slow, because different orders reach the
     same contracted graph and the algorithm's future depends only on the graph.
     So this is a memoised recursion over CONTRACTION STATES -- a state being
     the current partition of the vertices into supernodes -- and the value at a
     state is the probability of reaching two supernodes without ever having
     contracted an edge that crosses the target cut.

     P(state) = sum over non-crossing group pairs (A, B) of
                (multiplicity(A, B) / m) * P(state with A and B merged)

     with P = 1 when two groups remain: if no crossing edge was ever contracted
     then every group lies wholly on one side of the cut, so two groups must be
     exactly the two sides. Parallel edges between the same pair of groups all
     lead to the SAME state, which is why they are grouped by multiplicity
     rather than iterated -- the multiplicity is the whole reason the algorithm
     favours a small cut.

     A sampled approximation would pass labcheck and fail the lesson. This is
     exact, it is a rational, and it is compared against the 2/(n(n-1)) bound. */
  function kargerStateKey(group) {
    var seen = {}, next = 0, out = [];
    for (var v = 0; v < group.length; v += 1) {
      if (seen[group[v]] === undefined) { seen[group[v]] = next; next += 1; }
      out.push(seen[group[v]]);
    }
    return out.join(',');
  }
  function kargerExact(G, side, cap) {
    cap = cap === undefined ? 8 : cap;
    oracleCap('kargerExact', G.n, cap);
    var memo = {};
    function solve(group) {
      var groups = {}, list = [];
      group.forEach(function (g, v) {
        if (!groups[g]) { groups[g] = []; list.push(g); }
        groups[g].push(v);
      });
      if (list.length === 2) return R(1n, 1n);
      var key = kargerStateKey(group);
      if (memo[key] !== undefined) return memo[key];
      var mult = {}, m = 0;
      G.arcs.forEach(function (a) {
        if (group[a.u] === group[a.v]) return;         /* a self-loop, which Karger drops */
        var lo = Math.min(group[a.u], group[a.v]), hi = Math.max(group[a.u], group[a.v]);
        mult[lo + '-' + hi] = (mult[lo + '-' + hi] || 0) + 1;
        m += 1;
      });
      if (!m) { memo[key] = R(0n, 1n); return memo[key]; }
      var total = R(0n, 1n);
      Object.keys(mult).forEach(function (pair) {
        var parts = pair.split('-').map(Number), A = parts[0], B = parts[1];
        /* A group lies wholly on one side, so the pair crosses the cut exactly
           when its two groups sit on different sides. */
        if (side[groups[A][0]] !== side[groups[B][0]]) return;
        var next = group.map(function (g) { return g === B ? A : g; });
        total = Radd(total, Rmul(R(BigInt(mult[pair]), BigInt(m)), solve(next)));
      });
      memo[key] = total;
      return total;
    }
    var start = [];
    for (var v = 0; v < G.n; v += 1) start.push(v);
    var p = solve(start);
    var N = BigInt(G.n);
    return { probability: p, bound: R(2n, N * (N - 1n)),
             beatsBound: Rcmp(p, R(2n, N * (N - 1n))) >= 0,
             states: Object.keys(memo).length };
  }
  /* One seeded contraction, for the animation beside the exact number. */
  function kargerRun(G, seed) {
    var group = [], v, trace = [], draws = algoStream(seed, 4 * G.n + 8), at = 0;
    for (v = 0; v < G.n; v += 1) group.push(v);
    function liveArcs() {
      return G.arcs.map(function (a, id) { return id; })
                   .filter(function (id) { return group[G.arcs[id].u] !== group[G.arcs[id].v]; });
    }
    var live = liveArcs(), groups = G.n;
    while (groups > 2 && live.length) {
      var id = live[draws[at++ % draws.length] % live.length], a = G.arcs[id];
      var from = group[a.v], into = group[a.u];
      group = group.map(function (g) { return g === from ? into : g; });
      groups -= 1;
      trace.push({ at: trace.length, arc: id, merged: [a.u, a.v], groups: groups });
      live = liveArcs();
    }
    return runOf({ group: group, cutSize: live.length, groups: groups }, { rounds: trace.length }, trace);
  }
  /* The true minimum cut, over every bipartition -- 2^(n-1) - 1 of them, so the
     cap is where a browser stops being interactive. */
  function minCutBrute(G, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('minCutBrute', G.n, cap);
    var best = null, bestSide = null;
    for (var mask = 1; mask < (1 << (G.n - 1)); mask += 1) {
      var side = [];
      for (var v = 0; v < G.n; v += 1) side.push((mask >> v) & 1);
      var size = 0;
      G.arcs.forEach(function (a) { if (side[a.u] !== side[a.v]) size += 1; });
      if (best === null || size < best) { best = size; bestSide = side; }
    }
    return { size: best, side: bestSide };
  }

  /* Miller-Rabin's strong test, with the squaring chain modulo n exact at every
     step. The shape is ALGO_JS.powerTrace's -- repeated squaring with the
     invariant result * base^m = x^n checked after every iteration -- with a
     modulus, which powerTrace has not got.

     A NONTRIVIAL SQUARE ROOT OF 1 is the certificate the lesson wants on
     screen: if some x in the chain squares to 1 without being 1 or n-1, then n
     is composite and gcd(x - 1, n) is a factor. */
  function powModTrace(x, e, n) {
    var X = BigInt(x), N = BigInt(n), rows = [];
    var result = 1n, base = X % N, m = BigInt(e), target = null;
    while (m > 0n) {
      if (m % 2n === 1n) result = (result * base) % N;
      rows.push({ result: result, base: base, m: m });
      base = (base * base) % N;
      m = m / 2n;
    }
    return { value: result, rows: rows };
  }
  function strongTest(n, a) {
    var N = BigInt(n), A = BigInt(a);
    if (N < 3n || N % 2n === 0n) return { valid: false };
    var d = N - 1n, s = 0;
    while (d % 2n === 0n) { d /= 2n; s += 1; }
    var pw = powModTrace(a, d, n), x = pw.value;
    var chain = [x], witness = true, nontrivialRoot = null, reason = null;
    if (x === 1n || x === N - 1n) { witness = false; reason = 'a^d is ' + (x === 1n ? '1' : 'n-1'); }
    for (var i = 1; i < s && witness; i += 1) {
      var prev = x;
      x = (x * x) % N;
      chain.push(x);
      if (x === 1n && prev !== 1n && prev !== N - 1n) nontrivialRoot = prev;
      if (x === N - 1n) { witness = false; reason = 'the chain reached n-1 at step ' + i; }
    }
    return { valid: true, d: d, s: s, chain: chain, witness: witness,
             nontrivialRoot: nontrivialRoot,
             reason: reason || 'the chain never reached n-1, so a is a witness',
             squarings: pw.rows.length };
  }
  /* Every base in [2, n-2] tested. The lesson's figure is the FRACTION of bases
     that are witnesses -- at least 3/4 for a composite, and the Carmichael
     numbers the mode offers are where the Fermat test fails and this one does
     not. n <= 2000, because the test is n - 3 modular exponentiations. */
  function witnessCount(n, cap) {
    cap = cap === undefined ? 2000 : cap;
    oracleCap('witnessCount', n, cap);
    var witnesses = 0, total = 0, examples = [];
    for (var a = 2; a <= n - 2; a += 1) {
      var r = strongTest(n, a);
      if (!r.valid) continue;
      total += 1;
      if (r.witness) { witnesses += 1; if (examples.length < 5) examples.push(a); }
    }
    return { witnesses: witnesses, total: total, examples: examples,
             fraction: total ? R(BigInt(witnesses), BigInt(total)) : R(0n, 1n),
             prime: witnesses === 0 && total > 0 };
  }

  /* MAX-3-SAT over every assignment. The mean number of satisfied clauses is
     computed exactly -- as a rational over 2^n -- and compared with 7m/8, which
     is exact too when every clause has three distinct variables: each clause is
     satisfied by 7 of its 8 local assignments. Where a clause repeats a
     variable the two numbers differ, and that is the mode's second arm. */
  function max3satEnumerate(formula, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('max3satEnumerate', formula.n, cap);
    var m = formula.clauses.length, hist = {}, best = 0, bestAssign = null, total = 0n;
    forEachSubset(formula.n, function (mask) {
      var assign = maskAssign(mask, formula.n), sat = satEval(formula, assign);
      hist[sat] = (hist[sat] || 0) + 1;
      total += BigInt(sat);
      if (sat > best) { best = sat; bestAssign = assign; }
    });
    var count = 2n ** BigInt(formula.n);
    var distinctVars = formula.clauses.every(function (cl) {
      var vs = cl.map(function (l) { return Math.abs(l); });
      return vs.length === 3 && vs[0] !== vs[1] && vs[1] !== vs[2] && vs[0] !== vs[2];
    });
    return { mean: R(total, count), sevenEighths: R(BigInt(7 * m), 8n),
             matchesSevenEighths: Requ(R(total, count), R(BigInt(7 * m), 8n)),
             allDistinct: distinctVars, best: best, bestAssignment: bestAssign,
             histogram: hist, assignments: count };
  }
"""


# --------------------------------------------- 4.13 reduction (course 9)

REDUCTION_JS = r"""
  /* Reductions, each one built and then CHECKED: the transformed instance is
     constructed, both problems are brute-forced, and the two answers are shown
     to agree. That is what makes a reduction a fact on the page rather than an
     assertion, and it is why every mode here has a cap -- the checking is
     exponential in both directions at once. */

  /* Search from decision, by fixing one variable at a time: n calls to a
     decision oracle produce a satisfying assignment. The oracle is played by
     ORACLE_JS.satBrute, which is the joke the lesson makes deliberately -- an
     exponential oracle is still an oracle, and the REDUCTION is what is being
     shown, not an efficient algorithm. */
  function fixVariable(formula, v, value) {
    var clauses = [];
    for (var i = 0; i < formula.clauses.length; i += 1) {
      var cl = formula.clauses[i], keep = [], satisfied = false;
      for (var k = 0; k < cl.length; k += 1) {
        var lit = cl[k];
        if (Math.abs(lit) === v) {
          if ((lit > 0) === value) { satisfied = true; break; }
        } else keep.push(lit);
      }
      if (!satisfied) clauses.push(keep);
    }
    return { n: formula.n, clauses: clauses };
  }
  function selfReduce(formula) {
    var c = counter(), assign = [], cur = formula, trace = [];
    var first = satBrute(formula);
    c.calls += 1;
    if (!first.result.satisfiable) {
      return runOf({ satisfiable: false, assignment: null }, usedCounts(c), trace);
    }
    for (var v = 1; v <= formula.n; v += 1) {
      var withTrue = fixVariable(cur, v, true);
      var ok = satBrute(withTrue).result.satisfiable
               && !withTrue.clauses.some(function (cl) { return cl.length === 0; });
      c.calls += 1;
      assign.push(ok);
      cur = fixVariable(cur, v, ok);
      trace.push({ at: v - 1, variable: v, set: ok, clausesLeft: cur.clauses.length });
    }
    return runOf({ satisfiable: true, assignment: assign,
                   verified: satEval(formula, assign) === formula.clauses.length,
                   oracleCalls: c.calls }, usedCounts(c), trace);
  }

  /* Hamilton circuit to TSP: distance 1 on an edge, 2 off it, budget n. A tour
     of length n exists exactly when a Hamilton circuit does, and both sides are
     brute-forced so the reader sees the two answers agree rather than being
     told they must. */
  function tspFromGraph(G) {
    var D = [], i, j;
    var adj = dgAdjacency(G);
    for (i = 0; i < G.n; i += 1) {
      D.push([]);
      for (j = 0; j < G.n; j += 1) D[i].push(i === j ? 0 : (adj[i][j] ? 1 : 2));
    }
    return { D: D, budget: G.n };
  }
  function checkTspReduction(G) {
    var made = tspFromGraph(G);
    var tour = tspBrute(made.D, made.budget);
    var ham = hamiltonBrute(G);
    return { D: made.D, budget: made.budget, tourLength: tour.result.length,
             withinBudget: tour.result.withinBudget, hasCircuit: ham.result.circuit !== null,
             agree: tour.result.withinBudget === (ham.result.circuit !== null) };
  }

  /* 3-SAT to independent set: a triangle per clause, one vertex per literal,
     and an edge between every pair of contradictory literals. An independent
     set of size m picks one true literal per clause without contradiction,
     which is a satisfying assignment. */
  function satToIndependentSet(formula) {
    var nodes = [], i, k;
    formula.clauses.forEach(function (cl, ci) {
      cl.forEach(function (lit, li) { nodes.push({ clause: ci, lit: lit, index: nodes.length }); });
    });
    var G = dgNew(nodes.length, false);
    for (i = 0; i < nodes.length; i += 1) {
      for (k = i + 1; k < nodes.length; k += 1) {
        if (nodes[i].clause === nodes[k].clause) { dgAdd(G, i, k, 1, 0); continue; }
        if (nodes[i].lit === -nodes[k].lit) dgAdd(G, i, k, 1, 0);
      }
    }
    return { graph: G, nodes: nodes, k: formula.clauses.length };
  }
  function checkIndependentSetReduction(formula) {
    var made = satToIndependentSet(formula);
    var iset = independentSetBrute(made.graph, made.k);
    var sat = satBrute(formula);
    var readBack = null;
    if (iset.result.atLeastK) {
      readBack = new Array(formula.n).fill(false);
      iset.result.atLeastK.forEach(function (idx) {
        var lit = made.nodes[idx].lit;
        readBack[Math.abs(lit) - 1] = lit > 0;
      });
    }
    return { graph: made.graph, k: made.k, size: iset.result.size,
             satisfiable: sat.result.satisfiable,
             agree: (iset.result.size >= made.k) === sat.result.satisfiable,
             assignment: readBack,
             readBackSatisfies: readBack ? satEval(formula, readBack) === formula.clauses.length : null };
  }

  /* The complement, and the three sets that are the same fact three ways: an
     independent set in G is a clique in the complement, and its complement in
     V is a vertex cover. |S| + |C| = V, checked. */
  function complementGraph(G) {
    var adj = dgAdjacency(G), H = dgNew(G.n, false);
    for (var i = 0; i < G.n; i += 1) {
      for (var j = i + 1; j < G.n; j += 1) if (!adj[i][j]) dgAdd(H, i, j, 1, 0);
    }
    return H;
  }
  function checkComplementIdentity(G) {
    var iset = independentSetBrute(G), cover = vertexCoverBrute(G);
    var clique = cliqueBrute(complementGraph(G));
    return { independent: iset.result.size, cover: cover.result.size,
             cliqueInComplement: clique.result.size, V: G.n,
             identityHolds: iset.result.size + cover.result.size === G.n,
             cliqueMatches: clique.result.size === iset.result.size };
  }

  /* 3-SAT to subset sum, by the digit table: one base-10 column per variable
     and per clause, two numbers per variable, two slack numbers per clause, and
     a target of 1s and 4s. Base 10 rather than base 2 so no column can carry,
     which is the step readers skip and the reason the reduction works. */
  function satToSubsetSum(formula) {
    var n = formula.n, m = formula.clauses.length, rows = [], i, j;
    function digits(vals) {
      var s = 0n, pow = 1n;
      for (var k = vals.length - 1; k >= 0; k -= 1) { s += BigInt(vals[k]) * pow; pow *= 10n; }
      return s;
    }
    for (i = 1; i <= n; i += 1) {
      var t = new Array(n + m).fill(0), f = new Array(n + m).fill(0);
      t[i - 1] = 1; f[i - 1] = 1;
      formula.clauses.forEach(function (cl, ci) {
        if (cl.indexOf(i) !== -1) t[n + ci] = 1;
        if (cl.indexOf(-i) !== -1) f[n + ci] = 1;
      });
      rows.push({ label: 'x' + i + ' true', value: digits(t), digits: t.slice() });
      rows.push({ label: 'x' + i + ' false', value: digits(f), digits: f.slice() });
    }
    for (j = 0; j < m; j += 1) {
      for (var s = 1; s <= 2; s += 1) {
        var slack = new Array(n + m).fill(0);
        slack[n + j] = s;
        rows.push({ label: 'slack ' + (j + 1) + '.' + s, value: digits(slack), digits: slack.slice() });
      }
    }
    var target = new Array(n + m).fill(0);
    for (i = 0; i < n; i += 1) target[i] = 1;
    for (j = 0; j < m; j += 1) target[n + j] = 4;
    return { rows: rows, target: digits(target), targetDigits: target, columns: n + m };
  }
  /* The DP that verifies it -- pseudo-polynomial in the target, which is the
     other half of the lesson: this table is huge because the NUMBERS are huge,
     and the reduction's numbers are exponential in the formula's size. */
  function subsetSumDp(nums, T) {
    var c = counter(), reach = { '0': [] }, keys = ['0'];
    nums.forEach(function (v, i) {
      var added = [];
      keys.forEach(function (k) {
        var next = (BigInt(k) + v).toString();
        c.reads += 1;
        if (reach[next] === undefined && BigInt(next) <= T) { reach[next] = reach[k].concat([i]); added.push(next); }
      });
      keys = keys.concat(added);
    });
    var hit = reach[T.toString()];
    return runOf({ reachable: keys.length, members: hit === undefined ? null : hit,
                   found: hit !== undefined }, usedCounts(c), []);
  }

  /* The clause gadget's colourings, enumerated against the clause's satisfying
     assignments: the counts must match, which is what "the gadget encodes the
     clause" means. `gadget` is a DIGRAPH_JS graph with some vertices pinned. */
  function colouringEnumerate(G, k, pinned, cap) {
    cap = cap === undefined ? 9 : cap;
    oracleCap('colouringEnumerate', G.n, cap);
    var adj = dgAdjacency(G), colourings = [], total = Math.pow(k, G.n);
    for (var code = 0; code < total; code += 1) {
      var colour = [], x = code, v;
      for (v = 0; v < G.n; v += 1) { colour.push(x % k); x = Math.floor(x / k); }
      var ok = true;
      if (pinned) {
        Object.keys(pinned).forEach(function (p) { if (colour[p] !== pinned[p]) ok = false; });
      }
      for (v = 0; ok && v < G.n; v += 1) {
        for (var u = v + 1; u < G.n; u += 1) if (adj[v][u] && colour[v] === colour[u]) { ok = false; break; }
      }
      if (ok) colourings.push(colour);
    }
    return { colourings: colourings, count: colourings.length, examined: total };
  }
"""


# ------------------------------------------------ 4.14 coping (course 9)

COPING_JS = r"""
  /* What to do when the problem is hard: search with a bound, solve a special
     case exactly, approximate with a guarantee, or parameterise. Every mode
     prints the RATIO the algorithm achieved beside the ratio it promised, and
     the optimum both are measured against is a brute-force one.

     The charges in `setcover` are exact fractions and the bound they are
     compared against is H_n * OPT with H_n = sysdesign_core.harmonic(n, 1),
     exact -- which is the whole reason that function is a dependency of this
     block. */

  /* Branch and bound on the 0/1 knapsack. Two arms: no bound at all, which
     explores the whole 2^n tree, and the fractional relaxation as the bound,
     which is GREEDY_JS.fractionalKnapsack -- the point being that the bound is
     the SAME algorithm the greedy lesson already built. */
  function branchBound(items, W, useBound) {
    var c = counter(), best = 0, bestSet = [], trace = [], pruned = 0;
    function relax(i, left) {
      /* the fractional optimum of the items from i on, which is an upper bound
         on any completion -- and it is exact, a rational compared with Rcmp */
      var rest = items.slice(i);
      if (!rest.length || left <= 0) return R(0n, 1n);
      return fractionalKnapsack(rest, left).result.value;
    }
    (function go(i, left, value, chosen) {
      c.nodes += 1;
      if (value > best) { best = value; bestSet = chosen.slice(); }
      if (i >= items.length) return;
      if (useBound) {
        var bound = Radd(R(BigInt(value), 1n), relax(i, left));
        trace.push({ at: trace.length, depth: i, value: value, bound: bound });
        if (Rcmp(bound, R(BigInt(best), 1n)) <= 0) { pruned += 1; return; }
      } else {
        trace.push({ at: trace.length, depth: i, value: value, bound: null });
      }
      if (items[i].w <= left) {
        chosen.push(i);
        go(i + 1, left - items[i].w, value + items[i].v, chosen);
        chosen.pop();
      }
      go(i + 1, left, value, chosen);
    })(0, W, 0, []);
    var exact = knapsackBrute(items, W);
    return runOf({ value: best, members: bestSet, pruned: pruned,
                   full: Math.pow(2, items.length), optimum: exact.result.value,
                   correct: best === exact.result.value },
                 usedCounts(c), trace);
  }

  /* Vertex cover from a MAXIMAL MATCHING: take both ends of every matched edge.
     The matching is a lower bound on OPT and the cover is twice it, so the
     ratio is at most 2 -- and the tight instance the mode offers is a perfect
     matching, where it is exactly 2. */
  function maximalMatching(G) {
    var c = counter(), used = new Array(G.n).fill(false), matched = [];
    G.arcs.forEach(function (a, id) {
      c.compares += 1;
      if (a.u === a.v || used[a.u] || used[a.v]) return;
      used[a.u] = true; used[a.v] = true;
      matched.push(id);
    });
    var cover = [];
    matched.forEach(function (id) { cover.push(G.arcs[id].u); cover.push(G.arcs[id].v); });
    cover.sort(function (x, y) { return x - y; });
    var opt = vertexCoverBrute(G);
    return runOf({ matching: matched, cover: cover, size: cover.length,
                   optimum: opt.result.size,
                   ratio: opt.result.size ? R(BigInt(cover.length), BigInt(opt.result.size)) : R(0n, 1n),
                   lowerBound: matched.length, withinTwo: cover.length <= 2 * opt.result.size },
                 usedCounts(c), []);
  }

  /* The metric TSP 2-approximation: an MST, doubled into an Euler tour, then
     shortcut. The shortcut step is where the TRIANGLE INEQUALITY is used, and
     the mode's toggle drops it -- on a non-metric instance the bound simply
     fails, which is not a bug in the algorithm but the hypothesis doing work. */
  function mstTour(D) {
    var n = D.length, G = dgNew(n, false), i, j;
    for (i = 0; i < n; i += 1) for (j = i + 1; j < n; j += 1) dgAdd(G, i, j, D[i][j], 0);
    var mst = primRun(G, 0);
    var adj = [];
    for (i = 0; i < n; i += 1) adj.push([]);
    mst.result.arcs.forEach(function (id) {
      adj[G.arcs[id].u].push(G.arcs[id].v);
      adj[G.arcs[id].v].push(G.arcs[id].u);
    });
    var euler = [], seen = new Array(n).fill(false);
    (function walk(v) {
      euler.push(v); seen[v] = true;
      adj[v].sort(function (a, b) { return a - b; }).forEach(function (u) {
        if (!seen[u]) { walk(u); euler.push(v); }
      });
    })(0);
    var tour = [], onTour = new Array(n).fill(false);
    euler.forEach(function (v) { if (!onTour[v]) { onTour[v] = true; tour.push(v); } });
    var length = 0;
    for (i = 0; i < tour.length; i += 1) length += D[tour[i]][tour[(i + 1) % tour.length]];
    var metric = true;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) for (var k = 0; k < n; k += 1) {
      if (D[i][j] > D[i][k] + D[k][j]) metric = false;
    }
    var opt = tspBrute(D);
    return runOf({ mst: mst.result.arcs, mstWeight: mst.result.weight, euler: euler,
                   tour: tour, length: length, optimum: opt.result.length,
                   ratio: R(BigInt(length), BigInt(opt.result.length || 1)),
                   metric: metric, withinTwo: length <= 2 * opt.result.length },
                 mst.counts, []);
  }

  /* Greedy set cover, with each element's CHARGE as an exact fraction: the set
     chosen at a step costs 1 and covers k new elements, so each of them is
     charged 1/k. The charges sum to the cover's size by construction, and the
     bound is H_n * OPT -- an exact rational times an integer, so the page can
     print the two and the reader can see one under the other. */
  function greedySetCover(sets, universe) {
    var c = counter(), covered = {}, chosen = [], charges = {}, trace = [];
    var target = universe.slice();
    while (Object.keys(covered).length < target.length) {
      var best = -1, bestNew = [];
      sets.forEach(function (s, i) {
        c.compares += 1;
        if (chosen.indexOf(i) !== -1) return;
        var fresh = s.filter(function (e) { return !covered[e]; });
        if (fresh.length > bestNew.length) { best = i; bestNew = fresh; }
      });
      if (best === -1) break;
      chosen.push(best);
      var price = R(1n, BigInt(bestNew.length));
      bestNew.forEach(function (e) { covered[e] = true; charges[e] = price; });
      trace.push({ at: trace.length, set: best, fresh: bestNew.slice(), charge: price });
    }
    var total = R(0n, 1n);
    Object.keys(charges).forEach(function (e) { total = Radd(total, charges[e]); });
    var opt = setCoverBrute(sets, target);
    var Hn = harmonic(target.length, 1);
    var bound = Rmul(Hn, R(BigInt(opt.result.size), 1n));
    return runOf({ chosen: chosen, size: chosen.length, charges: charges,
                   chargeTotal: total, optimum: opt.result.size, Hn: Hn, bound: bound,
                   chargesSumToSize: Requ(total, R(BigInt(chosen.length), 1n)),
                   withinBound: Rcmp(R(BigInt(chosen.length), 1n), bound) <= 0 },
                 usedCounts(c), trace);
  }
  /* The optimum cover, over every subfamily. Twelve sets is 4096 subfamilies. */
  function setCoverBrute(sets, universe, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('setCoverBrute', sets.length, cap);
    var best = null, bestPick = [], examined = 0;
    forEachSubset(sets.length, function (mask) {
      examined += 1;
      if (best !== null && popcount(mask) >= best) return;
      var members = maskMembers(mask, sets.length), hit = {};
      members.forEach(function (i) { sets[i].forEach(function (e) { hit[e] = true; }); });
      if (universe.every(function (e) { return hit[e]; })) {
        if (best === null || members.length < best) { best = members.length; bestPick = members; }
      }
    });
    return runOf({ size: best === null ? null : best, members: bestPick },
                 { nodes: examined }, []);
  }

  /* The knapsack FPTAS: scale every value down by a factor that depends on
     epsilon, solve the scaled instance exactly by the value DP, and lose at
     most epsilon * OPT. epsilon is a RATIONAL, so the scale factor and the
     promised loss are exact and the measured loss can be compared with the
     promise as a fraction rather than as two decimals. */
  function valueDp(items, W) {
    /* The DP is indexed by VALUE, not by weight: best[v] is the least weight
       that achieves value v. That is the table the FPTAS shrinks -- scaling the
       values shortens this array, which is the whole trick -- and it carries
       the chosen items, because the approximation's quality is the ORIGINAL
       value of the set the scaled table picked. */
    var c = counter(), totalValue = items.reduce(function (t, it) { return t + it.v; }, 0);
    var best = new Array(totalValue + 1).fill(null), pick = new Array(totalValue + 1).fill(null);
    best[0] = 0; pick[0] = [];
    items.forEach(function (it, i) {
      for (var v = totalValue; v >= it.v; v -= 1) {
        c.reads += 1;
        if (best[v - it.v] === null) continue;
        var w = best[v - it.v] + it.w;
        if (best[v] === null || w < best[v]) { best[v] = w; pick[v] = pick[v - it.v].concat([i]); }
      }
    });
    var answer = 0, members = [];
    for (var v2 = totalValue; v2 >= 0; v2 -= 1) {
      if (best[v2] !== null && best[v2] <= W) { answer = v2; members = pick[v2] || []; break; }
    }
    return runOf({ value: answer, members: members, table: best, cells: totalValue + 1 },
                 usedCounts(c), []);
  }
  function fptasScale(items, W, eps) {
    var vmax = items.reduce(function (t, it) { return Math.max(t, it.v); }, 0);
    /* K = eps * vmax / n, kept as a rational and used as a divisor so the
       scaled values are exact floors rather than rounded doubles. */
    var K = Rdiv(Rmul(eps, R(BigInt(vmax), 1n)), R(BigInt(items.length), 1n));
    var scaled = items.map(function (it) {
      return { w: it.w, v: Rzero(K) ? it.v : Number(Rfloor(Rdiv(R(BigInt(it.v), 1n), K))) };
    });
    var approx = valueDp(scaled, W);
    /* The set the SCALED table chose, valued at the ORIGINAL prices. That is
       what the guarantee is about, and re-deriving the set any other way is how
       an FPTAS lab ends up reporting the scaled number as the answer. */
    var chosen = approx.result.members.slice();
    var got = chosen.reduce(function (t, i) { return t + items[i].v; }, 0);
    var exact = knapsackBrute(items, W).result.value;
    var loss = exact - got;
    return runOf({ K: K, scaled: scaled, chosen: chosen, value: got, optimum: exact,
                   loss: loss, promised: Rmul(eps, R(BigInt(exact), 1n)),
                   withinPromise: Rcmp(R(BigInt(loss), 1n), Rmul(eps, R(BigInt(exact), 1n))) <= 0,
                   cells: approx.result.cells },
                 approx.counts, []);
  }

  /* Derandomisation by conditional expectations. At each variable the exact
     conditional expectation of the number of satisfied clauses is computed for
     both values -- rationals, because they are sums of powers of one half --
     and the larger is taken. The final assignment is guaranteed to be at least
     the unconditional mean, which is the whole method, and the page prints both
     branches at every step so the reader sees the choice being made. */
  function condExpect(formula, partial) {
    var total = R(0n, 1n);
    formula.clauses.forEach(function (cl) {
      var free = 0, satisfied = false;
      cl.forEach(function (lit) {
        var v = Math.abs(lit) - 1;
        if (partial[v] === undefined || partial[v] === null) { free += 1; return; }
        if ((lit > 0) === partial[v]) satisfied = true;
      });
      if (satisfied) { total = Radd(total, R(1n, 1n)); return; }
      /* every free literal must be false to lose the clause: 1 - 2^-free */
      total = Radd(total, Rsub(R(1n, 1n), R(1n, 2n ** BigInt(free))));
    });
    return total;
  }
  function derandomise(formula) {
    var partial = new Array(formula.n).fill(null), trace = [], c = counter();
    var start = condExpect(formula, partial);
    for (var v = 0; v < formula.n; v += 1) {
      var t = partial.slice(), f = partial.slice();
      t[v] = true; f[v] = false;
      var et = condExpect(formula, t), ef = condExpect(formula, f);
      c.compares += 1;
      partial[v] = Rcmp(et, ef) >= 0;
      trace.push({ at: v, variable: v + 1, ifTrue: et, ifFalse: ef, took: partial[v] });
    }
    var got = satEval(formula, partial);
    return runOf({ assignment: partial, satisfied: got, expectation: start,
                   atLeastExpectation: Rcmp(R(BigInt(got), 1n), start) >= 0 },
                 usedCounts(c), trace);
  }

  /* Fixed-parameter vertex cover: a bounded search tree of depth k. Pick any
     uncovered edge -- one of its two ends must be in the cover -- and branch.
     The tree has at most 2^k nodes no matter how big the graph is, and the mode
     prints 2^k * n against 2^n, which is the whole idea of parameterising. */
  function fptVertexCover(G, k) {
    var c = counter(), found = null, trace = [];
    (function go(cover, budget) {
      c.nodes += 1;
      if (found) return;
      var inSet = new Array(G.n).fill(false);
      cover.forEach(function (v) { inSet[v] = true; });
      var bad = null;
      for (var i = 0; i < G.arcs.length && !bad; i += 1) {
        var a = G.arcs[i];
        if (a.u !== a.v && !inSet[a.u] && !inSet[a.v]) bad = a;
      }
      if (!bad) { found = cover.slice(); return; }
      trace.push({ at: trace.length, budget: budget, edge: [bad.u, bad.v], cover: cover.slice() });
      if (budget === 0) return;
      go(cover.concat([bad.u]), budget - 1);
      go(cover.concat([bad.v]), budget - 1);
    })([], k);
    var exact = vertexCoverBrute(G);
    return runOf({ cover: found, size: found ? found.length : null, k: k,
                   optimum: exact.result.size, exists: !!found,
                   correct: !!found === (exact.result.size <= k),
                   treeBound: Math.pow(2, k + 1), work: Math.pow(2, k) * G.n,
                   bruteWork: Math.pow(2, G.n) },
                 usedCounts(c), trace);
  }

  /* DPLL: unit propagation, pure literals, then a decision. The counters are
     the content -- propagations and pure literals are free progress, decisions
     and conflicts are the search -- and the mode's hard-random toggle produces
     an instance at the satisfiability threshold where the free progress stops. */
  function dpllRun(formula) {
    var c = counter(), trace = [];
    function simplify(clauses, lit) {
      var out = [];
      for (var i = 0; i < clauses.length; i += 1) {
        var cl = clauses[i];
        if (cl.indexOf(lit) !== -1) continue;
        out.push(cl.filter(function (l) { return l !== -lit; }));
      }
      return out;
    }
    var answer = null;
    (function solve(clauses, assign, depth) {
      if (answer) return;
      c.nodes += 1;
      var guard = 0;
      while (guard < 200) {
        guard += 1;
        var unit = null, i;
        for (i = 0; i < clauses.length; i += 1) if (clauses[i].length === 1) { unit = clauses[i][0]; break; }
        if (unit !== null) {
          c.calls += 1;
          trace.push({ at: trace.length, depth: depth, kind: 'unit', literal: unit });
          assign = assign.concat([unit]);
          clauses = simplify(clauses, unit);
          continue;
        }
        var seen = {}, pure = null;
        clauses.forEach(function (cl) { cl.forEach(function (l) { seen[l] = true; }); });
        Object.keys(seen).forEach(function (l) {
          var v = Number(l);
          if (pure === null && !seen[-v]) pure = v;
        });
        if (pure !== null) {
          c.reads += 1;
          trace.push({ at: trace.length, depth: depth, kind: 'pure', literal: pure });
          assign = assign.concat([pure]);
          clauses = simplify(clauses, pure);
          continue;
        }
        break;
      }
      if (clauses.some(function (cl) { return cl.length === 0; })) {
        c.rounds += 1;
        trace.push({ at: trace.length, depth: depth, kind: 'conflict' });
        return;
      }
      if (!clauses.length) { answer = assign; return; }
      var pick = Math.abs(clauses[0][0]);
      c.compares += 1;
      trace.push({ at: trace.length, depth: depth, kind: 'decision', literal: pick });
      solve(simplify(clauses, pick), assign.concat([pick]), depth + 1);
      if (!answer) solve(simplify(clauses, -pick), assign.concat([-pick]), depth + 1);
    })(formula.clauses.map(function (cl) { return cl.slice(); }), [], 0);
    var full = null;
    if (answer) {
      full = new Array(formula.n).fill(false);
      answer.forEach(function (l) { full[Math.abs(l) - 1] = l > 0; });
    }
    var brute = satBrute(formula);
    var counts = usedCounts(c);
    return runOf({ satisfiable: !!answer, assignment: full,
                   decisions: trace.filter(function (t) { return t.kind === 'decision'; }).length,
                   propagations: trace.filter(function (t) { return t.kind === 'unit'; }).length,
                   pures: trace.filter(function (t) { return t.kind === 'pure'; }).length,
                   conflicts: counts.rounds || 0,
                   bruteWork: Math.pow(2, formula.n),
                   agrees: (!!answer) === brute.result.satisfiable,
                   verified: full ? satEval(formula, full) === formula.clauses.length : null },
                 counts, trace);
  }
"""

__all__ = [
    # shared
    "COUNT_JS", "RFIXED_JS", "SERIES_JS", "DIGRAPH_JS", "ORACLE_JS",
    "SEEDED_JS", "TREEDRAW_JS",
    # one per kit, in the order of the design's sections 4.1 - 4.14
    "SEQ_JS", "HEAP_JS", "HASH_JS", "TREE_JS", "SORT_JS", "GRAPHKIT_JS",
    "FLOW_JS", "GREEDY_JS", "DP_JS", "STRINGS_JS", "GEOM_JS", "RANDOM_JS",
    "REDUCTION_JS", "COPING_JS",
]
