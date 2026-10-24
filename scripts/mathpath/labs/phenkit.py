"""phenkit -- the lab kit of Phenomenology of Perception, Read Along.

Specified in docs/phenomenology/PLAN.md section D (D.0 conventions, D.1 the
fifteen modes, D.3 what the kit must never do); the report an author
configures a lesson from is docs/phenomenology/kit-report.md. Fifteen modes:

  stimulus     a named model's prediction from two measured magnitudes, beside
               a reported difference                                (family 1)
  grouping     the Gestalt proximity rule over dots on a line          (1)
  cues         remembered words that fit a partly seen word; the candidates
               a judgement-from-signs account keeps as cues arrive     (1)
  size         angular size; the retinal-image and unconscious-inference
               predictions and a Brunswik ratio                        (1)
  perspective  faces seen from view directions of whole-number length; the
               two readings of one parallel-projection drawing          (1)
  variation    the invariant core of a set of coded variants           (2)
  cases        observations x the opponents' accounts, counted         (2)
  schema       body-relative coordinates; habitual and present reach; a
               tool's reach; obstacles against a project and a level   (3)
  sorting      a categorical sort against a chain of resemblances      (3)
  level        tilt as image minus a spatial level, re-anchored        (3)
  depth        convergence and disparity as the classical theory computes
               them                                                    (1)
  motion       implied speed and Wertheimer's bands                    (1)
  light        luminance as reflectance x illumination, and the ratio to a
               surround                                                (1)
  triangle     the angles of a triangle through a parallel at a vertex (3)
  time         the river from two standpoints; Husserl's diagram; one moment
               across many presents                                    (3)

Shared machinery -- parsing, printing, the preset menu, the wiring -- is
phenkit_core.py. Each mode is a table of fields, a table of views (which
fields and tiles a view shows) and one pure JS function
<xx>Compute(view, inst, opts) that scripts/mathcheck.js calls directly
(section "phenkit"). A page ships RATIONAL_JS, PH_CORE_JS and its own mode's
block only.

VIEW IS NOT A CONTROL. cfg["view"] fixes which inputs and tiles the page shows;
an unknown view raises. The redraw-only controls are cuStep (cfg `step`),
caPair (cfg `pair`), lePeriod (cfg `period`) and trVertex (cfg `vertex`);
their options and range come from the cfg, never from a preset.

EXACT. Every tile is a rational over BigInt. The only floats are SVG pixel
positions (the triangle, the tilted room, the strip of dots, the cube drawings,
the time diagram) and the degree figure of size/angle, which is printed beside
its exact ratio and marked with ≈. No tile, status sentence or expectation is
read from a drawing.

IDS. Every tile id is unique within the kit and begins with its mode's prefix
(st gr cu sz pe vr ca sc so le de mo li tr ti). Grepped against
scripts/mathpath/labs/*.py on 2026-10-24: no other kit defines a JS function
named ph*, or one of the <xx>Compute functions below, and the element ids
stPreset, grPreset, ... meet other kits' ids only on other pages.
"""

from . import phenkit_core as pc

KIT = "phenkit"
LESSON = "the lesson's model"

# ---------------------------------------------------------------------------
# stimulus
# ---------------------------------------------------------------------------

STIMULUS_JS = r"""
  /* stimulus: the named model predicts the difference the stimuli measure. */
  function stCompute(view, inst, opts) {
    var u = inst.unit, pred = Rsub(inst.a, inst.b), gap = Rsub(inst.reported, pred);
    return {
      tiles: { stPredicted: phQty(pred, u), stReported: phQty(inst.reported, u), stGap: phQty(gap, u) },
      status: 'The stimuli measure ' + phQty(inst.a, u) + ' and ' + phQty(inst.b, u) + ', so on ' + opts.model
        + ', the predicted difference is ' + phQty(pred, u) + '. The reported difference is ' + phQty(inst.reported, u)
        + ', and the report minus the prediction is ' + phQty(gap, u)
        + '. The lab computes the prediction; it does not compute what is seen.',
      table: null
    };
  }
"""

STIMULUS_FIELDS = {
    "a": ({"kind": "nn", "what": "First stimulus, as measured"}, None),
    "b": ({"kind": "nn", "what": "Second stimulus, as measured"}, None),
    "unit": ({"kind": "word", "words": pc.UNITS, "what": "Unit (mm, cm, m or km)"}, "cm"),
    "reported": ({"kind": "num", "what": "Reported difference (first minus second, signed)"}, None),
}
STIMULUS_VIEWS = {
    "illusion": dict(fields=["a", "b", "unit", "reported"],
                     tiles=[("Predicted difference (first minus second)", "stPredicted"),
                            ("Reported difference", "stReported"), ("Report minus prediction", "stGap")]),
}

# ---------------------------------------------------------------------------
# grouping
# ---------------------------------------------------------------------------

GROUPING_JS = r"""
  /* grouping: Wertheimer's proximity rule as the lab states it -- sort the
     dots; a gap at least `ratio` times the smallest gap separates groups. */
  function grGroupsOf(points, ratio) {
    var p = points.slice().sort(Rcmp), gaps = [], i;
    for (i = 1; i < p.length; i += 1) gaps.push(Rsub(p[i], p[i - 1]));
    var min = gaps.reduce(function (m, g) { return Rcmp(g, m) < 0 ? g : m; }, gaps[0]);
    var cut = Rmul(min, ratio), groups = [[p[0]]];
    gaps.forEach(function (g, k) {
      if (Rcmp(g, cut) >= 0) groups.push([]);
      groups[groups.length - 1].push(p[k + 1]);
    });
    return { sorted: p, gaps: gaps, min: min, cut: cut, groups: groups };
  }
  var GR_COLOURS = ['var(--cyan)', 'var(--amber)', 'var(--green)', 'var(--purple)', 'var(--blue)', 'var(--red)'];
  function grStrip(r) {
    var lo = Rnum(r.sorted[0]), hi = Rnum(r.sorted[r.sorted.length - 1]), span = hi - lo || 1, inner = '';
    inner += phLine(20, 30, 620, 30, 'var(--line-strong)');
    r.groups.forEach(function (g, k) {
      g.forEach(function (x) {
        inner += '<circle cx="' + phPx(20 + 600 * (Rnum(x) - lo) / span) + '" cy="30" r="9" fill="' + GR_COLOURS[k % 6] + '"></circle>';
      });
    });
    return phSvg(640, 60, r.groups.length + ' groups of dots on a line', inner);
  }
  function grCompute(view, inst, opts) {
    var r = grGroupsOf(inst.points, inst.ratio);
    for (var i = 0; i < r.gaps.length; i += 1) {
      if (Rzero(r.gaps[i])) return { refuse: 'Two dots are at ' + phNum(r.sorted[i]) + '; every dot needs its own position' };
    }
    var groups = r.groups.map(function (g) { return '{' + g.map(phNum).join(', ') + '}'; }).join(' ');
    return {
      tiles: { grGaps: r.gaps.map(phNum).join(', '), grGroups: groups, grCount: String(r.groups.length) },
      status: 'Sorted, the dots leave gaps of ' + r.gaps.map(phNum).join(', ') + '. The smallest is ' + phNum(r.min)
        + ', so on ' + opts.model + ' a gap of at least ' + phNum(inst.ratio) + ' × ' + phNum(r.min) + ' = ' + phNum(r.cut)
        + ' separates groups: ' + r.groups.length + (r.groups.length === 1 ? ' group' : ' groups')
        + '. The groups are relations between dots; no single dot carries one.',
      table: { caption: 'Each gap against the threshold ' + phNum(r.cut), head: ['between', 'gap', 'separates'],
        rows: r.gaps.map(function (g, k) {
          var sep = Rcmp(g, r.cut) >= 0;
          return [phNum(r.sorted[k]) + ' and ' + phNum(r.sorted[k + 1]), phNum(g), { t: sep ? 'yes' : 'no', c: sep ? 'tone-amber' : '' }];
        }) },
      svg: grStrip(r)
    };
  }
"""

GROUPING_FIELDS = {
    "points": ({"kind": "list", "each": {"kind": "num"}, "sep": "ws", "lo": 2, "hi": 16,
                "what": "Positions of the dots on the line"}, None),
    "ratio": ({"kind": "pos", "what": "A gap at least this many times the smallest separates groups"}, 2),
}
GROUPING_VIEWS = {
    "proximity": dict(fields=["points", "ratio"], figure=True,
                      tiles=[("Gaps, in order", "grGaps"), ("Groups the rule predicts", "grGroups"),
                             ("Number of groups", "grCount")]),
}

# ---------------------------------------------------------------------------
# cues
# ---------------------------------------------------------------------------

