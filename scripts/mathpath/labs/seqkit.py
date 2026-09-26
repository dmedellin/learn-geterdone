"""Course 1 of Algorithms: sequences, their cost models, and union-find.

Four modes, four lessons of `data-structures`:

    arraylist   Arrays, Linked Lists, and the Cost Model
    twostack    Stacks, Queues, and the Two-Stack Queue
    unionfind   Union-Find
    workload    Choosing a Structure

Every number below is a COUNT produced by running the operation sequence on the
representation drawn beside it, in the word-RAM model the course states: an
array index costs 1, reaching the i-th node of a list costs i + 1. Nothing here
quotes a complexity class, and where the count disagrees with the class the
count is what the page prints.

The engine is `algo_core.SEQ_JS` -- `seqRun`, `workloadRun`, `twoStackRun`,
`unionFindRun` -- concatenated as it ships, with `ilog2` from `algorithms.ALGO_JS`
(the sorted array searches by bisection and SEQ_JS calls it). This module adds
only what a PANEL needs and an engine does not have: expanding a named pattern
into an operation sequence, pairing two runs into one table, reconstructing the
two stacks from a trace, and three drawings.

THE DRAWING RULE. Every drawing here is two functions: one that BUILDS the
markup from the thing it draws and returns a string, and one that INSTALLS it,
taking the element as its first argument and tolerating null. That is what makes
`forestSvg` assertable in `scripts/mathcheck.js` and what the repository's
previous drawing helpers -- closed over an element inside a lab function --
could not be.

The one place this kit could not follow the design. §4.1's `workload` row names
`algo_core.workloadRun(mix, n)`, and that function ranks the five SEQUENCE
structures SEQ_JS defines: dynamic array, sorted array, doubly-linked list,
stack and queue. The lesson's own five are sorted array, hash table, AVL tree,
heap and union-find, and three of those have no cost model in SEQ_JS. Rather
than write a second cost model here -- which is exactly the drift the shared
core exists to prevent -- the mode ranks the five `workloadRun` actually knows
and names them. The lesson's POINT survives intact, because it is about the
"not supported" column rather than about which five: a stack cannot answer a
search at all, and a sorted array cannot be told where to insert.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, SEQ_JS, SERIES_JS, TREEDRAW_JS
from .algorithms import ALGO_JS
from .common import Lab, cfg_literal

SEQKIT_JS = r"""
  /* ===================== an operation sequence, from a pattern ==============

     The sequence is the reader's input, so it is expanded here rather than
     stored: `at` is read off the CURRENT size, so moving the position slider or
     changing n moves every cost with it. A delete on an empty list is dropped
     rather than counted as free, which is the difference between "cheap" and
     "did not happen". */
  function seqAt(n, pct) {
    if (n <= 1) return 0;
    return Math.max(0, Math.min(n - 1, Math.round((pct / 100) * (n - 1))));
  }
  function seqExpand(pattern, reps, n0, pct) {
    var ops = [], size = n0, r, i, op;
    for (r = 0; r < reps; r += 1) {
      for (i = 0; i < pattern.length; i += 1) {
        op = pattern[i];
        if (op === 'deleteAt' && size <= 1) continue;
        ops.push({ op: op, at: seqAt(size, pct) });
        if (op.indexOf('insert') === 0) size += 1;
        if (op === 'deleteAt') size -= 1;
      }
    }
    return ops;
  }

  /* ===================== two representations, one sequence =================

     Both runs come from `seqRun`, which is the shared engine; this only pairs
     them, so the table is a comparison rather than two tables the reader has to
     align by eye. `decidedBy` is the operation KIND whose two columns differ
     most in total, which is the answer to "which operation decided it" -- the
     question the lesson asks and a total cannot answer. */
  function seqCompare(ops, n0) {
    var A = seqRun(ops, 'array', n0), L = seqRun(ops, 'list', n0);
    var rows = [], ac = 0, lc = 0, byOp = {}, order = [], i, a, l, k;
    for (i = 0; i < ops.length; i += 1) {
      a = A.trace[i]; l = L.trace[i];
      ac += a.cost; lc += l.cost;
      rows.push({ at: i, op: ops[i].op, index: ops[i].at, size: a.n,
                  array: a.cost, list: l.cost,
                  arrayTotal: ac, listTotal: lc, gap: a.cost - l.cost });
      k = ops[i].op;
      if (!byOp[k]) { byOp[k] = { op: k, count: 0, array: 0, list: 0 }; order.push(k); }
      byOp[k].count += 1; byOp[k].array += a.cost; byOp[k].list += l.cost;
    }
    var kinds = order.map(function (key) { return byOp[key]; });
    var ranked = kinds.slice().sort(function (x, y) {
      return Math.abs(y.array - y.list) - Math.abs(x.array - x.list);
    });
    return { rows: rows, array: A, list: L, kinds: kinds,
             arrayTotal: ac, listTotal: lc,
             winner: ac === lc ? 'tie' : (ac < lc ? 'array' : 'list'),
             decidedBy: ranked.length ? ranked[0] : null,
             ratio: (ac && lc) ? R(BigInt(ac), BigInt(lc)) : null };
  }
  function seqCumulative(rows, which) {
    return rows.map(function (r) { return which === 'array' ? r.arrayTotal : r.listTotal; });
  }

  /* ========================= the two-stack queue ===========================

     Reading the reader's sequence. One letter is one operation and the keys are
     numbered in enqueue order, so what the drawing shows is the reader's own
     string. A character that means nothing is REPORTED rather than ignored
     silently: a typo that quietly shortens the sequence would change every
     count on the panel with no sign that it had. */
  function twoStackParse(text, cap) {
    var ops = [], bad = [], key = 1, i, ch;
    for (i = 0; i < text.length; i += 1) {
      ch = text.charAt(i);
      if (ch === ' ' || ch === ',' || ch === '\t' || ch === '.') continue;
      if (ch === 'e' || ch === 'E' || ch === '+') { ops.push({ op: 'enqueue', key: key }); key += 1; }
      else if (ch === 'd' || ch === 'D' || ch === '-') ops.push({ op: 'dequeue' });
      else if (bad.indexOf(ch) < 0) bad.push(ch);
    }
    var over = ops.length > cap;
    return { ops: over ? ops.slice(0, cap) : ops, ignored: bad, truncated: over };
  }

  /* The two stacks at a step, DERIVED from the trace rather than replayed.

     `twoStackRun` records what each operation cost and whether it transferred,
     and that is enough: a transfer moves everything then on the in stack, so
     after the last transfer at or before this step, the elements enqueued
     BEFORE it and not yet dequeued are the out stack, and those enqueued after
     it are the in stack. Replaying the loop here instead would be a second
     implementation of the structure, free to drift from the one being counted. */
  function twoStackState(run, upto) {
    var enq = [], popped = 0, lastTransfer = -1, i, t;
    for (i = 0; i <= upto && i < run.trace.length; i += 1) {
      t = run.trace[i];
      if (t.op === 'enqueue') enq.push({ key: t.key, at: i });
      if (t.moved) lastTransfer = i;
      if (t.took !== null && t.took !== undefined) popped += 1;
    }
    var live = enq.slice(popped);
    return {
      outStack: live.filter(function (e) { return e.at < lastTransfer; }),
      inStack: live.filter(function (e) { return e.at > lastTransfer; }),
      served: popped, lastTransfer: lastTransfer
    };
  }

  /* Both stacks, drawn. The in stack grows upward from the left, the out stack
     from the right, and the arrow between them is the transfer that costs. */
  function stacksSvg(state, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 520 : opts.width;
    var h = opts.height === undefined ? 192 : opts.height;
    var cell = 22, base = h - 30, s = '';
    function column(items, x, colour, name, tip) {
      var i, y, txt;
      s += '<text x="' + x + '" y="' + (base + 18) + '" text-anchor="middle" font-size="11" '
        + 'fill="var(--muted)">' + name + '</text>';
      s += '<line x1="' + (x - 30) + '" y1="' + base + '" x2="' + (x + 30) + '" y2="' + base
        + '" stroke="var(--line-strong)" stroke-width="2" />';
      for (i = 0; i < items.length; i += 1) {
        y = base - (i + 1) * cell;
        s += '<rect x="' + (x - 26) + '" y="' + (y + 2) + '" width="52" height="' + (cell - 4)
          + '" rx="4" fill="' + colour + '" opacity="0.34" stroke="var(--line-strong)" />';
        txt = String(items[i].key === undefined ? items[i] : items[i].key);
        s += '<text x="' + x + '" y="' + (y + cell - 7) + '" text-anchor="middle" font-size="11" '
          + 'font-weight="700" fill="var(--text)">' + txt + '</text>';
      }
      if (!items.length) {
        s += '<text x="' + x + '" y="' + (base - 10) + '" text-anchor="middle" font-size="11" '
          + 'fill="var(--muted)">empty</text>';
      }
      if (tip) {
        s += '<text x="' + x + '" y="' + (base - items.length * cell - 8) + '" text-anchor="middle" '
          + 'font-size="10" fill="var(--muted)">' + tip + '</text>';
      }
    }
    column(state.inStack, w * 0.28, 'var(--cyan)', 'in', 'newest on top');
    column(state.outStack, w * 0.72, 'var(--amber)', 'out', 'next to leave on top');
    s += '<path d="M' + (w * 0.28 + 44) + ' ' + (base - 52) + ' L' + (w * 0.72 - 44) + ' '
      + (base - 52) + '" stroke="var(--line-strong)" stroke-width="1.6" stroke-dasharray="5 4" '
      + 'fill="none" />';
    s += '<polygon points="' + (w * 0.72 - 44) + ',' + (base - 52) + ' ' + (w * 0.72 - 53) + ','
      + (base - 56) + ' ' + (w * 0.72 - 53) + ',' + (base - 48)
      + '" fill="var(--line-strong)" />';
    s += '<text x="' + (w / 2) + '" y="' + (base - 58) + '" text-anchor="middle" font-size="11" '
      + 'fill="var(--muted)">every element crosses once, and pays once</text>';
    return s;
  }
  function drawStacks(el, state, opts) {
    var s = stacksSvg(state, opts);
    if (el) el.innerHTML = s;
    return s;
  }

  /* ============================== union-find ===============================

     The three sequences the lesson asks for. `chain` is the misconception made
     concrete: with no rank rule every union links the first root under the
     second, so unioning 0-1, 1-2, 2-3 ... builds a path, and the find at the
     end walks all of it. */
  function ufSequence(pattern, n) {
    var ops = [], i, step;
    if (pattern === 'chain') {
      for (i = 0; i + 1 < n; i += 1) ops.push({ op: 'union', a: i, b: i + 1 });
    } else if (pattern === 'pairs') {
      for (step = 1; step < n; step *= 2) {
        for (i = 0; i + step < n; i += 2 * step) ops.push({ op: 'union', a: i, b: i + step });
      }
    } else if (pattern === 'star') {
      for (i = 1; i < n; i += 1) ops.push({ op: 'union', a: i, b: 0 });
    } else {
      throw new Error('unknown union sequence: ' + pattern);
    }
    for (i = 0; i < n; i += 1) ops.push({ op: 'find', a: i });
    return ops;
  }
  /* All four combinations on ONE sequence. The lesson's claim is that either
     rule alone is already good and the pair is what flattens the forest, and a
     claim about four cases is checked by running four cases. */
  function ufAllRules(ops, n) {
    var combos = [{ rank: false, compress: false }, { rank: true, compress: false },
                  { rank: false, compress: true }, { rank: true, compress: true }];
    return combos.map(function (rules) {
      var run = unionFindRun(ops, rules, n);
      return { rank: rules.rank, compress: rules.compress, run: run,
               hops: run.counts.hops || 0, worst: run.result.worstHops,
               maxRank: run.result.maxRank, bound: run.result.bound,
               maxSize: run.result.maxSize, holds: run.result.rankBoundHolds };
    });
  }

  /* Hops PER FIND, which is the figure the panel plots -- a total cannot show
     that the first find after a union walks further than the rest, and under
     path compression that the second find of the same element walks one. Read
     off the trace the engine already keeps. */
  function ufFindHops(run) {
    return run.trace.filter(function (t) { return t.op === 'find'; })
                    .map(function (t) { return t.hops; });
  }

  /* The forest as trees. TREEDRAW_JS is generic over the node type, so the node
     is { i } and `kids` reads the parent array -- the same renderer the search
     trees use, with no second layout written here. */
  function ufNodes(parent) {
    var nodes = parent.map(function (p, i) { return { i: i, p: p }; });
    return {
      nodes: nodes,
      roots: nodes.filter(function (nd) { return nd.p === nd.i; }),
      kids: function (nd) {
        var out = [], j;
        for (j = 0; j < parent.length; j += 1) if (parent[j] === nd.i && j !== nd.i) out.push(nodes[j]);
        return out;
      }
    };
  }
  function ufTreeSizes(parent) {
    var size = parent.map(function () { return 0; }), i, r, guard;
    for (i = 0; i < parent.length; i += 1) {
      r = i; guard = 0;
      while (parent[r] !== r && guard <= parent.length) { r = parent[r]; guard += 1; }
      size[r] += 1;
    }
    return size;
  }
  /* Each tree gets width in proportion to the number of elements in it, and
     every tree is scaled to the SAME depth -- otherwise a two-node set would be
     drawn as tall as the path the lesson is warning about, which is the one
     thing the picture is for. */
  function forestLayout(parent, opts) {
    opts = opts || {};
    var width = opts.width === undefined ? 620 : opts.width;
    var height = opts.height === undefined ? 176 : opts.height;
    var t = ufNodes(parent), sizes = ufTreeSizes(parent), total = 0;
    t.roots.forEach(function (r) { total += sizes[r.i]; });
    if (!total) total = 1;
    var layouts = [], xoff = 0, maxDepth = 0;
    t.roots.forEach(function (root) {
      var w = Math.max(58, (sizes[root.i] / total) * width);
      var L = treeLayout(root, t.kids, function (nd) { return String(nd.i); },
                         { width: w, height: height });
      L.nodes.forEach(function (nd) { nd.x += xoff; });
      if (L.depth > maxDepth) maxDepth = L.depth;
      L.root = root.i;
      layouts.push(L);
      xoff += w;
    });
    var rows = Math.max(1, maxDepth);
    layouts.forEach(function (L) {
      L.nodes.forEach(function (nd) { nd.y = 22 + (nd.depth / rows) * (height - 44); });
    });
    return { layouts: layouts, depth: maxDepth, span: xoff, trees: t.roots.length };
  }
  /* The radius follows the depth when the caller does not fix it: a path of
     sixteen elements and a flat star of sixteen are the two pictures this mode
     exists to put side by side, and one circle size cannot draw both. */
  function forestSvg(parent, opts) {
    opts = opts || {};
    var f = forestLayout(parent, opts), s = '';
    var h = opts.height === undefined ? 176 : opts.height;
    var r = opts.radius;
    if (r === undefined) {
      r = Math.max(6, Math.min(14, Math.floor((h - 44) / (2 * Math.max(1, f.depth)))));
    }
    var o = { highlight: opts.highlight, fill: opts.fill, note: opts.note, radius: r };
    f.layouts.forEach(function (L) { s += treeSvg(L, o); });
    return s;
  }
  function drawForest(el, parent, opts) {
    var s = forestSvg(parent, opts);
    if (el) el.innerHTML = s;
    return s;
  }

  /* ============================== the workload =============================

     `workloadRun` returns a row per structure with the operations it cannot
     answer kept as their own field. The bars draw only the structures that can
     answer the whole mix; the rest get the list of what they refuse, because a
     short bar and a refusal are different answers and drawing them alike is the
     misconception the lesson names. */
  function workloadMix(counts) {
    var mix = {};
    Object.keys(counts).forEach(function (k) { if (counts[k] > 0) mix[k] = counts[k]; });
    return mix;
  }
  function workloadBarsSvg(rows, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 520 : opts.width;
    var top = 18, rowH = 30, left = 128, max = 1, s = '';
    rows.forEach(function (r) { if (r.usable && r.total > max) max = r.total; });
    rows.forEach(function (r, i) {
      var y = top + i * rowH;
      s += '<text x="4" y="' + (y + 14) + '" font-size="11" fill="var(--text)">' + r.label + '</text>';
      if (r.usable) {
        var len = Math.max(2, (r.total / max) * (w - left - 66));
        s += '<rect x="' + left + '" y="' + (y + 3) + '" width="' + len.toFixed(1)
          + '" height="16" rx="4" fill="var(--cyan)" opacity="'
          + (r.best ? '0.72' : '0.36') + '" />';
        s += '<text x="' + (left + len + 6).toFixed(1) + '" y="' + (y + 16)
          + '" font-size="11" font-weight="700" fill="var(--text)">' + r.total + '</text>';
      } else {
        s += '<text x="' + left + '" y="' + (y + 16) + '" font-size="11" fill="var(--red)">'
          + 'cannot answer ' + r.unsupported.join(', ') + '</text>';
      }
    });
    s += '<text x="4" y="' + (top + rows.length * rowH + 12) + '" font-size="11" fill="var(--muted)">'
      + 'bar length is the total cost of the whole mix, counted by running it</text>';
    return s;
  }
  function drawWorkloadBars(el, rows, opts) {
    var s = workloadBarsSvg(rows, opts);
    if (el) el.innerHTML = s;
    return s;
  }
  /* The ranking, with the winner marked so the drawing and the table agree by
     construction rather than by both being written the same way twice. */
  function workloadRanked(mix, n) {
    var run = workloadRun(mix, n);
    var rows = run.result.rows.map(function (r) {
      return { rep: r.rep, label: r.label, total: r.total, usable: r.usable,
               unsupported: r.unsupported, best: r.rep === run.result.best };
    });
    return { rows: rows, ranked: run.result.ranked, best: run.result.best, ops: run.counts.calls };
  }
  var SEQ_OP_NAMES = {
    index: 'index', search: 'search', insertFront: 'insert at the front',
    insertEnd: 'insert at the end', deleteAt: 'delete at a position', min: 'minimum'
  };
  function seqOpName(op) { return SEQ_OP_NAMES[op] || op; }
  /* "a, b or c" -- a list a sentence can contain, which "a or b or c or d" is not. */
  function capitalise(text) { return text.charAt(0).toUpperCase() + text.slice(1); }
  function andList(items) {
    if (items.length <= 1) return items.join('');
    return items.slice(0, -1).join(', ') + ' or ' + items[items.length - 1];
  }
