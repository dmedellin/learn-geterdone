"""Lab for course 7: graphs and trees."""

from .common import Lab, cfg_literal

# The algorithms the workbench runs, as one block so that scripts/mathcheck.js
# can execute exactly the JavaScript that ships. Everything here is pure: it
# reads N, A and LESSON and touches no element. The DOM code that paints the
# results follows in graph_lab.
#
# Edge weights are a function of the endpoints, w(i, j) = ((7i + 13j) mod 9) + 1,
# so they are deterministic and reproducible: two readers who build the same
# graph get the same minimum spanning tree. A lesson that supplies its own
# example may attach weights to its edges; those apply only while the lesson
# preset is selected, and an edge the reader adds takes the formula weight.
GRAPH_JS = r"""
  var N = 6, A = [], LESSON = null, useLessonWeights = false;

  function blank(n) {
    var M = [];
    for (var i = 0; i < n; i += 1) { var r = []; for (var j = 0; j < n; j += 1) r.push(0); M.push(r); }
    return M;
  }
  function link(M, i, j) { if (i !== j) { M[i][j] = 1; M[j][i] = 1; } }
  function weight(i, j) {
    var a = Math.min(i, j), b = Math.max(i, j);
    if (useLessonWeights && LESSON && LESSON.w[a + '-' + b] !== undefined) return LESSON.w[a + '-' + b];
    return ((7 * a + 13 * b) % 9) + 1;
  }
  /* A lesson's own example: a list of [i, j] or [i, j, w] with 1-based labels. */
  function lessonFrom(list) {
    if (!list || !list.length) return null;
    var w = {}, edges = [];
    list.forEach(function (e) {
      var a = Math.min(e[0], e[1]) - 1, b = Math.max(e[0], e[1]) - 1;
      edges.push([a, b]);
      if (e.length > 2) w[a + '-' + b] = e[2];
    });
    return { edges: edges, w: w };
  }

  var PRESETS = {
    path: function (n) { var M = blank(n); for (var i = 0; i + 1 < n; i += 1) link(M, i, i + 1); return M; },
    cycle: function (n) { var M = blank(n); for (var i = 0; i < n; i += 1) link(M, i, (i + 1) % n); return M; },
    complete: function (n) { var M = blank(n); for (var i = 0; i < n; i += 1) for (var j = i + 1; j < n; j += 1) link(M, i, j); return M; },
    star: function (n) { var M = blank(n); for (var i = 1; i < n; i += 1) link(M, 0, i); return M; },
    bipartite: function (n) {
      var M = blank(n), half = Math.floor(n / 2);
      for (var i = 0; i < half; i += 1) for (var j = half; j < n; j += 1) link(M, i, j);
      return M;
    },
    tree: function (n) { var M = blank(n); for (var i = 1; i < n; i += 1) link(M, i, Math.floor((i - 1) / 2)); return M; },
    petersen: function (n) {
      var M = blank(n);
      for (var i = 0; i + 2 < n && i < 3; i += 1) link(M, i, (i + 1) % 3);
      if (n >= 6) { link(M, 3, 4); link(M, 4, 5); link(M, 5, 3); link(M, 0, 3); }
      return M;
    },
    lesson: function (n) {
      var M = blank(n);
      if (LESSON) LESSON.edges.forEach(function (e) { if (e[0] < n && e[1] < n) link(M, e[0], e[1]); });
      return M;
    },
    empty: function (n) { return blank(n); }
  };

  function edges() {
    var out = [];
    for (var i = 0; i < N; i += 1) for (var j = i + 1; j < N; j += 1) if (A[i][j]) out.push([i, j, weight(i, j)]);
    return out;
  }
  function degree(v) { var d = 0; for (var j = 0; j < N; j += 1) d += A[v][j]; return d; }
  function neighbours(v) { var out = []; for (var j = 0; j < N; j += 1) if (A[v][j]) out.push(j); return out; }

  /* Components of the graph, or of the graph with one vertex deleted. */
  function componentsOf(skip) {
    var seen = new Array(N).fill(false), comps = [];
    if (skip !== undefined && skip >= 0) seen[skip] = true;
    for (var s = 0; s < N; s += 1) {
      if (seen[s]) continue;
      var stack = [s], comp = [];
      seen[s] = true;
      while (stack.length) {
        var v = stack.pop(); comp.push(v);
        neighbours(v).forEach(function (u) { if (!seen[u]) { seen[u] = true; stack.push(u); } });
      }
      comps.push(comp.sort(function (a, b) { return a - b; }));
    }
    return comps;
  }

  /* Bridges and cut vertices, each found the way the lesson defines it:
     remove it and count the components again. */
  function cuts() {
    var base = componentsOf().length, bridges = [], cutVertices = [];
    edges().forEach(function (e) {
      A[e[0]][e[1]] = 0; A[e[1]][e[0]] = 0;
      var after = componentsOf();
      A[e[0]][e[1]] = 1; A[e[1]][e[0]] = 1;
      if (after.length > base) {
        var side = after.filter(function (c) { return c.indexOf(e[0]) !== -1 || c.indexOf(e[1]) !== -1; });
        bridges.push({ edge: [e[0], e[1]], sides: side });
      }
    });
    for (var v = 0; v < N; v += 1) if (componentsOf(v).length > base) cutVertices.push(v);
    return { components: base, bridges: bridges, cutVertices: cutVertices };
  }

  function bfs(start) {
    var dist = new Array(N).fill(-1), parent = new Array(N).fill(-1), order = [];
    dist[start] = 0;
    var queue = [start];
    while (queue.length) {
      var v = queue.shift();
      order.push(v);
      neighbours(v).forEach(function (u) {
        if (dist[u] === -1) { dist[u] = dist[v] + 1; parent[u] = v; queue.push(u); }
      });
    }
    return { dist: dist, parent: parent, order: order };
  }

  function dfs(start) {
    var seen = new Array(N).fill(false), order = [], parent = new Array(N).fill(-1);
    (function visit(v) {
      seen[v] = true; order.push(v);
      neighbours(v).forEach(function (u) { if (!seen[u]) { parent[u] = v; visit(u); } });
    })(start);
    return { order: order, parent: parent };
  }

  /* The three recursive orders and level order, on the tree rooted at
     `root` with children taken in increasing label order. Inorder needs a
     binary tree: a single child counts as the left child, and a vertex with
     three children makes inorder undefined -- which is reported, because it
     is the lesson's point. On a graph with cycles the tree is the depth-first
     spanning tree and the edges it leaves out are counted. */
  function rootedOrders(root) {
    var t = dfs(root), children = [];
    for (var v = 0; v < N; v += 1) children.push([]);
    for (var u = 0; u < N; u += 1) if (t.parent[u] !== -1) children[t.parent[u]].push(u);
    var pre = [], post = [], ino = [], tooMany = -1;
    (function walk(v) {
      pre.push(v);
      if (children[v].length > 2 && tooMany === -1) tooMany = v;
      if (children[v].length) walk(children[v][0]);
      ino.push(v);
      for (var k = 1; k < children[v].length; k += 1) walk(children[v][k]);
      post.push(v);
    })(root);
    var level = [], queue = [root];
    while (queue.length) { var w = queue.shift(); level.push(w); children[w].forEach(function (c) { queue.push(c); }); }
    return { pre: pre, ino: tooMany === -1 ? ino : null, tooMany: tooMany, post: post, level: level,
             reached: t.order.length, treeEdges: t.order.length - 1, parent: t.parent };
  }

  function dijkstra(start) {
    var dist = new Array(N).fill(Infinity), parent = new Array(N).fill(-1), done = new Array(N).fill(false);
    dist[start] = 0;
    for (var it = 0; it < N; it += 1) {
      var best = -1;
      for (var v = 0; v < N; v += 1) if (!done[v] && dist[v] < Infinity && (best === -1 || dist[v] < dist[best])) best = v;
      if (best === -1) break;
      done[best] = true;
      neighbours(best).forEach(function (u) {
        var alt = dist[best] + weight(best, u);
        if (alt < dist[u]) { dist[u] = alt; parent[u] = best; }
      });
    }
    return { dist: dist, parent: parent };
  }

  function twoColour() {
    var colour = new Array(N).fill(-1), conflict = null;
    for (var s = 0; s < N; s += 1) {
      if (colour[s] !== -1) continue;
      colour[s] = 0;
      var queue = [s];
      while (queue.length) {
        var v = queue.shift();
        var nb = neighbours(v);
        for (var k = 0; k < nb.length; k += 1) {
          var u = nb[k];
          if (colour[u] === -1) { colour[u] = 1 - colour[v]; queue.push(u); }
          else if (colour[u] === colour[v] && !conflict) conflict = [v, u];
        }
      }
    }
    return { colour: colour, conflict: conflict };
  }

  function greedyColour() {
    var colour = new Array(N).fill(-1);
    for (var v = 0; v < N; v += 1) {
      var used = {};
      neighbours(v).forEach(function (u) { if (colour[u] !== -1) used[colour[u]] = true; });
      var c = 0;
      while (used[c]) c += 1;
      colour[v] = c;
    }
    return colour;
  }

  /* The clique number by exhaustive search over vertex subsets: n <= 8 means
     at most 255 of them. A K_k inside the graph forces chi >= k. */
  function cliqueNumber() {
    var best = 0, bestSet = [];
    for (var mask = 1; mask < (1 << N); mask += 1) {
      var members = [];
      for (var v = 0; v < N; v += 1) if (mask & (1 << v)) members.push(v);
      if (members.length <= best) continue;
      var ok = true;
      for (var i = 0; ok && i < members.length; i += 1)
        for (var j = i + 1; j < members.length; j += 1) if (!A[members[i]][members[j]]) { ok = false; break; }
      if (ok) { best = members.length; bestSet = members; }
    }
    return { size: best, vertices: bestSet };
  }

  function kruskal() {
    var es = edges().slice().sort(function (a, b) { return a[2] - b[2] || a[0] - b[0] || a[1] - b[1]; });
    var parent = [];
    for (var i = 0; i < N; i += 1) parent.push(i);
    function find(x) { while (parent[x] !== x) { parent[x] = parent[parent[x]]; x = parent[x]; } return x; }
    var chosen = [], total = 0, considered = [];
    es.forEach(function (e) {
      var a = find(e[0]), b = find(e[1]);
      if (a === b) { considered.push([e, false]); return; }
      parent[a] = b;
      chosen.push(e); total += e[2];
      considered.push([e, true]);
    });
    return { chosen: chosen, total: total, considered: considered };
  }

  /* Hamilton by exhaustive search. n is capped at 8, so 8! = 40320 permutations
     is instant -- and the cap is itself the lesson: this is the algorithm that
     does not scale, and course 8 comes back to why. */
  function hamilton() {
    var best = null, bestCircuit = null;
    var used = new Array(N).fill(false);
    function walk(path) {
      if (path.length === N) {
        if (!best) best = path.slice();
        if (A[path[path.length - 1]][path[0]] && !bestCircuit) bestCircuit = path.slice();
        return;
      }
      for (var v = 0; v < N; v += 1) {
        if (used[v]) continue;
        if (path.length && !A[path[path.length - 1]][v]) continue;
        used[v] = true; path.push(v);
        walk(path);
        path.pop(); used[v] = false;
        if (best && bestCircuit) return;
      }
    }
    walk([]);
    return { path: best, circuit: bestCircuit };
  }

  function matrixPower(k) {
    var M = A.map(function (r) { return r.slice(); });
    for (var step = 1; step < k; step += 1) {
      var out = blank(N);
      for (var i = 0; i < N; i += 1) for (var j = 0; j < N; j += 1) {
        var s = 0;
        for (var t = 0; t < N; t += 1) s += M[i][t] * A[t][j];
        out[i][j] = s;
      }
      M = out;
    }
    return M;
  }
  function triangles() {
    var M3 = matrixPower(3), closed = 0;
    for (var v = 0; v < N; v += 1) closed += M3[v][v];
    return closed / 6;
  }

  /* Does the graph contain K_{3,3} as a subgraph? Every 6-subset, every split
     into 3 + 3, every cross pair adjacent. */
  function hasK33() {
    if (N < 6) return null;
    for (var mask = 0; mask < (1 << N); mask += 1) {
      var members = [];
      for (var v = 0; v < N; v += 1) if (mask & (1 << v)) members.push(v);
      if (members.length !== 6) continue;
      for (var split = 0; split < 64; split += 1) {
        var left = [], right = [];
        for (var k = 0; k < 6; k += 1) (split & (1 << k) ? left : right).push(members[k]);
        if (left.length !== 3 || left[0] !== members[0]) continue;
        var ok = true;
        for (var i = 0; ok && i < 3; i += 1) for (var j = 0; j < 3; j += 1) if (!A[left[i]][right[j]]) { ok = false; break; }
        if (ok) return { left: left, right: right };
      }
    }
    return null;
  }

  /* Planarity as far as counting takes it. The bounds are necessary; a
     K5 or K_{3,3} SUBGRAPH is conclusive; at most four vertices or at most
     eight edges is conclusive the other way, because a subdivision of K5 has
     at least ten edges and one of K_{3,3} at least nine. Anything else is
     open: subdivisions are not searched for. */
  function planarity() {
    var E = edges().length, tri = triangles();
    var bound = 3 * N - 6, bound2 = 2 * N - 4;
    var clique = cliqueNumber(), k33 = hasK33();
    var r = { V: N, E: E, bound: bound, bound2: bound2, triangles: tri,
              k5: clique.size >= 5 ? clique.vertices.slice(0, 5) : null, k33: k33, verdict: 'open' };
    if (N >= 3 && E > bound) r.verdict = 'bound';
    else if (N >= 3 && tri === 0 && E > bound2) r.verdict = 'bound2';
    else if (r.k5) r.verdict = 'k5';
    else if (r.k33) r.verdict = 'k33';
    else if (N <= 4 || E <= 8) r.verdict = 'planar';
    return r;
  }
"""