CUES_JS = r"""
  /* cues/pattern: a word fits when it has the pattern's length and agrees at
     every letter that was seen (_ is a letter not seen). */
  function cuFits(word, pattern) {
    if (word.length !== pattern.length) return false;
    for (var i = 0; i < pattern.length; i += 1) if (pattern[i] !== '_' && pattern[i] !== word[i]) return false;
    return true;
  }
  function cuPatternFit(words, pattern, context) {
    return words.filter(function (w) { return cuFits(w.word, pattern) && (context === null || w.tag === context); });
  }
  /* cues/sequence: the candidates consistent with every one of the first k cues. */
  function cuKept(cands, cues, k) {
    return cands.filter(function (c) { return cues.slice(0, k).every(function (q) { return c.cues.indexOf(q) >= 0; }); });
  }
  function cuSequence(cands, cues, step) {
    var shown = Math.min(step, cues.length), kept = cuKept(cands, cues, shown), before = cuKept(cands, cues, shown - 1);
    return { shown: shown, clamped: step > cues.length, kept: kept,
             removed: before.filter(function (c) { return kept.indexOf(c) < 0; }) };
  }
  function cuNames(list) { return phNames(list.map(function (c) { return c.name; })); }
  function cuCompute(view, inst, opts) {
    if (view === 'pattern') {
      var tags = inst.words.filter(function (w) { return w.tag !== null; }).map(function (w) { return w.tag; });
      if (inst.context !== null && tags.indexOf(inst.context) < 0) {
        return { refuse: 'No remembered word carries the context "' + inst.context + '"; the tags are ' + phNames(tags) };
      }
      var all = cuPatternFit(inst.words, inst.pattern, null), fit = cuPatternFit(inst.words, inst.pattern, inst.context);
      var words = function (l) { return phNames(l.map(function (w) { return w.word; })); };
      return {
        tiles: { cuCount: String(fit.length), cuCandidates: words(fit), cuContext: inst.context === null ? PH_DASH : inst.context },
        status: 'Of ' + inst.words.length + ' remembered words, ' + all.length + ' fit the letters ' + inst.pattern
          + (inst.context === null ? '' : ', and ' + fit.length + ' of those ' + (fit.length === 1 ? 'carries' : 'carry') + ' the context ' + inst.context)
          + '. On ' + opts.model + ' memory supplies the candidates; what selects among them is the pattern'
          + (inst.context === null ? '' : ' and the context') + '.',
        table: null
      };
    }
    var known = [];
    inst.candidates.forEach(function (c) { c.cues.forEach(function (q) { if (known.indexOf(q) < 0) known.push(q); }); });
    for (var i = 0; i < inst.cues.length; i += 1) {
      if (known.indexOf(inst.cues[i]) < 0) {
        return { refuse: 'No candidate is consistent with the cue "' + inst.cues[i] + '"; the cues the candidates list are ' + phNames(known) };
      }
    }
    var s = cuSequence(inst.candidates, inst.cues, opts.step), text = opts.cue_text || {};
    var rows = inst.cues.map(function (q, k) {
      var after = cuSequence(inst.candidates, inst.cues, k + 1);
      return [String(k + 1), q + (text[q] ? ': ' + text[q] : ''), String(after.kept.length), cuNames(after.kept), cuNames(after.removed)];
    });
    return {
      tiles: { cuCount: String(s.kept.length), cuCandidates: cuNames(s.kept), cuRemoved: cuNames(s.removed) },
      status: (s.clamped ? 'Step ' + opts.step + ' is past this instance\'s ' + inst.cues.length + ' cue'
        + (inst.cues.length === 1 ? '' : 's') + ', so the lab shows step ' + s.shown + '. ' : '')
        + 'After ' + s.shown + ' of ' + inst.cues.length + ' cues (' + inst.cues.slice(0, s.shown).join(', ') + '), '
        + opts.model + ' keeps ' + s.kept.length + ' of ' + inst.candidates.length + ' candidates: ' + cuNames(s.kept) + '.',
      table: { caption: 'Candidates kept after each cue', head: ['step', 'cue', 'kept', 'candidates', 'removed by this cue'], rows: rows }
    };
  }
"""

_CUE = {"kind": "tokens"}
CUES_FIELDS = {
    "words": ({"kind": "list", "each": {"kind": "wordtag"}, "sep": "ws", "lo": 1, "hi": 40, "unique": True,
               "what": "Remembered words (a word may carry a tag: gate:door)"}, None),
    "pattern": ({"kind": "pattern", "what": "The letters seen, _ for each letter not seen"}, None),
    "context": ({"kind": "tag", "what": "Context (a tag, or empty)"}, ""),
    "candidates": ({"kind": "rec", "sub": [["name", {"kind": "name"}], ["cues", _CUE]], "lo": 1, "hi": 8,
                    "unique": True, "what": "Candidates: name, the cues it is consistent with; separated by ;"}, None),
    "cues": ({"kind": "list", "each": {"kind": "name"}, "sep": "ws", "lo": 1, "hi": 6,
              "what": "Cues, in the order they arrive"}, None),
}
CUES_VIEWS = {
    "pattern": dict(fields=["words", "pattern", "context"],
                    tiles=[("Words that fit", "cuCount"), ("Candidates, in list order", "cuCandidates"),
                           ("Context", "cuContext")]),
    "sequence": dict(fields=["candidates", "cues"], step=True,
                     tiles=[("Candidates kept", "cuCount"), ("Kept, in list order", "cuCandidates"),
                            ("Removed by the last cue", "cuRemoved")]),
}

# ---------------------------------------------------------------------------
# size
# ---------------------------------------------------------------------------

SIZE_JS = r"""
  /* size/angle: the small-angle form, size / distance in radians. The degree
     figure converts that ratio with pi and is marked approximate. */
  function szDegreesOf(r) { return '≈ ' + (Rnum(r) * 180 / Math.PI).toFixed(2) + '°'; }
  /* size/constancy: the retinal-image account predicts the size that subtends
     the same angle at the standard distance; an inference from an assumed
     distance concludes size x assumed / distance; Brunswik's ratio places the
     reported size between the two. */
  function szConstancy(size, distance, standard, assumed, reported) {
    var retinal = Rdiv(Rmul(size, standard), distance), inferred = Rdiv(Rmul(size, assumed), distance);
    return { retinal: retinal, inferred: inferred, brunswik: Rdiv(Rsub(reported, retinal), Rsub(size, retinal)) };
  }
  function szCompute(view, inst, opts) {
    var u = inst.unit;
    if (view === 'angle') {
      var r = Rdiv(inst.size, inst.distance);
      return {
        tiles: { szRatio: phApprox(r, 4, 'rad'), szDegrees: szDegreesOf(r) },
        status: 'On ' + opts.model + ', ' + phQty(inst.size, u) + ' at ' + phQty(inst.distance, u) + ' subtends '
          + phNum(inst.size) + ' / ' + phNum(inst.distance) + ' = ' + phApprox(r, 4, 'rad')
          + ', the small-angle form, which is ' + szDegreesOf(r) + '. The figure says how large the angle is, not how large anything looks.',
        table: null
      };
    }
    if (Requ(inst.distance, inst.standard_distance)) {
      return { refuse: 'The distance equals the standard distance, ' + phQty(inst.distance, u)
        + ', so both accounts predict the size itself and there is nothing to correct' };
    }
    var assumed = inst.assumed === null ? inst.distance : inst.assumed;
    var c = szConstancy(inst.size, inst.distance, inst.standard_distance, assumed, inst.reported);
    return {
      tiles: { szRetinal: phQty(c.retinal, u), szInferred: phQty(c.inferred, u), szBrunswik: phPct(c.brunswik) },
      status: 'A ' + phQty(inst.size, u) + ' object at ' + phQty(inst.distance, u) + ' subtends the angle that '
        + phQty(c.retinal, u) + ' subtends at ' + phQty(inst.standard_distance, u) + ': the retinal-image account\'s prediction. '
        + 'An inference that assumes a distance of ' + phQty(assumed, u) + ' would conclude ' + phQty(c.inferred, u)
        + '. The reported size, ' + phQty(inst.reported, u) + ', gives a Brunswik ratio of ' + phPct(c.brunswik)
        + ' (1 is full constancy, 0 none).',
      table: null
    };
  }
"""

_UNIT = ({"kind": "word", "words": pc.UNITS, "what": "Unit (mm, cm, m or km)"}, "cm")
SIZE_FIELDS = {
    "size": ({"kind": "pos", "what": "Size of the object"}, None),
    "distance": ({"kind": "pos", "what": "Its distance"}, None),
    "unit": _UNIT,
    "standard_distance": ({"kind": "pos", "what": "The standard distance it is compared at"}, None),
    "assumed": ({"kind": "optpos", "what": "The distance an inference assumes (empty: the true distance)"}, ""),
    "reported": ({"kind": "nn", "what": "The size reported at the standard distance"}, None),
}
SIZE_VIEWS = {
    "angle": dict(fields=["size", "distance", "unit"],
                  tiles=[("Size / distance (small-angle radians)", "szRatio"), ("In degrees", "szDegrees")]),
    "constancy": dict(fields=["size", "distance", "standard_distance", "assumed", "reported", "unit"],
                      tiles=[("Retinal-image prediction (same angle at the standard distance)", "szRetinal"),
                             ("The size an inference from the assumed distance would conclude", "szInferred"),
                             ("Brunswik ratio", "szBrunswik")]),
}

# ---------------------------------------------------------------------------
# perspective
# ---------------------------------------------------------------------------