"""


# --------------------------------------------------------------- the furniture


def _options(items, chosen):
    return "".join(
        '<option value="%s"%s>%s</option>' % (key, " selected" if key == chosen else "", label)
        for key, label in items
    )


def _select(cid, label, items, chosen):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n'
        "        </div>\n" % (cid, cid, label, cid, _options(items, chosen))
    )


def _text(cid, label, value):
    return (
        '        <div class="field" id="%sField">\n'
        '          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" />\n'
        "        </div>\n" % (cid, cid, label, cid, value)
    )


def _range(cid, label, lo, hi, value, step=1):
    """One slider, its name and its readout.

    The readout starts as a dash. Every figure on the panel is written by
    redraw() from the arithmetic, so a lab whose script died shows dashes rather
    than a plausible number nothing computed.
    """
    return (
        '        <div id="%sRow">\n'
        '          <div class="range-row"><label class="small-copy" for="%s" id="%sLab">%s</label>'
        '<span class="range-value" id="%sOut">&mdash;</span></div>\n'
        '          <input id="%s" type="range" min="%d" max="%d" step="%d" value="%d" />\n'
        "        </div>\n" % (cid, cid, cid, label, cid, cid, lo, hi, step, value)
    )


def _kpi_dyn(rows):
    """A kpi grid whose labels redraw() writes.

    One figure on this panel changes meaning with a control: with union by rank
    on it is a RANK, and with the rule off it is simply how deep the sequence
    made the tree. A fixed label over a changing quantity is the same defect as
    a mode silently ignored, one level down.
    """
    return (
        '        <div class="kpi-grid">\n'
        + "".join(
            '          <div class="kpi"><span id="%sLab">%s</span><strong id="%s">&mdash;</strong>'
            "</div>\n" % (cid, label, cid)
            for cid, label in rows
        )
        + "        </div>\n"
    )


def _kpi(rows):
    return (
        '        <div class="kpi-grid">\n'
        + "".join(
            '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
            % (label, cid)
            for cid, label in rows
        )
        + "        </div>\n"
    )


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _stage(cid, svg_id, label, height, width=520):
    return (
        '      <div class="lab-stage" id="%s" tabindex="0" role="region" aria-label="%s">'
        '<svg id="%s" style="min-width:%dpx" viewBox="0 0 %d %d" role="img" aria-label="%s">'
        "</svg></div>\n" % (cid, label, svg_id, width, width, height, label)
    )


def _preset_index(cfg, presets, mode):
    """Which worked example the panel opens on.

    Every lesson opens on its own, and an unknown preset raises for the same
    reason an unknown mode does: a silent fallback ships a page that looks
    finished and is about something else.
    """
    want = cfg.get("preset")
    keys = [p["key"] for p in presets]
    if want is None:
        return 0
    if isinstance(want, bool):
        raise ValueError("seqkit mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "seqkit mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "seqkit mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


_CORE_JS = RATIONAL_JS + ALGO_JS + COUNT_JS + SERIES_JS + TREEDRAW_JS + SEQ_JS + SEQKIT_JS


# ============================================================ mode: arraylist

ARRAYLIST_PRESETS = [
    {
        "key": "four-operations",
        "label": "index, insert at the front, insert at the end, delete from the middle",
        "pattern": ["index", "insertFront", "insertEnd", "deleteAt"],
        "n": 16, "reps": 4, "pct": 50,
        "claim": "the sequence the cost model is stated on",
    },
    {
        "key": "front-insertions",
        "label": "three insertions at the front, then one index",
        "pattern": ["insertFront", "insertFront", "insertFront", "index"],
        "n": 24, "reps": 4, "pct": 50,
        "claim": "where the list is supposed to win",
    },
    {
        "key": "random-access",
        "label": "three indexes, then one insertion at the end",
        "pattern": ["index", "index", "index", "insertEnd"],
        "n": 24, "reps": 4, "pct": 80,
        "claim": "where the array wins and the list cannot",
    },
    {
        "key": "scan-bound",
        "label": "search, insert at the end, search, delete at a position",
        "pattern": ["search", "insertEnd", "search", "deleteAt"],
        "n": 20, "reps": 4, "pct": 50,
        "claim": "where both must walk and the representation stops mattering",
    },
]

ARRAYLIST_SCRIPT = r"""
  var plot = document.getElementById('alPlot');
  var table = document.getElementById('alTable');
  var status = document.getElementById('alStatus');
  var sel = document.getElementById('alPreset');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('arraylist: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('alN').value = p.n;
    document.getElementById('alReps').value = p.reps;
    document.getElementById('alPct').value = p.pct;
  }

  function readState() {
    var p = preset();
    var n = +document.getElementById('alN').value;
    var reps = +document.getElementById('alReps').value;
    var pct = +document.getElementById('alPct').value;
    document.getElementById('alNOut').textContent = n + ' elements';
    document.getElementById('alRepsOut').textContent = reps + (reps === 1 ? ' round' : ' rounds');
    document.getElementById('alPctOut').textContent = pct === 0 ? 'the front'
      : (pct === 100 ? 'the back' : pct + '% of the way along');
    return { p: p, n: n, reps: reps, pct: pct,
             ops: seqExpand(p.pattern, reps, n, pct) };
  }

  function redraw() {
    var st = readState();
    var cmp = seqCompare(st.ops, st.n);
    var xs = st.ops.map(function (o, i) { return i + 1; });
    drawSeries(plot, [
      { label: 'array', values: seqCumulative(cmp.rows, 'array'), colour: 'var(--cyan)', points: true },
      { label: 'list', values: seqCumulative(cmp.rows, 'list'), colour: 'var(--amber)', points: true }
    ], xs, { xlabel: 'operation' });

    var h = '<thead><tr><th>step</th><th>operation</th><th>position</th><th>size</th>'
          + '<th>array</th><th>list</th><th>array so far</th><th>list so far</th></tr></thead><tbody>';
    cmp.rows.forEach(function (r) {
      h += '<tr><td>' + (r.at + 1) + '</td><td>' + seqOpName(r.op) + '</td><td>'
        + (r.op === 'insertFront' || r.op === 'insertEnd' || r.op === 'search' || r.op === 'min'
            ? '&mdash;' : r.index)
        + '</td><td>' + r.size + '</td><td class="tone-cyan">' + r.array
        + '</td><td class="tone-amber">' + r.list + '</td><td>' + r.arrayTotal
        + '</td><td>' + r.listTotal + '</td></tr>';
    });
    table.innerHTML = h + '</tbody>';

    document.getElementById('alOps').textContent = st.ops.length;
    document.getElementById('alArray').textContent = cmp.arrayTotal;
    document.getElementById('alList').textContent = cmp.listTotal;
    document.getElementById('alWinner').textContent = cmp.winner === 'tie' ? 'a tie'
      : (cmp.winner === 'array' ? 'the array' : 'the list');
    document.getElementById('alRatio').textContent = cmp.ratio ? Rtext(cmp.ratio) : '—';
    document.getElementById('alDecider').textContent = cmp.decidedBy
      ? seqOpName(cmp.decidedBy.op) : '—';

    var d = cmp.decidedBy;
    var msg = 'This sequence of <strong>' + st.ops.length + '</strong> operations costs <strong>'
      + cmp.arrayTotal + '</strong> on the array and <strong>' + cmp.listTotal
      + '</strong> on the doubly-linked list, counted by running it. ';
    if (d) {
      msg += 'The operation that decided it is <strong>' + seqOpName(d.op) + '</strong>: '
        + d.count + (d.count === 1 ? ' of them costs ' : ' of them cost ') + d.array
        + ' on the array and ' + d.list + ' on the list. ';
    }
    msg += '<span class="tone-red">The list does not insert in one step.</span> Splicing a node in '
      + 'costs one; REACHING the position costs i + 1 hops, and the position column above is where '
      + 'that cost comes from. The array pays the mirror image: reaching any index is one, and '
      + 'making room is a shift of everything after it.';
    status.innerHTML = msg;
  }

  ['alN', 'alReps', 'alPct'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _arraylist(cfg):
    idx = _preset_index(cfg, ARRAYLIST_PRESETS, "arraylist")
    p = ARRAYLIST_PRESETS[idx]
    markup = (
        _toolbar(
            "Two representations, one sequence",
            "cost counted in the word RAM, not quoted from a class",
            _swatch("tone-cyan", "dynamic array") + _swatch("tone-amber", "doubly-linked list"),
        )
        + _stage(
            "alStage", "alPlot",
            "Cumulative cost of the operation sequence on a dynamic array and on a "
            "doubly-linked list.", 220,
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="alTable">'
          "</table></div>\n"
        + '      <div class="status-banner" id="alStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("alPreset", "Operation sequence",
                [(q["key"], q["label"]) for q in ARRAYLIST_PRESETS], p["key"])
        + _range("alN", "starting size", 4, 64, p["n"])
        + _range("alReps", "how many times the sequence repeats", 1, 8, p["reps"])
        + _range("alPct", "where index and delete reach", 0, 100, p["pct"], 5)
        + _kpi([
            ("alOps", "Operations run"),
            ("alArray", "Array total"),
            ("alList", "List total"),
            ("alWinner", "Cheaper here"),
            ("alRatio", "Array : list"),
            ("alDecider", "Decided by"),
        ])
    )
    return Lab(
        title="Arrays against linked lists",
        subtitle="One operation sequence, two representations, two counts",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Compose a sequence and watch both representations pay"),
        panel_intro=cfg.get(
            "panel_intro",
            "Costs are counted in the word RAM the course states: an array index is `1`, "
            "reaching the i-th node of a list is `i + 1`, and a shift moves every element after "
            "the gap. Nothing here is a complexity class — the table is the sequence executed.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", ARRAYLIST_PRESETS) + ARRAYLIST_SCRIPT,
    )


# ============================================================= mode: twostack

TWOSTACK_PRESETS = [
    {"key": "fill-then-drain", "label": "three in, three out",
     "text": "EEEDDD", "step": 3},
    {"key": "alternating", "label": "one in, one out, repeatedly",
     "text": "EDEDEDED", "step": 4},
    {"key": "bulk-then-drain", "label": "six in, six out",
     "text": "EEEEEEDDDDDD", "step": 6},
    {"key": "refill-between", "label": "refills between the drains",
     "text": "EEDEEDEEDDDD", "step": 5},
]

TWOSTACK_SCRIPT = r"""
  var stage = document.getElementById('tsStacks');
  var plot = document.getElementById('tsPlot');
  var table = document.getElementById('tsTable');
  var status = document.getElementById('tsStatus');
  var sel = document.getElementById('tsPreset');
  var box = document.getElementById('tsSeq');
  var CAP = 28;

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('twostack: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    box.value = p.text;
    document.getElementById('tsStep').value = p.step;
  }

  function redraw() {
    var parsed = twoStackParse(box.value || '', CAP);
    var run = twoStackRun(parsed.ops);
    var last = Math.max(0, parsed.ops.length - 1);
    var stepIn = +document.getElementById('tsStep').value;
    var step = Math.min(stepIn, last);
    document.getElementById('tsStepOut').textContent = parsed.ops.length
      ? ('after step ' + (step + 1) + ' of ' + parsed.ops.length) : 'nothing to run';

    var state = twoStackState(run, step);
    drawStacks(stage, state, {});

    var xs = parsed.ops.map(function (o, i) { return i + 1; });
    var totals = run.trace.map(function (t) { return t.total; });
    var bound = run.trace.map(function (t) { return t.bound; });
    var credits = run.trace.map(function (t) { return t.credits; });
    drawSeries(plot, [
      { label: 'cost so far', values: totals, colour: 'var(--cyan)', points: true },
      { label: '3m', values: bound, colour: 'var(--amber)', dashed: true },
      { label: 'credit in the bank', values: credits, colour: 'var(--green)' }
    ], xs.length ? xs : [0], { xlabel: 'operation' });

    var h = '<thead><tr><th>step</th><th>operation</th><th>element</th><th>moved</th>'
          + '<th>cost</th><th>cost so far</th><th>3m</th><th>credit</th></tr></thead><tbody>';
    run.trace.forEach(function (t, i) {
      h += '<tr' + (i === step ? ' class="tone-cyan"' : '') + '><td>' + (i + 1) + '</td><td>'
        + t.op + '</td><td>' + (t.op === 'enqueue' ? t.key : (t.took === null ? '&mdash;' : t.took))
        + '</td><td>' + t.moved + '</td><td>' + t.cost + '</td><td>' + t.total + '</td><td>'
        + t.bound + '</td><td' + (t.credits < 0 ? ' class="tone-red"' : '') + '>' + t.credits
        + '</td></tr>';
    });
    table.innerHTML = h + '</tbody>';

    var worst = 0, worstAt = 0;
    run.trace.forEach(function (t, i) { if (t.cost > worst) { worst = t.cost; worstAt = i + 1; } });
    var amortised = run.result.total && parsed.ops.length
      ? R(BigInt(run.result.total), BigInt(parsed.ops.length)) : null;
    document.getElementById('tsOps').textContent = parsed.ops.length;
    document.getElementById('tsTotal').textContent = run.result.total;
    document.getElementById('tsBound').textContent = run.result.bound;
    document.getElementById('tsWorst').textContent = parsed.ops.length
      ? (worst + ' at step ' + worstAt) : '—';
    document.getElementById('tsAvg').textContent = amortised ? Rtext(amortised) : '—';
    document.getElementById('tsCredit').textContent = run.result.creditsNeverNegative
      ? 'never negative' : 'went negative';

    var msg = '';
    if (parsed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + parsed.ignored.join(' ')
        + '</span> &mdash; e adds an element and d removes one. ';
    }
    if (parsed.truncated) msg += 'Only the first ' + CAP + ' operations are run. ';
    if (!parsed.ops.length) {
      status.innerHTML = msg + 'Type a sequence of e and d to run it.';
      return;
    }
    msg += 'The ' + parsed.ops.length + ' operations cost <strong>' + run.result.total
      + '</strong> in all, against the <strong>' + run.result.bound + '</strong> the credit '
      + 'argument allows for ' + run.result.enqueues + ' enqueues &mdash; '
      + (run.result.withinBound ? 'inside it' : 'OUTSIDE it, which would refute the bound')
      + '. The expensive step is step <strong>' + worstAt + '</strong>, costing <strong>'
      + worst + '</strong>: that is the transfer, and it is real. '
      + '<span class="tone-red">Amortised does not mean each dequeue is fast.</span> '
      + 'Charge every enqueue 3, spend 1 on the push, and the element carries 2 into the bank; '
      + 'the transfer and the pop each spend 1 of its own. The credit column is that bank, and it '
      + (run.result.creditsNeverNegative ? 'never goes negative, which is the proof.'
                                         : 'went negative, which would break the argument.');
    status.innerHTML = msg;
  }

  document.getElementById('tsStep').addEventListener('input', redraw);
  box.addEventListener('input', redraw);
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _twostack(cfg):
    idx = _preset_index(cfg, TWOSTACK_PRESETS, "twostack")
    p = TWOSTACK_PRESETS[idx]
    markup = (
        _toolbar(
            "A queue from two stacks",
            "one expensive dequeue, and the credit that already paid for it",
            _swatch("tone-cyan", "cost so far") + _swatch("tone-amber", "3m")
            + _swatch("tone-green", "credit"),
        )
        + _stage("tsStage", "tsStacks", "The in stack and the out stack after the chosen step.", 192)
        + _stage(
            "tsPlotStage", "tsPlot",
            "Cumulative cost against the 3m line, with the credit balance after each operation.",
            220,
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="tsTable">'
          "</table></div>\n"
        + '      <div class="status-banner" id="tsStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("tsPreset", "Worked sequence",
                [(q["key"], q["label"]) for q in TWOSTACK_PRESETS], p["key"])
        + _text("tsSeq", "Your own sequence (e enqueues, d dequeues)", p["text"])
        + _range("tsStep", "show the stacks after", 0, 27, p["step"])
        + _kpi([
            ("tsOps", "Operations"),
            ("tsTotal", "Total cost"),
            ("tsBound", "The 3m bound"),
            ("tsWorst", "Worst single step"),
            ("tsAvg", "Cost per operation"),
            ("tsCredit", "Credit balance"),
        ])
    )
    return Lab(
        title="Stacks, queues and the amortised bound",
        subtitle="Every element crosses once, so every element costs three",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a sequence and find the expensive dequeue"),
        panel_intro=cfg.get(
            "panel_intro",
            "One unit of cost is one element touched: a push, a transfer, a pop. Charge every "
            "enqueue `3` and the bank never runs dry, so `m` enqueues cost at most `3m` however "
            "the operations interleave. The bank is the credit column, and the bound beside it is "
            "evaluated rather than asserted.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", TWOSTACK_PRESETS) + TWOSTACK_SCRIPT,
    )


# ============================================================ mode: unionfind

UNIONFIND_PRESETS = [
    {"key": "chain", "label": "union each element with the next", "n": 12,
     "rank": 0, "compress": 0},
    {"key": "pairs", "label": "pair up, then pair the pairs", "n": 12,
     "rank": 1, "compress": 0},
    {"key": "star", "label": "union everything into one element", "n": 12,
     "rank": 0, "compress": 1},
]

UNIONFIND_SCRIPT = r"""
  var stage = document.getElementById('ufForest');
  var plot = document.getElementById('ufPlot');
  var table = document.getElementById('ufTable');
  var status = document.getElementById('ufStatus');
  var sel = document.getElementById('ufPattern');
  var rankSel = document.getElementById('ufRank');
  var compressSel = document.getElementById('ufCompress');

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('unionfind: no sequence named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('ufN').value = p.n;
    rankSel.value = p.rank ? 'on' : 'off';
    compressSel.value = p.compress ? 'on' : 'off';
  }
  function ruleName(rank, compress) {
    if (rank && compress) return 'both rules';
    if (rank) return 'union by rank only';
    if (compress) return 'path compression only';
    return 'neither rule';
  }

  function redraw() {
    var n = +document.getElementById('ufN').value;
    document.getElementById('ufNOut').textContent = n + ' elements';
    var ops = ufSequence(sel.value, n);
    var rows = ufAllRules(ops, n);
    var rank = rankSel.value === 'on', compress = compressSel.value === 'on';
    var shown = rows.filter(function (r) { return r.rank === rank && r.compress === compress; })[0];

    drawForest(stage, shown.run.result.parent, { width: 620, height: 280 });

    /* Per find, measured, against the ceiling union by rank buys. A rank-r root
       has at least 2^r elements under it, so in a set of n elements no root has
       rank above floor(log2 n) -- and with no compression the rank IS the
       depth, which makes that the deepest a find can ever walk. The measured
       curve is allowed to sit under it and, without the rank rule, above it. */
    var hops = ufFindHops(shown.run);
    var ceiling = hops.map(function () { return ilog2(Math.max(1, shown.maxSize)); });
    drawSeries(plot, [
      { label: 'hops', values: hops, colour: 'var(--cyan)', points: true },
      { label: 'log2 of the set', values: ceiling, colour: 'var(--amber)', dashed: true }
    ], hops.map(function (v, i) { return i + 1; }), { xlabel: 'find' });

    var h = '<thead><tr><th>union by rank</th><th>path compression</th><th>pointer hops</th>'
          + '<th>worst single find</th><th>tallest root, rank r</th><th>2^r</th>'
          + '<th>largest set</th><th>2^r fits inside it</th></tr></thead><tbody>';
    rows.forEach(function (r) {
      h += '<tr' + (r === shown ? ' class="tone-cyan"' : '') + '><td>' + (r.rank ? 'on' : 'off')
        + '</td><td>' + (r.compress ? 'on' : 'off') + '</td><td>' + r.hops + '</td><td>'
        + r.worst + '</td><td>' + r.maxRank + '</td><td>' + r.bound + '</td><td>' + r.maxSize
        + '</td><td class="' + (r.holds ? 'tone-green' : 'tone-red') + '">'
        + (r.holds ? 'yes' : 'no') + '</td></tr>';
    });
    table.innerHTML = h + '</tbody>';

    var plain = rows[0], both = rows[3];
    document.getElementById('ufOps').textContent = ops.length;
    document.getElementById('ufHops').textContent = shown.hops;
    document.getElementById('ufWorst').textContent = shown.worst;
    document.getElementById('ufTallestLab').textContent = rank
      ? 'Rank of the tallest root' : 'Depth of the tallest tree';
    document.getElementById('ufTallest').textContent = shown.maxRank;
    document.getElementById('ufBound').textContent = shown.bound
      + (shown.holds ? ' ≤ ' : ' > ') + shown.maxSize;
    document.getElementById('ufSaved').textContent = plain.hops
      ? (plain.hops - both.hops) + ' of ' + plain.hops : '—';

    status.innerHTML = 'With <strong>' + ruleName(rank, compress) + '</strong> this sequence of '
      + ops.length + ' operations walks <strong>' + shown.hops + '</strong> parent pointers, and '
      + 'the worst single find walks <strong>' + shown.worst + '</strong>. The tallest root has '
      + (rank
          ? 'rank <strong>' + shown.maxRank + '</strong>, and union by rank forces at least '
            + '<strong>' + shown.bound + '</strong> elements beneath a root of that rank; the set '
            + 'holds <strong>' + shown.maxSize + '</strong>, so the bound '
            + (shown.holds ? 'holds, as the induction says it must.'
                           : 'FAILS, which would refute the induction.')
          : 'depth <strong>' + shown.maxRank + '</strong>, because with no rank rule nothing stops '
            + 'a tree growing as tall as the sequence makes it. A root that deep would need '
            + '<strong>' + shown.bound + '</strong> elements under it to satisfy the bound and '
            + 'this set holds <strong>' + shown.maxSize + '</strong>, so the bound '
            + (shown.holds ? 'still happens to hold here.'
                           : 'does not hold &mdash; which is the point. It is a claim about union '
                             + 'BY RANK, and there is no rank rule here to make it true.'))
      + ' <span class="tone-red">Union does not link the two roots either way.</span> '
      + 'With no rank rule this sequence walks ' + plain.hops + ' pointers and with both rules '
      + both.hops + '; the rank rule is what refuses to hang the taller tree under the shorter '
      + 'one, and a rank-r tree has 2^r elements by induction on that refusal. Turn that round '
      + 'and it is the dashed line above the finds: no root in a set of ' + shown.maxSize
      + ' elements can have rank past ' + ilog2(Math.max(1, shown.maxSize)) + ', so no find can '
      + 'walk further than that '
      + (rank ? 'and none above does.' : '— and with no rank rule to enforce it, they do.')
      + ' The near-constant '
      + 'bound that both rules together give is STATED on this path and not proved: its proof '
      + 'needs machinery no Subject here teaches. What is proved is the log bound above.';
  }

  document.getElementById('ufN').addEventListener('input', redraw);
  [rankSel, compressSel].forEach(function (el) { el.addEventListener('change', redraw); });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _unionfind(cfg):
    idx = _preset_index(cfg, UNIONFIND_PRESETS, "unionfind")
    p = UNIONFIND_PRESETS[idx]
    markup = (
        _toolbar(
            "Sets as trees",
            "pointer hops under each combination of the two rules",
            _swatch("tone-cyan", "the drawn combination") + _swatch("tone-green", "bound holds")
            + _swatch("tone-red", "bound fails"),
        )
        + _stage(
            "ufStage", "ufForest",
            "The union-find forest: one tree per set, each node labelled by its element.",
            280, 660,
        )
        + _stage(
            "ufPlotStage", "ufPlot",
            "Pointer hops walked by each find in turn, against the depth a rank-r root allows.",
            220,
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="ufTable">'
          "</table></div>\n"
        + '      <div class="status-banner" id="ufStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("ufPattern", "Union sequence",
                [(q["key"], q["label"]) for q in UNIONFIND_PRESETS], p["key"])
        + _range("ufN", "elements", 4, 16, p["n"])
        + _select("ufRank", "Union by rank", [("off", "off"), ("on", "on")],
                  "on" if p["rank"] else "off")
        + _select("ufCompress", "Path compression", [("off", "off"), ("on", "on")],
                  "on" if p["compress"] else "off")
        + _kpi_dyn([
            ("ufOps", "Operations"),
            ("ufHops", "Pointer hops"),
            ("ufWorst", "Worst find"),
            ("ufTallest", "Tallest root"),
            ("ufBound", "2^r against the set"),
            ("ufSaved", "Hops the rules save"),
        ])
    )
    return Lab(
        title="Union by rank and path compression",
        subtitle="Four combinations of two rules, on one sequence",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Issue unions and finds, and watch the forest flatten"),
        panel_intro=cfg.get(
            "panel_intro",
            "A set is a rooted tree and a find walks to the root, so the cost of a find is the "
            "depth of the element. Union by rank refuses to hang the taller tree under the "
            "shorter, which forces a rank-r tree to hold at least `2^r` elements; path "
            "compression flattens what it walks. Every hop below was walked.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", UNIONFIND_PRESETS) + UNIONFIND_SCRIPT,
    )


# ============================================================= mode: workload

WORKLOAD_PRESETS = [
    {"key": "lookup-heavy", "label": "mostly lookups, and the smallest now and then",
     "n": 32, "index": 2, "search": 12, "insertFront": 0, "insertEnd": 0,
     "deleteAt": 2, "min": 2},
    {"key": "queue-like", "label": "insert at one end, remove at the other",
     "n": 32, "index": 0, "search": 0, "insertFront": 8, "insertEnd": 0,
     "deleteAt": 8, "min": 0},
    {"key": "priority-like", "label": "insert, then repeatedly take the minimum",
     "n": 32, "index": 0, "search": 0, "insertFront": 0, "insertEnd": 8,
     "deleteAt": 0, "min": 8},
    {"key": "everything", "label": "a little of every operation",
     "n": 32, "index": 3, "search": 3, "insertFront": 3, "insertEnd": 3,
     "deleteAt": 3, "min": 3},
]

WORKLOAD_SCRIPT = r"""
  var stage = document.getElementById('wlBars');
  var table = document.getElementById('wlTable');
  var status = document.getElementById('wlStatus');
  var sel = document.getElementById('wlPreset');
  var OPS = ['index', 'search', 'insertFront', 'insertEnd', 'deleteAt', 'min'];
  var SLIDER = { index: 'wlIndex', search: 'wlSearch', insertFront: 'wlFront',
                 insertEnd: 'wlEnd', deleteAt: 'wlDelete', min: 'wlMin' };

  function preset() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === sel.value) return PRESETS[i];
    throw new Error('workload: no preset named ' + sel.value);
  }
  function applyPreset() {
    var p = preset();
    document.getElementById('wlN').value = p.n;
    OPS.forEach(function (op) { document.getElementById(SLIDER[op]).value = p[op]; });
  }

  function redraw() {
    var n = +document.getElementById('wlN').value, counts = {}, total = 0;
    OPS.forEach(function (op) {
      var v = +document.getElementById(SLIDER[op]).value;
      counts[op] = v; total += v;
      document.getElementById(SLIDER[op] + 'Out').textContent = v
        + (v === 1 ? ' call' : ' calls');
    });
    document.getElementById('wlNOut').textContent = n + ' elements';

    if (!total) {
      stage.innerHTML = '';
      table.innerHTML = '';
      document.getElementById('wlOps').textContent = '0';
      ['wlBest', 'wlBestCost', 'wlWorst', 'wlRefused', 'wlSpread'].forEach(function (id) {
        document.getElementById(id).textContent = '—';
      });
      status.innerHTML = 'Ask for at least one operation and every structure will run the mix.';
      return;
    }

    var out = workloadRanked(workloadMix(counts), n);
    drawWorkloadBars(stage, out.rows, { width: 520 });

    var h = '<thead><tr><th>structure</th><th>total cost</th><th>cannot answer</th>'
          + '<th>rank</th></tr></thead><tbody>';
    out.rows.forEach(function (r) {
      var place = 0;
      out.ranked.forEach(function (q, i) { if (q.rep === r.rep) place = i + 1; });
      h += '<tr><td>' + r.label + '</td><td>' + (r.usable ? r.total : '&mdash;')
        + '</td><td class="' + (r.usable ? 'tone-muted' : 'tone-red') + '">'
        + (r.usable ? 'nothing' : r.unsupported.map(seqOpName).join(', '))
        + '</td><td>' + (r.usable ? place : 'not in the running') + '</td></tr>';
    });
    table.innerHTML = h + '</tbody>';

    var best = out.ranked.length ? out.ranked[0] : null;
    var worst = out.ranked.length ? out.ranked[out.ranked.length - 1] : null;
    var refused = out.rows.filter(function (r) { return !r.usable; });
    document.getElementById('wlOps').textContent = out.ops;
    document.getElementById('wlBest').textContent = best ? best.label : 'none of them';
    document.getElementById('wlBestCost').textContent = best ? best.total : '—';
    document.getElementById('wlWorst').textContent = worst ? worst.label : '—';
    document.getElementById('wlRefused').textContent = refused.length;
    document.getElementById('wlSpread').textContent = (best && worst && best.total)
      ? Rtext(R(BigInt(worst.total), BigInt(best.total))) : '—';

    var msg = 'This mix of <strong>' + out.ops + '</strong> operations on <strong>' + n
      + '</strong> elements is cheapest on <strong>' + (best ? best.label : 'nothing here')
      + '</strong>';
    if (best && worst && best.rep !== worst.rep) {
      msg += ', at ' + best.total + ' against ' + worst.total + ' on the ' + worst.label;
    }
    msg += '. ';
    if (refused.length) {
      msg += '<span class="tone-red">' + refused.length
        + (refused.length === 1 ? ' structure is' : ' structures are')
        + ' not slow &mdash; they are out of the running.</span> '
        + capitalise(refused.map(function (r) {
            return 'a ' + r.label + ' cannot answer ' + andList(r.unsupported.map(seqOpName));
          }).join(', and '))
        + '. "Not supported" is its own column, not a large number: the mix decides the '
        + 'structure, and the operations a structure refuses decide it first.';
    } else {
      msg += 'Every structure here can answer every operation in this mix, so the choice is a '
        + 'comparison of totals. Ask for an operation one of them refuses and the table changes '
        + 'shape: the refusal is its own answer, not a slow one.';
    }
    status.innerHTML = msg;
  }

  ['wlN'].concat(OPS.map(function (op) { return SLIDER[op]; })).forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  sel.addEventListener('change', function () { applyPreset(); redraw(); });
  redraw(); window.redrawLab = redraw;
"""


def _workload(cfg):
    idx = _preset_index(cfg, WORKLOAD_PRESETS, "workload")
    p = WORKLOAD_PRESETS[idx]
    markup = (
        _toolbar(
            "The mix decides the structure",
            "five representations, one operation mix, and the operations each refuses",
            _swatch("tone-cyan", "total cost") + _swatch("tone-red", "cannot answer"),
        )
        + _stage(
            "wlStage", "wlBars",
            "Total cost of the operation mix on each structure, with refusals named rather "
            "than costed.", 200,
        )
        + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="wlTable">'
          "</table></div>\n"
        + '      <div class="status-banner" id="wlStatus" style="margin-top:12px;"></div>'
    )
    controls = (
        _select("wlPreset", "Workload",
                [(q["key"], q["label"]) for q in WORKLOAD_PRESETS], p["key"])
        + _range("wlN", "elements held", 8, 64, p["n"])
        + _range("wlIndex", "index by position", 0, 16, p["index"])
        + _range("wlSearch", "search for a value", 0, 16, p["search"])
        + _range("wlFront", "insert at the front", 0, 16, p["insertFront"])
        + _range("wlEnd", "insert at the end", 0, 16, p["insertEnd"])
        + _range("wlDelete", "delete at a position", 0, 16, p["deleteAt"])
        + _range("wlMin", "take the minimum", 0, 16, p["min"])
        + _kpi([
            ("wlOps", "Operations in the mix"),
            ("wlBest", "Cheapest"),
            ("wlBestCost", "Its total"),
            ("wlWorst", "Dearest that can run it"),
            ("wlRefused", "Out of the running"),
            ("wlSpread", "Dearest : cheapest"),
        ])
    )
    return Lab(
        title="Choosing from the operation mix",
        subtitle="Totals where a structure can answer, a refusal where it cannot",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set the mix and let every structure run it"),
        panel_intro=cfg.get(
            "panel_intro",
            "Five sequence representations run the same mix and are ranked on what it cost them. "
            "A structure that cannot answer an operation at all is not given a large number: it "
            "is named, and it leaves the ranking. That column is the whole instrument — the "
            "data does not choose the structure, and neither does the fastest single operation.",
        ),
        script=_CORE_JS + cfg_literal("PRESETS", WORKLOAD_PRESETS) + WORKLOAD_SCRIPT,
    )


_BUILDERS = {
    "arraylist": _arraylist,
    "twostack": _twostack,
    "unionfind": _unionfind,
    "workload": _workload,
}

MODES = tuple(_BUILDERS)


def seqkit_lab(cfg):
    """The sequences kit: four modes, four lessons.

    An unknown mode RAISES. Falling back to a default is how a lesson on
    choosing a structure ends up showing the reader a two-stack queue, on a page
    that builds, renders, redraws and passes every markup assertion in the suite
    while teaching the wrong thing.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "seqkit: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["SEQKIT_JS", "MODES", "seqkit_lab"]
