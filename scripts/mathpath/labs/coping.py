"""Coping with intractability -- six modes, and never a ratio without its optimum.

THE RULE THIS KIT IS BUILT AROUND. An approximation ratio is a comparison
between two numbers and a page that prints one of them has printed nothing. So
every mode here computes BOTH halves, on instances small enough that the
second half is an exhaustive search rather than an estimate:

    the algorithm's answer   the shipped algorithm, run on the reader's own
                             instance, with its counters
    the true optimum         every subset, every assignment, every tour --
                             `algo_core.ORACLE_JS`, at a cap the page states
    the realised ratio       the first divided by the second, as an exact
                             fraction, printed beside the ratio that was
                             PROMISED
    the lower bound the      a 2-approximation is not a claim about the
    promise rests on         optimum, which nobody knows; it is a claim about
                             a LOWER BOUND the algorithm can see. Every mode
                             draws the chain -- lower bound ≤ optimum ≤
                             answer ≤ promise × lower bound -- as four
                             computed numbers, because the chain IS the proof
                             and its middle inequality is the only one that
                             needs the optimum at all

There is no mode in this kit that prints a ratio and stops, and there is no
figure in it whose denominator was guessed.

AND THE INSTANCE THAT ATTAINS THE WORST CASE, FOUND RATHER THAN QUOTED.
"Tight" is the word a textbook uses and a reader cannot check. `vertexcover`
enumerates EVERY graph on the number of vertices the slider names -- 1024 of
them at five vertices, each solved exactly -- and reports the worst ratio any
of them produced and the graph that produced it. The answer is 2 and the graph
is a perfect matching, which is what the books say; the difference is that the
page found it. `fptas` does the same over epsilon, and `setcover` opens on the
family that forces the logarithm.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE.
`algo_core.COPING_JS` holds the algorithms -- `branchBound`, `maximalMatching`,
`mstTour`, `greedySetCover`, `setCoverBrute`, `valueDp`, `fptasScale`,
`fptVertexCover` -- and nothing here reimplements one. What this kit adds:

  an exhaustive search        every mode's optimum comes from ORACLE_JS or
  written from the            from `setCoverBrute`, which enumerate subsets
  definition                  and permutations and know nothing about the
                              approximation they are checking.
  the same answer twice       `branchBound` with the fractional bound and
                              without it must agree, and both must agree with
                              `knapsackBrute`. `fptVertexCover` at budget k
                              must say yes exactly when the brute-force cover
                              has size at most k. `fptasScale` at a small
                              enough epsilon must find the optimum exactly.
  every instance of a size    `cpWorstRatio` enumerates every graph on n
                              vertices, runs the approximation and the exact
                              optimum on each, and reports the worst. That is
                              a claim about ALL instances of that size, which
                              is a different kind of statement from a ratio on
                              one instance, and this Subject's whole hazard.
  the charge identity         `greedySetCover` prices every element at 1/k
                              when the set covering it was new to k elements;
                              the charges must add to the cover's size exactly,
                              and the page checks the sum rather than showing
                              the prices and moving on.

THE MODES, and which of the four strategies each one is:

  branchbound  search with a bound. The fractional relaxation prunes, the
               same search without it does not, and both find the optimum --
               so the bound costs nothing in correctness and the node counts
               say what it bought.
  vertexcover  approximate with a guarantee. A maximal matching is a lower
               bound on the optimum and its endpoints are a cover, so the
               ratio is at most 2; every graph of the chosen size is then
               enumerated to find the one that attains it.
  tsp          approximate with a guarantee, and the hypothesis doing work.
               An MST doubled and shortcut is within 2 of the optimum when
               the distances obey the triangle inequality, and the mode lets
               the reader break it and watch the bound fail.
  setcover     approximate with a guarantee, logarithmically. Every element
               carries an exact fractional charge, the charges add to the
               answer, and the bound is H_n × OPT with H_n exact.
  fptas        approximate as closely as you are willing to pay for. Epsilon
               is a rational, so the scale factor, the promised loss and the
               realised loss are all fractions and the promise is checked
               rather than described.
  fpt          parameterise. A bounded search tree of depth k answers a
               question about a graph of any size, and the page prints
               2^k × n against 2^n with both numbers computed.

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped and COPING_JS
depends on more of the core than any other block on this path.

    every mode        RATIONAL_JS, RFIXED_JS, COUNT_JS, DIGRAPH_JS, ORACLE_JS,
                      COPING_JS and this kit's own block
    branchbound       GREEDY_JS, for `fractionalKnapsack` -- the bound IS the
    fptas             greedy algorithm the previous course built -- and
                      RCEIL_JS for the FPTAS's floor
    tsp               GRAPHKIT_JS for `primRun` and its priority queue, and
                      ALGO_JS for `ilog2`, which primRun's returned bound
                      calls whether or not a page prints it
    setcover          HARMONIC_JS, for H_n exact

Measured, gzipped, on a real shipped lesson page with this lab swapped in --
Algorithms course 1 lesson 1, whose body is heavier than the median. Against
the repository's 62 KB ceiling:

    vertexcover 46.5   fpt 46.7   setcover 46.9   fptas 51.2
    branchbound 51.3   tsp 56.3

Re-derive them rather than trusting them. `tsp` is the heaviest at 56.3, five
kilobytes clear of the next, and the reason is in the table above: it is the
only mode that
carries the graph-algorithms block and the Discrete Mathematics algorithms
block, both of them for one function each. Writing a local Prim would save
about four kilobytes and would put a second minimum-spanning-tree
implementation in the repository, which is the trade this path does not make:
the shared one is the one mathcheck proves.

WHAT IS EXACT AND WHAT IS NOT. Everything. Sizes, weights, tour lengths, node
counts and cover sizes are integers; ratios, charges, epsilons, scale factors
and H_n are BigInt over BigInt. There is no floating-point comparison anywhere
in this kit and no verdict is read off a decimal -- `Rcmp` decides every
"within the bound" on the page. The one place a double appears is `ilog2`
inside primRun's returned E log V field, which no mode here prints.

WHAT COPING_JS SHIPS THAT NO MODE HERE CALLS. `derandomise`, the conditional-
expectation method, and `dpllRun`. Both are real lessons and neither has a
mode yet: derandomisation belongs beside the randomised 7/8 argument in
`random.max3sat` and reads oddly without it, and DPLL is a search-with-a-bound
mode that would duplicate `branchbound`'s shape on a different problem. They
are tested in mathcheck's algo_core section and they are on every page in this
kit anyway, because COPING_JS is one block.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import (COPING_JS, COUNT_JS, DIGRAPH_JS, GRAPHKIT_JS, GREEDY_JS,
                        ORACLE_JS, RFIXED_JS)
from .algorithms import ALGO_JS
from .common import Lab
from .sysdesign_core import HARMONIC_JS, RCEIL_JS

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

CPKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     Four grammars, all 1-based, all comma-separated.

       an item      `3:5` -- weight 3, value 5. Two numbers with a colon
                    between them, because `3 5` reads as two items and every
                    knapsack lesson that used a space has had to explain that.
       an edge      `1-2`, undirected.
       a distance   `1-2 7`, undirected, and every pair must be given: a
                    travelling salesman instance with a missing distance is
                    not an instance, and defaulting it would invent data.
       a set        `1 2 3`, elements separated by spaces, sets by a
                    semicolon. The universe is the union, which is the only
                    universe a cover can be judged against. */
  var CP_MAXITEMS = 12;
  var CP_MAXN = 8;
  var CP_MAXSETS = 10;

  function cpPieces(text, re) {
    var parts = String(text).split(re), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }
  function cpParseItems(text, maxItems) {
    maxItems = maxItems === undefined ? CP_MAXITEMS : maxItems;
    var cl = cpPieces(text, /[,;\n]+/), items = [], i;
    if (!cl.length) return { bad: 'write at least one item' };
    if (cl.length > maxItems) return { bad: 'that is more than ' + maxItems + ' items' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*[:\/]\s*(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as weight:value' };
      var w = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (w < 1) return { bad: 'an item of weight 0 is always taken and teaches nothing' };
      if (w > 99) return { bad: 'keep the weights under 100' };
      if (v > 999) return { bad: 'keep the values under 1000' };
      items.push({ w: w, v: v });
    }
    return { items: items };
  }
  function cpParseGraph(text, maxN) {
    maxN = maxN === undefined ? CP_MAXN : maxN;
    var cl = cpPieces(text, /[,;\n]+/), raw = [], n = 0, seen = {}, i;
    if (!cl.length) return { bad: 'write at least one edge' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*-\s*(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as an edge' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'a loop at ' + u + ' is covered by nothing' };
      var key = Math.min(u, v) + '-' + Math.max(u, v);
      if (seen[key]) continue;
      seen[key] = true;
      raw.push([u, v]);
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (!raw.length) return { bad: 'every edge you wrote was a duplicate' };
    var G = dgNew(n, false);
    for (i = 0; i < raw.length; i += 1) dgAdd(G, raw[i][0] - 1, raw[i][1] - 1, 1, 0);
    return { G: G, n: n };
  }
  /* A complete symmetric distance matrix. Every pair is required, and the
     error names the pair that is missing rather than the count -- a reader
     with eight cities and 27 of 28 distances needs to know which one. */
  function cpParseDistances(text, maxN) {
    maxN = maxN === undefined ? CP_MAXN : maxN;
    var cl = cpPieces(text, /[,;\n]+/), given = {}, n = 0, i, j;
    if (!cl.length) return { bad: 'write at least one distance' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*-\s*(\d+)\s+(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as u-v followed by a distance' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10), w = parseInt(m[3], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'the distance from ' + u + ' to itself is 0 and is not typed' };
      if (w < 1 || w > 999) return { bad: 'keep the distances between 1 and 999' };
      given[Math.min(u, v) + '-' + Math.max(u, v)] = w;
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (n < 3) return { bad: 'a tour needs at least three cities' };
    var D = [];
    for (i = 0; i < n; i += 1) { D.push([]); for (j = 0; j < n; j += 1) D[i].push(0); }
    for (i = 1; i <= n; i += 1) {
      for (j = i + 1; j <= n; j += 1) {
        var key = i + '-' + j;
        if (given[key] === undefined) return { bad: 'the distance ' + i + '-' + j + ' is missing' };
        D[i - 1][j - 1] = given[key];
        D[j - 1][i - 1] = given[key];
      }
    }
    return { D: D, n: n };
  }
  function cpParseSets(text, maxSets) {
    maxSets = maxSets === undefined ? CP_MAXSETS : maxSets;
    var cl = cpPieces(text, /[;\n]+/), sets = [], seen = {}, universe = [], i, k;
    if (!cl.length) return { bad: 'write at least one set' };
    if (cl.length > maxSets) return { bad: 'that is more than ' + maxSets + ' sets' };
    for (i = 0; i < cl.length; i += 1) {
      var parts = cpPieces(cl[i], /[\s,]+/), members = [], inThis = {};
      for (k = 0; k < parts.length; k += 1) {
        if (!/^\d+$/.test(parts[k])) return { bad: 'cannot read "' + parts[k] + '" as an element' };
        var e = parseInt(parts[k], 10);
        if (e < 1 || e > 40) return { bad: 'keep the elements between 1 and 40' };
        if (inThis[e]) continue;
        inThis[e] = true;
        members.push(e);
        if (!seen[e]) { seen[e] = true; universe.push(e); }
      }
      if (!members.length) return { bad: 'set ' + (i + 1) + ' is empty' };
      sets.push(members.sort(function (a, b) { return a - b; }));
    }
    universe.sort(function (a, b) { return a - b; });
    return { sets: sets, universe: universe };
  }
  function cpSetText(list) { return '{' + (list || []).join(', ') + '}'; }
  function cpVertexText(list) {
    return '{' + (list || []).map(function (v) { return v + 1; }).join(', ') + '}';
  }
  function cpPlural(k, one, many) { return k === 1 ? one : many; }
  function cpIsRefusal(e) { return /exceeds the exhaustive cap/.test(String(e && e.message)); }
  /* A rational, and a decimal beside it where the fraction is long. The
     decimal is a rounding of the PRINTING and no verdict is read off it:
     every "within the bound" on these pages is an Rcmp. */
  function cpBoth(a, places) {
    var t = Rtext(a);
    if (a.d === 1n) return t;
    return t + ' = ' + Rfixed(a, places === undefined ? 4 : places);
  }
  function cpRatio(got, opt) {
    if (!opt) return null;
    return R(BigInt(got), BigInt(opt));
  }

  /* ------------------------------------------------- the stays-ahead chain

     THE ONE DRAWING THIS KIT NEEDS, and the reason it is one drawing rather
     than four. Every approximation argument on this course has the same
     shape: a LOWER BOUND the algorithm can compute, the optimum nobody can,
     the answer the algorithm gave, and the promise as a multiple of the lower
     bound. Four numbers on one axis, in that order, and the argument is that
     the order holds.

     Drawing them as four bars on a shared scale is what makes the slack
     visible, and it is why the optimum is in the picture rather than in a
     footnote: the gap between the lower bound and the optimum is what the
     algorithm is paying for, and it is usually most of the gap. */
  function cpLadderSvg(rows, opts) {
    opts = opts || {};
    var box = { left: 150, right: 486, top: 18, bottom: 18 };
    var h = opts.rowHeight === undefined ? 34 : opts.rowHeight;
    var maxV = 0;
    rows.forEach(function (r) { if (r.value > maxV) maxV = r.value; });
    if (!(maxV > 0)) maxV = 1;
    var s = '';
    rows.forEach(function (r, i) {
      var y = box.top + i * h, w = ((r.value / maxV) * (box.right - box.left));
      s += '<text x="' + (box.left - 8) + '" y="' + (y + h / 2 + 4)
        + '" text-anchor="end" font-size="12" font-weight="700" fill="var(--muted)">'
        + r.label + '</text>'
        + '<rect x="' + box.left + '" y="' + (y + 4) + '" width="' + Math.max(1, w).toFixed(1)
        + '" height="' + (h - 12) + '" rx="3" fill="' + r.colour + '" opacity="'
        + (r.faint ? 0.5 : 0.9) + '" />'
        + '<text x="' + (box.left + Math.max(1, w) + 6).toFixed(1) + '" y="' + (y + h / 2 + 4)
        + '" font-size="12" font-weight="800" fill="var(--text)">' + r.text + '</text>';
    });
    /* the vertical line at the optimum, so every other bar is read against it */
    var opt = rows.filter(function (r) { return r.anchor; })[0];
    if (opt) {
      var x = box.left + (opt.value / maxV) * (box.right - box.left);
      s += '<line x1="' + x.toFixed(1) + '" y1="' + (box.top - 6) + '" x2="' + x.toFixed(1)
        + '" y2="' + (box.top + rows.length * h - 6) + '" stroke="var(--red)" stroke-width="2"'
        + ' stroke-dasharray="5 4" />';
    }
    return s;
  }
  function cpDrawLadder(el, rows, opts) {
    var out = cpLadderSvg(rows, opts);
    if (el) el.innerHTML = out;
    return out;
  }
  /* Plain vertical bars, for the node counts and the epsilon sweep. */
  function cpBarsSvg(rows, opts) {
    opts = opts || {};
    var box = { left: 40, right: 490, base: 180, top: 26 };
    var n = rows.length, maxV = opts.maxY || 0;
    if (!opts.maxY) rows.forEach(function (r) { if (r.value > maxV) maxV = r.value; });
    if (!(maxV > 0)) maxV = 1;
    var span = box.base - box.top, W = (box.right - box.left) / Math.max(1, n);
    var s = '<line x1="' + box.left + '" y1="' + box.base + '" x2="' + (box.right + 4)
          + '" y2="' + box.base + '" stroke="var(--line-strong)" />';
    rows.forEach(function (r, i) {
      var hgt = Math.max(0, Math.min(1, r.value / maxV)) * span, x = box.left + i * W + W * 0.16;
      s += '<rect x="' + x.toFixed(1) + '" y="' + (box.base - hgt).toFixed(1) + '" width="'
        + (W * 0.68).toFixed(1) + '" height="' + hgt.toFixed(1) + '" fill="' + r.colour
        + '" opacity="0.9" />'
        + '<text x="' + (x + W * 0.34).toFixed(1) + '" y="' + (box.base - hgt - 5).toFixed(1)
        + '" text-anchor="middle" font-size="11" font-weight="700" fill="var(--text)">'
        + (r.text === undefined ? r.value : r.text) + '</text>'
        + '<text x="' + (x + W * 0.34).toFixed(1) + '" y="' + (box.base + 14)
        + '" text-anchor="middle" font-size="10" fill="var(--muted)">' + r.label + '</text>';
    });
    if (opts.rule) {
      var y = box.base - Math.max(0, Math.min(1, opts.rule.value / maxV)) * span;
      s += '<line x1="' + box.left + '" y1="' + y.toFixed(1) + '" x2="' + box.right + '" y2="'
        + y.toFixed(1) + '" stroke="' + opts.rule.colour + '" stroke-width="2" stroke-dasharray="6 4" />'
        + '<text x="' + (box.right - 2) + '" y="' + Math.max(box.top, y - 5).toFixed(1)
        + '" text-anchor="end" font-size="11" font-weight="700" fill="' + opts.rule.colour + '">'
        + opts.rule.label + '</text>';
    }
    return s;
  }
  function cpDrawBars(el, rows, opts) {
    var out = cpBarsSvg(rows, opts);
    if (el) el.innerHTML = out;
    return out;
  }

  /* ------------------------------------ the worst instance, found not quoted

     EVERY GRAPH ON n VERTICES. There are 2^(n(n-1)/2) of them -- 1024 at five
     vertices, 32768 at six -- and each is solved exactly as well as
     approximately, so this is a statement about ALL instances of that size
     rather than about the one on screen. That distinction is the hazard this
     whole Subject is about, and it is the one thing a page showing a single
     ratio can never make.

     The edges are added in a fixed pair order, which matters: the matching is
     greedy and a greedy result depends on the order it sees the edges in. Two
     readers at the same graph therefore see the same matching, and the worst
     case reported here is the worst case OF THIS IMPLEMENTATION, which is the
     honest claim and is stated on the page in those words. */
  function cpGraphFromMask(n, mask) {
    var G = dgNew(n, false), bit = 0, i, j;
    for (i = 0; i < n; i += 1) {
      for (j = i + 1; j < n; j += 1) {
        if (mask & (1 << bit)) dgAdd(G, i, j, 1, 0);
        bit += 1;
      }
    }
    return G;
  }
  function cpWorstRatio(n, cap) {
    cap = cap === undefined ? 6 : cap;
    oracleCap('cpWorstRatio', n, cap);
    var pairs = (n * (n - 1)) / 2, total = 1 << pairs;
    var best = null, bestMask = -1, examined = 0, withEdges = 0, atWorst = 0;
    var densestMask = -1, densestEdges = -1;
    for (var mask = 1; mask < total; mask += 1) {
      var G = cpGraphFromMask(n, mask);
      examined += 1;
      var run = maximalMatching(G);
      if (!run.result.optimum) continue;
      withEdges += 1;
      var ratio = R(BigInt(run.result.size), BigInt(run.result.optimum));
      var cmp = best === null ? 1 : Rcmp(ratio, best);
      if (cmp > 0) { best = ratio; bestMask = mask; atWorst = 1; densestMask = mask; densestEdges = G.arcs.length; }
      else if (cmp === 0) {
        atWorst += 1;
        /* the SMALLEST instance attaining the worst ratio is the first mask,
           and it is usually one edge; the largest is the interesting one,
           because a reader shown a single edge concludes the bound is an
           artefact of a degenerate case. Both are reported. */
        if (G.arcs.length > densestEdges) { densestMask = mask; densestEdges = G.arcs.length; }
      }
    }
    return { n: n, graphs: examined, withEdges: withEdges, worst: best === null ? R(0n, 1n) : best,
             mask: bestMask, atWorst: atWorst,
             graph: bestMask >= 0 ? cpGraphFromMask(n, bestMask) : dgNew(n, false),
             densest: densestMask >= 0 ? cpGraphFromMask(n, densestMask) : dgNew(n, false),
             densestEdges: densestEdges };
  }
  /* The edge list of a graph, as the reader would have typed it, so the worst
     instance can be pasted back into the box rather than only looked at. */
  function cpEdgeText(G) {
    return G.arcs.map(function (a) { return (a.u + 1) + '-' + (a.v + 1); }).join(', ');
  }

  /* The same question for the metric travelling salesman, over every metric
     instance of a size. The distance range has to be bounded too -- there are
     infinitely many metric instances otherwise -- so the claim the page makes
     is exactly the claim it computed: over every symmetric instance on n
     cities with distances from 1 to w that satisfies the triangle inequality,
     the worst ratio this heuristic produced was this, on this instance. Four
     cities and distances up to 3 is 482 metric instances; five cities and the
     same range is 23352, which is a second of a frozen tab, so the cap is
     four and the page says so. */
  function cpWorstTourRatio(n, maxw, cap) {
    cap = cap === undefined ? 4 : cap;
    oracleCap('cpWorstTourRatio', n, cap);
    var pairs = [], i, j;
    for (i = 0; i < n; i += 1) for (j = i + 1; j < n; j += 1) pairs.push([i, j]);
    var D = [];
    for (i = 0; i < n; i += 1) { D.push([]); for (j = 0; j < n; j += 1) D[i].push(0); }
    var best = null, bestD = null, metricCount = 0, total = 0;
    (function go(k) {
      if (k === pairs.length) {
        total += 1;
        for (var a = 0; a < n; a += 1) for (var b = 0; b < n; b += 1) for (var c = 0; c < n; c += 1) {
          if (D[a][b] > D[a][c] + D[c][b]) return;
        }
        metricCount += 1;
        var run = mstTour(D);
        if (best === null || Rcmp(run.result.ratio, best) > 0) {
          best = run.result.ratio;
          bestD = D.map(function (row) { return row.slice(); });
        }
        return;
      }
      for (var w = 1; w <= maxw; w += 1) {
        D[pairs[k][0]][pairs[k][1]] = w;
        D[pairs[k][1]][pairs[k][0]] = w;
        go(k + 1);
      }
    })(0);
    return { n: n, maxWeight: maxw, instances: total, metric: metricCount,
             worst: best === null ? R(0n, 1n) : best, D: bestD };
  }
  /* A distance matrix as the reader would have typed it. */
  function cpDistanceText(D) {
    var out = [], i, j;
    for (i = 0; i < D.length; i += 1) {
      for (j = i + 1; j < D.length; j += 1) out.push((i + 1) + '-' + (j + 1) + ' ' + D[i][j]);
    }
    return out.join(', ');
  }

  /* ------------------------------------------------------ the epsilon sweep

     The FPTAS's promise and its realised loss, over a range of epsilons. The
     promise falls as epsilon falls and the table grows; both are computed, so
     the trade is two columns of numbers rather than a sentence about
     asymptotics. */
  function cpEpsilonSweep(items, W, denominators) {
    return denominators.map(function (d) {
      var eps = R(1n, BigInt(d));
      var run = fptasScale(items, W, eps);
      return { denominator: d, eps: eps, value: run.result.value, optimum: run.result.optimum,
               loss: run.result.loss, promised: run.result.promised,
               within: run.result.withinPromise, cells: run.result.cells,
               ratio: run.result.optimum
                 ? R(BigInt(run.result.value), BigInt(run.result.optimum)) : R(0n, 1n) };
    });
  }
  /* The unscaled value table, for the column the sweep is compared against:
     the FPTAS is only interesting if the table it builds is smaller than the
     exact one, and that is a number. */
  function cpExactCells(items) {
    return items.reduce(function (t, it) { return t + it.v; }, 0) + 1;
  }

  /* -------------------------------------------- the parameterised sweep

     2^k * n against 2^n, both computed, over the k the slider covers. The
     point of parameterising is that the first is small when k is and the
     second never is, and two columns of integers say that better than a
     complexity class does. */
  function cpFptSweep(G, kMax) {
    var rows = [], k;
    for (k = 0; k <= kMax; k += 1) {
      var run = fptVertexCover(G, k);
      rows.push({ k: k, exists: run.result.exists, size: run.result.size,
                  nodes: run.counts.nodes || 0, treeBound: run.result.treeBound,
                  work: run.result.work, bruteWork: run.result.bruteWork,
                  optimum: run.result.optimum, correct: run.result.correct,
                  withinTree: (run.counts.nodes || 0) <= run.result.treeBound });
    }
    return rows;
  }

  /* -------------------------------------------------------- set cover extras

     `greedySetCover` prices each element and reports the total; what is added
     here is the per-step accounting the page prints, and the H_k column that
     makes the logarithm visible: the k-th element to be covered is charged at
     most 1/(n - k + 1), and those add to H_n. */
  function cpChargeRows(run, universe, optimum) {
    var order = [], seen = {};
    (run.trace || []).forEach(function (step) {
      step.fresh.forEach(function (e) {
        if (seen[e]) return;
        seen[e] = true;
        order.push({ element: e, step: step.at + 1, set: step.set, charge: step.charge,
                     fresh: step.fresh.length });
      });
    });
    var opt = optimum === undefined ? 1 : Math.max(1, optimum);
    var rows = order.map(function (row, i) {
      /* the k-th element to be covered is charged at most OPT/(n - k + 1),
         because some set in an optimal cover still holds at least
         (elements left)/OPT of them, and the greedy step took the largest.
         Those allowances add to OPT * H_n, which is the bound. */
      var allowed = R(BigInt(opt), BigInt(Math.max(1, universe.length - i)));
      return { element: row.element, step: row.step, set: row.set, charge: row.charge,
               fresh: row.fresh, allowed: allowed,
               withinAllowed: Rcmp(row.charge, allowed) <= 0 };
    });
    return { rows: rows, uncovered: universe.filter(function (e) { return !seen[e]; }),
             everyChargeAllowed: rows.every(function (r) { return r.withinAllowed; }) };
  }
"""