PERSPECTIVE_JS = r"""
  /* perspective/faces: a face is visible from a view when its outward normal
     has a positive dot product with the view; its foreshortening is that dot
     product over the view's length. The face normals are the six axis
     directions, so the dot product is one component of the view. */
  function peSees(dir) {
    var out = [];
    PH_FACES.forEach(function (f) {
      var n = PH_DIRS[f], dot = BigInt(n[0]) * dir.v[0] + BigInt(n[1]) * dir.v[1] + BigInt(n[2]) * dir.v[2];
      if (dot > 0n) out.push({ face: f, fs: R(dot, dir.len) });
    });
    return out;
  }
  function peUnionOf(sets) {
    return PH_FACES.filter(function (f) { return sets.some(function (s) { return s.indexOf(f) >= 0; }); });
  }
  /* The smallest set of views whose faces together are the union; among
     equal sizes, the first in list order (subsets by size, then
     lexicographically by position). */
  function peCoverOf(sets) {
    var union = peUnionOf(sets), n = sets.length, best = null;
    for (var size = 1; size <= n && !best; size += 1) {
      var idx = [];
      for (var i = 0; i < size; i += 1) idx.push(i);
      while (true) {
        if (peUnionOf(idx.map(function (k) { return sets[k]; })).length === union.length) { best = idx.slice(); break; }
        var j = size - 1;
        while (j >= 0 && idx[j] === n - size + j) j -= 1;
        if (j < 0) break;
        idx[j] += 1;
        for (var t = j + 1; t < size; t += 1) idx[t] = idx[t - 1] + 1;
      }
    }
    return best || [];
  }
  function peConsistentOf(views) {
    var any = false, bad = [];
    views.forEach(function (v) {
      if (!v.reports.length) return;
      any = true;
      var seen = v.sees.map(function (s) { return s.face; });
      var wrong = v.reports.filter(function (f) { return seen.indexOf(f) < 0; });
      if (wrong.length) bad.push(v.name + ' (' + wrong.join(', ') + ')');
    });
    if (!any) return PH_DASH;
    return bad.length ? 'no: ' + bad.join(', ') : 'yes';
  }
  function peViews(list, allowed) {
    var names = {};
    for (var i = 0; i < list.length; i += 1) {
      var r = list[i], name = r.name ? r.name : r.direction.text;
      if (names[name]) return { refuse: 'Two views are named ' + name + '; give each its own name' };
      names[name] = true;
      if (allowed && allowed.indexOf(r.direction.v.join(' ')) < 0) {
        return { refuse: 'This lesson\'s views are ' + allowed.join('; ') + ', and ' + r.direction.text + ' is not one of them' };
      }
      var reports = r.reports || [];
      for (var k = 0; k < reports.length; k += 1) {
        if (PH_FACES.indexOf(reports[k]) < 0) return { refuse: 'View ' + name + ' reports "' + reports[k] + '", which is not a face: the faces are ' + PH_FACES.join(', ') };
      }
      list[i] = { name: name, dir: r.direction, reports: reports, sees: peSees(r.direction) };
    }
    return { views: list };
  }
  function peSeenText(v) { return v.sees.map(function (s) { return s.face + ' ' + phNum(s.fs); }).join(', '); }

  /* perspective/necker: the box [0,w] x [0,h] x [0,d] (x right, y up, z
     towards the viewer), drawn by parallel projection along d = (k, k, 1):
     (x, y, z) -> (x - kz, y - kz). Reading B is its mirror image in the plane
     through the centre perpendicular to d, exact because d is rational. A wire
     figure draws every edge; a solid one only the edges of faces whose outward
     normal has a positive dot product with d. */
  var PE_FACES = [['front', 2, 1, [0, 0, 1]], ['back', 2, 0, [0, 0, -1]], ['right', 0, 1, [1, 0, 0]],
                  ['left', 0, 0, [-1, 0, 0]], ['above', 1, 1, [0, 1, 0]], ['below', 1, 0, [0, -1, 0]]];
  function peBox(o) {
    var size = [o.w, o.h, o.d], verts = [], edges = [];
    for (var m = 0; m < 8; m += 1) verts.push([m & 1 ? size[0] : R0, m & 2 ? size[1] : R0, m & 4 ? size[2] : R0]);
    for (var a = 0; a < 8; a += 1) for (var b = a + 1; b < 8; b += 1) {
      var diff = a ^ b;
      if (diff === 1 || diff === 2 || diff === 4) edges.push([a, b]);
    }
    return { size: size, verts: verts, edges: edges };
  }
  function peDot3(p, q) { return Radd(Radd(Rmul(p[0], q[0]), Rmul(p[1], q[1])), Rmul(p[2], q[2])); }
  function peReflect(p, c, d) {
    var t = Rdiv(peDot3([Rsub(p[0], c[0]), Rsub(p[1], c[1]), Rsub(p[2], c[2])], d), peDot3(d, d));
    return p.map(function (x, i) { return Rsub(x, Rmul(Rmul(R(2n), t), d[i])); });
  }
  function peProject(p, k) { return [Rsub(p[0], Rmul(k, p[2])), Rsub(p[1], Rmul(k, p[2]))]; }
  /* The faces a reading shows: the edges of those faces (or every edge, for a
     wire), projected; a degenerate edge is not drawn, a repeated one once. */
  function peDrawing(box, points, normals, d, k, wire) {
    var keep = box.edges.filter(function (e) {
      if (wire) return true;
      return PE_FACES.some(function (f, fi) {
        var on = function (v) { return ((v >> f[1]) & 1) === f[2]; };
        return on(e[0]) && on(e[1]) && Rsign(peDot3(normals[fi], d)) > 0;
      });
    });
    var segs = {};
    keep.forEach(function (e) {
      var p = peProject(points[e[0]], k), q = peProject(points[e[1]], k);
      if (Requ(p[0], q[0]) && Requ(p[1], q[1])) return;
      var a = Rtext(p[0]) + ',' + Rtext(p[1]), b = Rtext(q[0]) + ',' + Rtext(q[1]);
      segs[a < b ? a + '|' + b : b + '|' + a] = [p, q];
    });
    return segs;
  }
  function peNecker(o, k) {
    var box = peBox(o), d = [k, k, R1], c = box.size.map(function (x) { return Rdiv(x, R(2n)); });
    var normalsA = PE_FACES.map(function (f) { return f[3].map(function (x) { return R(BigInt(x)); }); });
    var pointsB = box.verts.map(function (p) { return peReflect(p, c, d); });
    /* A normal reflects as a direction: n - 2 (n.d / d.d) d. */
    var normalsB = normalsA.map(function (n) { return peReflect(n, [R0, R0, R0], d); });
    var A = peDrawing(box, box.verts, normalsA, d, k, o.wire), B = peDrawing(box, pointsB, normalsB, d, k, o.wire);
    var ka = Object.keys(A).sort(), kb = Object.keys(B).sort();
    return { A: A, B: B, edges: ka.length, same: ka.join(';') === kb.join(';') };
  }
  function peSketch(segs, x0, label) {
    var all = [], inner = '';
    Object.keys(segs).forEach(function (key) { all.push(segs[key][0], segs[key][1]); });
    if (!all.length) return phText(x0 + 140, 120, label + ': nothing drawn', 'middle');
    var xs = all.map(function (p) { return Rnum(p[0]); }), ys = all.map(function (p) { return Rnum(p[1]); });
    var lo = Math.min.apply(null, xs), hi = Math.max.apply(null, xs), bo = Math.min.apply(null, ys), to = Math.max.apply(null, ys);
    var sc = 200 / Math.max(hi - lo, to - bo, 1e-9);
    var px = function (p) { return [x0 + 40 + (Rnum(p[0]) - lo) * sc, 220 - (Rnum(p[1]) - bo) * sc]; };
    Object.keys(segs).forEach(function (key) {
      var a = px(segs[key][0]), b = px(segs[key][1]);
      inner += phLine(a[0], a[1], b[0], b[1], 'var(--text)');
    });
    return inner + phText(x0 + 140, 250, label, 'middle');
  }
  function peCompute(view, inst, opts) {
    if (view === 'necker') {
      if (Rcmp(Rabs(inst.offset), R(2n)) > 0) return { refuse: 'The offset is ' + phNum(inst.offset) + '; this lab draws offsets from −2 to 2' };
      var r = peNecker(inst.object, inst.offset);
      return {
        tiles: { peEdges: String(r.edges), peReadings: r.same ? '2' : '1', peSame: r.same ? 'identical drawings' : 'different drawings' },
        status: 'Projected along (' + phNum(inst.offset) + ', ' + phNum(inst.offset) + ', 1), reading A draws ' + r.edges
          + ' edges. Reading B, the mirror image across the plane perpendicular to the line of sight, projects point for point onto the same places, and '
          + (r.same ? 'draws the identical edges: the drawing does not decide which face is in front.'
            : 'draws different edges, so this drawing fits one reading only.'),
        table: null,
        svg: phSvg(640, 264, 'reading A and reading B', peSketch(r.A, 20, 'reading A') + peSketch(r.B, 340, 'reading B'))
      };
    }
    var got = peViews(inst.views, view === 'own' ? opts.allowed : null);
    if (got.refuse) return got;
    var views = got.views, sets = views.map(function (v) { return v.sees.map(function (s) { return s.face; }); });
    var union = peUnionOf(sets), unseen = PH_FACES.filter(function (f) { return union.indexOf(f) < 0; });
    var cover = peCoverOf(sets), most = Math.max.apply(null, sets.map(function (s) { return s.length; }));
    var tiles = {
      peVisible: views.map(function (v) { return v.name + ': ' + peSeenText(v); }).join('; '),
      peUnion: union.length + ' of 6', peMax: String(most), peUnseen: phNames(unseen),
      peCover: cover.map(function (k) { return views[k].name; }).join(', ') + ' (' + cover.length + (cover.length === 1 ? ' view)' : ' views)'),
      peConsistent: peConsistentOf(views)
    };
    return {
      tiles: tiles,
      status: (views.length === 1 ? 'One view sees ' : views.length + ' views see ') + union.length + ' of the 6 faces' + (views.length === 1 ? ' (' : ' between them (')
        + phNames(union) + '); ' + (unseen.length ? phNames(unseen) + (unseen.length === 1 ? ' is' : ' are') + ' seen from none of them. '
          : 'none is unseen. ') + 'No view sees more than ' + most + ', and none sees a face at its true size unless it looks straight at it.',
      table: { caption: 'What each view sees (foreshortening: projected over true area)', head: ['view', 'direction', 'faces seen', 'reported'],
        rows: views.map(function (v) { return [v.name, v.dir.text + ' (length ' + v.dir.len + ')', peSeenText(v), v.reports.length ? v.reports.join(', ') : PH_DASH]; }) }
    };
  }
"""

_VIEWS = {"kind": "rec", "sub": [["direction", {"kind": "dir"}], ["name", {"kind": "label"}],
                                 ["reports", {"kind": "tokens"}]], "opt": 2, "lo": 1, "hi": 6,
          "what": "Views: direction, a name, the faces its viewer reports; separated by ;"}
PERSPECTIVE_FIELDS = {
    "object": ({"kind": "solid", "what": "The object: cube, or box width depth height"}, "cube"),
    "views": (_VIEWS, None),
    "offset": ({"kind": "num", "what": "Offset k: the drawing projects along (k, k, 1)"}, "1/2"),
}
PERSPECTIVE_VIEWS = {
    "faces": dict(fields=["object", "views"],
                  tiles=[("Faces each view sees, with foreshortening", "peVisible"), ("Faces seen by some view", "peUnion"),
                         ("Most faces one view sees", "peMax"), ("Smallest set of views that sees them all", "peCover"),
                         ("Reports consistent with the directions", "peConsistent")]),
    "own": dict(fields=["object", "views"], family=3, model=LESSON,
                tiles=[("Faces seen by some view", "peUnion"), ("Faces no view sees", "peUnseen")]),
    "necker": dict(fields=[("object", {"kind": "necker", "what": "The figure: wire cube, wire box W D H, solid cube "
                                                     "or solid box W D H"}, None), "offset"], figure=True,
                   tiles=[("Edges in reading A's drawing", "peEdges"), ("Readings the drawing fits", "peReadings"),
                          ("The two readings give", "peSame")]),
}

# ---------------------------------------------------------------------------
# variation
# ---------------------------------------------------------------------------

VARIATION_JS = r"""
  /* variation: the core is what every variant of the kind has; the kit only
     counts the lesson's coding, it decides no cell. */
  function vrCoreOf(variants) {
    var kind = variants.filter(function (v) { return v.kind; }), order = [];
    kind.forEach(function (v) { v.props.forEach(function (p) { if (order.indexOf(p) < 0) order.push(p); }); });
    var core = order.filter(function (p) { return kind.every(function (v) { return v.props.indexOf(p) >= 0; }); });
    return { kind: kind, core: core, vary: order.filter(function (p) { return core.indexOf(p) < 0; }) };
  }
  function vrBreakOf(variants, core) {
    var out = variants.filter(function (v) { return !v.kind; }).map(function (v) {
      var lacks = core.filter(function (p) { return v.props.indexOf(p) < 0; });
      return v.name + ' lacks ' + (lacks.length ? lacks.join(', ') : 'none of the core');
    });
    return out.length ? out.join('; ') : 'no variant is marked no';
  }
  function vrCompute(view, inst, opts) {
    inst = { variants: inst.variants.map(function (v) { return { name: v.name, kind: v.kind, props: v.properties || [] }; }) };
    var r = vrCoreOf(inst.variants);
    if (!r.kind.length) return { refuse: 'No variant is marked yes, so there is no kind whose core could be found' };
    return {
      tiles: { vrCore: phNames(r.core), vrVary: phNames(r.vary), vrBreak: vrBreakOf(inst.variants, r.core) },
      status: 'Across ' + r.kind.length + ' variant' + (r.kind.length === 1 ? '' : 's') + ' marked yes, '
        + (r.core.length ? phNames(r.core) + (r.core.length === 1 ? ' stays' : ' stay') : 'no property stays')
        + (r.vary.length ? ' and ' + phNames(r.vary) + ' ' + (r.vary.length === 1 ? 'varies' : 'vary') : '')
        + '. The properties and the yes and no are ' + opts.model + '; the lab only counts.',
      table: { caption: 'The variants as coded', head: ['variant', 'of the kind', 'properties'],
        rows: inst.variants.map(function (v) { return [v.name, v.kind ? 'yes' : 'no', v.props.length ? v.props.join(' ') : PH_DASH]; }) }
    };
  }
"""