def graph_lab(cfg):
    """One editable graph, and every algorithm in the course run against it.

    The graph is the reader's: they add and remove edges and the whole panel
    re-derives. That matters more here than anywhere else on the path, because
    almost every theorem in graph theory is a claim about ALL graphs, and the
    fastest way to understand one is to try to break it. The handshake theorem
    holds no matter what you draw; Euler's condition fails the moment you give a
    third vertex odd degree; a graph stops being bipartite exactly when you
    close an odd cycle. Each of those is checked here by running the definition.

    A lesson may hand the lab its own worked example as cfg["example"], a list
    of [i, j] or [i, j, w] edges with 1-based labels; that adds a preset "This
    lesson's example" and the page can open on it.
    """
    example = cfg.get("example") or None
    markup = """      <div class="lab-toolbar">
        <div class="lab-title"><strong>Build a graph, run the algorithms</strong><span id="gCaption">Click a cell in the adjacency matrix to toggle an edge</span></div>
        <div class="inline-legend"><span class="tone-cyan"><i class="legend-swatch"></i>in the result</span><span class="tone-amber"><i class="legend-swatch"></i>visited / root</span><span class="tone-muted"><i class="legend-swatch"></i>not used</span></div>
      </div>
      <div class="lab-stage">
        <svg id="gPlot" viewBox="0 0 460 300" role="img" aria-label="A graph drawn with its vertices evenly spaced on a circle and its edges as straight lines."></svg>
      </div>
      <div class="grid-2" style="margin-top:12px;">
        <div class="table-wrap"><table class="tt" id="gMatrix"></table></div>
        <div class="table-wrap"><table class="tt" id="gFacts"></table></div>
      </div>
      <div class="status-banner" id="gStatus" style="margin-top:12px;"></div>"""
    lesson_option = (
        '            <option value="lesson">This lesson&rsquo;s example</option>\n' if example else ""
    )
    controls = """        <div class="field">
          <label for="gAlgo">Algorithm</label>
          <select id="gAlgo">
            <option value="degree">Degrees and the handshake theorem</option>
            <option value="components">Connected components</option>
            <option value="cuts">Bridges and cut vertices</option>
            <option value="bfs">Breadth-first search from vertex 1</option>
            <option value="dfs">Depth-first search from vertex 1</option>
            <option value="path">Shortest path 1 &rarr; last (unweighted)</option>
            <option value="dijkstra">Dijkstra 1 &rarr; last (weighted)</option>
            <option value="bipartite">Bipartite test / 2-colouring</option>
            <option value="euler">Euler path and circuit</option>
            <option value="hamilton">Hamilton path and circuit</option>
            <option value="tree">Is it a tree?</option>
            <option value="orders">Traversal orders, rooted at 1</option>
            <option value="spanning">Spanning tree (BFS)</option>
            <option value="mst">Minimum spanning tree (Kruskal)</option>
            <option value="colour">Greedy colouring and the clique bound</option>
            <option value="planar">Planarity by counting</option>
            <option value="walks">Walk counts from A<sup>k</sup></option>
          </select>
        </div>
        <div class="field">
          <label for="gPreset">Preset graph</label>
          <select id="gPreset">
""" + lesson_option + """            <option value="path">Path</option>
            <option value="cycle">Cycle</option>
            <option value="complete">Complete K&#8345;</option>
            <option value="star">Star</option>
            <option value="bipartite">Complete bipartite</option>
            <option value="tree">Tree</option>
            <option value="petersen">Two triangles joined</option>
            <option value="empty">No edges</option>
          </select>
        </div>
        <div>
          <div class="range-row"><label class="small-copy" for="gN">Vertices</label><span class="range-value" id="gNOut">6</span></div>
          <input id="gN" type="range" min="3" max="8" value="6" />
        </div>
        <div class="kpi-grid">
          <div class="kpi"><span>|V|</span><strong id="gV">&mdash;</strong></div>
          <div class="kpi"><span>|E|</span><strong id="gE">&mdash;</strong></div>
          <div class="kpi"><span>Σ deg</span><strong id="gSum">&mdash;</strong></div>
        </div>"""

    script = GRAPH_JS + cfg_literal("LESSON_EDGES", example) + r"""
  LESSON = lessonFrom(LESSON_EDGES);
  var algoSel = document.getElementById('gAlgo'), presetSel = document.getElementById('gPreset');
  var nS = document.getElementById('gN');
  var plot = document.getElementById('gPlot'), matrix = document.getElementById('gMatrix');
  var facts = document.getElementById('gFacts'), status = document.getElementById('gStatus');

  function lab(v) { return v + 1; }
  function seq(list, sep) { return list.map(lab).join(sep || ' → '); }
  function edgeName(e) { return lab(e[0]) + '–' + lab(e[1]); }
  function setOf(list) { return '{' + list.map(lab).join(', ') + '}'; }

  /* --- drawing ---------------------------------------------------------- */
  function positions() {
    var pts = [];
    for (var i = 0; i < N; i += 1) {
      var ang = -Math.PI / 2 + (2 * Math.PI * i) / N;
      pts.push([230 + 105 * Math.cos(ang), 150 + 105 * Math.sin(ang)]);
    }
    return pts;
  }

  function draw(highlightEdges, vertexColours, labels) {
    var pts = positions(), s = '';
    var hi = {};
    (highlightEdges || []).forEach(function (e) { hi[Math.min(e[0], e[1]) + '-' + Math.max(e[0], e[1])] = true; });
    var weighted = algoSel.value === 'dijkstra' || algoSel.value === 'mst';
    edges().forEach(function (e) {
      var on = hi[e[0] + '-' + e[1]];
      s += '<line x1="' + pts[e[0]][0] + '" y1="' + pts[e[0]][1] + '" x2="' + pts[e[1]][0] + '" y2="' + pts[e[1]][1]
        + '" stroke="' + (on ? 'var(--cyan)' : 'var(--line-strong)') + '" stroke-width="' + (on ? 3.4 : 1.8) + '" />';
      if (weighted) {
        var mx = (pts[e[0]][0] + pts[e[1]][0]) / 2, my = (pts[e[0]][1] + pts[e[1]][1]) / 2;
        s += '<circle cx="' + mx + '" cy="' + my + '" r="9" fill="var(--panel-solid)" stroke="var(--line)" />';
        s += '<text x="' + mx + '" y="' + (my + 4) + '" text-anchor="middle" font-size="10" fill="'
          + (on ? 'var(--cyan)' : 'var(--muted)') + '" font-weight="700">' + e[2] + '</text>';
      }
    });
    var PALETTE = ['var(--cyan)', 'var(--purple)', 'var(--amber)', 'var(--green)', 'var(--red)', 'var(--blue)'];
    for (var i = 0; i < N; i += 1) {
      var c = vertexColours && vertexColours[i] !== undefined && vertexColours[i] !== -1
        ? PALETTE[vertexColours[i] % PALETTE.length] : 'var(--panel-3)';
      s += '<circle cx="' + pts[i][0] + '" cy="' + pts[i][1] + '" r="17" fill="' + c
        + '" stroke="var(--line-strong)" stroke-width="2" />';
      var label = labels && labels[i] !== undefined ? labels[i] : (i + 1);
      s += '<text x="' + pts[i][0] + '" y="' + (pts[i][1] + 5) + '" text-anchor="middle" font-size="13" font-weight="800" fill="'
        + (vertexColours && vertexColours[i] !== undefined && vertexColours[i] !== -1 ? 'var(--on-accent)' : 'var(--text)')
        + '">' + label + '</text>';
    }
    plot.innerHTML = s;
  }

  function paintMatrix(power) {
    var M = power ? matrixPower(power) : A;
    var h = '<caption>' + (power ? 'A^' + power + ' — entry (i, j) counts walks of length ' + power + '; switch the algorithm to edit the graph' : 'adjacency matrix A — click to toggle')
      + '</caption><thead><tr><th></th>';
    for (var j = 1; j <= N; j += 1) h += '<th>' + j + '</th>';
    h += '</tr></thead><tbody>';
    for (var i = 0; i < N; i += 1) {
      h += '<tr><th class="rowhead">' + (i + 1) + '</th>';
      for (var j2 = 0; j2 < N; j2 += 1) {
        h += '<td class="' + (M[i][j2] ? 'on' : '') + '" data-i="' + i + '" data-j="' + j2
          + '" role="button" tabindex="0" style="cursor:pointer;">' + M[i][j2] + '</td>';
      }
      h += '</tr>';
    }
    matrix.innerHTML = h + '</tbody>';
  }

  function factRows(rows) {
    facts.innerHTML = '<thead><tr><th>quantity</th><th>value</th></tr></thead><tbody>'
      + rows.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + r[1] + '</td></tr>'; }).join('')
      + '</tbody>';
  }

  var ALGOS = {
    degree: function () {
      var degs = [], sum = 0, odd = [];
      for (var v = 0; v < N; v += 1) { var d = degree(v); degs.push(d); sum += d; if (d % 2) odd.push(v + 1); }
      draw([], null, degs);
      factRows([
        ['degree sequence', degs.slice().sort(function (a, b) { return b - a; }).join(', ')],
        ['Σ deg(v)', sum],
        ['2|E|', 2 * edges().length],
        ['vertices of odd degree', odd.length ? odd.join(', ') : 'none']
      ]);
      status.innerHTML = 'Each vertex is labelled with its degree. Σ deg(v) = <strong>' + sum
        + '</strong> and 2|E| = <strong>' + (2 * edges().length) + '</strong> — equal, as the handshake theorem '
        + 'requires, because every edge contributes exactly 2 to the total. There are <strong>' + odd.length
        + '</strong> vertices of odd degree, and that number is always even: it cannot be otherwise, since '
        + 'the total is even.';
    },
    components: function () {
      var comps = componentsOf(), colour = new Array(N).fill(0);
      comps.forEach(function (c, i) { c.forEach(function (v) { colour[v] = i; }); });
      draw(edges(), colour);
      factRows([
        ['components', comps.length],
        ['sizes', comps.map(function (c) { return c.length; }).join(', ')],
        ['connected', comps.length === 1 ? 'yes' : 'no']
      ]);
      status.innerHTML = comps.length === 1
        ? 'One component: every vertex reaches every other. A graph on ' + N + ' vertices needs at least '
          + (N - 1) + ' edges to be connected, and this one has ' + edges().length + '.'
        : '<strong>' + comps.length + ' components:</strong> ' + comps.map(setOf).join(', ')
          + '. No path crosses between them, so no walk, no matter how long, joins two of these sets.'
          + (edges().length < N - 1 ? ' With ' + edges().length + ' edges and ' + N + ' vertices, fewer than '
            + (N - 1) + ', disconnection was guaranteed before any search.' : '');
    },
    cuts: function () {
      var r = cuts(), colour = new Array(N).fill(-1);
      r.cutVertices.forEach(function (v) { colour[v] = 2; });
      draw(r.bridges.map(function (b) { return b.edge; }), colour);
      factRows([
        ['components', r.components],
        ['bridges', r.bridges.length ? r.bridges.map(function (b) { return edgeName(b.edge); }).join(', ') : 'none'],
        ['cut vertices', r.cutVertices.length ? r.cutVertices.map(lab).join(', ') : 'none'],
        ['edges on a cycle', edges().length - r.bridges.length]
      ]);
      var first = r.bridges[0];
      status.innerHTML = (r.bridges.length
          ? '<strong>' + r.bridges.length + ' bridge' + (r.bridges.length === 1 ? '' : 's') + '</strong> (highlighted): '
            + 'removing ' + edgeName(first.edge) + ' leaves ' + first.sides.map(setOf).join(' and ')
            + ' with no path between them. A bridge is exactly an edge on no cycle; the other '
            + (edges().length - r.bridges.length) + ' edge(s) each lie on a cycle and have an alternative route. '
          : (edges().length ? '<strong>No bridges:</strong> every edge lies on a cycle, so removing any one of them leaves a route round. '
            : '<strong>No edges,</strong> so nothing to remove. '))
        + (r.cutVertices.length
          ? '<strong>Cut vert' + (r.cutVertices.length === 1 ? 'ex' : 'ices') + ' ' + r.cutVertices.map(lab).join(', ')
            + '</strong> (coloured): deleting one raises the component count above ' + r.components + '.'
          : 'No cut vertex: deleting any single vertex leaves the rest as connected as before.');
    },
    bfs: function () {
      var r = bfs(0), used = [];
      for (var v = 0; v < N; v += 1) if (r.parent[v] !== -1) used.push([r.parent[v], v]);
      draw(used, null, r.dist.map(function (d) { return d === -1 ? '∞' : d; }));
      factRows([
        ['visit order', seq(r.order)],
        ['tree edges', used.map(edgeName).join(', ') || '—'],
        ['unreachable', r.dist.filter(function (d) { return d === -1; }).length],
        ['eccentricity of 1', Math.max.apply(null, r.dist)]
      ]);
      status.innerHTML = 'Labels are distances from vertex 1 in EDGES, not in geometry. Breadth-first search '
        + 'settles every vertex at distance k before any at distance k+1, which is exactly why its tree gives '
        + 'shortest paths in an unweighted graph — and why the same argument fails once edges have weights. '
        + 'The ' + (edges().length - used.length) + ' edge(s) not in the tree each join two vertices already reached.';
    },
    dfs: function () {
      var r = dfs(0), used = [];
      for (var v = 0; v < N; v += 1) if (r.parent[v] !== -1) used.push([r.parent[v], v]);
      var pos = new Array(N).fill('—');
      r.order.forEach(function (v, i) { pos[v] = i + 1; });
      draw(used, null, pos);
      factRows([
        ['visit order', seq(r.order)],
        ['tree edges', used.map(edgeName).join(', ') || '—'],
        ['visited', r.order.length + ' of ' + N],
        ['back edges', edges().filter(function (e) { return r.order.indexOf(e[0]) !== -1; }).length - used.length]
      ]);
      status.innerHTML = 'Labels are the ORDER of first visit. Depth-first search follows one branch as far as it '
        + 'goes before backtracking, so its tree is deep and narrow where breadth-first search is wide and shallow. '
        + 'Every edge not in the tree is a back edge to an ancestor, and each one closes a cycle; a graph with none '
        + 'is acyclic. Both searches visit every vertex of the component, and neither is a shortest-path algorithm '
        + 'in a weighted graph.';
    },
    path: function () {
      var r = bfs(0), target = N - 1, used = [], route = [];
      if (r.dist[target] !== -1) {
        var v = target;
        while (v !== -1) { route.unshift(v); if (r.parent[v] !== -1) used.push([r.parent[v], v]); v = r.parent[v]; }
      }
      draw(used, null, null);
      factRows([
        ['from → to', '1 → ' + N],
        ['distance (edges)', r.dist[target] === -1 ? 'unreachable' : r.dist[target]],
        ['route', route.length ? seq(route) : '—']
      ]);
      status.innerHTML = r.dist[target] === -1
        ? 'Vertex ' + N + ' is unreachable from vertex 1: they lie in different components.'
        : 'Shortest route uses <strong>' + r.dist[target] + '</strong> edges. In an unweighted graph "shortest" '
          + 'means fewest edges, and breadth-first search finds it without looking at any other path.';
    },
    dijkstra: function () {
      var r = dijkstra(0), target = N - 1, used = [], route = [];
      if (r.dist[target] < Infinity) {
        var v = target;
        while (v !== -1) { route.unshift(v); if (r.parent[v] !== -1) used.push([r.parent[v], v]); v = r.parent[v]; }
      }
      var bfsr = bfs(0);
      draw(used, null, r.dist.map(function (d) { return d === Infinity ? '∞' : d; }));
      factRows([
        ['weighted distance', r.dist[target] === Infinity ? 'unreachable' : r.dist[target]],
        ['route', route.length ? seq(route) : '—'],
        ['edges used', route.length ? route.length - 1 : 0],
        ['fewest-edge distance', bfsr.dist[target] === -1 ? '—' : bfsr.dist[target]]
      ]);
      var differs = route.length > 1 && bfsr.dist[target] !== -1 && (route.length - 1) !== bfsr.dist[target];
      status.innerHTML = 'Labels are total WEIGHT from vertex 1. '
        + (differs
            ? '<strong>The cheapest route to ' + N + ' uses ' + (route.length - 1) + ' edges while the shortest uses '
              + bfsr.dist[target] + '.</strong> That gap is the whole reason Dijkstra exists: counting edges and '
              + 'adding weights are different questions.'
            : 'Here the cheapest route to ' + N + ' happens to use the fewest edges too. Toggle an edge to break that — '
              + 'the two answers coincide only by accident.');
    },
    bipartite: function () {
      var r = twoColour();
      draw(edges(), r.conflict ? null : r.colour);
      var sides = [[], []];
      if (!r.conflict) for (var v = 0; v < N; v += 1) sides[r.colour[v]].push(v + 1);
      factRows([
        ['bipartite', r.conflict ? 'no' : 'yes'],
        ['part X', r.conflict ? '—' : '{' + sides[0].join(', ') + '}'],
        ['part Y', r.conflict ? '—' : '{' + sides[1].join(', ') + '}'],
        ['conflict', r.conflict ? 'vertices ' + (r.conflict[0] + 1) + ' and ' + (r.conflict[1] + 1) : 'none']
      ]);
      status.innerHTML = r.conflict
        ? '<strong>Not bipartite.</strong> Vertices ' + (r.conflict[0] + 1) + ' and ' + (r.conflict[1] + 1)
          + ' are adjacent and the 2-colouring forced them the same colour, which means an ODD cycle passes '
          + 'through them. A graph is bipartite exactly when it has no odd cycle — nothing else can obstruct it.'
        : '<strong>Bipartite.</strong> The two colours are a partition into independent sets, and every edge '
          + 'crosses between them. Equivalently: every cycle in this graph has even length.';
    },
    euler: function () {
      var odd = [];
      for (var v = 0; v < N; v += 1) if (degree(v) % 2) odd.push(v + 1);
      var comps = componentsOf().filter(function (c) { return c.some(function (v) { return degree(v) > 0; }); });
      var connected = comps.length <= 1;
      var circuit = connected && odd.length === 0 && edges().length > 0;
      var pathOnly = connected && odd.length === 2;
      draw(edges(), null, null);
      factRows([
        ['odd-degree vertices', odd.length ? odd.join(', ') + ' (' + odd.length + ')' : 'none'],
        ['edges connected', connected ? 'yes' : 'no'],
        ['Euler circuit', circuit ? 'yes' : 'no'],
        ['Euler path', circuit || pathOnly ? 'yes' : 'no']
      ]);
      status.innerHTML = circuit
        ? '<strong>An Euler circuit exists.</strong> Every vertex has even degree and the edges form one connected '
          + 'piece — that is the complete criterion, and it is checkable in one pass over the degrees.'
        : pathOnly
          ? '<strong>An Euler path exists but no circuit.</strong> Exactly two vertices have odd degree (' + odd.join(' and ')
            + '), and any Euler path must start at one and end at the other.'
          : '<strong>Neither.</strong> ' + (connected
              ? 'There are ' + odd.length + ' odd-degree vertices; an Euler path allows 0 or 2 and nothing else, '
                + 'because every visit to a vertex uses two edge-ends.'
              : 'The edges are not all in one component, so no single walk can cover them.');
    },
    hamilton: function () {
      var r = hamilton();
      var used = [];
      var s = r.circuit || r.path;
      if (s) for (var i = 0; i + 1 < s.length; i += 1) used.push([s[i], s[i + 1]]);
      if (r.circuit) used.push([s[s.length - 1], s[0]]);
      draw(used, null, null);
      factRows([
        ['Hamilton path', r.path ? seq(r.path) : 'none'],
        ['Hamilton circuit', r.circuit ? seq(r.circuit) + ' → ' + (r.circuit[0] + 1) : 'none'],
        ['search space', N + '! = ' + (function () { var f = 1; for (var i = 2; i <= N; i += 1) f *= i; return f; })() + ' orderings']
      ]);
      status.innerHTML = (r.circuit
          ? '<strong>A Hamilton circuit exists.</strong> '
          : r.path ? '<strong>A Hamilton path exists, but no circuit.</strong> ' : '<strong>Neither exists.</strong> ')
        + 'Note how it was found: by trying orderings until one worked. Unlike the Euler condition, which is a '
        + 'one-pass check on degrees, no simple criterion decides this — deciding it in general is NP-complete, '
        + 'which is why the vertex count here stops at 8.';
    },
    tree: function () {
      var comps = componentsOf(), E = edges().length;
      var connected = comps.length === 1;
      var acyclic = E === N - comps.length;
      var isTree = connected && E === N - 1;
      draw(edges(), null, null);
      var leaves = [];
      for (var v = 0; v < N; v += 1) if (degree(v) === 1) leaves.push(v + 1);
      factRows([
        ['|V|', N], ['|E|', E], ['|V| − 1', N - 1],
        ['connected', connected ? 'yes' : 'no'],
        ['acyclic', acyclic ? 'yes' : 'no'],
        ['tree', isTree ? 'yes' : 'no'],
        ['leaves', leaves.length ? leaves.join(', ') : 'none']
      ]);
      status.innerHTML = isTree
        ? '<strong>A tree.</strong> Connected with exactly ' + (N - 1) + ' edges — and for a connected graph those '
          + 'two conditions force each other: one more edge creates a cycle, one fewer disconnects it. Every pair '
          + 'of vertices is joined by exactly one path, and every edge is a bridge.'
        : connected
          ? '<strong>Connected but not a tree:</strong> ' + E + ' edges where a tree on ' + N + ' vertices has exactly ' + (N - 1)
            + '. The extra ' + (E - (N - 1)) + ' edge(s) close cycles.'
          : acyclic
            ? '<strong>Not a tree, but a forest:</strong> ' + comps.length + ' components and no cycle, so ' + E
              + ' = ' + N + ' − ' + comps.length + ' edges, one tree per component.'
            : '<strong>Neither a tree nor a forest:</strong> ' + comps.length + ' components, so not connected, and '
              + E + ' edges where a forest with ' + comps.length + ' components has ' + (N - comps.length)
              + ' — the extra ' + (E - (N - comps.length)) + ' close cycles.'
              + (E === N - 1 ? ' The count |E| = |V| − 1 holds and proves nothing on its own.' : '');
    },
    orders: function () {
      var r = rootedOrders(0), used = [];
      for (var v = 0; v < N; v += 1) if (r.parent[v] !== -1) used.push([r.parent[v], v]);
      var colour = new Array(N).fill(-1);
      colour[0] = 2;
      draw(used, colour);
      var left = edges().length - r.treeEdges;
      factRows([
        ['preorder', seq(r.pre, ' ')],
        ['inorder', r.ino ? seq(r.ino, ' ') : 'undefined — vertex ' + lab(r.tooMany) + ' has 3 or more children'],
        ['postorder', seq(r.post, ' ')],
        ['level order', seq(r.level, ' ')],
        ['vertices in the tree', r.reached + ' of ' + N],
        ['edges not in the tree', left]
      ]);
      status.innerHTML = 'Rooted at vertex 1 (coloured), children taken in increasing order; a single child counts as '
        + 'the left child. Preorder is the depth-first visit order: the root before its subtrees. Postorder finishes '
        + 'every subtree before its root. '
        + (r.ino
          ? 'Inorder puts each root between its two subtrees, which needs at most two children per vertex — true here.'
          : '<strong>Inorder is undefined:</strong> vertex ' + lab(r.tooMany) + ' has ' + '3 or more children, and there '
            + 'is no single place for the root among them. Pre- and postorder generalise; inorder does not.')
        + (left > 0 ? ' <strong>This graph is not a tree:</strong> the orders are those of the depth-first spanning '
          + 'tree from 1, and ' + left + ' edge(s) were left out.' : '')
        + (r.reached < N ? ' ' + (N - r.reached) + ' vertex(es) are unreachable from 1 and are not in the tree.' : '');
    },
    spanning: function () {
      var r = bfs(0), used = [];
      for (var v = 0; v < N; v += 1) if (r.parent[v] !== -1) used.push([r.parent[v], v]);
      var reached = r.order.length;
      draw(used, null, null);
      factRows([
        ['tree edges', used.length],
        ['vertices spanned', reached + ' of ' + N],
        ['edges left out', edges().length - used.length]
      ]);
      status.innerHTML = reached === N
        ? 'A spanning tree: <strong>' + used.length + ' edges reaching all ' + N + ' vertices</strong>, which is '
          + N + ' − 1 exactly. Every connected graph has one, and the ' + (edges().length - used.length)
          + ' edges left out are precisely the ones that would close a cycle.'
        : 'No spanning tree exists: the graph is disconnected, so a search from vertex 1 reaches only '
          + reached + ' of ' + N + ' vertices. What you get is a spanning tree of one COMPONENT.';
    },
    mst: function () {
      var r = kruskal(), rows = [];
      r.considered.forEach(function (c) {
        rows.push([edgeName(c[0]) + ' (w ' + c[0][2] + ')', c[1] ? 'taken' : 'rejected: closes a cycle']);
      });
      draw(r.chosen, null, null);
      factRows([['total weight', r.total], ['edges chosen', r.chosen.length + ' of ' + edges().length]].concat(rows.slice(0, 8)));
      status.innerHTML = r.chosen.length === N - 1
        ? 'Kruskal takes edges in increasing weight and skips any that would close a cycle. Total weight '
          + '<strong>' + r.total + '</strong>. The greedy choice is provably optimal here — which is unusual, '
          + 'and course 8 explains what makes this problem yield to greed when most do not.'
        : 'The graph is disconnected, so Kruskal produces a minimum spanning FOREST: '
          + r.chosen.length + ' edges, weight ' + r.total + '. No set of edges can span a disconnected graph.';
    },
    colour: function () {
      var colour = greedyColour();
      var used = Math.max.apply(null, colour) + 1;
      var maxDeg = 0, E = edges().length;
      for (var v = 0; v < N; v += 1) maxDeg = Math.max(maxDeg, degree(v));
      var clique = cliqueNumber(), bip = !twoColour().conflict;
      var lower = Math.max(clique.size, E === 0 ? 1 : (bip ? 2 : 3));
      draw(edges(), colour);
      factRows([
        ['clique number ω (lower bound)', clique.size + (clique.size >= 2 ? '  — ' + setOf(clique.vertices) : '')],
        ['colours used by greedy (upper bound)', used],
        ['max degree Δ', maxDeg],
        ['greedy bound Δ + 1', maxDeg + 1],
        ['bipartite (2-colourable)', bip ? 'yes' : 'no']
      ]);
      status.innerHTML = 'Greedy colouring in vertex order used <strong>' + used + '</strong> colour'
        + (used === 1 ? '' : 's') + ', never more than Δ + 1 = ' + (maxDeg + 1) + '. '
        + (lower === used
          ? (clique.size >= lower
              ? 'The clique ' + setOf(clique.vertices) + ' forces χ ≥ ' + lower
              : 'An odd cycle forces χ ≥ 3 (the largest clique, ' + setOf(clique.vertices) + ', only gives 2)')
            + ' and greedy achieved ' + used + ': <strong>the bounds meet, so χ = ' + used + '.</strong>'
          : (bip && used > 2
            ? '<strong>The graph is bipartite, so χ = 2</strong>, and greedy used ' + used + ': the order it visited '
              + 'vertices in cost it ' + (used - 2) + ' colour(s) it did not need. Greedy is a bound, not the answer.'
            : '<strong>χ is somewhere between ' + lower + ' and ' + used + '.</strong> The largest clique gives the lower bound and '
              + 'greedy the upper; closing the gap means a better order or an exhaustive search, and finding χ '
              + 'in general is NP-hard.'));
    },
    planar: function () {
      var r = planarity();
      var hi = [];
      if (r.verdict === 'k5') for (var i = 0; i < 5; i += 1) for (var j = i + 1; j < 5; j += 1) hi.push([r.k5[i], r.k5[j]]);
      if (r.verdict === 'k33') r.k33.left.forEach(function (a) { r.k33.right.forEach(function (b) { hi.push([a, b]); }); });
      draw(hi, null, null);
      var rows = [
        ['|V|, |E|', r.V + ', ' + r.E],
        ['3|V| − 6', r.bound + (r.E > r.bound ? '  — EXCEEDED' : '  — satisfied')],
        ['triangles', r.triangles],
        ['2|V| − 4 (triangle-free only)', r.triangles === 0 ? r.bound2 + (r.E > r.bound2 ? '  — EXCEEDED' : '  — satisfied') : 'does not apply'],
        ['K₅ subgraph', r.k5 ? setOf(r.k5) : 'none'],
        ['K₃,₃ subgraph', r.k33 ? setOf(r.k33.left) + ' × ' + setOf(r.k33.right) : 'none']
      ];
      var verdict = {
        bound: 'NOT PLANAR: |E| = ' + r.E + ' > ' + r.bound,
        bound2: 'NOT PLANAR: triangle-free and |E| = ' + r.E + ' > ' + r.bound2,
        k5: 'NOT PLANAR: contains K₅',
        k33: 'NOT PLANAR: contains K₃,₃',
        planar: 'PLANAR',
        open: 'inconclusive by counting'
      }[r.verdict];
      rows.push(['verdict', verdict]);
      factRows(rows);
      status.innerHTML = r.verdict === 'bound'
        ? '<strong>Not planar.</strong> A simple planar graph on ' + r.V + ' vertices has at most 3·' + r.V + ' − 6 = '
          + r.bound + ' edges, from V − E + F = 2 and 3F ≤ 2E. This one has ' + r.E + ', so no crossing-free drawing exists — '
          + 'settled by arithmetic, with no drawing attempted.'
        : r.verdict === 'bound2'
          ? '<strong>Not planar.</strong> |E| = ' + r.E + ' passes the general bound ' + r.bound + ', but the graph has no '
            + 'triangle, so every face would need at least 4 edges and 4F ≤ 2E gives |E| ≤ 2·' + r.V + ' − 4 = ' + r.bound2
            + '. Exceeded.'
          : r.verdict === 'k5' || r.verdict === 'k33'
            ? '<strong>Not planar.</strong> Both counting bounds pass, but the highlighted edges are a '
              + (r.verdict === 'k5' ? 'K₅' : 'K₃,₃') + ' inside the graph, and by Kuratowski a graph containing either '
              + 'obstruction (or a subdivision of one) cannot be drawn without crossings.'
            : r.verdict === 'planar'
              ? '<strong>Planar.</strong> ' + (r.V <= 4 ? 'Every graph on at most four vertices is planar — K₄ is the largest, and it is.'
                : 'With ' + r.E + ' edges no subdivision of K₅ (at least 10 edges) or of K₃,₃ (at least 9) can fit, so by '
                + 'Kuratowski the graph is planar.') + ' The counting bounds were satisfied, as they must be.'
              : '<strong>Inconclusive by counting.</strong> |E| = ' + r.E + ' satisfies ' + r.bound
                + (r.triangles === 0 ? ' and ' + r.bound2 : '') + ', and no K₅ or K₃,₃ sits inside the graph as a subgraph — but the '
                + 'bounds are necessary, not sufficient, and this lab does not search for SUBDIVISIONS. The Petersen graph '
                + 'passes both bounds and is not planar. Settling it is Kuratowski, or a drawing.';
    },
    walks: function () {
      draw(edges(), null, null);
      paintMatrix(2);
      var M2 = matrixPower(2), M3 = matrixPower(3);
      var closed3 = 0;
      for (var v = 0; v < N; v += 1) closed3 += M3[v][v];
      factRows([
        ['A²[1][1] = deg(1)', M2[0][0]],
        ['walks of length 2 from 1 to ' + N, M2[0][N - 1]],
        ['walks of length 3 from 1 to ' + N, M3[0][N - 1]],
        ['Σ A³[v][v]', closed3 + ' = 6 × (number of triangles) = ' + (closed3 / 6)]
      ]);
      status.innerHTML = 'The matrix above is A², whose (i, j) entry counts walks of length 2 from i to j — '
        + 'a fact that follows from how matrix multiplication sums over the middle vertex. The diagonal of A³ '
        + 'counts closed walks of length 3, and each triangle contributes 6 of them (3 starting points × 2 directions), '
        + 'so this graph has <strong>' + (closed3 / 6) + '</strong> triangle(s). To change the graph, switch the '
        + 'algorithm to Degrees, toggle, and switch back.';
    }
  };

  function redraw() {
    document.getElementById('gNOut').textContent = nS.value;
    document.getElementById('gV').textContent = N;
    document.getElementById('gE').textContent = edges().length;
    var sum = 0;
    for (var v = 0; v < N; v += 1) sum += degree(v);
    document.getElementById('gSum').textContent = sum;
    if (algoSel.value !== 'walks') paintMatrix(0);
    (ALGOS[algoSel.value] || ALGOS.degree)();
  }

  function rebuild() {
    N = +nS.value;
    useLessonWeights = presetSel.value === 'lesson';
    A = (PRESETS[presetSel.value] || PRESETS.empty)(N);
    redraw();
  }

  function toggle(td) {
    var i = +td.dataset.i, j = +td.dataset.j;
    if (i === j) return;
    A[i][j] = A[i][j] ? 0 : 1;
    A[j][i] = A[i][j];
    redraw();
  }
  matrix.addEventListener('click', function (e) {
    var td = e.target.closest('td[data-i]');
    if (!td || algoSel.value === 'walks') return;
    toggle(td);
  });
  matrix.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var td = e.target.closest('td[data-i]');
    if (!td || algoSel.value === 'walks') return;
    e.preventDefault();
    toggle(td);
  });
  algoSel.addEventListener('change', redraw);
  presetSel.addEventListener('change', rebuild);
  nS.addEventListener('input', rebuild);

  algoSel.value = """ + '"%s"' % cfg.get("algo", "degree") + r""";
  presetSel.value = """ + '"%s"' % cfg.get("preset", "cycle") + r""";
  nS.value = """ + str(cfg.get("n", 6)) + r""";
  rebuild();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Graph workbench",
        subtitle="Your graph, the course's algorithms",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Build and analyse"),
        panel_intro=cfg.get(
            "panel_intro",
            "Toggle any cell of the adjacency matrix and everything re-derives. "
            "Try to break the theorem the lesson just stated; that is the fastest "
            "way to see what it actually rules out.",
        ),
        script=script,
    )
