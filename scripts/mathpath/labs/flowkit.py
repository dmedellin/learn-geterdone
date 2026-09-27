"""Flow -- four modes, one residual network, and a certificate.

THIS IS THE KIT WHERE THE ALGORITHM PROVES ITSELF. Everywhere else on this path
a page measures a count and puts a proved bound beside it. Here the algorithm
produces its own proof: when no augmenting path remains, the set reachable from
the source in the residual network is a cut whose capacity EQUALS the flow's
value, and every mode below asserts that equality on the reader's own network
rather than describing it.

THE REVERSE ARC IS THE SUBJECT, and the kit is built so a reader can turn it
off. `algo_core.maxflow(G, s, t, { reverse: false })` builds the residual
network without backward arcs, which is the preset the `augment` mode opens on:
the forward-only search gets stuck below the maximum, in four vertices, and the
same network with backward arcs reaches it. Undoing an earlier choice is not an
optimisation. It is the reason the algorithm is correct.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE.
`algo_core.FLOW_JS` holds the algorithms -- residual, bfsPath, augment,
maxflow, minCutFrom, matchingNetwork, konigCover, gadgetBuild -- and nothing
here reimplements one. What this kit adds is the checking:

  every cut, enumerated      `minCutBrute` lists every set containing the
                             source and not the sink, at a cap it states, and
                             reports the smallest capacity. The theorem is then
                             a comparison of two numbers the page computed
                             separately, and the cut the algorithm returns is
                             checked to be one of the smallest.
  conservation, arc by arc   a flow is checked at every interior vertex and
                             against every capacity, so "a flow" is a verdict
                             and not an assumption.
  the matching, exhaustively `matchingBrute` maximises over every subset of the
                             pairs through ORACLE_JS's `bruteOptimal`, which
                             knows nothing about flow at all -- and a greedy
                             maximal matching is run beside it, because the
                             misconception is that a matching nothing can be
                             added to is maximum.
  Menger, in the gadget      with every capacity 1 the flow value counts
                             arc-disjoint paths, and the minimum cut counts the
                             arcs that must be cut to separate the two ends.
                             The page computes both and compares them.

THE MODES:

  augment   the residual network drawn beside the original, the bottleneck
            pushed per augmentation, and the forward-only failure as a preset
  mincut    the reachable set, the cut's arcs and capacity against the flow
            value, every cut enumerated, and a set of saturated arcs that is
            not a cut
  matching  a bipartite editor, the network built from it, the matching, the
            cut read as a vertex cover, and the deficient set when the matching
            is imperfect
  gadget    vertex splitting, unit capacities and a super-source, each drawn
            beside the original network, solved, with the correspondence

BLOCKS PER MODE. COUNT_JS, DIGRAPH_JS, FLOW_JS and this kit's own block are on
every page here and come to about 10 KB gzipped. ORACLE_JS is added by the
three modes that enumerate something -- `mincut` for every cut, `matching` for
every subset of the pairs, `gadget` for the cut that Menger's count is compared
with -- and `augment` does not carry it, because `augment` enumerates nothing:
its whole content is one path at a time.

Measured, on a real lesson page rendered by scripts/mathpath/render.py --
gzipped, against the repository's 62 KB ceiling:

    augment 36.0   matching 38.9   mincut 39.2   gadget 39.6

Re-derive these rather than trusting them. `augment` is the lightest because it
is the one mode that enumerates nothing and therefore does not ship the oracle
block.

Nothing here rounds. Capacities, flows, bottlenecks, cut capacities, matching
sizes and cover sizes are integers, and integer arithmetic at these sizes is
exact in any representation.

EVERY PRESET PINS WHAT IT PRINTS, AND NO PRESET CARRIES A NOTE ANY MORE.
A preset used to carry two pieces of prose: a `label` in the <select> and a
`note` about the outcome. Nothing in this repository could read either, and a
sweep of fifteen kits found 57 of those strings false about the lab they
described. Rendering does not help -- `dpkit` printed its selected note into
the status banner and had a HIGHER correction rate than `graphkit`, which
rendered none -- so the notes here are deleted rather than re-checked, and
each preset now carries `expect`: {kpi element id: the exact text the page
prints}. scripts/build_paths.py writes it to
scripts/generated-expectations.json and scripts/labcheck.js selects the option
on the BUILT page, dispatches the menu's own change handler and compares
getElementById(id).textContent. Every figure below was read off the running
kit with `node scripts/labcheck.js --observe <page>`. See `_expect` and
scripts/mathpath/AGENTS.md.

NOTHING HERE RENDERED A PRESET NOTE, so nothing in the markup changed when
they went. The `built.note` in `_gadget`'s status line is NOT one: it comes
back from `algo_core.gadgetBuild` and is one of three fixed sentences about
the transformation that ran, chosen by `kind` rather than written per
instance.
"""

from .algo_core import COUNT_JS, DIGRAPH_JS, FLOW_JS, ORACLE_JS
from .common import Lab

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

FKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     A network clause is `u>v c`: an arc from u to v of capacity c, 1-based,
     because that is what the prose uses. There is no cost field anywhere in
     this kit: the cheapest flow of a given value is a linear programme and this
     course does not develop the algorithm for it, so a cost column here would
     be a control with nothing behind it. */
  var FK_MAXN = 10;
  var FK_MAXARCS = 22;

  function fkClauses(text) {
    var parts = String(text).split(/[,;\n]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }
  function fkParse(text, maxN) {
    maxN = maxN === undefined ? FK_MAXN : maxN;
    var cl = fkClauses(text), raw = [], n = 0, i;
    if (!cl.length) return { bad: 'write at least one arc' };
    if (cl.length > FK_MAXARCS) return { bad: 'that is more than ' + FK_MAXARCS + ' arcs' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*(?:>|to)\s*(\d+)(?:[\s:]+(\d+))?$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '"' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10);
      var c = m[3] === undefined ? 1 : parseInt(m[3], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'a loop at ' + u + ' carries flow nowhere' };
      if (c < 0 || c > 999) return { bad: 'keep the capacity between 0 and 999' };
      raw.push([u, v, c]);
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (n < 2) return { bad: 'a network needs a source and a sink' };
    var G = dgNew(n, true);
    for (i = 0; i < raw.length; i += 1) dgAdd(G, raw[i][0] - 1, raw[i][1] - 1, 0, raw[i][2]);
    return { G: G, n: n };
  }
  /* Bipartite pairs, as the reader writes them: `1-2` is left 1 to right 2. */
  function fkParsePairs(text, left, right) {
    var cl = fkClauses(text), out = [], seen = {}, i;
    if (!cl.length) return { bad: 'write at least one pair' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*(?:-|to)\s*(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as a pair' };
      var a = parseInt(m[1], 10), b = parseInt(m[2], 10);
      if (a < 1 || a > left) return { bad: 'there is no ' + a + ' on the left' };
      if (b < 1 || b > right) return { bad: 'there is no ' + b + ' on the right' };
      var k = a + '-' + b;
      if (!seen[k]) { seen[k] = true; out.push([a - 1, b - 1]); }
    }
    return { pairs: out };
  }
  function fkLabel(v) { return v + 1; }
  function fkNames(list) {
    return (list || []).map(function (v) { return v + 1; }).join(', ');
  }
  function fkArcName(a) { return (a.u + 1) + ' → ' + (a.v + 1); }
  function fkPlural(n, one, many) { return n === 1 ? one : many; }
  /* Every capacity added up: the finite stand-in for "no bound" that a gadget
     needs. It is never binding -- no cut can exceed it -- and unlike Infinity
     it cannot become a bottleneck of Infinity and hang the augmentation loop. */
  function fkTotalCap(G) {
    return G.arcs.reduce(function (t, a) { return t + a.cap; }, 0);
  }

  /* --------------------------------------------- the OTHER way to pick a path

     `bfsPath` takes the shortest augmenting path, which is Edmonds-Karp and
     bounds the number of augmentations. This takes the FIRST path a depth-first
     search finds, which is the naive choice, and it is here for two reasons.

     It is how the forward-only failure is exhibited without a hand-picked path.
     On the four-vertex network the shortest path never goes through the middle
     arc, so a breadth-first search cannot get stuck; a depth-first one takes the
     middle arc immediately, and with backward arcs switched off it is then stuck
     one unit below the maximum. The failure is produced by a rule, not by a
     path typed into a preset, so it survives the reader editing the network.

     And it is how the cost of the CHOICE is measured: the same network, the same
     algorithm, two path rules, two counts of augmentations. */
  function fkDfsPath(res, s, t) {
    var G = res.graph, idx = dgIndex(G), n = G.n;
    var seen = new Array(n).fill(false), prev = new Array(n).fill(-1), order = [];
    var found = false;
    (function walk(v) {
      if (found) return;
      seen[v] = true; order.push(v);
      if (v === t) { found = true; return; }
      for (var k = 0; k < idx.out[v].length; k += 1) {
        var id = idx.out[v][k], u = G.arcs[id].v;
        if (seen[u] || G.arcs[id].cap <= 0) continue;
        prev[u] = id;
        walk(u);
        if (found) return;
      }
    })(s);
    if (!found) return { path: null, reachable: order };
    var path = [], at = t;
    while (at !== s) { path.push(prev[at]); at = G.arcs[prev[at]].u; }
    return { path: path.reverse(), reachable: order };
  }
  function fkFindPath(res, s, t, rule) {
    return rule === 'dfs' ? fkDfsPath(res, s, t) : bfsPath(res, s, t);
  }
  /* The augmentation replayed step by step, so the panel can stand at any one of
     them: `residual`, `fkFindPath` and `augment` are called exactly as maxflow
     calls them, and the state before each push is kept rather than recomputed. */
  function fkAugmentations(G, s, t, opts) {
    opts = opts || {};
    var f = zeroFlow(G), steps = [], guard = 0;
    while (guard < 400) {
      guard += 1;
      var res = residual(G, f, opts);
      var found = fkFindPath(res, s, t, opts.rule);
      if (!found.path) {
        steps.push({ flow: f.slice(), residual: res, path: null, reachable: found.reachable,
                     value: flowValue(G, f, s) });
        break;
      }
      var a = augment(G, f, res, found.path);
      steps.push({ flow: f.slice(), residual: res, path: found.path, bottleneck: a.bottleneck,
                   after: a.flow.slice(), value: flowValue(G, f, s),
                   valueAfter: flowValue(G, a.flow, s) });
      f = a.flow;
    }
    return { steps: steps, flow: f, value: flowValue(G, f, s),
             augmentations: steps.filter(function (x) { return x.path; }).length };
  }
  /* A step index a control hands in, clamped into a list that may have got
     shorter since it was set -- which is what makes a second redraw safe. */
  function fkStep(want, length) {
    if (!length) return 0;
    var k = parseInt(want, 10);
    if (!isFinite(k) || k < 0) k = 0;
    return Math.min(k, length - 1);
  }

  /* ---------------------------------------------- is this thing even a flow

     Conservation at every interior vertex and every arc inside its capacity,
     checked separately, because they fail separately and a reader who is told
     only "not a flow" has learned nothing. */
  function fkCheckFlow(G, f, s, t) {
    var overfull = [], negative = [], violated = [], rows = [], v;
    G.arcs.forEach(function (a, id) {
      if (f[id] > a.cap) overfull.push(id);
      if (f[id] < 0) negative.push(id);
    });
    for (v = 0; v < G.n; v += 1) {
      var out = 0, into = 0;
      G.arcs.forEach(function (a, id) {
        if (a.u === v) out += f[id];
        if (a.v === v) into += f[id];
      });
      var net = out - into, want = (v === s || v === t) ? null : 0;
      rows.push({ v: v, out: out, into: into, net: net, want: want,
                  ok: want === null || net === 0 });
      if (want !== null && net !== 0) violated.push(v);
    }
    return { rows: rows, violated: violated, overfull: overfull, negative: negative,
             ok: !violated.length && !overfull.length && !negative.length };
  }

  /* ------------------------------------------------------ every cut, listed

     A cut is a set containing the source and not the sink; its capacity is the
     total capacity of the arcs leaving the set, and arcs coming back in
     contribute NOTHING -- which is the line readers most often get wrong and
     the reason this is written out rather than inferred from the flow.

     The theorem is then two numbers the page computed by different routes: the
     value the augmenting-path algorithm reached, and the smallest capacity in
     this list. Ten vertices is 256 sets, which is instant; above that it is
     refused through oracleCap rather than run slowly. */
  function cutCapacity(G, inS) {
    var cap = 0;
    G.arcs.forEach(function (a) { if (inS[a.u] && !inS[a.v]) cap += a.cap; });
    return cap;
  }
  function cutBack(G, inS) {
    var cap = 0;
    G.arcs.forEach(function (a) { if (!inS[a.u] && inS[a.v]) cap += a.cap; });
    return cap;
  }
  function minCutBrute(G, s, t, cap) {
    cap = cap === undefined ? 10 : cap;
    oracleCap('minCutBrute', G.n, cap);
    var best = null, bestSets = [], examined = 0, all = [];
    forEachSubset(G.n, function (mask) {
      if (!(mask & (1 << s))) return;
      if (mask & (1 << t)) return;
      examined += 1;
      var inS = [], i;
      for (i = 0; i < G.n; i += 1) inS.push(!!(mask & (1 << i)));
      var c = cutCapacity(G, inS);
      all.push({ mask: mask, S: maskMembers(mask, G.n), capacity: c, back: cutBack(G, inS) });
      if (best === null || c < best) { best = c; bestSets = [mask]; }
      else if (c === best) bestSets.push(mask);
    });
    return runOf({ capacity: best, minimal: bestSets, cuts: all, count: examined },
                 { nodes: examined }, []);
  }
  /* Is the given set one of the smallest? The algorithm returns ONE cut and the
     enumeration finds all of them, so this is the honest comparison: not "the
     same set" but "a set of the same, smallest, capacity". */
  function cutIsMinimum(brute, S) {
    var mask = 0;
    S.forEach(function (v) { mask |= (1 << v); });
    return brute.result.minimal.indexOf(mask) !== -1;
  }

  /* --------------------------------- saturated is not the same as being a cut

     The misconception has a shape: take the saturated arcs, delete them, and
     see whether the sink is still reachable. Where it is, that set of arcs is
     not a cut however full every one of them is. */
  function saturatedArcs(G, f) {
    var out = [];
    G.arcs.forEach(function (a, id) { if (a.cap > 0 && f[id] === a.cap) out.push(id); });
    return out;
  }
  function reachesWithout(G, skip, s, t) {
    var block = {};
    (skip || []).forEach(function (id) { block[id] = true; });
    var idx = dgIndex(G), seen = new Array(G.n).fill(false), stack = [s], order = [];
    seen[s] = true;
    while (stack.length) {
      var v = stack.pop();
      order.push(v);
      idx.out[v].forEach(function (id) {
        if (block[id]) return;
        var u = G.arcs[id].v;
        if (!seen[u]) { seen[u] = true; stack.push(u); }
      });
    }
    return { reaches: seen[t], seen: seen, order: order };
  }

  /* ------------------------------------------------- matching, three answers

     greedyMatching takes the pairs in the order typed and keeps any whose ends
     are both free. That is a MAXIMAL matching -- nothing can be added to it --
     and the misconception is that maximal means maximum. matchingBrute
     maximises over every subset of the pairs through ORACLE_JS's bruteOptimal,
     which has never heard of a flow network. The flow is the third answer, and
     all three are printed. */
  function greedyMatching(pairs) {
    var usedL = {}, usedR = {}, out = [];
    pairs.forEach(function (p, id) {
      if (usedL[p[0]] || usedR[p[1]]) return;
      usedL[p[0]] = true; usedR[p[1]] = true;
      out.push({ id: id, left: p[0], right: p[1] });
    });
    return out;
  }
  function matchingBrute(pairs, cap) {
    cap = cap === undefined ? 16 : cap;
    return bruteOptimal(pairs, function (members) {
      var usedL = {}, usedR = {}, i;
      for (i = 0; i < members.length; i += 1) {
        var p = pairs[members[i]];
        if (usedL[p[0]] || usedR[p[1]]) return null;
        usedL[p[0]] = true; usedR[p[1]] = true;
      }
      return members.length;
    }, cap);
  }
  /* Hall's condition, read off the cut: the source side's left vertices are a
     set S, and the right vertices they can reach are N(S). When the matching is
     imperfect the cut exhibits an S with |N(S)| smaller than |S|, which is the
     deficiency, and this returns the set rather than the inequality. */
  function hallDeficient(net, f, pairs) {
    var cut = minCutFrom(net.graph, f, net.s), inS = {};
    cut.S.forEach(function (v) { inS[v] = true; });
    var S = [], i;
    for (i = 0; i < net.left; i += 1) if (inS[i]) S.push(i);
    var nb = {};
    pairs.forEach(function (p) { if (inS[p[0]]) nb[p[1]] = true; });
    var N = Object.keys(nb).map(function (k) { return parseInt(k, 10); })
      .sort(function (a, b) { return a - b; });
    return { S: S, neighbours: N, deficient: N.length < S.length,
             deficiency: S.length - N.length, cut: cut };
  }

  /* ------------------------------------------- the gadgets, with finite bounds

     gadgetBuild leaves an uncapped arc at Infinity, which is right as a
     statement and wrong as a number: a bottleneck of Infinity never terminates.
     Every uncapped arc here is therefore given the total capacity of the
     original network, which no cut can exceed and which is therefore never
     binding -- the same statement, in a number the arithmetic can hold. */
  function fkVertexCaps(G, spec) {
    var total = fkTotalCap(G) + 1, caps = [], v;
    for (v = 0; v < G.n; v += 1) {
      caps.push(spec && spec[v] !== undefined && spec[v] !== null ? spec[v] : total);
    }
    return caps;
  }
  /* Arc-disjoint paths, counted by walking the unit flow rather than read off
     its value: take a unit out of the source, follow saturated arcs to the
     sink, and remove them. The count must equal the flow value, and where it
     does the paths themselves can be printed. */
  function unitPaths(G, f, s, t) {
    var left = f.slice(), idx = dgIndex(G), paths = [], guard = 0;
    while (guard < 200) {
      guard += 1;
      var path = [s], at = s, moved = true;
      while (at !== t && moved) {
        moved = false;
        for (var k = 0; k < idx.out[at].length; k += 1) {
          var id = idx.out[at][k];
          if (left[id] <= 0) continue;
          left[id] -= 1;
          at = G.arcs[id].v;
          path.push(at);
          moved = true;
          break;
        }
      }
      if (at !== t) break;
      paths.push(path);
    }
    return paths;
  }
"""


# ---------------------------------------------------------------------------
# One core per mode. `augment` enumerates nothing, so it does not carry the
# oracle block: its whole content is one augmenting path at a time.
# ---------------------------------------------------------------------------

_BASE_JS = COUNT_JS + DIGRAPH_JS + FLOW_JS + FKIT_JS
_ORACLE_JS = COUNT_JS + DIGRAPH_JS + ORACLE_JS + FLOW_JS + FKIT_JS


# ---------------------------------------------------------------------------
# Control furniture. The same shapes every kit on this path uses. Drawings take
# only the two viewBox widths theme.py gives a horizontal-scroll minimum, 520
# and 660, because any other width shrinks the labels to illegibility on a
# phone instead of scrolling it.
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
    """A text box that starts EMPTY and is filled by the script at startup.

    Every arc a reader types here contains a `>`, which a value attribute in the
    markup cannot carry: escaped as `&gt;` a browser decodes it and
    scripts/labcheck.js does not, and left raw it terminates that harness's tag
    scan. So the value is assigned from the script before the first redraw, and
    the placeholder -- which carries no `>` -- still says what the box is for.
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


def _expect(presets):
    """{preset id: {kpi element id: the exact text the page prints}}.

    A preset's `label` says which network it is and no check here can read it.
    Its `expect` says what the page PRINTS once it is selected, tile by tile,
    and scripts/labcheck.js selects the option on the BUILT page, dispatches
    the menu's own change handler and compares getElementById(kpi).textContent
    against it. Every figure below was read off the running kit with
    `node scripts/labcheck.js --observe <page>`, never out of the code that
    computes it. See scripts/mathpath/AGENTS.md for the rule.

    Tiles are read with every OTHER control at the value the markup ships --
    the first-found rule, backward arcs off, the source and sink the preset
    names -- so a claim that only appears after the reader moves one of those
    cannot be pinned here. Those are named in a comment beside the preset that
    makes them.
    """
    return {p["id"]: dict(p.get("expect") or {}) for p in presets}


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "flowkit: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form. A flow computed on the network
# on screen is a fact about that network; the theorem is about all of them, and
# what makes the difference here is that the certificate travels with the
# answer. Spelled once so no mode can quietly drop it.
_CERTIFICATE = (
    "  /* Every number below came from running the algorithm on the network on\n"
    "     screen. What makes this course different from the rest of the path is\n"
    "     that the answer arrives with its own proof: a cut of the same capacity\n"
    "     as the flow's value. Where a page prints that equality it has computed\n"
    "     both sides separately, and where it prints a claim about every network\n"
    "     it enumerates the whole space at a cap it states. */\n"
)


# ---------------------------------------------------------------------------
# augment -- the residual network, and the arc that undoes a choice
# ---------------------------------------------------------------------------

_AG_PRESETS = [
    {
        "id": "forwardonly",
        "label": "four vertices, five arcs, every capacity 1",
        "spec": "1>2 1, 1>3 1, 2>3 1, 2>4 1, 3>4 1",
        "source": "1", "sink": "4",
        # Half of this preset's point is pinnable and half is not. The tiles are
        # read with agReverse at the value the markup ships (off), which is the
        # half that shows the rule stopping at 1 below a maximum of 2. "Put the
        # backward arcs in and the same rule reaches 2" is visible only after
        # the reader moves that control, so it is not pinned.
        "expect": {
            "agValue": "1",
            "agMax": "2",
        },
    },
    {
        "id": "classic",
        "label": "six vertices, capacities from 4 to 20",
        "spec": "1>2 16, 1>3 13, 2>3 10, 3>2 4, 2>4 12, 3>5 14, 4>3 9, 5>4 7, 4>6 20, 5>6 4",
        "source": "1", "sink": "6",
        "expect": {
            "agValue": "20",
            "agMax": "23",
            "agRounds": "5, against 3 for the shortest-path rule with backward arcs",
        },
    },
    {
        "id": "zigzag",
        "label": "one thin arc between two fat ones",
        "spec": "1>2 100, 1>3 100, 2>3 1, 2>4 100, 3>4 100",
        "source": "1", "sink": "4",
        # agRule ships at "dfs", the rule that walks into the thin arc, so that
        # is what these tiles are about. "The shortest-path rule ignores it" is
        # a claim about the OTHER value of that control and is not pinned; the
        # comparison in agRounds is as close as the shipped state gets.
        "expect": {
            "agValue": "199",
            "agMax": "200",
            "agRounds": "3, against 2 for the shortest-path rule with backward arcs",
        },
    },
    {
        "id": "parallel",
        "label": "two arcs between the same pair",
        "spec": "1>2 3, 1>2 4, 2>3 5",
        "source": "1", "sink": "3",
        "expect": {
            "agValue": "5",
            "agMax": "5",
            "agSat": "1 \u2192 2, 2 \u2192 3",
        },
    },
]


def _augment(cfg):
    chosen = _chosen(_AG_PRESETS, cfg)
    markup = (
        _toolbar(
            "Augmenting paths in the residual network",
            "a backward arc carries the flow already sent, so a later path can take it back",
            [("cyan", "on this augmenting path"), ("purple", "a backward arc"),
             ("red", "saturated, no residual left")],
        )
        + _stage(_svg("agPlot", "0 0 660 300",
                      "The network, each arc labelled with the flow it carries out of its "
                      "capacity.")
                 + _svg("agRes", "0 0 660 300",
                        "The residual network at this step, each arc labelled with what is left "
                        "on it, and the augmenting path drawn heavy."))
        + _table("agSteps")
        + _table("agFlow")
        + _banner("agStatus")
    )
    controls = (
        _select("agPreset", "Worked example", _options(_AG_PRESETS), chosen["id"])
        + _text("agSpec", "Arcs with capacities, as tail&gt;head c", chosen["spec"])
        + _range("agSource", "Source", 1, 10, chosen["source"])
        + _range("agSink", "Sink", 1, 10, chosen["sink"])
        + _select("agRule", "Choose each augmenting path by",
                  [("dfs", "the first one a search finds"),
                   ("bfs", "the shortest one, in arcs")], "dfs")
        + _select("agReverse", "Backward arcs in the residual network",
                  [("off", "leave them out"), ("on", "put them in")], "off")
        + _range("agStep", "Augmentation", 1, 40, 1)
        + _kpis([("Value this rule reaches", "agValue"),
                 ("The true maximum", "agMax"),
                 ("Augmentations used", "agRounds"),
                 ("Bottleneck pushed at this step", "agBottle"),
                 ("Is the result a flow at all", "agLegal"),
                 ("Arcs saturated at the end", "agSat")])
        + _hint(
            "agHint",
            "An arc is <span class=\"tt\">1&gt;2 16</span>: tail, head, capacity. The residual "
            "network holds a forward arc wherever capacity is left and a backward arc wherever "
            "flow has been sent; pushing along a backward arc <em>reduces</em> the flow on the arc "
            "it came from. Switch the backward arcs off and take the first path a search finds, and "
            "the algorithm stops below the maximum &mdash; that is the whole reason they are there.",
        )
    )
    script = _BASE_JS + _CERTIFICATE + _presets_js(
        "AGP", _AG_PRESETS, ["spec", "source", "sink"]) + r"""
  var presetIn = document.getElementById('agPreset'), specIn = document.getElementById('agSpec');
  var srcIn = document.getElementById('agSource'), srcOut = document.getElementById('agSourceOut');
  var sinkIn = document.getElementById('agSink'), sinkOut = document.getElementById('agSinkOut');
  var ruleIn = document.getElementById('agRule'), revIn = document.getElementById('agReverse');
  var stepIn = document.getElementById('agStep'), stepOut = document.getElementById('agStepOut');
  var plot = document.getElementById('agPlot'), resPlot = document.getElementById('agRes');
  var stepsT = document.getElementById('agSteps'), flowT = document.getElementById('agFlow');
  var status = document.getElementById('agStatus');
  var KPIS = ['agValue', 'agMax', 'agRounds', 'agBottle', 'agLegal', 'agSat'];

  function blank(why) {
    plot.innerHTML = ''; resPlot.innerHTML = ''; stepsT.innerHTML = ''; flowT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 16</span>: a tail, a head and a capacity.';
  }

  function redraw() {
    var parsed = fkParse(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    srcIn.max = n; sinkIn.max = n;
    var s = fkStep(parseInt(srcIn.value, 10) - 1, n);
    var t = fkStep(parseInt(sinkIn.value, 10) - 1, n);
    srcOut.textContent = String(s + 1);
    sinkOut.textContent = String(t + 1);
    if (s === t) { blank('the source and the sink are the same vertex'); return; }

    var opts = { rule: ruleIn.value, reverse: revIn.value === 'on' };
    var play = fkAugmentations(G, s, t, opts);
    var best = maxflow(G, s, t);
    stepIn.max = Math.max(1, play.steps.length);
    var k = fkStep(parseInt(stepIn.value, 10) - 1, play.steps.length);
    stepOut.textContent = (k + 1) + ' of ' + play.steps.length;
    var here = play.steps[k];

    var legal = fkCheckFlow(G, play.flow, s, t);
    var sat = saturatedArcs(G, play.flow);

    var colours = [], v;
    for (v = 0; v < n; v += 1) colours.push(v === s ? 3 : (v === t ? 4 : -1));
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                label: 'flow', flow: here.flow,
                                highlight: here.path
                                  ? here.path.map(function (rid) { return here.residual.meta[rid].from; })
                                  : sat,
                                colours: colours });
    var RG = here.residual.graph;
    resPlot.innerHTML = RG.arcs.length
      ? dgSvg(RG, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }), label: 'cap',
                    highlight: here.path || [], colours: colours })
      : '<text x="24" y="150" font-size="12" fill="var(--muted)">the residual network is empty: '
        + 'every arc is full and none carries anything back</text>';

    var rows = '';
    play.steps.forEach(function (st, i) {
      if (!st.path) {
        rows += '<tr class="' + (i === k ? 'tone-cyan' : '') + '"><th class="rowhead">'
          + (i + 1) + '</th><td>no path left</td><td>—</td><td>' + st.value + '</td><td>'
          + 'the search reached ' + fkNames(st.reachable) + ' and stopped</td></tr>';
        return;
      }
      var names = st.path.map(function (rid) {
        var meta = st.residual.meta[rid], a = st.residual.graph.arcs[rid];
        return (a.u + 1) + (meta.forward ? ' → ' : ' ⇠ ') + (a.v + 1);
      }).join(', ');
      rows += '<tr class="' + (i === k ? 'tone-cyan' : '') + '"><th class="rowhead">' + (i + 1)
        + '</th><td>' + names + '</td><td>' + st.bottleneck + '</td><td>' + st.valueAfter
        + '</td><td>' + (st.path.some(function (rid) { return !st.residual.meta[rid].forward; })
            ? '<span class="tone-purple">uses a backward arc, undoing an earlier push</span>'
            : 'forward arcs only') + '</td></tr>';
    });
    stepsT.innerHTML = '<caption>Every augmentation: the path in the residual network, the '
      + 'bottleneck pushed along it, and the value afterwards</caption><thead><tr><th>step</th>'
      + '<th>path</th><th>bottleneck</th><th>value after</th><th>what it used</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    var frows = '';
    G.arcs.forEach(function (a, id) {
      frows += '<tr' + (play.flow[id] === a.cap && a.cap > 0 ? ' class="tone-red"' : '')
        + '><th class="rowhead">' + fkArcName(a) + '</th><td>' + here.flow[id] + '</td><td>'
        + play.flow[id] + '</td><td>' + a.cap + '</td><td>' + (a.cap - play.flow[id]) + '</td><td>'
        + (play.flow[id] === a.cap && a.cap > 0 ? 'full'
            : play.flow[id] === 0 ? 'empty' : 'part full') + '</td></tr>';
    });
    flowT.innerHTML = '<caption>Every arc, at this step and at the end &mdash; the flow is an '
      + 'array with one entry per arc, which is why two arcs between one pair are two '
      + 'numbers</caption><thead><tr><th>arc</th><th>flow here</th><th>flow at the end</th>'
      + '<th>capacity</th><th>spare</th><th>state</th></tr></thead><tbody>' + frows + '</tbody>';

    document.getElementById('agValue').textContent = play.value;
    document.getElementById('agMax').textContent = best.result.value;
    document.getElementById('agRounds').textContent = play.augmentations + ', against '
      + best.result.augmentations + ' for the shortest-path rule with backward arcs';
    document.getElementById('agBottle').textContent = here.path ? here.bottleneck : 'none left';
    document.getElementById('agLegal').textContent = legal.ok
      ? 'yes: conserved and inside every capacity'
      : (legal.violated.length ? 'no, conservation fails at ' + fkNames(legal.violated)
          : 'no, an arc is over capacity');
    document.getElementById('agSat').textContent = sat.length
      ? sat.map(function (id) { return fkArcName(G.arcs[id]); }).join(', ') : 'none';

    var stuck = play.value < best.result.value;
    var last = play.steps[play.steps.length - 1];
    var usedBack = play.steps.some(function (st) {
      return st.path && st.path.some(function (rid) { return !st.residual.meta[rid].forward; });
    });
    status.innerHTML = '<strong>Value ' + play.value + ' after ' + play.augmentations
      + ' augmentation' + fkPlural(play.augmentations, '', 's') + '</strong>'
      + (stuck
          ? ', and the true maximum is <span class="tone-red">' + best.result.value + '</span>. '
            + 'This run is <span class="tone-red">stuck below it</span>. '
          : ', which is the maximum. ')
      + (revIn.value === 'off'
          ? 'Backward arcs are switched off, so the residual network holds only spare capacity and '
            + 'nothing that carries flow back. '
            + (stuck
                ? 'The search now reaches only ' + fkNames(last.reachable) + ' and there is no path '
                  + 'to the sink &mdash; yet no arc out of the source is full, so nothing about the '
                  + 'capacities has stopped it. What has stopped it is a choice made earlier that '
                  + 'cannot be taken back. Switch the backward arcs on and watch the same rule '
                  + 'finish.'
                : 'On this network and with this rule it happened to reach the maximum anyway, '
                  + 'which is luck: switch the path rule to the first one found and try again.')
          : 'Backward arcs are in, and '
            + (usedBack
                ? '<span class="tone-purple">at least one augmentation used one</span> &mdash; that '
                  + 'push reduced the flow on an arc an earlier push had loaded. Undoing a choice is '
                  + 'not an optimisation here; it is the reason the algorithm is correct. '
                : 'no augmentation needed one on this network, so try the four-vertex example with '
                  + 'the first-found rule. ')
            + 'The search finally reached ' + fkNames(last.reachable) + ' and no further, and that '
            + 'set is a cut whose capacity equals the value. ')
      + 'The flow was checked rather than assumed: conservation at every interior vertex and every '
      + 'arc against its capacity, and it is <span class="' + (legal.ok ? 'tone-green">a flow'
          : 'tone-red">not a flow, which would be a defect') + '</span>. '
      + 'Vocabulary, once, because another subject uses it for the same objects: this is a residual '
      + '<em>network</em>, those are backward <em>arcs</em>, an <em>arc</em> is a directed edge and '
      + 'the circles are <em>nodes</em>.';
  }

  function apply() {
    var p = AGP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; srcIn.value = p.source; sinkIn.value = p.sink; stepIn.value = '1';
    redraw();
  }
  var START = AGP[presetIn.value];
  if (START && !specIn.value) {
    specIn.value = START.spec; srcIn.value = START.source; sinkIn.value = START.sink;
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  sinkIn.addEventListener('input', redraw);
  ruleIn.addEventListener('change', redraw);
  revIn.addEventListener('change', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Maximum flow by augmenting paths",
        subtitle="The residual network carries the flow already sent, so a later path can take it back",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the network, then switch the backward arcs off"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each augmentation is one row: the path through the residual network, the bottleneck "
            "pushed along it, and the value afterwards. The result is checked against the maximum "
            "the shortest-path rule reaches with backward arcs in place.",
        ),
        script=script,
        expect={"agPreset": _expect(_AG_PRESETS)},
    )


# ---------------------------------------------------------------------------
# mincut -- the certificate, against every cut there is
# ---------------------------------------------------------------------------

_MC_PRESETS = [
    {
        "id": "classic",
        "label": "six vertices and ten arcs, capacities from 4 to 20",
        "spec": "1>2 16, 1>3 13, 2>3 10, 3>2 4, 2>4 12, 3>5 14, 4>3 9, 5>4 7, 4>6 20, 5>6 4",
        "source": "1", "sink": "6",
        "expect": {
            "mcValue": "23",
            "mcCap": "23 \u2014 equal",
            "mcCount": "16, of which 1 tie at the smallest",
        },
    },
    {
        "id": "saturated",
        "label": "a path of three arcs beside a direct one",
        "spec": "1>2 1, 2>3 1, 3>4 5, 1>4 1",
        "source": "1", "sink": "4",
        # mcSat is the tile this preset exists for: three arcs end up full and
        # only two of them are in the cut, so "saturated" and "in the minimum
        # cut" are shown to be different properties by a count rather than by a
        # sentence. WHICH arc is the odd one out is drawn, not printed, so it
        # cannot be pinned.
        "expect": {
            "mcValue": "2",
            "mcSat": "3 full, 2 in the cut",
        },
    },
    {
        "id": "manycuts",
        "label": "a chain of three arcs, each of capacity 1",
        "spec": "1>2 1, 2>3 1, 3>4 1",
        "source": "1", "sink": "4",
        "expect": {
            "mcValue": "1",
            "mcCount": "4, of which 3 tie at the smallest",
        },
    },
    {
        "id": "backwards",
        "label": "five arcs, one of them pointing back from 3 to 2",
        "spec": "1>2 5, 2>3 5, 3>2 9, 3>4 5, 2>4 1",
        "source": "1", "sink": "4",
        "expect": {
            "mcValue": "5",
            "mcCap": "5 \u2014 equal",
            "mcSat": "2 full, 1 in the cut",
        },
    },
]

_MC_CAP = 10


def _mincut(cfg):
    chosen = _chosen(_MC_PRESETS, cfg)
    markup = (
        _toolbar(
            "The reachable set is the cut, and its capacity is the flow",
            "two numbers computed separately, and they are equal",
            [("cyan", "reachable from the source in the residual network"),
             ("red", "an arc of the cut"), ("purple", "full, but in no cut")],
        )
        + _stage(_svg("mcPlot", "0 0 660 300",
                      "The network with the reachable set filled and the arcs of the cut drawn "
                      "heavy.")
                 + _svg("mcBars", "0 0 660 140",
                        "Every cut of this network as one bar of its capacity, sorted, with the "
                        "smallest marked."))
        + _table("mcArcs")
        + _table("mcCuts")
        + _banner("mcStatus")
    )
    controls = (
        _select("mcPreset", "Worked example", _options(_MC_PRESETS), chosen["id"])
        + _text("mcSpec", "Arcs with capacities, as tail&gt;head c", chosen["spec"])
        + _range("mcSource", "Source", 1, 10, chosen["source"])
        + _range("mcSink", "Sink", 1, 10, chosen["sink"])
        + _kpis([("The maximum flow's value", "mcValue"),
                 ("The capacity of the cut it returns", "mcCap"),
                 ("Smallest capacity over every cut", "mcBrute"),
                 ("Cuts enumerated, and how many tie", "mcCount"),
                 ("Full arcs, and how many are in the cut", "mcSat"),
                 ("Augmentations, against V times E", "mcRounds")])
        + _hint(
            "mcHint",
            "A cut is a set of vertices holding the source and not the sink, and its capacity is "
            "the total capacity of the arcs <em>leaving</em> it &mdash; arcs coming back in "
            "contribute nothing, which is the part most often got wrong. Every such set is "
            "enumerated below, so the theorem is a comparison of two numbers this page worked out "
            "separately rather than a sentence you are asked to accept.",
        )
    )
    script = _ORACLE_JS + _CERTIFICATE + _presets_js(
        "MCP", _MC_PRESETS, ["spec", "source", "sink"]) + r"""
  var presetIn = document.getElementById('mcPreset'), specIn = document.getElementById('mcSpec');
  var srcIn = document.getElementById('mcSource'), srcOut = document.getElementById('mcSourceOut');
  var sinkIn = document.getElementById('mcSink'), sinkOut = document.getElementById('mcSinkOut');
  var plot = document.getElementById('mcPlot'), bars = document.getElementById('mcBars');
  var arcsT = document.getElementById('mcArcs'), cutsT = document.getElementById('mcCuts');
  var status = document.getElementById('mcStatus');
  var KPIS = ['mcValue', 'mcCap', 'mcBrute', 'mcCount', 'mcSat', 'mcRounds'];
  var CAP = """ + str(_MC_CAP) + r""";

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; arcsT.innerHTML = ''; cutsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 16</span>: a tail, a head and a capacity.';
  }

  /* Every cut as one bar, sorted by capacity: the smallest ones are the block on
     the left, and how many of them there are answers whether the cut is unique. */
  function cutBars(cuts, best) {
    var sorted = cuts.slice().sort(function (a, b) { return a.capacity - b.capacity; });
    var top = sorted.length ? sorted[sorted.length - 1].capacity : 1;
    var w = Math.max(2, Math.min(18, Math.floor(600 / Math.max(1, sorted.length))));
    var s = '', i;
    for (i = 0; i < sorted.length; i += 1) {
      var h = Math.max(3, (sorted[i].capacity / Math.max(1, top)) * 96);
      s += '<rect x="' + (28 + i * w).toFixed(1) + '" y="' + (114 - h).toFixed(1) + '" width="'
        + Math.max(1, w - 1) + '" height="' + h.toFixed(1) + '" fill="var('
        + (sorted[i].capacity === best ? '--red' : '--line-strong') + ')" opacity="'
        + (sorted[i].capacity === best ? '0.95' : '0.45') + '" />';
    }
    s += '<line x1="28" y1="114" x2="648" y2="114" stroke="var(--line-strong)" />';
    s += '<text x="28" y="130" font-size="11" fill="var(--red)">smallest ' + best + '</text>';
    s += '<text x="648" y="130" text-anchor="end" font-size="11" fill="var(--muted)">largest '
      + top + '</text>';
    s += '<text x="28" y="16" font-size="11" fill="var(--muted)">' + sorted.length
      + ' cuts, sorted by capacity</text>';
    return s;
  }

  function redraw() {
    var parsed = fkParse(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    srcIn.max = n; sinkIn.max = n;
    var s = fkStep(parseInt(srcIn.value, 10) - 1, n);
    var t = fkStep(parseInt(sinkIn.value, 10) - 1, n);
    srcOut.textContent = String(s + 1);
    sinkOut.textContent = String(t + 1);
    if (s === t) { blank('the source and the sink are the same vertex'); return; }

    var run = maxflow(G, s, t), f = run.result.flow;
    var cut = minCutFrom(G, f, s);
    var brute = null, refused = null;
    try { brute = minCutBrute(G, s, t, CAP); }
    catch (err) { refused = err.message; }
    var sat = saturatedArcs(G, f);
    var inCut = {};
    cut.arcs.forEach(function (e) { inCut[e.id] = true; });
    var satNotInCut = sat.filter(function (id) { return !inCut[id]; });
    var without = reachesWithout(G, satNotInCut, s, t);

    var inS = {};
    cut.S.forEach(function (v) { inS[v] = true; });
    var colours = [], v;
    for (v = 0; v < n; v += 1) colours.push(inS[v] ? 0 : -1);
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 150, radius: 118 }),
                                label: 'flow', flow: f, colours: colours,
                                highlight: cut.arcs.map(function (e) { return e.id; }) });
    bars.innerHTML = brute
      ? cutBars(brute.result.cuts, brute.result.capacity)
      : '<text x="28" y="70" font-size="12" fill="var(--muted)">' + refused + '</text>';

    var arows = '';
    G.arcs.forEach(function (a, id) {
      var full = a.cap > 0 && f[id] === a.cap;
      arows += '<tr class="' + (inCut[id] ? 'tone-red' : (full ? 'tone-purple' : '')) + '">'
        + '<th class="rowhead">' + fkArcName(a) + '</th><td>' + f[id] + ' of ' + a.cap + '</td><td>'
        + (inS[a.u] ? 'in the set' : 'outside') + ' → ' + (inS[a.v] ? 'in the set' : 'outside')
        + '</td><td>' + (inCut[id] ? 'leaves the set: counted'
            : (!inS[a.u] && inS[a.v]) ? 'comes back in: counted as nothing'
            : 'both ends on one side') + '</td><td>' + (full ? 'full' : 'has ' + (a.cap - f[id])
            + ' spare') + '</td></tr>';
    });
    arcsT.innerHTML = '<caption>Every arc against the cut: which side each end is on, whether it '
      + 'counts, and whether it is full</caption><thead><tr><th>arc</th><th>flow</th>'
      + '<th>ends</th><th>contribution to the capacity</th><th>state</th></tr></thead><tbody>'
      + arows + '</tbody>';

    var crows = '';
    if (brute) {
      var sortedCuts = brute.result.cuts.slice().sort(function (a, b) {
        return a.capacity - b.capacity || a.S.length - b.S.length; });
      sortedCuts.slice(0, 8).forEach(function (c) {
        crows += '<tr' + (c.capacity === brute.result.capacity ? ' class="tone-red"' : '')
          + '><th class="rowhead">{' + fkNames(c.S) + '}</th><td>' + c.capacity + '</td><td>'
          + c.back + '</td><td>' + (c.capacity === brute.result.capacity ? 'one of the smallest'
              + (cutIsMinimum(brute, cut.S) && c.S.join(',') === cut.S.join(',')
                  ? ', and the one the algorithm returned' : '')
              : (c.capacity - brute.result.capacity) + ' above the smallest') + '</td></tr>';
      });
      if (sortedCuts.length > 8) {
        crows += '<tr><th class="rowhead">and ' + (sortedCuts.length - 8) + ' more</th>'
          + '<td colspan="3">every remaining set has capacity at least '
          + sortedCuts[8].capacity + '</td></tr>';
      }
    }
    cutsT.innerHTML = '<caption>Every set holding the source and not the sink, smallest '
      + 'first</caption><thead><tr><th>the set</th><th>capacity leaving it</th>'
      + '<th>capacity coming back in</th><th>where it stands</th></tr></thead><tbody>'
      + (crows || '<tr><td colspan="4">' + refused + '</td></tr>') + '</tbody>';

    var ties = brute ? brute.result.minimal.length : 0;
    document.getElementById('mcValue').textContent = run.result.value;
    document.getElementById('mcCap').textContent = cut.capacity
      + (cut.capacity === run.result.value ? ' — equal' : ' — not equal, report it');
    document.getElementById('mcBrute').textContent = brute ? String(brute.result.capacity)
      : 'refused above ' + CAP + ' vertices';
    document.getElementById('mcCount').textContent = brute
      ? brute.result.count + ', of which ' + ties + ' tie at the smallest' : '—';
    document.getElementById('mcSat').textContent = sat.length + ' full, ' + cut.arcs.length
      + ' in the cut';
    document.getElementById('mcRounds').textContent = run.result.augmentations + ', against '
      + (n * G.arcs.length) + ' for V times E';

    var equal = cut.capacity === run.result.value;
    var bruteEqual = brute ? brute.result.capacity === run.result.value : null;
    status.innerHTML = '<strong>Flow ' + run.result.value + ', cut ' + cut.capacity + '</strong>'
      + (equal ? ' &mdash; <span class="tone-green">equal</span>, and that equality is the '
          + 'certificate: no flow can exceed any cut, so a flow that meets one is maximum and the '
          + 'cut proves it. '
        : ' &mdash; <span class="tone-red">not equal, which cannot happen</span>. ')
      + 'The set is {<span class="tone-cyan">' + fkNames(cut.S) + '</span>}, and it was not chosen: '
      + 'it is everything still reachable from the source once no augmenting path remains. '
      + (brute
          ? 'All <span class="tone-purple">' + brute.result.count + '</span> sets holding the source '
            + 'and not the sink were then listed, and the smallest capacity among them is '
            + '<span class="' + (bruteEqual ? 'tone-green' : 'tone-red') + '">'
            + brute.result.capacity + '</span>'
            + (bruteEqual ? ', which is the flow value again, by a third route. ' : '. ')
            + (ties > 1
                ? 'There are ' + ties + ' sets of that capacity, so the minimum cut is not unique '
                  + 'either &mdash; the algorithm returns one of them, and '
                  + (cutIsMinimum(brute, cut.S)
                      ? 'the one it returned is among the smallest.'
                      : '<span class="tone-red">the one it returned is not among them.</span>')
                + ' '
                : 'It is the only set of that capacity here. ')
          : '<span class="tone-amber">The enumeration is refused on this network: ' + refused
            + '.</span> ')
      + 'Every arc of the cut is full &mdash; it has to be, or the search would have crossed it '
      + '&mdash; but <span class="tone-purple">' + sat.length + ' arc'
      + fkPlural(sat.length, ' is', 's are') + ' full</span> in all against '
      + cut.arcs.length + ' in the cut. '
      + (satNotInCut.length
          ? 'So the full arcs are NOT the cut: ' + satNotInCut.map(function (id) {
              return fkArcName(G.arcs[id]); }).join(', ')
            + ' ' + fkPlural(satNotInCut.length, 'is', 'are') + ' full and in no cut at all, and '
            + 'deleting ' + fkPlural(satNotInCut.length, 'it', 'them') + ' leaves the sink '
            + (without.reaches
                ? '<span class="tone-purple">still reachable</span> from the source. Being full is '
                  + 'a fact about one arc; being a cut is a fact about a set.'
                : 'unreachable, which on this network makes them a cut as well — edit a '
                  + 'capacity and the two come apart.')
          : 'On this network every full arc happens to be in the cut, which is a fact about this '
            + 'network: try the example with the full arc buried inside the set.')
      + ' Choosing the shortest augmenting path each time kept the number of augmentations at '
      + run.result.augmentations + ' here, and the reason it is bounded at all is that the shortest '
      + 'distance from the source to the sink in the residual network never falls: it is what stops '
      + 'the same arc being saturated again and again. One sentence on the cheapest flow of a given '
      + 'value, which this page does not develop: augment along the cheapest residual path instead '
      + 'of the shortest, and the flow stays cheapest for its value.';
  }

  function apply() {
    var p = MCP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; srcIn.value = p.source; sinkIn.value = p.sink;
    redraw();
  }
  var START = MCP[presetIn.value];
  if (START && !specIn.value) {
    specIn.value = START.spec; srcIn.value = START.source; sinkIn.value = START.sink;
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  sinkIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Max-flow min-cut, with the cut enumerated",
        subtitle="The residual-reachable set is a cut of the same capacity, and every other cut is at least as large",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the network and read the certificate"),
        panel_intro=cfg.get(
            "panel_intro",
            "The flow's value and the cut's capacity are computed separately and compared. Every "
            "set holding the source and not the sink is then enumerated, so the claim that no cut "
            "is smaller is a fact about a list.",
        ),
        script=script,
        expect={"mcPreset": _expect(_MC_PRESETS)},
    )