VARIATION_FIELDS = {
    "variants": ({"kind": "rec", "sub": [["name", {"kind": "name"}], ["kind", {"kind": "yesno"}],
                                         ["properties", {"kind": "tokens"}]], "opt": 1, "lo": 1, "hi": 10,
                  "unique": True,
                  "what": "Variants: name, yes or no (still of the kind), its properties; separated by ;"}, None),
}
VARIATION_VIEWS = {
    "core": dict(fields=["variants"],
                 tiles=[("Core: in every variant of the kind", "vrCore"),
                        ("Varies among the variants of the kind", "vrVary"),
                        ("Variants not of the kind, and the core they lack", "vrBreak")]),
}

# ---------------------------------------------------------------------------
# cases
# ---------------------------------------------------------------------------

CASES_JS = r"""
  /* cases: observations x the opponents' accounts (a cfg key, fixed for the
     lesson). Each cell is the lesson's coding -- y consistent, n inconsistent,
     - silent -- and the kit only counts it. */
  function caRecordOf(obs, a) {
    var r = { y: 0, n: 0, s: 0 };
    obs.forEach(function (o) { var c = o.cells[a]; if (c === 'y') r.y += 1; else if (c === 'n') r.n += 1; else r.s += 1; });
    return r;
  }
  function caSplitOf(obs, i, j) {
    return obs.filter(function (o) { var p = o.cells[i], q = o.cells[j]; return (p === 'y' && q === 'n') || (p === 'n' && q === 'y'); });
  }
  function caCompute(view, inst, opts) {
    var acc = opts.accounts, pair = opts.pair.split('-').map(Number);
    var obs = inst.observations.map(function (o) {
      return { name: o.observation, cells: acc.map(function (_a, k) { return o['a' + k]; }) };
    });
    var recs = acc.map(function (_a, k) { return caRecordOf(obs, k); });
    var survivors = acc.filter(function (_a, k) { return recs[k].n === 0; });
    var split = caSplitOf(obs, pair[0], pair[1]);
    var tone = { y: 'tone-green', n: 'tone-red', '-': 'tone-muted' };
    return {
      tiles: {
        caRecord: acc.map(function (a, k) {
          return a + ': absorbs ' + recs[k].y + ' of ' + obs.length + ', fails ' + recs[k].n + ', silent ' + recs[k].s;
        }).join('; '),
        caSurvivors: phNames(survivors),
        caSplit: phNames(split.map(function (o) { return o.name; }))
      },
      status: obs.length + ' observation' + (obs.length === 1 ? '' : 's') + ', coded against ' + acc.join(' and ')
        + ' (' + opts.model + '). ' + (survivors.length ? 'Failing none: ' + phNames(survivors) + '.' : 'Every account fails at least one.')
        + ' The compared pair, ' + acc[pair[0]] + ' and ' + acc[pair[1]] + ', part on ' + split.length + '. The coding is an interpretation; the count is exact, and the record is not a ranking.',
      table: { caption: 'The lesson\'s coding: y consistent, n inconsistent, - silent', head: ['observation'].concat(acc),
        rows: obs.map(function (o) { return [o.name].concat(o.cells.map(function (c) { return { t: c, c: tone[c] }; })); }) }
    };
  }
"""

CASES_VIEWS = {
    "table": dict(fields=["observations"],
                  tiles=[("Each account's record", "caRecord"), ("Accounts that fail no observation", "caSurvivors"),
                         ("Observations on which the compared pair part", "caSplit")]),
}

# ---------------------------------------------------------------------------
# schema
# ---------------------------------------------------------------------------

SCHEMA_JS = r"""
  /* schema/coordinates: a body at B facing theta (counter-clockwise from
     east, a Pythagorean angle, so cos and sin are exact). An object at P is
     ahead (P - B).(cos, sin) and left (P - B).(-sin, cos). */
  function scBodyOf(body, x, y) {
    var dx = Rsub(x, body.x), dy = Rsub(y, body.y), c = body.facing.cos, s = body.facing.sin;
    return { ahead: Radd(Rmul(dx, c), Rmul(dy, s)), left: Radd(Rmul(Rneg(dx), s), Rmul(dy, c)) };
  }
  function scBodyText(b) {
    return (Rsign(b.ahead) < 0 ? 'behind ' + phNum(Rneg(b.ahead)) : 'ahead ' + phNum(b.ahead)) + ', '
      + (Rsign(b.left) < 0 ? 'right ' + phNum(Rneg(b.left)) : 'left ' + phNum(b.left));
  }
  function scWithin(objects, ok) { return phNames(objects.filter(ok).map(function (o) { return o.name; })); }
  function scCompute(view, inst, opts) {
    var u = opts.unit, q = function (r) { return phQty(r, u); };
    if (view === 'coordinates') {
      var body = inst.body[0];
      var rows = inst.objects.map(function (o) { return { o: o, b: scBodyOf(body, o.x, o.y) }; });
      var framed = rows.filter(function (r) { return r.o.given; });
      return {
        tiles: {
          scRoom: rows.map(function (r) { return r.o.name + ' (' + phNum(r.o.x) + ', ' + phNum(r.o.y) + ')'; }).join('; '),
          scBody: rows.map(function (r) { return r.o.name + ' ' + scBodyText(r.b); }).join('; '),
          scFrame: framed.length ? framed.map(function (r) {
            return r.o.name + ': ' + (r.o.given === 'body' ? 'given in the body\'s situation: no conversion'
              : 'given as a position in objective space: converted to ' + scBodyText(r.b));
          }).join('; ') : 'no object has a given frame'
        },
        status: 'On ' + opts.model + ', the body stands at (' + phNum(body.x) + ', ' + phNum(body.y) + ') facing '
          + phAngleText(body.facing) + ' (counter-clockwise from east). Room coordinates stay put as the body turns or walks; '
          + 'coordinates relative to the body change with it.',
        table: { caption: 'Each object in the room and relative to the body', head: ['object', 'room', 'relative to the body', 'given'],
          rows: rows.map(function (r) { return [r.o.name, '(' + phNum(r.o.x) + ', ' + phNum(r.o.y) + ')', scBodyText(r.b), r.o.given || PH_DASH]; }) }
      };
    }
    if (view === 'habitual') {
      var inH = function (o) { return Rcmp(o.distance, inst.habitual_reach[o.side]) <= 0; };
      var inP = function (o) { return Rcmp(o.distance, inst.present_reach[o.side]) <= 0; };
      return {
        tiles: { scHabitual: scWithin(inst.objects, inH), scPresent: scWithin(inst.objects, inP),
                 scAppeal: scWithin(inst.objects, function (o) { return inH(o) && !inP(o); }) },
        status: 'On ' + opts.model + ', the habitual body reaches ' + q(inst.habitual_reach.left) + ' on the left and '
          + q(inst.habitual_reach.right) + ' on the right; the present body ' + q(inst.present_reach.left) + ' and '
          + q(inst.present_reach.right) + '. An object within the first and not the second still appeals to a hand that is not there.',
        table: { caption: 'Each object against both reaches', head: ['object', 'side', 'distance', 'habitual', 'present'],
          rows: inst.objects.map(function (o) { return [o.name, o.side, q(o.distance), inH(o) ? 'within' : 'beyond', inP(o) ? 'within' : 'beyond']; }) }
      };
    }
    if (view === 'tool') {
      var reach = Radd(inst.reach, inst.tool), need = Radd(inst.height, inst.clearance);
      var clear = function (w) { var d = Rsub(w, need); return Rsign(d) >= 0 ? 'clears by ' + q(d) : 'does not clear by ' + q(Rneg(d)); };
      return {
        tiles: { scReach: q(reach), scWithin: scWithin(inst.objects, function (o) { return Rcmp(o.distance, reach) <= 0; }),
                 scClears: inst.openings.length === 1 ? clear(inst.openings[0])
                   : (inst.openings.length ? inst.openings.map(function (w) { return q(w) + ': ' + clear(w); }).join('; ') : 'no opening') },
        status: 'On ' + opts.model + ', a reach of ' + q(inst.reach) + ' with a ' + q(inst.tool) + ' tool reaches ' + q(reach)
          + '; a body ' + q(inst.height) + ' with ' + q(inst.clearance) + ' added needs ' + q(need)
          + ' to pass. The lab makes the comparison the habit does not make.',
        table: null
      };
    }
    /* obstacle */
    var taller = function (lim) { return phNames(inst.rocks.filter(function (r) { return Rcmp(r, lim) > 0; }).map(q)); };
    return {
      tiles: { scProject: inst.project === 'climb' ? taller(inst.capacity) : 'none', scLevel: taller(inst.general_level) },
      status: 'Rocks of ' + inst.rocks.map(q).join(', ') + '. Relative to the project (' + inst.project + ')'
        + (inst.project === 'climb' ? ', a rock taller than the capacity of ' + q(inst.capacity) + ' is an obstacle'
          : ', no rock is an obstacle, because nothing is to be climbed')
        + '; relative to the body\'s general level of ' + q(inst.general_level) + ', a taller rock stands out whatever the project. '
        + 'Both reckonings are ' + opts.model + '.',
      table: null
    };
  }
"""