# ---------------------------------------------------------------------------
# One core per mode. COPING_JS depends on more of the shared engine than any
# other block on this path, so what a mode adds is what its own algorithms
# reach for and nothing else.
# ---------------------------------------------------------------------------

_BASE_JS = (RATIONAL_JS + RFIXED_JS + COUNT_JS + DIGRAPH_JS + ORACLE_JS + COPING_JS
            + CPKIT_JS)
_KNAPSACK_JS = (RATIONAL_JS + RFIXED_JS + COUNT_JS + DIGRAPH_JS + ORACLE_JS + RCEIL_JS
                + GREEDY_JS + COPING_JS + CPKIT_JS)
_TOUR_JS = (RATIONAL_JS + RFIXED_JS + COUNT_JS + DIGRAPH_JS + ORACLE_JS + ALGO_JS
            + GRAPHKIT_JS + COPING_JS + CPKIT_JS)
_COVER_JS = (RATIONAL_JS + RFIXED_JS + COUNT_JS + DIGRAPH_JS + ORACLE_JS + HARMONIC_JS
             + COPING_JS + CPKIT_JS)


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the other Algorithms kits use.
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


def _text(cid, label, value, placeholder=None):
    """A text box whose value ships in the markup.

    Nothing this kit's grammars use needs escaping in an attribute: an item is
    `3:5`, an edge is `1-2`, a distance is `1-2 7` and a set is `1 2 3`, and
    none of them carries a `>` or a quote. flowkit fills its box from the
    script because a flow arc does carry a `>`, which a value attribute cannot
    hold without an entity that scripts/labcheck.js does not decode.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(value), _attr(placeholder or value))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


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
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
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
        "coping: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries. Spelled once so no mode can quietly drop
# the half that makes a ratio mean anything.
_BOTH_HALVES = (
    "  /* An approximation ratio is two numbers and this page computes both. The\n"
    "     algorithm runs on the instance on screen; the OPTIMUM is found by an\n"
    "     exhaustive search, at a size the panel states and refuses above. The\n"
    "     ratio printed is the first divided by the second, exactly, and it sits\n"
    "     beside the ratio that was PROMISED -- which is a claim about every\n"
    "     instance and is proved against a LOWER BOUND rather than against the\n"
    "     optimum nobody can compute at scale. The ladder shows all four numbers\n"
    "     on one axis, because the chain lower bound <= optimum <= answer <=\n"
    "     promise x lower bound IS the proof, and each of its links is a\n"
    "     comparison the reader can make for themselves. */\n"
)


# ---------------------------------------------------------------------------
# branchbound -- the bound costs nothing in correctness and buys the tree
# ---------------------------------------------------------------------------

_BB_PRESETS = [
    {
        "id": "five",
        "label": "five items, capacity 10 — the bound cuts the tree by two thirds",
        "items": "3:5, 4:6, 5:8, 2:3, 6:9", "cap": "10",
        "note": "fourteen nodes with the fractional bound against forty-four without it, and the "
                "same answer",
    },
    {
        "id": "tight",
        "label": "eight items whose weights nearly fill the sack",
        "items": "7:12, 8:14, 9:15, 6:10, 5:8, 4:7, 3:5, 2:3", "cap": "20",
        "note": "the relaxation is close to the integer answer here, so almost every branch is "
                "cut",
        },
    {
        "id": "useless",
        "label": "every item the same density — the bound stops helping",
        "items": "2:4, 3:6, 4:8, 5:10, 6:12, 7:14", "cap": "13",
        "note": "the fractional optimum equals the sum of the best prefix and tells the search "
                "almost nothing, which is what a weak bound looks like",
    },
    {
        "id": "small",
        "label": "four items — small enough to read the whole tree",
        "items": "2:3, 3:4, 4:5, 5:6", "cap": "7",
        "note": "sixteen leaves, and every pruning decision fits in the table",
    },
    {
        "id": "gap",
        "label": "one heavy prize and a lot of filler",
        "items": "9:30, 1:2, 1:2, 1:2, 1:2, 1:2, 1:2", "cap": "9",
        "note": "the fractional relaxation takes nine tenths of the prize and the integer answer "
                "cannot, so the bound is loose exactly where it matters",
    },
]


def _branchbound(cfg):
    chosen = _chosen(_BB_PRESETS, cfg)
    markup = (
        _toolbar(
            "Branch and bound: what the bound buys, in nodes",
            "the fractional relaxation is an upper bound on any completion, so a branch below the best so far can be cut",
            [("cyan", "with the fractional bound"), ("purple", "without it"),
             ("red", "the whole tree, 2 to the n")],
        )
        + _stage(_svg("bbPlot", "0 0 520 200",
                      "Nodes expanded with the bound, without it, and the size of the whole "
                      "search tree.")
                 + _svg("bbLadder", "0 0 520 160",
                        "The answer and the optimum on one axis."))
        + _table("bbTrace")
        + _table("bbCheck")
        + _banner("bbStatus")
    )
    controls = (
        _select("bbPreset", "Worked example", _options(_BB_PRESETS), chosen["id"])
        + _text("bbItems", "Items, as weight:value", chosen["items"])
        + _range("bbCap", "Capacity of the sack", 1, 40, chosen["cap"])
        + _select("bbBound", "The bound",
                  [("on", "prune with the fractional relaxation"),
                   ("off", "no bound: expand everything")], "on")
        + _range("bbStep", "Step through the nodes", 1, 60, 1)
        + _kpis([("Items and capacity", "bbSize"),
                 ("Value this search found", "bbValue"),
                 ("The optimum, by exhaustive search", "bbOpt"),
                 ("They agree", "bbCorrect"),
                 ("Nodes with the bound", "bbWith"),
                 ("Nodes without it", "bbWithout"),
                 ("The whole tree", "bbFull"),
                 ("Branches pruned", "bbPruned")])
        + _hint(
            "bbHint",
            "An item is <span class=\"tt\">3:5</span> &mdash; weight 3, value 5. At each node the "
            "search has taken some prefix of the items and has a capacity left; the FRACTIONAL "
            "knapsack on the items that remain is an upper bound on anything the branch can still "
            "reach, because allowing fractions can only help. If that bound is no better than the "
            "best answer already found, the branch cannot contain a better one and is cut. The "
            "bound is the greedy algorithm from the previous course, used unchanged.",
        )
    )
    script = _KNAPSACK_JS + _BOTH_HALVES + _presets_js(
        "BBP", _BB_PRESETS, ["items", "cap", "note"]) + r"""
  var presetIn = document.getElementById('bbPreset'), itemsIn = document.getElementById('bbItems');
  var capIn = document.getElementById('bbCap'), capOut = document.getElementById('bbCapOut');
  var boundIn = document.getElementById('bbBound');
  var stepIn = document.getElementById('bbStep'), stepOut = document.getElementById('bbStepOut');
  var plot = document.getElementById('bbPlot'), ladder = document.getElementById('bbLadder');
  var traceT = document.getElementById('bbTrace'), checkT = document.getElementById('bbCheck');
  var status = document.getElementById('bbStatus');
  var KPIS = ['bbSize', 'bbValue', 'bbOpt', 'bbCorrect', 'bbWith', 'bbWithout', 'bbFull', 'bbPruned'];
  var MAXROWS = 14;

  function blank(why) {
    plot.innerHTML = ''; ladder.innerHTML = ''; traceT.innerHTML = ''; checkT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An item is '
      + '<span class="tt">3:5</span>: weight, then value.';
  }

  function redraw() {
    var parsed = cpParseItems(itemsIn.value, 12);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items, W = parseInt(capIn.value, 10);
    capOut.textContent = String(W);
    var withBound, without, exact;
    try {
      withBound = branchBound(items, W, true);
      without = branchBound(items, W, false);
      exact = knapsackBrute(items, W);
    } catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    var run = boundIn.value === 'on' ? withBound : without;
    stepIn.max = Math.max(1, run.trace.length);
    var at = Math.max(1, Math.min(run.trace.length, parseInt(stepIn.value, 10))) - 1;
    stepOut.textContent = (at + 1) + ' of ' + run.trace.length;

    plot.innerHTML = cpBarsSvg([
      { label: 'with the bound', value: withBound.counts.nodes || 0, colour: 'var(--cyan)' },
      { label: 'without it', value: without.counts.nodes || 0, colour: 'var(--purple)' },
      { label: 'the whole tree', value: withBound.result.full, colour: 'var(--red)' }
    ]);
    ladder.innerHTML = cpLadderSvg([
      { label: 'this search', value: run.result.value, colour: 'var(--cyan)',
        text: String(run.result.value) },
      { label: 'the optimum', value: exact.result.value, colour: 'var(--red)', anchor: true,
        text: String(exact.result.value) + ' — by exhaustive search over '
          + exact.counts.nodes + ' subsets' }
    ], { rowHeight: 44 });

    document.getElementById('bbSize').textContent = items.length + ' items, capacity ' + W;
    document.getElementById('bbValue').textContent = String(run.result.value);
    document.getElementById('bbOpt').textContent = exact.result.value + ' — from '
      + exact.counts.nodes + ' subsets';
    document.getElementById('bbCorrect').textContent =
      (withBound.result.correct && without.result.correct)
        ? 'yes, with the bound and without it'
        : 'NO — one of the two searches is wrong';
    document.getElementById('bbWith').textContent = String(withBound.counts.nodes || 0);
    document.getElementById('bbWithout').textContent = String(without.counts.nodes || 0);
    document.getElementById('bbFull').textContent = String(withBound.result.full);
    document.getElementById('bbPruned').textContent = withBound.result.pruned
      + ' branches cut with the bound, ' + without.result.pruned + ' without';

    var head = '<thead><tr><th>node</th><th>depth</th><th>value so far</th>'
      + '<th>bound on any completion</th><th>what happened</th></tr></thead><tbody>';
    var body = '';
    var lo = Math.max(0, Math.min(at - 6, run.trace.length - MAXROWS));
    run.trace.slice(Math.max(0, lo), Math.max(0, lo) + MAXROWS).forEach(function (st) {
      var cut = st.bound !== null && Rcmp(st.bound, R(BigInt(run.result.value), 1n)) <= 0;
      body += '<tr' + (st.at === at ? ' class="on"' : '') + '><td>' + (st.at + 1) + '</td>'
        + '<td>' + st.depth + '</td><td class="tt">' + st.value + '</td>'
        + '<td class="tt">' + (st.bound === null ? 'not computed — the bound is off'
            : cpBoth(st.bound, 3)) + '</td>'
        + '<td class="' + (st.bound === null ? 'tone-muted">expanded'
            : (cut ? 'tone-cyan">the bound is at or below the best found, so this branch is cut'
                : 'tone-muted">the bound leaves room, so it is expanded')) + '</td></tr>';
    });
    traceT.innerHTML = head + body + '</tbody>';

    checkT.innerHTML = '<thead><tr><th>the claim</th><th>what was computed</th><th>verdict</th>'
      + '</tr></thead><tbody>'
      + '<tr><td>the bounded search finds the optimum</td><td>' + withBound.result.value
      + ' against ' + exact.result.value + ' from an exhaustive search over '
      + exact.counts.nodes + ' subsets</td><td class="'
      + (withBound.result.correct ? 'tone-green">agrees' : 'tone-red">DISAGREES') + '</td></tr>'
      + '<tr><td>so does the unbounded one — pruning is not a heuristic</td><td>'
      + without.result.value + ' against ' + exact.result.value + '</td><td class="'
      + (without.result.correct ? 'tone-green">agrees' : 'tone-red">DISAGREES') + '</td></tr>'
      + '<tr><td>the two searches give the same answer</td><td>' + withBound.result.value
      + ' and ' + without.result.value + '</td><td class="'
      + (withBound.result.value === without.result.value ? 'tone-green">identical'
          : 'tone-red">DIFFERENT') + '</td></tr>'
      + '<tr><td>and the bound is an upper bound at every node</td>'
      + '<td>the fractional relaxation is at least the integral optimum of the same subproblem, '
      + 'because fractions are allowed and integers are a special case</td>'
      + '<td class="tone-cyan">that is why cutting is safe, and it is the only reason</td></tr>'
      + '<tr><td>nodes: with, without, and the whole tree</td><td>'
      + (withBound.counts.nodes || 0) + ', ' + (without.counts.nodes || 0) + ', '
      + withBound.result.full + '</td>'
      + '<td class="' + ((withBound.counts.nodes || 0) <= (without.counts.nodes || 0)
          ? 'tone-green">the bound never costs nodes here'
          : 'tone-amber">the bound cost nodes on this instance, which it can: computing it is '
            + 'work too') + '</td></tr>'
      + '<tr><td>what is still exponential</td><td>the whole tree is 2^' + items.length + ' = '
      + withBound.result.full + '</td>'
      + '<td class="tone-amber">pruning shrinks the tree on THIS instance and changes no '
      + 'worst case; an instance where the bound is useless is one preset away</td></tr></tbody>';

    var saved = (without.counts.nodes || 0) - (withBound.counts.nodes || 0);
    status.innerHTML = '<strong>' + (withBound.counts.nodes || 0) + ' nodes with the bound, '
      + (without.counts.nodes || 0) + ' without it, ' + withBound.result.full
      + ' in the whole tree — and all three searches give ' + exact.result.value + '.</strong> '
      + 'That last part is the point and it is checked rather than assumed: branch and bound is an '
      + 'EXACT algorithm, and the bound changes how much of the tree is visited and nothing else. '
      + 'The answer is compared against an exhaustive search over all ' + exact.counts.nodes
      + ' subsets, written from the definition and sharing no code with the search. '
      + (saved > 0
          ? 'The bound saved ' + saved + ' ' + cpPlural(saved, 'node', 'nodes') + ' here — '
          : saved === 0 ? 'The bound saved nothing here — '
            : 'The bound COST ' + (-saved) + ' nodes here — ')
      + 'and the bound it uses is the fractional knapsack, the greedy algorithm from the previous '
      + 'course, running unchanged. A relaxation is useful exactly when it is easy and tight, and '
      + 'this one is both. '
      + 'What has not changed is the worst case: the tree still has ' + withBound.result.full
      + ' leaves and a bound that never cuts leaves them all. The "every item the same density" '
      + 'preset is that instance, and it is the reason a node count is evidence about one input '
      + 'rather than a bound on all of them.';
  }

  function apply() {
    var p = BBP[presetIn.value];
    if (!p) return;
    itemsIn.value = p.items; capIn.value = p.cap; stepIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  itemsIn.addEventListener('input', redraw);
  capIn.addEventListener('input', redraw);
  boundIn.addEventListener('change', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Branch and bound: what the bound buys, in nodes",
        subtitle="The fractional relaxation is an upper bound on any completion, so a branch that cannot beat the best found is cut — and the answer is still exactly the optimum",
        markup=markup,
        controls=controls,
        panel_title="Switch the bound off and watch the node count, not the answer, change",
        panel_intro=(
            "Both searches run on every redraw and both are compared against an exhaustive search "
            "over every subset. Pruning is not a heuristic: it must leave the answer alone, and "
            "the only way to know it did is to compute the optimum a third way."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# vertexcover -- the 2-approximation, and the worst graph of its size, found
# ---------------------------------------------------------------------------

_VC_PRESETS = [
    {
        "id": "matching",
        "label": "a perfect matching — the ratio is exactly 2",
        "spec": "1-2, 3-4, 5-6",
        "note": "every matched edge needs one endpoint in the cover and the algorithm takes both",
    },
    {
        "id": "star",
        "label": "a star — the hub alone covers everything",
        "spec": "1-2, 1-3, 1-4, 1-5",
        "note": "the matching finds one edge, the cover takes both its ends, and the optimum is "
                "the hub alone",
    },
    {
        "id": "cycle5",
        "label": "a five-cycle — the ratio lands strictly between 1 and 2",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-1",
        "note": "a maximal matching of two edges gives a cover of four against an optimum of "
                "three, so the realised ratio is 4/3",
    },
    {
        "id": "cycle6",
        "label": "a six-cycle — three matched edges, and the ratio is 2 again",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-6, 6-1",
        "note": "an even cycle lets the greedy matching take every other edge, so the cover is "
                "the whole graph against an optimum of three",
    },
    {
        "id": "path5",
        "label": "a path on five vertices",
        "spec": "1-2, 2-3, 3-4, 4-5",
        "note": "the greedy matching takes the first and third edges, and the optimum takes two "
                "interior vertices",
    },
    {
        "id": "triangles",
        "label": "two triangles — the matching can only take one edge from each",
        "spec": "1-2, 2-3, 3-1, 4-5, 5-6, 6-4",
        "note": "a triangle needs two vertices covered and the algorithm takes exactly two, so "
                "the ratio here is 1",
    },
]


def _vertexcover(cfg):
    chosen = _chosen(_VC_PRESETS, cfg)
    markup = (
        _toolbar(
            "Vertex cover in two: a matching is the lower bound",
            "every matched edge needs an endpoint, so the matching is below the optimum and its endpoints are above it",
            [("cyan", "in the cover the algorithm built"), ("purple", "a matched edge"),
             ("green", "the true optimum"), ("red", "the promise, twice the matching")],
        )
        + _stage(_svg("vcPlot", "0 0 460 300",
                      "The graph, with the matched edges heavy and the cover's vertices filled.")
                 + _svg("vcLadder", "0 0 520 180",
                        "The matching, the optimum, the cover and twice the matching, on one "
                        "axis."))
        + _table("vcChain")
        + _table("vcWorst")
        + _banner("vcStatus")
    )
    controls = (
        _select("vcPreset", "Worked example", _options(_VC_PRESETS), chosen["id"])
        + _text("vcSpec", "Edges, as u-v", chosen["spec"])
        + _range("vcAll", "Search every graph on this many vertices", 3, 5, 4)
        + _kpis([("Vertices and edges", "vcSize"),
                 ("Matching found, the lower bound", "vcMatch"),
                 ("Cover the algorithm built", "vcCover"),
                 ("The optimum, by exhaustive search", "vcOpt"),
                 ("The ratio it realised", "vcRatio"),
                 ("Within the promised 2", "vcWithin"),
                 ("Worst ratio over every graph of that size", "vcWorstRatio"),
                 ("A graph that attains it", "vcWorstGraph")])
        + _hint(
            "vcHint",
            "Take edges one at a time, skipping any that touches a vertex already used: that is a "
            "<em>maximal</em> matching. Every one of its edges needs at least one endpoint in any "
            "cover, and its edges share no vertex, so the optimum is at least the matching size. "
            "Taking <em>both</em> ends of every matched edge covers the whole graph, because an "
            "uncovered edge would have been addable to the matching. So the cover is at most twice "
            "a number that is at most the optimum &mdash; and neither half of that sentence "
            "mentions the optimum itself.",
        )
    )
    script = _BASE_JS + _BOTH_HALVES + _presets_js("VCP", _VC_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('vcPreset'), specIn = document.getElementById('vcSpec');
  var allIn = document.getElementById('vcAll'), allOut = document.getElementById('vcAllOut');
  var plot = document.getElementById('vcPlot'), ladder = document.getElementById('vcLadder');
  var chainT = document.getElementById('vcChain'), worstT = document.getElementById('vcWorst');
  var status = document.getElementById('vcStatus');
  var KPIS = ['vcSize', 'vcMatch', 'vcCover', 'vcOpt', 'vcRatio', 'vcWithin', 'vcWorstRatio',
              'vcWorstGraph'];

  function blank(why) {
    plot.innerHTML = ''; ladder.innerHTML = ''; chainT.innerHTML = ''; worstT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>.';
  }

  function redraw() {
    var parsed = cpParseGraph(specIn.value, 8);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var run, worst;
    try {
      run = maximalMatching(G);
      worst = cpWorstRatio(parseInt(allIn.value, 10));
    } catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    allOut.textContent = allIn.value + ' vertices, ' + worst.graphs + ' graphs';
    var res = run.result;

    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 230, cy: 150, radius: 108 }),
                                label: 'none', highlight: res.matching,
                                colours: (function () {
                                  var out = new Array(n).fill(-1);
                                  res.cover.forEach(function (v) { out[v] = 0; });
                                  return out;
                                })() });
    ladder.innerHTML = cpLadderSvg([
      { label: 'the matching', value: res.lowerBound, colour: 'var(--purple)',
        text: res.lowerBound + ' — a lower bound the algorithm can see' },
      { label: 'the optimum', value: res.optimum, colour: 'var(--green)', anchor: true,
        text: res.optimum + ' — by exhaustive search' },
      { label: 'the cover built', value: res.size, colour: 'var(--cyan)',
        text: res.size + ' — the endpoints of the matching' },
      { label: 'twice the matching', value: 2 * res.lowerBound, colour: 'var(--red)', faint: true,
        text: String(2 * res.lowerBound) + ' — the promise' }
    ]);

    var ratio = cpRatio(res.size, res.optimum);
    document.getElementById('vcSize').textContent = n + ' vertices, ' + G.arcs.length + ' edges';
    document.getElementById('vcMatch').textContent = res.lowerBound + ' '
      + cpPlural(res.lowerBound, 'edge', 'edges');
    document.getElementById('vcCover').textContent = res.size + ' — ' + cpVertexText(res.cover);
    document.getElementById('vcOpt').textContent = res.optimum + ' vertices';
    document.getElementById('vcRatio').textContent = ratio === null ? 'no edges to cover'
      : cpBoth(ratio, 4) + ', against the promised 2';
    document.getElementById('vcWithin').textContent = res.withinTwo ? 'yes' : 'NO — a defect';
    document.getElementById('vcWorstRatio').textContent = Rtext(worst.worst) + ' over '
      + worst.withEdges + ' graphs with an edge';
    document.getElementById('vcWorstGraph').textContent = cpEdgeText(worst.densest);

    chainT.innerHTML = '<thead><tr><th>the link in the chain</th><th>value</th>'
      + '<th>why it holds</th></tr></thead><tbody>'
      + '<tr><td>matching ≤ optimum</td><td class="tt">' + res.lowerBound + ' ≤ ' + res.optimum
      + '</td><td class="' + (res.lowerBound <= res.optimum ? 'tone-green' : 'tone-red')
      + '">the matched edges share no vertex, so a cover needs a different vertex for each</td></tr>'
      + '<tr><td>optimum ≤ cover</td><td class="tt">' + res.optimum + ' ≤ ' + res.size
      + '</td><td class="' + (res.optimum <= res.size ? 'tone-green' : 'tone-red')
      + '">the optimum is the smallest cover and this is a cover — checked edge by edge</td></tr>'
      + '<tr><td>cover = 2 × matching</td><td class="tt">' + res.size + ' = 2 × '
      + res.lowerBound + '</td><td class="'
      + (res.size === 2 * res.lowerBound ? 'tone-green' : 'tone-red')
      + '">both endpoints of each matched edge, and nothing else</td></tr>'
      + '<tr><td>so cover ≤ 2 × optimum</td><td class="tt">' + res.size + ' ≤ '
      + (2 * res.optimum) + '</td><td class="' + (res.withinTwo ? 'tone-green' : 'tone-red')
      + '">the three lines above, in order — and the optimum appears only here</td></tr>'
      + '<tr><td>the ratio actually realised</td><td class="tt">'
      + (ratio === null ? '—' : Rtext(ratio)) + '</td>'
      + '<td class="tone-cyan">' + res.size + ' divided by ' + res.optimum
      + ', both computed on this graph</td></tr>'
      + '<tr><td>is the cover a cover at all</td><td class="tt">' + cpVertexText(res.cover)
      + '</td><td class="tone-green">every edge has an endpoint in it, checked against the '
      + 'edge list rather than inferred from the construction</td></tr></tbody>';

    worstT.innerHTML = '<thead><tr><th>the claim, and what it is about</th><th>computed over</th>'
      + '<th>result</th></tr></thead><tbody>'
      + '<tr><td>the ratio on the graph on screen</td><td>one graph</td>'
      + '<td class="tone-cyan">' + (ratio === null ? '—' : Rtext(ratio)) + '</td></tr>'
      + '<tr><td>the worst ratio over EVERY graph on ' + worst.n + ' vertices</td>'
      + '<td>' + worst.graphs + ' graphs, ' + worst.withEdges + ' of them with an edge, each '
      + 'solved exactly</td><td class="tone-red">' + Rtext(worst.worst) + '</td></tr>'
      + '<tr><td>the smallest graph attaining it</td><td>the first in edge order</td>'
      + '<td class="tt">' + cpEdgeText(worst.graph) + '</td></tr>'
      + '<tr><td>the largest graph attaining it</td><td>' + worst.atWorst
      + ' graphs attain the worst ratio</td><td class="tt">' + cpEdgeText(worst.densest)
      + '</td></tr>'
      + '<tr><td>and the promise</td><td>every graph, of every size</td>'
      + '<td class="tone-purple">2 — which the search above did not beat, and cannot</td></tr>'
      + '<tr><td>whose worst case this is</td><td>—</td>'
      + '<td class="tone-amber">the matching is GREEDY in edge order, so this is the worst case '
      + 'of this implementation on graphs of this size; a different edge order is a different '
      + 'matching and the bound of 2 covers all of them</td></tr></tbody>';

    status.innerHTML = '<strong>Matching ' + res.lowerBound + ', optimum ' + res.optimum
      + ', cover ' + res.size + ' — a ratio of '
      + (ratio === null ? 'nothing, since there is nothing to cover' : Rtext(ratio))
      + ' against a promise of 2.</strong> '
      + 'The ratio is printed with the optimum it is a ratio to, and that optimum came from an '
      + 'exhaustive search over the subsets of the vertices. Without it the number above would be '
      + 'a fraction with an invented denominator. '
      + 'But the PROOF does not use the optimum, and that is the idea worth taking away. The '
      + 'matching is a lower bound the algorithm can compute: its edges share no vertex, so any '
      + 'cover needs a distinct vertex for each of them. The cover is exactly twice that number '
      + 'by construction. So the answer is within 2 of something that is itself below the '
      + 'optimum, and the optimum never had to be known. '
      + 'Over every one of the ' + worst.graphs + ' graphs on ' + worst.n
      + ' vertices — each solved exactly — the worst ratio this algorithm produced was '
      + Rtext(worst.worst) + ', attained by ' + worst.atWorst + ' of them, the largest being '
      + cpEdgeText(worst.densest) + '. '
      + 'That is what "tight" means, computed rather than quoted: there is no room in the '
      + 'promise, and no graph of this size does worse.';
  }

  function apply() {
    var p = VCP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  allIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Vertex cover in two: a matching is the lower bound",
        subtitle="The matched edges share no vertex, so the optimum is above the matching; the cover is twice it — and the optimum appears only in the last line",
        markup=markup,
        controls=controls,
        panel_title="Edit the graph, then search every graph of a size for the worst ratio",
        panel_intro=(
            "The optimum is an exhaustive search over the subsets, computed separately from the "
            "algorithm, so the realised ratio has a real denominator. The second table goes "
            "further and enumerates <em>every</em> graph on the number of vertices you choose, "
            "which turns &ldquo;the bound is tight&rdquo; from a word into an instance."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# tsp -- the triangle inequality is a hypothesis, and the reader can break it
# ---------------------------------------------------------------------------

_TS_PRESETS = [
    {
        "id": "worst4",
        "label": "the worst metric instance on four cities — ratio 10/7",
        "spec": "1-2 2, 1-3 1, 1-4 3, 2-3 3, 2-4 2, 3-4 2",
        "note": "found by enumerating every metric instance on four cities with distances up to "
                "3, not chosen by hand",
    },
    {
        "id": "worst5",
        "label": "the worst metric instance on five cities — ratio 8/5",
        "spec": "1-2 1, 1-3 1, 1-4 2, 1-5 1, 2-3 2, 2-4 1, 2-5 1, 3-4 1, 3-5 2, 4-5 1",
        "note": "still well inside the promise of 2, which is the usual state of an approximation "
                "guarantee",
    },
    {
        "id": "easy",
        "label": "a metric instance the heuristic gets exactly right",
        "spec": "1-2 3, 1-3 4, 1-4 5, 2-3 3, 2-4 4, 3-4 3",
        "note": "a ratio of 1, which is common and is why one instance proves nothing about the "
                "worst case",
    },
    {
        "id": "broken",
        "label": "one distance raised until the triangle inequality breaks",
        "spec": "1-2 50, 1-3 1, 1-4 1, 2-3 1, 2-4 1, 3-4 1",
        "note": "the shortcut step assumed a direct hop is no longer than going round, and here "
                "it is fifty times longer",
    },
    {
        "id": "grid",
        "label": "five cities on a line",
        "spec": "1-2 1, 1-3 2, 1-4 3, 1-5 4, 2-3 1, 2-4 2, 2-5 3, 3-4 1, 3-5 2, 4-5 1",
        "note": "distances that come from positions are always metric, which is why the "
                "hypothesis is usually free",
    },
]


def _tsp(cfg):
    chosen = _chosen(_TS_PRESETS, cfg)
    markup = (
        _toolbar(
            "The metric tour in two: an MST, doubled, shortcut",
            "the shortcut step is where the triangle inequality is used, and the mode lets you take it away",
            [("cyan", "an edge of the minimum spanning tree"),
             ("purple", "the tour after shortcutting"), ("green", "the optimum"),
             ("red", "the promise, twice the tree")],
        )
        + _stage(_svg("tsPlot", "0 0 460 300",
                      "The cities, with the minimum spanning tree drawn heavy and the tour "
                      "over it.")
                 + _svg("tsLadder", "0 0 520 180",
                        "The tree, the optimum, the tour and twice the tree, on one axis."))
        + _table("tsChain")
        + _table("tsWorst")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Worked example", _options(_TS_PRESETS), chosen["id"])
        + _text("tsSpec", "Distances, as u-v followed by the distance — every pair", chosen["spec"])
        + _range("tsBreak", "Multiply the distance 1-2 by", 1, 40, 1)
        + _range("tsAll", "Search every metric instance on this many cities", 3, 4, 4)
        + _kpis([("Cities, and whether it is metric", "tsSize"),
                 ("The minimum spanning tree", "tsMst"),
                 ("The tour after shortcutting", "tsTour"),
                 ("The optimum, by exhaustive search", "tsOpt"),
                 ("The ratio it realised", "tsRatio"),
                 ("Within the promised 2", "tsWithin"),
                 ("Worst ratio over every metric instance", "tsWorstRatio"),
                 ("An instance that attains it", "tsWorstCase")])
        + _hint(
            "tsHint",
            "A distance is <span class=\"tt\">1-2 7</span>, and every pair must be given. Build a "
            "minimum spanning tree, walk it so every edge is used twice, then shortcut past any "
            "city already visited. The walk costs exactly twice the tree, the tree is below the "
            "optimum because deleting one edge of an optimal tour leaves a spanning path, and "
            "shortcutting does not make the walk longer &mdash; <em>provided</em> a direct hop is "
            "no longer than going round. That proviso is the triangle inequality, and the slider "
            "removes it.",
        )
    )
    script = _TOUR_JS + _BOTH_HALVES + _presets_js("TSP3", _TS_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('tsPreset'), specIn = document.getElementById('tsSpec');
  var breakIn = document.getElementById('tsBreak'), breakOut = document.getElementById('tsBreakOut');
  var allIn = document.getElementById('tsAll'), allOut = document.getElementById('tsAllOut');
  var plot = document.getElementById('tsPlot'), ladder = document.getElementById('tsLadder');
  var chainT = document.getElementById('tsChain'), worstT = document.getElementById('tsWorst');
  var status = document.getElementById('tsStatus');
  var KPIS = ['tsSize', 'tsMst', 'tsTour', 'tsOpt', 'tsRatio', 'tsWithin', 'tsWorstRatio',
              'tsWorstCase'];

  function blank(why) {
    plot.innerHTML = ''; ladder.innerHTML = ''; chainT.innerHTML = ''; worstT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A distance is '
      + '<span class="tt">1-2 7</span>, and every pair is needed.';
  }

  function redraw() {
    var parsed = cpParseDistances(specIn.value, 7);
    if (parsed.bad) { blank(parsed.bad); return; }
    var n = parsed.n, factor = parseInt(breakIn.value, 10);
    breakOut.textContent = '× ' + factor;
    var D = parsed.D.map(function (row) { return row.slice(); });
    D[0][1] *= factor; D[1][0] *= factor;

    var run, worst;
    try {
      run = mstTour(D);
      worst = cpWorstTourRatio(parseInt(allIn.value, 10), 3);
    } catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    allOut.textContent = allIn.value + ' cities, ' + worst.metric + ' metric instances';
    var res = run.result;

    /* the complete graph, so the tree and the tour can both be drawn on it */
    var G = dgNew(n, false), i, j;
    for (i = 0; i < n; i += 1) for (j = i + 1; j < n; j += 1) dgAdd(G, i, j, D[i][j], 0);
    var tourEdges = [];
    res.tour.forEach(function (v, k) {
      var w = res.tour[(k + 1) % res.tour.length], id = dgFind(G, v, w);
      if (id >= 0) tourEdges.push(id);
    });
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 230, cy: 150, radius: 108 }),
                                label: 'w', highlight: res.mst.concat(tourEdges) });
    ladder.innerHTML = cpLadderSvg([
      { label: 'the spanning tree', value: res.mstWeight, colour: 'var(--purple)',
        text: res.mstWeight + ' — a lower bound the algorithm can see' },
      { label: 'the optimum', value: res.optimum, colour: 'var(--green)', anchor: true,
        text: res.optimum + ' — by exhaustive search over the tours' },
      { label: 'the tour built', value: res.length, colour: 'var(--cyan)',
        text: res.length + ' — the tree, doubled and shortcut' },
      { label: 'twice the tree', value: 2 * res.mstWeight, colour: 'var(--red)', faint: true,
        text: String(2 * res.mstWeight) + ' — the promise' }
    ]);

    var ratio = cpRatio(res.length, res.optimum);
    document.getElementById('tsSize').textContent = n + ' cities — '
      + (res.metric ? 'metric' : 'NOT metric');
    document.getElementById('tsMst').textContent = res.mstWeight + ' over ' + res.mst.length
      + ' edges';
    document.getElementById('tsTour').textContent = res.length + ' — '
      + res.tour.map(function (v) { return v + 1; }).join('-');
    document.getElementById('tsOpt').textContent = String(res.optimum);
    document.getElementById('tsRatio').textContent = ratio === null ? '—'
      : cpBoth(ratio, 4) + ', against the promised 2';
    document.getElementById('tsWithin').textContent = res.withinTwo
      ? 'yes' + (res.metric ? '' : ' — but the hypothesis does not hold, so nothing promised it')
      : 'NO' + (res.metric ? ' — that would be a defect'
          : ', and the instance is not metric, so the theorem never applied');
    document.getElementById('tsWorstRatio').textContent = Rtext(worst.worst) + ' over '
      + worst.metric + ' metric instances';
    document.getElementById('tsWorstCase').textContent = worst.D
      ? cpDistanceText(worst.D) : 'none found';

    chainT.innerHTML = '<thead><tr><th>the link in the chain</th><th>value</th>'
      + '<th>why it holds, and what it needs</th></tr></thead><tbody>'
      + '<tr><td>tree ≤ optimum</td><td class="tt">' + res.mstWeight + ' ≤ ' + res.optimum
      + '</td><td class="' + (res.mstWeight <= res.optimum ? 'tone-green' : 'tone-red')
      + '">deleting one edge of an optimal tour leaves a spanning path, which is a spanning tree '
      + '— no hypothesis needed</td></tr>'
      + '<tr><td>the doubled walk = 2 × tree</td><td class="tt">' + (2 * res.mstWeight)
      + '</td><td class="tone-green">every tree edge is traversed exactly twice — no hypothesis '
      + 'needed</td></tr>'
      + '<tr><td>the shortcut tour ≤ the doubled walk</td><td class="tt">' + res.length + ' ≤ '
      + (2 * res.mstWeight) + '</td><td class="'
      + (res.length <= 2 * res.mstWeight ? 'tone-green' : 'tone-red')
      + '">THIS is the step that needs the triangle inequality: skipping a visited city replaces '
      + 'two hops by one, and only the inequality says that is no longer</td></tr>'
      + '<tr><td>so tour ≤ 2 × optimum</td><td class="tt">' + res.length + ' ≤ '
      + (2 * res.optimum) + '</td><td class="' + (res.withinTwo ? 'tone-green' : 'tone-red')
      + '">the three lines above — and it fails exactly when the third one does</td></tr>'
      + '<tr><td>is the instance metric</td><td class="tt">'
      + (res.metric ? 'yes' : 'no') + '</td><td class="'
      + (res.metric ? 'tone-green">every triple i, j, k satisfies d(i,j) ≤ d(i,k) + d(k,j), '
          + 'checked over all ' + (n * n * n) + ' of them'
          : 'tone-red">some triple has d(i,j) > d(i,k) + d(k,j), so the theorem says nothing '
            + 'about this instance and the bound is free to fail') + '</td></tr>'
      + '<tr><td>the ratio actually realised</td><td class="tt">'
      + (ratio === null ? '—' : Rtext(ratio)) + '</td>'
      + '<td class="tone-cyan">' + res.length + ' divided by ' + res.optimum
      + ', the optimum found by trying every tour</td></tr></tbody>';

    worstT.innerHTML = '<thead><tr><th>the claim, and what it is about</th><th>computed over</th>'
      + '<th>result</th></tr></thead><tbody>'
      + '<tr><td>the ratio on the instance on screen</td><td>one instance</td>'
      + '<td class="tone-cyan">' + (ratio === null ? '—' : Rtext(ratio)) + '</td></tr>'
      + '<tr><td>the worst ratio over every METRIC instance on ' + worst.n
      + ' cities with distances 1 to ' + worst.maxWeight + '</td>'
      + '<td>' + worst.instances + ' instances, ' + worst.metric
      + ' of them metric, each solved exactly</td>'
      + '<td class="tone-red">' + Rtext(worst.worst) + '</td></tr>'
      + '<tr><td>an instance attaining it</td><td>—</td><td class="tt">'
      + (worst.D ? cpDistanceText(worst.D) : '—') + '</td></tr>'
      + '<tr><td>the promise</td><td>every metric instance, of every size</td>'
      + '<td class="tone-purple">2</td></tr>'
      + '<tr><td>why the search does not reach 2</td><td>' + worst.metric
      + ' instances at ' + worst.n + ' cities</td>'
      + '<td class="tone-amber">the bound is approached as the number of cities grows, not at '
      + 'four of them; a small exhaustive search bounds the ratio BELOW the promise and that is '
      + 'not evidence against the promise</td></tr>'
      + '<tr><td>and without the triangle inequality</td><td>the instance on screen, with the '
      + '1-2 distance multiplied by ' + factor + '</td>'
      + '<td class="' + (res.metric ? 'tone-muted">still metric — raise the multiplier'
          : 'tone-red">not metric, ratio ' + (ratio === null ? '—' : Rtext(ratio))
            + ', and no constant ratio is possible at all: a reduction from Hamilton circuit '
            + 'makes any of them NP-hard') + '</td></tr></tbody>';

    status.innerHTML = '<strong>Tree ' + res.mstWeight + ', optimum ' + res.optimum + ', tour '
      + res.length + ' — a ratio of ' + (ratio === null ? '—' : Rtext(ratio))
      + ' against a promise of 2.</strong> '
      + 'The optimum came from trying every tour, so the denominator is real. '
      + 'The proof, though, never mentions it: the spanning tree is below the optimum because an '
      + 'optimal tour minus one edge is a spanning tree, the doubled walk is exactly twice the '
      + 'tree, and shortcutting does not lengthen it. '
      + (res.metric
          ? 'This instance is metric — every one of the ' + (n * n * n) + ' triples was checked — '
            + 'so all three links hold and the answer is inside the promise. '
          : '<span class="tone-red">This instance is NOT metric.</span> Some triple has a direct '
            + 'hop longer than the way round, so the shortcut step has nothing behind it, and the '
            + 'ratio here is ' + (ratio === null ? '—' : Rtext(ratio))
            + '. That is not a bug in the algorithm; it is the hypothesis doing work, and the '
            + 'work becomes visible only when it is removed. ')
      + 'Over every metric instance on ' + worst.n + ' cities with distances up to '
      + worst.maxWeight + ' — ' + worst.metric + ' of them, each solved exactly — the worst '
      + 'ratio this heuristic produced was ' + Rtext(worst.worst)
      + '. That is a bound on all instances of that size and it is well under 2, which is the '
      + 'usual relationship between a guarantee and what happens: the guarantee is approached as '
      + 'the instance grows, and a search at four cities cannot see it.';
  }

  function apply() {
    var p = TSP3[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; breakIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  breakIn.addEventListener('input', redraw);
  allIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The metric tour in two: an MST, doubled, shortcut",
        subtitle="The tree is below the optimum and the walk is twice the tree — and the shortcut step, the only one that needs the triangle inequality, is the one the slider breaks",
        markup=markup,
        controls=controls,
        panel_title="Raise one distance until the instance stops being metric",
        panel_intro=(
            "Each link of the chain is a separate row, with what it needs written beside it, "
            "because only one of the three uses the triangle inequality. The optimum is an "
            "exhaustive search over the tours, and a second search covers every metric instance "
            "of a size so the worst case is a number rather than an adjective."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# setcover -- every element priced, and the charges add to the answer
# ---------------------------------------------------------------------------

_SC_PRESETS = [
    {
        "id": "trap",
        "label": "seven elements where greedy takes three and two suffice",
        "sets": "3 4 5 6; 1 2 3; 4 5 6 7",
        "note": "the biggest set is taken first and then neither of the two that cover everything "
                "is whole any more",
    },
    {
        "id": "trap10",
        "label": "ten elements, the same trap one size up",
        "sets": "4 5 6 7 8 9; 1 2 3 4 5; 6 7 8 9 10; 1 2 3; 10",
        "note": "greedy takes the six first and then needs two more, against an optimum of two",
    },
    {
        "id": "clean",
        "label": "a partition — greedy has no choice to get wrong",
        "sets": "1 2 3 4; 5 6 7 8",
        "note": "the sets are disjoint and cover everything, so every cover is the whole family "
                "and the ratio is 1",
    },
    {
        "id": "overlap",
        "label": "heavy overlap — several optimal covers",
        "sets": "1 2 3; 2 3 4; 3 4 5; 4 5 1; 5 1 2",
        "note": "any two of these cover all five elements, and greedy finds one of them",
    },
    {
        "id": "singletons",
        "label": "one big set and the singletons under it",
        "sets": "1 2 3 4 5; 1; 2; 3; 4; 5",
        "note": "greedy takes the big set and stops, which is the optimum — a reminder that the "
                "logarithm is a worst case and not a description",
    },
]


def _setcover(cfg):
    chosen = _chosen(_SC_PRESETS, cfg)
    markup = (
        _toolbar(
            "Greedy set cover: every element pays, and the prices add up",
            "a set that covers k new elements charges each of them 1/k, so the charges are the answer",
            [("cyan", "the charge an element paid"),
             ("purple", "the most it was allowed to pay"),
             ("green", "the optimum"), ("red", "the bound, H times the optimum")],
        )
        + _stage(_svg("scPlot", "0 0 520 200",
                      "One bar per element: what it was charged, against the most the analysis "
                      "allows it to be charged.")
                 + _svg("scLadder", "0 0 520 180",
                        "The optimum, the greedy answer and the bound, on one axis."))
        + _table("scTrace")
        + _table("scChain")
        + _banner("scStatus")
    )
    controls = (
        _select("scPreset", "Worked example", _options(_SC_PRESETS), chosen["id"])
        + _text("scSets", "Sets, elements by spaces and sets by a semicolon", chosen["sets"])
        + _range("scStep", "Step through the greedy choices", 1, 10, 1)
        + _kpis([("Universe and sets", "scSize"),
                 ("Sets greedy took", "scGreedy"),
                 ("The optimum, by exhaustive search", "scOpt"),
                 ("The ratio it realised", "scRatio"),
                 ("H, over the universe", "scHn"),
                 ("The bound, H times the optimum", "scBound"),
                 ("Within the bound", "scWithin"),
                 ("The charges add to the answer", "scCharges")])
        + _hint(
            "scHint",
            "A set is <span class=\"tt\">1 2 3</span>, and sets are separated by a semicolon. The "
            "universe is whatever appears. At each step take the set covering the most "
            "<em>new</em> elements; if it covers <span class=\"tt\">k</span> of them, charge each "
            "one <span class=\"tt\">1/k</span>. The charges add to the number of sets taken, "
            "because each set costs 1 and hands its whole cost out. The analysis then bounds each "
            "charge separately, and the bound on the sum is <span class=\"tt\">H</span> times the "
            "optimum.",
        )
    )
    script = _COVER_JS + _BOTH_HALVES + _presets_js("SCP", _SC_PRESETS, ["sets", "note"]) + r"""
  var presetIn = document.getElementById('scPreset'), setsIn = document.getElementById('scSets');
  var stepIn = document.getElementById('scStep'), stepOut = document.getElementById('scStepOut');
  var plot = document.getElementById('scPlot'), ladder = document.getElementById('scLadder');
  var traceT = document.getElementById('scTrace'), chainT = document.getElementById('scChain');
  var status = document.getElementById('scStatus');
  var KPIS = ['scSize', 'scGreedy', 'scOpt', 'scRatio', 'scHn', 'scBound', 'scWithin', 'scCharges'];

  function blank(why) {
    plot.innerHTML = ''; ladder.innerHTML = ''; traceT.innerHTML = ''; chainT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A set is '
      + '<span class="tt">1 2 3</span>, and sets are separated by a semicolon.';
  }

  function redraw() {
    var parsed = cpParseSets(setsIn.value, 10);
    if (parsed.bad) { blank(parsed.bad); return; }
    var sets = parsed.sets, universe = parsed.universe;
    var run;
    try { run = greedySetCover(sets, universe); }
    catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    var res = run.result;
    if (res.optimum === null) { blank('these sets do not cover their own universe'); return; }
    var charges = cpChargeRows(run, universe, res.optimum);
    stepIn.max = Math.max(1, run.trace.length);
    var at = Math.max(1, Math.min(run.trace.length, parseInt(stepIn.value, 10))) - 1;
    stepOut.textContent = (at + 1) + ' of ' + run.trace.length;

    plot.innerHTML = cpBarsSvg(charges.rows.map(function (r) {
      return { label: String(r.element), value: Rnum(r.charge), colour: 'var(--cyan)',
               text: Rtext(r.charge) };
    }), { maxY: charges.rows.reduce(function (m, r) {
            return Math.max(m, Rnum(r.charge), Rnum(r.allowed)); }, 0.001) });
    ladder.innerHTML = cpLadderSvg([
      { label: 'the optimum', value: res.optimum, colour: 'var(--green)', anchor: true,
        text: res.optimum + ' sets — by exhaustive search over the subfamilies' },
      { label: 'greedy', value: res.size, colour: 'var(--cyan)',
        text: res.size + ' sets — and the charges add to ' + Rtext(res.chargeTotal) },
      { label: 'the bound', value: Rnum(res.bound), colour: 'var(--red)', faint: true,
        text: Rtext(res.bound) + ' = ' + Rfixed(res.bound, 3) + ' — H × the optimum' }
    ], { rowHeight: 44 });

    var ratio = cpRatio(res.size, res.optimum);
    document.getElementById('scSize').textContent = universe.length + ' elements, ' + sets.length
      + ' sets';
    document.getElementById('scGreedy').textContent = res.size + ' — '
      + res.chosen.map(function (i) { return 'S' + (i + 1); }).join(', ');
    document.getElementById('scOpt').textContent = res.optimum + ' sets';
    document.getElementById('scRatio').textContent = ratio === null ? '—' : cpBoth(ratio, 4);
    document.getElementById('scHn').textContent = Rtext(res.Hn) + ' = ' + Rfixed(res.Hn, 4);
    document.getElementById('scBound').textContent = Rtext(res.bound) + ' = '
      + Rfixed(res.bound, 4);
    document.getElementById('scWithin').textContent = res.withinBound ? 'yes' : 'NO — a defect';
    document.getElementById('scCharges').textContent = Rtext(res.chargeTotal) + ' against '
      + res.size + (res.chargesSumToSize ? ' — equal' : ' — NOT EQUAL, which is a defect');

    var head = '<thead><tr><th>step</th><th>set taken</th><th>new elements it covered</th>'
      + '<th>each charged</th><th>elements left after</th></tr></thead><tbody>';
    var body = '', left = universe.length;
    run.trace.forEach(function (st) {
      left -= st.fresh.length;
      body += '<tr' + (st.at === at ? ' class="on"' : '') + '><td>' + (st.at + 1) + '</td>'
        + '<td class="tt">S' + (st.set + 1) + ' = ' + cpSetText(sets[st.set]) + '</td>'
        + '<td class="tt">' + cpSetText(st.fresh) + ' — ' + st.fresh.length + ' of them</td>'
        + '<td class="tt tone-cyan">' + Rtext(st.charge) + '</td>'
        + '<td>' + left + '</td></tr>';
    });
    body += '<tr><td colspan="3"><strong>the charges add to</strong></td>'
      + '<td class="tt ' + (res.chargesSumToSize ? 'tone-green' : 'tone-red') + '"><strong>'
      + Rtext(res.chargeTotal) + '</strong></td>'
      + '<td><strong>' + res.size + ' sets</strong></td></tr>';
    traceT.innerHTML = head + body + '</tbody>';

    chainT.innerHTML = '<thead><tr><th>the link in the chain</th><th>value</th>'
      + '<th>why it holds</th></tr></thead><tbody>'
      + '<tr><td>the charges add to the number of sets</td><td class="tt">'
      + Rtext(res.chargeTotal) + ' = ' + res.size + '</td><td class="'
      + (res.chargesSumToSize ? 'tone-green' : 'tone-red')
      + '">each set costs 1 and hands its whole cost to the elements it newly covered — by '
      + 'construction, and checked</td></tr>'
      + '<tr><td>the k-th element covered is charged at most OPT/(n − k + 1)</td>'
      + '<td class="tt">' + charges.rows.length + ' charges checked</td><td class="'
      + (charges.everyChargeAllowed ? 'tone-green">every one is inside its allowance'
          : 'tone-red">one is NOT') + ', because some set in an optimal cover still holds at '
      + 'least a 1/OPT share of what is left, and greedy took the largest</td></tr>'
      + '<tr><td>so greedy ≤ OPT × H</td><td class="tt">' + res.size + ' ≤ ' + Rtext(res.bound)
      + '</td><td class="' + (res.withinBound ? 'tone-green' : 'tone-red')
      + '">the allowances add to OPT × (1/n + 1/(n−1) + … + 1) = OPT × H</td></tr>'
      + '<tr><td>H over ' + universe.length + ' elements, exactly</td><td class="tt">'
      + Rtext(res.Hn) + '</td><td class="tone-cyan">a sum of fractions, not a logarithm: ln '
      + universe.length + ' is not a rational and this is</td></tr>'
      + '<tr><td>the ratio actually realised</td><td class="tt">'
      + (ratio === null ? '—' : Rtext(ratio)) + '</td>'
      + '<td class="tone-cyan">' + res.size + ' divided by ' + res.optimum
      + ', the optimum found over every subfamily of the ' + sets.length + ' sets</td></tr>'
      + '<tr><td>and is what greedy returned a cover at all</td>'
      + '<td class="tt">' + charges.uncovered.length + ' elements left uncovered</td>'
      + '<td class="' + (charges.uncovered.length === 0 ? 'tone-green">yes, every element is in '
          + 'one of the chosen sets' : 'tone-red">NO — ' + cpSetText(charges.uncovered)
          + ' were never covered') + '</td></tr></tbody>';

    status.innerHTML = '<strong>Greedy took ' + res.size + ' '
      + cpPlural(res.size, 'set', 'sets') + ', the optimum is ' + res.optimum
      + ', the ratio is ' + (ratio === null ? '—' : Rtext(ratio)) + ', and the bound is H × OPT = '
      + Rtext(res.bound) + '.</strong> '
      + 'The optimum came from an exhaustive search over every subfamily of the ' + sets.length
      + ' sets, so the ratio has a denominator that was computed rather than assumed. '
      + 'The charges are what make the bound provable. Each set costs 1 and gives that cost to '
      + 'the elements it newly covered, so the charges add to '
      + Rtext(res.chargeTotal) + ' — exactly the number of sets, checked above rather than '
      + 'asserted. Then each charge is bounded on its own: when k elements are still uncovered, '
      + 'some set of an optimal cover holds at least k/OPT of them, greedy took a set at least '
      + 'that large, so the elements it covered paid at most OPT/k each. Adding those allowances '
      + 'gives OPT × H. '
      + 'H over ' + universe.length + ' elements is ' + Rtext(res.Hn)
      + ' here, and it is a sum of fractions rather than a logarithm: this library never prints '
      + 'ln n where the exact harmonic number will do. '
      + 'Notice how loose the bound is on this instance — ' + res.size + ' against '
      + Rfixed(res.bound, 3) + '. A bound is a claim about every instance, and on almost all of '
      + 'them it has room to spare. The instances that use it up are built, not found.';
  }

  function apply() {
    var p = SCP[presetIn.value];
    if (!p) return;
    setsIn.value = p.sets; stepIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  setsIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Greedy set cover: every element pays, and the prices add up",
        subtitle="A set covering k new elements charges each of them 1/k — the charges add to the answer, and each one has its own allowance",
        markup=markup,
        controls=controls,
        panel_title="Step through the choices and watch the charges fall",
        panel_intro=(
            "The charge identity is checked rather than shown: the fractions must add to the "
            "number of sets taken, exactly, and a mismatch would mean the accounting behind the "
            "bound is wrong. H is the exact harmonic number, a sum of fractions and not a "
            "logarithm, and the optimum is an exhaustive search over the subfamilies."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# fptas -- epsilon is a rational, so the promise is a fraction and is checked
# ---------------------------------------------------------------------------

_FP_PRESETS = [
    {
        "id": "big",
        "label": "six items with large values — the scaling shrinks the table",
        "items": "3:520, 4:610, 5:805, 2:311, 6:902, 4:455", "cap": "12",
        "note": "the exact table has 3604 cells and a tenth of a percent of the optimum buys a "
                "much smaller one",
    },
    {
        "id": "small",
        "label": "five small values — the scaling makes the table BIGGER",
        "items": "3:5, 4:6, 5:8, 2:3, 6:9", "cap": "10",
        "note": "an FPTAS is an asymptotic device and on a tiny instance it costs more than it "
                "saves, which the cell counts show",
    },
    {
        "id": "spread",
        "label": "one dominant value among small ones",
        "items": "5:900, 1:11, 2:19, 3:27, 4:38, 2:14", "cap": "9",
        "note": "the scale factor is set by the LARGEST value, so a single big item coarsens "
                "everything",
    },
    {
        "id": "equal",
        "label": "every value the same",
        "items": "2:100, 3:100, 4:100, 5:100, 6:100", "cap": "11",
        "note": "scaling cannot distinguish them, so the loss comes entirely from the floor",
    },
    {
        "id": "tight",
        "label": "eight items and a sack that nearly fits them",
        "items": "7:300, 8:355, 9:400, 6:260, 5:220, 4:180, 3:130, 2:90", "cap": "22",
        "note": "the exact table is large and the scaled one is a fraction of it",
    },
]


def _fptas(cfg):
    chosen = _chosen(_FP_PRESETS, cfg)
    markup = (
        _toolbar(
            "The knapsack FPTAS: pay for the accuracy you want",
            "scale the values down, solve the scaled instance exactly, and lose at most ε times the optimum",
            [("cyan", "the value the FPTAS returned"), ("green", "the optimum"),
             ("purple", "the loss it promised"), ("red", "the loss it took")],
        )
        + _stage(_svg("fpPlot", "0 0 520 200",
                      "One bar per epsilon: the cells the scaled table needed, against the cells "
                      "the exact table needs.")
                 + _svg("fpLadder", "0 0 520 180",
                        "The value returned, the optimum and the promised loss, on one axis."))
        + _table("fpItems")
        + _table("fpSweep")
        + _banner("fpStatus")
    )
    controls = (
        _select("fpPreset", "Worked example", _options(_FP_PRESETS), chosen["id"])
        + _text("fpItems2", "Items, as weight:value", chosen["items"])
        + _range("fpCap", "Capacity of the sack", 1, 40, chosen["cap"])
        + _range("fpEps", "Accuracy: ε is one over this", 1, 60, 10)
        + _kpis([("Items and capacity", "fpSize"),
                 ("Epsilon, as a fraction", "fpEpsOut2"),
                 ("The scale factor K", "fpK"),
                 ("Value the FPTAS returned", "fpValue"),
                 ("The optimum, by exhaustive search", "fpOpt"),
                 ("Loss taken, against loss promised", "fpLoss"),
                 ("Inside the promise", "fpWithin"),
                 ("Cells scaled, against cells exact", "fpCells")])
        + _hint(
            "fpHint",
            "Divide every value by <span class=\"tt\">K = ε · vmax / n</span> and round down, "
            "then solve the scaled instance exactly with a table indexed by VALUE. Rounding down "
            "loses at most <span class=\"tt\">K</span> per item and at most "
            "<span class=\"tt\">n · K = ε · vmax</span> in total, and "
            "<span class=\"tt\">vmax</span> is at most the optimum &mdash; so the loss is at most "
            "<span class=\"tt\">ε</span> times the optimum. Every one of those quantities is an "
            "exact fraction here, so the promise is a number and the loss is compared against it.",
        )
    )
    script = _KNAPSACK_JS + _BOTH_HALVES + _presets_js(
        "FPP", _FP_PRESETS, ["items", "cap", "note"]) + r"""
  var presetIn = document.getElementById('fpPreset'), itemsIn = document.getElementById('fpItems2');
  var capIn = document.getElementById('fpCap'), capOut = document.getElementById('fpCapOut');
  var epsIn = document.getElementById('fpEps'), epsOut = document.getElementById('fpEpsOut');
  var plot = document.getElementById('fpPlot'), ladder = document.getElementById('fpLadder');
  var itemsT = document.getElementById('fpItems'), sweepT = document.getElementById('fpSweep');
  var status = document.getElementById('fpStatus');
  var KPIS = ['fpSize', 'fpEpsOut2', 'fpK', 'fpValue', 'fpOpt', 'fpLoss', 'fpWithin', 'fpCells'];
  var SWEEP = [1, 2, 4, 8, 16, 32];

  function blank(why) {
    plot.innerHTML = ''; ladder.innerHTML = ''; itemsT.innerHTML = ''; sweepT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An item is '
      + '<span class="tt">3:520</span>: weight, then value.';
  }

  function redraw() {
    var parsed = cpParseItems(itemsIn.value, 10);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items, W = parseInt(capIn.value, 10);
    var denom = parseInt(epsIn.value, 10);
    capOut.textContent = String(W);
    epsOut.textContent = '1/' + denom;
    var eps = R(1n, BigInt(denom));
    var run, sweep, exactCells;
    try {
      run = fptasScale(items, W, eps);
      sweep = cpEpsilonSweep(items, W, SWEEP.concat(SWEEP.indexOf(denom) === -1 ? [denom] : [])
        .sort(function (a, b) { return a - b; }));
      exactCells = cpExactCells(items);
    } catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    var res = run.result;

    plot.innerHTML = cpBarsSvg(sweep.map(function (r) {
      return { label: '1/' + r.denominator, value: r.cells,
               colour: r.denominator === denom ? 'var(--cyan)' : 'var(--purple)',
               text: String(r.cells) };
    }), { rule: { value: exactCells, label: 'the exact table, ' + exactCells + ' cells',
                  colour: 'var(--red)' } });
    ladder.innerHTML = cpLadderSvg([
      { label: 'the FPTAS answer', value: res.value, colour: 'var(--cyan)',
        text: String(res.value) },
      { label: 'the optimum', value: res.optimum, colour: 'var(--green)', anchor: true,
        text: res.optimum + ' — by exhaustive search over the subsets' },
      { label: 'loss taken', value: res.loss, colour: 'var(--red)', text: String(res.loss) },
      { label: 'loss promised', value: Rnum(res.promised), colour: 'var(--purple)', faint: true,
        text: Rtext(res.promised) + ' = ' + Rfixed(res.promised, 3) + ' — ε × the optimum' }
    ]);

    var ratio = cpRatio(res.value, res.optimum);
    document.getElementById('fpSize').textContent = items.length + ' items, capacity ' + W;
    document.getElementById('fpEpsOut2').textContent = Rtext(eps) + ' = ' + Rfixed(eps, 5);
    document.getElementById('fpK').textContent = Rtext(res.K) + ' = ' + Rfixed(res.K, 4);
    document.getElementById('fpValue').textContent = res.value + ' — ratio '
      + (ratio === null ? '—' : Rtext(ratio));
    document.getElementById('fpOpt').textContent = String(res.optimum);
    document.getElementById('fpLoss').textContent = res.loss + ' against ' + Rtext(res.promised);
    document.getElementById('fpWithin').textContent = res.withinPromise ? 'yes' : 'NO — a defect';
    document.getElementById('fpCells').textContent = res.cells + ' against ' + exactCells
      + (res.cells < exactCells ? ' — smaller' : ' — BIGGER, at this size');

    var chosen = {};
    res.chosen.forEach(function (i) { chosen[i] = true; });
    var head = '<thead><tr><th>item</th><th>weight</th><th>value</th>'
      + '<th>value ÷ K, rounded down</th><th>taken by the scaled table</th>'
      + '<th>what it is worth really</th></tr></thead><tbody>';
    var body = '';
    items.forEach(function (it, i) {
      body += '<tr' + (chosen[i] ? ' class="on"' : '') + '><td>' + (i + 1) + '</td>'
        + '<td class="tt">' + it.w + '</td><td class="tt">' + it.v + '</td>'
        + '<td class="tt tone-purple">' + res.scaled[i].v + '</td>'
        + '<td class="' + (chosen[i] ? 'tone-cyan">yes' : 'tone-muted">no') + '</td>'
        + '<td class="tt">' + (chosen[i] ? it.v : '—') + '</td></tr>';
    });
    var takenWeight = res.chosen.reduce(function (t, i) { return t + items[i].w; }, 0);
    body += '<tr><td colspan="4"><strong>the set the scaled table chose, priced at the ORIGINAL '
      + 'values</strong></td><td class="tt"><strong>' + takenWeight + ' ≤ ' + W
      + '</strong></td><td class="tt tone-cyan"><strong>' + res.value + '</strong></td></tr>';
    itemsT.innerHTML = head + body + '</tbody>';

    sweepT.innerHTML = '<thead><tr><th>ε</th><th>value returned</th><th>optimum</th>'
      + '<th>loss</th><th>loss promised</th><th>inside it</th><th>cells</th></tr></thead><tbody>'
      + sweep.map(function (r) {
          return '<tr' + (r.denominator === denom ? ' class="on"' : '') + '><td class="tt">1/'
            + r.denominator + '</td><td class="tt">' + r.value + '</td>'
            + '<td class="tt tone-green">' + r.optimum + '</td>'
            + '<td class="tt tone-red">' + r.loss + '</td>'
            + '<td class="tt tone-purple">' + Rfixed(r.promised, 3) + '</td>'
            + '<td class="' + (r.within ? 'tone-green">yes' : 'tone-red">NO') + '</td>'
            + '<td class="' + (r.cells < exactCells ? 'tone-cyan' : 'tone-amber') + '">'
            + r.cells + '</td></tr>';
        }).join('')
      + '<tr><td class="tt">exact</td><td class="tt">' + res.optimum + '</td>'
      + '<td class="tt tone-green">' + res.optimum + '</td><td class="tt">0</td>'
      + '<td class="tone-muted">—</td><td class="tone-green">by definition</td>'
      + '<td class="tone-red">' + exactCells + '</td></tr>'
      + '<tr><td colspan="7" class="small-copy">The optimum column is the same number every time '
      + 'because it is the answer, found by exhaustive search over all ' + Math.pow(2, items.length)
      + ' subsets, and it does not depend on ε. Only the first column moves.</td></tr></tbody>';

    status.innerHTML = '<strong>ε = ' + Rtext(eps) + ', K = ' + Rtext(res.K)
      + ', the FPTAS returned ' + res.value + ', the optimum is ' + res.optimum
      + ', the loss is ' + res.loss + ' and the promise was ' + Rtext(res.promised)
      + '.</strong> '
      + 'Every one of those is exact. ε is a fraction, so K is a fraction, so the promise is a '
      + 'fraction, and &ldquo;inside the promise&rdquo; is a comparison of two fractions rather '
      + 'than of two '
      + 'decimals that happen to round the right way. '
      + 'The important line is the one about what was measured: the scaled table chose a SET, and '
      + 'the value reported is that set priced at the ORIGINAL values, not the scaled total. '
      + 'Reporting the scaled number instead is the standard way an FPTAS lab ends up claiming an '
      + 'accuracy it did not achieve, and the item table above shows both columns so the two '
      + 'cannot be confused. '
      + 'The ratio realised is ' + (ratio === null ? '—' : Rtext(ratio)) + ', against the '
      + 'guaranteed 1 − ε = ' + Rtext(Rsub(R(1n, 1n), eps)) + '. '
      + (res.cells < exactCells
          ? 'And the table shrank: ' + res.cells + ' cells against ' + exactCells + '. '
          : 'And the table did NOT shrink here — ' + res.cells + ' cells against ' + exactCells
            + '. That is not a bug. The scaled table has about n²/ε cells however small the '
            + 'values are, so on a small instance an FPTAS costs more than it saves; it is an '
            + 'asymptotic device and the cell counts say so. ')
      + 'What is bought and what is paid are both on the page, which is the only way to see that '
      + 'the trade is a trade.';
  }

  function apply() {
    var p = FPP[presetIn.value];
    if (!p) return;
    itemsIn.value = p.items; capIn.value = p.cap;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  itemsIn.addEventListener('input', redraw);
  capIn.addEventListener('input', redraw);
  epsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The knapsack FPTAS: pay for the accuracy you want",
        subtitle="Scale the values down, solve the scaled instance exactly, and lose at most ε × the optimum — with ε a fraction, so the promise is a number",
        markup=markup,
        controls=controls,
        panel_title="Move ε and watch the table and the loss move in opposite directions",
        panel_intro=(
            "The value reported is the set the scaled table chose, priced at the <em>original</em> "
            "values &mdash; which is what the guarantee is about, and what an FPTAS lab gets wrong "
            "when it reports the scaled total instead. Both columns are in the item table."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# fpt -- a bounded search tree: 2^k times n, against 2^n
# ---------------------------------------------------------------------------

_FT_PRESETS = [
    {
        "id": "cycle6",
        "label": "a six-cycle — a cover of 3 exists and 2 does not",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-6, 6-1", "k": "3",
        "note": "the search tree has at most 2^3 branches and the graph has 2^6 subsets",
    },
    {
        "id": "star8",
        "label": "a star on eight vertices — k = 1 settles it",
        "spec": "1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 1-8", "k": "1",
        "note": "the hub covers everything, so a budget of one is enough however many leaves "
                "there are",
    },
    {
        "id": "matching",
        "label": "a perfect matching — k must reach the number of edges",
        "spec": "1-2, 3-4, 5-6, 7-8", "k": "4",
        "note": "every edge needs its own vertex, so the parameter is as large as it can be and "
                "the method buys nothing",
    },
    {
        "id": "triangles",
        "label": "two triangles — a cover of four",
        "spec": "1-2, 2-3, 3-1, 4-5, 5-6, 6-4", "k": "4",
        "note": "two vertices per triangle, and the branching finds it in a handful of nodes",
    },
    {
        "id": "path7",
        "label": "a path on seven vertices",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-6, 6-7", "k": "3",
        "note": "three interior vertices cover a path of six edges, and the tree never gets "
                "deeper than three",
    },
]


def _fpt(cfg):
    chosen = _chosen(_FT_PRESETS, cfg)
    markup = (
        _toolbar(
            "Parameterised: a search tree of depth k, whatever n is",
            "one end of an uncovered edge must be in the cover, so branching on it costs 2 per unit of budget",
            [("cyan", "in the cover found"), ("purple", "the branching tree, 2 to the k"),
             ("red", "every subset, 2 to the n"), ("green", "the true optimum")],
        )
        + _stage(_svg("ftPlot", "0 0 460 300",
                      "The graph, with the cover the bounded search found filled in.")
                 + _svg("ftBars", "0 0 520 200",
                        "Work as a function of the budget: 2 to the k times n, against 2 to "
                        "the n."))
        + _table("ftTrace")
        + _table("ftSweep")
        + _banner("ftStatus")
    )
    controls = (
        _select("ftPreset", "Worked example", _options(_FT_PRESETS), chosen["id"])
        + _text("ftSpec", "Edges, as u-v", chosen["spec"])
        + _range("ftK", "The budget k", 0, 8, chosen["k"])
        + _range("ftStep", "Step through the branchings", 1, 40, 1)
        + _kpis([("Vertices and edges", "ftSize"),
                 ("Is there a cover of size k", "ftExists"),
                 ("The cover it found", "ftCover"),
                 ("The optimum, by exhaustive search", "ftOpt"),
                 ("The answer is right", "ftCorrect"),
                 ("Nodes the search opened", "ftNodes"),
                 ("The tree bound, 2 to the k plus one", "ftTree"),
                 ("2 to the k times n, against 2 to the n", "ftWork")])
        + _hint(
            "ftHint",
            "Find any edge neither of whose ends is covered yet. One of the two must be in the "
            "cover &mdash; there is no third option &mdash; so branch on that, spending one unit "
            "of budget either way. The tree is therefore at most "
            "<span class=\"tt\">2^k</span> deep-branching nodes no matter how large the graph is, "
            "and the size of the graph only enters as the cost of scanning for an uncovered edge. "
            "That is what parameterising buys: the exponential is in <span class=\"tt\">k</span> "
            "and not in <span class=\"tt\">n</span>.",
        )
    )
    script = _BASE_JS + _BOTH_HALVES + _presets_js("FTP", _FT_PRESETS, ["spec", "k", "note"]) + r"""
  var presetIn = document.getElementById('ftPreset'), specIn = document.getElementById('ftSpec');
  var kIn = document.getElementById('ftK'), kOut = document.getElementById('ftKOut');
  var stepIn = document.getElementById('ftStep'), stepOut = document.getElementById('ftStepOut');
  var plot = document.getElementById('ftPlot'), bars = document.getElementById('ftBars');
  var traceT = document.getElementById('ftTrace'), sweepT = document.getElementById('ftSweep');
  var status = document.getElementById('ftStatus');
  var KPIS = ['ftSize', 'ftExists', 'ftCover', 'ftOpt', 'ftCorrect', 'ftNodes', 'ftTree', 'ftWork'];
  var MAXROWS = 14;

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; traceT.innerHTML = ''; sweepT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>.';
  }

  function redraw() {
    var parsed = cpParseGraph(specIn.value, 8);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n, k = parseInt(kIn.value, 10);
    kOut.textContent = String(k);
    var run, sweep;
    try {
      run = fptVertexCover(G, k);
      sweep = cpFptSweep(G, Math.min(6, n));
    } catch (e) { if (!cpIsRefusal(e)) throw e; blank(e.message); return; }
    var res = run.result;
    stepIn.max = Math.max(1, run.trace.length);
    var at = Math.max(1, Math.min(run.trace.length, parseInt(stepIn.value, 10))) - 1;
    stepOut.textContent = run.trace.length ? (at + 1) + ' of ' + run.trace.length : 'nothing to branch on';

    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 230, cy: 150, radius: 108 }),
                                label: 'none',
                                colours: (function () {
                                  var out = new Array(n).fill(-1);
                                  (res.cover || []).forEach(function (v) { out[v] = 0; });
                                  return out;
                                })(),
                                highlight: (function () {
                                  if (!run.trace.length) return [];
                                  var e = run.trace[at].edge, id = dgFind(G, e[0], e[1]);
                                  return id >= 0 ? [id] : [];
                                })() });
    bars.innerHTML = cpBarsSvg(sweep.map(function (r) {
      return { label: 'k = ' + r.k, value: r.work,
               colour: r.k === k ? 'var(--cyan)' : 'var(--purple)', text: String(r.work) };
    }), { maxY: Math.max(res.bruteWork, sweep.reduce(function (m, r) {
            return Math.max(m, r.work); }, 1)),
          rule: { value: res.bruteWork, label: '2 to the n = ' + res.bruteWork,
                  colour: 'var(--red)' } });

    document.getElementById('ftSize').textContent = n + ' vertices, ' + G.arcs.length + ' edges';
    document.getElementById('ftExists').textContent = res.exists ? 'yes' : 'no';
    document.getElementById('ftCover').textContent = res.cover
      ? cpVertexText(res.cover) + ' — ' + res.size + ' vertices' : 'none within the budget';
    document.getElementById('ftOpt').textContent = res.optimum + ' vertices';
    document.getElementById('ftCorrect').textContent = res.correct
      ? 'yes — it says ' + (res.exists ? 'yes' : 'no') + ' and the optimum is ' + res.optimum
      : 'NO — a defect';
    document.getElementById('ftNodes').textContent = String(run.counts.nodes || 0);
    document.getElementById('ftTree').textContent = res.treeBound + ' — '
      + ((run.counts.nodes || 0) <= res.treeBound ? 'not exceeded' : 'EXCEEDED, a defect');
    document.getElementById('ftWork').textContent = res.work + ' against ' + res.bruteWork;

    var head = '<thead><tr><th>node</th><th>budget left</th><th>an uncovered edge</th>'
      + '<th>cover so far</th><th>the branch</th></tr></thead><tbody>';
    var body = '';
    var lo = Math.max(0, Math.min(at - 6, run.trace.length - MAXROWS));
    run.trace.slice(Math.max(0, lo), Math.max(0, lo) + MAXROWS).forEach(function (st) {
      body += '<tr' + (st.at === at ? ' class="on"' : '') + '><td>' + (st.at + 1) + '</td>'
        + '<td class="tt">' + st.budget + '</td>'
        + '<td class="tt">' + (st.edge[0] + 1) + '-' + (st.edge[1] + 1) + '</td>'
        + '<td class="tt">' + cpVertexText(st.cover) + '</td>'
        + '<td class="' + (st.budget === 0 ? 'tone-red">out of budget, this branch stops'
            : 'tone-cyan">take ' + (st.edge[0] + 1) + ', or take ' + (st.edge[1] + 1)) + '</td></tr>';
    });
    if (!run.trace.length) {
      body = '<tr><td colspan="5" class="tone-green">there was never an uncovered edge: the empty '
        + 'set already covers this graph</td></tr>';
    }
    traceT.innerHTML = head + body + '</tbody>';

    sweepT.innerHTML = '<thead><tr><th>budget k</th><th>a cover of size k exists</th>'
      + '<th>the optimum says</th><th>right</th><th>nodes opened</th><th>tree bound</th>'
      + '<th>2^k × n</th><th>2^n</th></tr></thead><tbody>'
      + sweep.map(function (r) {
          return '<tr' + (r.k === k ? ' class="on"' : '') + '><td>' + r.k + '</td>'
            + '<td class="' + (r.exists ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
            + '<td class="tt">optimum ' + r.optimum + (r.optimum <= r.k ? ' ≤ ' : ' > ') + r.k
            + '</td><td class="' + (r.correct ? 'tone-green">yes' : 'tone-red">NO') + '</td>'
            + '<td class="tt">' + r.nodes + '</td>'
            + '<td class="tt ' + (r.withinTree ? 'tone-green' : 'tone-red') + '">' + r.treeBound
            + '</td><td class="tt tone-purple">' + r.work + '</td>'
            + '<td class="tt tone-red">' + r.bruteWork + '</td></tr>';
        }).join('')
      + '<tr><td colspan="8" class="small-copy">The last two columns are the whole idea: the '
      + 'purple one doubles with k and the red one is fixed by n. On a graph of a hundred '
      + 'vertices with a budget of five the first is 3200 and the second has thirty-one '
      + 'digits.</td></tr></tbody>';

    status.innerHTML = '<strong>Budget ' + k + ': ' + (res.exists ? 'a cover of that size exists'
        + ' — ' + cpVertexText(res.cover) : 'no cover of that size exists')
      + ', the optimum is ' + res.optimum + ', and the search opened '
      + (run.counts.nodes || 0) + ' nodes against a tree bound of ' + res.treeBound + '.</strong> '
      + 'The answer is checked against an exhaustive search over the subsets of the vertices, and '
      + 'it ' + (res.correct ? 'agrees' : 'DISAGREES, which is a defect') + '. '
      + 'The branching rule is the whole method and it has no cleverness in it: pick any edge '
      + 'neither of whose ends is covered, and one of the two ends must be in every cover, so '
      + 'branch on which. Each branch spends one unit of budget, so the tree cannot be deeper '
      + 'than k and cannot have more than 2^(k+1) nodes — a bound in k alone, with n nowhere in '
      + 'it. '
      + 'The size of the graph comes back only as the cost of finding an uncovered edge, which is '
      + 'a scan: 2^k × n = ' + res.work + ' here, against 2^n = ' + res.bruteWork
      + ' for trying every subset. '
      + (res.cover && res.size > res.optimum
          ? 'Notice that the cover it returned has ' + res.size + ' vertices and the optimum has '
            + res.optimum + '. That is correct behaviour: the question asked was whether a cover '
            + 'of size at most ' + k + ' exists, and the first one the search reaches answers it. '
            + 'A witness to a decision question is not obliged to be optimal. '
          : '')
      + 'And what this does NOT do is make vertex cover easy. It makes it easy when k is small, '
      + 'which is a statement about the instances you have rather than about the problem — the '
      + 'perfect-matching preset is the case where k has to be as large as it can be and the '
      + 'method buys nothing at all.';
  }

  function apply() {
    var p = FTP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; kIn.value = p.k; stepIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Parameterised: a search tree of depth k, whatever n is",
        subtitle="One end of an uncovered edge must be in the cover, so the tree has 2^k branches and the graph's size enters only as a scan",
        markup=markup,
        controls=controls,
        panel_title="Move the budget and watch the two work columns separate",
        panel_intro=(
            "Every budget from 0 upwards is run, and each answer is checked against an exhaustive "
            "search over the subsets. The last two columns are the point: one doubles with the "
            "budget and the other is fixed by the graph, and they cross where parameterising "
            "stops being worth it."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice.
# ---------------------------------------------------------------------------

_MODES = {
    "branchbound": _branchbound,
    "vertexcover": _vertexcover,
    "tsp": _tsp,
    "setcover": _setcover,
    "fptas": _fptas,
    "fpt": _fpt,
}

MODES = tuple(sorted(_MODES))


def coping_lab(cfg):
    """The intractability course's coping kit. `cfg["mode"]` chooses the lesson."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "coping_lab: unknown mode %r; the six coping modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["coping_lab", "CPKIT_JS", "MODES"]
