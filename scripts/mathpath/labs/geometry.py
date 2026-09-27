"""Geometric Algorithms -- eight modes over one list of INTEGER points.

WHAT THIS KIT PROVES, and it is one thing said eight ways: every question this
course asks -- which side, do they cross, which is closer, what is the area, is
the point inside, how far apart are the two furthest -- reduces to the SIGN of a
determinant, and that sign is either exact or it is worthless. `algo_core`'s
GEOM_JS computes every determinant in BigInt for that reason. This kit adds the
part a reader cannot be told: what the same arithmetic in double precision does
to the same input, measured on the page rather than warned about in a footnote.

THE MEASUREMENT THE COURSE IS BUILT ON. `orient2Float` is the one deliberate
floating-point routine in GEOM_JS, and it is there to be wrong in front of the
reader. At a = (0, 0), b = (2^k + 1, 2^k), c = (2^k, 2^k - 1) the exact
determinant is -1 for every k -- a right turn, always. In doubles the two
products are 2^2k - 1 and 2^2k, which are the same double as soon as 2k > 53, so
the test reports 0 and the three points read as collinear. The `orient` mode
sweeps k from 20 to 48 and counts the disagreements; the threshold is k = 27 and
nothing about it is an estimate.

AND WHAT THAT COSTS. `hull`'s predicate control runs Andrew's monotone chain
with `orientSign` and then again with the double, changing nothing else. On the
same three points the exact chain returns three vertices and the double chain
returns two: a false "collinear" pops a real vertex off the stack and the hull
comes back with a corner missing. That is the whole argument for exact
predicates, and it is a number on the page.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE. Nothing here
reimplements an algorithm from GEOM_JS. What this kit adds is the CHECKING, and
every mode carries an oracle that answers the same question by a route that
shares no code with the algorithm:

  geoVertexBrute      p is a hull vertex iff p is outside the convex hull of
                      the other points, and p is outside a hull iff some line
                      through p has every other point weakly on one side AND
                      every point ON that line strictly beyond p along it. No
                      sort, no stack, no incremental anything -- the definition,
                      in BigInt, at O(n^3).
  geoBoundaryBrute    the same definition without the second clause, which is
                      the BOUNDARY rather than the vertex set. The two differ
                      exactly where three points are collinear, and that
                      difference is what separates the two hull algorithms'
                      answers on degenerate input.
  geoSegOracle        two segments cross iff the parametric system has a
                      solution with both parameters in [0, 1] -- solved in
                      BigInt with no division, by comparing numerators against
                      the determinant. `straddle` answers the same question
                      from four orientation signs; they are different
                      computations and the mode prints both.
  geoAreaTrapezoid    2A by the trapezoid rule, sum (x_i - x_{i+1})(y_i +
                      y_{i+1}), against `shoelace2`'s sum of cross products.
  geoWinding          the WINDING NUMBER, which is a different question from ray
                      parity and happens to give the same verdict on a simple
                      polygon. The mode checks the polygon is simple before it
                      says so.
  geoClosestBrute     every pair.
  geoSweepBrute       every pair, through geoSegOracle.
  geoDet3             the same determinant as the cofactor expansion of
                      [[ax, ay, 1], [bx, by, 1], [cx, cy, 1]] -- six products
                      of the coordinates themselves rather than of their
                      differences, so a transposed term in either shows as a
                      disagreement rather than as a plausible number. The
                      mathcheck section adds a third route over algebra_core's
                      rationals.

DEGENERATE INPUT IS THE SUBJECT, NOT AN EDGE CASE, and three kinds of it are on
the page rather than excluded from the presets:

  three collinear points   the `edges` preset puts a point in the middle of
                           each side of a square. The monotone chain returns
                           four vertices, gift wrapping returns six, and the
                           boundary oracle returns eight. All three are right
                           about different questions and the page says which.
  duplicate points         `geoDedupe` removes them and REPORTS how many,
                           because both hull routines mishandle them: the chain
                           can return the same point twice and gift wrapping
                           does return it twice. Deduplication is the lesson,
                           not a workaround, and the count is a KPI.
  a hull that is a segment the `segment` preset is five collinear points. The
                           chain returns the two ends; gift wrapping returns all
                           five; and one point on its own is the case
                           `monotoneChain` gets wrong (see the defect note).

A DEFECT IN A FILE THIS KIT DOES NOT OWN, worked around here and reported
rather than patched. `algo_core.monotoneChain` on a single point returns
`hull: [], h: 0` -- `lower` and `upper` are both `[p]` and both are sliced to
nothing. The hull of one point is that point. `geoChainWith` below is the same
algorithm with the predicate as a parameter (which is what the float arm needs
anyway) and it returns `[p]`; scripts/mathcheck.js pins it to `monotoneChain` on
every input with two or more distinct points, so the two cannot drift, and
asserts the one-point disagreement so the defect cannot be silently fixed
without this note being revisited. The same file's `jarvis` includes SOME
collinear boundary points and not others -- on a square with a midpoint on
each side it returns two of those four midpoints and not the other two --
because its tie-break is the index order of the lexicographic sort. It is a boundary walk, not a vertex list, and the `hull`
mode labels it as one and checks it against `geoBoundaryBrute` rather than
against the vertex set.

THE MODES, and the figure each one is for:

  orient     the exact determinant, the same determinant by cofactors, the
             double, and the swept family where the double's answer changes
  hull       both hull algorithms, both predicates, the brute-force vertex set,
             pushes and pops against 2n, and n*h against n log2 n
  segments   four orientation signs, the box filter, and the parametric oracle,
             on the collinear and touching cases where implementations are wrong
  sweep      pair tests actually made against all C(k, 2) of them, and the
             crossing set against every pair
  closest    the divide-and-conquer squared distance against every pair, and the
             strip comparisons against 7n
  polygon    2A twice, the orientation the sign carries, ray parity including
             the vertex rule, and the winding number
  calipers   the squared diameter from h antipodal pairs against all C(n, 2)
  kdtree     nodes visited by a range query against n, and the points found
             against a scan

Every figure on every one of these pages is an integer or an exact fraction.
Three things are not, and each is labelled where it appears: `orient2Float`,
which is the subject; the n log2 n reference column, which is a drawing and no
verdict is read off it; and the decimal printed after each exact fraction,
which is a reading aid beside the value rather than the value.

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped. COUNT_JS,
GEOM_JS and this kit's own block are on every page here. The rest is added only
where it is called:

    ALGO_JS      hull      -- `ilog2`, and only `hull`. `jarvis` returns
                 n log2 n as a field and therefore calls it whether or not the
                 page prints one; nothing else in GEOM_JS takes a logarithm,
                 so `calipers` carried the block for nothing until the modes
                 were audited for what they actually call.
    TREEDRAW_JS  kdtree    -- the 2-d tree is drawn as a tree.
    RATIONAL_JS  polygon, closest, kdtree -- the area as a fraction, and the
                 measured-against-bound ratios. A ratio of two integers is
                 printed as the fraction, with the decimal beside it rather
                 than instead of it.

Measured, on a lesson page rendered by scripts/mathpath/render.py -- gzipped,
against the repository's 62 KB ceiling. Re-derive rather than trusting these;
they go stale as the engine grows:

    calipers 33.7   sweep 33.8   segments 33.9   orient 34.2   closest 35.6
    polygon 36.0   kdtree 36.6   hull 37.4

The spread is the block table above and nothing else: `hull` is the heaviest
because it is the only mode that carries ALGO_JS, `kdtree` next because it is
the only one that carries the tree renderer, and the four lightest carry
neither.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, GEOM_JS, TREEDRAW_JS
from .algorithms import ALGO_JS
from .common import Lab

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, nothing closed over a DOM
# element, so scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

GEOKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     A clause is `x, y` and clauses are separated by semicolons or newlines.
     Coordinates are WHOLE NUMBERS and a decimal point is refused rather than
     rounded: every predicate below is a BigInt determinant, and a coordinate
     that is not an integer is a coordinate this course cannot be exact about.
     Anything past 2^53 is refused too -- not because the determinant would
     overflow, which it cannot, but because the NUMBER the reader typed would
     already be the wrong number before any determinant was taken. */
  function geoParse(text, cap) {
    var clauses = String(text === undefined || text === null ? '' : text)
                    .replace(/[()\[\]]/g, ' ').split(/[;\n]+/);
    var pts = [], i;
    for (i = 0; i < clauses.length; i += 1) {
      var body = clauses[i].trim();
      if (!body) continue;
      var parts = body.split(/[,\s]+/).filter(function (s) { return s.length; });
      if (parts.length !== 2) return { bad: 'clause ' + (i + 1) + ' is not one point' };
      if (!/^-?\d+$/.test(parts[0]) || !/^-?\d+$/.test(parts[1])) {
        return { bad: 'every coordinate must be a whole number' };
      }
      var x = parseInt(parts[0], 10), y = parseInt(parts[1], 10);
      if (!Number.isSafeInteger(x) || !Number.isSafeInteger(y)) {
        return { bad: 'a coordinate is past 2^53, where the input itself is already rounded' };
      }
      pts.push([x, y]);
    }
    if (!pts.length) return { bad: 'no points' };
    if (cap && pts.length > cap) return { bad: pts.length + ' points, and this mode stops at ' + cap };
    return { points: pts };
  }
  function geoParseSegments(text, cap) {
    var p = geoParse(text, cap ? 2 * cap : 0);
    if (p.bad) return p;
    if (p.points.length % 2 !== 0) return { bad: 'a segment is two points, so the count must be even' };
    var segs = [], i;
    for (i = 0; i < p.points.length; i += 2) segs.push([p.points[i], p.points[i + 1]]);
    if (!segs.length) return { bad: 'no segments' };
    return { segments: segs, points: p.points };
  }
  function geoPointText(p) { return '(' + p[0] + ', ' + p[1] + ')'; }
  function geoListText(list) { return list.map(geoPointText).join(' '); }
  function geoKey(p) { return p[0] + '|' + p[1]; }
  function geoPlural(n, one, many) { return n === 1 ? one : many; }
  function geoStep(v, lo, hi) { return v < lo ? lo : (v > hi ? hi : v); }
  /* Duplicates are removed and COUNTED. Both hull routines misbehave on them
     -- the chain can return one point twice and gift wrapping does -- so this
     is the first thing every hull mode does, and the count is shown. */
  function geoDedupe(points) {
    var seen = {}, out = [], dropped = 0;
    points.forEach(function (p) {
      var k = geoKey(p);
      if (seen[k]) { dropped += 1; return; }
      seen[k] = true; out.push(p);
    });
    return { points: out, dropped: dropped };
  }
  /* (b - a) . (c - a), in BigInt. Used to place a collinear point ALONG a
     line, which a determinant cannot do: it is zero for every point on it. */
  function geoDot(a, b, c) {
    return (BigInt(b[0]) - BigInt(a[0])) * (BigInt(c[0]) - BigInt(a[0]))
         + (BigInt(b[1]) - BigInt(a[1])) * (BigInt(c[1]) - BigInt(a[1]));
  }
  /* The SAME determinant as orient2, by cofactor expansion of
     [[ax, ay, 1], [bx, by, 1], [cx, cy, 1]]. Six products in a different
     arrangement, so a transposed term shows as a disagreement rather than as a
     plausible number that nothing contradicts. */
  function geoDet3(a, b, c) {
    var ax = BigInt(a[0]), ay = BigInt(a[1]), bx = BigInt(b[0]), by = BigInt(b[1]);
    var cx = BigInt(c[0]), cy = BigInt(c[1]);
    return ax * (by - cy) - ay * (bx - cx) + (bx * cy - cx * by);
  }
  function geoFloatSign(a, b, c) {
    var d = orient2Float(a, b, c);
    return d > 0 ? 1 : (d < 0 ? -1 : 0);
  }
  /* THE FAMILY THE COURSE OPENS ON. a = (0, 0), b = (2^k + 1, 2^k),
     c = (2^k, 2^k - 1). The exact determinant is (2^k+1)(2^k-1) - 2^k*2^k,
     which is -1 for every k: a right turn, always, at any magnitude. In
     doubles both products land on the same representable number once
     2k > 53, and the test reports 0. */
  function geoNeedle(k) {
    var P = Math.pow(2, k);
    return [[0, 0], [P + 1, P], [P, P - 1]];
  }
  function geoNeedleSweep(lo, hi) {
    var rows = [], k, disagree = 0, first = null;
    for (k = lo; k <= hi; k += 1) {
      var t = geoNeedle(k);
      if (!Number.isSafeInteger(t[1][0])) break;
      var ex = orientSign(t[0], t[1], t[2]), fl = geoFloatSign(t[0], t[1], t[2]);
      if (ex !== fl) { disagree += 1; if (first === null) first = k; }
      rows.push({ k: k, tri: t, exact: ex, float: fl, det: orient2(t[0], t[1], t[2]),
                  detFloat: orient2Float(t[0], t[1], t[2]), agree: ex === fl });
    }
    return { rows: rows, disagree: disagree, first: first, tested: rows.length };
  }
  /* p is OUTSIDE the convex hull of `others`, exactly and from the definition.
     There is a separating line through p with every other point weakly on one
     side, and every point that lies ON that line lies strictly beyond p along
     it -- which is the clause that distinguishes "p is a vertex" from "p sits
     inside an edge". Rotating a separating line about p until it touches a
     point of the set is why testing the lines through p and each other point
     is enough. */
  function geoOutside(p, others) {
    if (!others.length) return true;
    for (var j = 0; j < others.length; j += 1) {
      var t = others[j];
      if (t[0] === p[0] && t[1] === p[1]) return false;
      var pos = 0, neg = 0, on = [], r;
      for (r = 0; r < others.length; r += 1) {
        var s = orientSign(p, t, others[r]);
        if (s > 0) pos += 1; else if (s < 0) neg += 1; else on.push(others[r]);
      }
      if (pos && neg) continue;
      var ok = true;
      for (r = 0; r < on.length; r += 1) if (geoDot(p, t, on[r]) <= 0n) { ok = false; break; }
      if (ok) return true;
    }
    return false;
  }
  /* The VERTEX set: every point that is outside the hull of the others. */
  function geoVertexBrute(points) {
    var out = [], i;
    for (i = 0; i < points.length; i += 1) {
      var others = points.filter(function (_, j) { return j !== i; });
      if (geoOutside(points[i], others)) out.push(points[i]);
    }
    return out;
  }
  /* The BOUNDARY set, in the words the definition is usually given in: some
     line through the point has every other point on one side. An edge's
     interior satisfies that and is not a vertex, which is the whole of the
     difference between the two hull algorithms on degenerate input. */
  function geoBoundaryBrute(points) {
    var out = [], i, j, r;
    for (i = 0; i < points.length; i += 1) {
      var p = points[i], on = points.length < 2;
      for (j = 0; j < points.length && !on; j += 1) {
        if (j === i) continue;
        var pos = 0, neg = 0;
        for (r = 0; r < points.length; r += 1) {
          var s = orientSign(p, points[j], points[r]);
          if (s > 0) pos += 1; else if (s < 0) neg += 1;
        }
        if (!(pos && neg)) on = true;
      }
      if (on) out.push(p);
    }
    return out;
  }
  function geoSameSet(a, b) {
    return a.map(geoKey).sort().join(' ') === b.map(geoKey).sort().join(' ');
  }
  /* Andrew's monotone chain with the PREDICATE AS A PARAMETER, so the double
     arm is the exact arm with one function swapped and nothing else changed.
     It is pinned to algo_core's monotoneChain in scripts/mathcheck.js on every
     input with two or more distinct points; the one place they differ is a
     single point, where monotoneChain returns an empty hull. */
  function geoChainWith(points, sign) {
    var pts = lexSort(points), pops = 0, pushes = 0, trace = [];
    function half(list, name) {
      var stack = [];
      list.forEach(function (p) {
        while (stack.length >= 2
               && sign(stack[stack.length - 2], stack[stack.length - 1], p) <= 0) {
          var off = stack.pop();
          pops += 1;
          trace.push({ at: trace.length, side: name, action: 'pop', point: off,
                       depth: stack.length });
        }
        stack.push(p); pushes += 1;
        trace.push({ at: trace.length, side: name, action: 'push', point: p,
                     depth: stack.length });
      });
      return stack;
    }
    var lower = half(pts, 'lower'), upper = half(pts.slice().reverse(), 'upper');
    var hull = lower.slice(0, -1).concat(upper.slice(0, -1));
    if (!hull.length && pts.length) hull = [pts[0]];
    return { hull: hull, h: hull.length, lower: lower, upper: upper, trace: trace,
             pops: pops, pushes: pushes, bound: 2 * pts.length };
  }
  function geoExactHull(points) { return geoChainWith(points, orientSign); }
  function geoFloatHull(points) { return geoChainWith(points, geoFloatSign); }

  /* Two segments cross, by exact PARAMETERS rather than by four orientations.
     p1 + t(p2 - p1) = q1 + u(q2 - q1); t and u are ratios of determinants, and
     the test 0 <= t <= 1 is done by comparing numerator with denominator after
     forcing the denominator positive, so nothing is ever divided. */
  function geoSegOracle(p1, p2, q1, q2) {
    var rx = BigInt(p2[0]) - BigInt(p1[0]), ry = BigInt(p2[1]) - BigInt(p1[1]);
    var sx = BigInt(q2[0]) - BigInt(q1[0]), sy = BigInt(q2[1]) - BigInt(q1[1]);
    var wx = BigInt(q1[0]) - BigInt(p1[0]), wy = BigInt(q1[1]) - BigInt(p1[1]);
    var den = rx * sy - ry * sx;
    if (den !== 0n) {
      var tn = wx * sy - wy * sx, un = wx * ry - wy * rx;
      var d = den < 0n ? -den : den;
      var ts = den < 0n ? -tn : tn, us = den < 0n ? -un : un;
      return { intersect: ts >= 0n && ts <= d && us >= 0n && us <= d,
               parallel: false, collinear: false };
    }
    if (wx * ry - wy * rx !== 0n) return { intersect: false, parallel: true, collinear: false };
    var rr = rx * rx + ry * ry;
    if (rr === 0n) return { intersect: onSegment(q1, q2, p1), parallel: true, collinear: true };
    var t0 = wx * rx + wy * ry, t1 = t0 + (sx * rx + sy * ry);
    var lo = t0 < t1 ? t0 : t1, hi = t0 < t1 ? t1 : t0;
    return { intersect: hi >= 0n && lo <= rr, parallel: true, collinear: true };
  }
  function geoSweepBrute(segments) {
    var out = [], i, j;
    for (i = 0; i < segments.length; i += 1) for (j = i + 1; j < segments.length; j += 1) {
      if (geoSegOracle(segments[i][0], segments[i][1],
                       segments[j][0], segments[j][1]).intersect) out.push([i, j]);
    }
    return out;
  }
  function geoPairKeys(list) {
    return list.map(function (p) { return Math.min(p[0], p[1]) + '-' + Math.max(p[0], p[1]); })
               .sort().join(' ');
  }

  /* 2A by the trapezoid rule: sum (x_i - x_{i+1})(y_i + y_{i+1}). Algebraically
     the shoelace sum, arithmetically a different set of products, which is what
     makes it worth printing beside it. */
  function geoAreaTrapezoid(poly) {
    var s = 0n, i;
    for (i = 0; i < poly.length; i += 1) {
      var a = poly[i], b = poly[(i + 1) % poly.length];
      s += (BigInt(a[0]) - BigInt(b[0])) * (BigInt(a[1]) + BigInt(b[1]));
    }
    return s;
  }
  /* The WINDING NUMBER: how many times the boundary goes round the point.
     A different question from ray parity, with the same answer on a simple
     polygon -- which is why the mode checks simplicity before it says so. */
  function geoWinding(poly, q) {
    var w = 0, on = false, i;
    for (i = 0; i < poly.length; i += 1) {
      var a = poly[i], b = poly[(i + 1) % poly.length];
      if (onSegment(a, b, q)) on = true;
      if (a[1] <= q[1]) {
        if (b[1] > q[1] && orientSign(a, b, q) > 0) w += 1;
      } else if (b[1] <= q[1] && orientSign(a, b, q) < 0) w -= 1;
    }
    return { winding: w, inside: !on && w !== 0, onBoundary: on };
  }
  function geoSimple(poly) {
    var n = poly.length, bad = [], i, j;
    for (i = 0; i < n; i += 1) for (j = i + 1; j < n; j += 1) {
      if ((i + 1) % n === j || (j + 1) % n === i) continue;
      if (geoSegOracle(poly[i], poly[(i + 1) % n], poly[j], poly[(j + 1) % n]).intersect) {
        bad.push([i, j]);
      }
    }
    return { simple: bad.length === 0, crossings: bad };
  }
  function geoClosestBrute(points) {
    var best = null, pair = null, tests = 0, i, j;
    for (i = 0; i < points.length; i += 1) for (j = i + 1; j < points.length; j += 1) {
      tests += 1;
      var d = dist2(points[i], points[j]);
      if (best === null || d < best) { best = d; pair = [points[i], points[j]]; }
    }
    return { d2: best, pair: pair, tests: tests };
  }
  function geoRangeBrute(points, rect) {
    return points.filter(function (p) {
      return p[0] >= rect[0] && p[0] <= rect[2] && p[1] >= rect[1] && p[1] <= rect[3];
    });
  }

  /* ------------------------------------------------------------- the drawing

     One frame for every mode: the data's own bounding box mapped into the
     viewBox with one scale on both axes, so a right angle stays a right angle
     and the picture of a determinant is not a picture of a stretch. */
  function geoFrame(points, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 520 : opts.width;
    var h = opts.height === undefined ? 300 : opts.height;
    var pad = opts.pad === undefined ? 24 : opts.pad;
    var xs = points.map(function (p) { return p[0]; });
    var ys = points.map(function (p) { return p[1]; });
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    var y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    if (x1 === x0) { x0 -= 1; x1 += 1; }
    if (y1 === y0) { y0 -= 1; y1 += 1; }
    var s = Math.min((w - 2 * pad) / (x1 - x0), (h - 2 * pad) / (y1 - y0));
    var ox = pad + ((w - 2 * pad) - (x1 - x0) * s) / 2;
    var oy = pad + ((h - 2 * pad) - (y1 - y0) * s) / 2;
    return {
      w: w, h: h,
      X: function (x) { return ox + (x - x0) * s; },
      Y: function (y) { return h - oy - (y - y0) * s; }
    };
  }
  function geoLine(f, a, b, tone, width, dash) {
    return '<line x1="' + f.X(a[0]).toFixed(1) + '" y1="' + f.Y(a[1]).toFixed(1)
      + '" x2="' + f.X(b[0]).toFixed(1) + '" y2="' + f.Y(b[1]).toFixed(1)
      + '" stroke="var(--' + tone + ')" stroke-width="' + (width || 1.6) + '"'
      + (dash ? ' stroke-dasharray="' + dash + '"' : '') + ' />';
  }
  function geoPoly(f, pts, tone, fill) {
    if (pts.length < 2) return '';
    var d = pts.map(function (p) { return f.X(p[0]).toFixed(1) + ',' + f.Y(p[1]).toFixed(1); }).join(' ');
    return '<polygon points="' + d + '" fill="' + (fill ? 'var(--' + tone + ')' : 'none')
      + '" fill-opacity="' + (fill ? '0.14' : '0') + '" stroke="var(--' + tone
      + ')" stroke-width="2" stroke-linejoin="round" />';
  }
  function geoDot2(f, p, tone, radius, label) {
    var s = '<circle cx="' + f.X(p[0]).toFixed(1) + '" cy="' + f.Y(p[1]).toFixed(1)
      + '" r="' + (radius || 4.5) + '" fill="var(--' + tone + ')" stroke="var(--line-strong)" '
      + 'stroke-width="1" />';
    if (label) {
      s += '<text x="' + (f.X(p[0]) + 7).toFixed(1) + '" y="' + (f.Y(p[1]) - 6).toFixed(1)
        + '" font-size="9" font-weight="700" fill="var(--muted)">' + label + '</text>';
    }
    return s;
  }
  function geoRect(f, rect, tone) {
    var x = Math.min(f.X(rect[0]), f.X(rect[2])), y = Math.min(f.Y(rect[1]), f.Y(rect[3]));
    var w = Math.abs(f.X(rect[2]) - f.X(rect[0])), h = Math.abs(f.Y(rect[3]) - f.Y(rect[1]));
    return '<rect x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + w.toFixed(1)
      + '" height="' + h.toFixed(1) + '" fill="var(--' + tone + ')" fill-opacity="0.10" '
      + 'stroke="var(--' + tone + ')" stroke-width="1.6" stroke-dasharray="4 3" />';
  }
  function geoScene(points, layers, opts) {
    var f = geoFrame(points, opts);
    return { frame: f, svg: layers(f) };
  }
"""