_NAME = {"kind": "name"}
SCHEMA_FIELDS = {
    "body": ({"kind": "rec", "sub": [["x", {"kind": "num"}], ["y", {"kind": "num"}], ["facing", {"kind": "angle"}]],
              "lo": 1, "hi": 1, "what": "The body: x, y, facing (east, north, 3-4-5, ...)"}, None),
    "objects_room": ({"kind": "rec", "sub": [["name", _NAME], ["x", {"kind": "num"}], ["y", {"kind": "num"}],
                                             ["given", {"kind": "word", "words": ["body", "objective"]}]],
                      "opt": 1, "lo": 1, "hi": 6, "unique": True,
                      "what": "Objects: name, x, y, and optionally body or objective; separated by ;"}, None),
    "habitual_reach": ({"kind": "reach", "what": "Habitual reach (70, or left 70, right 70)"}, None),
    "present_reach": ({"kind": "reach", "what": "Present reach (70, or left 70, right 0)"}, None),
    "objects_side": ({"kind": "rec", "sub": [["name", _NAME], ["side", {"kind": "word", "words": ["left", "right"]}],
                                             ["distance", {"kind": "nn"}]], "lo": 1, "hi": 8, "unique": True,
                      "what": "Objects: name, left or right, distance; separated by ;"}, None),
    "reach": ({"kind": "nn", "what": "Reach of the arm"}, None),
    "tool": ({"kind": "nn", "what": "Length of the tool (0 for none)"}, 0),
    "height": ({"kind": "nn", "what": "The body's height or width at the opening"}, 0),
    "clearance": ({"kind": "nn", "what": "Added to it (a hat's feather; 0 for none)"}, 0),
    "objects_far": ({"kind": "rec", "sub": [["name", _NAME], ["distance", {"kind": "nn"}]], "lo": 0, "hi": 8,
                     "unique": True, "what": "Objects: name, distance; separated by ; (may be empty)"}, ""),
    "openings": ({"kind": "list", "each": {"kind": "pos"}, "sep": "ws", "lo": 0, "hi": 4,
                  "what": "Openings to pass (may be empty)"}, ""),
    "rocks": ({"kind": "list", "each": {"kind": "pos"}, "sep": "ws", "lo": 1, "hi": 8, "what": "Heights of the rocks"},
              None),
    "project": ({"kind": "word", "words": ["climb", "pass", "none"], "what": "The project (climb, pass or none)"}, None),
    "capacity": ({"kind": "nn", "what": "Height the climber can manage"}, None),
    "general_level": ({"kind": "nn", "what": "The body's general level"}, None),
}
SCHEMA_VIEWS = {
    "coordinates": dict(fields=["body", ("objects", "objects_room")],
                        tiles=[("Room coordinates", "scRoom"), ("Relative to the body", "scBody"),
                               ("The frame each target is given in", "scFrame")]),
    "habitual": dict(fields=["habitual_reach", "present_reach", ("objects", "objects_side")], unit=True,
                     tiles=[("Within the habitual reach", "scHabitual"), ("Within the present reach", "scPresent"),
                            ("Appeal only to the habitual body", "scAppeal")]),
    "tool": dict(fields=["reach", "tool", "height", "clearance", ("objects", "objects_far"), "openings"], unit=True,
                 tiles=[("Reach with the tool", "scReach"), ("Objects within it", "scWithin"),
                        ("At the opening", "scClears")]),
    "obstacle": dict(fields=["rocks", "project", "capacity", "general_level"], unit=True,
                     tiles=[("Obstacles relative to the project", "scProject"),
                            ("Taller than the body's general level", "scLevel")]),
}

# ---------------------------------------------------------------------------
# sorting
# ---------------------------------------------------------------------------

SORTING_JS = r"""
  /* sorting: the categorical sort groups by hue name; the chain picks, at
     each step, the unsorted sample nearest the last one picked, by
     |difference in lightness| + 1 if the hue differs, ties in list order. */
  function soDistance(p, q) {
    var d = p.lightness.n - q.lightness.n;
    return (d < 0n ? -d : d) + (p.hue.toLowerCase() === q.hue.toLowerCase() ? 0n : 1n);
  }
  function soChainOf(samples, start) {
    var left = samples.slice(), cur = start, chain = [{ s: start, d: null }];
    left.splice(left.indexOf(start), 1);
    while (left.length) {
      var best = 0;
      for (var i = 1; i < left.length; i += 1) if (soDistance(cur, left[i]) < soDistance(cur, left[best])) best = i;
      chain.push({ s: left[best], d: soDistance(cur, left[best]) });
      cur = left[best];
      left.splice(best, 1);
    }
    return chain;
  }
  function soCategories(samples) {
    var hues = [];
    samples.forEach(function (s) { if (hues.indexOf(s.hue.toLowerCase()) < 0) hues.push(s.hue.toLowerCase()); });
    return hues.map(function (h) { return { hue: h, names: samples.filter(function (s) { return s.hue.toLowerCase() === h; }).map(function (s) { return s.name; }) }; });
  }
  function soCompute(view, inst, opts) {
    var start = null;
    inst.samples.forEach(function (s) { if (s.name.toLowerCase() === inst.start.toLowerCase()) start = s; });
    if (!start) return { refuse: 'The start, "' + inst.start + '", is not one of the samples: ' + phNames(inst.samples.map(function (s) { return s.name; })) };
    var chain = soChainOf(inst.samples, start), part = null;
    chain.forEach(function (c) { if (!part && c.s.hue.toLowerCase() !== start.hue.toLowerCase()) part = c.s.name; });
    return {
      tiles: { soCategorical: soCategories(inst.samples).map(function (c) { return c.hue + ': ' + c.names.join(', '); }).join('; '),
               soChain: chain.map(function (c) { return c.s.name; }).join(' → '), soPart: part || 'none' },
      status: 'The rule of ' + opts.model + ': from ' + start.name + ', take at each step the unsorted sample nearest the last one '
        + 'taken, counting the difference in lightness plus 1 when the hue differs, ties in list order. '
        + (part ? 'The chain leaves ' + start.hue + ' at ' + part + '.' : 'The chain never leaves ' + start.hue + '.'),
      table: { caption: 'The chain, step by step', head: ['step', 'sample', 'hue', 'lightness', 'distance from the last'],
        rows: chain.map(function (c, k) { return [String(k + 1), c.s.name, c.s.hue, phNum(c.s.lightness), c.d === null ? PH_DASH : String(c.d)]; }) }
    };
  }
"""

SORTING_FIELDS = {
    "samples": ({"kind": "rec", "sub": [["name", _NAME], ["hue", _NAME], ["lightness", {"kind": "l10"}]],
                 "lo": 2, "hi": 12, "unique": True,
                 "what": "Samples: name, hue, lightness 0 to 10; separated by ;"}, None),
    "start": ({"kind": "name", "what": "The sample the chain starts from"}, None),
}
SORTING_VIEWS = {
    "sort": dict(fields=["samples", "start"],
                 tiles=[("Categorical sort, by hue name", "soCategorical"), ("Chain of resemblances", "soChain"),
                        ("Where the chain leaves the start's hue", "soPart")]),
}

# ---------------------------------------------------------------------------
# level
# ---------------------------------------------------------------------------

LEVEL_JS = r"""
  /* level: the lesson's model. The image is tilted; the spatial level starts
     somewhere; tilt is image minus level, normalised to (-180, 180]. No
     trigonometry: a tilt of the field is subtracted, not projected. */
  function leNorm(x) {
    while (Rcmp(x, R(180n)) > 0) x = Rsub(x, R(360n));
    while (Rcmp(x, R(-180n)) <= 0) x = Radd(x, R(360n));
    return x;
  }
  function leSeriesOf(image, start, rule, at, share, n) {
    var level = start, levels = [], tilts = [];
    for (var p = 1; p <= n; p += 1) {
      if (rule === 'switch') level = p >= at ? image : start;
      levels.push(level);
      var d = leNorm(Rsub(image, level));
      tilts.push(d);
      if (rule === 'share') level = leNorm(Radd(level, Rmul(share, d)));
    }
    return { levels: levels, tilts: tilts };
  }
  function leRoom(image, level, tilt) {
    var cx = 160, cy = 120, inner = '', rad = function (r) { return Rnum(r) * Math.PI / 180; };
    var corner = function (ang, dx, dy) {
      var c = Math.cos(ang), s = Math.sin(ang);
      return [cx + dx * c - dy * s, cy - (dx * s + dy * c)];
    };
    var a = rad(image), pts = [[-80, -80], [80, -80], [80, 80], [-80, 80]].map(function (p) { return corner(a, p[0], p[1]); });
    for (var i = 0; i < 4; i += 1) inner += phLine(pts[i][0], pts[i][1], pts[(i + 1) % 4][0], pts[(i + 1) % 4][1], i === 0 ? 'var(--amber)' : 'var(--text)');
    var l = rad(level), e1 = corner(l, -110, 0), e2 = corner(l, 110, 0);
    inner += phLine(e1[0], e1[1], e2[0], e2[1], 'var(--cyan)', ' stroke-dasharray="6 4"');
    inner += phText(330, 100, 'image ' + phDeg(image)) + phText(330, 124, 'level ' + phDeg(level)) + phText(330, 148, 'difference ' + phDeg(tilt));
    return phSvg(520, 240, 'the room as imaged, with the level dashed', inner);
  }
  function leCompute(view, inst, opts) {
    if (inst.rule === 'switch' && Rcmp(inst.at, R(2n)) < 0) {
      return { refuse: 'The jump comes at period 2 or later; period 1 is the starting level' };
    }
    var at = Number(inst.at.n), s = leSeriesOf(inst.image, inst.level, inst.rule, at, inst.share, 10), k = opts.period - 1;
    return {
      tiles: { lePerceived: phDeg(s.tilts[k]), leLevel: phDeg(s.levels[k]), leSeries: s.tilts.slice(0, 5).map(phDeg).join(', ') },
      status: 'On ' + opts.model + ', at period ' + opts.period + ' the image is tilted ' + phDeg(inst.image) + ' and the level stands at '
        + phDeg(s.levels[k]) + ', so the model predicts a tilt of ' + phDeg(s.tilts[k]) + '. '
        + (inst.rule === 'switch' ? 'The level jumps to the image at period ' + at + ', all at once.'
          : 'Each period the level moves ' + phNum(inst.share) + ' of the remaining difference.'),
      table: { caption: 'Period by period', head: ['period', 'level', 'image − level'],
        rows: s.tilts.map(function (t, i) { return [String(i + 1), phDeg(s.levels[i]), { t: phDeg(t), c: i === k ? 'tone-amber' : '' }]; }) },
      svg: leRoom(inst.image, s.levels[k], s.tilts[k])
    };
  }
"""