# ---------------------------------------------------------------------------
# matching -- the same computation with unit capacities, and Koenig's theorem
# ---------------------------------------------------------------------------

_MT_PRESETS = [
    {
        "id": "maximal",
        "label": "two on each side, three pairs",
        "left": "2", "right": "2", "pairs": "2-2, 1-2, 2-1",
        "expect": {
            "mtSize": "2 of 3 pairs",
            "mtGreedy": "1 \u2014 maximal, not maximum",
        },
    },
    {
        "id": "perfect",
        "label": "three on each side, six pairs",
        "left": "3", "right": "3", "pairs": "1-1, 1-2, 2-2, 2-3, 3-1, 3-3",
        "expect": {
            "mtSize": "3 of 6 pairs",
            "mtCover": "3 \u2014 equal",
            "mtHall": "holds: every left vertex is matched",
        },
    },
    {
        "id": "hall",
        "label": "three on the left competing for two",
        "left": "3", "right": "2", "pairs": "1-1, 2-1, 3-1, 3-2",
        "expect": {
            "mtSize": "2 of 4 pairs",
            "mtHall": "fails at {1, 2}",
        },
    },
    {
        "id": "star",
        "label": "one popular right vertex",
        "left": "4", "right": "4", "pairs": "1-1, 2-1, 3-1, 4-1, 4-4",
        "expect": {
            "mtSize": "2 of 5 pairs",
            "mtCover": "2 \u2014 equal",
            "mtHall": "fails at {1, 2, 3}",
        },
    },
]