# ---------------------------------------------------------------------------
# One core per mode, not one for the kit -- the largest single lever there is on
# page weight. `orient` never takes a logarithm and must not carry ALGO_JS to
# avoid one; `segments` draws no tree and must not carry the tree renderer.
# ---------------------------------------------------------------------------

_BASE_JS = COUNT_JS + GEOM_JS + GEOKIT_JS
_RATIO_JS = COUNT_JS + RATIONAL_JS + GEOM_JS + GEOKIT_JS
_HULL_JS = COUNT_JS + GEOM_JS + ALGO_JS + GEOKIT_JS
_TREE_JS = COUNT_JS + RATIONAL_JS + GEOM_JS + TREEDRAW_JS + GEOKIT_JS


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on this path uses. Drawings take
# only the two viewBox widths theme.py gives a horizontal-scroll minimum -- 520
# and 660 -- because any other width shrinks the labels to illegibility on a
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


def _text(cid, label, placeholder):
    """A text box that starts EMPTY and is filled by the script at startup.

    graphkit.py met this first and the reason is the same here: a default
    carried in the markup has to survive scripts/labcheck.js's tag scan as well
    as a browser's entity decoding, and the two disagree. The value goes in from
    the script before the first redraw; the placeholder says what the box is for.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(placeholder))
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
        "geometry: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form. This Subject's hazard is that a
# count on one input is not a bound, and geometry's version of it is sharper: a
# predicate that was right on the points you tried is not a predicate. Spelled
# once so no mode can quietly drop it, and each mode says it in its own nouns.
_ONE_INPUT = (
    "  /* Every number below came from running the algorithm on the points on\n"
    "     screen. That is one input. Where a page states something about all\n"
    "     inputs it either checks the definition exhaustively on this one and\n"
    "     says so, or it names the proof the lesson gives -- and where the\n"
    "     measured count and the proved bound differ, both are printed. */\n"
)


# ---------------------------------------------------------------------------
# orient -- the sign the whole subject rests on, exactly and in doubles
# ---------------------------------------------------------------------------

_OR_PRESETS = [
    {
        "id": "turn",
        "label": "an ordinary left turn, small coordinates",
        "spec": "0, 0; 4, 0; 2, 3",
        "note": "nothing near the edge of anything: the double and the exact test agree",
    },
    {
        "id": "collinear",
        "label": "three points genuinely on one line",
        "spec": "0, 0; 3, 3; 7, 7",
        "note": "the determinant is 0 and both tests say so, which is the case that is easy",
    },
    {
        "id": "needle",
        "label": "a right turn the double test calls collinear",
        "spec": "0, 0; 134217729, 134217728; 134217728, 134217727",
        "note": "2^27 + 1 and 2^27: the exact determinant is −1 and the double reads 0",
    },
    {
        "id": "thin",
        "label": "the same shape one power of two lower down",
        "spec": "0, 0; 67108865, 67108864; 67108864, 67108863",
        "note": "2^26: the last magnitude at which the double still gets the sign right",
    },
    {
        "id": "area1",
        "label": "a triangle of area one half, at readable size",
        "spec": "0, 0; 7, 3; 5, 2",
        "note": "the smallest nonzero doubled area there is, and both tests find it",
    },
]


def _orient(cfg):
    chosen = _chosen(_OR_PRESETS, cfg)
    markup = (
        _toolbar(
            "The sign of one determinant",
            "computed three ways, two of them exact",
            [("cyan", "the three points, in the order typed"),
             ("purple", "the line through the first two"),
             ("red", "a magnitude at which the double test is wrong")],
        )
        + _stage(_svg("orPlot", "0 0 520 260",
                      "The three points and the line through the first two, so the "
                      "third point's side is visible."))
        + _table("orWays")
        + _table("orSweep")
        + _banner("orStatus")
    )
    controls = (
        _select("orPreset", "Worked example", _options(_OR_PRESETS), chosen["id"])
        + _text("orSpec", "Three points, as x, y", "0, 0; 4, 0; 2, 3")
        + _range("orK", "Highlight the swept family at 2 to the", 20, 48, 27)
        + _kpis([("Exact determinant", "orExact"), ("Sign, exactly", "orSign"),
                 ("Double determinant", "orFloat"), ("Sign, in doubles", "orFSign"),
                 ("Swept magnitudes", "orTested"),
                 ("Magnitudes the double gets wrong", "orWrong")])
        + _hint(
            "orHint",
            "Three points, each <span class=\"tt\">x, y</span>, separated by semicolons. "
            "Coordinates are whole numbers: a decimal point is refused rather than rounded, "
            "because a coordinate that is not exact makes every determinant below a statement "
            "about some other three points. The lower table sweeps one family of triples whose "
            "exact determinant is −1 at every magnitude, and reports the magnitude at which the "
            "double test stops agreeing.",
        )
    )
    script = _BASE_JS + _ONE_INPUT + _presets_js("ORP", _OR_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('orPreset'), specIn = document.getElementById('orSpec');
  var kIn = document.getElementById('orK'), kOut = document.getElementById('orKOut');
  var plot = document.getElementById('orPlot'), ways = document.getElementById('orWays');
  var sweep = document.getElementById('orSweep'), status = document.getElementById('orStatus');
  var KPIS = ['orExact', 'orSign', 'orFloat', 'orFSign', 'orTested', 'orWrong'];
  var SWEEP_LO = 20, SWEEP_HI = 48;

  function blank(why) {
    plot.innerHTML = ''; ways.innerHTML = ''; sweep.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Three points, each '
      + '<span class="tt">x, y</span>: <span class="tt">0, 0; 4, 0; 2, 3</span>.';
  }
  function sideWord(s) {
    return s > 0 ? 'left turn' : (s < 0 ? 'right turn' : 'collinear');
  }

  function redraw() {
    var parsed = geoParse(specIn.value, 3);
    if (parsed.bad) { blank(parsed.bad); return; }
    if (parsed.points.length !== 3) { blank('this mode takes exactly three points'); return; }
    var a = parsed.points[0], b = parsed.points[1], c = parsed.points[2];
    var k = geoStep(parseInt(kIn.value, 10), SWEEP_LO, SWEEP_HI);
    kOut.textContent = String(k);

    var det = orient2(a, b, c), det3 = geoDet3(a, b, c);
    var sgn = orientSign(a, b, c);
    var fdet = orient2Float(a, b, c), fsgn = geoFloatSign(a, b, c);

    /* The line through a and b is drawn past both ends so the third point's
       side is a side rather than a gap at the end of a segment. */
    var ex = b[0] - a[0], ey = b[1] - a[1];
    var far1 = [a[0] - ex, a[1] - ey], far2 = [b[0] + ex, b[1] + ey];
    var f = geoFrame([a, b, c, far1, far2], { width: 520, height: 260 });
    plot.innerHTML = geoLine(f, far1, far2, 'purple', 1.4, '5 4')
      + geoLine(f, a, b, 'purple', 2)
      + geoDot2(f, a, 'cyan', 5, 'a ' + geoPointText(a))
      + geoDot2(f, b, 'cyan', 5, 'b ' + geoPointText(b))
      + geoDot2(f, c, sgn === 0 ? 'amber' : (sgn > 0 ? 'green' : 'red'), 5,
                'c ' + geoPointText(c));

    var agree = sgn === fsgn;
    ways.innerHTML = '<caption>The same determinant three ways. Two are exact and must agree '
      + 'exactly; the third is the one every textbook writes and the reason this course does '
      + 'not</caption><thead><tr><th>route</th><th>value</th><th>sign</th><th>what it says</th>'
      + '</tr></thead><tbody>'
      + '<tr><th class="rowhead">2×2 determinant, BigInt</th><td class="tt">' + det
      + '</td><td>' + sgn + '</td><td>' + sideWord(sgn) + '</td></tr>'
      + '<tr><th class="rowhead">3×3 cofactor expansion, BigInt</th><td class="tt">' + det3
      + '</td><td>' + (det3 > 0n ? 1 : (det3 < 0n ? -1 : 0)) + '</td><td>'
      + (det === det3 ? 'the same six products in a different order, and the same number'
                      : '<span class="tone-red">a different number: one of the two is wrong</span>')
      + '</td></tr>'
      + '<tr' + (agree ? '' : ' class="tone-red"') + '><th class="rowhead">2×2 determinant, doubles'
      + '</th><td class="tt">' + fdet + '</td><td>' + fsgn + '</td><td>'
      + (agree ? sideWord(fsgn) + ', which is right here'
               : '<strong>' + sideWord(fsgn) + ', and that is wrong</strong>')
      + '</td></tr></tbody>';

    var sw = geoNeedleSweep(SWEEP_LO, SWEEP_HI);
    var rows = '';
    sw.rows.forEach(function (r) {
      rows += '<tr' + (r.k === k ? ' class="tone-cyan"' : (r.agree ? '' : ' class="tone-red"'))
        + '><th class="rowhead">2^' + r.k + '</th><td class="tt">' + r.tri[1][0] + ', '
        + r.tri[1][1] + '</td><td class="tt">' + r.det + '</td><td class="tt">' + r.detFloat
        + '</td><td>' + r.exact + '</td><td>' + r.float + '</td><td>'
        + (r.agree ? '<span class="tone-green">agree</span>'
                   : '<span class="tone-red">the double says collinear</span>') + '</td></tr>';
    });
    sweep.innerHTML = '<caption>One family of triples: a = (0, 0), b = (2^k + 1, 2^k), '
      + 'c = (2^k, 2^k − 1). The exact determinant is −1 at every magnitude, so every row '
      + 'is the same right turn</caption><thead><tr><th>magnitude</th><th>b</th>'
      + '<th>exact</th><th>double</th><th>sign</th><th>sign</th><th>verdict</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('orExact').textContent = String(det);
    document.getElementById('orSign').textContent = sgn + ' — ' + sideWord(sgn);
    document.getElementById('orFloat').textContent = String(fdet);
    document.getElementById('orFSign').textContent = fsgn + ' — ' + sideWord(fsgn);
    document.getElementById('orTested').textContent = sw.tested;
    document.getElementById('orWrong').textContent = sw.disagree
      + (sw.first === null ? ' — none' : ' — from 2^' + sw.first + ' up');

    status.innerHTML = '<strong>' + det + '</strong> is the doubled signed area of the triangle '
      + 'a b c, and its sign is <span class="tone-' + (sgn > 0 ? 'green' : (sgn < 0 ? 'red' : 'amber'))
      + '">' + sideWord(sgn) + '</span>. '
      + (agree
          ? 'The double arithmetic agrees here. '
          : '<span class="tone-red">The double arithmetic does not: it reports ' + fdet
            + ', so it calls these three points ' + sideWord(fsgn) + '.</span> ')
      + 'Across the ' + sw.tested + ' magnitudes swept below, the double test got '
      + '<span class="tone-' + (sw.disagree ? 'red' : 'green') + '">' + sw.disagree
      + '</span> of them wrong'
      + (sw.first === null ? '. ' : ', every one of them from 2^' + sw.first + ' upward. ')
      + 'Every disagreement is in the same direction: the double says collinear where the exact '
      + 'test says a turn, and it never reports the opposite turn. That is not luck. The two '
      + 'coordinate differences are integers below 2^53 and therefore exact, rounding to nearest '
      + 'is monotone, so the rounded product of the larger pair can never fall below the rounded '
      + 'product of the smaller one — it can only tie. The failure mode is a vertex that '
      + 'disappears, and the hull page is where it disappears.';
  }

  function apply() {
    var p = ORP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = ORP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  kIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Which side of the line, and what the answer costs in doubles",
        subtitle="One determinant, computed exactly twice and approximately once",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type three points and read the sign"),
        panel_intro=cfg.get(
            "panel_intro",
            "The determinant is computed in your browser in BigInt, again by a different "
            "expansion, and a third time in ordinary double arithmetic. The first two must "
            "agree. The third is the one that decides whether the rest of this course works.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# hull -- two algorithms, two predicates, and the definition as the referee
# ---------------------------------------------------------------------------

_HU_PRESETS = [
    {
        "id": "general",
        "label": "nine points in general position",
        "spec": "0, 0; 6, 0; 6, 6; 0, 6; 3, 3; 2, 1; 4, 5; 1, 4; 5, 2",
        "note": "no three collinear, so both algorithms and both predicates agree",
    },
    {
        "id": "edges",
        "label": "a square with a point in the middle of each side",
        "spec": "0, 0; 2, 0; 4, 0; 4, 2; 4, 4; 2, 4; 0, 4; 0, 2; 2, 2",
        "note": "four vertices, eight boundary points, and gift wrapping returns six",
    },
    {
        "id": "segment",
        "label": "five points on one line: the hull is a segment",
        "spec": "0, 0; 1, 1; 2, 2; 3, 3; 4, 4",
        "note": "the chain returns the two ends and gift wrapping returns all five",
    },
    {
        "id": "duplicate",
        "label": "the same point typed more than once",
        "spec": "0, 0; 0, 0; 4, 0; 0, 4; 2, 2; 4, 0",
        "note": "two duplicates removed before anything else happens, and counted",
    },
    {
        "id": "needle",
        "label": "a triangle the double predicate flattens",
        "spec": "0, 0; 134217729, 134217728; 134217728, 134217727",
        "note": "three vertices exactly, two in doubles: switch the predicate and watch one go",
    },
    {
        "id": "single",
        "label": "one point, typed twice",
        "spec": "3, 3; 3, 3",
        "note": "the hull of one point is that point, which is the case the shipped chain drops",
    },
]


def _hull(cfg):
    chosen = _chosen(_HU_PRESETS, cfg)
    markup = (
        _toolbar(
            "The convex hull, and the definition that referees it",
            "two algorithms, two predicates, one brute-force answer",
            [("cyan", "a hull vertex, by the definition"),
             ("amber", "on the boundary but not a vertex"),
             ("muted", "strictly inside")],
        )
        + _stage(_svg("huPlot", "0 0 520 300",
                      "The points, with the hull drawn as a closed polygon and each point "
                      "coloured by whether the definition makes it a vertex."))
        + _table("huPoints")
        + _table("huTrace")
        + _banner("huStatus")
    )
    controls = (
        _select("huPreset", "Worked example", _options(_HU_PRESETS), chosen["id"])
        + _text("huSpec", "Points, as x, y", "0, 0; 6, 0; 6, 6; 0, 6; 3, 3")
        + _select("huAlgo", "Draw the hull found by",
                  [("chain", "Andrew's monotone chain"),
                   ("jarvis", "gift wrapping, one vertex at a time")], "chain")
        + _select("huPred", "Decide each turn with",
                  [("exact", "the exact determinant, in BigInt"),
                   ("double", "the same determinant in doubles")], "exact")
        + _kpis([("Points typed", "huN"), ("Duplicates removed", "huDup"),
                 ("Hull vertices, exactly", "huH"), ("Hull vertices, in doubles", "huFH"),
                 ("Gift wrapping returns", "huJH"), ("On the boundary, by definition", "huB"),
                 ("Pushes and pops", "huStack"), ("Work: n·h against n log2 n", "huWork")])
        + _hint(
            "huHint",
            "Points are <span class=\"tt\">x, y</span> separated by semicolons. Duplicates are "
            "removed first and counted, because both algorithms return a repeated point when "
            "handed one. The colour of each point is decided by the definition and not by either "
            "algorithm: a point is a vertex when some line through it has every other point "
            "strictly beyond it, and on the boundary when some line through it has every other "
            "point on one side.",
        )
    )
    script = _HULL_JS + _ONE_INPUT + _presets_js("HUP", _HU_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('huPreset'), specIn = document.getElementById('huSpec');
  var algoIn = document.getElementById('huAlgo'), predIn = document.getElementById('huPred');
  var plot = document.getElementById('huPlot'), table = document.getElementById('huPoints');
  var traceT = document.getElementById('huTrace'), status = document.getElementById('huStatus');
  var KPIS = ['huN', 'huDup', 'huH', 'huFH', 'huJH', 'huB', 'huStack', 'huWork'];

  function blank(why) {
    plot.innerHTML = ''; table.innerHTML = ''; traceT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Points are '
      + '<span class="tt">x, y</span> separated by semicolons: '
      + '<span class="tt">0, 0; 4, 0; 2, 3</span>.';
  }

  function redraw() {
    var parsed = geoParse(specIn.value, 24);
    if (parsed.bad) { blank(parsed.bad); return; }
    var typed = parsed.points, clean = geoDedupe(typed), P = clean.points;

    var exact = geoExactHull(P), dbl = geoFloatHull(P);
    var wrap = P.length >= 2 ? jarvis(P) : null;
    var verts = geoVertexBrute(P), bound = geoBoundaryBrute(P);
    var shown = predIn.value === 'double' ? dbl : exact;
    var drawn = algoIn.value === 'jarvis' && wrap ? wrap.result.hull : shown.hull;

    var vkeys = {}, bkeys = {};
    verts.forEach(function (p) { vkeys[geoKey(p)] = true; });
    bound.forEach(function (p) { bkeys[geoKey(p)] = true; });
    var f = geoFrame(P, { width: 520, height: 300 });
    var svg = geoPoly(f, drawn, algoIn.value === 'jarvis' ? 'amber' : 'cyan', true);
    P.forEach(function (p) {
      var tone = vkeys[geoKey(p)] ? 'cyan' : (bkeys[geoKey(p)] ? 'amber' : 'muted');
      svg += geoDot2(f, p, tone, vkeys[geoKey(p)] ? 5 : 4, null);
    });
    plot.innerHTML = svg;

    var rows = '';
    P.forEach(function (p, i) {
      var isV = !!vkeys[geoKey(p)], isB = !!bkeys[geoKey(p)];
      var inChain = exact.hull.some(function (q) { return geoKey(q) === geoKey(p); });
      var inDbl = dbl.hull.some(function (q) { return geoKey(q) === geoKey(p); });
      var inWrap = wrap && wrap.result.hull.some(function (q) { return geoKey(q) === geoKey(p); });
      rows += '<tr' + (isV === inChain ? '' : ' class="tone-red"') + '><th class="rowhead">'
        + geoPointText(p) + '</th><td>' + (isV ? '<span class="tone-cyan">vertex</span>'
            : (isB ? '<span class="tone-amber">on an edge</span>'
                   : '<span class="tone-muted">inside</span>'))
        + '</td><td>' + (inChain ? 'yes' : 'no') + '</td><td>'
        + (inDbl ? 'yes' : '<span class="' + (isV ? 'tone-red' : '') + '">no</span>')
        + '</td><td>' + (wrap ? (inWrap ? 'yes' : 'no') : '—') + '</td></tr>';
    });
    table.innerHTML = '<caption>One row per distinct point: what the definition says, and which '
      + 'of the three runs put it on the hull</caption><thead><tr><th>point</th>'
      + '<th>by definition</th><th>chain, exact</th><th>chain, doubles</th>'
      + '<th>gift wrapping</th></tr></thead><tbody>' + rows + '</tbody>';

    var trows = '';
    shown.trace.slice(0, 26).forEach(function (s) {
      trows += '<tr><th class="rowhead">' + (s.at + 1) + '</th><td>' + s.side + '</td><td>'
        + (s.action === 'pop' ? '<span class="tone-red">pop</span>'
                              : '<span class="tone-green">push</span>')
        + '</td><td class="tt">' + geoPointText(s.point) + '</td><td>' + s.depth + '</td></tr>';
    });
    traceT.innerHTML = '<caption>The stack, step by step. A point is pushed once and popped at '
      + 'most once. Each chain PUSHES every point once, so pushes alone is 2n and the two '
      + 'chains together cost at most 4n stack operations'
      + (shown.trace.length > 26 ? ' (first 26 of ' + shown.trace.length + ')' : '')
      + '</caption><thead><tr><th>step</th><th>chain</th><th>action</th><th>point</th>'
      + '<th>stack depth</th></tr></thead><tbody>' + trows + '</tbody>';

    document.getElementById('huN').textContent = typed.length + ' typed, ' + P.length + ' distinct';
    document.getElementById('huDup').textContent = clean.dropped;
    document.getElementById('huH').textContent = exact.h;
    document.getElementById('huFH').textContent = dbl.h
      + (dbl.h === exact.h ? '' : ' — a vertex short');
    document.getElementById('huJH').textContent = wrap ? wrap.result.h : '—';
    document.getElementById('huB').textContent = bound.length;
    /* pushes ALONE is 2n -- each of the two chains pushes every point once --
       so the ceiling on pushes PLUS pops is 4n. This printed "against 2n" and
       so contradicted itself on every hull page: 18 + 12 = 30 against 2n = 18. */
    document.getElementById('huStack').textContent = shown.pushes + ' + ' + shown.pops + ' = '
      + (shown.pushes + shown.pops) + ' against 4n = ' + (2 * shown.bound);
    document.getElementById('huWork').textContent = wrap
      ? (wrap.result.work + ' against ' + wrap.result.nlogn) : '—';

    var chainRight = geoSameSet(exact.hull, verts);
    var wrapInBound = !wrap || wrap.result.hull.every(function (p) { return !!bkeys[geoKey(p)]; });
    status.innerHTML = '<strong>' + P.length + ' distinct point'
      + geoPlural(P.length, '', 's') + ', ' + exact.h + ' hull vert'
      + geoPlural(exact.h, 'ex', 'ices') + '.</strong> '
      + (clean.dropped
          ? '<span class="tone-amber">' + clean.dropped + ' duplicate'
            + geoPlural(clean.dropped, ' was', 's were') + ' removed before anything ran.</span> '
          : '')
      + (chainRight
          ? 'The chain\u2019s answer is exactly the set the definition picks out, checked point by '
            + 'point above. '
          : '<span class="tone-red">The chain and the definition disagree, which cannot happen: '
            + 'one of the two is wrong.</span> ')
      + (bound.length > exact.h
          ? 'There are <span class="tone-amber">' + (bound.length - exact.h) + '</span> further '
            + 'point' + geoPlural(bound.length - exact.h, '', 's') + ' ON the boundary and not a '
            + 'vertex, so the two algorithms answer different questions here: the chain returns '
            + exact.h + ' and gift wrapping returns ' + (wrap ? wrap.result.h : '—')
            + '. Neither is a bug in arithmetic; they are different conventions about a collinear '
            + 'point, and only one of them is a convex polygon\u2019s vertex list. '
          : 'No point of this set lies BETWEEN two hull vertices, so the boundary and the vertex '
            + 'set are the same ' + exact.h + ' points and the two conventions cannot be told '
            + 'apart here. That is weaker than no three being collinear -- which this sentence '
            + 'used to claim, and which is false on the opening preset, where four collinear '
            + 'triples all pass through the interior point. ')
      + (dbl.h === exact.h
          ? 'Both predicates return the same hull at this magnitude. '
          : '<span class="tone-red">The double predicate returns ' + dbl.h + ' vertices against '
            + exact.h + '.</span> A determinant that rounded to zero read as a straight line, the '
            + 'chain popped a real corner off the stack, and nothing downstream can recover it: '
            + 'the hull is simply missing a vertex. ')
      + (wrapInBound ? '' : '<span class="tone-red">Gift wrapping returned a point the definition '
            + 'does not place on the boundary at all.</span>');
  }

  function apply() {
    var p = HUP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = HUP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  algoIn.addEventListener('change', redraw);
  predIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The convex hull, and the three answers a collinear point produces",
        subtitle="Two algorithms and two predicates, refereed by the definition itself",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type points and watch the hull answer change"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every point is classified from the definition by brute force before either "
            "algorithm runs, so the table above is a check and not a restatement. Switch the "
            "predicate to doubles on the last worked example and count the vertices again.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# segments -- four signs, a box filter, and the cases that are usually wrong
# ---------------------------------------------------------------------------

_SG_PRESETS = [
    {
        "id": "proper",
        "label": "an ordinary crossing, interiors only",
        "spec": "0, 0; 6, 6; 0, 6; 6, 0",
        "note": "all four signs nonzero and opposite in pairs: the textbook case",
    },
    {
        "id": "touch",
        "label": "one segment ends on the other",
        "spec": "0, 0; 6, 0; 3, 0; 3, 5",
        "note": "a T-junction: one sign is zero, so the proper test says no and they do meet",
    },
    {
        "id": "overlap",
        "label": "collinear and overlapping",
        "spec": "0, 0; 6, 0; 4, 0; 10, 0",
        "note": "all four signs are zero, and an implementation that stops there says no",
    },
    {
        "id": "apart",
        "label": "collinear, boxes touching, no overlap",
        "spec": "0, 0; 4, 0; 6, 0; 10, 0",
        "note": "all four signs zero again, and this time they really do miss",
    },
    {
        "id": "shared",
        "label": "a shared endpoint and nothing else",
        "spec": "0, 0; 4, 0; 4, 0; 4, 5",
        "note": "the boundary case between meeting and not, and both tests must say yes",
    },
    {
        "id": "parallel",
        "label": "parallel, never meeting",
        "spec": "0, 0; 6, 0; 0, 2; 6, 2",
        "note": "the determinant of the direction pair is zero and they are not collinear",
    },
    {
        "id": "point",
        "label": "a segment that is a single point",
        "spec": "3, 2; 3, 2; 0, 0; 6, 4",
        "note": "a degenerate segment on the other one: both routes must still answer",
    },
]


def _segments(cfg):
    chosen = _chosen(_SG_PRESETS, cfg)
    markup = (
        _toolbar(
            "Do these two segments meet",
            "four orientation signs against an exact parametric solve",
            [("cyan", "the first segment"), ("purple", "the second"),
             ("green", "they meet"), ("red", "they do not")],
        )
        + _stage(_svg("sgPlot", "0 0 520 260",
                      "The two segments, drawn with their bounding boxes."))
        + _table("sgSigns")
        + _banner("sgStatus")
    )
    controls = (
        _select("sgPreset", "Worked example", _options(_SG_PRESETS), chosen["id"])
        + _text("sgSpec", "Four points: p1, p2, q1, q2", "0, 0; 6, 6; 0, 6; 6, 0")
        + _kpis([("Proper crossing", "sgProper"), ("Touching", "sgTouch"),
                 ("Bounding boxes overlap", "sgBox"),
                 ("Verdict from the four signs", "sgVerdict"),
                 ("Verdict from the parameters", "sgOracle"),
                 ("The two routes agree", "sgAgree")])
        + _hint(
            "sgHint",
            "Four points, each <span class=\"tt\">x, y</span>: the first two are one segment and "
            "the last two are the other. The four signs decide a PROPER crossing, where each "
            "segment has the other's endpoints strictly on opposite sides. Every remaining case "
            "is a zero sign, and a zero sign means collinear, which is where the second test "
            "has to take over. The parametric route below never looks at a sign at all.",
        )
    )
    script = _BASE_JS + _ONE_INPUT + _presets_js("SGP", _SG_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('sgPreset'), specIn = document.getElementById('sgSpec');
  var plot = document.getElementById('sgPlot'), signs = document.getElementById('sgSigns');
  var status = document.getElementById('sgStatus');
  var KPIS = ['sgProper', 'sgTouch', 'sgBox', 'sgVerdict', 'sgOracle', 'sgAgree'];

  function blank(why) {
    plot.innerHTML = ''; signs.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Four points: '
      + '<span class="tt">0, 0; 6, 6; 0, 6; 6, 0</span>.';
  }
  function yesno(v) { return v ? '<span class="tone-green">yes</span>'
                               : '<span class="tone-muted">no</span>'; }

  function redraw() {
    var parsed = geoParse(specIn.value, 4);
    if (parsed.bad) { blank(parsed.bad); return; }
    if (parsed.points.length !== 4) { blank('this mode takes exactly four points'); return; }
    var p1 = parsed.points[0], p2 = parsed.points[1];
    var q1 = parsed.points[2], q2 = parsed.points[3];

    var s = straddle(p1, p2, q1, q2);
    var oracle = geoSegOracle(p1, p2, q1, q2);
    var agree = s.intersect === oracle.intersect;

    var f = geoFrame([p1, p2, q1, q2], { width: 520, height: 260 });
    var tone = s.intersect ? 'green' : 'red';
    plot.innerHTML = geoRect(f, [Math.min(p1[0], p2[0]), Math.min(p1[1], p2[1]),
                                 Math.max(p1[0], p2[0]), Math.max(p1[1], p2[1])], 'muted')
      + geoRect(f, [Math.min(q1[0], q2[0]), Math.min(q1[1], q2[1]),
                    Math.max(q1[0], q2[0]), Math.max(q1[1], q2[1])], 'muted')
      + geoLine(f, p1, p2, 'cyan', 3) + geoLine(f, q1, q2, 'purple', 3)
      + geoDot2(f, p1, 'cyan', 4.5, 'p1') + geoDot2(f, p2, 'cyan', 4.5, 'p2')
      + geoDot2(f, q1, 'purple', 4.5, 'q1') + geoDot2(f, q2, 'purple', 4.5, 'q2')
      + '<text x="12" y="18" font-size="10" font-weight="800" fill="var(--' + tone + ')">'
      + (s.intersect ? 'they meet' : 'they do not meet') + '</text>';

    var NAMES = ['orient(q1, q2, p1)', 'orient(q1, q2, p2)',
                 'orient(p1, p2, q1)', 'orient(p1, p2, q2)'];
    var DETS = [orient2(q1, q2, p1), orient2(q1, q2, p2),
                orient2(p1, p2, q1), orient2(p1, p2, q2)];
    var rows = '';
    s.d.forEach(function (d, i) {
      rows += '<tr' + (d === 0 ? ' class="tone-amber"' : '') + '><th class="rowhead tt">'
        + NAMES[i] + '</th><td class="tt">' + DETS[i] + '</td><td>' + d + '</td><td>'
        + (d === 0 ? 'collinear — the sign alone decides nothing here'
                   : (d > 0 ? 'left of the line' : 'right of the line')) + '</td></tr>';
    });
    signs.innerHTML = '<caption>The four orientations. A proper crossing needs the first pair '
      + 'to have opposite signs and the second pair too; a zero anywhere means the case has to '
      + 'be finished on the segment rather than on the line</caption><thead><tr>'
      + '<th>determinant</th><th>value</th><th>sign</th><th>what it says</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    document.getElementById('sgProper').textContent = s.proper ? 'yes' : 'no';
    document.getElementById('sgTouch').textContent = s.touching ? 'yes' : 'no';
    document.getElementById('sgBox').textContent = s.boxes ? 'yes' : 'no';
    document.getElementById('sgVerdict').textContent = s.intersect ? 'they meet' : 'they miss';
    document.getElementById('sgOracle').textContent = oracle.intersect ? 'they meet' : 'they miss';
    document.getElementById('sgAgree').textContent = agree ? 'yes' : 'NO';

    var zeros = s.d.filter(function (d) { return d === 0; }).length;
    status.innerHTML = '<strong>' + (s.intersect ? 'They meet' : 'They do not meet') + '.</strong> '
      + 'Proper crossing ' + yesno(s.proper) + ', touching ' + yesno(s.touching)
      + ', bounding boxes overlap ' + yesno(s.boxes) + '. '
      + (zeros
          ? '<span class="tone-amber">' + zeros + ' of the four signs '
            + geoPlural(zeros, 'is', 'are') + ' zero</span>, so the proper test alone cannot '
            + 'settle this input and the collinear cases have to be finished on the SEGMENTS '
            + 'rather than on the lines. '
            + (s.proper === s.intersect
                ? 'Here it happens to reach the right verdict anyway, which is exactly why a '
                  + 'test that stops at `proper` survives so long. '
                : 'An implementation that returned `proper` and stopped would answer '
                  + '<span class="tone-red">' + (s.proper ? 'yes' : 'no') + '</span> where the '
                  + 'right answer is <span class="tone-green">' + (s.intersect ? 'yes' : 'no')
                  + '</span>. ')
          : 'No sign is zero, so the four-orientation test settles it on its own and the '
            + 'collinear machinery below is never reached. ')
      + (s.boxes && !s.intersect
          ? 'The boxes do overlap and the segments still miss, which is why the box test is a '
            + 'filter and never an answer. '
          : '')
      + (agree
          ? 'Solving p1 + t(p2 − p1) = q1 + u(q2 − q1) exactly — t and u as ratios of '
            + 'determinants, compared against 1 without ever dividing — reaches the same verdict '
            + 'by a route with no orientation sign in it.'
          : '<span class="tone-red">The parametric solve disagrees. Two exact routes to one '
            + 'question cannot both be right, and this page is not entitled to say which.</span>');
  }

  function apply() {
    var p = SGP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = SGP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Do two segments meet, including every case where one sign is zero",
        subtitle="Four orientations against an exact solve for the two parameters",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type two segments and read both verdicts"),
        panel_intro=cfg.get(
            "panel_intro",
            "The four-sign test and a parametric solve answer the same question by different "
            "arithmetic. They agree on every preset here. The presets are chosen so that four "
            "of the seven are cases the four-sign test alone gets wrong.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# sweep -- the tests a sweep does not make
# ---------------------------------------------------------------------------

_SW_PRESETS = [
    {
        "id": "spread",
        "label": "six segments spread along the line",
        "spec": "0, 0; 3, 3; 1, 4; 4, 1; 6, 0; 9, 3; 7, 4; 10, 1; 12, 0; 15, 3; 13, 4; 16, 1",
        "note": "two crossings, and the sweep never compares the first pair with the last",
    },
    {
        "id": "bundle",
        "label": "everything crossing everything",
        "spec": "0, 0; 8, 8; 0, 8; 8, 0; 0, 4; 8, 4; 4, 0; 4, 8",
        "note": "the worst case: the status list holds all four at once and the sweep saves nothing",
    },
    {
        "id": "chain",
        "label": "a staircase, each meeting only the next",
        "spec": "0, 0; 3, 1; 3, 1; 6, 2; 6, 2; 9, 3; 9, 3; 12, 4",
        "note": "shared endpoints count as crossings, which is a decision and the page states it",
    },
    {
        "id": "none",
        "label": "six segments and no crossing at all",
        "spec": "0, 0; 2, 1; 3, 0; 5, 1; 6, 0; 8, 1; 0, 4; 2, 5; 3, 4; 5, 5; 6, 4; 8, 5",
        "note": "the answer is empty and the work still is not, which is the honest figure",
    },
]


def _sweep(cfg):
    chosen = _chosen(_SW_PRESETS, cfg)
    markup = (
        _toolbar(
            "The sweep line, and the pairs it never tests",
            "tests actually made against every pair there is",
            [("cyan", "on the status list right now"), ("muted", "not yet, or already gone"),
             ("red", "a crossing pair")],
        )
        + _stage(_svg("swPlot", "0 0 660 280",
                      "The segments with the sweep line at the chosen event, the active "
                      "segments drawn heavy."))
        + _table("swEvents")
        + _banner("swStatus")
    )
    controls = (
        _select("swPreset", "Worked example", _options(_SW_PRESETS), chosen["id"])
        + _text("swSpec", "Segments, two points each", "0, 0; 4, 4; 0, 4; 4, 0")
        + _range("swAt", "Stop the sweep after event", 1, 40, 1)
        + _kpis([("Segments", "swN"), ("Events", "swE"),
                 ("Pair tests the sweep made", "swTests"),
                 ("Pairs there are", "swAll"), ("Crossings found", "swFound"),
                 ("Crossings by testing every pair", "swOracle")])
        + _hint(
            "swHint",
            "Two points make a segment, so the count must be even. The sweep sorts the endpoints "
            "by x and keeps a status list of the segments the line currently crosses; a new "
            "segment is tested only against that list. The saving is real and it is not a bound: "
            "on the second worked example the list holds everything and the sweep does every "
            "test the brute force does.",
        )
    )
    script = _BASE_JS + _ONE_INPUT + _presets_js("SWP", _SW_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('swPreset'), specIn = document.getElementById('swSpec');
  var atIn = document.getElementById('swAt'), atOut = document.getElementById('swAtOut');
  var plot = document.getElementById('swPlot'), table = document.getElementById('swEvents');
  var status = document.getElementById('swStatus');
  var KPIS = ['swN', 'swE', 'swTests', 'swAll', 'swFound', 'swOracle'];

  function blank(why) {
    plot.innerHTML = ''; table.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Two points make a segment: '
      + '<span class="tt">0, 0; 4, 4; 0, 4; 4, 0</span>.';
  }

  function redraw() {
    var parsed = geoParseSegments(specIn.value, 10);
    if (parsed.bad) { blank(parsed.bad); return; }
    var segs = parsed.segments;
    var run = sweepEvents(segs), res = run.result, steps = run.trace;
    var brute = geoSweepBrute(segs);
    atIn.max = steps.length;
    var at = geoStep(parseInt(atIn.value, 10), 1, steps.length);
    atOut.textContent = at + ' of ' + steps.length;
    var step = steps[at - 1];
    var active = {};
    step.active.forEach(function (i) { active[i] = true; });
    var crossSet = {};
    res.crossings.forEach(function (p) { crossSet[p[0]] = true; crossSet[p[1]] = true; });

    var all = parsed.points.slice();
    var f = geoFrame(all, { width: 660, height: 280 });
    var svg = '';
    segs.forEach(function (s, i) {
      var tone = active[i] ? 'cyan' : (crossSet[i] ? 'red' : 'muted');
      svg += geoLine(f, s[0], s[1], tone, active[i] ? 3 : 1.6);
    });
    svg += geoLine(f, [step.x, Math.min.apply(null, all.map(function (p) { return p[1]; })) - 1],
                      [step.x, Math.max.apply(null, all.map(function (p) { return p[1]; })) + 1],
                   'amber', 1.8, '4 3');
    res.crossings.forEach(function (pair) {
      var A = segs[pair[0]], B = segs[pair[1]];
      svg += geoDot2(f, [(A[0][0] + A[1][0] + B[0][0] + B[1][0]) / 4,
                         (A[0][1] + A[1][1] + B[0][1] + B[1][1]) / 4], 'red', 3.5, null);
    });
    plot.innerHTML = svg;

    var rows = '';
    steps.forEach(function (t, i) {
      rows += '<tr' + (i === at - 1 ? ' class="tone-cyan"' : '') + '><th class="rowhead">'
        + (i + 1) + '</th><td>x = ' + t.x + '</td><td>' + t.kind + '</td><td>segment '
        + (t.seg + 1) + '</td><td>' + (t.active.length
            ? t.active.map(function (s) { return s + 1; }).join(', ') : 'empty')
        + '</td><td>' + t.active.length + '</td></tr>';
    });
    table.innerHTML = '<caption>Every event in x order, with the status list after it. The pair '
      + 'tests a start event makes is the size of the list it joins</caption><thead><tr>'
      + '<th>event</th><th>at</th><th>kind</th><th>segment</th><th>status list</th>'
      + '<th>size</th></tr></thead><tbody>' + rows + '</tbody>';

    var agree = geoPairKeys(res.crossings) === geoPairKeys(brute);
    document.getElementById('swN').textContent = segs.length;
    document.getElementById('swE').textContent = res.events.length;
    document.getElementById('swTests').textContent = res.tests;
    document.getElementById('swAll').textContent = res.allPairs;
    document.getElementById('swFound').textContent = res.crossings.length;
    document.getElementById('swOracle').textContent = brute.length + (agree ? '' : ' — DISAGREE');

    status.innerHTML = '<strong>' + res.crossings.length + ' crossing'
      + geoPlural(res.crossings.length, '', 's') + ' among ' + segs.length + ' segments, from '
      + '<span class="tone-cyan">' + res.tests + '</span> pair test'
      + geoPlural(res.tests, '', 's') + ' rather than ' + res.allPairs + '.</strong> '
      + (res.tests < res.allPairs
          ? 'The sweep skipped ' + (res.allPairs - res.tests) + ' pair'
            + geoPlural(res.allPairs - res.tests, '', 's') + ' because their x ranges never '
            + 'overlapped, and no test can find a crossing between two segments that are never '
            + 'on the line together. '
          : '<span class="tone-amber">The sweep made every test the brute force would.</span> '
            + 'The status list held all of them at once, so sorting the endpoints bought '
            + 'nothing here. That is not a flaw in the sweep: it is what its bound says, and '
            + 'the bound is about the OUTPUT size as well as the input. ')
      + 'Every pair was then tested again outside the sweep, and '
      + (agree
          ? 'the two crossing sets are the same. The saving is in the work, not in the answer.'
          : '<span class="tone-red">they are not the same set. The sweep is missing a '
            + 'crossing or inventing one.</span>');
  }

  function apply() {
    var p = SWP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; atIn.value = 1;
    redraw();
  }
  var START = SWP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  atIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Sorting the work down, and the input where it sorts nothing down",
        subtitle="Pair tests the sweep line made, against every pair there is",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type segments and step the line across them"),
        panel_intro=cfg.get(
            "panel_intro",
            "The crossings the sweep reports are checked against testing every pair, which is "
            "the definition. The two counts beside them are the point of the lesson: the same "
            "answer, and a different amount of work to reach it.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# closest -- the strip, and the seven neighbours it never exceeds
# ---------------------------------------------------------------------------

_CL_PRESETS = [
    {
        "id": "scatter",
        "label": "twelve points, one close pair",
        "spec": "2, 9; 5, 1; 8, 14; 11, 4; 14, 12; 17, 2; 20, 10; 23, 6; 26, 15; 29, 3; 12, 5; 13, 4",
        "note": "the close pair straddles the dividing line, which is what the strip is for",
    },
    {
        "id": "column",
        "label": "two columns either side of the split",
        "spec": "0, 0; 0, 3; 0, 6; 0, 9; 0, 12; 1, 1; 1, 4; 1, 7; 1, 10; 1, 13",
        "note": "every point is in the strip, and the seven-neighbour rule is what caps the work",
    },
    {
        "id": "grid",
        "label": "a regular grid: many pairs at the minimum",
        "spec": "0, 0; 4, 0; 8, 0; 0, 4; 4, 4; 8, 4; 0, 8; 4, 8; 8, 8",
        "note": "twelve pairs tie at distance 4, so the answer is a value and not a pair",
    },
    {
        "id": "duplicate",
        "label": "the same point twice: distance zero",
        "spec": "0, 0; 5, 5; 9, 2; 5, 5; 3, 8",
        "note": "squared distance 0, which is exactly representable and needs no special case",
    },
    {
        "id": "pair",
        "label": "two points and nothing else",
        "spec": "0, 0; 3, 4",
        "note": "the base case, where the recursion never happens",
    },
]


def _closest(cfg):
    chosen = _chosen(_CL_PRESETS, cfg)
    markup = (
        _toolbar(
            "The closest pair, without a square root",
            "divide and conquer against every pair",
            [("cyan", "the closest pair"), ("purple", "in the strip"), ("muted", "everything else")],
        )
        + _stage(_svg("clPlot", "0 0 660 280",
                      "The points with the closest pair joined and the dividing line drawn."))
        + _table("clLevels")
        + _banner("clStatus")
    )
    controls = (
        _select("clPreset", "Worked example", _options(_CL_PRESETS), chosen["id"])
        + _text("clSpec", "Points, as x, y", "2, 9; 5, 1; 8, 14; 11, 4")
        + _kpis([("Points", "clN"), ("Squared distance", "clD2"),
                 ("The pair", "clPair"), ("Comparisons, divide and conquer", "clDC"),
                 ("Comparisons, every pair", "clBrute"),
                 ("Strip comparisons against 7n", "clStrip")])
        + _hint(
            "clHint",
            "Points are <span class=\"tt\">x, y</span> separated by semicolons. Nothing here is "
            "square-rooted: the answer is a squared distance, which is an exact integer, and "
            "comparing squared distances orders points the same way comparing distances does. "
            "The strip column is the claim the lesson proves — each point in the strip is "
            "compared with at most seven others — beside the number of comparisons actually made.",
        )
    )
    script = _RATIO_JS + _ONE_INPUT + _presets_js("CLP", _CL_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('clPreset'), specIn = document.getElementById('clSpec');
  var plot = document.getElementById('clPlot'), levels = document.getElementById('clLevels');
  var status = document.getElementById('clStatus');
  var KPIS = ['clN', 'clD2', 'clPair', 'clDC', 'clBrute', 'clStrip'];

  function blank(why) {
    plot.innerHTML = ''; levels.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Points are '
      + '<span class="tt">x, y</span> separated by semicolons.';
  }

  function redraw() {
    var parsed = geoParse(specIn.value, 24);
    if (parsed.bad) { blank(parsed.bad); return; }
    var P = parsed.points;
    if (P.length < 2) { blank('a closest pair needs two points'); return; }

    var run = closestPair(P), res = run.result;
    var brute = geoClosestBrute(P);
    var agree = String(res.d2) === String(brute.d2);
    var sorted = lexSort(P), mid = sorted[sorted.length >> 1];

    var f = geoFrame(P, { width: 660, height: 280 });
    var ys = P.map(function (p) { return p[1]; });
    var svg = geoLine(f, [mid[0], Math.min.apply(null, ys) - 1],
                         [mid[0], Math.max.apply(null, ys) + 1], 'purple', 1.4, '4 3');
    P.forEach(function (p) { svg += geoDot2(f, p, 'muted', 4, null); });
    if (res.pair) {
      svg += geoLine(f, res.pair[0], res.pair[1], 'cyan', 3);
      svg += geoDot2(f, res.pair[0], 'cyan', 5.5, geoPointText(res.pair[0]));
      svg += geoDot2(f, res.pair[1], 'cyan', 5.5, geoPointText(res.pair[1]));
    }
    plot.innerHTML = svg;

    var rows = '';
    res.levels.forEach(function (l, i) {
      var per = l.strip ? R(BigInt(l.compares), BigInt(l.strip)) : null;
      rows += '<tr><th class="rowhead">' + (i + 1) + '</th><td>' + l.depth + '</td><td>' + l.n
        + '</td><td>' + l.strip + '</td><td>' + l.compares + '</td><td>'
        + (per ? Rtext(per) + ' = ' + Rnum(per).toFixed(2) : '—') + '</td></tr>';
    });
    levels.innerHTML = '<caption>One row per merge, deepest first: the size of the strip and the '
      + 'comparisons made inside it. The last column is comparisons per strip point, and the '
      + 'lesson proves it cannot pass 7</caption><thead><tr><th>merge</th><th>depth</th>'
      + '<th>points</th><th>in the strip</th><th>comparisons</th><th>per strip point</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    var dc = run.counts.compares || 0;
    /* The busiest strip, as an exact fraction: compared by cross-multiplying
       rather than by dividing, so the winner is decided without rounding. */
    var worst = R(0n, 1n);
    res.levels.forEach(function (l) {
      if (!l.strip) return;
      var r = R(BigInt(l.compares), BigInt(l.strip));
      if (Rcmp(r, worst) > 0) worst = r;
    });
    document.getElementById('clN').textContent = P.length;
    document.getElementById('clD2').textContent = String(res.d2)
      + (res.d2 === 0n ? ' — two points coincide' : '');
    document.getElementById('clPair').textContent = res.pair
      ? (geoPointText(res.pair[0]) + ' ' + geoPointText(res.pair[1])) : '—';
    document.getElementById('clDC').textContent = dc;
    document.getElementById('clBrute').textContent = brute.tests;
    document.getElementById('clStrip').textContent = res.stripCompares + ' against ' + res.bound;

    status.innerHTML = '<strong>Squared distance ' + res.d2 + '</strong>'
      + (res.pair ? ', between ' + geoPointText(res.pair[0]) + ' and '
                    + geoPointText(res.pair[1]) : '') + '. '
      + (agree
          ? 'Testing all ' + brute.tests + ' pairs reaches the same value, so the recursion did '
            + 'not miss a pair by splitting it across the line — which is the one way this '
            + 'algorithm can be wrong and still look finished. '
          : '<span class="tone-red">Testing every pair gives ' + brute.d2 + ' instead. The '
            + 'recursion missed a pair.</span> ')
      + 'It used <span class="tone-cyan">' + dc + '</span> comparison'
      + geoPlural(dc, '', 's') + ' against ' + brute.tests + ' for the brute force'
      + (dc < brute.tests ? '' : ', which at this size is no saving at all — the recursion pays '
          + 'for itself only once n is large enough that n log n is under n(n−1)/2')
      + '. Inside the strips it made ' + res.stripCompares + ' comparison'
      + geoPlural(res.stripCompares, '', 's') + ' against the bound of 7n = ' + res.bound
      + ', and the busiest single strip ran at ' + Rtext(worst) + ' = '
      + Rnum(worst).toFixed(2) + ' comparisons per point. '
      + 'The bound is a proof about every input; ' + Rtext(worst) + ' is a measurement of '
      + 'this one, and the gap between them is not evidence that the proof is loose.';
  }

  function apply() {
    var p = CLP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = CLP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The closest pair, as a squared distance that is never rounded",
        subtitle="Divide and conquer against every pair, and the strip against 7n",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type points and watch the strip do the work"),
        panel_intro=cfg.get(
            "panel_intro",
            "Distances here are squared and therefore integers, so the comparison that decides "
            "the answer is exact. The brute force runs beside the recursion on the same points, "
            "because a recursion that drops a pair across the dividing line still returns a "
            "plausible number.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# polygon -- the doubled area, and the ray that hits a vertex
# ---------------------------------------------------------------------------

_PG_PRESETS = [
    {
        "id": "ell",
        "label": "an L, so the shape is not convex",
        "spec": "0, 0; 6, 0; 6, 2; 2, 2; 2, 6; 0, 6",
        "query": "1, 5",
        "note": "a point inside the arm the convex hull would have swallowed",
    },
    {
        "id": "vertex",
        "label": "a triangle, with the ray aimed at a vertex",
        "spec": "0, 0; 8, 0; 4, 4",
        "query": "-2, 0",
        "note": "the ray leaves along an edge and through two vertices at once",
    },
    {
        "id": "comb",
        "label": "a comb: the ray crosses six times",
        "spec": "0, 0; 12, 0; 12, 6; 10, 6; 10, 2; 8, 2; 8, 6; 6, 6; 6, 2; 4, 2; 4, 6; 2, 6; 2, 2; 0, 2",
        "query": "-1, 4",
        "note": "an even count outside and an odd one inside, on the same horizontal line",
    },
    {
        "id": "clockwise",
        "label": "a square typed clockwise",
        "spec": "0, 0; 0, 5; 5, 5; 5, 0",
        "query": "2, 2",
        "note": "the doubled area comes out negative, which is the orientation and not an error",
    },
    {
        "id": "flat",
        "label": "a degenerate polygon of zero area",
        "spec": "0, 0; 3, 3; 6, 6",
        "query": "3, 3",
        "note": "three collinear vertices: area 0, and no interior for a point to be in",
    },
]


def _polygon(cfg):
    chosen = _chosen(_PG_PRESETS, cfg)
    markup = (
        _toolbar(
            "Area, orientation, and inside",
            "two formulas for the area and two definitions of inside",
            [("cyan", "the polygon"), ("amber", "the ray from the query point"),
             ("green", "inside"), ("red", "outside")],
        )
        + _stage(_svg("pgPlot", "0 0 660 300",
                      "The polygon with the query point and the horizontal ray drawn from it."))
        + _table("pgEdges")
        + _banner("pgStatus")
    )
    controls = (
        _select("pgPreset", "Worked example", _options(_PG_PRESETS), chosen["id"])
        + _text("pgSpec", "Vertices in order, as x, y", "0, 0; 6, 0; 6, 2; 2, 2; 2, 6; 0, 6")
        + _text("pgQuery", "The query point, as x, y", "1, 5")
        + _kpis([("Doubled area, shoelace", "pgA2"), ("Doubled area, trapezoid rule", "pgA2b"),
                 ("Area", "pgArea"), ("Orientation", "pgTurn"),
                 ("Ray crossings", "pgCross"), ("Inside, by parity", "pgIn"),
                 ("Winding number", "pgWind"), ("The two definitions agree", "pgAgree")])
        + _hint(
            "pgHint",
            "Vertices in order around the polygon; the last joins back to the first. The doubled "
            "area is kept doubled so that it stays an integer, and it is halved only at the end. "
            "Its SIGN is the orientation and is information, not noise: type the fourth worked "
            "example and watch it go negative without the shape changing. The ray test counts an "
            "edge only when one endpoint is strictly above the ray and the other is not, which "
            "is the rule that makes a ray through a vertex count once rather than twice.",
        )
    )
    script = _RATIO_JS + _ONE_INPUT + _presets_js("PGP", _PG_PRESETS, ["spec", "query", "note"]) + r"""
  var presetIn = document.getElementById('pgPreset'), specIn = document.getElementById('pgSpec');
  var queryIn = document.getElementById('pgQuery');
  var plot = document.getElementById('pgPlot'), edges = document.getElementById('pgEdges');
  var status = document.getElementById('pgStatus');
  var KPIS = ['pgA2', 'pgA2b', 'pgArea', 'pgTurn', 'pgCross', 'pgIn', 'pgWind', 'pgAgree'];

  function blank(why) {
    plot.innerHTML = ''; edges.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Vertices in order: '
      + '<span class="tt">0, 0; 6, 0; 6, 2; 2, 2</span>.';
  }

  function redraw() {
    var parsed = geoParse(specIn.value, 20);
    if (parsed.bad) { blank(parsed.bad); return; }
    var poly = parsed.points;
    if (poly.length < 3) { blank('a polygon needs three vertices'); return; }
    var q = geoParse(queryIn.value, 1);
    if (q.bad || q.points.length !== 1) { blank('the query point is one point, as x, y'); return; }
    var Q = q.points[0];

    var a2 = shoelace2(poly), a2b = geoAreaTrapezoid(poly);
    var par = rayParity(poly, Q), wind = geoWinding(poly, Q);
    var simple = geoSimple(poly);
    var agree = par.inside === wind.inside && par.onBoundary === wind.onBoundary;

    var xs = poly.map(function (p) { return p[0]; }).concat([Q[0]]);
    var f = geoFrame(poly.concat([Q]), { width: 660, height: 300 });
    var rayEnd = [Math.max.apply(null, xs) + 2, Q[1]];
    var svg = geoPoly(f, poly, 'cyan', true)
      + geoLine(f, Q, rayEnd, 'amber', 1.6, '5 4')
      + geoDot2(f, Q, par.onBoundary ? 'amber' : (par.inside ? 'green' : 'red'), 5.5,
                geoPointText(Q));
    poly.forEach(function (p, i) { svg += geoDot2(f, p, 'cyan', 4, String(i + 1)); });
    plot.innerHTML = svg;

    var counted = {};
    par.detail.forEach(function (d) { counted[d.edge] = d.counted; });
    var rows = '';
    poly.forEach(function (p, i) {
      var b = poly[(i + 1) % poly.length];
      var term = BigInt(p[0]) * BigInt(b[1]) - BigInt(b[0]) * BigInt(p[1]);
      var straddles = (p[1] > Q[1]) !== (b[1] > Q[1]);
      rows += '<tr' + (counted[i] ? ' class="tone-amber"' : '') + '><th class="rowhead">'
        + geoPointText(p) + ' → ' + geoPointText(b) + '</th><td class="tt">' + term
        + '</td><td>' + (straddles ? 'yes' : 'no') + '</td><td>'
        + (counted[i] === undefined ? '—' : (counted[i] ? 'counted' : 'not counted'))
        + '</td><td>' + (onSegment(p, b, Q) ? '<span class="tone-amber">the point is on it</span>'
                                            : '') + '</td></tr>';
    });
    edges.innerHTML = '<caption>One row per edge: its contribution to the doubled area, whether '
      + 'it straddles the ray’s height, and whether the half-open rule counted it</caption>'
      + '<thead><tr><th>edge</th><th>x1·y2 − x2·y1</th><th>straddles the ray</th>'
      + '<th>crossing</th><th>note</th></tr></thead><tbody>' + rows + '</tbody>';

    var absA = a2 < 0n ? -a2 : a2;
    document.getElementById('pgA2').textContent = String(a2);
    document.getElementById('pgA2b').textContent = String(a2b)
      + (a2 === a2b ? '' : ' — DISAGREE');
    document.getElementById('pgArea').textContent = Rtext(R(absA, 2n));
    document.getElementById('pgTurn').textContent = a2 > 0n ? 'counter-clockwise'
      : (a2 < 0n ? 'clockwise' : 'no orientation: the area is zero');
    document.getElementById('pgCross').textContent = par.crossings;
    document.getElementById('pgIn').textContent = par.onBoundary ? 'on the boundary'
      : (par.inside ? 'inside' : 'outside');
    document.getElementById('pgWind').textContent = wind.winding;
    document.getElementById('pgAgree').textContent = agree ? 'yes' : 'NO';

    status.innerHTML = '<strong>2A = ' + a2 + ', so the area is ' + Rtext(R(absA, 2n))
      + '</strong> and the vertices are typed '
      + (a2 > 0n ? 'counter-clockwise' : (a2 < 0n ? 'clockwise'
          : 'along a line, giving no orientation at all')) + '. '
      + (a2 === a2b
          ? 'The trapezoid rule, which multiplies different pairs of coordinates together, '
            + 'returns the same integer. '
          : '<span class="tone-red">The trapezoid rule returns ' + a2b + ' instead, and two '
            + 'exact formulas for one area cannot disagree.</span> ')
      + 'The ray from ' + geoPointText(Q) + ' crossed <span class="tone-amber">' + par.crossings
      + '</span> edge' + geoPlural(par.crossings, '', 's') + ', so the point is '
      + '<span class="tone-' + (par.onBoundary ? 'amber' : (par.inside ? 'green' : 'red')) + '">'
      + (par.onBoundary ? 'on the boundary' : (par.inside ? 'inside' : 'outside')) + '</span>. '
      + (simple.simple
          ? 'The polygon is simple — no two non-adjacent edges meet — so the winding number and '
            + 'the parity must agree, and the winding number came out ' + wind.winding + '. '
          : '<span class="tone-amber">The polygon is not simple: ' + simple.crossings.length
            + ' pair' + geoPlural(simple.crossings.length, '', 's') + ' of non-adjacent edges '
            + 'meet.</span> Parity and winding are then different questions and may disagree; '
            + 'the winding number is ' + wind.winding + '. ')
      + (agree ? '' : '<span class="tone-red">They disagree here.</span> ')
      + (absA === 0n
          ? 'With zero area there is no interior, so every point the polygon touches is on its '
            + 'boundary and every other point is outside. The test still answers, which is what '
            + 'a degenerate case is supposed to do.'
          : 'Nothing above was rounded: the doubled area is an integer and the parity is a count.');
  }

  function apply() {
    var p = PGP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; queryIn.value = p.query;
    redraw();
  }
  var START = PGP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; queryIn.value = START.query; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  queryIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The doubled area, its sign, and whether a point is inside",
        subtitle="Two exact formulas for the area, and two definitions of inside",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type a polygon and a point to ask about"),
        panel_intro=cfg.get(
            "panel_intro",
            "The area is computed twice by different products and printed doubled, because 2A "
            "is an integer and A is not. Inside is decided twice as well, once by ray parity "
            "and once by the winding number, and the page checks the polygon is simple before "
            "claiming the two must agree.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# calipers -- h pairs instead of all of them
# ---------------------------------------------------------------------------

_CA_PRESETS = [
    {
        "id": "convex",
        "label": "eight points in convex position",
        "spec": "0, 3; 2, 0; 6, 0; 9, 3; 9, 7; 6, 10; 2, 10; 0, 7",
        "note": "every point is a hull vertex, so the calipers walk all of them",
    },
    {
        "id": "cloud",
        "label": "sixteen points, four on the hull",
        "spec": "0, 0; 12, 0; 12, 9; 0, 9; 3, 2; 5, 4; 7, 3; 9, 5; 4, 6; 6, 7; 8, 6; 2, 5; 10, 2; 5, 1; 7, 8; 3, 7",
        "note": "the diameter is a hull pair, so twelve interior points cost nothing",
    },
    {
        "id": "thin",
        "label": "a long thin sliver",
        "spec": "0, 0; 40, 1; 20, 1; 10, 0; 30, 1",
        "note": "the hull is a quadrilateral and the diameter is its long diagonal",
    },
    {
        "id": "segment",
        "label": "collinear points: the hull is a segment",
        "spec": "0, 0; 3, 3; 6, 6; 9, 9; 12, 12",
        "note": "two hull vertices, and the diameter is the whole segment",
    },
    {
        "id": "square",
        "label": "a square: two diagonals tie",
        "spec": "0, 0; 6, 0; 6, 6; 0, 6",
        "note": "the squared diameter is 72 and two different pairs attain it",
    },
]


def _calipers(cfg):
    chosen = _chosen(_CA_PRESETS, cfg)
    markup = (
        _toolbar(
            "The two furthest points",
            "h antipodal pairs against all n(n − 1)/2 of them",
            [("cyan", "the diameter"), ("purple", "an antipodal pair"),
             ("muted", "not on the hull")],
        )
        + _stage(_svg("caPlot", "0 0 520 300",
                      "The points, the hull as a closed polygon, and the diameter drawn heavy."))
        + _table("caPairs")
        + _banner("caStatus")
    )
    controls = (
        _select("caPreset", "Worked example", _options(_CA_PRESETS), chosen["id"])
        + _text("caSpec", "Points, as x, y", "0, 3; 2, 0; 6, 0; 9, 3")
        + _kpis([("Points", "caN"), ("Hull vertices", "caH"),
                 ("Squared diameter, calipers", "caD2"),
                 ("Squared diameter, every pair", "caBrute"),
                 ("Antipodal pairs examined", "caPairs2"),
                 ("Pairs there are", "caAll")])
        + _hint(
            "caHint",
            "Points are <span class=\"tt\">x, y</span> separated by semicolons. The diameter of a "
            "set is the diameter of its convex hull, because a point inside the hull cannot be "
            "an endpoint of the longest segment. The calipers then walk the hull once and look "
            "only at ANTIPODAL pairs — the pairs that admit parallel supporting lines. The "
            "distance is squared and therefore an exact integer, so the comparison that picks "
            "the winner never rounds.",
        )
    )
    script = _BASE_JS + _ONE_INPUT + _presets_js("CAP", _CA_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('caPreset'), specIn = document.getElementById('caSpec');
  var plot = document.getElementById('caPlot'), table = document.getElementById('caPairs');
  var status = document.getElementById('caStatus');
  var KPIS = ['caN', 'caH', 'caD2', 'caBrute', 'caPairs2', 'caAll'];

  function blank(why) {
    plot.innerHTML = ''; table.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> Points are '
      + '<span class="tt">x, y</span> separated by semicolons.';
  }

  function redraw() {
    var parsed = geoParse(specIn.value, 24);
    if (parsed.bad) { blank(parsed.bad); return; }
    var P = geoDedupe(parsed.points).points;
    if (P.length < 2) { blank('a diameter needs two distinct points'); return; }

    var hull = geoExactHull(P).hull;
    var run = calipers(hull), res = run.result;
    var brute = diameterBrute(P);
    var agree = String(res.d2) === String(brute.d2);

    var f = geoFrame(P, { width: 520, height: 300 });
    var svg = geoPoly(f, hull, 'purple', false);
    P.forEach(function (p) { svg += geoDot2(f, p, 'muted', 4, null); });
    hull.forEach(function (p) { svg += geoDot2(f, p, 'purple', 4.5, null); });
    if (res.pair) {
      svg += geoLine(f, res.pair[0], res.pair[1], 'cyan', 3);
      svg += geoDot2(f, res.pair[0], 'cyan', 5.5, geoPointText(res.pair[0]));
      svg += geoDot2(f, res.pair[1], 'cyan', 5.5, geoPointText(res.pair[1]));
    }
    plot.innerHTML = svg;

    var rows = '';
    res.pairs.forEach(function (pr, i) {
      var a = hull[pr[0]], b = hull[pr[1]], d = dist2(a, b);
      rows += '<tr' + (String(d) === String(res.d2) ? ' class="tone-cyan"' : '')
        + '><th class="rowhead">' + (i + 1) + '</th><td class="tt">' + geoPointText(a)
        + '</td><td class="tt">' + geoPointText(b) + '</td><td>' + d + '</td><td>'
        + (String(d) === String(res.d2) ? 'the diameter' : '') + '</td></tr>';
    });
    table.innerHTML = '<caption>The antipodal pairs the calipers visited, in order round the '
      + 'hull. There are ' + res.pairs.length + ' of them against ' + (P.length * (P.length - 1) / 2)
      + ' pairs of points</caption><thead><tr><th>step</th><th>from</th><th>to</th>'
      + '<th>squared distance</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    var ties = 0;
    for (var i = 0; i < P.length; i += 1) for (var j = i + 1; j < P.length; j += 1) {
      if (String(dist2(P[i], P[j])) === String(brute.d2)) ties += 1;
    }
    document.getElementById('caN').textContent = P.length;
    document.getElementById('caH').textContent = hull.length;
    document.getElementById('caD2').textContent = String(res.d2);
    document.getElementById('caBrute').textContent = String(brute.d2)
      + (agree ? '' : ' — DISAGREE');
    document.getElementById('caPairs2').textContent = res.pairs.length;
    document.getElementById('caAll').textContent = P.length * (P.length - 1) / 2;

    status.innerHTML = '<strong>Squared diameter ' + res.d2 + '</strong>'
      + (res.pair ? ', between ' + geoPointText(res.pair[0]) + ' and '
                    + geoPointText(res.pair[1]) : '')
      + (ties > 1 ? ', and <span class="tone-amber">' + ties + ' pairs attain it</span>, so the '
          + 'answer is a value and the pair printed is one of several'
          : ', attained by that pair alone') + '. '
      + (agree
          ? 'Testing all ' + (P.length * (P.length - 1) / 2) + ' pairs gives the same value. '
          : '<span class="tone-red">Testing all pairs gives ' + brute.d2 + ' instead, so the '
            + 'calipers skipped the pair that wins.</span> ')
      + 'The hull has <span class="tone-purple">' + hull.length + '</span> of the ' + P.length
      + ' points on it, and the calipers looked at ' + res.pairs.length + ' antipodal pair'
      + geoPlural(res.pairs.length, '', 's') + '. '
      + (hull.length < P.length
          ? 'The ' + (P.length - hull.length) + ' interior point'
            + geoPlural(P.length - hull.length, '', 's') + ' cost nothing after the hull was '
            + 'built: the point of a convex hull furthest from anything is always a vertex, so '
            + 'for any point q strictly inside there is a hull vertex at least as far from '
            + 'every other point as q is, and q cannot be an endpoint of the longest segment. '
          : 'Every point is a hull vertex here, so the hull bought nothing and the calipers are '
            + 'walking the whole input. ')
      + 'h is a property of this input, not a bound: on a set whose points all sit on a circle '
          + 'h is n, and the walk is then linear in n rather than in something smaller.';
  }

  function apply() {
    var p = CAP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec;
    redraw();
  }
  var START = CAP[presetIn.value];
  if (START && !specIn.value) specIn.value = START.spec;
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The two furthest points, from h pairs instead of all of them",
        subtitle="Rotating calipers against every pair, with the distance left squared",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type points and read the diameter off the hull"),
        panel_intro=cfg.get(
            "panel_intro",
            "The calipers walk the hull once and examine only antipodal pairs. Every pair of "
            "points is then tested anyway, on the same input, because an algorithm that visits "
            "the wrong pairs returns a distance that is real and not the largest.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# kdtree -- nodes visited, against n
# ---------------------------------------------------------------------------

_KD_PRESETS = [
    {
        "id": "scatter",
        "label": "sixteen points, a small window",
        "spec": "1, 1; 3, 9; 5, 4; 7, 12; 9, 2; 11, 7; 13, 14; 15, 5; 2, 6; 4, 13; 6, 8; 8, 3; 10, 11; 12, 1; 14, 9; 16, 6",
        "rect": "0, 0, 6, 6",
        "note": "four points found, and far fewer than sixteen nodes visited to find them",
    },
    {
        "id": "everything",
        "label": "a window that contains every point",
        "spec": "1, 1; 3, 9; 5, 4; 7, 12; 9, 2; 11, 7; 13, 14; 15, 5; 2, 6; 4, 13; 6, 8; 8, 3",
        "rect": "0, 0, 20, 20",
        "note": "the query visits every node, because it has to report every point",
    },
    {
        "id": "empty",
        "label": "a window with nothing in it",
        "spec": "1, 1; 3, 9; 5, 4; 7, 12; 9, 2; 11, 7; 13, 14; 15, 5; 2, 6; 4, 13; 6, 8; 8, 3",
        "rect": "17, 17, 19, 19",
        "note": "nothing found, and the visit count is the honest cost of finding out",
    },
    {
        "id": "column",
        "label": "a tall thin window",
        "spec": "1, 1; 3, 9; 5, 4; 7, 12; 9, 2; 11, 7; 13, 14; 15, 5; 2, 6; 4, 13; 6, 8; 8, 3",
        "rect": "4, 0, 6, 20",
        "note": "narrow in x and open in y: the x splits prune and the y splits do not",
    },
]


def _kdtree(cfg):
    chosen = _chosen(_KD_PRESETS, cfg)
    markup = (
        _toolbar(
            "Range search, and the nodes it did not visit",
            "nodes visited against n, on the same query",
            [("cyan", "reported"), ("amber", "the query window"), ("muted", "not reported")],
        )
        + _stage(_svg("kdPlot", "0 0 520 280",
                      "The points with the query rectangle drawn and the reported points "
                      "highlighted.")
                 + _svg("kdTree", "0 0 660 240",
                        "The 2-d tree, each node labelled with its splitting coordinate."))
        + _table("kdRows")
        + _banner("kdStatus")
    )
    controls = (
        _select("kdPreset", "Worked example", _options(_KD_PRESETS), chosen["id"])
        + _text("kdSpec", "Points, as x, y", "1, 1; 3, 9; 5, 4; 7, 12")
        + _text("kdRect", "The window, as x0, y0, x1, y1", "0, 0, 6, 6")
        + _kpis([("Points", "kdN"), ("Tree nodes", "kdNodes"),
                 ("Nodes visited", "kdVisited"), ("Points reported", "kdFound"),
                 ("Points found by scanning", "kdBrute"),
                 ("Visited as a fraction of n", "kdFrac")])
        + _hint(
            "kdHint",
            "The tree splits on x at even depths and on y at odd ones, always at the median, so "
            "it is balanced by construction. A subtree is skipped when the window lies wholly on "
            "one side of the splitting coordinate — that is the entire saving, and it is a "
            "property of the QUERY, not of the tree. Widen the window until it covers everything "
            "and the visit count rises to the number of nodes.",
        )
    )
    script = _TREE_JS + _ONE_INPUT + _presets_js("KDP", _KD_PRESETS, ["spec", "rect", "note"]) + r"""
  var presetIn = document.getElementById('kdPreset'), specIn = document.getElementById('kdSpec');
  var rectIn = document.getElementById('kdRect');
  var plot = document.getElementById('kdPlot'), treeEl = document.getElementById('kdTree');
  var table = document.getElementById('kdRows'), status = document.getElementById('kdStatus');
  var KPIS = ['kdN', 'kdNodes', 'kdVisited', 'kdFound', 'kdBrute', 'kdFrac'];

  function blank(why) {
    plot.innerHTML = ''; treeEl.innerHTML = ''; table.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> The window is four numbers: '
      + '<span class="tt">0, 0, 6, 6</span>.';
  }
  function parseRect(text) {
    var parts = String(text || '').split(/[,;\s]+/).filter(function (s) { return s.length; });
    if (parts.length !== 4) return null;
    var out = [], i;
    for (i = 0; i < 4; i += 1) {
      if (!/^-?\d+$/.test(parts[i])) return null;
      out.push(parseInt(parts[i], 10));
    }
    return [Math.min(out[0], out[2]), Math.min(out[1], out[3]),
            Math.max(out[0], out[2]), Math.max(out[1], out[3])];
  }
  function countNodes(t) { return t ? 1 + countNodes(t.l) + countNodes(t.r) : 0; }

  function redraw() {
    var parsed = geoParse(specIn.value, 24);
    if (parsed.bad) { blank(parsed.bad); return; }
    var P = geoDedupe(parsed.points).points;
    var rect = parseRect(rectIn.value);
    if (!rect) { blank('the window is four whole numbers'); return; }

    var tree = kdBuild(P, 0);
    var run = kdRange(tree, rect), res = run.result;
    var brute = geoRangeBrute(P, rect);
    var nodes = countNodes(tree);
    var agree = geoSameSet(res.found, brute);

    var corners = [[rect[0], rect[1]], [rect[2], rect[3]]];
    var f = geoFrame(P.concat(corners), { width: 520, height: 280 });
    var inside = {};
    res.found.forEach(function (p) { inside[geoKey(p)] = true; });
    var svg = geoRect(f, rect, 'amber');
    P.forEach(function (p) {
      svg += geoDot2(f, p, inside[geoKey(p)] ? 'cyan' : 'muted', inside[geoKey(p)] ? 5 : 4, null);
    });
    plot.innerHTML = svg;
    treeEl.innerHTML = drawTree(null, tree, kdKids, function (n) {
      return (n.axis === 0 ? 'x=' : 'y=') + n.point[n.axis];
    }, { width: 660, height: 240 });

    var rows = '';
    (function walk(n, depth) {
      if (!n) return;
      rows += '<tr' + (inside[geoKey(n.point)] ? ' class="tone-cyan"' : '')
        + '><th class="rowhead tt">' + geoPointText(n.point) + '</th><td>' + depth + '</td><td>'
        + (n.axis === 0 ? 'x' : 'y') + ' = ' + n.point[n.axis] + '</td><td>'
        + (inside[geoKey(n.point)] ? 'reported' : '') + '</td></tr>';
      walk(n.l, depth + 1); walk(n.r, depth + 1);
    })(tree, 0);
    table.innerHTML = '<caption>Every node of the tree, in pre-order, with the coordinate it '
      + 'splits on</caption><thead><tr><th>point</th><th>depth</th><th>splits on</th>'
      + '<th></th></tr></thead><tbody>' + rows + '</tbody>';

    document.getElementById('kdN').textContent = P.length;
    document.getElementById('kdNodes').textContent = nodes;
    document.getElementById('kdVisited').textContent = res.visited;
    document.getElementById('kdFound').textContent = res.found.length;
    document.getElementById('kdBrute').textContent = brute.length + (agree ? '' : ' — DISAGREE');
    document.getElementById('kdFrac').textContent = nodes
      ? Rtext(R(BigInt(res.visited), BigInt(nodes))) : '—';

    status.innerHTML = '<strong>' + res.found.length + ' point'
      + geoPlural(res.found.length, '', 's') + ' in the window, after visiting ' + res.visited
      + ' of the ' + nodes + ' node' + geoPlural(nodes, '', 's') + '.</strong> '
      + (agree
          ? 'Scanning all ' + P.length + ' points reports the same set, so nothing was pruned '
            + 'that should have been kept. '
          : '<span class="tone-red">Scanning all ' + P.length + ' points reports '
            + brute.length + ' instead: a subtree was pruned that contained an answer.</span> ')
      + (res.visited < nodes
          ? 'The ' + (nodes - res.visited) + ' node'
            + geoPlural(nodes - res.visited, '', 's') + ' never visited '
            + geoPlural(nodes - res.visited, 'was', 'were') + ' in a subtree lying wholly on one '
            + 'side of a split, and the window on the other. '
          : '<span class="tone-amber">Every node was visited.</span> ')
      + 'That fraction is a measurement of this window on this tree. It is not the bound: the '
      + 'proved worst case for a two-dimensional range query is on the order of √n plus the '
      + 'number of points reported, and a query that reports everything must visit everything '
      + 'no matter how the tree is built.';
  }

  function apply() {
    var p = KDP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; rectIn.value = p.rect;
    redraw();
  }
  var START = KDP[presetIn.value];
  if (START && !specIn.value) { specIn.value = START.spec; rectIn.value = START.rect; }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  rectIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Range search in two dimensions, and the nodes the query skipped",
        subtitle="Nodes visited against the number of nodes, on a window you choose",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type points and a window to search"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tree is built on the median at each level, so it is balanced whatever the "
            "points are. The saving comes from the window, and the same points with a wider "
            "window visit every node — which is the figure beside the one the lesson proves.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice -- the markup assertions
# pass, labcheck passes, and a reader is shown a range query under the heading
# about exact predicates.
# ---------------------------------------------------------------------------

_MODES = {
    "orient": _orient,
    "hull": _hull,
    "segments": _segments,
    "sweep": _sweep,
    "closest": _closest,
    "polygon": _polygon,
    "calipers": _calipers,
    "kdtree": _kdtree,
}

MODES = tuple(sorted(_MODES))


def geometry_lab(cfg):
    """The geometry course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "geometry_lab: unknown mode %r; the eight modes of the geometry course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["geometry_lab", "GEOKIT_JS", "MODES"]