LEVEL_FIELDS = {
    "image": ({"kind": "deg", "what": "Tilt of the image, degrees (−180 to 180)"}, None),
    "level": ({"kind": "deg", "what": "Starting level, degrees"}, 0),
    "rule": ({"kind": "word", "words": ["switch", "share"], "what": "Re-anchoring (switch or share)"}, None),
    "at": ({"kind": "count", "what": "switch: the period the level jumps to the image"}, 2),
    "share": ({"kind": "share", "what": "share: the part of the remaining difference the level moves each period"},
              "1/2"),
}
LEVEL_VIEWS = {
    "tilt": dict(fields=["image", "level", "rule", "at", "share"], figure=True, period=True,
                 tiles=[("Predicted tilt (image − level), at the period shown", "lePerceived"),
                        ("Level, at the period shown", "leLevel"), ("Predicted tilt, periods 1 to 5", "leSeries")]),
}

# ---------------------------------------------------------------------------
# depth
# ---------------------------------------------------------------------------

DEPTH_JS = r"""
  /* depth: the classical theory's signs, in the small-angle form it states:
     convergence iod / d, disparity iod (1/near - 1/far), in radians. */
  function deSigns(iod, near, far) {
    return { near: Rdiv(iod, near), far: Rdiv(iod, far), disparity: Rmul(iod, Rsub(Rinv(near), Rinv(far))) };
  }
  function deCompute(view, inst, opts) {
    var u = opts.unit;
    if (Rcmp(inst.near, inst.far) > 0) return { refuse: 'The near distance, ' + phQty(inst.near, u) + ', is farther than the far one, ' + phQty(inst.far, u) };
    var s = deSigns(inst.iod, inst.near, inst.far);
    return {
      tiles: { deConvergence: phQty(inst.near, u) + ': ' + phApprox(s.near, 4, 'rad') + '; ' + phQty(inst.far, u) + ': ' + phApprox(s.far, 4, 'rad'),
               deDisparity: phApprox(s.disparity, 4, 'rad') },
      status: 'Eyes ' + phQty(inst.iod, u) + ' apart converge by ' + phApprox(s.near, 4, 'rad') + ' on a point at ' + phQty(inst.near, u)
        + ' and ' + phApprox(s.far, 4, 'rad') + ' at ' + phQty(inst.far, u) + '; the disparity between the two is '
        + phApprox(s.disparity, 4, 'rad') + '. On ' + opts.model + ' the mind reads depth from these signs; the lab computes the signs, not a depth anyone sees.',
      table: null
    };
  }
"""

DEPTH_FIELDS = {
    "iod": ({"kind": "pos", "what": "Interocular distance"}, None),
    "near": ({"kind": "pos", "what": "Near distance"}, None),
    "far": ({"kind": "pos", "what": "Far distance"}, None),
}
DEPTH_VIEWS = {
    "binocular": dict(fields=["iod", "near", "far"], unit=True,
                      tiles=[("Convergence (iod / distance, small-angle radians)", "deConvergence"),
                             ("Disparity, iod × (1/near − 1/far)", "deDisparity")]),
}

# ---------------------------------------------------------------------------
# motion
# ---------------------------------------------------------------------------

MOTION_JS = r"""
  /* motion: the implied speed, and the band the interval falls in by the
     thresholds as later textbooks report Wertheimer (1912). */
  function moBandOf(interval, sim, succ) {
    if (Rcmp(interval, sim) < 0) return 'seen together';
    return Rcmp(interval, succ) <= 0 ? 'motion' : 'seen in succession';
  }
  function moCompute(view, inst, opts) {
    if (Rcmp(inst.simultaneous, inst.succession) > 0) {
      return { refuse: 'The simultaneity threshold, ' + phNum(inst.simultaneous) + ' ms, is above the succession threshold, ' + phNum(inst.succession) + ' ms' };
    }
    var v = Rdiv(inst.separation, inst.interval), band = moBandOf(inst.interval, inst.simultaneous, inst.succession);
    return {
      tiles: { moSpeed: phNum(v) + ' ' + opts.unit + ' per ms', moBand: band },
      status: 'Two lights ' + phQty(inst.separation, opts.unit) + ' apart, ' + phNum(inst.interval) + ' ms between them, imply a speed of '
        + phNum(v) + ' ' + opts.unit + ' per ms. On ' + opts.model + ' (together below ' + phNum(inst.simultaneous) + ' ms, in succession above '
        + phNum(inst.succession) + ' ms), the interval falls in the band: ' + band + '. Two lights are two lights: nothing in these figures moves.',
      table: null
    };
  }
"""

MOTION_FIELDS = {
    "separation": ({"kind": "pos", "what": "Separation of the two lights"}, None),
    "interval": ({"kind": "pos", "what": "Interval between them, ms"}, None),
    "simultaneous": ({"kind": "pos", "what": "Below this many ms: seen together (textbook figure)"}, 30),
    "succession": ({"kind": "pos", "what": "Above this many ms: seen in succession (textbook figure)"}, 200),
}
MOTION_VIEWS = {
    "phi": dict(fields=["separation", "interval", "simultaneous", "succession"], unit=True,
                tiles=[("Implied speed", "moSpeed"), ("Band, by the textbook thresholds", "moBand")]),
}

# ---------------------------------------------------------------------------
# light
# ---------------------------------------------------------------------------

LIGHT_JS = r"""
  /* light: luminance = reflectance x illumination (the empiricist's sensation),
     and each surface's luminance over the surround's (Wallach's ratio). */
  function liLuminances(surfaces) { return surfaces.map(function (s) { return Rmul(s.reflectance, s.illumination); }); }
  function liBrightestOf(surfaces, lum) {
    var top = lum.reduce(function (m, x) { return Rcmp(x, m) > 0 ? x : m; }, lum[0]);
    return surfaces.filter(function (_s, k) { return Requ(lum[k], top); }).map(function (s) { return s.name; });
  }
  function liCompute(view, inst, opts) {
    var lum = liLuminances(inst.surfaces), at = -1;
    inst.surfaces.forEach(function (s, k) { if (s.name.toLowerCase() === inst.surround.toLowerCase()) at = k; });
    if (at < 0) return { refuse: 'The surround, "' + inst.surround + '", is not one of the surfaces' };
    if (Rzero(lum[at])) return { refuse: 'The surround sends no light, so no ratio to it exists' };
    var ratio = lum.map(function (x) { return Rdiv(x, lum[at]); }), top = liBrightestOf(inst.surfaces, lum);
    var each = function (v) { return inst.surfaces.map(function (s, k) { return s.name + ' ' + phNum(v[k]); }).join(', '); };
    return {
      tiles: { liLuminance: each(lum), liRatio: each(ratio), liBrightest: top.join(', ') },
      status: 'Luminance is reflectance × illumination: ' + each(lum) + '. On ' + opts.model + ', a surface\'s ratio to the surround ('
        + inst.surfaces[at].name + ', ' + phNum(lum[at]) + ') is ' + each(ratio) + '. Greatest luminance: '
        + top.join(', ') + '. The lab computes the light, not the colour anyone sees.',
      table: { caption: 'Each surface', head: ['surface', 'reflectance', 'illumination', 'luminance', 'over the surround'],
        rows: inst.surfaces.map(function (s, k) { return [s.name, phNum(s.reflectance), phNum(s.illumination), phNum(lum[k]), phNum(ratio[k])]; }) }
    };
  }
"""

LIGHT_FIELDS = {
    "surfaces": ({"kind": "rec", "sub": [["name", _NAME], ["reflectance", {"kind": "share"}],
                                         ["illumination", {"kind": "nn"}]], "lo": 1, "hi": 6, "unique": True,
                  "what": "Surfaces: name, reflectance (0 to 1), illumination; separated by ;"}, None),
    "surround": ({"kind": "name", "what": "The surface that is the surround"}, None),
}
LIGHT_VIEWS = {
    "ratio": dict(fields=["surfaces", "surround"],
                  tiles=[("Luminance, each surface", "liLuminance"), ("Ratio to the surround", "liRatio"),
                         ("Greatest luminance", "liBrightest")]),
}

# ---------------------------------------------------------------------------
# triangle
# ---------------------------------------------------------------------------

TRIANGLE_JS = r"""
  /* triangle: the third angle is 180 - a - b; the parallel through a vertex
     makes alternate angles equal to the two angles at the other vertices. */
  function trAnglesAt(a, b, c, vertex) {
    if (vertex === 'A') return [b, a, c];
    if (vertex === 'B') return [a, b, c];
    return [a, c, b];
  }
  function trFigure(a, b, vertex) {
    /* Pixels only: the vertices placed by floating-point trigonometry. */
    var ra = Rnum(a) * Math.PI / 180, rb = Rnum(b) * Math.PI / 180, rc = Math.PI - ra - rb;
    var ac = Math.sin(rb) / Math.sin(rc), P = { A: [0, 0], B: [1, 0], C: [ac * Math.cos(ra), ac * Math.sin(ra)] };
    var xs = [0, 1, P.C[0]], lo = Math.min.apply(null, xs), hi = Math.max.apply(null, xs);
    var sc = Math.min(440 / Math.max(hi - lo, 1e-9), 180 / Math.max(P.C[1], 1e-9));
    var px = function (p) { return [100 + (p[0] - lo) * sc, 220 - p[1] * sc]; }, inner = '';
    var A = px(P.A), B = px(P.B), C = px(P.C);
    inner += phLine(A[0], A[1], B[0], B[1], 'var(--text)') + phLine(B[0], B[1], C[0], C[1], 'var(--text)') + phLine(C[0], C[1], A[0], A[1], 'var(--text)');
    var V = { A: A, B: B, C: C }[vertex], opp = { A: [B, C], B: [C, A], C: [A, B] }[vertex];
    var dx = opp[1][0] - opp[0][0], dy = opp[1][1] - opp[0][1], len = Math.sqrt(dx * dx + dy * dy) || 1;
    inner += phLine(V[0] - 300 * dx / len, V[1] - 300 * dy / len, V[0] + 300 * dx / len, V[1] + 300 * dy / len, 'var(--amber)', ' stroke-dasharray="6 4"');
    inner += phText(A[0] - 14, A[1] + 16, 'A') + phText(B[0] + 6, B[1] + 16, 'B') + phText(C[0] + 6, C[1] - 6, 'C');
    return phSvg(640, 250, 'the triangle and the parallel through ' + vertex, inner);
  }
  function trCompute(view, inst, opts) {
    var a = inst.a, b = inst.b;
    if (Rsign(a) <= 0 || Rsign(b) <= 0 || Rcmp(Radd(a, b), R(180n)) >= 0) {
      return { refuse: 'No triangle has angles of ' + phDeg(a) + ' and ' + phDeg(b) + ' at A and B: each must be more than 0°, and together less than 180°' };
    }
    var c = Rsub(Rsub(R(180n), a), b), v = opts.vertex, t = trAnglesAt(a, b, c, v);
    return {
      tiles: { trC: phDeg(c), trAlternate: phDeg(t[0]) + ' and ' + phDeg(t[2]),
               trStraight: t.map(phDeg).join(' + ') + ' = ' + phDeg(phSum(t)) },
      status: 'On ' + opts.model + ', the angles at A and B are ' + phDeg(a) + ' and ' + phDeg(b) + ', so the angle at C is 180° − '
        + phDeg(a) + ' − ' + phDeg(b) + ' = ' + phDeg(c) + '. The parallel through ' + v + ' makes alternate angles of ' + phDeg(t[0])
        + ' and ' + phDeg(t[2]) + ', and with the angle at ' + v + ' they lie along one straight line.',
      table: null,
      svg: trFigure(a, b, v)
    };
  }
"""