_MT_CAP = 16


def _matching(cfg):
    chosen = _chosen(_MT_PRESETS, cfg)
    markup = (
        _toolbar(
            "Matching as a flow, and the cut as a cover",
            "unit capacities make the flow whole, and the cut names the cover",
            [("cyan", "matched"), ("red", "in the vertex cover"),
             ("purple", "a pair left unmatched")],
        )
        + _stage(_svg("mtPlot", "0 0 660 260",
                      "The two sides with every allowed pair drawn, and the matched pairs drawn "
                      "heavy.")
                 + _svg("mtNet", "0 0 660 280",
                        "The flow network built from it: a source, the left side, the right side "
                        "and a sink, every capacity one."))
        + _table("mtRows")
        + _table("mtCompare")
        + _banner("mtStatus")
    )
    controls = (
        _select("mtPreset", "Worked example", _options(_MT_PRESETS), chosen["id"])
        + _range("mtLeft", "Vertices on the left", 2, 4, chosen["left"])
        + _range("mtRight", "Vertices on the right", 2, 4, chosen["right"])
        + _text("mtPairs", "Allowed pairs, as left&minus;right", chosen["pairs"])
        + _kpis([("Size of the maximum matching", "mtSize"),
                 ("Size of the cover read off the cut", "mtCover"),
                 ("Maximum over every subset of the pairs", "mtBrute"),
                 ("A greedy maximal matching", "mtGreedy"),
                 ("Is every flow value a whole number", "mtWhole"),
                 ("Hall's condition", "mtHall")])
        + _hint(
            "mtHint",
            "A pair is <span class=\"tt\">2&minus;1</span>: the second vertex on the left with the "
            "first on the right. Every arc of the network gets capacity one, so an augmenting path "
            "has a bottleneck of one and moves a whole unit &mdash; which is why the answer is a "
            "matching and not a fraction of one. The minimum cut is then read back as a set of "
            "vertices covering every pair, and the two sizes agree; that is a theorem, checked here "
            "on your own instance.",
        )
    )
    script = _ORACLE_JS + _CERTIFICATE + _presets_js(
        "MTP", _MT_PRESETS, ["left", "right", "pairs"]) + r"""
  var presetIn = document.getElementById('mtPreset');
  var leftIn = document.getElementById('mtLeft'), leftOut = document.getElementById('mtLeftOut');
  var rightIn = document.getElementById('mtRight'), rightOut = document.getElementById('mtRightOut');
  var pairsIn = document.getElementById('mtPairs');
  var plot = document.getElementById('mtPlot'), net = document.getElementById('mtNet');
  var pairsT = document.getElementById('mtRows'), cmpT = document.getElementById('mtCompare');
  var status = document.getElementById('mtStatus');
  var KPIS = ['mtSize', 'mtCover', 'mtBrute', 'mtGreedy', 'mtWhole', 'mtHall'];
  var CAP = """ + str(_MT_CAP) + r""";

  function blank(why) {
    plot.innerHTML = ''; net.innerHTML = ''; pairsT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A pair is '
      + '<span class="tt">2-1</span>: a left label and a right label.';
  }

  /* The bipartite instance itself, as a graph with the two sides in two columns
     -- drawn with the shared renderer over dgLayered, so the picture of the
     instance and the picture of the network it becomes are the same code. */
  function bipartiteGraph(left, right, pairs) {
    var B = dgNew(left + right, true);
    pairs.forEach(function (p) { dgAdd(B, p[0], left + p[1], 0, 1); });
    return B;
  }

  function redraw() {
    var left = fkStep(parseInt(leftIn.value, 10) - 2, 3) + 2;
    var right = fkStep(parseInt(rightIn.value, 10) - 2, 3) + 2;
    leftOut.textContent = String(left);
    rightOut.textContent = String(right);
    var parsed = fkParsePairs(pairsIn.value, left, right);
    if (parsed.bad) { blank(parsed.bad); return; }
    var pairs = parsed.pairs;

    var netObj = matchingNetwork(left, right, pairs);
    var run = maxflow(netObj.graph, netObj.s, netObj.t);
    var f = run.result.flow;
    var matching = matchingFrom(netObj, f);
    var cover = konigCover(netObj, f);
    var greedy = greedyMatching(pairs);
    var brute = null, refused = null;
    try { brute = matchingBrute(pairs, CAP); }
    catch (err) { refused = err.message; }
    var hall = hallDeficient(netObj, f, pairs);
    var whole = f.every(function (x) { return x === Math.round(x); });

    var matchedPair = {};
    matching.forEach(function (m) { matchedPair[m.left + '-' + m.right] = true; });
    var inCover = { left: {}, right: {} };
    cover.cover.forEach(function (c) { inCover[c.side][c.v] = true; });

    var B = bipartiteGraph(left, right, pairs);
    var bLayers = [[], []], i;
    for (i = 0; i < left; i += 1) bLayers[0].push(i);
    for (i = 0; i < right; i += 1) bLayers[1].push(left + i);
    var bLabels = [], bColours = [];
    for (i = 0; i < left; i += 1) { bLabels.push('L' + (i + 1)); bColours.push(inCover.left[i] ? 4 : -1); }
    for (i = 0; i < right; i += 1) { bLabels.push('R' + (i + 1)); bColours.push(inCover.right[i] ? 4 : -1); }
    var bHigh = [];
    B.arcs.forEach(function (a, id) {
      if (matchedPair[a.u + '-' + (a.v - left)]) bHigh.push(id);
    });
    plot.innerHTML = dgSvg(B, { points: dgLayered(left + right, bLayers, { width: 600, height: 250 }),
                                label: 'none', labels: bLabels, colours: bColours,
                                highlight: bHigh });

    var NG = netObj.graph;
    var nLayers = [[netObj.s], bLayers[0], bLayers[1], [netObj.t]];
    var nLabels = bLabels.concat(['s', 't']);
    var nColours = bColours.concat([3, 3]);
    net.innerHTML = dgSvg(NG, { points: dgLayered(NG.n, nLayers, { width: 600, height: 260 }),
                                label: 'flow', flow: f, labels: nLabels, colours: nColours,
                                highlight: netObj.middle.filter(function (id) { return f[id] > 0; }) });

    var prows = '';
    pairs.forEach(function (p, id) {
      var greedyHas = greedy.some(function (g) { return g.id === id; });
      prows += '<tr class="' + (matchedPair[p[0] + '-' + p[1]] ? 'tone-cyan' : '') + '">'
        + '<th class="rowhead">L' + (p[0] + 1) + ' with R' + (p[1] + 1) + '</th><td>'
        + (matchedPair[p[0] + '-' + p[1]] ? 'matched' : 'not matched') + '</td><td>'
        + (greedyHas ? 'taken by the greedy pass' : 'left by the greedy pass') + '</td><td>'
        + (inCover.left[p[0]] ? 'L' + (p[0] + 1) : (inCover.right[p[1]] ? 'R' + (p[1] + 1)
            : 'nothing — report it')) + '</td></tr>';
    });
    pairsT.innerHTML = '<caption>Every allowed pair: whether the maximum matching uses it, '
      + 'whether a greedy pass took it, and which cover vertex covers it</caption><thead><tr>'
      + '<th>pair</th><th>in the matching</th><th>greedy</th><th>covered by</th></tr></thead>'
      + '<tbody>' + prows + '</tbody>';

    cmpT.innerHTML = '<caption>Four answers to the same question, and where each one comes '
      + 'from</caption><thead><tr><th>method</th><th>size</th><th>what it knows about</th>'
      + '</tr></thead><tbody>'
      + '<tr><th class="rowhead">maximum flow with unit capacities</th><td class="tone-cyan">'
      + run.result.value + '</td><td>augmenting paths, and nothing about matchings</td></tr>'
      + '<tr><th class="rowhead">the cut read as a vertex cover</th><td class="tone-cyan">'
      + cover.size + '</td><td>the residual-reachable set, and nothing else</td></tr>'
      + '<tr><th class="rowhead">every subset of the pairs</th><td class="tone-cyan">'
      + (brute ? brute.result.value : refused) + '</td><td>'
      + (brute ? brute.counts.nodes + ' subsets tried, and no flow network at all' : '—')
      + '</td></tr>'
      + '<tr><th class="rowhead">a greedy pass in the order typed</th><td class="tone-purple">'
      + greedy.length + '</td><td>only whether both ends are free</td></tr></tbody>';

    document.getElementById('mtSize').textContent = matching.length + ' of ' + pairs.length
      + ' pairs';
    document.getElementById('mtCover').textContent = cover.size
      + (cover.size === matching.length ? ' — equal' : ' — not equal, report it');
    document.getElementById('mtBrute').textContent = brute
      ? brute.result.value + (brute.result.value === matching.length ? ' — equal' : ' — report it')
      : 'refused above ' + CAP + ' pairs';
    document.getElementById('mtGreedy').textContent = greedy.length
      + (greedy.length < matching.length ? ' — maximal, not maximum' : ' — maximum here too');
    document.getElementById('mtWhole').textContent = whole ? 'yes, every one' : 'no — report it';
    document.getElementById('mtHall').textContent = matching.length === left
      ? 'holds: every left vertex is matched'
      : (hall.deficient ? 'fails at {' + fkNames(hall.S) + '}' : 'no deficient set found');

    var agree = cover.size === matching.length;
    var bruteAgree = brute ? brute.result.value === matching.length : null;
    status.innerHTML = '<strong>Matching ' + matching.length + ', cover ' + cover.size
      + '</strong>' + (agree
          ? ' &mdash; <span class="tone-green">the same number</span>, which is the theorem: no '
            + 'cover can be smaller than a matching, since each matched pair needs its own cover '
            + 'vertex, so a cover that meets one proves both are extreme. '
          : ' &mdash; <span class="tone-red">not the same, which cannot happen.</span> ')
      + 'The matching was not searched for directly: it is the middle layer of a maximum flow, and '
      + 'every capacity in that network is 1, so an augmenting path has a bottleneck of 1 and moves '
      + 'a whole unit. That is why the answer is a matching and not a half of one &mdash; every '
      + 'flow value here is <span class="' + (whole ? 'tone-green">a whole number'
          : 'tone-red">not whole, which cannot happen') + '</span>. '
      + (brute
          ? 'All ' + brute.counts.nodes + ' subsets of the ' + pairs.length + ' pairs were then '
            + 'tried, keeping the largest with no shared end, and the biggest is <span class="'
            + (bruteAgree ? 'tone-green' : 'tone-red') + '">' + brute.result.value + '</span>'
            + (bruteAgree ? ' &mdash; the same again, by a route with no network in it. ' : '. ')
          : '<span class="tone-amber">The enumeration is refused here: ' + refused + '.</span> ')
      + (greedy.length < matching.length
          ? 'A greedy pass in the order you typed produced <span class="tone-purple">'
            + greedy.length + '</span> pair' + fkPlural(greedy.length, '', 's') + ', and nothing '
            + 'can be added to it &mdash; every remaining pair has an end already used. It is '
            + 'MAXIMAL and not maximum, and the difference is an augmenting path: the flow found '
            + 'one that reroutes an earlier choice, which a greedy pass has no way to do. '
          : 'A greedy pass reached the same size here, which is a fact about the order the pairs '
            + 'were typed in rather than about greed: reorder them and watch it fall behind. ')
      + (matching.length === left
          ? 'Every left vertex is matched, so Hall’s condition holds on this instance.'
          : (hall.deficient
              ? 'The matching leaves ' + (left - matching.length) + ' left vert'
                + fkPlural(left - matching.length, 'ex', 'ices') + ' unmatched, and the source side '
                + 'of the cut says why: the set {<span class="tone-red">' + fkNames(hall.S)
                + '</span>} on the left reaches only {' + fkNames(hall.neighbours) + '} on the '
                + 'right &mdash; ' + hall.S.length + ' vertices competing for '
                + hall.neighbours.length + ', short by ' + hall.deficiency + '. That set is not '
                + 'searched for either; it is read off the same cut.'
              : 'The matching is imperfect and no deficient set was read off the cut, which cannot '
                + 'happen — report it.'));
  }

  function apply() {
    var p = MTP[presetIn.value];
    if (!p) return;
    leftIn.value = p.left; rightIn.value = p.right; pairsIn.value = p.pairs;
    redraw();
  }
  var START = MTP[presetIn.value];
  if (START && !pairsIn.value) {
    leftIn.value = START.left; rightIn.value = START.right; pairsIn.value = START.pairs;
  }
  presetIn.addEventListener('change', apply);
  leftIn.addEventListener('input', redraw);
  rightIn.addEventListener('input', redraw);
  pairsIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Bipartite matching as a flow, and the cover the cut names",
        subtitle="Unit capacities make the answer whole, and the minimum cut is a vertex cover of the same size",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the pairs; the network is built from them"),
        panel_intro=cfg.get(
            "panel_intro",
            "The matching is the middle layer of a maximum flow, and the cover is read off the same "
            "cut. Both are compared with a search over every subset of the pairs, which knows "
            "nothing about flow, and with a greedy pass that stops too early.",
        ),
        script=script,
        expect={"mtPreset": _expect(_MT_PRESETS)},
    )


# ---------------------------------------------------------------------------
# gadget -- the graph is transformed, the algorithm is not
# ---------------------------------------------------------------------------

_GD_PRESETS = [
    {
        "id": "uncapped",
        "label": "split every vertex, with no vertex actually capped",
        "kind": "split",
        "spec": "1>2 5, 1>3 4, 2>4 3, 3>4 6, 2>3 2",
        "caps": "",
        "source": "1", "sink": "4",
        "expect": {
            "gdAfter": "8 and 9",
            "gdValue": "9",
            "gdCheck": "uncapped, and it gives the original answer",
        },
    },
    {
        "id": "capped",
        "label": "the same network with one vertex capped",
        "kind": "split",
        "spec": "1>2 5, 1>3 4, 2>4 3, 3>4 6, 2>3 2",
        "caps": "3:2",
        "source": "1", "sink": "4",
        "expect": {
            "gdValue": "5",
            "gdCheck": "capping cannot raise the answer, and it did not",
        },
    },
    {
        "id": "disjoint",
        "label": "six arcs, every capacity set to 1",
        "kind": "unit",
        "spec": "1>2 9, 1>3 9, 2>4 9, 3>4 9, 2>3 9, 1>4 9",
        "caps": "",
        "source": "1", "sink": "4",
        "expect": {
            "gdValue": "3",
            "gdCheck": "3 routes walked out of the flow, matching its value",
        },
    },
    {
        "id": "many",
        "label": "two places it starts and two it ends",
        "kind": "supersource",
        "spec": "1>3 4, 2>3 3, 3>4 5, 3>5 4",
        "caps": "",
        "source": "1", "sink": "4",
        "expect": {
            "gdBefore": "5 and 4",
            "gdAfter": "7 and 8",
            "gdValue": "7",
        },
    },
]


def _gadget(cfg):
    chosen = _chosen(_GD_PRESETS, cfg)
    markup = (
        _toolbar(
            "The network is transformed and the algorithm is untouched",
            "a constraint becomes a capacity, and the answer reads back",
            [("cyan", "an arc of the original"), ("purple", "an arc the gadget added"),
             ("red", "the cut of the transformed network")],
        )
        + _stage(_svg("gdPlot", "0 0 660 260",
                      "The original network as typed.")
                 + _svg("gdNew", "0 0 660 300",
                        "The transformed network, solved, with the arcs the gadget added drawn "
                        "differently."))
        + _table("gdMap")
        + _table("gdResult")
        + _banner("gdStatus")
    )
    controls = (
        _select("gdPreset", "Worked example", _options(_GD_PRESETS), chosen["id"])
        + _select("gdKind", "The transformation",
                  [("split", "a capacity on what passes through a vertex"),
                   ("unit", "routes that share no arc"),
                   ("supersource", "several starts and several ends")], chosen["kind"])
        + _text("gdSpec", "Arcs with capacities, as tail&gt;head c", chosen["spec"])
        + _text("gdCaps", "Vertex capacities, as vertex:capacity", chosen["caps"] or "3:2")
        + _range("gdSource", "Source", 1, 10, chosen["source"])
        + _range("gdSink", "Sink", 1, 10, chosen["sink"])
        + _kpis([("Vertices and arcs before", "gdBefore"),
                 ("Vertices and arcs after", "gdAfter"),
                 ("The transformed network's value", "gdValue"),
                 ("What that means in the original", "gdMeans"),
                 ("Smallest cut over every set", "gdCut"),
                 ("The check this gadget carries", "gdCheck")])
        + _hint(
            "gdHint",
            "Splitting a vertex turns a limit on what may pass through it into an ordinary arc from "
            "an in-copy to an out-copy. Setting every capacity to one turns the flow value into a "
            "count of routes sharing no arc. Joining every start to one super-source and every end "
            "to one super-sink turns a many-to-many question into a single source-to-sink one. In "
            "all three the algorithm is the same; only the drawing changed. An arc that should have "
            "no bound is given the total capacity of the whole network, which no cut can exceed.",
        )
    )
    script = _ORACLE_JS + _CERTIFICATE + _presets_js(
        "GDP", _GD_PRESETS, ["kind", "spec", "caps", "source", "sink"]) + r"""
  var presetIn = document.getElementById('gdPreset'), kindIn = document.getElementById('gdKind');
  var specIn = document.getElementById('gdSpec'), capsIn = document.getElementById('gdCaps');
  var srcIn = document.getElementById('gdSource'), srcOut = document.getElementById('gdSourceOut');
  var sinkIn = document.getElementById('gdSink'), sinkOut = document.getElementById('gdSinkOut');
  var plot = document.getElementById('gdPlot'), newPlot = document.getElementById('gdNew');
  var mapT = document.getElementById('gdMap'), resultT = document.getElementById('gdResult');
  var status = document.getElementById('gdStatus');
  var KPIS = ['gdBefore', 'gdAfter', 'gdValue', 'gdMeans', 'gdCut', 'gdCheck'];

  function blank(why) {
    plot.innerHTML = ''; newPlot.innerHTML = ''; mapT.innerHTML = ''; resultT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An arc is '
      + '<span class="tt">1&gt;2 5</span>, and a vertex capacity is '
      + '<span class="tt">3:2</span>.';
  }

  /* "3:2, 4:1" -- a capacity on what may pass THROUGH a vertex. A vertex left
     out is uncapped, and uncapped here is the total capacity of the network
     rather than Infinity: the same statement, in a number the arithmetic holds. */
  function readCaps(text, n) {
    var spec = [], parts = fkClauses(text), i;
    for (i = 0; i < parts.length; i += 1) {
      var m = /^(\d+)\s*[:=]\s*(\d+)$/.exec(parts[i]);
      if (!m) return { bad: 'cannot read "' + parts[i] + '" as a vertex capacity' };
      var v = parseInt(m[1], 10), c = parseInt(m[2], 10);
      if (v < 1 || v > n) return { bad: 'this network has no vertex ' + v };
      spec[v - 1] = c;
    }
    return { spec: spec };
  }

  function redraw() {
    var parsed = fkParse(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n, kind = kindIn.value;
    srcIn.max = n; sinkIn.max = n;
    var s = fkStep(parseInt(srcIn.value, 10) - 1, n);
    var t = fkStep(parseInt(sinkIn.value, 10) - 1, n);
    srcOut.textContent = String(s + 1);
    sinkOut.textContent = String(t + 1);
    if (s === t) { blank('the source and the sink are the same vertex'); return; }

    var caps = readCaps(capsIn.value, n);
    if (caps.bad) { blank(caps.bad); return; }

    var idx = dgIndex(G), sources = [], sinks = [], v;
    for (v = 0; v < n; v += 1) {
      if (!idx.inn[v].length) sources.push(v);
      if (!idx.out[v].length) sinks.push(v);
    }

    var built, spec;
    if (kind === 'split') {
      spec = { graph: G, s: s, t: t, vertexCap: fkVertexCaps(G, caps.spec) };
      built = gadgetBuild('split', spec);
    } else if (kind === 'unit') {
      built = gadgetBuild('unit', { graph: G, s: s, t: t });
    } else {
      if (!sources.length || !sinks.length) {
        blank('every vertex here has something coming in and something going out, so there is '
          + 'nothing for a super-source to join');
        return;
      }
      /* gadgetBuild leaves an uncapped joining arc at Infinity. Passing the
         whole network's capacity instead is the same statement in a number the
         arithmetic can hold: an isolated vertex would otherwise be a source AND
         a sink joined to both ends by two infinite arcs, whose bottleneck is
         Infinity and whose residual is then Infinity minus Infinity. */
      var big = fkTotalCap(G) + 1, wide = [], w;
      for (w = 0; w < n; w += 1) wide.push(big);
      built = gadgetBuild('supersource', { graph: G, sources: sources, sinks: sinks,
                                           sourceCap: wide, sinkCap: wide });
    }
    var H = built.graph;
    var run = maxflow(H, built.s, built.t);
    var f = run.result.flow;
    var cut = minCutFrom(H, f, built.s);
    var brute = null, refused = null;
    try { brute = minCutBrute(H, built.s, built.t, 12); }
    catch (err) { refused = err.message; }
    var plain = maxflow(G, s, t);

    var origColours = [], i;
    for (v = 0; v < n; v += 1) {
      origColours.push(v === s ? 3 : (v === t ? 4 : (caps.spec[v] !== undefined ? 2 : -1)));
    }
    plot.innerHTML = dgSvg(G, { points: dgLayout(n, { cx: 330, cy: 130, radius: 96 }),
                                label: 'cap', colours: origColours });

    var hLabels = [], hColours = [];
    if (kind === 'split') {
      for (v = 0; v < n; v += 1) { hLabels.push((v + 1) + 'i'); hColours.push(1); }
      for (v = 0; v < n; v += 1) { hLabels.push((v + 1) + 'o'); hColours.push(0); }
    } else if (kind === 'supersource') {
      for (v = 0; v < n; v += 1) hLabels.push(String(v + 1));
      hLabels.push('S'); hLabels.push('T');
      for (v = 0; v < n; v += 1) hColours.push(sources.indexOf(v) !== -1 ? 1
        : (sinks.indexOf(v) !== -1 ? 2 : -1));
      hColours.push(3); hColours.push(4);
    } else {
      for (v = 0; v < n; v += 1) { hLabels.push(String(v + 1)); hColours.push(v === s ? 3 : (v === t ? 4 : -1)); }
    }
    newPlot.innerHTML = dgSvg(H, { points: dgLayout(H.n, { cx: 330, cy: 150, radius: 122 }),
                                   label: 'flow', flow: f, labels: hLabels, colours: hColours,
                                   highlight: cut.arcs.map(function (e) { return e.id; }) });

    var mrows = '';
    if (kind === 'split') {
      for (v = 0; v < n; v += 1) {
        var cap = spec.vertexCap[v], typed = caps.spec[v] !== undefined;
        mrows += '<tr' + (typed ? ' class="tone-purple"' : '') + '><th class="rowhead">' + (v + 1)
          + '</th><td>' + (v + 1) + 'i and ' + (v + 1) + 'o</td><td>' + cap + '</td><td>'
          + (typed ? 'you capped it' : 'uncapped, so the whole network’s capacity') + '</td>'
          + '<td>' + (f[v] === undefined ? '—' : f[v]) + '</td></tr>';
      }
    } else if (kind === 'unit') {
      var paths = unitPaths(H, f, built.s, built.t);
      paths.forEach(function (path, k) {
        mrows += '<tr><th class="rowhead">route ' + (k + 1) + '</th><td>'
          + path.map(function (x) { return x + 1; }).join(' → ') + '</td><td>1</td><td>'
          + 'shares no arc with the others</td><td>1</td></tr>';
      });
      if (!paths.length) {
        mrows = '<tr><th class="rowhead">no route</th><td>the sink cannot be reached at all</td>'
          + '<td>0</td><td>—</td><td>0</td></tr>';
      }
    } else {
      sources.forEach(function (x) {
        mrows += '<tr class="tone-purple"><th class="rowhead">' + (x + 1) + '</th><td>S to '
          + (x + 1) + '</td><td>' + (fkTotalCap(G) + 1) + '</td><td>nothing comes into it, so it '
          + 'is a source</td><td>' + (f[dgFind(H, H.n - 2, x)] === undefined ? '—'
              : f[dgFind(H, H.n - 2, x)]) + '</td></tr>';
      });
      sinks.forEach(function (x) {
        mrows += '<tr class="tone-purple"><th class="rowhead">' + (x + 1) + '</th><td>'
          + (x + 1) + ' to T</td><td>' + (fkTotalCap(G) + 1) + '</td><td>nothing leaves it, so it '
          + 'is a sink</td><td>' + (f[dgFind(H, x, H.n - 1)] === undefined ? '—'
              : f[dgFind(H, x, H.n - 1)]) + '</td></tr>';
      });
    }
    mapT.innerHTML = '<caption>The correspondence: what each piece of the original became, and '
      + 'what it carries</caption><thead><tr><th>in the original</th><th>in the transformed '
      + 'network</th><th>capacity</th><th>why</th><th>flow on it</th></tr></thead><tbody>'
      + mrows + '</tbody>';

    var uncapped = kind === 'split' && !fkClauses(capsIn.value).length;
    resultT.innerHTML = '<caption>What each network answers</caption><thead><tr><th>network</th>'
      + '<th>vertices</th><th>arcs</th><th>maximum flow</th><th>minimum cut</th></tr></thead>'
      + '<tbody><tr><th class="rowhead">as typed</th><td>' + n + '</td><td>' + G.arcs.length
      + '</td><td class="tone-cyan">' + plain.result.value + '</td><td>'
      + minCutFrom(G, plain.result.flow, s).capacity + '</td></tr>'
      + '<tr><th class="rowhead">after the transformation</th><td>' + H.n + '</td><td>'
      + H.arcs.length + '</td><td class="tone-cyan">' + run.result.value + '</td><td>'
      + cut.capacity + '</td></tr></tbody>';

    document.getElementById('gdBefore').textContent = n + ' and ' + G.arcs.length;
    document.getElementById('gdAfter').textContent = H.n + ' and ' + H.arcs.length;
    document.getElementById('gdValue').textContent = run.result.value;
    document.getElementById('gdMeans').textContent = kind === 'split'
      ? 'the most that can pass, obeying the vertex caps'
      : kind === 'unit' ? 'routes sharing no arc' : 'the most all the starts can send together';
    document.getElementById('gdCut').textContent = brute
      ? brute.result.capacity + (brute.result.capacity === run.result.value ? ' — equal' : ' — report it')
      : 'refused: ' + refused;
    var checkText, checkOk;
    if (kind === 'split') {
      checkOk = uncapped ? run.result.value === plain.result.value : run.result.value <= plain.result.value;
      checkText = uncapped
        ? (checkOk ? 'uncapped, and it gives the original answer' : 'uncapped and different — report it')
        : (checkOk ? 'capping cannot raise the answer, and it did not' : 'capping raised it — report it');
    } else if (kind === 'unit') {
      var pcount = unitPaths(H, f, built.s, built.t).length;
      checkOk = pcount === run.result.value;
      checkText = checkOk ? pcount + ' routes walked out of the flow, matching its value'
        : 'the routes do not add up — report it';
    } else {
      var outOfSources = 0;
      G.arcs.forEach(function (a, id) { if (sources.indexOf(a.u) !== -1) outOfSources += f[id]; });
      checkOk = outOfSources === run.result.value;
      checkText = checkOk ? 'everything the starts send adds to the value'
        : 'the starts send a different total — report it';
    }
    document.getElementById('gdCheck').textContent = checkText;

    var head = kind === 'split'
      ? 'Each vertex became two, joined by an arc carrying its own capacity'
      : kind === 'unit'
        ? 'Every capacity was set to 1'
        : 'One super-source above ' + sources.length + ' start'
          + fkPlural(sources.length, '', 's') + ' and one super-sink below ' + sinks.length
          + ' end' + fkPlural(sinks.length, '', 's');
    status.innerHTML = '<strong>' + head + ': ' + n + ' vertices and ' + G.arcs.length
      + ' arcs became ' + H.n + ' and ' + H.arcs.length + '.</strong> ' + built.note + '. '
      + 'The same augmenting-path algorithm was then run on it, unchanged, and reached '
      + '<span class="tone-cyan">' + run.result.value + '</span>. '
      + (brute
          ? 'Every set holding the new source and not the new sink was enumerated, and the smallest '
            + 'capacity among them is <span class="' + (brute.result.capacity === run.result.value
                ? 'tone-green' : 'tone-red') + '">' + brute.result.capacity + '</span>'
            + (brute.result.capacity === run.result.value
                ? ' &mdash; the certificate survives the transformation, because the transformation '
                  + 'produced an ordinary network. '
                : ', which cannot happen. ')
          : '<span class="tone-amber">The enumeration is refused on the transformed network: '
            + refused + '.</span> ')
      + '<span class="' + (checkOk ? 'tone-green' : 'tone-red') + '">' + checkText + '.</span> '
      + (kind === 'split'
          ? (uncapped
              ? 'With nothing capped, the answer had to come back at ' + plain.result.value
                + ' &mdash; the same as the untransformed network &mdash; and it did. Now cap a '
                + 'vertex and watch it fall: a limit on what may pass THROUGH a place is an arc, and '
                + 'no new algorithm is needed for it.'
              : 'Without the split there is nowhere to write a limit on a vertex at all: a capacity '
                + 'lives on an arc, so the vertex is made into one. The untransformed network allows '
                + plain.result.value + ' and this allows ' + run.result.value + '.')
          : kind === 'unit'
            ? 'With every capacity 1 the value counts routes that share no arc, and the minimum cut '
              + 'counts the arcs that must be removed to stop every one of them &mdash; the same two '
              + 'numbers, so the largest number of arc-disjoint routes equals the fewest arcs that '
              + 'separate the two ends.'
            : 'Each added arc is given the whole network’s capacity rather than no bound, which '
              + 'is never binding and is a number the arithmetic can hold: Infinity would make a '
              + 'bottleneck infinite and the augmentation would never stop. The answer reads back '
              + 'as what all the starts can send together.');
  }

  function apply() {
    var p = GDP[presetIn.value];
    if (!p) return;
    kindIn.value = p.kind; specIn.value = p.spec; capsIn.value = p.caps;
    srcIn.value = p.source; sinkIn.value = p.sink;
    redraw();
  }
  var START = GDP[presetIn.value];
  if (START && !specIn.value) {
    kindIn.value = START.kind; specIn.value = START.spec; capsIn.value = START.caps;
    srcIn.value = START.source; sinkIn.value = START.sink;
  }
  presetIn.addEventListener('change', apply);
  kindIn.addEventListener('change', redraw);
  specIn.addEventListener('input', redraw);
  capsIn.addEventListener('input', redraw);
  srcIn.addEventListener('input', redraw);
  sinkIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Modelling with flow: the graph changes, the algorithm does not",
        subtitle="Vertex capacities by splitting a vertex, disjoint routes by unit capacities, many starts by one super-source",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Pick the transformation and type the network"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each transformation is built from your network and drawn beside it, then solved by "
            "the same algorithm. The correspondence table says what every piece became, and each "
            "gadget carries a check that its answer means what it claims.",
        ),
        script=script,
        expect={"gdPreset": _expect(_GD_PRESETS)},
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice.
# ---------------------------------------------------------------------------

_MODES = {
    "augment": _augment,
    "mincut": _mincut,
    "matching": _matching,
    "gadget": _gadget,
}

MODES = tuple(sorted(_MODES))


def flowkit_lab(cfg):
    """The flow course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "flowkit_lab: unknown mode %r; the four flow modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["flowkit_lab", "FKIT_JS", "MODES"]
