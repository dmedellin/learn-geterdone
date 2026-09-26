"""Search trees: the invariant, the shape problem, balance, augmentation, and two
randomised trees that replace balance with a coin.

Seven modes, seven lessons, two courses. Five belong to `data-structures`, where
a search tree is the structure whose cost is decided by something the reader
controls and does not usually think about -- the insertion order -- and two to
`randomised-algorithms`, where the coin does the balancing:

    bst         Binary Search Trees
    orders      The Shape Problem and Random BSTs
    rotate      Rotations and the AVL Invariant
    avl         AVL Insertion
    augment     Augmenting a Tree
    treap       Treaps
    skiplist    Skip Lists

THE ARITHMETIC IS `algo_core.TREE_JS`, concatenated as it ships: `bstRun`,
`bstValid`, `bstFromOrder`, `rotate`, `minAvlNodes`, `avlInsert`, `augmentWalk`,
`treapInsert`, `skipBuild`. Heights, depths, comparisons, rotations and hops are
counts, produced by running the operation on the tree drawn beside them. Mean
depths are exact rationals, because a mean of integers is a fraction.

THE DRAWING IS `algo_core.TREEDRAW_JS`, and that is the point of it. Six kinds
of tree are drawn on this path -- plain search trees, AVL trees, treaps, the
counterexample to the local check, the tree after a rotation, and the
size-annotated tree -- and every one of them was going to be a helper closed
over its own lab's element. `treeLayout` puts x at the in-order position and y
at the depth, which is the layout that makes a search tree's in-order sequence
readable straight off the picture; `drawBst` below is the four lines that adapt
it to a `{key, l, r, size, height, priority}` node, and it is the only adapter.

WHAT ROUNDS HERE, AND WHERE IT SAYS SO. One of the path's four approximations is
on this kit, and it is the MODEL rather than the arithmetic:

  `randomBstDepthApprox(n)` = 2 ln n, on `orders` and on `treap`. Math.log is
  correctly rounded, so the number is the asymptote to about 1e-15 -- and the
  asymptote is about 15% wrong about the tree. At n = 15 it reads 5.42 while a
  balanced tree on fifteen keys has height 3 and a mean depth near 2.9. So it is
  never printed as "the answer": it is drawn as a dashed reference curve, its
  KPI is labelled asymptotic, and the panel says in words which of the numbers
  beside it is the measured height, which is the measured mean depth, and which
  is the asymptote -- because they are three different quantities and the
  failure mode of this lesson is reading them as one.

`skiplist` prints `2 log2 n` next to the hops it counted. That is a REFERENCE
CURVE, sampled at double precision, and it is not one of the four: no verdict is
read off it, and the panel says so on the row.

TWO THINGS THE ENGINE DID NOT HAVE AND A PANEL NEEDS.

  `rotateAt`. `rotate(node, dir)` rotates at the node it is given and returns
  the new subtree root, which is right and is not enough: a lesson that lets the
  reader click any node has to splice the result back under that node's parent.
  So `rotateAt` rebuilds the path, and it reports whether the rotation was
  POSSIBLE rather than silently returning the tree unchanged -- `rotate` returns
  `t` when the child it would lift is missing, and a panel that could not tell
  that apart from a rotation would show "in-order unchanged" as a success.

  `localOnlyTree`. The misconception of the first lesson is that the search-tree
  property is a local check, and the only thing that settles it is an instance
  where the two checks disagree. It is built here rather than stored as data,
  so `bstValid` and `bstLocallyValid` are evaluated on it in the reader's
  browser like everything else.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, RFIXED_JS, SEEDED_JS, SERIES_JS, TREE_JS, TREEDRAW_JS
from .common import Lab, cfg_literal
from .sysdesign_core import APPROX_JS, STREAM_JS

TREEKIT_JS = r"""
  /* ===================== what the reader typed ============================= */
  function treeParseKeys(text, cap) {
    var out = [], seen = {}, ignored = [], truncated = false;
    (String(text === undefined || text === null ? '' : text).match(/-?\d+/g) || [])
      .forEach(function (token) {
        var v = parseInt(token, 10);
        if (!isFinite(v) || v < 0) { ignored.push(token); return; }
        if (seen[v]) return;
        seen[v] = true;
        if (out.length < cap) out.push(v); else truncated = true;
      });
    return { keys: out, ignored: ignored, truncated: truncated };
  }
  /* insert, delete and search in one line: 40 inserts, -40 deletes, ?40 looks
     up. Keys are non-negative, so the minus sign is free to mean something. */
  function treeParseOps(text, cap) {
    var ops = [], ignored = [], truncated = false;
    (String(text === undefined || text === null ? '' : text).match(/[+?-]?\d+/g) || [])
      .forEach(function (token) {
        var op = 'insert', body = token;
        if (token.charAt(0) === '-') { op = 'delete'; body = token.slice(1); }
        else if (token.charAt(0) === '?') { op = 'search'; body = token.slice(1); }
        else if (token.charAt(0) === '+') { body = token.slice(1); }
        var v = parseInt(body, 10);
        if (!isFinite(v) || v < 0) { ignored.push(token); return; }
        if (ops.length < cap) ops.push({ op: op, key: v }); else truncated = true;
      });
    return { ops: ops, ignored: ignored, truncated: truncated };
  }

  /* ===================== insertion orders ==================================

     The SAME KEY SET in four orders, which is the whole content of the shape
     lesson: the keys do not decide the tree, the order does.

       sorted      1, 2, 3, ...        a path of height n - 1
       reversed    n, n-1, ...         the same path, mirrored
       shuffled    a uniformly random permutation from the reader's seed, by
                   Fisher-Yates over SEEDED_JS
       bisect      the middle, then the middle of each half: the order that
                   gives the SHORTEST possible tree, so the reader has both ends
                   of the range rather than only the bad one */
  function insertOrder(kind, n, seed) {
    var keys = [], i;
    for (i = 1; i <= n; i += 1) keys.push(i * 10);
    if (kind === 'sorted') return keys;
    if (kind === 'reversed') return keys.slice().reverse();
    if (kind === 'bisect') {
      var out = [];
      (function half(lo, hi) {
        if (lo > hi) return;
        var mid = Math.floor((lo + hi) / 2);
        out.push(keys[mid]);
        half(lo, mid - 1);
        half(mid + 1, hi);
      })(0, keys.length - 1);
      return out;
    }
    var perm = algoPermutation(n, seed);
    return perm.map(function (p) { return keys[p]; });
  }

  /* ===================== rotation at a chosen node =========================

     rotate() rotates at the node it is handed. A panel that lets the reader
     pick any node has to put the result back under that node's parent, which
     is what this does, on a COPY -- so the before picture survives to be drawn
     beside the after one.

     `rotated` is false when the rotation was impossible: rotate() returns the
     node unchanged when the child it would lift is missing, and a panel that
     could not tell that from a real rotation would report "in-order unchanged"
     as though something had happened. */
  function rotateAt(root, key, dir) {
    var copy = bstCopy(root), possible = false, found = false;
    function go(t) {
      if (!t) return null;
      if (t.key === key) {
        found = true;
        possible = dir === 'right' ? !!t.l : !!t.r;
        return rotate(t, dir);
      }
      if (key < t.key) t.l = go(t.l); else t.r = go(t.r);
      return bstFix(t);
    }
    var out = go(copy);
    return { root: bstFix(out), rotated: possible, found: found };
  }

  /* ===================== the counterexample to the local check =============

     Every node sits between its two children -- 10 is below 20, 30 is above it,
     25 is above 10 -- and the tree is not a search tree, because 25 is in 20's
     LEFT subtree. bstValid carries the bounds down and says so; bstLocallyValid
     checks only parent against child and does not. Built here rather than
     stored, so both verdicts are computed in the reader's browser. */
  function localOnlyTree() {
    var root = bstNode(20), left = bstNode(10), right = bstNode(30), rogue = bstNode(25);
    left.r = rogue;
    root.l = left;
    root.r = right;
    bstFix(rogue); bstFix(left); bstFix(right); bstFix(root);
    return root;
  }

  /* ===================== sizes, checked rather than trusted ================

     "Augmentation is free" is the misconception, and a rotation is where it
     stops being free. So the panel recomputes every subtree size from the tree
     it is looking at and compares: an attribute that goes stale through a
     rotation shows up here as a false, not as a wrong answer three queries
     later. */
  function sizesValid(t) {
    if (!t) return true;
    if (t.size !== 1 + (t.l ? t.l.size : 0) + (t.r ? t.r.size : 0)) return false;
    return sizesValid(t.l) && sizesValid(t.r);
  }
  /* A tree as a string, so two trees can be compared for SHAPE rather than for
     height. Two treaps on the same (key, priority) set are the same tree, and
     equal heights would be much weaker evidence for that than equal shapes. */
  function treeShape(t) {
    if (!t) return '.';
    return '(' + t.key + ' ' + treeShape(t.l) + ' ' + treeShape(t.r) + ')';
  }
  /* The tallest an AVL tree with n nodes can be: the largest h whose minimum
     node count N(h) still fits inside n. A search over the recurrence, not a
     logarithm. */
  function avlHeightBound(n) {
    var rows = minAvlNodes(28).rows, best = 0;
    for (var i = 0; i < rows.length; i += 1) if (rows[i].n <= n) best = rows[i].h;
    return best;
  }

  /* ===================== priorities for a treap ============================

     Ranked rather than taken raw, so no two keys share a priority: a tie would
     leave the treap shape undetermined and the mode's whole claim -- two
     insertion orders of the same (key, priority) set give the same tree -- would
     be false for a reason that has nothing to do with treaps. */
  function treapPriorities(keys, seed) {
    var draws = algoStream(seed, keys.length);
    var idx = keys.map(function (_k, i) { return i; });
    idx.sort(function (a, b) { return draws[a] - draws[b] || a - b; });
    var map = {};
    idx.forEach(function (i, rank) { map[keys[i]] = rank + 1; });
    return map;
  }
  function prioritiesFor(order, map) {
    return order.map(function (k) { return map[k]; });
  }

  /* ===================== the two reference curves ==========================

     Neither is a count and the panels say so on the row where each appears.
     2 ln n is one of the four approximations this path names: an ASYMPTOTE for
     the mean depth of a tree built from a uniformly random order, which is
     about 15% wrong about any particular small tree. 2 log2 n is a reference
     curve for a skip list's expected hops, sampled at double precision; no
     verdict is read off it. */
  function hopsReference(n) { return n > 1 ? 2 * Math.log2(n) : 1; }

  /* ===================== the drawings ======================================

     drawBst is the only adapter between TREEDRAW_JS and a {key, l, r, size,
     height, priority} node, and it is four lines: which children, what label,
     which nodes to highlight, what note rides above each circle. Everything
     that draws a tree on this kit goes through it. */
  function bstLayout(root, opts) {
    opts = opts || {};
    return treeLayout(root, bstKids, function (t) { return String(t.key); },
                      { width: opts.width === undefined ? 660 : opts.width,
                        height: opts.height === undefined ? 210 : opts.height });
  }
  function bstSvg(root, opts) {
    opts = opts || {};
    var layout = bstLayout(root, opts), marked = [];
    if (opts.mark) {
      layout.nodes.forEach(function (nd) { if (opts.mark(nd.node)) marked.push(nd.id); });
    }
    var radius = opts.radius === undefined
      ? Math.max(6, Math.min(14, Math.floor(96 / (layout.depth + 1)))) : opts.radius;
    return treeSvg(layout, {
      highlight: marked, radius: radius,
      note: opts.note ? function (nd) { return opts.note(nd.node); } : null
    });
  }
  function drawBst(el, root, opts) {
    var s = root ? bstSvg(root, opts) : '<text x="20" y="40" font-size="12" '
      + 'fill="var(--muted)">the tree is empty</text>';
    if (el) el.innerHTML = s;
    return s;
  }
  /* A skip list: one row per level, a node drawn where its key sits in sorted
     order, and the search path picked out. The express lanes are the lesson, so
     the row a node is missing from matters as much as the rows it is in. */
  function skipListSvg(sorted, maxLevel, path) {
    var n = sorted.length, colW = n > 1 ? (596 / (n - 1)) : 0;
    var rowH = Math.max(16, Math.min(34, Math.floor(196 / (maxLevel + 1))));
    var onPath = {};
    (path || []).forEach(function (p) { onPath[p.level + ':' + p.key] = true; });
    var s = '', lvl, i;
    for (lvl = maxLevel; lvl >= 0; lvl -= 1) {
      var y = 22 + (maxLevel - lvl) * rowH, prevX = null;
      s += '<text x="0" y="' + (y + 4) + '" font-size="10" fill="var(--muted)">L' + lvl + '</text>';
      for (i = 0; i < n; i += 1) {
        if (sorted[i].level < lvl) continue;
        var x = 34 + i * colW;
        if (prevX !== null) s += '<line x1="' + prevX.toFixed(1) + '" y1="' + y + '" x2="'
          + x.toFixed(1) + '" y2="' + y + '" stroke="var(--line-strong)" stroke-width="1.4" />';
        var hot = onPath[lvl + ':' + sorted[i].key];
        s += '<circle cx="' + x.toFixed(1) + '" cy="' + y + '" r="' + (rowH >= 24 ? 8 : 6)
          + '" fill="var(' + (hot ? '--cyan' : '--panel-3')
          + ')" stroke="var(--line-strong)" stroke-width="1.4" />';
        prevX = x;
      }
    }
    var base = 22 + maxLevel * rowH + 20;
    for (i = 0; i < n; i += 1) {
      if (n <= 20 || i % 2 === 0) {
        s += '<text x="' + (34 + i * colW).toFixed(1) + '" y="' + base
          + '" text-anchor="middle" font-size="9" fill="var(--muted)">' + sorted[i].key + '</text>';
      }
    }
    return s;
  }
  function drawSkipList(el, sorted, maxLevel, path) {
    var s = skipListSvg(sorted, maxLevel, path);
    if (el) el.innerHTML = s;
    return s;
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

    The readout opens as a dash, so a lab whose script died shows dashes rather
    than a plausible number that nothing computed.
    """
    return (
        '        <div id="%sRow">\n'
        '          <div class="range-row"><label class="small-copy" for="%s" id="%sLab">%s</label>'
        '<span class="range-value" id="%sOut">&mdash;</span></div>\n'
        '          <input id="%s" type="range" min="%d" max="%d" step="%d" value="%d" />\n'
        "        </div>\n" % (cid, cid, cid, label, cid, cid, lo, hi, step, value)
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


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>\n' % (cid, text)


def _swatch(tone, text):
    return '<span class="%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)


def _toolbar(name, sub, legend=""):
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n' % (name, sub)
        + ('        <div class="inline-legend">%s</div>\n' % legend if legend else "")
        + "      </div>\n"
    )


def _stage(cid, svg_id, label, height, width=520):
    return (
        '      <div class="lab-stage" id="%s" tabindex="0" role="region" aria-label="%s">'
        '<svg id="%s" style="min-width:%dpx" viewBox="0 0 %d %d" role="img" aria-label="%s">'
        "</svg></div>\n" % (cid, label, svg_id, width, width, height, label)
    )


def _table(cid):
    return (
        '      <div class="table-wrap" style="margin-top:12px;">'
        '<table class="tt" id="%s"></table></div>\n' % cid
    )


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


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
        raise ValueError("tree mode %r: preset must be a key or an index" % mode)
    if isinstance(want, int):
        if 0 <= want < len(presets):
            return want
        raise ValueError(
            "tree mode %r has %d presets; index %d is out of range" % (mode, len(presets), want)
        )
    if want in keys:
        return keys.index(want)
    raise ValueError(
        "tree mode %r has no preset %r; known presets: %s" % (mode, want, ", ".join(keys))
    )


# Every mode needs the rationals, the counter convention, the renderer and the
# engine. The seeded stream, the plot and the logarithm are added only by the
# modes that use them, because the ceiling on a published page is 62 KB gzipped.
_CORE_JS = RATIONAL_JS + COUNT_JS + TREEDRAW_JS + TREE_JS + TREEKIT_JS
_SEED_JS = STREAM_JS + SEEDED_JS
_BASIC_JS = _CORE_JS
_DEPTH_JS = RATIONAL_JS + COUNT_JS + RFIXED_JS + SERIES_JS + STREAM_JS + SEEDED_JS \
    + APPROX_JS + TREEDRAW_JS + TREE_JS + TREEKIT_JS
_TREAP_JS = RATIONAL_JS + COUNT_JS + RFIXED_JS + STREAM_JS + SEEDED_JS + APPROX_JS \
    + TREEDRAW_JS + TREE_JS + TREEKIT_JS
_SKIP_JS = RATIONAL_JS + COUNT_JS + RFIXED_JS + SERIES_JS + STREAM_JS + SEEDED_JS \
    + TREEDRAW_JS + TREE_JS + TREEKIT_JS


# ================================================================== mode: bst

BST_PRESETS = [
    {"key": "two-child-delete", "label": "build a tree, then delete a node with two children",
     "ops": "50 30 70 20 40 60 80 -30"},
    {"key": "delete-the-root", "label": "delete the root, so the successor comes from the far side",
     "ops": "50 30 70 20 40 60 80 -50"},
    {"key": "degenerate", "label": "insert in sorted order and get a path",
     "ops": "10 20 30 40 50 60"},
    {"key": "search", "label": "build, then look two keys up",
     "ops": "50 30 70 20 40 60 80 ?40 ?55"},
]

BST_SCRIPT = r"""
  var stage = document.getElementById('tbTree');
  var oddEl = document.getElementById('tbLocal');
  var table = document.getElementById('tbTable');
  var status = document.getElementById('tbStatus');
  var preset = document.getElementById('tbPreset');
  var box = document.getElementById('tbOps');
  var step = document.getElementById('tbStep');
  var CAP = 24;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('bst: no preset named ' + preset.value);
  }
  function applyPreset() { box.value = presetOf().ops; }

  function redraw() {
    var parsed = treeParseOps(box.value, CAP);
    var run = bstRun(parsed.ops);
    var last = Math.max(0, run.trace.length - 1);
    var at = Math.min(+step.value, last);
    document.getElementById('tbStepOut').textContent = run.trace.length
      ? ('after operation ' + (at + 1) + ' of ' + run.trace.length) : 'nothing to run';

    var frame = run.trace.length ? run.trace[at] : null;
    drawBst(stage, frame ? frame.tree : null, {
      width: 660, height: 210,
      mark: function (nd) { return frame && nd.key === frame.key; }
    });

    var odd = localOnlyTree();
    drawBst(oddEl, odd, { width: 520, height: 170, radius: 14 });

    document.getElementById('tbHeight').textContent = run.result.height;
    document.getElementById('tbNodes').textContent = run.result.inorder.length;
    document.getElementById('tbCompares').textContent = (run.counts.compares || 0);
    document.getElementById('tbValid').textContent = run.result.valid
      ? 'a search tree' : 'NOT a search tree';
    document.getElementById('tbLocalCheck').textContent = bstLocallyValid(odd)
      ? 'passes the local check' : 'fails the local check';
    document.getElementById('tbGlobalCheck').textContent = bstValid(odd, null, null)
      ? 'passes the global check' : 'fails the global check';
    document.getElementById('tbNote').textContent = frame ? frame.note : '—';

    var rows = '';
    run.trace.forEach(function (t, i) {
      rows += '<tr' + (i === at ? ' class="tone-cyan"' : '') + '><td>' + (i + 1) + '</td><td>'
        + t.op + '</td><td>' + t.key + '</td><td>' + t.note + '</td><td class="tt">'
        + (t.inorder.length ? t.inorder.join(' ') : 'empty') + '</td><td>'
        + (t.valid ? 'yes' : 'NO') + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>step</th><th>operation</th><th>key</th><th>what happened</th>'
      + '<th>in-order</th><th>still a search tree</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = '';
    if (parsed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + parsed.ignored.join(' ')
        + '</span> &mdash; write a number to insert it, a minus sign before it to delete it, a '
        + 'question mark before it to search for it. ';
    }
    if (parsed.truncated) msg += 'Only the first ' + CAP + ' operations are run. ';
    if (!run.trace.length) {
      status.innerHTML = msg + 'Type some operations to run them.';
      return;
    }
    var deletions = run.trace.filter(function (t) {
      return t.op === 'delete' && /successor/.test(t.note);
    });
    msg += 'The tree holds ' + run.result.inorder.length
      + (run.result.inorder.length === 1 ? ' key' : ' keys') + ' at height <strong>'
      + run.result.height + '</strong>, and reading it in order gives <span class="tt">'
      + run.result.inorder.join(' ') + '</span> &mdash; sorted, which is the invariant, not a '
      + 'coincidence. ' + (run.counts.compares || 0) + ' comparisons were counted. ';
    if (deletions.length) {
      msg += '<span class="tone-cyan">Deleting a node with two children</span> could not just '
        + 'remove it: ' + deletions[0].note + ', because the in-order successor is the smallest '
        + 'key above the one leaving and has no left child by construction, so removing IT is the '
        + 'easy case. ';
    }
    msg += '<span class="tone-red">The search-tree property is not a local check.</span> '
      + 'The small tree beside the big one has every node between its two children &mdash; 10 '
      + 'below 20, 30 above it, 25 above 10 &mdash; so it '
      + (bstLocallyValid(odd) ? 'passes' : 'fails') + ' a check that compares each node with its '
      + 'children, and it ' + (bstValid(odd, null, null) ? 'passes' : 'fails')
      + ' the real one. 25 is in 20&rsquo;s LEFT subtree, so a search for 25 turns left at 20 and '
      + 'then right past it, and never finds it. The invariant is about whole subtrees.';
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  box.addEventListener('input', redraw);
  step.addEventListener('input', redraw);
  redraw(); window.redrawLab = redraw;
"""


def _bst(cfg):
    p = BST_PRESETS[_preset_index(cfg, BST_PRESETS, "bst")]
    markup = (
        _toolbar(
            "Insert, search, and the two-child delete",
            "the invariant checked globally, with the local check's counterexample beside it",
            _swatch("tone-cyan", "the key this step touched")
            + _swatch("tone-muted", "the rest of the tree"),
        )
        + _stage("tbStage", "tbTree", "The search tree after the chosen operation.", 240, 660)
        + _stage("tbCounter", "tbLocal",
                 "A tree that passes a local parent-child check and is not a search tree.", 190)
        + _table("tbTable")
        + _banner("tbStatus")
    )
    controls = (
        _select("tbPreset", "Worked example",
                [(q["key"], q["label"]) for q in BST_PRESETS], p["key"])
        + _text("tbOps", "Operations", p["ops"])
        + _range("tbStep", "show the tree after", 0, 23, 7)
        + _kpi([
            ("tbHeight", "Height"),
            ("tbNodes", "Keys held"),
            ("tbCompares", "Comparisons counted"),
            ("tbValid", "This tree"),
            ("tbNote", "What this step did"),
            ("tbLocalCheck", "The small tree, locally"),
            ("tbGlobalCheck", "The small tree, globally"),
        ])
        + _hint(
            "tbHint",
            "Write <span class=\"tt\">40</span> to insert, <span class=\"tt\">-40</span> to "
            "delete, <span class=\"tt\">?40</span> to search. Every comparison is counted as the "
            "operation runs, and the in-order column is read off the tree after each step "
            "&mdash; if it is ever out of order the invariant has been broken.",
        )
    )
    return Lab(
        title="Binary search trees, operated by hand",
        subtitle="Delete a node with two children and watch its successor move up",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Run a sequence, step through it, check the invariant"),
        panel_intro=cfg.get(
            "panel_intro",
            "Everything left of a node is below it and everything right is above it — at every "
            "node, about whole subtrees. The second picture is a tree that satisfies the same "
            "claim about each node and its two children and is not a search tree at all.",
        ),
        script=_BASIC_JS + cfg_literal("PRESETS", BST_PRESETS) + BST_SCRIPT,
    )


# =============================================================== mode: orders

ORDERS_PRESETS = [
    {"key": "sorted", "label": "sorted input, which gives a path", "order": "sorted",
     "n": 15, "seed": 7},
    {"key": "shuffled", "label": "a seeded shuffle of the same keys", "order": "shuffled",
     "n": 15, "seed": 7},
    {"key": "bisect", "label": "middle first, which gives the shortest tree", "order": "bisect",
     "n": 15, "seed": 7},
]

ORDERS_SCRIPT = r"""
  var stage = document.getElementById('toTree');
  var plot = document.getElementById('toPlot');
  var table = document.getElementById('toTable');
  var status = document.getElementById('toStatus');
  var preset = document.getElementById('toPreset');
  var orderSel = document.getElementById('toOrder');
  var own = document.getElementById('toOwn');
  var KINDS = ['sorted', 'reversed', 'shuffled', 'bisect'];
  var NAMES = { sorted: 'sorted', reversed: 'reversed', shuffled: 'seeded shuffle',
                bisect: 'middle first', own: 'the order you typed' };
  var SWEEP = [4, 8, 12, 16, 24, 32, 48, 64];
  var CAP = 20;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('orders: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    orderSel.value = p.order;
    document.getElementById('toN').value = p.n;
    document.getElementById('toSeed').value = p.seed;
  }

  function redraw() {
    var n = +document.getElementById('toN').value;
    var seed = +document.getElementById('toSeed').value;
    var kind = orderSel.value;
    document.getElementById('toNOut').textContent = n + ' keys';
    document.getElementById('toSeedOut').textContent = 'seed ' + seed;
    document.getElementById('toOwnField').hidden = kind !== 'own';
    document.getElementById('toNRow').hidden = kind === 'own';
    document.getElementById('toSeedRow').hidden = kind !== 'shuffled';

    var typed = treeParseKeys(own.value, CAP);
    var order = kind === 'own' ? typed.keys : insertOrder(kind, n, seed);
    if (!order.length) {
      stage.innerHTML = '';
      table.innerHTML = '';
      status.innerHTML = 'Type some keys to insert, in the order you want them inserted.';
      return;
    }
    var run = bstFromOrder(order);
    var r = run.result;
    drawBst(stage, r.root, { width: 660, height: 230 });

    var asym = randomBstDepthApprox(order.length);
    document.getElementById('toHeight').textContent = r.height + ' — counted';
    document.getElementById('toMean').textContent = Rtext(r.meanDepth) + ' = '
      + Rfixed(r.meanDepth, 3) + ' — counted';
    document.getElementById('toAsym').textContent = asym.toFixed(3) + ' — asymptotic';
    document.getElementById('toCompares').textContent = (run.counts.compares || 0);
    document.getElementById('toWorst').textContent = (order.length - 1) + ' — sorted input';
    document.getElementById('toBest').textContent = bstFromOrder(
      insertOrder('bisect', order.length, seed)).result.height + ' — middle first';

    var values = SWEEP.map(function (k) {
      return Rnum(bstFromOrder(insertOrder(kind === 'own' ? 'shuffled' : kind, k, seed))
        .result.meanDepth);
    });
    drawSeries(plot, [
      { label: 'mean depth counted', colour: 'var(--cyan)', points: true, values: values },
      { label: '2 ln n', colour: 'var(--amber)', dashed: true,
        values: predicted(SWEEP, randomBstDepthApprox) }
    ], SWEEP, { xlabel: 'n' });

    var rows = '';
    KINDS.forEach(function (k) {
      var got = bstFromOrder(insertOrder(k, order.length, seed)).result;
      rows += '<tr' + (k === kind ? ' class="tone-cyan"' : '') + '><td>' + NAMES[k] + '</td><td>'
        + got.height + '</td><td class="tt">' + Rtext(got.meanDepth) + '</td><td>'
        + Rfixed(got.meanDepth, 3) + '</td><td class="tone-amber">' + asym.toFixed(3)
        + '</td></tr>';
    });
    if (kind === 'own') {
      rows += '<tr class="tone-cyan"><td>' + NAMES.own + '</td><td>' + r.height + '</td>'
        + '<td class="tt">' + Rtext(r.meanDepth) + '</td><td>' + Rfixed(r.meanDepth, 3)
        + '</td><td class="tone-amber">' + asym.toFixed(3) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>insertion order</th><th>height, counted</th>'
      + '<th>mean depth, exactly</th><th>mean depth, as a decimal</th>'
      + '<th>2 ln n, asymptotic</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = '';
    if (kind === 'own' && typed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + typed.ignored.join(' ')
        + '</span> &mdash; keys are non-negative whole numbers. ';
    }
    msg += 'The same ' + order.length + ' keys in the ' + NAMES[kind] + ' order give a tree of '
      + 'height <strong>' + r.height + '</strong> and mean depth <strong>' + Rtext(r.meanDepth)
      + '</strong> = ' + Rfixed(r.meanDepth, 3) + '. Sorted input would give height '
      + (order.length - 1) + '; middle-first would give '
      + bstFromOrder(insertOrder('bisect', order.length, seed)).result.height
      + '. <span class="tone-cyan">The key set does not decide the tree; the order does.</span> '
      + '<span class="tone-amber">2 ln n reads ' + asym.toFixed(3) + ' here, and it is neither '
      + 'of the two numbers above it.</span> It is an ASYMPTOTIC statement about the MEAN DEPTH '
      + 'of a tree built from a uniformly random order &mdash; not the height, and not this '
      + 'tree: the height counted here is ' + r.height + ' and the mean depth counted here is '
      + Rfixed(r.meanDepth, 3) + '. At these sizes the asymptote is out by tens of per cent, '
      + 'which is what an asymptote is entitled to be. It is drawn dashed for exactly that '
      + 'reason. The recurrence behind the expected-height result is the one randomised '
      + 'quicksort solves in the next course, and the treap is what closes the loop.';
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  orderSel.addEventListener('change', redraw);
  own.addEventListener('input', redraw);
  ['toN', 'toSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _orders(cfg):
    p = ORDERS_PRESETS[_preset_index(cfg, ORDERS_PRESETS, "orders")]
    markup = (
        _toolbar(
            "One key set, four insertion orders",
            "the height and the mean depth are counted; the dashed curve is an asymptote",
            _swatch("tone-cyan", "counted")
            + _swatch("tone-amber", "2 ln n, asymptotic")
            + _swatch("tone-muted", "the other orders"),
        )
        + _stage("toStage", "toTree", "The tree the chosen insertion order builds.", 260, 660)
        + _stage("toPlotStage", "toPlot",
                 "Mean depth counted at growing n against the 2 ln n asymptote.", 224)
        + _table("toTable")
        + _banner("toStatus")
    )
    controls = (
        _select("toPreset", "Worked example",
                [(q["key"], q["label"]) for q in ORDERS_PRESETS], p["key"])
        + _select("toOrder", "Insertion order",
                  [("sorted", "sorted"), ("reversed", "reversed"),
                   ("shuffled", "a seeded shuffle"), ("bisect", "middle first"),
                   ("own", "the order you type")], p["order"])
        + _range("toN", "keys n", 3, 20, p["n"])
        + _range("toSeed", "shuffle seed", 1, 40, p["seed"])
        + _text("toOwn", "Your order", "50 30 70 20 40 60 80")
        + _kpi([
            ("toHeight", "Height of this tree"),
            ("toMean", "Mean depth of this tree"),
            ("toAsym", "2 ln n"),
            ("toCompares", "Comparisons to build it"),
            ("toWorst", "Height from sorted input"),
            ("toBest", "Height from middle-first"),
        ])
        + _hint(
            "toHint",
            "Three different numbers sit side by side here and the lesson is that they are "
            "different: the HEIGHT of this tree, counted; the MEAN DEPTH of this tree, an exact "
            "fraction; and 2 ln n, which is the asymptotic mean depth of a tree built from a "
            "uniformly random order and is about neither of them at these sizes.",
        )
    )
    return Lab(
        title="The shape problem: order decides the tree",
        subtitle="Height and mean depth counted, with 2 ln n drawn dashed as the asymptote it is",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Insert the same keys four ways"),
        panel_intro=cfg.get(
            "panel_intro",
            "Sorted input gives a path of height `n − 1`; middle-first gives the shortest tree "
            "the keys admit; a seeded shuffle gives something close to `O(log n)`. The dashed "
            "`2 ln n` is an asymptote for the mean depth, not a prediction of this tree's height.",
        ),
        script=_DEPTH_JS + cfg_literal("PRESETS", ORDERS_PRESETS) + ORDERS_SCRIPT,
    )


# =============================================================== mode: rotate

ROTATE_PRESETS = [
    {"key": "right-heavy", "label": "a left-leaning tree, rotated right at the root",
     "keys": "50 30 70 20 40 10", "node": 4, "dir": "right"},
    {"key": "left-heavy", "label": "a right-leaning tree, rotated left at the root",
     "keys": "20 10 40 30 50 60", "node": 1, "dir": "left"},
    {"key": "inner", "label": "a rotation below the root",
     "keys": "50 30 70 20 40 35 45", "node": 1, "dir": "left"},
]

ROTATE_SCRIPT = r"""
  var before = document.getElementById('trBefore');
  var after = document.getElementById('trAfter');
  var table = document.getElementById('trTable');
  var status = document.getElementById('trStatus');
  var preset = document.getElementById('trPreset');
  var box = document.getElementById('trKeys');
  var dirSel = document.getElementById('trDir');
  var nodeSlider = document.getElementById('trNode');
  var CAP = 15;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('rotate: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    box.value = p.keys;
    nodeSlider.value = p.node;
    dirSel.value = p.dir;
  }
  function balanceNote(nd) { return 'b ' + (bstHeight(nd.l) - bstHeight(nd.r)); }

  function redraw() {
    var parsed = treeParseKeys(box.value, CAP);
    if (!parsed.keys.length) {
      before.innerHTML = ''; after.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'Type some keys to build a tree.';
      return;
    }
    var root = bstFromOrder(parsed.keys).result.root;
    var keys = bstInorder(root);
    var idx = Math.min(+nodeSlider.value, keys.length - 1);
    var pivot = keys[idx];
    var dir = dirSel.value;
    document.getElementById('trNodeOut').textContent = 'rotate at ' + pivot;

    var out = rotateAt(root, pivot, dir);
    drawBst(before, root, { width: 520, height: 180, radius: 13,
                            mark: function (nd) { return nd.key === pivot; },
                            note: balanceNote });
    drawBst(after, out.root, { width: 520, height: 180, radius: 13,
                               mark: function (nd) { return nd.key === pivot; },
                               note: balanceNote });

    var inBefore = bstInorder(root).join(' '), inAfter = bstInorder(out.root).join(' ');
    var n = keys.length, bound = avlHeightBound(n);
    document.getElementById('trSame').textContent = inBefore === inAfter
      ? 'unchanged' : 'CHANGED, which would be a bug';
    document.getElementById('trDone').textContent = out.rotated
      ? 'performed' : 'not possible: that child is missing';
    document.getElementById('trHBefore').textContent = bstHeight(root);
    document.getElementById('trHAfter').textContent = bstHeight(out.root);
    document.getElementById('trNodes').textContent = n;
    document.getElementById('trBound').textContent = bound + ' at ' + n + ' nodes';
    document.getElementById('trMin').textContent = minAvlNodes(bstHeight(out.root)).n + ' nodes';

    var rows = '';
    minAvlNodes(Math.max(6, bound + 2)).rows.forEach(function (r) {
      rows += '<tr' + (r.h === bound ? ' class="tone-cyan"' : '') + '><td>' + r.h + '</td><td>'
        + r.n + '</td><td>' + (r.h >= 2 ? 'N(' + (r.h - 1) + ') + N(' + (r.h - 2) + ') + 1'
                                        : 'by definition') + '</td><td>'
        + (r.n <= n ? 'fits inside ' + n + ' nodes' : 'needs more than ' + n) + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>height h</th><th>N(h), fewest nodes</th>'
      + '<th>from the recurrence</th><th>against this tree</th></tr></thead><tbody>' + rows
      + '</tbody>';

    status.innerHTML = 'Rotating ' + dir + ' at <strong>' + pivot + '</strong> '
      + (out.rotated
          ? 'lifts its ' + (dir === 'right' ? 'left' : 'right') + ' child into its place. '
          : '<span class="tone-red">is not possible</span>: ' + pivot + ' has no '
            + (dir === 'right' ? 'left' : 'right') + ' child to lift, so nothing moved. ')
      + 'The in-order sequence is <span class="tt">' + inAfter + '</span>, which is '
      + (inBefore === inAfter ? '<strong>exactly what it was</strong>'
                              : '<span class="tone-red">not what it was</span>')
      + '. <span class="tone-cyan">No key changes its in-order position; only pointers move</span> '
      + '&mdash; which is why a rotation preserves the search-tree property and why every '
      + 'balanced tree is allowed to use one. The height went from ' + bstHeight(root) + ' to '
      + bstHeight(out.root) + ', and the small numbers above the circles are balance factors, '
      + 'the left height minus the right. Requiring every one of them to be &minus;1, 0 or 1 '
      + 'forces the height down: the smallest AVL tree of height h has N(h) = N(h&minus;1) + '
      + 'N(h&minus;2) + 1 nodes, which is Fibonacci growth, so ' + n + ' nodes cannot be taller '
      + 'than <strong>' + bound + '</strong>. That table is the bound, evaluated from the '
      + 'recurrence rather than quoted as 1.44 log&#8322; n.';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  dirSel.addEventListener('change', redraw);
  box.addEventListener('input', redraw);
  nodeSlider.addEventListener('input', redraw);
  redraw(); window.redrawLab = redraw;
"""


def _rotate(cfg):
    p = ROTATE_PRESETS[_preset_index(cfg, ROTATE_PRESETS, "rotate")]
    markup = (
        _toolbar(
            "One rotation, before and after",
            "the in-order sequence is the thing that must not change",
            _swatch("tone-cyan", "the node rotated") + _swatch("tone-muted", "balance factors"),
        )
        + _stage("trStageA", "trBefore", "The tree before the rotation, with balance factors.", 200)
        + _stage("trStageB", "trAfter", "The same tree after the rotation.", 200)
        + _table("trTable")
        + _banner("trStatus")
    )
    controls = (
        _select("trPreset", "Worked example",
                [(q["key"], q["label"]) for q in ROTATE_PRESETS], p["key"])
        + _text("trKeys", "Keys, in insertion order", p["keys"])
        + _range("trNode", "which node to rotate at", 0, 14, p["node"])
        + _select("trDir", "Direction",
                  [("right", "right: lift the left child"),
                   ("left", "left: lift the right child")], p["dir"])
        + _kpi([
            ("trSame", "In-order sequence"),
            ("trDone", "The rotation"),
            ("trHBefore", "Height before"),
            ("trHAfter", "Height after"),
            ("trNodes", "Nodes"),
            ("trBound", "Tallest an AVL tree may be"),
            ("trMin", "Fewest nodes at that height"),
        ])
        + _hint(
            "trHint",
            "The slider picks the node by its position in sorted order, so it always names a node "
            "that exists. The N(h) table is the recurrence N(h) = N(h&minus;1) + N(h&minus;2) + 1 "
            "evaluated, and the height bound is the largest h whose N(h) still fits inside this "
            "tree &mdash; a search over the recurrence, with no logarithm anywhere near it.",
        )
    )
    return Lab(
        title="Rotations and the AVL invariant",
        subtitle="A local rewrite that moves pointers and leaves the sorted order alone",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Rotate a node and check what did not change"),
        panel_intro=cfg.get(
            "panel_intro",
            "A rotation lifts one child into its parent's place and rehangs one subtree. Nothing "
            "else moves, and no key changes its position in sorted order — which is the whole "
            "licence every balanced tree operates under.",
        ),
        script=_BASIC_JS + cfg_literal("PRESETS", ROTATE_PRESETS) + ROTATE_SCRIPT,
    )


# ================================================================== mode: avl

AVL_PRESETS = [
    {"key": "ascending", "label": "insert one to ten in order",
     "keys": "1 2 3 4 5 6 7 8 9 10", "count": 10},
    {"key": "ll", "label": "the outside case on the left", "keys": "30 20 10", "count": 3},
    {"key": "lr", "label": "the inside case on the left, which needs two rotations",
     "keys": "30 10 20", "count": 3},
    {"key": "rl", "label": "the inside case on the right", "keys": "10 30 20", "count": 3},
    {"key": "mixed", "label": "a sequence that produces all four cases",
     "keys": "50 25 75 10 5 30 27 60 90 80 70 98 62", "count": 13},
]

AVL_SCRIPT = r"""
  var stage = document.getElementById('taTree');
  var plain = document.getElementById('taPlain');
  var table = document.getElementById('taTable');
  var status = document.getElementById('taStatus');
  var preset = document.getElementById('taPreset');
  var box = document.getElementById('taKeys');
  var count = document.getElementById('taCount');
  var CAP = 20;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('avl: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    box.value = p.keys;
    count.value = p.count;
  }
  function balanceNote(nd) { return 'b ' + (bstHeight(nd.l) - bstHeight(nd.r)); }

  function redraw() {
    var parsed = treeParseKeys(box.value, CAP);
    var all = parsed.keys;
    var upto = Math.max(1, Math.min(+count.value, all.length));
    document.getElementById('taCountOut').textContent = all.length
      ? ('after ' + upto + ' of ' + all.length + ' inserts') : 'nothing to insert';
    if (!all.length) {
      stage.innerHTML = ''; plain.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'Type some keys to insert.';
      return;
    }
    var keys = all.slice(0, upto);
    var run = avlInsert(keys);
    var r = run.result;
    drawBst(stage, r.root, { width: 660, height: 210, note: balanceNote });
    drawBst(plain, bstFromOrder(keys).result.root, { width: 520, height: 190 });

    var cases = {};
    run.trace.forEach(function (t) { cases[t.rebalance] = (cases[t.rebalance] || 0) + 1; });
    var named = Object.keys(cases).sort();
    var doubles = (cases.LR || 0) + (cases.RL || 0);
    document.getElementById('taHeight').textContent = r.height;
    document.getElementById('taPlainH').textContent = r.plainHeight;
    document.getElementById('taRots').textContent = r.rebalances;
    document.getElementById('taCases').textContent = named.length ? named.join(', ') : 'none yet';
    document.getElementById('taDoubles').textContent = doubles;
    document.getElementById('taMin').textContent = r.minNodesForHeight + ' nodes';
    document.getElementById('taBound').textContent = avlHeightBound(keys.length);

    var rows = '';
    run.trace.forEach(function (t, i) {
      var dbl = t.rebalance === 'LR' || t.rebalance === 'RL';
      rows += '<tr' + (dbl ? ' class="tone-amber"' : '') + '><td>' + (i + 1) + '</td><td>'
        + t.key + '</td><td>' + t.rebalance + '</td><td>'
        + (dbl ? 'double: two rotations' : 'single: one rotation') + '</td><td>' + t.root
        + '</td></tr>';
    });
    if (!rows) rows = '<tr><td colspan="5">no rebalance was needed yet</td></tr>';
    table.innerHTML = '<thead><tr><th>#</th><th>inserting</th><th>case</th><th>fix</th>'
      + '<th>new subtree root</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = '';
    if (parsed.ignored.length) {
      msg += '<span class="tone-red">Ignored ' + parsed.ignored.join(' ')
        + '</span> &mdash; keys are non-negative whole numbers. ';
    }
    msg += upto + (upto === 1 ? ' insertion' : ' insertions') + ' needed <strong>' + r.rebalances + '</strong> rebalance'
      + (r.rebalances === 1 ? '' : 's') + ' and left the tree at height <strong>' + r.height
      + '</strong>. The same keys in the same order, inserted into a plain search tree, give '
      + 'height <strong>' + r.plainHeight + '</strong>. ';
    if (doubles) {
      msg += '<span class="tone-amber">' + doubles
        + (doubles === 1 ? ' of those was a double rotation' : ' of those were double rotations')
        + '</span> &mdash; the LR and RL cases, where the new key went into the INSIDE grandchild. A '
        + 'single rotation there swaps the two sides of the problem without fixing it, which is '
        + 'why the inside cases need two. ';
    } else if (r.rebalances) {
      msg += 'All of them were single rotations, the LL and RR cases, where the new key went into '
        + 'the outside grandchild. Insert 30, 10, 20 to get an inside case instead. ';
    }
    msg += 'Requiring the left and right heights to differ by at most 1 at every node bounds '
      + 'the height at <strong>' + avlHeightBound(keys.length) + '</strong> for ' + keys.length
      + ' nodes: an AVL tree of height ' + r.height + ' needs at least ' + r.minNodesForHeight
      + ' nodes, by the Fibonacci recurrence N(h) = N(h&minus;1) + N(h&minus;2) + 1. One fix at '
      + 'the lowest unbalanced ancestor restores the invariant all the way to the root, which is '
      + 'why the rebalance count stays small.';
    status.innerHTML = msg;
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  box.addEventListener('input', redraw);
  count.addEventListener('input', redraw);
  redraw(); window.redrawLab = redraw;
"""


def _avl(cfg):
    p = AVL_PRESETS[_preset_index(cfg, AVL_PRESETS, "avl")]
    markup = (
        _toolbar(
            "AVL insertion, with the case named",
            "four cases, two of which need two rotations",
            _swatch("tone-amber", "a double rotation")
            + _swatch("tone-muted", "balance factors above each node"),
        )
        + _stage("taStage", "taTree", "The AVL tree after the chosen number of insertions.",
                 240, 660)
        + _stage("taPlainStage", "taPlain", "The plain search tree on the same insertion order.",
                 210)
        + _table("taTable")
        + _banner("taStatus")
    )
    controls = (
        _select("taPreset", "Worked example",
                [(q["key"], q["label"]) for q in AVL_PRESETS], p["key"])
        + _text("taKeys", "Keys, in insertion order", p["keys"])
        + _range("taCount", "insert the first", 1, 20, p["count"])
        + _kpi([
            ("taHeight", "AVL height"),
            ("taPlainH", "Plain search tree height"),
            ("taRots", "Rebalances"),
            ("taCases", "Cases seen"),
            ("taDoubles", "Of them, double rotations"),
            ("taMin", "Fewest nodes at this height"),
            ("taBound", "Tallest this many nodes may be"),
        ])
        + _hint(
            "taHint",
            "The case is named as it happens: LL and RR are fixed by one rotation, LR and RL by "
            "two. Insert 30, 10, 20 for an inside case and 30, 20, 10 for an outside one, and "
            "watch the plain tree beside it grow into a path while the AVL tree does not.",
        )
    )
    return Lab(
        title="AVL insertion and the four cases",
        subtitle="One fix at the lowest unbalanced ancestor restores the invariant everywhere",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Insert a sequence and name each rebalance"),
        panel_intro=cfg.get(
            "panel_intro",
            "After an insert, the lowest node whose two subtrees differ in height by two is "
            "fixed by one of four cases. The inside cases need a double rotation, and a single "
            "one there moves the problem rather than removing it.",
        ),
        script=_BASIC_JS + cfg_literal("PRESETS", AVL_PRESETS) + AVL_SCRIPT,
    )


# ============================================================== mode: augment

AUGMENT_PRESETS = [
    {"key": "select", "label": "select the i-th smallest key", "op": "select",
     "keys": "50 25 75 12 37 62 87 6 18", "i": 3, "lo": 20, "hi": 70},
    {"key": "rank", "label": "rank a key", "op": "rank",
     "keys": "50 25 75 12 37 62 87 6 18", "i": 5, "lo": 20, "hi": 70},
    {"key": "range", "label": "count the keys in an interval", "op": "range",
     "keys": "50 25 75 12 37 62 87 6 18", "i": 3, "lo": 20, "hi": 70},
]

AUGMENT_SCRIPT = r"""
  var stage = document.getElementById('tgTree');
  var rotated = document.getElementById('tgRot');
  var table = document.getElementById('tgTable');
  var status = document.getElementById('tgStatus');
  var preset = document.getElementById('tgPreset');
  var opSel = document.getElementById('tgOp');
  var box = document.getElementById('tgKeys');
  var CAP = 15;

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('augment: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    opSel.value = p.op;
    box.value = p.keys;
    document.getElementById('tgI').value = p.i;
    document.getElementById('tgLo').value = p.lo;
    document.getElementById('tgHi').value = p.hi;
  }
  function sizeNote(nd) { return 'size ' + nd.size; }

  function redraw() {
    var parsed = treeParseKeys(box.value, CAP);
    if (!parsed.keys.length) {
      stage.innerHTML = ''; rotated.innerHTML = ''; table.innerHTML = '';
      status.innerHTML = 'Type some keys to build a tree.';
      return;
    }
    var root = bstFromOrder(parsed.keys).result.root;
    var keys = bstInorder(root), n = keys.length;
    var op = opSel.value;
    var i = Math.max(1, Math.min(+document.getElementById('tgI').value, n));
    var lo = +document.getElementById('tgLo').value;
    var hi = Math.max(lo, +document.getElementById('tgHi').value);
    document.getElementById('tgIOut').textContent = op === 'rank'
      ? ('rank of ' + keys[i - 1]) : ('the ' + i + ordinalSuffix(i) + ' smallest');
    document.getElementById('tgLoOut').textContent = 'from ' + lo;
    document.getElementById('tgHiOut').textContent = 'to ' + hi;
    document.getElementById('tgIRow').hidden = op === 'range';
    document.getElementById('tgLoRow').hidden = op !== 'range';
    document.getElementById('tgHiRow').hidden = op !== 'range';

    var query = op === 'select' ? { op: 'select', i: i }
      : (op === 'rank' ? { op: 'rank', key: keys[i - 1] } : { op: 'range', lo: lo, hi: hi });
    var walk = augmentWalk(root, query);
    var touched = {};
    walk.trace.forEach(function (t) { touched[t.node] = true; });
    drawBst(stage, root, { width: 660, height: 210, note: sizeNote,
                           mark: function (nd) { return !!touched[nd.key]; } });

    var spun = rotateAt(root, root.key, root.l ? 'right' : 'left');
    drawBst(rotated, spun.root, { width: 520, height: 190, note: sizeNote });

    var scan = op === 'select' ? keys[i - 1]
      : (op === 'rank' ? i
        : keys.filter(function (k) { return k >= lo && k <= hi; }).length);
    document.getElementById('tgAnswer').textContent = walk.result.value === null
      ? 'no such key' : walk.result.value;
    document.getElementById('tgScan').textContent = String(walk.result.value) === String(scan)
      ? 'agrees with a scan' : 'DISAGREES with a scan';
    document.getElementById('tgVisited').textContent = walk.trace.length + ' of ' + n;
    document.getElementById('tgHeight').textContent = bstHeight(root);
    document.getElementById('tgSizes').textContent = sizesValid(root)
      ? 'every size correct' : 'A SIZE IS STALE';
    document.getElementById('tgAfter').textContent = sizesValid(spun.root)
      ? 'every size still correct' : 'A SIZE WENT STALE';

    var rows = '';
    walk.trace.forEach(function (t, k) {
      rows += '<tr><td>' + (k + 1) + '</td><td>' + t.node + '</td><td>' + t.leftSize + '</td><td>'
        + (t.running === undefined ? (t.want === undefined ? '&mdash;' : t.want) : t.running)
        + '</td><td>' + (t.want === undefined ? '&mdash;' : t.want) + '</td></tr>';
    });
    table.innerHTML = '<thead><tr><th>step</th><th>at node</th><th>left subtree size</th>'
      + '<th>running total</th><th>looking for</th></tr></thead><tbody>' + rows + '</tbody>';

    var msg = 'The answer is <strong>'
      + (walk.result.value === null ? 'no such key' : walk.result.value) + '</strong>, reached in '
      + walk.trace.length + ' node visits out of ' + n + ' keys, at a height of '
      + bstHeight(root) + '. A scan of the in-order list gives ' + scan + ', so the walk '
      + (String(walk.result.value) === String(scan) ? 'agrees with it'
         : '<span class="tone-red">disagrees with it</span>')
      + ' &mdash; and the walk is the lesson, because it is O(height) rather than O(n). '
      + '<span class="tone-cyan">The step readers get wrong is the subtraction at a right '
      + 'turn</span>: going right past a node discards that node and its whole left subtree, so '
      + 'the index drops by leftSize + 1 and the running rank rises by the same. '
      + '<span class="tone-red">The augmentation is not free.</span> The second picture is this '
      + 'tree after one rotation at the root; every subtree size in it has been recomputed from '
      + 'its children, and the panel checks all of them rather than trusting the field &mdash; ';
    msg += (sizesValid(spun.root)
      ? 'they are all still correct, because size is computable from a node&rsquo;s two children '
        + 'in constant time and the rotation recomputes both nodes it moved.'
      : '<span class="tone-red">one of them is stale.</span>')
      + ' That is the test an attribute has to pass to ride along: size, subtree sum and subtree '
      + 'minimum pass it; a median field does not, because a node&rsquo;s median cannot be '
      + 'computed from its two children&rsquo;s medians.';
    status.innerHTML = msg;
  }

  function ordinalSuffix(k) {
    var t = k % 10, h = k % 100;
    if (t === 1 && h !== 11) return 'st';
    if (t === 2 && h !== 12) return 'nd';
    if (t === 3 && h !== 13) return 'rd';
    return 'th';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  opSel.addEventListener('change', redraw);
  box.addEventListener('input', redraw);
  ['tgI', 'tgLo', 'tgHi'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _augment(cfg):
    p = AUGMENT_PRESETS[_preset_index(cfg, AUGMENT_PRESETS, "augment")]
    markup = (
        _toolbar(
            "Subtree sizes, and the walks they buy",
            "rank, select and a range count, none of them a scan",
            _swatch("tone-cyan", "a node the walk visited")
            + _swatch("tone-muted", "its subtree size"),
        )
        + _stage("tgStage", "tgTree", "The size-annotated tree, with the walk picked out.",
                 240, 660)
        + _stage("tgRotStage", "tgRot", "The same tree after one rotation, with sizes recomputed.",
                 210)
        + _table("tgTable")
        + _banner("tgStatus")
    )
    controls = (
        _select("tgPreset", "Worked example",
                [(q["key"], q["label"]) for q in AUGMENT_PRESETS], p["key"])
        + _select("tgOp", "Query",
                  [("select", "select: the i-th smallest key"),
                   ("rank", "rank: how many keys are at most this one"),
                   ("range", "range: how many keys lie in an interval")], p["op"])
        + _text("tgKeys", "Keys, in insertion order", p["keys"])
        + _range("tgI", "which key", 1, 15, p["i"])
        + _range("tgLo", "interval starts at", 0, 100, p["lo"], 1)
        + _range("tgHi", "interval ends at", 0, 100, p["hi"], 1)
        + _kpi([
            ("tgAnswer", "Answer"),
            ("tgScan", "Against a scan"),
            ("tgVisited", "Nodes visited"),
            ("tgHeight", "Height"),
            ("tgSizes", "Sizes before the rotation"),
            ("tgAfter", "Sizes after the rotation"),
        ])
        + _hint(
            "tgHint",
            "Every subtree size shown is recomputed from the tree in your browser and checked "
            "against its two children, before and after a rotation &mdash; an attribute that goes "
            "stale through a rotation shows up here as a failed check rather than as a wrong "
            "answer three queries later.",
        )
    )
    return Lab(
        title="Augmenting a tree with subtree sizes",
        subtitle="Rank and select become walks, and the rotation has to maintain the field",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Ask for a rank, a select or a range count"),
        panel_intro=cfg.get(
            "panel_intro",
            "Storing the size of each subtree turns `rank(k)` and `select(i)` into single "
            "root-to-node walks. The price is that every rotation must recompute the field — and "
            "the panel checks that it did, rather than taking the number on trust.",
        ),
        script=_BASIC_JS + cfg_literal("PRESETS", AUGMENT_PRESETS) + AUGMENT_SCRIPT,
    )


# ================================================================ mode: treap

TREAP_PRESETS = [
    {"key": "sorted-against-shuffled", "label": "sorted against a shuffle of the same keys",
     "n": 12, "seed": 5, "a": "sorted", "b": "shuffled"},
    {"key": "two-shuffles", "label": "two different shuffles of the same keys",
     "n": 12, "seed": 8, "a": "shuffled", "b": "reversed"},
    {"key": "larger", "label": "twenty keys",
     "n": 20, "seed": 5, "a": "sorted", "b": "shuffled"},
]

TREAP_SCRIPT = r"""
  var leftEl = document.getElementById('tpA');
  var rightEl = document.getElementById('tpB');
  var table = document.getElementById('tpTable');
  var status = document.getElementById('tpStatus');
  var preset = document.getElementById('tpPreset');
  var aSel = document.getElementById('tpOrderA');
  var bSel = document.getElementById('tpOrderB');
  var NAMES = { sorted: 'sorted', reversed: 'reversed', shuffled: 'a seeded shuffle',
                bisect: 'middle first' };

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('treap: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    aSel.value = p.a;
    bSel.value = p.b;
    document.getElementById('tpN').value = p.n;
    document.getElementById('tpSeed').value = p.seed;
  }

  function redraw() {
    var n = +document.getElementById('tpN').value;
    var seed = +document.getElementById('tpSeed').value;
    document.getElementById('tpNOut').textContent = n + ' keys';
    document.getElementById('tpSeedOut').textContent = 'seed ' + seed;

    var keys = insertOrder('sorted', n, seed);
    var pri = treapPriorities(keys, seed);
    var orderA = insertOrder(aSel.value, n, seed);
    var orderB = insertOrder(bSel.value, n, seed + 1);
    var A = treapInsert(orderA, prioritiesFor(orderA, pri));
    var B = treapInsert(orderB, prioritiesFor(orderB, pri));

    function note(nd) { return 'p ' + nd.priority; }
    drawBst(leftEl, A.result.root, { width: 520, height: 190, note: note });
    drawBst(rightEl, B.result.root, { width: 520, height: 190, note: note });

    var same = treeShape(A.result.root) === treeShape(B.result.root);
    var asym = randomBstDepthApprox(n);
    var plain = bstFromOrder(orderA).result;
    document.getElementById('tpHeightA').textContent = A.result.height + ' — counted';
    document.getElementById('tpHeightB').textContent = B.result.height + ' — counted';
    document.getElementById('tpSame').textContent = same
      ? 'the same tree, node for node' : 'DIFFERENT, which would refute the claim';
    document.getElementById('tpMean').textContent = Rtext(A.result.meanDepth) + ' = '
      + Rfixed(A.result.meanDepth, 3) + ' — counted';
    document.getElementById('tpAsym').textContent = asym.toFixed(3) + ' — asymptotic';
    document.getElementById('tpRots').textContent = (A.counts.swaps || 0) + ' and '
      + (B.counts.swaps || 0);
    document.getElementById('tpHeap').textContent = A.result.heapOrdered && B.result.heapOrdered
      ? 'heap order holds in both' : 'HEAP ORDER BROKEN';
    document.getElementById('tpPlain').textContent = plain.height + ' — counted';

    var rows = '';
    rows += '<tr><td>' + NAMES[aSel.value] + ' insertion</td><td>' + A.result.height + '</td>'
      + '<td class="tt">' + Rtext(A.result.meanDepth) + '</td><td>'
      + Rfixed(A.result.meanDepth, 3) + '</td><td>' + (A.counts.swaps || 0) + '</td></tr>';
    rows += '<tr><td>' + NAMES[bSel.value] + ' insertion</td><td>' + B.result.height + '</td>'
      + '<td class="tt">' + Rtext(B.result.meanDepth) + '</td><td>'
      + Rfixed(B.result.meanDepth, 3) + '</td><td>' + (B.counts.swaps || 0) + '</td></tr>';
    rows += '<tr class="tone-red"><td>plain search tree, ' + NAMES[aSel.value]
      + ' insertion</td><td>' + plain.height + '</td><td class="tt">'
      + Rtext(plain.meanDepth) + '</td><td>' + Rfixed(plain.meanDepth, 3)
      + '</td><td>0, it has none</td></tr>';
    rows += '<tr class="tone-amber"><td>2 ln n, the asymptote</td><td>&mdash;</td>'
      + '<td class="tt">&mdash;</td><td>' + asym.toFixed(3) + '</td><td>&mdash;</td></tr>';
    table.innerHTML = '<thead><tr><th>tree</th><th>height, counted</th>'
      + '<th>mean depth, exactly</th><th>mean depth, as a decimal</th><th>rotations</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'Each key was given a priority from the seed, and both trees were built '
      + 'from the SAME (key, priority) set in two different insertion orders &mdash; '
      + NAMES[aSel.value] + ' on the left, ' + NAMES[bSel.value] + ' on the right. They are '
      + (same ? '<strong>the same tree, node for node</strong>'
             : '<span class="tone-red">different trees, which would refute the claim</span>')
      + '. That is the point: the treap is the unique tree that is a search tree on the keys and '
      + 'a heap on the priorities, so the insertion order cannot reach it. A plain search tree on '
      + 'the same ' + NAMES[aSel.value] + ' order has height <strong>' + plain.height
      + '</strong> against the treap&rsquo;s <strong>' + A.result.height + '</strong>. '
      + '<span class="tone-red">Rotations here restore heap order only.</span> There is no '
      + 'balance invariant anywhere in a treap and nothing checks one; the depth is a '
      + 'probabilistic consequence of the priorities being random. '
      + '<span class="tone-amber">2 ln n reads ' + asym.toFixed(3) + ', and it is an '
      + 'asymptote</span> for the mean depth of a randomly built tree &mdash; the mean depth '
      + 'counted here is ' + Rfixed(A.result.meanDepth, 3) + ' and the height counted here is '
      + A.result.height + '.';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  [aSel, bSel].forEach(function (el) { el.addEventListener('change', redraw); });
  ['tpN', 'tpSeed'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _treap(cfg):
    p = TREAP_PRESETS[_preset_index(cfg, TREAP_PRESETS, "treap")]
    markup = (
        _toolbar(
            "The same keys, the same priorities, two insertion orders",
            "a search tree on the keys and a heap on the priorities, which fixes the shape",
            _swatch("tone-cyan", "the first order")
            + _swatch("tone-muted", "priorities above each node"),
        )
        + _stage("tpStageA", "tpA", "The treap built by the first insertion order.", 210)
        + _stage("tpStageB", "tpB", "The treap built by the second insertion order.", 210)
        + _table("tpTable")
        + _banner("tpStatus")
    )
    controls = (
        _select("tpPreset", "Worked example",
                [(q["key"], q["label"]) for q in TREAP_PRESETS], p["key"])
        + _select("tpOrderA", "First insertion order",
                  [("sorted", "sorted"), ("reversed", "reversed"),
                   ("shuffled", "a seeded shuffle"), ("bisect", "middle first")], p["a"])
        + _select("tpOrderB", "Second insertion order",
                  [("sorted", "sorted"), ("reversed", "reversed"),
                   ("shuffled", "a seeded shuffle"), ("bisect", "middle first")], p["b"])
        + _range("tpN", "keys n", 4, 24, p["n"])
        + _range("tpSeed", "priority seed", 1, 40, p["seed"])
        + _kpi([
            ("tpHeightA", "Height, first order"),
            ("tpHeightB", "Height, second order"),
            ("tpSame", "The two trees"),
            ("tpMean", "Mean depth"),
            ("tpAsym", "2 ln n"),
            ("tpPlain", "Plain tree, same order"),
            ("tpRots", "Rotations, first and second"),
            ("tpHeap", "Heap order"),
        ])
        + _hint(
            "tpHint",
            "Priorities are ranked rather than taken raw, so no two keys share one &mdash; a tie "
            "would leave the shape undetermined and the claim would fail for a reason that has "
            "nothing to do with treaps. 2 ln n is labelled because it is an asymptote for the "
            "mean depth, not a prediction of either height above it.",
        )
    )
    return Lab(
        title="Treaps: a random priority instead of a balance rule",
        subtitle="The shape is the one a random insertion order would have built, whatever order you use",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Insert the same keys twice, in two different orders"),
        panel_intro=cfg.get(
            "panel_intro",
            "Give every key a random priority and keep heap order on the priorities. The "
            "resulting tree is unique — so two insertion orders of the same `(key, priority)` set "
            "end at the same tree, and the shape no longer depends on the order at all.",
        ),
        script=_TREAP_JS + cfg_literal("PRESETS", TREAP_PRESETS) + TREAP_SCRIPT,
    )


# ============================================================= mode: skiplist

SKIPLIST_PRESETS = [
    {"key": "sixteen", "label": "sixteen keys from one coin tape", "n": 16, "seed": 1, "target": 12},
    {"key": "eight", "label": "eight keys, so every level is readable", "n": 8, "seed": 6,
     "target": 6},
    {"key": "thirty", "label": "thirty keys", "n": 30, "seed": 6, "target": 20},
]

SKIPLIST_SCRIPT = r"""
  var stage = document.getElementById('tsList');
  var plot = document.getElementById('tsPlot');
  var table = document.getElementById('tsTable');
  var status = document.getElementById('tsStatus');
  var preset = document.getElementById('tsPreset');
  var SWEEP = [4, 8, 12, 16, 24, 32];

  function presetOf() {
    for (var i = 0; i < PRESETS.length; i += 1) if (PRESETS[i].key === preset.value) return PRESETS[i];
    throw new Error('skiplist: no preset named ' + preset.value);
  }
  function applyPreset() {
    var p = presetOf();
    document.getElementById('tsN').value = p.n;
    document.getElementById('tsSeed').value = p.seed;
    document.getElementById('tsTarget').value = p.target;
  }
  function build(n, seed) {
    var keys = insertOrder('sorted', n, seed);
    return skipBuild(keys, algoCoins(seed, 8 * n + 16));
  }

  function redraw() {
    var n = +document.getElementById('tsN').value;
    var seed = +document.getElementById('tsSeed').value;
    var run = build(n, seed);
    var r = run.result;
    var idx = Math.max(1, Math.min(+document.getElementById('tsTarget').value, n));
    var target = r.sorted[idx - 1].key;
    document.getElementById('tsNOut').textContent = n + ' keys';
    document.getElementById('tsSeedOut').textContent = 'tape seed ' + seed;
    document.getElementById('tsTargetOut').textContent = 'search for ' + target;

    var found = r.search(target);
    drawSkipList(stage, r.sorted, r.maxLevel, found.path);

    var ref = hopsReference(n);
    document.getElementById('tsMax').textContent = 'L' + r.maxLevel;
    document.getElementById('tsMean').textContent = Rtext(r.meanHops) + ' = '
      + Rfixed(r.meanHops, 3) + ' — counted';
    document.getElementById('tsWorst').textContent = r.worstHops + ' — counted';
    document.getElementById('tsRef').textContent = ref.toFixed(3) + ' — a reference curve';
    document.getElementById('tsThis').textContent = found.hops + ' — counted';
    document.getElementById('tsPromoted').textContent = r.levels.filter(function (l) {
      return l > 0;
    }).length + ' of ' + n;

    drawSeries(plot, [
      { label: 'hops counted', colour: 'var(--cyan)', points: true,
        values: SWEEP.map(function (k) { return Rnum(build(k, seed).result.meanHops); }) },
      { label: '2 log2 n', colour: 'var(--amber)', dashed: true,
        values: predicted(SWEEP, hopsReference) }
    ], SWEEP, { xlabel: 'n' });

    var dist = {};
    r.levels.forEach(function (l) { dist[l] = (dist[l] || 0) + 1; });
    var rows = '';
    for (var lvl = 0; lvl <= r.maxLevel; lvl += 1) {
      var half = n / Math.pow(2, lvl + 1);
      rows += '<tr' + (lvl === r.maxLevel ? ' class="tone-cyan"' : '') + '><td>L' + lvl
        + '</td><td>' + (dist[lvl] || 0) + '</td><td>'
        + r.sorted.filter(function (e) { return e.level >= lvl; }).length + '</td><td>'
        + half.toFixed(2) + '</td></tr>';
    }
    table.innerHTML = '<thead><tr><th>level</th><th>keys whose top level is this</th>'
      + '<th>keys present at this level</th><th>n / 2^(level+1)</th></tr></thead><tbody>'
      + rows + '</tbody>';

    status.innerHTML = 'The coin tape promoted <strong>' + r.levels.filter(function (l) {
      return l > 0;
    }).length + '</strong> of the ' + n + ' keys above the bottom list, and the tallest reached '
      + '<strong>L' + r.maxLevel + '</strong>. Searching for ' + target + ' took <strong>'
      + found.hops + '</strong> hop' + (found.hops === 1 ? '' : 's') + '; over all ' + n
      + ' searches the mean is <strong>'
      + Rtext(r.meanHops) + '</strong> = ' + Rfixed(r.meanHops, 3) + ' and the worst is '
      + r.worstHops + '. <span class="tone-amber">2 log&#8322; n reads ' + ref.toFixed(3)
      + ', and it is a reference curve rather than a count</span> &mdash; it is sampled at double '
      + 'precision, nothing is decided from it, and the hops beside it were counted by walking '
      + 'the list. <span class="tone-cyan">Each key chose its own level once, when it was '
      + 'inserted, from the run of heads at its place on the tape.</span> Nothing is ever '
      + 'rebuilt: there is no global structure to maintain, which is the whole trade against a '
      + 'balanced tree. Change the seed and the levels change; change n and they do not move, '
      + 'because each is local.';
  }

  preset.addEventListener('change', function () { applyPreset(); redraw(); });
  ['tsN', 'tsSeed', 'tsTarget'].forEach(function (id) {
    document.getElementById(id).addEventListener('input', redraw);
  });
  redraw(); window.redrawLab = redraw;
"""


def _skiplist(cfg):
    p = SKIPLIST_PRESETS[_preset_index(cfg, SKIPLIST_PRESETS, "skiplist")]
    markup = (
        _toolbar(
            "Express lanes from a coin tape",
            "hops counted, against a reference curve that is not a count",
            _swatch("tone-cyan", "the search path")
            + _swatch("tone-amber", "2 log2 n, a reference curve"),
        )
        + _stage("tsStage", "tsList", "The skip list, one row per level, with the search path.",
                 250, 660)
        + _stage("tsPlotStage", "tsPlot",
                 "Mean hops counted at growing n against the 2 log2 n reference.", 224)
        + _table("tsTable")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Worked example",
                [(q["key"], q["label"]) for q in SKIPLIST_PRESETS], p["key"])
        + _range("tsN", "keys n", 4, 32, p["n"])
        + _range("tsSeed", "coin tape seed", 1, 40, p["seed"])
        + _range("tsTarget", "search for the key at position", 1, 32, p["target"])
        + _kpi([
            ("tsMax", "Tallest level"),
            ("tsMean", "Mean hops"),
            ("tsWorst", "Worst search"),
            ("tsThis", "Hops for this search"),
            ("tsRef", "2 log2 n"),
            ("tsPromoted", "Keys above the bottom list"),
        ])
        + _hint(
            "tsHint",
            "The tape is the reader's: a key's level is the run of heads at its place on it, "
            "chosen once at insertion and never revisited. The low bit of a power-of-two-modulus "
            "generator is not a coin, so the tape comes from the prime-modulus stream where it "
            "is one.",
        )
    )
    return Lab(
        title="Skip lists: randomness instead of rebalancing",
        subtitle="Each key picks its own level from a coin, and nothing is ever rebuilt",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Fix the tape, then count the hops"),
        panel_intro=cfg.get(
            "panel_intro",
            "Promote each element to the next level while the coin keeps coming up heads. The "
            "search drops a level whenever the next node overshoots, and every hop it takes is "
            "counted — the dashed `2 log₂ n` beside the count is a reference curve, not a claim.",
        ),
        script=_SKIP_JS + cfg_literal("PRESETS", SKIPLIST_PRESETS) + SKIPLIST_SCRIPT,
    )


# --------------------------------------------------------------- the registry

_BUILDERS = {
    "bst": _bst,
    "orders": _orders,
    "rotate": _rotate,
    "avl": _avl,
    "augment": _augment,
    "treap": _treap,
    "skiplist": _skiplist,
}

MODES = tuple(_BUILDERS)


def tree_lab(cfg):
    """The search-tree kit: seven modes across two courses.

    An unknown mode RAISES. A kit that quietly fell back to a default would
    render a finished-looking page carrying another lesson's widget: every
    markup assertion passes, labcheck passes, and the reader is shown one
    lesson's arithmetic under another lesson's title.
    """
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _BUILDERS:
        raise ValueError(
            "tree: unknown mode %r; this kit implements %s"
            % (mode, ", ".join(sorted(_BUILDERS)))
        )
    return _BUILDERS[mode](cfg)


__all__ = ["TREEKIT_JS", "MODES", "tree_lab"]