TRIANGLE_FIELDS = {
    "a": ({"kind": "num", "what": "Angle at A, degrees"}, None),
    "b": ({"kind": "num", "what": "Angle at B, degrees"}, None),
}
TRIANGLE_VIEWS = {
    "parallel": dict(fields=["a", "b"], figure=True, vertex=True,
                     tiles=[("Angle at C", "trC"), ("Alternate angles at the parallel", "trAlternate"),
                            ("Along the parallel", "trStraight")]),
}

# ---------------------------------------------------------------------------
# time
# ---------------------------------------------------------------------------

TIME_JS = r"""
  /* time/river: on the bank, the water downstream of the observer has passed;
     carried by the current, the water downstream is still to come. With no
     observer, every parcel is simply where it is. */
  function tiRiverOf(parcels, observer, standpoint) {
    if (observer === null) return { past: [], future: [] };
    var down = parcels.filter(function (p) { return Rcmp(p.position, observer) > 0; }).map(function (p) { return p.name; });
    var up = parcels.filter(function (p) { return Rcmp(p.position, observer) < 0; }).map(function (p) { return p.name; });
    return standpoint === 'bank' ? { past: down, future: up } : { past: up, future: down };
  }
  /* time/diagram and ekstasis: under the present at position p, the moment at
     i < p is retained at depth p - i. */
  function tiColumnOf(moments, p) {
    var out = [];
    for (var i = 0; i < p; i += 1) out.push({ name: moments[i], depth: p - i });
    return out;
  }
  function tiPrimes(name, depth) { var s = name; for (var i = 0; i < depth; i += 1) s += '′'; return s; }
  /* The order of the moments in each column, compared column by column
     against the longest one. */
  function tiOrderOf(columns) {
    var ref = columns.reduce(function (m, c) { return c.seq.length > m.seq.length ? c : m; }, columns[0]);
    if (!ref.seq.length) return 'no column retains a moment';
    for (var k = 0; k < columns.length; k += 1) {
      var mine = ref.seq.filter(function (n) { return columns[k].seq.indexOf(n) >= 0; });
      if (mine.join('|') !== columns[k].seq.join('|') || mine.length !== columns[k].seq.length) {
        return 'the column at ' + columns[k].present + ' breaks the order ' + ref.seq.join(', ');
      }
    }
    return 'the order ' + ref.seq.join(', ') + ' is the same in every column';
  }
  function tiDiagram(moments, presents, span) {
    var n = moments.length, step = 520 / Math.max(n - 1, 1), y0 = 30, inner = '';
    var x = function (i) { return 60 + i * step; }, deepest = Math.max.apply(null, presents.map(function (p) { return p; }));
    inner += phLine(x(0), y0, x(n - 1), y0, 'var(--text)');
    moments.forEach(function (m, i) { inner += phText(x(i), y0 - 10, m, 'middle'); });
    var dy = Math.min(step, 200 / Math.max(deepest, 1));
    presents.forEach(function (p) {
      inner += phLine(x(p), y0, x(p), y0 + p * dy, 'var(--amber)');
      for (var i = 0; i < p; i += 1) {
        inner += phLine(x(i), y0, x(p), y0 + (p - i) * dy, 'var(--cyan)', ' stroke-dasharray="4 4"');
        inner += '<circle cx="' + phPx(x(p)) + '" cy="' + phPx(y0 + (p - i) * dy) + '" r="4" fill="var(--amber)"></circle>';
      }
      for (var j = 1; j <= span && p + j < n; j += 1) inner += phLine(x(p + j - 1), y0 + 6, x(p + j), y0 + 6, 'var(--green)', ' stroke-dasharray="2 4"');
    });
    return phSvg(640, 260, 'the diagram of retention: the line of nows, the obliques of sinking, the vertical at the present', inner);
  }
  function tiFind(moments, name) {
    for (var i = 0; i < moments.length; i += 1) if (moments[i].toLowerCase() === name.toLowerCase()) return i;
    return -1;
  }
  function tiCompute(view, inst, opts) {
    if (view === 'river') {
      var r = tiRiverOf(inst.parcels, inst.observer, inst.standpoint);
      return {
        tiles: { tiWorld: inst.parcels.map(function (p) { return p.name + ' at ' + phNum(p.position); }).join(', '),
                 tiPast: phNames(r.past), tiFuture: phNames(r.future) },
        status: inst.observer === null ? 'With no observer, every parcel of water is present where it is; nothing is past or future.'
          : 'On ' + opts.model + ', an observer at ' + phNum(inst.observer) + (inst.standpoint === 'bank' ? ' on the bank' : ' carried by the current')
            + ' counts ' + phNames(r.past) + ' as past and ' + phNames(r.future) + ' as future. In the river itself every parcel is present where it is.',
        table: null
      };
    }
    if (view === 'diagram') {
      var p = tiFind(inst.moments, inst.present);
      if (p < 0) return { refuse: 'The present, "' + inst.present + '", is not one of the moments: ' + inst.moments.join(', ') };
      var col = tiColumnOf(inst.moments, p), span = Number(inst.protention.n);
      var ahead = inst.moments.slice(p + 1, p + 1 + span);
      return {
        tiles: { tiRetained: phNames(col.map(function (c) { return c.name + ' at depth ' + c.depth; })),
                 tiProtended: phNames(ahead),
                 tiColumn: [inst.moments[p]].concat(col.slice().reverse().map(function (c) { return tiPrimes(c.name, c.depth); })).join(', ') },
        status: 'On ' + opts.model + ', at the present ' + inst.moments[p] + ' each earlier moment is held at a depth: '
          + phNames(col.map(function (c) { return c.name + ' at ' + c.depth; })) + '. '
          + (ahead.length < span ? 'The protention spans ' + span + ', and the list names only ' + ahead.length + ' moment' + (ahead.length === 1 ? '' : 's') + ' after the present. '
            : '') + 'A retention is not a copy recalled: the diagram computes depths, not memories.',
        table: null,
        svg: tiDiagram(inst.moments, [p], span)
      };
    }
    /* ekstasis */
    var at = [];
    for (var k = 0; k < inst.presents.length; k += 1) {
      var i = tiFind(inst.moments, inst.presents[k]);
      if (i < 0) return { refuse: 'The present "' + inst.presents[k] + '" is not one of the moments: ' + inst.moments.join(', ') };
      if (at.indexOf(i) >= 0) return { refuse: 'The present ' + inst.presents[k] + ' is listed twice' };
      at.push(i);
    }
    var columns = at.map(function (i) { return { present: inst.moments[i], seq: tiColumnOf(inst.moments, i).map(function (c) { return c.name; }), col: tiColumnOf(inst.moments, i) }; });
    var depths = inst.moments.map(function (m, mi) {
      var ds = at.filter(function (i) { return i > mi; }).map(function (i) { return i - mi; });
      return ds.length ? m + ': ' + ds.join(', ') : null;
    }).filter(function (x) { return x; });
    return {
      tiles: { tiColumns: columns.map(function (c) { return c.present + ': ' + phNames(c.col.map(function (x) { return x.name + ' ' + x.depth; })); }).join('; '),
               tiDepths: depths.length ? depths.join('; ') : 'none', tiOrder: tiOrderOf(columns) },
      status: 'On ' + opts.model + ', each present has its own column of retained moments; one moment sinks deeper under each later present, '
        + 'and the lab compares the order of the moments column by column. No single column is the whole of time.',
      table: null,
      svg: tiDiagram(inst.moments, at, 0)
    };
  }
"""

_MOMENTS = {"kind": "list", "each": _NAME, "sep": "comma", "lo": 1, "hi": 9, "unique": True,
            "what": "Moments, in order"}
TIME_FIELDS = {
    "parcels": ({"kind": "rec", "sub": [["name", _NAME], ["position", {"kind": "num"}]], "lo": 1, "hi": 9,
                 "unique": True, "what": "Parcels of water: name, position downstream; separated by ;"}, None),
    "observer": ({"kind": "numnone", "what": "The observer's position (or none)"}, None),
    "standpoint": ({"kind": "word", "words": ["bank", "current"], "what": "Standpoint (bank or current)"}, "bank"),
    "moments": (_MOMENTS, None),
    "present": ({"kind": "name", "what": "The present"}, None),
    "protention": ({"kind": "nncount", "what": "Protention span, in moments"}, 0),
    "presents": ({"kind": "list", "each": _NAME, "sep": "comma", "lo": 1, "hi": 9,
                  "what": "Presents, in turn"}, None),
}
TIME_VIEWS = {
    "river": dict(fields=["parcels", "observer", "standpoint"],
                  tiles=[("Every parcel, where it is now", "tiWorld"), ("Past, from the standpoint", "tiPast"),
                         ("Future, from the standpoint", "tiFuture")]),
    "diagram": dict(fields=["moments", "present", "protention"], figure=True,
                    tiles=[("Retained, with depth", "tiRetained"), ("Protended", "tiProtended"),
                           ("The vertical at the present", "tiColumn")]),
    "ekstasis": dict(fields=["moments", "presents"], figure=True,
                     tiles=[("Each present's column", "tiColumns"), ("Each moment's depth under later presents", "tiDepths"),
                            ("Order of the moments", "tiOrder")]),
}

# ---------------------------------------------------------------------------
# The modes
# ---------------------------------------------------------------------------

# mode: (prefix, JS, fn, fields, views, title, subtitle, family, default model)
_MODES = {
    "stimulus": ("st", STIMULUS_JS, "stCompute", STIMULUS_FIELDS, STIMULUS_VIEWS,
                 "A model's prediction from the stimulus", "the predicted difference beside the reported one", 1,
                 "the model named above"),
    "grouping": ("gr", GROUPING_JS, "grCompute", GROUPING_FIELDS, GROUPING_VIEWS,
                 "Grouping by proximity", "dots on a line, and the groups a gap rule predicts", 1,
                 "the Gestalt proximity rule (Wertheimer, 1923)"),
    "cues": ("cu", CUES_JS, "cuCompute", CUES_FIELDS, CUES_VIEWS,
             "Candidates and cues", "what fits what was seen, and what each cue removes", 1,
             "the model named above"),
    "size": ("sz", SIZE_JS, "szCompute", SIZE_FIELDS, SIZE_VIEWS,
             "Size and distance", "angular size, and what two accounts predict from it", 1, "geometric optics"),
    "perspective": ("pe", PERSPECTIVE_JS, "peCompute", PERSPECTIVE_FIELDS, PERSPECTIVE_VIEWS,
                    "Faces and views", "what a box shows from each direction, exactly", 1, "parallel projection"),
    "variation": ("vr", VARIATION_JS, "vrCompute", VARIATION_FIELDS, VARIATION_VIEWS,
                  "Free variation", "what every variant of the kind keeps", 2, "the lesson's coding"),
    "cases": ("ca", CASES_JS, "caCompute", None, CASES_VIEWS,
              "Cases against the accounts", "the lesson's coding, counted", 2, "the lesson's coding"),
    "schema": ("sc", SCHEMA_JS, "scCompute", SCHEMA_FIELDS, SCHEMA_VIEWS,
               "The body's space", "positions, reaches and obstacles relative to a body", 3, LESSON),
    "sorting": ("so", SORTING_JS, "soCompute", SORTING_FIELDS, SORTING_VIEWS,
                "Sorting colour samples", "a categorical sort beside a chain of resemblances", 3, LESSON),
    "level": ("le", LEVEL_JS, "leCompute", LEVEL_FIELDS, LEVEL_VIEWS,
              "The spatial level", "tilt as image minus level, period by period", 3, LESSON),
    "depth": ("de", DEPTH_JS, "deCompute", DEPTH_FIELDS, DEPTH_VIEWS,
              "Signs of depth", "convergence and disparity, in the small-angle form", 1,
              "the classical theory of depth from signs"),
    "motion": ("mo", MOTION_JS, "moCompute", MOTION_FIELDS, MOTION_VIEWS,
               "Two lights in alternation", "the implied speed, and the band the interval falls in", 1,
               "Wertheimer's bands, as later textbooks report them"),
    "light": ("li", LIGHT_JS, "liCompute", LIGHT_FIELDS, LIGHT_VIEWS,
              "Luminance and the surround", "reflectance × illumination, and each ratio to the surround", 1,
              "luminance as reflectance × illumination, with the ratio to the surround"),
    "triangle": ("tr", TRIANGLE_JS, "trCompute", TRIANGLE_FIELDS, TRIANGLE_VIEWS,
                 "The geometer's parallel", "the angles of a triangle, through a parallel at a vertex", 3, LESSON),
    "time": ("ti", TIME_JS, "tiCompute", TIME_FIELDS, TIME_VIEWS,
             "Time", "standpoints, retention and the columns of the diagram", 3, LESSON),
}
MODES = tuple(_MODES)

_BASE_KEYS = {"mode", "view", "presets", "preset", "title", "panel_title", "panel_intro", "model"}
_UNIT_MODES = ("depth", "motion")


def _intro(family, model):
    if family == 1:
        return ("This lab computes %s, exactly, from the figures as typed. Each tile is what that model predicts "
                "from the stimulus; none is a report of what is perceived." % model)
    if family == 2:
        return ("This lab counts the lesson's coding of the cases. Each cell is the lesson's reading of the chapter; "
                "the lab decides no cell, and the count is exact.")
    return ("This lab computes the lesson's model, exactly, from the figures as typed. The model illustrates the "
            "chapter; it is not the book's theory or an opponent's, and no figure is a report of experience.")


def _fields(mode, fields, view_fields):
    out = []
    for f in view_fields:
        if isinstance(f, str):
            spec, default = fields[f]
            out.append((f, spec, default))
        elif len(f) == 2:
            spec, default = fields[f[1]]
            out.append((f[0], spec, default))
        else:
            out.append(f)
    return out


def _accounts(cfg, kit):
    acc = cfg.get("accounts")
    if not isinstance(acc, list) or not 2 <= len(acc) <= 3:
        raise ValueError("%s: cfg['accounts'] must list the two or three opponents' accounts (PLAN.md D.1, cases); "
                         "the lesson fixes them and no preset can change them" % kit)
    for a in acc:
        if not isinstance(a, str) or not a.strip() or pc._BAD_NAME.search(a):
            raise ValueError("%s: account name %r is not usable (no , ; : = < > & or quotes)" % (kit, a))
    if len({a.lower() for a in acc}) != len(acc):
        raise ValueError("%s: cfg['accounts'] names an account twice" % kit)
    return [a.strip() for a in acc]


def _mode_lab(cfg, mode):
    prefix, js, fn, fields, views, title, subtitle, family, model_default = _MODES[mode]
    kit = "%s/%s" % (KIT, mode)
    view = pc.pick_view(cfg, kit, list(views))
    spec = views[view]
    family, model_default = spec.get("family", family), spec.get("model", model_default)
    kit = "%s/%s/%s" % (KIT, mode, view)
    model = pc.plain(cfg, kit, "model", model_default)
    fixed = {"model": model}
    allowed_keys = set(_BASE_KEYS)
    redraw = []
    if mode == "cases":
        acc = _accounts(cfg, kit)
        allowed_keys |= {"accounts", "pair"}
        sub = [["observation", {"kind": "name"}]] + [["a%d" % k, {"kind": "cell"}] for k in range(len(acc))]
        obs = {"kind": "rec", "sub": sub, "lo": 1, "hi": 10, "unique": True,
               "what": "Observations: name, then y, n or - for %s; separated by ;" % ", ".join(acc)}
        field_rows = [("observations", obs, None)]
        fixed["accounts"] = acc
        pairs = [(i, j) for i in range(len(acc)) for j in range(i + 1, len(acc))]
        want = cfg.get("pair", acc[:2])
        if not isinstance(want, list) or len(want) != 2 or any(w not in acc for w in want) or want[0] == want[1]:
            raise ValueError("%s: cfg['pair'] must name two different accounts of %s" % (kit, acc))
        i, j = sorted(acc.index(w) for w in want)
        redraw.append(dict(key="pair", id="caPair", label="Compare", value="%d-%d" % (i, j),
                           options=[("%d-%d" % (a, b), "%s against %s" % (acc[a], acc[b])) for a, b in pairs]))
    else:
        field_rows = _fields(mode, fields, spec["fields"])
    if spec.get("unit") or mode in _UNIT_MODES:
        allowed_keys.add("unit")
        unit = cfg.get("unit", "cm")
        if unit not in pc.UNITS:
            raise ValueError("%s: cfg['unit'] is %r; it is one of %s" % (kit, unit, ", ".join(pc.UNITS)))
        fixed["unit"] = unit
    if view == "own":
        allowed_keys.add("allowed")
        allowed = cfg.get("allowed")
        if allowed is not None:
            if not isinstance(allowed, list) or not allowed:
                raise ValueError("%s: cfg['allowed'] is a list of view directions" % kit)
            fixed["allowed"] = [" ".join(str(c) for c in pc.parse_dir(kit, str(a), "allowed view")) for a in allowed]
        else:
            fixed["allowed"] = None
    if spec.get("step"):
        allowed_keys |= {"step", "cue_text"}
        cue_text = cfg.get("cue_text", {})
        if not isinstance(cue_text, dict) or any(not isinstance(v, str) or "<" in v or ">" in v for v in cue_text.values()):
            raise ValueError("%s: cfg['cue_text'] maps a cue id to a plain sentence" % kit)
        fixed["cue_text"] = cue_text
    if spec.get("period"):
        allowed_keys.add("period")
        n = cfg.get("period", 1)
        if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 10:
            raise ValueError("%s: cfg['period'] is %r; the range runs 1 to 10" % (kit, n))
        redraw.append(dict(key="period", id="lePeriod", label="Period shown", lo=1, hi=10, value=n))
    if spec.get("vertex"):
        allowed_keys.add("vertex")
        v = cfg.get("vertex", "C")
        if v not in ("A", "B", "C"):
            raise ValueError("%s: cfg['vertex'] is %r; it is A, B or C" % (kit, v))
        redraw.append(dict(key="vertex", id="trVertex", label="Parallel through vertex", value=v,
                           options=[("A", "A"), ("B", "B"), ("C", "C")]))
    stray = sorted(set(cfg) - allowed_keys)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed_keys))))
    if spec.get("step"):
        # The range runs 1 .. the longest cue list in the lesson's presets
        # (D.1): fixed by the cfg, never by the preset shown.
        lists = [pc.parse("%s preset %r" % (kit, p.get("id")), CUES_FIELDS["cues"][0], pc.to_text(kit, CUES_FIELDS["cues"][0], p["cues"]))
                 for p in cfg.get("presets") or [] if isinstance(p, dict) and "cues" in p]
        hi = max([len(x) for x in lists] or [1])
        n = cfg.get("step", hi)
        if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= hi:
            raise ValueError("%s: cfg['step'] is %r; the range runs 1 to %d, the longest cue list" % (kit, n, hi))
        redraw.insert(0, dict(key="step", id="cuStep", label="Cues shown", lo=1, hi=hi, value=n))
    lab = pc.mode_lab(cfg, kit=kit, prefix=prefix, view=view, fields=field_rows, tiles=spec["tiles"],
                      mode_js=js, fn=fn, fixed=fixed, title=title, subtitle=subtitle,
                      panel_title="Change the figures, or choose a worked example",
                      panel_intro=_intro(family, model), redraw=redraw, figure=bool(spec.get("figure")),
                      fixed_keys=tuple(sorted(allowed_keys - _BASE_KEYS)) + ("model",))
    if view == "own" and fixed["allowed"]:
        for p in cfg["presets"]:
            where = "%s preset %r" % (kit, p["id"])
            for rec in pc.parse(where, _VIEWS, pc.to_text(where, _VIEWS, p["views"])):
                if " ".join(str(c) for c in rec["direction"]) not in fixed["allowed"]:
                    raise ValueError("%s: view %s is not among the lesson's views %s"
                                     % (where, rec["direction"], fixed["allowed"]))
    return lab


def phenkit_lab(cfg):
    """The Phenomenology of Perception kit. `cfg["mode"]` chooses the mode; an unknown mode or view raises."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in _MODES:
        raise ValueError("phenkit_lab: unknown mode %r; the fifteen modes are %s" % (mode, ", ".join(MODES)))
    return _mode_lab(cfg, mode)


__all__ = ["phenkit_lab", "MODES"]
