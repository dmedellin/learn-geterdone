#!/usr/bin/env node
/*
 * Test the ARITHMETIC the generated paths are built on.
 *
 * WHY THIS EXISTS, and why it is separate from labcheck.js. That harness proves
 * every published lab runs and paints. It cannot prove the numbers are right: a
 * lab that confidently reports the wrong roots passes it, and passes every
 * markup assertion in tests/ too. The footer of every algebra page promises the
 * reader that each figure is computed from the stated definition and that the
 * arithmetic is exact. This file is what makes that promise checkable.
 *
 * The same holds for the logic course: its truth tables and quantifier
 * verdicts are computed by evaluators in scripts/mathpath/labs/logic.py, and a
 * quantifier lab whose status text reasons about a different statement than
 * its evaluator computes runs, paints, and passes labcheck while teaching a
 * falsehood. That defect shipped once; the logic section below is what now
 * catches it.
 *
 * The JavaScript under test IS the JavaScript that ships. It is extracted from
 * scripts/mathpath/labs/algebra_core.py and scripts/mathpath/labs/logic.py,
 * which hold it as raw strings, so there is no second copy to drift -- testing
 * a transcription would prove nothing about the published pages.
 *
 * Usage:  node scripts/mathcheck.js
 */

const fs = require('fs');
const path = require('path');

const SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_core.py');
const src = fs.readFileSync(SOURCE, 'utf8');
const LOGIC_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'logic.py');
const logicSrc = fs.readFileSync(LOGIC_SOURCE, 'utf8');
const COUNTING_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'counting.py');
const countingSrc = fs.readFileSync(COUNTING_SOURCE, 'utf8');
const PROB_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'probability.py');
const probSrc = fs.readFileSync(PROB_SOURCE, 'utf8');
const NUMBER_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'number.py');
const numberSrc = fs.readFileSync(NUMBER_SOURCE, 'utf8');
const GRAPH_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'graph.py');
const graphSrc = fs.readFileSync(GRAPH_SOURCE, 'utf8');
const ALGO_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algorithms.py');
const algoSrc = fs.readFileSync(ALGO_SOURCE, 'utf8');
const SYSD_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'sysdesign_core.py');
const sysdSrc = fs.readFileSync(SYSD_SOURCE, 'utf8');
const ALGOCORE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algo_core.py');
const algoCoreSrc = fs.readFileSync(ALGOCORE_SOURCE, 'utf8');
const ESTIMATE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'estimate.py');
const estimateSrc = fs.readFileSync(ESTIMATE_SOURCE, 'utf8');
const LATENCY_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'latency.py');
const latencySrc = fs.readFileSync(LATENCY_SOURCE, 'utf8');

/* Each block is  NAME = r"""..."""  in the Python module. */
function blockFrom(text, name, where) {
  const m = new RegExp(name + ' = r"""([\\s\\S]*?)"""', 'm').exec(text);
  if (!m) { console.error('cannot find ' + name + ' in ' + where); process.exit(2); }
  return m[1];
}
function block(name) { return blockFrom(src, name, SOURCE); }
function logicBlock(name) { return blockFrom(logicSrc, name, LOGIC_SOURCE); }
function sysdBlock(name) { return blockFrom(sysdSrc, name, SYSD_SOURCE); }
function estimateBlock(name) { return blockFrom(estimateSrc, name, ESTIMATE_SOURCE); }
function latencyBlock(name) { return blockFrom(latencySrc, name, LATENCY_SOURCE); }
function countingBlock(name) { return blockFrom(countingSrc, name, COUNTING_SOURCE); }
function probBlock(name) { return blockFrom(probSrc, name, PROB_SOURCE); }
function numberBlock(name) { return blockFrom(numberSrc, name, NUMBER_SOURCE); }
function graphBlock(name) { return blockFrom(graphSrc, name, GRAPH_SOURCE); }
function algoBlock(name) { return blockFrom(algoSrc, name, ALGO_SOURCE); }
function algoCoreBlock(name) { return blockFrom(algoCoreSrc, name, ALGOCORE_SOURCE); }

let fails = 0;
function eq(got, want, label) {
  if (String(got) !== String(want)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ' + want); }
}
function near(got, want, tol, label) {
  if (!(Math.abs(got - want) <= tol)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ~' + want); }
}

/* A minimal SVG DOM, the same shape scripts/labcheck.js gives a real page. */
function El(name) { this.name = name; this.attrs = {}; this.children = []; this._text = ''; }
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return this.attrs[k]; };
El.prototype.appendChild = function (c) { this.children.push(c); return c; };
Object.defineProperty(El.prototype, 'textContent', {
  get: function () { return this._text; },
  set: function (v) { this._text = String(v); if (v === '') this.children = []; }
});
global.document = { createElementNS: function (_ns, n) { return new El(n); } };
function all(el, name, out) {
  out = out || [];
  el.children.forEach(function (c) { if (c.name === name) out.push(c); all(c, name, out); });
  return out;
}

eval(block('RATIONAL_JS') + block('POLY_JS') + block('EXPR_JS') + block('SURD_JS') + block('PLOT_JS'));

// ------------------------------------------------- exact rational arithmetic
console.log('exact rationals');
eq(Rtext(Radd(R(1n, 3n), R(1n, 6n))), '1/2', '1/3 + 1/6');
eq(Rtext(Rmul(R(2n, 3n), R(9n, 4n))), '3/2', '2/3 * 9/4');
eq(Rtext(Rdiv(R(-3n, 4n), R(6n, 8n))), '-1', '-3/4 / 3/4');
eq(Rtext(Rpow(R(2n, 3n), 3)), '8/27', '(2/3)^3');
eq(Rtext(Rpow(R(2n), -3)), '1/8', '2^-3');
eq(Rtext(Rparse('-7/14')), '-1/2', 'parse -7/14 in lowest terms');
eq(Rtext(Rparse('0.375')), '3/8', 'a decimal becomes an exact fraction');
eq(Rtext(Rsqrt(R(4n, 9n))), '2/3', 'sqrt(4/9)');
eq(Rsqrt(R(2n)), 'null', 'sqrt(2) is not rational, and says so');
eq(Rcmp(R(1n, 3n), R(1n, 2n)), -1, 'comparison');
/* Exactness is the whole promise: forty additions of a third stay a third. */
let big = R(1n, 3n);
for (let i = 0; i < 40; i += 1) big = Radd(big, R(1n, 3n));
eq(Rtext(big), '41/3', '41 thirds, exactly');

// ------------------------------------------------------ polynomials over Q
console.log('polynomials over Q');
function P() { return Array.prototype.slice.call(arguments).map(v => (typeof v === 'object' ? v : R(BigInt(v)))); }
eq(Ptext(P(-6, 1, 1)), 'x^2 + x - 6', 'standard form');
eq(Ptext(P(0, 0, 3)), '3x^2', 'a monomial');
eq(Ptext(P(1, -1)), '-x + 1', 'a leading -1 is written as a sign');
eq(Ptext([R(3n, 4n), R(1n)]), 'x + (3/4)', 'a fractional coefficient is bracketed');
eq(Ptext([]), '0', 'the zero polynomial');
eq(Pdeg([]), -1, 'the zero polynomial has degree -1');
eq(Ptext(Pmul(P(-2, 1), P(3, 1))), 'x^2 + x - 6', '(x-2)(x+3) expands');
eq(Rtext(Peval(P(-6, 1, 1), R(2n))), '0', 'p(2) = 0');
eq(Ptext(Pderiv(P(-6, 1, 1))), '2x + 1', 'derivative');
const dm = Pdivmod(P(-6, 1, 1), P(-2, 1));
eq(Ptext(dm.q) + ' r ' + Ptext(dm.r), 'x + 3 r 0', 'exact division');
const dm2 = Pdivmod(P(1, 0, 0, 1), P(-1, 1));
eq(Ptext(dm2.q) + ' r ' + Ptext(dm2.r), 'x^2 + x + 1 r 2', 'x^3+1 divided by x-1');
eq(Ptext(Pgcd(P(-6, 1, 1), P(-4, 0, 1))), 'x - 2', 'polynomial gcd');

// ---------------------------------------- the rational root theorem, applied
console.log('rational roots and factoring');
eq(Prationalroots(P(-6, 1, 1)).map(Rtext).join(','), '-3,2', 'roots of x^2+x-6');
eq(Prationalroots(P(-3, 5, 2)).map(Rtext).join(','), '-3,1/2', 'roots of 2x^2+5x-3');
eq(Prationalroots(P(1, 0, 1)).length, 0, 'x^2+1 has no rational root');
/* Factors come out in ascending order of their root: deterministic and stated. */
eq(Pfactortextfull(P(-6, 1, 1)), '(x + 3)(x - 2)', 'factor x^2+x-6');
eq(Pfactortextfull(P(-3, 5, 2)), '(x + 3)(2x - 1)', 'factor 2x^2+5x-3');
eq(Pfactortextfull(P(4, -4, 1)), '(x - 2)^2', 'a perfect square keeps its multiplicity');
eq(Pfactortextfull(P(1, 0, 1)), 'x^2 + 1', 'an irreducible polynomial is written as itself');
eq(Pfactortextfull(P(-4, 0, 1)), '(x + 2)(x - 2)', 'difference of squares');
eq(Pfactortextfull(P(0, -9, 0, 1)), 'x(x + 3)(x - 3)', 'x^3-9x');
eq(Pfactortextfull(P(6, -5, 1)), '(x - 2)(x - 3)', 'x^2-5x+6');
/* 4x^3-8x-12 = 4(x^3-2x-3), and +-1, +-3 are the only candidates: none works. */
eq(Pfactortextfull(P(-12, -8, 0, 4)), '4(x^3 - 2x - 3)', 'the content comes out, the cubic stays');
eq(Pfactor(P(-12, -8, 0, 4)).complete, false, 'a cubic leftover is not claimed complete');
eq(Pfactor(P(1, 0, 1)).complete, true, 'a quadratic leftover is complete');

// ------------------------------------------------------- expression parsing
console.log('the expression parser');
const ev = (s, x) => Eeval(Eparse(s), { x: x });
const pol = (s) => { const p = Epolyof(s); return p === null ? 'null' : Ptext(p); };
eq(ev('2x', 3), 6, 'implicit multiplication: 2x');
eq(ev('3(x+1)', 4), 15, '3(x+1)');
eq(ev('(x+1)(x-2)', 5), 18, '(x+1)(x-2)');
eq(ev('4x^2', 3), 36, '4x^2');
eq(ev('2sqrt(x)', 9), 6, '2sqrt(x)');
eq(Eeval(Eparse('xy'), { x: 3, y: 4 }), 12, 'xy is a product of two variables');
/* The two places a reader is marked wrong. */
eq(ev('-x^2', 3), -9, '-x^2 means -(x^2)');
eq(ev('(-x)^2', 3), 9, '(-x)^2');
eq(ev('2^3^2', 0), 512, '^ is right-associative');
eq(ev('8/2/2', 0), 2, '/ is left-associative');
eq(ev('2*3^2', 0), 18, 'power before times');
eq(isNaN(ev('sqrt(x)', -1)), true, 'outside the domain gives NaN, not an exception');
/* Errors are named rather than swallowed. */
const msg = (s) => { try { Eparse(s); return ''; } catch (e) { return e.message; } };
eq(msg('2x +'), 'the expression ends early', 'a trailing operator');
eq(msg('sqrtt(x)'), 'unknown function "sqrtt"', 'a typo in a function name');
eq(msg('x $ 2'), 'unexpected character "$"', 'a stray character');
eq(msg('(x+1'), 'expected ")"', 'an unclosed bracket');
/* Typed input reaches the EXACT machinery, not a float approximation of it. */
eq(pol('(x+1)(x-2)'), 'x^2 - x - 2', 'a typed product expands exactly');
eq(pol('(x/3) + 1/2'), '(1/3)x + (1/2)', 'rational coefficients stay exact');
eq(pol('(2x-1)^3'), '8x^3 - 12x^2 + 6x - 1', 'a typed cube expands');
eq(pol('sqrt(x)'), 'null', 'sqrt(x) is not a polynomial');
eq(pol('1/x'), 'null', 'division by x is not a polynomial');
eq(pol('0.1x + 0.2x'), '(3/10)x', '0.1 + 0.2 is 3/10, not 0.30000000000000004');

// ----------------------------------------------- surds and quadratic roots
console.log('exact surds and quadratic roots');
const Q = (v) => R(BigInt(v));
eq(surdtext(Rsurd(Q(9))), '3', 'sqrt(9)');
eq(surdtext(Rsurd(Q(8))), '2sqrt(2)', 'sqrt(8)');
eq(surdtext(Rsurd(R(1n, 2n))), '(1/2)sqrt(2)', 'sqrt(1/2)');
eq(surdtext(Rsurd(Q(72))), '6sqrt(2)', 'sqrt(72)');
let r = quadroots(Q(1), Q(-5), Q(6));
eq(r.kind + ' ' + r.roots.map(Rtext).join(','), 'rational 2,3', 'x^2-5x+6');
r = quadroots(Q(1), Q(-2), Q(-4));
eq(r.kind + ' ' + pmtext(r.p, r.s), 'irrational 1 +- sqrt(5)', 'x^2-2x-4 keeps its surd');
r = quadroots(Q(1), Q(-4), Q(4));
eq(r.kind + ' ' + Rtext(r.roots[0]), 'double 2', 'a repeated root');
r = quadroots(Q(1), Q(0), Q(1));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex +-i', 'x^2+1');
r = quadroots(Q(1), Q(-2), Q(5));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex 1 +- 2i', 'x^2-2x+5');
eq(quadroots(Q(2), Q(5), Q(-3)).roots.map(Rtext).join(','), '-3,1/2', '2x^2+5x-3');
r = quadroots(Q(3), Q(-6), Q(2));
eq(pmtext(r.p, r.s), '1 +- (1/3)sqrt(3)', '3x^2-6x+2');
/* The irrational pair really are roots: substitute them back. */
{
  const a = 3, b = -6, c = 2;
  const pv = Rnum(r.p), sv = Rnum(r.s.q) * Math.sqrt(Number(r.s.k));
  eq(Math.abs(a * (pv + sv) * (pv + sv) + b * (pv + sv) + c) < 1e-12, true, 'the + root checks out');
  eq(Math.abs(a * (pv - sv) * (pv - sv) + b * (pv - sv) + c) < 1e-12, true, 'the - root checks out');
}

// ------------------------------------------------------------- the grapher
console.log('the grapher');
{
  const svg = new El('svg');
  const p = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 });
  near(p.sx(-5), 44, 0.01, 'left edge');
  near(p.sx(5), 644, 0.01, 'right edge');
  near(p.sx(0), 344, 0.01, 'x = 0 is centred');
  near(p.sy(10), 16, 0.01, 'top edge');
  near(p.sy(-10), 386, 0.01, 'bottom edge');
  eq(p.sy(5) < p.sy(-5), true, 'positive y is higher on screen');
  p.frame();
  eq(svg.getAttribute('viewBox'), '0 0 660 420', 'viewBox');
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  eq(axes.length, 2, 'two axes');
  near(parseFloat(axes[0].attrs.y1), 201, 0.01, 'the x-axis sits at y = 0');
  near(parseFloat(axes[1].attrs.x1), 344, 0.01, 'the y-axis sits at x = 0');
}
{
  /* A window with zero out of view still gets a labelled frame. */
  const svg = new El('svg');
  Plot(svg, { xmin: 10, xmax: 20, ymin: 100, ymax: 200 }).frame();
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  near(parseFloat(axes[0].attrs.y1), 386, 0.01, 'the x-axis pins to the near edge');
  near(parseFloat(axes[1].attrs.x1), 44, 0.01, 'the y-axis pins to the near edge');
}
function runs(fn) {
  const svg = new El('svg');
  Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame().curve(fn);
  return all(svg, 'polyline');
}
eq(runs(x => x * x - 4).length, 1, 'a parabola is one unbroken run');
/* Joining across a pole draws a vertical line that is not part of the graph,
   which is exactly why readers believe 1/x is connected.
   The curve breaks for TWO different reasons and both need testing. A pole the
   sampler lands on exactly returns Infinity and breaks on the non-finite check;
   a pole it steps over returns two large finite values of opposite sign and can
   only be caught by the jump check. Sampling runs from -5 to 5 in 480 steps, so
   x = 0 IS a sample and x = 0.3 is not -- and a test using only 1/x passes with
   the jump check deleted, which is how this gap was found. */
eq(runs(x => 1 / x).length, 2, '1/x: a pole landed on exactly');
eq(runs(x => 1 / (x - 0.3)).length, 2, '1/(x-0.3): a pole stepped over');
eq(runs(x => 1 / (x * x - 0.09)).length, 3, 'two stepped-over poles give three runs');
{
  const rs = runs(x => Math.sqrt(x));
  eq(rs.length, 1, 'sqrt(x) is one run');
  eq(parseFloat(rs[0].attrs.points.split(' ')[0].split(',')[0]) >= 343.9, true,
     'sqrt(x) starts at x = 0 and not before');
}
{
  const svg = new El('svg');
  const pl = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame();
  pl.point(2, -4, 'plot-point root', '2');
  const c = all(svg, 'circle').filter(e => e.attrs.class === 'plot-point root');
  near(parseFloat(c[0].attrs.cx), 464, 0.01, 'a marked point lands where the number says');
  near(parseFloat(c[0].attrs.cy), 275, 0.01, 'and at the right height');
  pl.vline(3, 'plot-asym', 'x = 3');
  near(parseFloat(all(svg, 'line').filter(e => e.attrs.class === 'plot-asym')[0].attrs.x1), 524, 0.01,
       'an asymptote lands where the number says');
  const before = all(svg, 'circle').length;
  pl.point(NaN, 3); pl.point(1, Infinity);
  eq(all(svg, 'circle').length, before, 'a non-finite point is skipped, not drawn at NaN');
}
{
  const svg = new El('svg');
  NumberLine(svg, -10, 10).interval(-3, 5, true, false);
  const ends = all(svg, 'circle');
  eq(ends.length, 2, 'an interval has two endpoints');
  eq(ends[0].attrs.class, 'plot-end closed', 'a closed end is filled');
  eq(ends[1].attrs.class, 'plot-end open', 'an open end is hollow');
  near(parseFloat(ends[0].attrs.cx), 30 + (7 / 20) * 600, 0.01, 'the closed end is placed correctly');
}

// ---------------------------------------------------- propositional logic
console.log('propositional logic (course 1 labs)');
eval(logicBlock('PARSER_JS'));
{
  const T = { p: true }, F = { p: false };
  const env = (p, q) => ({ p, q });
  /* The conditional's one false row, and vacuous truth in both false-p rows. */
  const imp = parse('p -> q');
  eq(evalNode(imp, env(true, false)), false, 'T -> F is the one false row');
  eq(evalNode(imp, env(false, true)), true, 'F -> T is vacuously true');
  eq(evalNode(imp, env(false, false)), true, 'F -> F is vacuously true');
  /* Precedence: ~ binds tighter than &, and ~p & q differs from ~(p & q). */
  eq(evalNode(parse('~p & q'), env(false, false)), false, '~p & q at FF: negation binds tight');
  eq(evalNode(parse('~(p & q)'), env(false, false)), true, '~(p & q) at FF');
  /* Inclusive or vs xor part company in exactly the TT row. */
  eq(evalNode(parse('p | q'), env(true, true)), true, 'inclusive or is true at TT');
  eq(evalNode(parse('p ^ q'), env(true, true)), false, 'xor is false at TT');
  /* -> is right-associative: p -> q -> r is p -> (q -> r). */
  eq(evalNode(parse('p -> q -> r'), { p: true, q: true, r: false }), false, 'p->q->r at TTF');
  eq(evalNode(parse('p -> q -> r'), { p: false, q: true, r: false }), true, 'p->q->r at FTF: right-associative');
  /* Constants, so ⊤ and ⊥ mean what the pages say they mean. */
  eq(evalNode(parse('⊤'), {}), true, 'top is true');
  eq(evalNode(parse('⊥ -> p'), F), true, 'ex falso: bottom implies anything');
  /* Whole-table facts, over every assignment: the identities the lessons teach. */
  function rowsFor(vars) { return assignments(vars); }
  function agreeEverywhere(aSrc, bSrc, vars) {
    const a = parse(aSrc), b = parse(bSrc);
    return rowsFor(vars).every((e) => evalNode(a, e) === evalNode(b, e));
  }
  eq(agreeEverywhere('~(p & q)', '~p | ~q', ['p', 'q']), true, 'De Morgan over all four rows');
  eq(agreeEverywhere('p -> q', '~q -> ~p', ['p', 'q']), true, 'contraposition over all four rows');
  eq(agreeEverywhere('p -> q', 'q -> p', ['p', 'q']), false, 'the converse is NOT equivalent');
  const mt = parse('((p -> q) & ~q) -> ~p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(mt, e)), true, 'modus tollens is a tautology');
  const ac = parse('((p -> q) & q) -> p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(ac, e)), false, 'affirming the consequent is not');
  /* The row order the lessons teach: T before F, rightmost fastest. */
  eq(rowsFor(['p', 'q']).map((e) => (e.p ? 'T' : 'F') + (e.q ? 'T' : 'F')).join(' '),
     'TT TF FT FF', 'conventional row order');
}

// ------------------------------------------------------- quantifier verdicts
console.log('quantifier verdicts (course 1 labs)');
eval(logicBlock('QUANT_EVAL_JS'));
{
  /* Exhaustive over every 3x3 predicate: 512 grids. This is the check that
     would have caught the shipped row/column confusion, so it is done by
     enumeration rather than by trusting a handful of examples. */
  const N = 3;
  let thmOk = true, mirrorOk = true, negOk = true;
  for (let bits = 0; bits < 512; bits += 1) {
    const P = [], C = [];
    for (let x = 0; x < N; x += 1) {
      P.push([]); C.push([]);
      for (let y = 0; y < N; y += 1) {
        const v = ((bits >> (x * N + y)) & 1) === 1;
        P[x].push(v); C[x].push(!v);
      }
    }
    /* The lesson's theorem, and its mirror -- each in its own variables. */
    if (qExistsYForallX(P, N).v && !qForallXExistsY(P, N).v) thmOk = false;
    if (qExistsXForallY(P, N).v && !qForallYExistsX(P, N).v) mirrorOk = false;
    /* Lesson 10: negation flips every quantifier. Three dual pairs. */
    if (qForallForall(P, N).v !== !qExistsExists(C, N).v) negOk = false;
    if (qForallXExistsY(P, N).v !== !qExistsXForallY(C, N).v) negOk = false;
    if (qExistsYForallX(P, N).v !== !qForallYExistsX(C, N).v) negOk = false;
  }
  eq(thmOk, true, 'exists-y-forall-x implies forall-x-exists-y, all 512 grids');
  eq(mirrorOk, true, 'exists-x-forall-y implies forall-y-exists-x, all 512 grids');
  eq(negOk, true, 'negation duality across all three pairs, all 512 grids');

  /* A full row is not a full column: the regression that shipped. */
  const rowGrid = [[true, true, true], [false, false, false], [false, false, false]];
  eq(qExistsXForallY(rowGrid, N).v, true, 'a full row satisfies exists-x-forall-y');
  eq(qExistsYForallX(rowGrid, N).v, false, 'a full row does NOT satisfy exists-y-forall-x');
  eq(qForallXExistsY(rowGrid, N).v, false, 'and forall-x-exists-y fails: x = 2 has no y');

  /* The presets, on the 4-element universe the lessons publish. */
  function fill(n, fn) {
    const P = [];
    for (let x = 0; x < n; x += 1) { P.push([]); for (let y = 0; y < n; y += 1) P[x].push(!!fn(x + 1, y + 1)); }
    return P;
  }
  const diag = fill(4, (x, y) => x === y);
  eq(qForallXExistsY(diag, 4).v, true, 'identity: every x has its own y');
  eq(qExistsYForallX(diag, 4).v, false, 'identity: no single y serves every x — the lesson-9 separator');
  const succ = fill(4, (x, y) => y === x + 1);
  eq(qForallXExistsY(succ, 4).v, false, 'successor on {1..4}: forall-x-exists-y FAILS');
  eq(qForallXExistsY(succ, 4).why, 'x = 4 has no y at all', 'and names the top element as the reason');
  const le = fill(4, (x, y) => x <= y);
  const leVerdicts = [qForallForall(le, 4), qForallXExistsY(le, 4), qExistsYForallX(le, 4),
                      qForallYExistsX(le, 4), qExistsXForallY(le, 4), qExistsExists(le, 4)];
  eq(leVerdicts.filter((r) => r.v).length, 5, 'order preset: five of six verdicts true, as lesson 10 says');
  const leC = fill(4, (x, y) => !(x <= y));
  const leCVerdicts = [qForallForall(leC, 4), qForallXExistsY(leC, 4), qExistsYForallX(leC, 4),
                       qForallYExistsX(leC, 4), qExistsXForallY(leC, 4), qExistsExists(leC, 4)];
  eq(leCVerdicts.filter((r) => r.v).map((r) => r.why).join(';'),
     'x = 2, y = 1 works', 'complemented order preset: only exists-exists survives');
}

// ------------------------------------------------------------- counting
console.log('counting in BigInt (course 4 labs)');
{
  /* The course-4 labs promise the reader that every count is exact and that
     the derangement lab's three routes agree. The functions below are the
     shipped ones, extracted from counting.py; a wrong comb() would reach
     every page that lists selections, and a wrong derangeTerms() would ship a
     table that confidently disagrees with the lesson above it. */
  eval(countingBlock('BIGINT_JS') + countingBlock('DERANGE_JS'));

  eq(fact(0), 1n, '0! = 1');
  eq(fact(20), 2432902008176640000n, '20! exactly');
  eq(perm(10, 3), 720n, 'P(10,3) = 720');
  eq(perm(24, 12), 1295295050649600n, 'P(24,12), the largest P the lab can show');
  eq(perm(3, 5), 0n, 'P(n, r) with r > n is 0');
  eq(comb(52, 5), 2598960n, 'C(52,5) = 2 598 960');
  eq(comb(35, 12), 834451800n, 'C(35,12), the largest C(n+r-1, r) the lab can show');
  eq(comb(7, 5), 21n, 'C(7,5) = 21: five doughnuts from three kinds');
  eq(comb(6, 2), comb(5, 1) + comb(5, 2), "Pascal's rule at the lesson-5 preset");
  eq(comb(4, 7), 0n, 'C(n, r) with r > n is 0');
  eq(group(1295295050649600n), '1 295 295 050 649 600', 'digit grouping');

  const D = [1n, 0n, 1n, 2n, 9n, 44n, 265n, 1854n, 14833n, 133496n];
  for (let n = 0; n < D.length; n += 1) {
    eq(derangeFormula(n), D[n], 'D_' + n + ' by the alternating sum');
    eq(derangeRec(n), D[n], 'D_' + n + ' by the recurrence');
    if (n <= 8) eq(derangeBrute(n), D[n], 'D_' + n + ' by listing');
  }
  eq(derangeFormula(12), 176214841n, 'D_12, the largest n the slider allows');
  eq(derangeList(4).sort().join(','), '2143,2341,2413,3142,3412,3421,4123,4312,4321', 'the nine derangements of 1..4');
  const rows6 = derangeTerms(6).map((r) => r.running.toString()).join(',');
  eq(rows6, '720,0,360,240,270,264,265', 'the running total at n = 6 swings and settles on 265');
  eq(ratioDigits(265n, 720n, 7), '0.3680556', 'D_6/6! to seven places, rounded');
  eq(ratioDigits(1854n, 5040n, 7), '0.3678571', 'D_7/7! to seven places');
  eq(ratioDigits(14833n, 40320n, 7), '0.3678819', 'D_8/8! to seven places (the lesson table row)');
  eq(ratioDigits(1n, 3n, 4), '0.3333', 'ratioDigits pads and truncates correctly');
  eq(ratioDigits(0n, 1n, 7), '0.0000000', 'ratioDigits at zero');
  eq(ratioDigits(1n, 2n, 3), '0.500', 'ratioDigits at one half');
}

// ---------------------------------------------------------- probability
console.log('probability as exact fractions and summed distributions (course 5 labs)');
{
  /* The course-5 footer promises every probability is an exact fraction from
     the enumerated sample space, and that the distributions are summed term by
     term and compared with the closed forms. The functions below are the
     shipped ones, extracted from probability.py. The geometric case is the one
     that failed: a sum stopped at thirty terms reads 5.848 against a closed
     form of 6 at p = 1/6, and the lab printed both side by side. */
  eval(probBlock('FRACTION_JS') + probBlock('DIST_JS') + probBlock('BAYES_JS'));

  eq(frac(6, 36).text, '1/6', '6/36 reduces to 1/6');
  eq(frac(0, 15).text, '0', 'an empty event is 0, not 0/15');
  eq(frac(15, 15).text, '1', 'the whole space is 1');
  eq(frac(3, 0).text, 'undefined', 'conditioning on an empty event is undefined');
  eq(pct(frac(1, 6)), '16.67%', 'pct rounds to two places');
  eq(frac(18 * 6, 36 * 36).text, '1/12', 'P(A)·P(B) for first-even and sum-7, the lesson-5 pair');

  eq(comb(52, 5), 2598960, 'C(52,5) in doubles is still exact');
  eq(comb(20, 5), 15504, 'C(20,5)');

  const bin = binomialPmf(20, 0.25), mb = moments(bin.ks, bin.probs);
  near(bin.probs[5], 0.2023311518569244, 1e-12, 'P(X = 5) at n = 20, p = 1/4 (lesson 11 worked example)');
  near(mb.E, 5, 1e-12, 'E[X] summed = np = 5');
  near(mb.V, 3.75, 1e-12, 'Var(X) summed = np(1-p) = 3.75');
  near(mb.total, 1, 1e-12, 'the binomial sums to 1');
  near(bin.probs.slice(10).reduce((s, x) => s + x, 0), 0.01386441694376117, 1e-12, 'P(X >= 10) = 0.0139');
  const bin10 = binomialPmf(10, 0.5);
  near(bin10.probs[5], 0.24609375, 1e-15, 'P(exactly 5 heads in 10) = 252/1024');
  near(moments(bin10.ks, bin10.probs).E, 5, 1e-12, 'E[X] = 5 at n = 10, p = 1/2 (lesson 9 preset)');

  const K = geometricTerms(1 / 6);
  eq(K > 30, true, 'the geometric sum runs past the thirty drawn bars');
  eq(Math.pow(5 / 6, K) < 1e-15, true, 'and stops only when the tail is below 1e-15');
  const geo = geometricPmf(1 / 6, K), mg = moments(geo.ks, geo.probs);
  near(geo.probs[0], 1 / 6, 1e-15, 'P(X = 1) = 1/6, the mode');
  near(geo.probs[5], 0.06697959533607682, 1e-15, 'P(X = 6) = (5/6)^5 / 6');
  near(mg.E, 6, 1e-9, 'E[X] summed = 1/p = 6 (lesson 12 worked example)');
  near(mg.V, 30, 1e-6, 'Var(X) summed = (1-p)/p^2 = 30');
  near(mg.total, 1, 1e-12, 'the geometric sums to 1');
  near(moments(geo.ks.slice(0, 30), geo.probs.slice(0, 30)).E, 5.848342071608853, 1e-9,
       'thirty terms alone give 5.848 -- the figure the lab used to print beside 6');
  const geo12 = geometricPmf(1 / 12, geometricTerms(1 / 12)), mg12 = moments(geo12.ks, geo12.probs);
  near(mg12.E, 12, 1e-9, 'E[X] = 12 at the smallest p the slider allows');
  near(mg12.V, 132, 1e-6, 'Var(X) = 132 there');

  const uni = uniformPmf(6), mu = moments(uni.ks, uni.probs);
  near(mu.E, 3.5, 1e-12, 'a fair die: E[X] = 3.5 (lesson 8 preset)');
  near(mu.V, 35 / 12, 1e-12, 'a fair die: Var(X) = 35/12 (lesson 10)');
  const dice = diceSumPmf(), md = moments(dice.ks, dice.probs);
  eq(dice.probs.map((x) => Math.round(x * 36)).join(','), '1,2,3,4,5,6,5,4,3,2,1', 'the triangle over 36 (lesson 7 table)');
  near(md.E, 7, 1e-12, 'sum of two dice: E[X] = 7');
  near(md.V, 35 / 6, 1e-12, 'sum of two dice: Var(X) = 35/6, the lesson-10 worked example by another route');

  const cells = bayesCounts(1000000, 1000, 99, 5);
  eq([cells.D, cells.TP, cells.FN, cells.H, cells.FP, cells.TN].join(','), '1000,990,10,999000,49950,949050',
     'the four cells at 1 in 1000, 99%, 5%');
  eq(cells.posterior.text, '11/566', 'P(D|+) = 990/50940 = 11/566');
  near(cells.posterior.dec, 0.019434628975265017, 1e-15, 'about 2%, the lesson-6 answer');
  near(cells.npv.dec, 949050 / 949060, 1e-15, 'P(no D | -) from the same cells');
  eq(bayesCounts(1000000, 300000, 99, 5).posterior.text, '297/332', 'the worked example: prior 0.30 gives 297/332 = 0.895');
  eq(bayesCounts(1000000, 20000, 95, 10).posterior.text, '19/117', 'the standard: 2%, 95%, 10% gives 19/117');
  const rare = bayesCounts(1000000, 100, 99, 1);
  eq(rare.FP / rare.TP, 101, 'concept 3: 1 in 10 000 at a 1% false-positive rate is about 100 false positives per true one');
  eq(grp(50940), '50 940', 'digit grouping');
  eq(dec(990, 1000000), '0.00099', 'decimals are printed without trailing zeros');
  eq(dec(99, 100), '0.99', 'and a percentage as its decimal');
}

// -------------------------------------------------------- number theory
console.log('number theory in BigInt (course 6 labs)');
{
  /* The course-6 footer promises exact big-integer arithmetic, and lesson 14
     promises that the key the lab generates decrypts and is then recovered by
     factoring. The functions below are the shipped ones, extracted from
     number.py. The case that motivated this section: the lesson-14 worked
     example printed c = 3 for 9^7 mod 143 while the lab under it printed 48;
     the lab was right, and nothing checked either. */
  eval(numberBlock('NT_JS'));

  eq(bgcd(1071n, 462n), 21n, 'gcd(1071, 462) = 21 (lesson 5 worked example)');
  eq(bgcd(264n, 84n), 12n, 'gcd(264, 84) = 12 (lesson 4 worked example)');
  eq(bgcd(-12n, 18n), 6n, 'gcd ignores sign');
  eq(bgcd(17n, 0n), 17n, 'gcd(a, 0) = a, the base case');
  eq(egcd(1071n, 462n).join(','), '21,-3,7', '1071·(−3) + 462·7 = 21 (lesson 6 body)');
  eq(egcd(17n, 3120n).join(','), '1,-367,2', '17·(−367) + 3120·2 = 1 (lesson 6 worked example)');
  const tr = egcdTrace(17n, 3120n);
  eq(tr.g + ',' + tr.x + ',' + tr.y, '1,-367,2', 'the trace ends where egcd does');
  eq(tr.rows.every((r) => 17n * r.s + 3120n * r.t === r.r), true, 'r = a·s + b·t holds on every row of the trace');
  eq(tr.rows.map((r) => r.r).join(','), '17,3120,17,9,8,1,0', 'the remainders are the worked example\'s 9, 8, 1, 0');
  const trn = egcdTrace(-1071n, 462n);
  eq(-1071n * trn.x + 462n * trn.y, trn.g, 'a negative input keeps the identity true as typed');
  eq(modinv(17n, 3120n), 2753n, '17⁻¹ mod 3120 = 2753, the RSA private exponent');
  eq(modinv(7n, 26n), 15n, '7⁻¹ mod 26 = 15 (lesson 9 example, lesson 6 standard)');
  eq(modinv(5n, 26n), 21n, '5⁻¹ mod 26 = 21 (lesson 13 example)');
  eq(modinv(15n, 26n), 7n, '15⁻¹ mod 26 = 7 (lesson 13 worked example)');
  eq(modinv(6n, 9n), null, 'no inverse when the gcd is not 1');
  eq(modinv(2n, 4n), null, '2 has no inverse mod 4');
  eq(modinv(-367n, 3120n), 17n, 'the inverse of −367 ≡ 2753 is 17: a negative representative is reduced first');

  eq(modpow(7n, 128n, 13n), 3n, '7^128 mod 13 = 3 (lesson 8 body)');
  eq(modpow(3n, 200n, 50n), 1n, '3^200 mod 50 = 1 (lesson 8 worked example)');
  eq(modpow(5n, 117n, 19n), 1n, '5^117 mod 19 (lesson 8 standard)');
  eq(modpow(7n, 100n, 10n), 1n, '7^100 ends in 1 (lesson 7 worked example)');
  eq(modpow(7n, 1000n, 13n), 9n, '7^1000 mod 13 = 9 (lesson 11 body)');
  eq(modpow(3n, 1234567n, 100n), 87n, '3^1234567 mod 100 = 87 (lesson 11 worked example)');
  eq(modpow(2n, 1000000n, 77n), 23n, '2^1000000 mod 77 (lesson 11 standard) equals 2^40 mod 77');
  eq(modpow(2n, 40n, 77n), 23n, 'because the exponent reduces modulo φ(77) = 60');
  eq(modpow(2n, 10n, 7n), 2n, '2^10 mod 7 = 2, not the 1 that reducing the exponent mod 7 gives (lesson 11 mistake 1)');
  eq(modpow(-7n, 3n, 10n), 7n, 'a negative base is reduced into [0, m) first');
  eq(modpow(65n, 17n, 3233n), 2790n, '65^17 mod 3233 = 2790 (the textbook key)');
  eq(modpow(2790n, 2753n, 3233n), 65n, 'and 2790^2753 mod 3233 = 65 decrypts it');
  eq(modpow(9n, 7n, 143n), 48n, '9^7 mod 143 = 48 — the lesson-14 worked example, which once said 3');
  eq(modpow(48n, 103n, 143n), 9n, 'and 48^103 mod 143 = 9 decrypts it');
  eq(modpow(3n, 103n, 143n), 16n, 'the old ciphertext 3 would not have decrypted to 9');
  const mt = modpowTrace(7n, 128n, 13n, 64);
  eq(mt.result, 3n, 'the trace reaches the same answer as modpow');
  eq(mt.rows.length + ',' + mt.squarings + ',' + mt.mults, '8,7,1', '7^128: eight rows, seven squarings, one multiplication');
  eq(mt.rows.map((r) => r.power).join(','), '7,10,9,3,9,3,9,3', 'the powers 7, 10, 9, 3, 9, 3, 9, 3 the body lists');
  const mt2 = modpowTrace(3n, 200n, 50n, 64);
  eq(mt2.rows.map((r) => r.power).join(','), '3,9,31,11,21,41,31,11', 'the worked example\'s column: 3, 9, 31, 11, 21, 41, 31, 11');
  eq(mt2.rows.map((r) => (r.use ? 1 : 0)).join(''), '00010011', 'set bits at positions 3, 6 and 7');
  eq(mt2.squarings + ',' + mt2.mults + ',' + mt2.result, '7,3,1', 'seven squarings, three multiplications, result 1');
  eq(modpowTrace(5n, 117n, 19n, 64).squarings + ',' + modpowTrace(5n, 117n, 19n, 64).mults, '6,5', '5^117: six squarings, five set bits');
  eq(modpowTrace(7n, 2n ** 100n, 13n, 64).complete, false, 'a 101-bit exponent is reported as truncated at 64 rows');

  eq(isPrimeBig(2n), true, '2 is prime');
  eq(isPrimeBig(1n), false, '1 is not prime');
  eq(isPrimeBig(101n), true, '101 is prime (lesson 2: four divisions)');
  eq(isPrimeBig(149n), true, '149 is prime (lesson 2 quiz)');
  eq(isPrimeBig(561n), false, '561, a Carmichael number, is composite');
  eq(isPrimeBig(30031n), false, '2·3·5·7·11·13 + 1 is composite');
  eq(factorize(360n).map((pe) => pe.join('^')).join(','), '2^3,3^2,5^1', '360 = 2³·3²·5 (lesson 2 worked example)');
  eq(divisorCount(360n), 24n, '360 has 24 divisors');
  eq(divisorCount(2520n), 48n, '2520 has 48 divisors (lesson 2 standard)');
  eq(factorize(30031n).map((pe) => pe[0]).join(','), '59,509', '30031 = 59 · 509');
  eq(factorize(1071n).map((pe) => pe.join('^')).join(','), '3^2,7^1,17^1', '1071 = 3²·7·17');
  eq(factorize(1n).length, 0, '1 has no prime factors');
  eq(factorize(97n).map((pe) => pe.join('^')).join(','), '97^1', 'a prime is its own factorisation');
  eq(totient(7n), 6n, 'φ(7) = 6');
  eq(totient(9n), 6n, 'φ(9) = 6');
  eq(totient(12n), 4n, 'φ(12) = 4');
  eq(totient(15n), 8n, 'φ(15) = 8 (lesson 11 quiz)');
  eq(totient(35n), 24n, 'φ(35) = 24');
  eq(totient(100n), 40n, 'φ(100) = 40 (lesson 11 worked example)');
  eq(totient(77n), 60n, 'φ(77) = 60 (lesson 11 standard)');
  eq(totient(3120n), 768n, 'φ(3120) = 768');
  eq(totient(26n), 12n, 'φ(26) = 12, the affine multipliers');
  eq(totient(1n), 1n, 'φ(1) = 1');
  eq(modpow(7n, totient(13n), 13n), 1n, 'Fermat at the lesson-11 preset: 7^12 ≡ 1 (mod 13)');
  eq(modpow(2n, totient(4n), 4n), 0n, '2^φ(4) ≡ 0 (mod 4): the theorem needs a coprime base');

  const sun = crtPair(2n, 3n, 3n, 5n);
  eq(sun.x + ' mod ' + sun.lcm, '8 mod 15', 'x ≡ 2 (3), x ≡ 3 (5) gives 8 mod 15 (lesson 10 preset)');
  const sun2 = crtPair(8n, 15n, 2n, 7n);
  eq(sun2.x + ' mod ' + sun2.lcm, '23 mod 105', 'then with x ≡ 2 (7): Sun Tzu\'s 23 mod 105');
  const std = crtPair(crtPair(1n, 5n, 2n, 7n).x, 35n, 3n, 9n);
  eq(std.x + ' mod ' + std.lcm, '156 mod 315', 'the lesson-10 standard: 156 mod 315');
  const bad = crtPair(1n, 4n, 2n, 6n);
  eq(bad.x === null && bad.g === 2n, true, 'x ≡ 1 (4), x ≡ 2 (6) is inconsistent modulo gcd 2');
  const ok = crtPair(1n, 4n, 3n, 6n);
  eq(ok.x + ' mod ' + ok.lcm, '9 mod 12', 'x ≡ 1 (4), x ≡ 3 (6) is 9 modulo the lcm 12, not 24');
  eq(crtPair(1n, 2n, 3n, 4n).x, 3n, 'one modulus dividing the other');
  eq(crtPair(-1n, 4n, 5n, 6n).x, 11n, 'negative remainders are reduced first');
  {
    /* The construction the lab displays for coprime moduli must agree with the
       general solver: Σ aᵢMᵢyᵢ mod M. */
    const M = 15n, t1 = 2n * 5n * modinv(5n, 3n) % M, t2 = 3n * 3n * modinv(3n, 5n) % M;
    eq((t1 + t2) % M, sun.x, 'the displayed construction agrees with crtPair');
  }

  const g1 = lcgRun(5n, 3n, 8n, 0n, 9);
  eq(g1.seq.join(','), '0,3,2,5,4,7,6,1', 'a = 5, c = 3, m = 8 from 0: the lesson-12 body sequence');
  eq(g1.start + ',' + g1.period, '0,8', 'full period 8');
  const g2 = lcgRun(4n, 3n, 8n, 0n, 9);
  eq(g2.seq.join(',') + ' then ' + g2.next, '0,3,7 then 7', 'a = 4 collapses: 0, 3, 7, 7, …');
  eq(g2.start + ',' + g2.period, '2,1', 'period 1 after a tail of 2');
  const g3 = lcgRun(5n, 3n, 16n, 1n, 17);
  eq(g3.seq.join(','), '1,8,11,10,5,12,15,14,9,0,3,2,13,4,7,6', 'the worked example\'s good generator at m = 16');
  eq(g3.period, 16, 'period 16 — every value once');
  const g4 = lcgRun(6n, 3n, 16n, 1n, 17);
  eq(g4.seq.join(',') + ' then ' + g4.next + ',' + g4.period, '1,9 then 9,1', 'a = 6: 1, 9, 9, 9, … period 1');
  eq(hullDobell(5n, 3n, 16n).join(','), 'true,true,true', 'Hull–Dobell passes for (5, 3, 16)');
  eq(hullDobell(6n, 3n, 16n).join(','), 'true,false,false', 'and (6, 3, 16) fails the second and third: 2 ∤ 5 and 4 ∤ 5');
  eq(hullDobell(4n, 3n, 8n).join(','), 'true,false,false', '(4, 3, 8): a − 1 = 3 is divisible by neither 2 nor 4');
  eq(hullDobell(21n, 1n, 100n).join(','), 'true,true,true', '(21, 1, 100) passes: a full-period generator for the standard');
  eq(lcgRun(21n, 1n, 100n, 0n, 101).period, 100, 'and it does have period 100');
  eq(hullDobell(5n, 3n, 7n).join(','), 'true,false,true', 'm = 7: the third condition is vacuous, the second fails');
  eq(lcgRun(5n, 3n, 7n, 0n, 8).period + ',' + lcgRun(5n, 3n, 7n, 1n, 8).period, '6,1',
     'so the period depends on the seed: 6 from 0, and 1 from the fixed point 1');

  const af = affineMap(5n, 8n, 26n);
  eq(af.map[7], 17n, 'H = 7 → 17 = R under (5, 8) (lesson 13 body)');
  eq(af.distinct + ',' + af.inv, '26,21', 'all 26 letters distinct, a⁻¹ = 21');
  eq((((17n - 8n) * 21n) % 26n + 26n) % 26n, 7n, 'D(17) = 21·(17 − 8) ≡ 7 = H');
  const af2 = affineMap(15n, 9n, 26n);
  eq(af2.map[4] + ',' + af2.map[19], '17,8', 'the recovered key (15, 9) sends E → R and T → I (lesson 13 worked example)');
  const af3 = affineMap(3n, 24n, 26n);
  eq(af3.map[4] + ',' + af3.map[19], '10,3', 'the standard\'s key (3, 24) sends E → K and T → D');
  const af13 = affineMap(13n, 0n, 26n);
  eq(af13.distinct + ',' + af13.inv, '2,null', 'a = 13 gives two outputs and no inverse');
  eq(affineMap(2n, 5n, 26n).distinct, 13, 'an even multiplier gives thirteen outputs');
}

// ---------------------------------------------------------------- graphs
console.log('graph algorithms (course 7 workbench)');
{
  /* Every course-7 lesson renders through one workbench, and the panels quote
     what it prints at their presets: distances, visit orders, Kruskal's
     decisions, the clique bound, the planarity counts. The functions below
     are the shipped ones, extracted from graph.py. The case that motivated
     this section: lesson 8's panel promised that BFS and DFS draw different
     trees on a preset that was itself a tree, and nothing could have said so. */
  eval(graphBlock('GRAPH_JS'));
  const L = (a) => a.map((v) => v + 1).join(' ');
  const S = (a) => '{' + L(a) + '}';
  const tree = (parent) => parent.map((p, v) => (p === -1 ? null : (p + 1) + '-' + (v + 1))).filter(Boolean).join(',');
  function load(preset, n) { N = n; useLessonWeights = false; A = PRESETS[preset](n); }
  function custom(n, list) { LESSON = lessonFrom(list); useLessonWeights = true; N = n; A = PRESETS.lesson(n); }
  const degs = () => { const d = []; for (let v = 0; v < N; v += 1) d.push(degree(v)); return d.join(''); };

  load('complete', 5);
  eq(edges().length, 10, 'K5 has 10 edges (lesson 1 preset)');
  eq(degs(), '44444', 'every degree 4');
  load('bipartite', 6);
  eq(edges().length + ',' + degs(), '9,333333', 'K_{3,3}: 9 edges, every degree 3');
  load('cycle', 6);
  eq(edges().length + ',' + degs(), '6,222222', 'C6: 6 edges, every degree 2');

  custom(8, [[1, 2], [1, 3], [1, 5], [2, 4], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 7], [6, 8], [7, 8]]);
  eq(degs() + ',' + edges().length, '33333333,12', 'Q3 (lesson 2 preset): eight vertices of degree 3, twelve edges');
  eq(twoColour().conflict, null, 'and Q3 is bipartite');
  eq(hamilton().circuit !== null, true, 'and has a Hamilton circuit');

  load('cycle', 4);
  eq(JSON.stringify(matrixPower(2)), '[[2,0,2,0],[0,2,0,2],[2,0,2,0],[0,2,0,2]]', 'A² of C4 (lesson 3 worked example)');
  eq(matrixPower(3)[0][3] + ',' + triangles(), '4,0', 'A³[1][4] = 4 and no triangle');
  load('petersen', 6);
  eq(triangles() + ',' + edges().length, '2,7', 'two triangles joined: 2 triangles, 7 edges');

  custom(7, [[1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]);
  eq(componentsOf().map(S).join(' '), '{1 2 3 4} {5 6} {7}', 'lesson 4 worked example: three components');
  {
    const c = cuts();
    eq(c.bridges.map((b) => L(b.edge)).join(','), '3 4,5 6', 'bridges 3–4 and 5–6');
    eq(L(c.cutVertices), '3', 'the one cut vertex is 3');
    eq(c.bridges[0].sides.map(S).join(' '), '{1 2 3} {4}', 'removing 3–4 separates {1, 2, 3} from {4}');
    eq(componentsOf(2).length, 4, 'deleting vertex 3 leaves four components');
  }
  load('tree', 7);
  eq(cuts().bridges.length + ',' + L(cuts().cutVertices), '6,1 2 3', 'on the tree preset every edge is a bridge and every internal vertex a cut vertex');
  load('cycle', 6);
  eq(cuts().bridges.length + ',' + cuts().cutVertices.length, '0,0', 'a cycle has no bridge and no cut vertex');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]);
  eq(degs() + ',' + componentsOf().length, '222222,2', 'two disjoint triangles (lesson 5 preset): 2-regular, two components');
  load('cycle', 6);
  eq(degs() + ',' + componentsOf().length, '222222,1', 'C6: the same degrees, one component');

  load('cycle', 6);
  eq(twoColour().colour.join(''), '010101', 'C6 two-coloured by parity: X = {1, 3, 5}');
  load('cycle', 5);
  eq(L(twoColour().conflict), '3 4', 'C5: the conflict is at vertices 3 and 4 (lesson 6 worked example)');
  load('cycle', 6); link(A, 0, 2);
  eq(twoColour().conflict !== null, true, 'C6 plus the chord 1–3 is not bipartite');
  load('cycle', 6); link(A, 0, 3);
  eq(twoColour().conflict, null, 'C6 plus the chord 1–4 still is');

  load('cycle', 6);
  eq(L(hamilton().circuit), '1 2 3 4 5 6', 'C6 has a Hamilton circuit (lesson 7 preset)');
  A[0][1] = 0; A[1][0] = 0;
  eq(degs().split('').map((d, i) => (d % 2 ? i + 1 : null)).filter(Boolean).join(','), '1,2', 'minus 1–2: the odd vertices are 1 and 2');
  eq(L(hamilton().path) + '|' + hamilton().circuit, '1 6 5 4 3 2|null', 'a Hamilton path and no circuit');

  custom(6, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6]]);
  {
    const b = bfs(0), d = dfs(0);
    eq(b.dist.join(' '), '0 1 1 2 3 4', 'lesson 8 worked example: BFS distances');
    eq(L(b.order), '1 2 3 4 5 6', 'BFS order');
    eq(tree(b.parent), '1-2,1-3,2-4,4-5,5-6', 'BFS tree edges');
    eq(L(d.order), '1 2 4 3 5 6', 'DFS order');
    eq(tree(d.parent), '1-2,4-3,2-4,4-5,5-6', 'DFS tree edges: 4–3 is a tree edge, so 3–1 is the back edge');
  }
  load('tree', 7);
  eq(tree(bfs(0).parent) === tree(dfs(0).parent), true, 'on a tree BFS and DFS draw the same tree');

  custom(4, [[1, 2, 10], [1, 3, 3], [3, 2, 2], [2, 4, 1], [3, 4, 9]]);
  eq(weight(0, 1) + ',' + weight(1, 2), '10,2', 'the lesson preset carries its own weights');
  {
    const r = dijkstra(0);
    eq(r.dist.join(' '), '0 5 3 6', 'lesson 9 worked example: s = 0, a = 5, b = 3, t = 6');
    let v = 3; const route = []; while (v !== -1) { route.unshift(v); v = r.parent[v]; }
    eq(L(route), '1 3 2 4', 'route s → b → a → t');
    eq(bfs(0).dist[3], 2, 'against a fewest-edge distance of 2');
  }
  useLessonWeights = false;
  eq(weight(0, 1), 5, 'off the lesson preset the formula weight returns');
  load('complete', 6);
  eq(dijkstra(0).dist[5] + ',' + bfs(0).dist[5], '3,1', 'on K6 the cheapest route 1 → 6 is the direct edge');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]);
  eq(componentsOf().length + ',' + edges().length + ',' + (edges().length === N - componentsOf().length), '2,5,false',
     'lesson 10 graph C: two components, five edges, not acyclic');
  load('path', 6);
  eq(componentsOf().length + ',' + edges().length + ',' + degs(), '1,5,122221', 'graph A is a path with leaves 1 and 6');

  load('tree', 7);
  {
    const o = rootedOrders(0);
    eq(L(o.pre), '1 2 4 5 3 6 7', 'preorder on the tree preset (lesson 11)');
    eq(L(o.ino), '4 2 5 1 6 3 7', 'inorder');
    eq(L(o.post), '4 5 2 6 7 3 1', 'postorder');
    eq(L(o.level), '1 2 3 4 5 6 7', 'level order');
    eq(o.treeEdges + ',' + o.reached, '6,7', 'six tree edges reach all seven');
  }
  load('star', 7);
  eq(rootedOrders(0).ino + ',' + (rootedOrders(0).tooMany + 1), 'null,1', 'on a star inorder is undefined and vertex 1 is why');
  load('cycle', 5);
  eq(L(rootedOrders(0).pre) + ',' + rootedOrders(0).treeEdges, '1 2 3 4 5,4', 'on C5 the orders are those of the DFS spanning tree, one edge left out');

  custom(5, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [1, 5, 5], [1, 3, 6], [2, 4, 7]]);
  {
    const k = kruskal();
    eq(k.total + ',' + k.chosen.length, '10,4', 'lesson 12 worked example: total 10, four edges');
    eq(k.considered.map((c) => L(c[0].slice(0, 2)) + (c[1] ? '+' : '-')).join(','), '1 2+,2 3+,3 4+,4 5+,1 5-,1 3-,2 4-',
       'AB, BC, CD, DE taken; AE, AC, BD rejected, in weight order');
    eq(dijkstra(0).dist[4], 5, 'Dijkstra 1 → 5 on the same graph is the rejected edge of weight 5');
  }
  load('complete', 6);
  eq(kruskal().total + ',' + kruskal().chosen.length, '12,5', 'Kruskal on K6 with the formula weights');
  load('petersen', 6); A[0][3] = 0; A[3][0] = 0;
  eq(kruskal().chosen.length, 4, 'a disconnected graph gives a spanning forest with n − c edges');

  custom(5, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]]);
  eq(greedyColour().join(''), '01201', 'lesson 13 worked example: greedy colours 1, 2, 3, 1, 2');
  eq(cliqueNumber().size + ',' + S(cliqueNumber().vertices), '3,{1 2 3}', 'clique number 3 on the triangle');
  eq(Math.max(...degs().split('').map(Number)), 3, 'Δ = 3, so the greedy bound is 4');
  custom(6, [[1, 4], [1, 6], [3, 2], [3, 6], [5, 2], [5, 4]]);
  eq(Math.max(...greedyColour()) + 1 + ',' + twoColour().conflict + ',' + cliqueNumber().size, '3,null,2',
     'the bipartite trap: greedy uses three colours on a bipartite graph');
  load('cycle', 5);
  eq(Math.max(...greedyColour()) + 1 + ',' + cliqueNumber().size, '3,2', 'C5: greedy 3, clique 2, the odd cycle supplies the third');

  load('complete', 5);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.E + ',' + p.bound, 'bound,10,9', 'K5: 10 > 3·5 − 6 = 9 (lesson 14 preset)');
  }
  load('bipartite', 6);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.triangles + ',' + p.bound + ',' + p.bound2, 'bound2,0,12,8', 'K_{3,3}: passes 12, triangle-free, fails 8');
  }
  load('complete', 4);
  eq(planarity().verdict + ',' + planarity().E + ',' + planarity().bound, 'planar,6,6', 'K4: 6 ≤ 6 and planar');
  load('petersen', 6);
  eq(planarity().verdict, 'planar', 'seven edges: no subdivision of K5 or K_{3,3} fits');
  custom(8, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]);
  eq(planarity().verdict + ',' + S(planarity().k5), 'k5,{1 2 3 4 5}', 'K5 on eight vertices passes both bounds and is caught as a subgraph');
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]);
  {
    const p = planarity();
    eq(p.verdict + ',' + S(p.k33.left) + ',' + S(p.k33.right), 'k33,{1 2 3},{4 5 6}', 'K_{3,3} plus an isolated vertex passes 10 and is caught as a subgraph');
  }
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 7], [7, 6]]);
  eq(planarity().verdict, 'open', 'a subdivided K_{3,3} passes the bounds, has no K_{3,3} subgraph, and is reported open, not planar');
  load('cycle', 4); link(A, 0, 2); link(A, 1, 3);
  eq(planarity().verdict + ',' + planarity().triangles, 'planar,4', 'K4 built by hand: four triangles, planar');
}

// ------------------------------------------------------------ algorithms
console.log('algorithm counts and the witness verdict (course 8 lab)');
{
  /* Every course-8 lesson renders through one lab, and its panels quote what
     it prints: comparison counts, the loop-nest sums, the invariant trace,
     the dynamic array's copies, the master theorem's case, the amounts where
     greedy fails. The functions below are the shipped ones, extracted from
     algorithms.py. The case that motivated this section: the witness mode
     searched C ≤ 1000 over n ≤ 64 and reported n² = O(n) with C = 100,
     contradicting the lesson's own example directly above it. */
  eval(algoBlock('ALGO_JS'));
  const F = { one: 0, log: 1, n: 2, nlogn: 3, n2: 4, n3: 5, exp: 6, fact: 7, poly: 8, hundred: 9 };
  const W = (f, g) => { const w = witnessSearch(F[f], F[g], 16); return w ? w.C + ',' + w.k : 'none'; };
  eq(bigO(F.poly, F.n2) + ':' + W('poly', 'n2'), 'true:4,13', '3n² + 5n + 100 = O(n²) with C = 4, k = 13 (lesson 4 preset)');
  eq(bigO(F.n, F.n2) + ':' + W('n', 'n2'), 'true:1,1', 'n = O(n²) with C = 1, k = 1 (lesson 4 quiz)');
  eq(bigO(F.n2, F.n), false, 'n² ≠ O(n) — the lesson 4 example the old search contradicted');
  eq(bigO(F.nlogn, F.n), false, 'n log n ≠ O(n), though a search to n = 10⁹ would find C = 50');
  eq([bigO(F.n3, F.n2), bigO(F.log, F.one), bigO(F.fact, F.exp), bigO(F.exp, F.n3)].join(','), 'false,false,false,false',
     'n³ vs n², log n vs 1, n! vs 2ⁿ, 2ⁿ vs n³ are all false');
  eq(bigO(F.one, F.log) + ':' + W('one', 'log'), 'true:1,2', '1 = O(log n) needs k = 2 because log 1 = 0');
  eq(bigO(F.exp, F.fact) + ':' + W('exp', 'fact'), 'true:1,4', '2ⁿ = O(n!) from n = 4');
  eq(W('n3', 'exp'), '1,10', 'n³ ≤ 2ⁿ from n = 10');
  eq(W('hundred', 'n'), '100,1', '100n = O(n) with C = 100');
  {
    let bad = 0;
    for (let f = 0; f < FUNCS.length; f += 1) for (let g = 0; g < FUNCS.length; g += 1) if (bigO(f, g) && !witnessSearch(f, g, 16)) bad += 1;
    eq(bad, 0, 'every true relation among the ten functions has a witness in the grid');
  }
  eq(ratioAt(F.n2, F.n, 1000000), 1000000, 'the ratio n²/n at 10⁶ is 10⁶ — the disproof column');

  const S = (n, kind) => bubbleSort(makeArray(n, kind)) + ',' + insertionSort(makeArray(n, kind)) + ',' + mergeSort(makeArray(n, kind));
  eq(S(16, 'shuffle'), '120,77,48', 'n = 16 shuffled: bubble 120, insertion 77, merge 48 (lesson 6 worked example)');
  eq(insertionSort(makeArray(16, 'sorted')) + ',' + insertionSort(makeArray(16, 'reverse')), '15,120', 'insertion sort: 15 on sorted, 120 on reversed input');
  eq(S(24, 'shuffle'), '276,174,82', 'n = 24 shuffled');
  eq(S(1000, 'shuffle'), '499500,235149,7387', 'n = 1000: bubble 499 500 = n(n−1)/2, merge 7 387');
  eq(makeArray(16, 'shuffle').join(' '), '8 16 9 2 12 6 3 15 14 1 5 11 10 4 13 7', 'the shuffle is the same permutation for every reader');
  eq(linearSearch(makeArray(16, 'sorted'), 16) + ',' + binaryWorst(16), '16,5', 'linear 16, binary ⌊log₂16⌋ + 1 = 5');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (binaryWorst(n) !== ilog2(n) + 1) ok = false;
    eq(ok, true, 'binary search worst case is ⌊log₂ n⌋ + 1 for every n to 64');
  }
  eq(binaryWorst(1000), 10, 'and 10 at n = 1000');

  const nest = countNests(16);
  eq([nest.A, nest.B, nest.C, nest.D].join(','), '4096,136,64,816', 'lesson 5 nests at n = 16: n³, n(n+1)/2, n⌊log₂n⌋, n(n+1)(n+2)/6');
  {
    let ok = true;
    for (let n = 1; n <= 64; n += 1) { const r = countNests(n); if (r.A !== r.predA || r.B !== r.predB || r.C !== r.predC || r.D !== r.predD) ok = false; }
    eq(ok, true, 'every nest equals its formula for every n to 64');
  }

  const p = powerTrace(3, 13);
  eq([p.rows.every((r) => r.ok), p.rows.length, p.squarings, p.mults, p.value].join(','), 'true,5,4,3,1594323',
     'POWER(3, 13): the invariant holds on all five rows, 4 squarings, 3 multiplications, 3¹³ (lesson 2 preset)');
  eq(powerTrace(3, 1000).squarings + ',' + powerTrace(3, 1000).mults, '10,6', 'x¹⁰⁰⁰: 10 squarings and 6 multiplications against 999');
  eq(powerTrace(2, 64).value, 18446744073709551616n, '2⁶⁴ exactly, beyond double precision');

  const d16 = dynamicArray(16, 'double');
  eq([d16.copies, d16.total, d16.worst, d16.worstAt].join(','), '15,31,9,9', 'doubling, 16 inserts: 15 copies, total 31, worst insertion 9 at element 9 (lesson 8 worked example)');
  eq(d16.events.map((e) => e.at + ':' + e.from + '>' + e.to).join(' '), '2:1>2 3:2>4 5:4>8 9:8>16', 'resizes at inserts 2, 3, 5, 9');
  const d17 = dynamicArray(17, 'double');
  eq([d17.copies, d17.total, d17.amortised < 3].join(','), '31,48,true', '17 inserts: total 48, above 2n and still under 3n');
  eq(dynamicArray(16, 'one').copies, 120, 'growing by one copies 1 + ⋯ + 15 = 120');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (dynamicArray(n, 'double').amortised >= 3 || dynamicArray(n, 'half').amortised >= 4) ok = false;
    eq(ok, true, 'doubling stays under 3 and ×1.5 under 4 per insertion for every n to 64');
  }

  const M = (a, b, d) => { const m = masterCase(a, b, d); return m.which + ':' + m.result; };
  eq(M(4, 2, 1), '3:Θ(n^2)', 'lesson 7 baseline 4T(n/2) + n: case 3, Θ(n²)');
  eq(M(4, 2, 0), '3:Θ(n^2)', 'faster combining, d = 0: still Θ(n²)');
  eq(M(3, 2, 1), '3:Θ(n^log_2 3) ≈ Θ(n^1.585)', 'one fewer subproblem: Θ(n^1.585)');
  eq(M(9, 3, 2), '2:Θ(n^2 log n)', 'the standard\'s 9T(n/3) + n²: balanced');
  eq([M(2, 2, 1), M(1, 2, 0), M(2, 4, 1), M(7, 2, 2)].join('|'), '2:Θ(n log n)|2:Θ(log n)|1:Θ(n)|3:Θ(n^log_2 7) ≈ Θ(n^2.807)',
     'merge sort, binary search, course 3 lesson 11\'s last row, Strassen');

  eq(greedyFailures([1, 3, 4], 24).join(','), '6,10,14,18,22', 'greedy with {1, 3, 4} fails first at 6 (lesson 9 preset)');
  eq(greedyCoins([1, 3, 4], 6).picks.join('+') + ' vs ' + dpCoins([1, 3, 4], 6).picks.join('+'), '4+1+1 vs 3+3', 'at 6: 4 + 1 + 1 against 3 + 3');
  eq(dpCoins([1, 3, 4], 8).table.join(' '), '0 1 2 1 1 2 2 2 2', 'the lesson 10 table best[0..8]');
  eq(greedyFailures([1, 5, 10, 25], 99).length, 0, 'with {1, 5, 10, 25} greedy is optimal for every amount to 99');
}


// ---------------------------------- capacity, latency, queues and availability
console.log('system design: exact capacity, queueing and availability');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('HARMONIC_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
       + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS') + sysdBlock('STREAM_JS')
       + sysdBlock('REPLAY_JS') + sysdBlock('AVAIL_JS') + sysdBlock('APPROX_JS'));

  /* Zipf popularity: the cache hit rate is a ratio of harmonics, and it is the
     ratio that makes a small cache of a skewed workload worth having. */
  eq(Rtext(harmonic(4, 1)), '25/12', 'H(4,1) = 1 + 1/2 + 1/3 + 1/4');
  eq(Rtext(harmonic(3, 2)), '49/36', 'H(3,2) = 1 + 1/4 + 1/9');
  eq(Rtext(zipfHit(1, 4, 1)), '12/25', 'the most popular of four keys, s = 1');
  eq(Rtext(zipfHit(4, 4, 1)), '1', 'caching everything hits everything');

  /* Nearest rank, so a percentile is a value some request actually took. */
  eq(percentileRank(10, R(9n, 10n)), 9, 'p90 of ten samples is the 9th');
  eq(percentileRank(10, R(99n, 100n)), 10, 'p99 of ten samples is the 10th, not an interpolation');
  eq(percentileRank(100, R(1n, 2n)), 50, 'p50 of a hundred');
  const lat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100];
  eq(percentile(lat, R(9n, 10n)), 9, 'the p90 of that sample');
  eq(Rtext(empiricalCdf(lat, 5)), '1/2', 'P(X <= 5)');

  /* A latency budget adds distributions; fan-out takes their maximum. */
  const coin = [[0, R(1n, 2n)], [1, R(1n, 2n)]];
  eq(pmfConvolve(coin, coin).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:1/2 2:1/4', 'two independent stages add by convolution');
  eq(Rtext(pmfMean(pmfConvolve(coin, coin))), '1', 'and their means add');
  eq(pmfMax(coin, 2).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:3/4', 'the max of two: the tail is what fan-out costs');
  eq(Rtext(pmfTail(pmfConvolve(coin, coin), 0)), '3/4', 'P(sum > 0)');

  /* M/M/1 from the cut equations. */
  const q = mm1(R(1n, 1n), R(2n, 1n));
  eq(Rtext(q.rho) + ' ' + Rtext(q.L) + ' ' + Rtext(q.W) + ' ' + Rtext(q.Lq),
     '1/2 1 1 1/2', 'M/M/1 at lam = 1, mu = 2');
  eq(mm1(R(3n, 1n), R(2n, 1n)).stable, false, 'rho >= 1 does not settle');
  /* The knee: the last tenth of utilisation costs more than the first nine. */
  eq(Rtext(mm1(R(9n, 10n), R(1n, 1n)).L), '9', 'rho = 0.9 queues 9');
  eq(Rtext(mm1(R(99n, 100n), R(1n, 1n)).L), '99', 'rho = 0.99 queues 99');

  /* Erlang C must agree with M/M/1 at one server -- and s = 1 is exactly the
     case that cannot distinguish a from rho, so s = 2 and 3 are checked too. */
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).pWait), '1/2', 'Erlang C at s = 1 is rho');
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).L), Rtext(q.L), 'and its L is M/M/1 L');
  const e2 = erlangC(R(1n, 1n), R(1n, 1n), 2);
  eq(Rtext(e2.p0) + ' ' + Rtext(e2.pWait) + ' ' + Rtext(e2.L), '1/3 1/3 4/3', 'M/M/2 at a = 1');
  const e3 = erlangC(R(2n, 1n), R(1n, 1n), 3);
  eq(Rtext(e3.p0) + ' ' + Rtext(e3.pWait), '1/9 4/9', 'M/M/3 at a = 2');
  /* Pooling: one queue of two servers beats two queues of one. */
  eq(Rcmp(erlangC(R(1n, 1n), R(1n, 1n), 2).Wq, mm1(R(1n, 2n), R(1n, 1n)).Wq), -1,
     'a pooled M/M/2 waits less than two separate M/M/1s at the same load');

  /* A bounded queue is stable at any load, and Little's law must use the
     EFFECTIVE arrival rate, not the offered one. */
  const fk = mm1k(R(1n, 1n), R(1n, 1n), 3);
  eq(Rtext(fk.blocking), '1/4', 'M/M/1/3 at rho = 1 blocks a quarter');
  eq(Rtext(fk.L), '3/2', 'and holds 3/2 on average');
  eq(Rtext(fk.lamEff), '3/4', 'the effective rate is lam(1 - pK)');

  /* Availability composes three ways, and the three must agree where they meet. */
  eq(Rtext(availSeries([R(9n, 10n), R(9n, 10n)])), '81/100', 'series multiplies down');
  eq(Rtext(availParallel([R(9n, 10n), R(9n, 10n)])), '99/100', 'parallel multiplies up');
  const three = [R(9n, 10n), R(9n, 10n), R(9n, 10n)];
  eq(Rtext(availKofN(R(9n, 10n), 3, 3)), Rtext(availSeries(three)), 'n-of-n is series');
  eq(Rtext(availKofN(R(9n, 10n), 1, 3)), Rtext(availParallel(three)), '1-of-n is parallel');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'majority of three fair coins');
  /* Ten 99.9% dependencies in series are 99.0%, not "as good as the weakest". */
  const ten = []; for (let i = 0; i < 10; i += 1) ten.push(R(999n, 1000n));
  near(Number(Rdec(availSeries(ten), 6)), 0.990045, 1e-6, 'ten 99.9% dependencies give 99.0%');

  /* Retries: the geometric sum, and what it costs when p is high. */
  eq(Rtext(retryAttempts(R(1n, 2n), 2)), '7/4', 'two retries at p = 1/2 cost 7/4 attempts');
  eq(Rtext(retrySuccess(R(1n, 2n), 2)), '7/8', 'and succeed 7/8 of the time');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'at p = 0.9 the amplification approaches r + 1');

  /* The slotted queue is NOT M/M/1, and this is the assertion that stops a
     lesson claiming the continuous formula is "checked against the simulation".
     At p = 2/5, q = 1/2 the exact slotted mean is 12/5; rho/(1 - rho) is 4. */
  const slot = geoGeo1(R(2n, 5n), R(1n, 2n));
  eq(Rtext(slot.ratio), '2/3', 'Geo/Geo/1 ratio p(1-q)/(q(1-p))');
  eq(Rtext(slot.p0), '1/5', 'and its empty probability');
  eq(Rtext(slot.L), '12/5', 'the EXACT slotted mean');
  eq(Rtext(slot.rho), '4/5', 'at the same utilisation');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'where the continuous formula says 4');
  eq(Rcmp(slot.L, mm1(R(4n, 5n), R(1n, 1n)).L), -1,
     'the slotted mean is strictly below M/M/1 -- the two agree only in the limit');
  /* A second point with q != 1/2. At q = 1/2, (1 - q) = q and the ratio
     p(1-q)/(q(1-p)) is indistinguishable from pq/(q(1-p)) -- so one point
     cannot check the formula at all. */
  const slot2 = geoGeo1(R(1n, 4n), R(1n, 3n));
  eq(Rtext(slot2.ratio), '2/3', 'Geo/Geo/1 ratio at p = 1/4, q = 1/3');
  eq(Rtext(slot2.p0) + ' ' + Rtext(slot2.L), '1/4 9/4', 'its empty probability and exact mean');
  eq(Rtext(mm1(R(3n, 4n), R(1n, 1n)).L), '3', 'against 3 from the continuous formula');

  /* Little's Law as an identity about a trace, which is how it is proved here.
     Three customers, each in the system 2 slots, over a horizon of 6:
     area 6, L = 1, lambda = 1/2, W = 2, and L = lambda*W exactly. */
  const tr = littleFromTrace([0, 2, 4], [2, 4, 6]);
  eq(Rtext(tr.L) + ' ' + Rtext(tr.lambda) + ' ' + Rtext(tr.W), '1 1/2 2', 'L, lambda, W from the trace');
  eq(Rtext(tr.L), Rtext(Rmul(tr.lambda, tr.W)), 'L = lambda * W, exactly, with no model');
  eq(occupancyTrace([0, 2, 4], [2, 4, 6], 6).join(''), '111111', 'N(t) is 1 throughout');
  /* The same three customers, arriving together instead of spread out: the same
     total time in system over a third of the horizon, so L triples and W does
     not move. That is the identity doing work. */
  const tr2 = littleFromTrace([0, 0, 0], [2, 2, 2]);
  eq(Rtext(tr2.L) + ' ' + Rtext(tr2.W), '3 2', 'stacked arrivals triple L and leave W alone');
  eq(Rtext(tr2.L), Rtext(Rmul(tr2.lambda, tr2.W)), 'and the identity still holds');

  /* A seeded stream: same seed, same values, or a reader cannot check a lab. */
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     '1103527590,377401575,662824084', 'the stream is these values, not merely repeatable');
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','), 'and the same on a second call');
  const fair = [[1, R(1n, 2n)], [2, R(1n, 2n)]];
  eq(sampleFromPmf(fair, R(1n, 4n)), 1, 'inverse transform below the first mass');
  eq(sampleFromPmf(fair, R(3n, 4n)), 2, 'and above it');
  /* The boundary: u exactly at the cumulative mass. Half-open [lo, hi) is what
     keeps the sampler's frequencies equal to the pmf, so u = 1/2 is the SECOND
     value, and a <= here would bias every sampled distribution low. */
  eq(sampleFromPmf(fair, R(1n, 2n)), 2, 'u exactly on the boundary falls to the second value');
  eq(sampleFromPmf(fair, R(0n, 1n)), 1, 'and u = 0 to the first');

  /* Ceiling and floor, because 3.2 machines is four. */
  eq(Rceil(R(16n, 5n)), 4n, 'ceil(3.2) = 4 -- the sizing answer');
  eq(Rfloor(R(16n, 5n)), 3n, 'floor(3.2) = 3');
  eq(Rceil(R(4n, 1n)), 4n, 'an exact integer does not round up');
  eq(Rfloor(R(-16n, 5n)), -4n, 'floor of a negative goes down, not toward zero');
  eq(Rceil(R(-16n, 5n)), -3n, 'and ceil goes up');
  /* The case the sign guard exists for: an EXACT negative integer must not be
     pushed a further step. Without it -4 floors to -5. */
  eq(Rfloor(R(-4n, 1n)), -4n, 'floor of an exact negative integer is itself');
  eq(Rceil(R(-4n, 1n)), -4n, 'and so is its ceiling');

  /* Replacement policies on a trace, and the bound the lesson rests on.
     Trace A B C A B D A B C D, three slots. */
  const tr3 = ['A','B','C','A','B','D','A','B','C','D'];
  const opt = replayPolicy(tr3, 3, 'opt'), lru = replayPolicy(tr3, 3, 'lru');
  /* Exact rates, not merely an ordering: "OPT >= LRU" holds for several WRONG
     policies too, including one that evicts the nearest-future key. */
  eq(Rtext(opt.rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(lru.rate), '2/5', 'LRU gets 4');
  eq(Rcmp(opt.rate, lru.rate) > 0, true, 'and the bound is strict on this trace');
  eq(replayPolicy(tr3, 10, 'lru').misses, 4, 'a cache big enough misses only the compulsory four');
  eq(Rtext(replayPolicy(['A','A','A','A'], 1, 'lru').rate), '3/4', 'one key, one slot');

  /* The four places this subject rounds, and only these. */
  near(expNegApprox(1, 1e-15), Math.exp(-1), 1e-12, 'e^-1 by series');
  near(expNegApprox(5, 1e-15), Math.exp(-5), 1e-12, 'e^-5 by series');
  /* The arguments that expose a cancelling implementation. Summing the
     ALTERNATING series for e^-x is exact at 1 and 5 -- which is why the first
     version of this test passed -- and then 0.4% out at 17, 173% out at 20, and
     NEGATIVE past 21. A probability cannot be negative, so these are pinned by
     relative error rather than absolute, at arguments where the absolute error
     of a badly wrong answer is still tiny. */
  for (const x of [10, 12, 15, 17, 20, 21, 25, 40]) {
    const got = expNegApprox(x, 1e-15), want = Math.exp(-x);
    eq(got > 0, true, 'e^-' + x + ' is positive');
    eq(Math.abs(got - want) / want < 1e-10, true,
       'e^-' + x + ' is right to a relative 1e-10, not merely a small absolute error');
  }
  near(expNegApprox(-2, 1e-15), Math.exp(2), 1e-10, 'a negative argument gives e^|x|');
  near(standardErrorApprox(0.5, 100), 0.05, 1e-12, 'the standard error of a proportion');
  /* 1.44*log2(1/0.01) = 9.57 bits per key is the canonical 1% figure, and the
     rate it actually delivers at k = 7 is what the lesson quotes. */
  near(bloomApprox(9585, 1000, 7), 0.01004, 1e-4, 'a Bloom filter at 9.585 bits per key is ~1%');
  /* 9.585, not the 9.57 a textbook quotes: that figure uses 1.44 in place of
     1/ln2 = 1.4427. The lesson should give the exact form and note the rounding. */
  near(bitsPerKeyApprox(0.01), 9.585, 0.001, '1% costs 9.585 bits per key');
  near(sqrtApprox(R(2n, 1n), 1e-15), Math.SQRT2, 1e-12, 'a root that rounds, and says so');
  near(sqrtApprox(R(9n, 4n), 1e-15), 1.5, 1e-12, 'agreeing with Rsqrt where Rsqrt is exact');
  near(harmonicApprox(1000000, 1), 14.392727, 1e-4, 'the Zipf normaliser past where exact is readable');
}

// ------------------------------------- system design C2: latency and the tail
/* The `latency` kit's own arithmetic, on the numbers its eleven lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims. */
console.log('system design: latency, percentiles and the tail');
{
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('PERCENTILE_JS')
       + sysdBlock('PMF_JS') + sysdBlock('APPROX_JS') + latencyBlock('LATENCY_JS'));

  /* Rfixed exists because Rdec cannot do this. 0.999^693 has a 2079-digit
     numerator; Number() of it is Infinity and Infinity/Infinity is NaN, so the
     fan-out lesson at p99.9 would print NaN. Long division in BigInt instead. */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'a third to six places');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'two thirds, rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rfixed(R(7n, 1n), 0), '7', 'no places asked for, no decimal point');
  eq(Rfixed(Rpow(R(999n, 1000n), 693), 6), '0.499900', '0.999^693, which Number cannot hold');
  eq(String(Number(Rpow(R(999n, 1000n), 693).n)), 'Infinity', 'and this is why Rdec would give NaN');
  eq(Rpct(R(1n, 400n), 4), '0.2500%', 'a probability as a percentage');

  /* L1 and L3: the two terms, and the size at which they cross. */
  eq(Rtext(transferMs(64000, 100)), '128/25', '64 kB over 100 Mbit/s is 5.12 ms');
  eq(Rtext(bdpBytes(100, 80)), '1000000', '100 Mbit/s x 80 ms holds exactly one megabyte');
  eq(Rtext(linkTimeMs(5, 80, 14000, 10)), '2056/5', '5 round trips at 80 ms plus 14 kB at 10 Mbit/s');
  eq(Rtext(crossoverBytes(5, 80, 10)), '500000', 'the bytes catch 5 round trips at 500 kB');
  /* The crossover for ONE round trip IS the bandwidth-delay product -- L1 and
     L3 are the same fact, and if these ever disagree one of the two is wrong. */
  eq(Rtext(crossoverBytes(1, 80, 100)), Rtext(bdpBytes(100, 80)), 'k = 1 crossover is the BDP');

  /* L2: the floor. c is exact by definition, so this is an exact fraction. */
  eq(Rtext(lightFloorMs(5585)), '8377500000/149896229', 'New York to London, exactly');
  eq(Rfixed(lightFloorMs(5585), 3), '55.889', 'which is the 56 ms the course quotes');
  eq(Rfixed(unexplainedMs(76, 5585), 3), '20.111', 'a measured 76 ms leaves 20 ms to explain');
  eq(Rcmp(unexplainedMs(40, 5585), R(0n, 1n)) < 0, true, 'a measurement under the floor goes negative');

  /* L4: the longest path, its slack, and the two edges the lesson toggles. */
  const dagT = [4, 18, 6, 22, 55, 12, 3];
  const dagE = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]];
  const base = dagSchedule(dagT, dagE);
  eq(base.length, 92, 'the critical path is 92 ms, not the 120 ms the stages total');
  eq(base.slack.join(','), '0,0,12,33,0,0,0', 'cache has 12 ms spare and enrich 33');
  eq(base.path.join('-'), '0-1-4-5-6', 'gateway, authz, db, render, respond');
  /* Speeding up an off-path stage changes nothing: enrich to 1 ms is still 92. */
  eq(dagSchedule([4, 18, 6, 1, 55, 12, 3], dagE).length, 92, 'making enrich instant saves nothing');
  eq(dagSchedule([4, 18, 6, 22, 55, 12, 2], dagE).length, 91, 'a critical stage saves its whole millisecond');
  /* Serialising the cache behind authz puts it ON the path and costs 6 ms. */
  const serial = dagSchedule(dagT, dagE.concat([[1, 2]]));
  eq(serial.length + ' ' + serial.slack[2], '98 0', 'authz -> cache moves cache onto the path');
  /* Making the db wait for the enrichment costs the whole 22 ms of it. */
  const after = dagSchedule(dagT, dagE.concat([[3, 4]]));
  eq(after.length + ' ' + after.path.join('-'), '114 0-1-3-4-5-6', 'enrich -> db reroutes the path');

  /* L5: the rank, the value it selects, and the mean that is neither. */
  const s5 = parseSample('12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420');
  eq(s5.length, 20, 'twenty measurements');
  eq(percentile(s5, R(1n, 2n)) + ' ' + percentile(s5, R(95n, 100n)) + ' ' + percentile(s5, R(99n, 100n)),
     '19 180 420', 'p50, p95 and p99 by nearest rank');
  eq(Rtext(sampleMean(s5)), '266/5', 'the mean is 53.2 ms');
  eq(countBelow(s5, sampleMean(s5)), 17, '17 of 20 requests are faster than the average');
  /* Nothing in the sample IS the mean, which is the lesson. */
  eq(s5.indexOf(53), -1, 'and no request took 53 ms');
  eq(parseSample('   '), 'null', 'an empty sample is refused rather than guessed at');

  /* L6: p^n, the break-even n, and the same number from pmfMax. */
  eq(Rfixed(Rpow(R(99n, 100n), 69), 6), '0.499837', '0.99^69 is just under a half');
  eq(fanoutBreakEven(R(99n, 100n), 20000), 69, 'a p99 becomes the median at a fan-out of 69');
  eq(fanoutBreakEven(R(9n, 10n), 20000), 7, 'a p90 at 7');
  eq(fanoutBreakEven(R(19n, 20n), 20000), 14, 'a p95 at 14');
  eq(fanoutBreakEven(R(999n, 1000n), 20000), 693, 'and a p99.9 at 693');
  /* 68 must NOT be the answer: at n = 68 the probability is still above a half,
     and an off-by-one here is the whole content of the lesson. */
  eq(Rcmp(Rpow(R(99n, 100n), 68), R(1n, 2n)) > 0, true, '68 calls are still better than even');
  const twoWay = pmfMax([[0, R(99n, 100n)], [1, R(1n, 100n)]], 69);
  eq(Rtext(twoWay[0][1]), Rtext(Rpow(R(99n, 100n), 69)), 'pmfMax agrees with p^n exactly');

  /* L7: the hedge. The preset is 100 measured calls as run lengths. */
  const hSpec = parsePmfSpec('10:40, 12:25, 15:15, 20:10, 30:5, 50:3, 120:1, 300:1');
  const hPmf = pmfFromSpec(hSpec);
  eq(expandSpec(hSpec).length, 100, 'the run lengths expand to a hundred calls');
  eq(pmfPercentile(hPmf, R(99n, 100n)) + ' ' + pmfPercentile(hPmf, R(95n, 100n))
     + ' ' + pmfPercentile(hPmf, R(1n, 2n)), '120 30 12', 'p99, p95 and p50 of the service');
  eq(Rtext(hedgeLoad(hPmf, 30)), '1/20', 'a hedge at the p95 costs 5% more traffic');
  eq(Rtext(Rpow(hedgeLoad(hPmf, 30), 2)), '1/400', 'and the tail past it is that squared');
  eq(Rtext(hedgedTail(hPmf, 30, 42)), '7/400', 'P(hedged > 42) = P(X > 42) P(X > 12)');
  eq(hedgedQuantile(hPmf, 30, R(99n, 100n)), 45, 'the hedged p99 is 45 ms, down from 120');
  eq(hedgedQuantile(hPmf, 30, R(1n, 2n)), 12, 'and the median does not move');
  /* Hedging at the median doubles the load, which is the misconception. */
  eq(Rtext(hedgeLoad(hPmf, 12)), '7/20', 'hedging at the p50 sends a backup for a third of requests');

  /* L8: percentiles do not add. Two stages, seven atoms each. */
  const A = pmfFromSpec(parsePmfSpec('4:520, 6:250, 9:120, 14:60, 22:30, 38:16, 70:4'));
  const B = pmfFromSpec(parsePmfSpec('12:420, 17:300, 24:150, 34:80, 48:36, 72:12, 130:2'));
  const S = pmfNormalise(pmfConvolve(A, B));
  const q99 = R(99n, 100n);
  eq(pmfPercentile(A, q99) + ' ' + pmfPercentile(B, q99), '38 72', 'each stage has its own p99');
  eq(pmfPercentile(S, q99), 78, 'the SUM has a p99 of 78 ms');
  eq(pmfPercentile(A, q99) + pmfPercentile(B, q99), 110, 'while the two p99s add to 110');
  eq(pmfPercentile(S, q99) < pmfPercentile(A, q99) + pmfPercentile(B, q99), true,
     'p99(A + B) < p99(A) + p99(B) on these distributions');
  /* Means DO add, exactly -- the contrast the lesson is built on. */
  eq(Rtext(pmfMean(A)) + ' ' + Rtext(pmfMean(B)) + ' ' + Rtext(pmfMean(S)),
     '881/125 2414/125 659/25', 'the two means and the sum of the two stages');
  eq(Rtext(Radd(pmfMean(A), pmfMean(B))), Rtext(pmfMean(S)), 'expectation is linear; percentiles are not');
  eq(S.length, 43, '43 attainable totals from 7 x 7 pairs');
  eq(Rtext(pmfCdfAt(S, 78)), '3096/3125', 'the cumulative at 78 ms, exactly');
  eq(Rcmp(pmfCdfAt(S, 78), q99) >= 0, true, 'which does reach 99/100');
  eq(Rcmp(pmfCdfAt(S, 77), q99) < 0, true, 'while the atom below it does not -- so 78 is the rank');
  eq(parsePmfSpec('4:520, oops'), 'null', 'an unreadable stage is refused, not half-parsed');
  eq(parsePmfSpec('4:0'), 'null', 'and a zero weight is not a distribution');

  /* L9: the budget, allocated backwards from a 400 ms SLO. */
  const plan = budgetPlan(400, 208, [8, 20, 150, 40]);
  eq(Rtext(plan.avail) + ' ' + Rtext(plan.share), '192 48', '192 ms left, 48 ms each on an even split');
  eq(Rtext(plan.residual), '-26', 'the plan is 26 ms short');
  eq(plan.rows.map(function (r) { return r.fits ? 'y' : 'n'; }).join(''), 'yyny', 'search is the stage that cannot fit');
  eq(Rtext(plan.rows[2].residual), '-102', 'by 102 ms');
  eq(Rtext(plan.spare) + ' ' + Rtext(plan.need), '76 102', 'the others release 76 ms against a need of 102');
  eq(plan.balanced, true, 'and the residual balances both ways of counting it');
  /* Raise the SLO until it fits, and the two ways of counting still agree. */
  const roomy = budgetPlan(500, 208, [8, 20, 150, 40]);
  eq(Rtext(roomy.residual) + ' ' + roomy.balanced, '74 true', 'at a 500 ms SLO the plan fits');

  /* L10: the timeout, the retries and the calls it kills. */
  const tSpec = parsePmfSpec('8:45, 11:25, 16:15, 24:8, 45:4, 90:2, 400:1');
  const tSample = expandSpec(tSpec);
  eq(tSample.length, 100, 'a hundred measured calls');
  eq(Rtext(worstCaseMs(90, 1)), '180', 'one retry at a 90 ms timeout is 180 ms worst case');
  eq(Rtext(killFraction(tSample, 90)), '1/100', 'a timeout at the p99 kills one call in a hundred');
  eq(Rtext(allAttemptsLost(R(1n, 100n), 1)), '1/10000', 'and both attempts fail once in ten thousand');
  eq(Rtext(sampleMean(tSample)), '1827/100', 'the mean of that sample is 18.27 ms');
  /* The misconception, priced: a timeout at the mean throws away 15% of calls
     that were going to succeed. */
  eq(Rtext(killFraction(tSample, 18)), '3/20', 'a timeout at the mean kills 15% of good calls');
  eq(Rtext(killFraction(tSample, 400)), '0', 'a timeout past the maximum kills none');

  /* L11: the one rounded figure on the course, and the reason it rounds. */
  near(mathisMbitsApprox(1460, 100, R(1n, 100n)), 1.168, 1e-9, '1% loss at 100 ms bounds a flow at 1.168 Mbit/s');
  eq(streamsToFillApprox(10000, mathisMbitsApprox(1460, 100, R(1n, 100n))), 8562,
     'so 8562 streams are needed to fill a 10 Gbit/s link');
  /* Halving the loss multiplies the bound by sqrt(2), not by 2 -- the whole
     shape of the result is in that square root. */
  near(mathisMbitsApprox(1460, 100, R(1n, 200n)) / mathisMbitsApprox(1460, 100, R(1n, 100n)),
       Math.SQRT2, 1e-9, 'halving the loss buys a factor of sqrt 2');
  eq(Rsqrt(R(1n, 50n)), 'null', 'and 2% loss has no rational root at all, which is why sqrtApprox is used');
  near(mathisMbitsApprox(1460, 100, R(1n, 50n)), 0.826, 1e-3,
       'and twice the loss is not half the bound: 2% gives 0.826, not 0.584');
}


// ------------------------------------------- capacity estimation (kit: estimate)
/* The arithmetic of System Design course 1. Every case below is a claim some
   lesson on that course makes out loud, so a failure here is a page asserting
   something false, not a style regression. */
console.log('capacity estimation: intervals, unit chains, series and ceilings');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS') + sysdBlock('APPROX_JS')
       + estimateBlock('ESTIMATE_JS'));

  /* Printing an exact rational at a size that defeats Rdec. This is not
     cosmetic: Rdec goes through Number(n)/Number(d), and the storage mode
     routinely holds 10^15 over 10^72. */
  eq(Rround(R(1n, 3n), 4), '0.3333', 'a third to four places');
  eq(Rround(R(2n, 3n), 4), '0.6667', 'two thirds rounds up, not down');
  eq(Rround(R(1n, 2n), 0), '1', 'a half rounds half-up at zero places');
  eq(Rround(R(-1n, 3n), 3), '-0.333', 'and the sign survives');
  eq(Rround(R(10n ** 24n + 1n, 1n), 0), '1000000000000000000000001',
     '10^24 + 1 exactly, where a double would have said 1e+24');
  eq(Number(Rdec(R(10n ** 24n + 1n, 1n))) === 1e24, true,
     'which is exactly what Rdec does say, and why Rround exists');
  eq(groupDec('1234567.89'), '1 234 567.89', 'grouping stops at the decimal point');
  eq(groupDec('-1000'), '-1 000', 'and does not eat the sign');
  eq(showR(R(1234567n, 100n), 1), '12 345.7', 'a figure as a capacity page shows it');
  eq(Rtextg(R(100000n, 1n)), '100 000', 'an exact ratio, grouped');
  eq(Rtextg(R(125n, 108n)), '125/108', 'a small fraction is left alone');
  eq(powTen(5) + ' ' + powTen(-3), '10⁵ 10⁻³', 'decades read as decades');

  /* Widths in powers of ten: an exact integer search, and its rounded gloss. */
  eq(decadeBracket(R(64n, 1n)), 1, '64 is between 10^1 and 10^2');
  eq(decadeBracket(R(1n, 1n)), 0, '1 sits in decade 0');
  eq(decadeBracket(R(1000n, 1n)), 3, 'an exact power belongs to its own decade, not the one below');
  eq(decadeBracket(R(1n, 1000n)), -3, 'and a thousandth to -3');
  eq(decadeBracket(R(999n, 1000n)), -1, 'just under 1 is decade -1');
  near(log10Approx(R(1000n, 1n)), 3, 1e-12, 'log10 of a thousand');
  near(log10Approx(R(64n, 1n)), 1.80617997, 1e-6, 'log10 of the width three doubling factors give');
  /* The case Rnum cannot do: both ends past 2^53, the ratio small. */
  near(log10Approx(Rdiv(R(10n ** 40n, 1n), R(10n ** 37n, 1n))), 3, 1e-9,
       'a ratio of two numbers a double cannot hold');
  near(ratioApprox(R(3n * 10n ** 40n, 1n), R(10n ** 40n, 1n)), 3, 1e-9,
       'and the same ratio as a Number, for pixels');

  /* L1. Three factors at a factor of two: the product is at a factor of EIGHT,
     the interval is 64x end to end, and the arithmetic midpoint is four times
     the estimate -- which is the misconception the lesson names. */
  const C = [R(10000000n, 1n), R(100n, 1n), R(1000n, 1n)];
  const two = [R(2n, 1n), R(2n, 1n), R(2n, 1n)];
  const iv = productInterval(C, two, two);
  eq(Rtext(iv.centre), '1000000000000', 'the product of the central values');
  eq(Rtext(iv.lo) + ' ' + Rtext(iv.hi), '125000000000 8000000000000', 'the product interval');
  eq(Rtext(iv.down) + ' ' + Rtext(iv.up), '8 8', 'three half-widths of 2 multiply to 8, not to 6');
  eq(Rtext(iv.ratio), '64', 'and end to end the interval is 64x');
  eq(Rtext(Rdiv(arithMid(iv.lo, iv.hi), iv.centre)), '65/16',
     'the arithmetic midpoint is 65/16 of the estimate: it is dragged to the high end');
  eq(Rtext(geoMeanExact(iv.lo, iv.hi)), '1000000000000',
     'the geometric centre of a symmetric interval IS the product of the centres, exactly');
  /* Asymmetric: the root is irrational, so the page must round and say so. */
  const skew = productInterval(C, two, [R(2n, 1n), R(3n, 1n), R(2n, 1n)]);
  eq(Rtext(skew.up), '12', 'one factor skewed high widens only the high end');
  eq(geoMeanExact(skew.lo, skew.hi), 'null', 'and its geometric centre is not rational');
  near(geoMeanApprox(skew.lo, skew.hi), Math.sqrt(1.5) * 1e12, 1e4,
       'so it is computed by the rounded root, which is sqrt(3/2) x the centre');
  /* A factor known exactly contributes nothing to the width. */
  const one3 = [R(1n, 1n), R(1n, 1n), R(1n, 1n)];
  eq(Rtext(productInterval(C, one3, one3).ratio), '1', 'three exact factors give a point, not an interval');

  /* L2. 86400 against 10^5, in both directions -- the lesson's own numbers. */
  eq(Rtext(rpsExact(R(10000000n, 1n), R(100n, 1n))), '312500/27', '10M users x 100 actions a day, per second');
  eq(Rtext(rpsRounded(R(10000000n, 1n), R(100n, 1n))), '10000', 'and with the 10^5-second day');
  eq(Rtext(dayLengthRatio()), '125/108', 'the shortcut day is 125/108 of a real one');
  eq(Rtext(rateShortfallRatio()), '108/125', 'so the rate it gives is 108/125 of the truth');
  eq(Rtext(Rdiv(rpsExact(R(7n, 1n), R(13n, 1n)), rpsRounded(R(7n, 1n), R(13n, 1n)))), '125/108',
     'and the ratio does not depend on the volume, which is why it is quotable');
  eq(Rtrim(Rround(Rmul(Rsub(dayLengthRatio(), R(1n, 1n)), R(100n, 1n)), 2)), '15.74',
     'the 15.7% the lesson quotes is the DAY being long');
  eq(Rtext(Rmul(Rsub(R(1n, 1n), rateShortfallRatio()), R(100n, 1n))), '68/5',
     'the rate is low by 13.6%, which is a different number and the reader will confuse them');
  /* Turning it back: rate x 86400 must return the daily volume it came from. */
  eq(Rtext(Rmul(rpsExact(R(10000000n, 1n), R(100n, 1n)), R(86400n, 1n))), '1000000000',
     'the chain read upward returns where it started');

  /* L3. 100:1 is 1/101, not 1%. */
  const sp = splitRates(R(10000n, 1n), R(100n, 1n));
  eq(Rtext(sp.writeShare), '1/101', 'a 100:1 read/write ratio makes writes one part in 101');
  eq(Rtext(sp.readShare), '100/101', 'and reads the other hundred');
  eq(Rtext(Radd(sp.readShare, sp.writeShare)), '1', 'the two shares are a partition');
  eq(Rtext(sp.naiveWriteShare), '1/100', 'the instinct says 1/100');
  eq(Requ(sp.writeShare, sp.naiveWriteShare), false, 'which is not the same number');
  eq(Rtext(sp.naiveOver), '101/100', 'and overstates the write rate by exactly (r+1)/r');
  eq(Rtext(sp.writes) + ' ' + Rtext(sp.reads), '10000/101 1000000/101', 'the two rates, exactly');
  eq(Rtext(Radd(sp.writes, sp.reads)), '10000', 'and they add back to the total');
  eq(Rtext(splitRates(R(2n, 1n), R(1n, 1n)).writeShare), '1/2', '1:1 is half and half');

  /* L5. Bits, bytes, and the header that is charged once per request. */
  eq(Rtext(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n))), '96/5',
     '2000 req/s of 1200 B is 19.2 Mbit/s');
  eq(Rtrim(Rround(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)), 2)), '19.2', 'read as a decimal');
  eq(Rtext(Rdiv(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)),
                bandwidthNoEight(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)))), '8',
     'forgetting the factor of 8 is out by exactly 8, at every rate and every size');
  eq(Rtext(headerShare(R(1000n, 1n), R(200n, 1n))), '1/6', 'headers are a sixth of a 1 kB request');
  eq(Rtext(headerShare(R(200n, 1n), R(200n, 1n))), '1/2',
     'and half of one whose payload equals the header');
  eq(Rtext(headerCrossover(R(200n, 1n))), '200', 'which is why the crossover payload IS the header size');
  eq(Rcmp(headerShare(R(199n, 1n), R(200n, 1n)), R(1n, 2n)) > 0, true, 'below it they are the majority');

  /* L4. Storage as a series, with growth compounding once a month. */
  const gb500 = R(500n * 10n ** 9n, 1n);
  const terms = growthTerms(gb500, 90, R(5n, 100n));
  eq(terms.length, 3, '90 days is three monthly blocks');
  eq(terms.map(function (t) { return t.days; }).join(','), '30,30,30', 'each of them full');
  eq(Rtext(terms[2].rate), '551250000000', 'by the third month the daily ingest has compounded twice');
  eq(Rtext(terms[2].running), '47287500000000', 'and 47.2875 TB has accumulated');
  eq(Rtext(storageGrowth(gb500, 90, R(5n, 100n), 3)), '141862500000000', 'three copies of it');
  eq(Rtext(storageFlat(gb500, 90, 3)), '135000000000000', 'against 135 TB if ingest never grew');
  /* The invariant that catches an off-by-one in the block loop. */
  eq(Rtext(storageGrowth(gb500, 90, R(0n, 1n), 3)), Rtext(storageFlat(gb500, 90, 3)),
     'at zero growth the geometric series IS the arithmetic one');
  eq(Rtext(storageGrowth(gb500, 1, R(5n, 100n), 1)), Rtext(gb500), 'one day is one day of ingest');
  /* A part-month: 45 days is 30 at the first rate and 15 at the second. */
  const part = growthTerms(R(10n, 1n), 45, R(1n, 10n));
  eq(part.map(function (t) { return t.days; }).join(','), '30,15', 'the last block is short');
  eq(Rtext(part[1].rate), '11', 'and runs at the compounded rate');
  eq(Rtext(part[1].running), '465', '30x10 + 15x11');

  /* L6. The ratio between two rungs, exactly. */
  eq(Rtext(rungRatio(10000000, 100)), '100000',
     '10^5 main-memory references fit inside one disk seek -- the lesson’s headline');
  eq(Rtext(rungRatio(150000000, 1)), '150000000', 'and the whole ruler spans that from L1');
  eq(Rtext(rungRatio(4, 3)), '4/3', 'two rungs that do not divide stay a fraction');

  /* L7. Twenty-four buckets, a peak, a mean, and their ratio. */
  eq(profileWeights('flat', 12, 5).join(','), new Array(24).fill(10).join(','),
     'a flat profile is flat whatever the amplitude');
  const office = profileWeights('office', 21, 6);
  eq(office[21], 46, 'the busy hour carries 10 + 6x6');
  eq(office.reduce(function (a, b) { return a + b; }, 0), 456, 'and the day totals 456 weight');
  eq(office[9], 10, 'twelve hours away the profile is back at the floor');
  const spike = profileWeights('spike', 19, 10);
  eq(spike[19] + ',' + spike[18] + ',' + spike[20], '130,10,10', 'a spike is one bucket and nothing else');
  let shapeThrew = false;
  try { profileWeights('nonesuch', 0, 1); } catch (e) { shapeThrew = true; }
  eq(shapeThrew, true, 'an unknown profile shape raises rather than quietly going flat');
  const buckets = office.map(function (w) { return R(BigInt(w) * 1000000n, 1n); });
  const ps = peakStats(buckets);
  eq(ps.peakHour, 21, 'the peak is where the shape put it');
  eq(Rtext(ps.total), '456000000', 'the day’s total');
  eq(Rtext(ps.peakRps), '115000/9', 'peak requests a second');
  eq(Rtext(ps.meanRps), '47500/9', 'mean requests a second');
  eq(Rtext(ps.ratio), '46/19', 'peak over mean is 24 x the busiest bucket over the total, exactly');
  eq(Rtext(peakStats(new Array(24).fill(R(7n, 1n))).ratio), '1',
     'and a day with no shape at all has a multiplier of 1, which is the sanity check');

  /* L8. The ceiling, and the headroom named rather than assumed. */
  const mc = machineCount(R(20000n, 1n), R(40n, 1n), 8, R(60n, 100n));
  eq(Rtext(mc.capacity), '200', 'one 8-core machine at 40 ms a request serves 200 req/s');
  eq(Rtext(mc.usable), '120', 'of which 60% may be used');
  eq(Rtext(mc.exact), '500/3', 'so the fleet needs 500/3 machines');
  eq(mc.n, 167n, 'and machines are integers, so N = 167');
  eq(mc.nFull, 100n, 'sizing at 100% would have said 100');
  eq(Rtext(mc.spare), '13400', 'N leaves 13 400 req/s of headroom');
  eq(Rtext(Rmul(mc.utilisation, R(100n, 1n))), '10000/167',
     'the peak then sits at 10000/167 % of the fleet, which is 59.88');
  eq(Rtrim(Rround(Rmul(mc.utilisation, R(100n, 1n)), 2)), '59.88', 'read as a percentage');
  /* The ceiling must not round a whole number up: that is the off-by-one that
     buys a machine nobody needs, on every page that sizes anything. */
  eq(machineCount(R(24000n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 200n,
     'an exact 200 machines is 200, not 201');
  eq(machineCount(R(1n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 1n, 'and any positive load needs at least one');

  /* L9. The working set, and the inverse that the whole lesson rests on. */
  const hot = R(1n, 10n), share = R(9n, 10n);
  eq(Rtext(workingSetFraction(hot, share, R(8n, 10n))), '4/45',
     '80% of the hits from a tenth of the data that takes 90% of the reads');
  eq(Rtext(workingSetFraction(R(5n, 100n), R(75n, 100n), R(95n, 100n))), '81/100',
     'and 95% costs 81% of the data once the target is past the knee');
  eq(Rtext(hitRateAt(hot, share, hot)), '9/10', 'caching exactly the hot region gets exactly its share');
  eq(Rtext(hitRateAt(hot, share, R(1n, 1n))), '1', 'caching everything hits everything');
  eq(Rtext(hitRateAt(hot, share, R(0n, 1n))), '0', 'caching nothing hits nothing');
  eq(Rtext(workingSetFraction(hot, share, R(1n, 1n))), '1', 'and a 100% target needs all of it');
  /* Inverse, at ten targets either side of the knee. A sizing lesson whose
     curve and whose inverse disagree is giving the reader a number that its own
     graph contradicts. */
  let inverseOk = true;
  for (let t = 1; t <= 10; t += 1) {
    const target = R(BigInt(t), 10n);
    if (!Requ(hitRateAt(hot, share, workingSetFraction(hot, share, target)), target)) inverseOk = false;
  }
  eq(inverseOk, true, 'the memory a target needs, put back into the curve, returns that target');
  eq(Rtext(workingSetBytes(R(5n * 10n ** 12n, 1n), hot, share, R(8n, 10n))), '4000000000000/9',
     '5 TB, a tenth hot, 80% wanted: 444.4 GB');
  /* No skew at all: caching x of the data buys x of the hits, which is the
     "caching is not worth it here" case the lesson needs to be able to show. */
  eq(Rtext(workingSetFraction(R(1n, 2n), R(1n, 2n), R(9n, 10n))), '9/10',
     'with no skew the cache must hold as much as the hit rate you want');

  /* L10. Two routes, their ratio, the band, and the shared factor. */
  const routeA = [R(500000n, 1n), R(20n, 1n), R(2000000n, 1n)];
  const routeB = [R(10000000n, 1n), R(1800000n, 1n)];
  eq(Rtext(routeProduct(routeA)), '20000000000000', 'route A');
  eq(Rtext(routeProduct(routeB)), '18000000000000', 'route B');
  eq(Rtext(routeRatio(routeProduct(routeA), routeProduct(routeB))), '10/9', 'and the ratio between them');
  eq(Rtext(routeProduct([])), '1', 'an empty chain is the empty product');
  eq(withinBand(R(10n, 9n), R(8n, 1n)), true, '10/9 is inside a band of 8');
  eq(withinBand(R(9n, 10n), R(8n, 1n)), true, 'and so is its reciprocal');
  eq(withinBand(R(9n, 1n), R(8n, 1n)), false, 'nine is outside');
  /* The direction a naive check gets wrong: a ratio far BELOW 1 is just as much
     a disagreement as one far above, and "ratio < k" alone would pass it. */
  eq(withinBand(R(1n, 9n), R(8n, 1n)), false, 'and so is a ninth');
  eq(withinBand(R(1n, 1n), R(1n, 1n)), true, 'a band of 1 admits only exact agreement');
  eq(sharedFactors(['users', 'sessions', 'bytes'], [R(5n), R(3n), R(7n)],
                   ['rows', 'bytes'], [R(9n), R(7n)]).join(','), 'bytes',
     'a factor in both chains with the same value is shared');
  eq(sharedFactors(['bytes'], [R(7n)], ['bytes'], [R(8n)]).length, 0,
     'the same NAME at a different value is not: route B measured it for itself');
  eq(sharedFactors(['bytes'], [R(7n)], ['rows'], [R(7n)]).length, 0,
     'and a coincidence of value under another name is not either');

  /* Units and the slider ladder. */
  eq(fmtBytes(R(1500n, 1n), 2), '1.5 kB', 'kB is 1000 B, decimal, as a disk is sold');
  eq(fmtBytes(R(999n, 1n), 2), '999 B', 'and below that it stays bytes');
  eq(fmtBytes(R(47287500000000n, 1n), 2), '47.29 TB', 'the storage lesson’s own total');
  eq(fmtBytes(R(10n ** 15n, 1n), 2), '1 PB', 'and a petabyte is a petabyte');
  eq(Rtext(ladderValue(0)) + ' ' + Rtext(ladderValue(1)) + ' ' + Rtext(ladderValue(6)), '1 3/2 10',
     'the 1, 1.5, 2, 3, 5, 7 ladder, one rung per decade step');
  eq(Rtext(ladderValue(ladderIndex(0, 7))), '10000000', '10 million is a rung, so lesson 1 can open on it');
  eq(Rtext(ladderValue(ladderIndex(2, 6))), '2000000', 'and so is 2 MB');
}

// ------------------------------------------- caching and hit rates (kit: cache)
/* The `cache` kit's own arithmetic, on the numbers its ten lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Three of them are not figures but PINS. The stepper this kit uses to show a
   policy's cache contents duplicates the eviction rules of the core's
   replayPolicy, which is the tested one, so it is checked against it on every
   trace and every size below; the byte hit rate is checked against zipfHit at
   the shifted exponent it must equal; and the phase-averaged TTL simulation is
   checked against the closed form it is meant to confirm. A duplicated rule
   that nothing compares is a rule that has already drifted. */
console.log('system design: caching, skew, replacement and staleness');
{
  const CACHE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'cache.py');
  const cacheSrc = fs.readFileSync(CACHE_SOURCE, 'utf8');
  const cacheBlock = (name) => blockFrom(cacheSrc, name, CACHE_SOURCE);
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('HARMONIC_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('REPLAY_JS') + sysdBlock('APPROX_JS')
       + cacheBlock('CACHE_JS'));

  /* --- printing. Rnum goes through Number and this course overflows it. --- */
  eq(Rshow(R(1n, 3n), 3), '0.333', 'long division in BigInt');
  eq(Rshow(R(2n, 3n), 3), '0.667', 'rounded half up at the last digit');
  eq(Rshow(R(1n, 2n), 0), '1', 'and half rounds up, not to even');
  eq(Rshow(R(-1n, 3n), 3), '-0.333', 'the sign survives the division');
  /* The reason Rshow exists: a byte weight over fifty ranks leaves a double. */
  eq(Rnum(R(10n ** 400n + 1n, 3n * 10n ** 400n)), NaN, 'Rnum of a 400-digit ratio is NaN');
  eq(Rshow(R(10n ** 400n + 1n, 3n * 10n ** 400n), 4), '0.3333', 'Rshow of the same is a third');
  eq(Rpercent(R(1n, 3n), 2), '33.33%', 'a percentage of an exact probability');
  eq(groupNum(1234567), '1 234 567', 'digit grouping');
  eq(bytesText(1500), '1.50 kB', 'a kB is 1000 B: egress is billed in decimal units');
  eq(bytesText(40000000000n), '40.00 GB', 'and so is a GB');
  eq(moneyText(R(2400000n, 1n)), '$24 000.00', 'cents to dollars');

  /* --- L1: the backend sees the miss rate ---------------------------------
     The lesson's whole claim is the ratio: 90% to 99% is a tenfold cut, and
     99% to 99.9% is another one. Asserting the two loads alone would not
     catch a formula that had (1 - h) right and lambda wrong. */
  eq(Rtext(backendRate(R(10000n, 1n), R(9n, 10n))), '1000', '10k rps at 90% leaves 1000');
  eq(Rtext(backendRate(R(10000n, 1n), R(99n, 100n))), '100', 'and at 99%, 100');
  eq(Rtext(backendRho(R(10000n, 1n), R(9n, 10n), R(2000n, 1n))), '1/2', 'the backend sits at rho = 1/2');
  eq(Rtext(missMultiple(R(9n, 10n), R(99n, 100n))), '10', '90% to 99% divides the load by 10');
  eq(Rtext(missMultiple(R(99n, 100n), R(999n, 1000n))), '10', 'and 99% to 99.9% by 10 again');
  eq(missMultiple(R(9n, 10n), R(1n, 1n)), null, 'a perfect cache has no ratio, and says so');

  /* --- L2: an expectation, and a percentile that steps --------------------- */
  eq(Rtext(meanLatency(R(19n, 20n), R(1n, 1n), R(40n, 1n))), '59/20', 'the lesson mean, 2.95 ms');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(1n, 2n))), '1', 'the p50 is a hit');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'at h = 95% the p99 is the MISS latency -- the misconception, refuted');
  eq(Rtext(latencyQuantile(R(99n, 100n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '1',
     'and it flips exactly at h = q, not gradually');
  eq(Rtext(latencyQuantile(R(9899n, 10000n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'one ten-thousandth below q and it is the miss latency again');

  /* --- L3, L4: Zipf, exactly ---------------------------------------------- */
  eq(Rtext(rankTerm(2, 3)) + ' ' + Rtext(rankTerm(2, -3)) + ' ' + Rtext(rankTerm(5, 0)), '8 1/8 1',
     'i^e for e positive, negative and zero');
  eq(Rtext(zipfProb(1, 4, 1)), '12/25', 'the most popular of four keys at s = 1');
  eq(Rtext(zipfShare(4, 20, 1, 50).exact), '6466460/11167027',
     'the top 4 of 20 at s = 1 -- the L3 worked example, exactly');
  eq(zipfShare(4, 20, 1, 50).rounded, false, 'and it is not rounded');
  eq(Rtext(zipfHit(4, 20, 0)), '1/5', 's = 0 IS uniform popularity: 20% of the keys, 20% of the hits');
  eq(Rtext(zipfShare(0, 20, 1, 50).exact) + ' ' + Rtext(zipfShare(25, 20, 1, 50).exact), '0 1',
     'an empty cache hits nothing and a complete one hits everything');
  /* Past the limit the page must ROUND and must say so. A silent switch would
     print an approximation in the shape of an exact fraction. */
  eq(zipfShare(20, 200, 1, 50).rounded, true, 'past N = 50 the share is rounded');
  eq(zipfShare(20, 200, 1, 50).exact, null, 'and there is no exact fraction to offer');
  near(zipfShare(20, 200, 1, 50).value, 0.612101, 1e-5, 'the rounded value at N = 200');
  /* Sizing: the C a target costs, and the diminishing returns that follow. */
  eq(sizeForTarget(50, 2, R(9n, 10n)), 5, 'at N = 50, s = 2, ninety per cent costs 5 keys');
  eq(sizeForTarget(50, 2, R(99n, 100n)), 28, 'and ninety-nine per cent costs 28 -- the next nine');
  eq(sizeForTarget(20, 0, R(1n, 2n)), 10, 'under uniform popularity it IS proportional: half for half');
  eq(JSON.stringify(sizeTarget(200, 1, R(9n, 10n), 50)), '{"c":111,"rounded":true}',
     'past the limit the search rounds, and reports that it did');
  eq(hitCurve(4, 1, 50).join(' '), '0.48 0.72 0.88 1', 'h(C) for C = 1..4 at N = 4, s = 1');

  /* --- L10: the byte hit rate is a different number ------------------------
     It is the same harmonic ratio at exponent s - b, so the two must agree
     wherever both are defined. That identity is the assertion: it catches a
     sign error in the exponent, which no single value would. */
  eq(Rtext(byteWeight(20, 1, 0)), Rtext(harmonic(20, 1)), 'at b = 0 the byte weight IS the harmonic');
  eq(Rtext(byteHit(4, 20, 1, 0)), Rtext(zipfHit(4, 20, 1)),
     'so at b = 0 the byte hit rate IS the request hit rate -- the control');
  eq(Rtext(byteHit(4, 20, 2, 1)), Rtext(zipfHit(4, 20, 1)), 'and in general it is zipfHit at s - b');
  eq(Rtext(byteHit(4, 20, 1, 1)), '1/5',
     'at b = s it collapses to C/N: 57.9% of the requests, 20% of the bytes');
  eq(Rtext(byteHit(2, 4, 1, 2)), '3/10', 'b > s is allowed, and harmonicApprox could not compute it');
  near(byteHitApprox(4, 20, 1, 1), 0.2, 1e-12, 'the rounded path agrees with the exact one');
  eq(Rtext(objectBytes(3, 1, 100000)), '300000', 'rank 3 at b = 1 is three times the base size');
  eq(Rtext(egressCost(R(40000n * 1000000000n, 1n), R(2n, 1n), 30)), '2400000',
     '40 TB a day at 2c/GB is $24 000 a month');

  /* --- L5: replacement, and the bound the lesson rests on ------------------ */
  const T1 = parseTrace('A B C A B D A B C D');
  eq(T1.join(''), 'ABCABDABCD', 'the course trace parses');
  eq(parseTrace('a,b--c  A!!b').join('|'), 'A|B|C|A|B', 'any separator, and case folds');
  eq(traceKeys(T1).join(''), 'ABCD', 'four distinct keys, in first-use order');
  eq(Rtext(replayTrace(T1, 3, 'opt').rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(replayTrace(T1, 3, 'lru').rate), '2/5', 'LRU gets 4');
  eq(Rtext(replayTrace(T1, 3, 'fifo').rate), '1/5', 'FIFO gets 2');
  /* THE PIN. The stepper duplicates the core's eviction rules so that it can
     report cache contents; if the two ever disagree the page is showing one
     run and counting another. Checked on five traces at six sizes. */
  {
    let mismatches = 0;
    const traces = [T1, parseTrace('1 2 3 4 1 2 5 1 2 3 4 5'), parseTrace('A A A B C B C B C'),
                    parseTrace('A B C D E A B C D E A B'), parseTrace('A')];
    for (const t of traces) {
      for (let k = 1; k <= 6; k += 1) {
        for (const p of ['fifo', 'lru', 'opt']) {
          if (replayTrace(t, k, p).hits !== replayPolicy(t, k, p).hits) mismatches += 1;
        }
      }
    }
    eq(mismatches, 0, 'the kit stepper agrees with the core replay on every trace, size and policy');
  }
  /* LFU is the one policy the core does not implement, so it needs a trace
     that separates it from the two it would otherwise be mistaken for. On
     A A A B C B C B C at two slots it keeps the stale hot key and gets 2
     where FIFO, LRU and OPT all get 6. */
  const T2 = parseTrace('A A A B C B C B C');
  eq(replayTrace(T2, 2, 'lfu').hits, 2, 'LFU holds the once-hot key and thrashes on the rest');
  eq(replayTrace(T2, 2, 'lru').hits, 6, 'LRU lets it go');
  eq(replayTrace(T2, 2, 'fifo').hits, 6, 'so does FIFO');
  eq(replayTrace(T2, 2, 'opt').hits, 6, 'and the bound is 6 as well, so LFU is losing 4 hits');
  /* An unknown policy must throw. The core silently treats one as FIFO, which
     would show a FIFO run under an LFU heading. */
  {
    let threw = false;
    try { replayTrace(T1, 3, 'random'); } catch (err) { threw = true; }
    eq(threw, true, 'an unknown policy throws rather than quietly becoming FIFO');
  }
  /* Belady's anomaly, measured. FIFO misses 9 times with three slots and 10
     with four; LRU and OPT are stack algorithms and never rise. */
  const BEL = parseTrace('1 2 3 4 1 2 5 1 2 3 4 5');
  eq(missBySize(BEL, 'fifo', 6).join(','), '12,12,9,10,5,5', 'FIFO misses against cache size');
  eq(missBySize(BEL, 'lru', 6).join(','), '12,12,10,8,5,5', 'LRU never rises');
  eq(missBySize(BEL, 'opt', 6).join(','), '12,9,7,6,5,5', 'nor does the bound');
  eq(JSON.stringify(firstAnomaly(BEL, 'fifo', 6)), '{"k":3,"up":4,"from":9,"to":10}',
     "Belady's anomaly, found rather than asserted");
  eq(firstAnomaly(BEL, 'lru', 6), null, 'and LRU has none');
  eq(firstAnomaly(BEL, 'opt', 6), null, 'and neither has OPT');
  eq(firstAnomaly(T1, 'fifo', 6), null, 'the course trace does not show one, which is why the kit ships both');

  /* --- L6: TTL and staleness ---------------------------------------------- */
  eq(Rtext(staleFraction(R(10n, 1n), R(60n, 1n))), '1/12', 'T/(2U) below U');
  eq(Rtext(staleFraction(R(120n, 1n), R(60n, 1n))), '3/4', '1 - U/(2T) above it');
  eq(Rtext(staleFraction(R(60n, 1n), R(60n, 1n))), '1/2', 'and the two branches meet at T = U');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(10n, 1n))), '1/50', 'a 10 s TTL at 5 reads/s misses 2%');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(1n, 10n))), '1',
     'a TTL shorter than the gap between reads misses everything, and the rate caps at 1');
  /* The boundary the simulation turns on: a refresh at the same instant as an
     update picks up the NEW value, so the next update is strictly after. */
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(0n, 1n), R(60n, 1n))), '60',
     'an update at the refresh instant does not make the copy stale');
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(10n, 1n), R(60n, 1n))), '10', 'the next one does');
  /* THE SECOND PIN: the phase-averaged simulation must reproduce the closed
     form it is printed beside, or the page is showing two models. */
  eq(Rtext(staleRun(R(10n, 1n), R(60n, 1n), R(15n, 1n), 24).fraction), '1/12', 'one run at one phase');
  eq(Rtext(staleAverage(R(10n, 1n), R(60n, 1n), 24, 24)), Rtext(staleFraction(R(10n, 1n), R(60n, 1n))),
     'and 24 midpoint phases reproduce T/(2U) exactly');
  eq(Rtext(staleAverage(R(120n, 1n), R(60n, 1n), 24, 2)), Rtext(staleFraction(R(120n, 1n), R(60n, 1n))),
     'the same on the other branch');
  eq(Rtext(staleAverage(R(25n, 1n), R(60n, 1n), 24, 10)), '5/24',
     'and with T not dividing U it still lands on the formula');

  /* --- L7: the stampede ---------------------------------------------------- */
  eq(Rtext(stampedeSize(R(500n, 1n), R(40n, 1n))), '20', 'lambda*d: 500 rps through a 40 ms window');
  eq(Rtext(stampedeSize(R(500n, 1n), R(1n, 1n))), '1/2', 'a 1 ms window lets half a request through');
  eq(String(stampedeCount(R(500n, 1n), R(1n, 1n))), '1', 'which the backend counts as one');
  eq(Rtext(stampedeTotal(R(500n, 1n), R(40n, 1n), 10)), '200', 'ten hot keys expiring together');

  /* --- L8: write-through against write-back -------------------------------- */
  const W = parseTrace('A B A C A B A D A B');
  eq(distinctPerWindow(W, 5).map((x) => x.distinct).join(','), '3,3', 'three distinct keys per flush');
  eq(coalescing(W, 5).writes + ' ' + coalescing(W, 5).distinct + ' ' + Rtext(coalescing(W, 5).ratio),
     '10 6 5/3', 'ten writes become six, a ratio of 5/3');
  eq(coalescing(W, 5).peak, 3, 'and the largest dirty set is three keys');
  eq(Rtext(coalescing(W, 1).ratio), '1', 'flushing every write coalesces nothing');
  eq(Rtext(coalescing(W, 99).ratio), '5/2', 'and one flush for the whole trace coalesces most');
  eq(Rtext(bytesAtRisk(3, 4000)), '12000', 'three 4 kB keys is 12 kB at risk');

  /* --- L9: the second level is conditional --------------------------------- */
  eq(Rtext(globalHit(R(4n, 5n), R(1n, 2n))), '9/10', '80% then half the rest is 90%, not 130%');
  eq(Rtext(globalMiss(R(4n, 5n), R(1n, 2n))), '1/10', 'the global miss is the PRODUCT');
  eq(Rtext(Radd(globalHit(R(4n, 5n), R(1n, 2n)), globalMiss(R(4n, 5n), R(1n, 2n)))), '1',
     'and the two account for everything');
  eq(Rtext(levelLatency(R(4n, 5n), R(1n, 2n), R(1n, 1n), R(5n, 1n), R(50n, 1n))), '7',
     't1 + (1-h1)(t2 + (1-h2)t3) = 7 ms');
  eq(Rtext(naiveSumHit(R(4n, 5n), R(1n, 2n))), '13/10',
     'adding the rates gives 130%, which is how you know it is the wrong operation');
  eq(Rtext(conditionalShare(R(4n, 5n), R(1n, 2n))), '1/10',
     "L2's measured 50% is 10% of all requests, not 50%");
}

// ------------------------------- system design C3: queues and utilisation
/* The `queue` kit's own arithmetic, on the numbers its thirteen lessons print.

   The block this section exists for is the Geo/Geo/1 convergence. A slotted
   simulation is NOT M/M/1 at finite slot size, and a lesson that says its
   formula is "checked against the simulation" is comparing two models. The
   assertions below pin the exact discrete mean at three slot sizes and the rate
   at which it approaches the continuous one, so a change that quietly restores
   the false claim fails here rather than on the page. */
console.log('system design: queues, Little\'s Law and the slotted chain');
{
  const QUEUE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'queue.py');
  const queueSrc = fs.readFileSync(QUEUE_SOURCE, 'utf8');
  const queueBlock = (name) => blockFrom(queueSrc, name, QUEUE_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + queueBlock('QUEUE_KIT_JS'));

  /* --- L1: mu is a rate ------------------------------------------------- */
  eq(Rtext(muFromServiceMs(1)), '1000', 'a 1 ms service is 1000 per second, not 1');
  eq(Rtext(muFromServiceMs(4)), '250', 'a 4 ms service is 250 per second');
  eq(Rtext(serviceMsFromMu(muFromServiceMs(4))), '4', 'and back again');
  eq(Rtext(Rdiv(R(800n, 1n), muFromServiceMs(1))), '4/5', 'rho = lambda/mu at the lesson preset');
  eq(Rtext(growthPerSec(R(1200n, 1n), muFromServiceMs(1))), '200', 'above rho = 1 the backlog grows at lambda - mu');
  eq(Rtext(backlogAfter(R(1200n, 1n), muFromServiceMs(1), 60)), '12000', 'a minute of that is 12 000 waiting');
  eq(Rtext(backlogAfter(R(800n, 1n), muFromServiceMs(1), 60)), '0', 'and below rho = 1 nothing accumulates');

  /* --- L2: Little's Law inside a window ---------------------------------- */
  /* The lesson's trace: five customers over ten slots, area 17. */
  const A = [0, 1, 2, 5, 6], D = [3, 4, 6, 8, 10];
  const w10 = littleWindow(A, D, 10);
  eq(w10.area + ' ' + w10.arrived + ' ' + w10.done + ' ' + w10.inflight, '17 5 5 0', 'the whole trace, counted');
  eq(Rtext(w10.L) + ' ' + Rtext(w10.lambda) + ' ' + Rtext(w10.W), '17/10 1/2 17/5', 'L, lambda and W over it');
  eq(Rtext(w10.lamW), Rtext(w10.L), 'and lambda*W IS L, with no model assumed');
  eq(w10.holds, true, 'the identity holds on a window everyone has left');
  eq(occupancyTrace(A, D, 10).join(''), '1232122211', 'the N(t) staircase the area is under');
  eq(Rtext(littleFromTrace(A, D).L), Rtext(w10.L), 'and the core agrees at the full horizon');
  /* Cut the window short and it stops holding -- which is the misconception,
     and the assertion that keeps the lab honest about WHY. */
  const w8 = littleWindow(A, D, 8);
  eq(w8.inflight, 1, 'at T = 8 one customer is still in the system');
  eq(Rtext(w8.L) + ' vs ' + Rtext(w8.lamW), '15/8 vs 65/32', 'so L and lambda*W part company');
  eq(w8.holds, false, 'the law did not fail; the window did');

  /* --- L3: the same identity, solved three ways -------------------------- */
  eq(Rtext(littleSolve('L', R(1n, 2n), R(4n, 1n))), '2', 'L = lambda*W');
  eq(Rtext(littleSolve('W', R(2n, 1n), R(1n, 2n))), '4', 'W = L/lambda');
  eq(Rtext(littleSolve('lambda', R(2n, 1n), R(4n, 1n))), '1/2', 'lambda = L/W');
  /* The unit trap the lesson is about: 500/s at 40 ms is 20, not 20 000. */
  eq(Rtext(poolForRate(R(500n, 1n), R(40n, 1n))), '20', '500 per second at 40 ms needs 20 connections');
  eq(Rtext(poolCapPerSec(20, R(40n, 1n))), '500', 'and 20 connections at 40 ms cap at 500 per second');
  eq(Rtext(poolForRate(poolCapPerSec(20, R(40n, 1n)), R(40n, 1n))), '20', 'the two are inverses');

  /* --- L4, L7: the slotted chain, which is the point of this section ------ */
  /* The closed form the kit's docstring states, checked against the core's
     geoGeo1 at four points. One point would not do it: at q = 1/2 several wrong
     formulas coincide with the right one. */
  function closed(p, q) {
    const rho = Rdiv(p, q);
    return Rdiv(Rmul(rho, Rsub(R(1n, 1n), p)), Rsub(R(1n, 1n), rho));
  }
  const pts = [[2, 5, 1, 2], [4, 5, 1, 1], [1, 4, 1, 3], [2, 25, 1, 10]];
  pts.forEach(function (t) {
    const p = R(BigInt(t[0]), BigInt(t[1])), q = R(BigInt(t[2]), BigInt(t[3]));
    eq(Rtext(geoGeo1(p, q).L), Rtext(closed(p, q)),
       'Geo/Geo/1 L = rho(1-p)/(1-rho) at p = ' + Rtext(p) + ', q = ' + Rtext(q));
    eq(Rtext(geoGeo1(p, q).p0), Rtext(Rsub(R(1n, 1n), Rdiv(p, q))),
       'and its empty probability is 1 - rho at p = ' + Rtext(p));
  });
  /* The convergence panel L7 ships, exactly. At lambda = 4/5, mu = 1 the
     largest legal slot is 1, and each tenth of it closes the gap by a factor of
     ten -- linear in Delta, because the gap is rho*p/(1 - rho) and p = lambda*Delta. */
  eq(Rtext(largestLegalSlot(R(4n, 5n), R(1n, 1n))), '1', 'the largest slot where lambda*D and mu*D are probabilities');
  eq(Rtext(largestLegalSlot(R(1n, 1n), R(2n, 1n))), '1/2', 'and it is set by whichever rate is larger');
  const conv = convergenceRows(R(4n, 5n), R(1n, 1n), 3);
  eq(conv.map(r => Rtext(r.delta) + ':' + Rtext(r.L)).join(' '),
     '1:4/5 1/10:92/25 1/100:496/125', 'the exact slotted mean at Delta = 1, 1/10, 1/100');
  eq(conv.map(r => Rtext(r.gap)).join(' '), '16/5 8/25 4/125',
     'and the shortfall against rho/(1-rho), falling by exactly ten each step');
  eq(Rtext(Rdiv(conv[0].gap, conv[1].gap)) + ' ' + Rtext(Rdiv(conv[1].gap, conv[2].gap)), '10 10',
     'exactly ten, because the gap is linear in the slot');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'while the continuous formula says 4 at every slot size');
  eq(Rtext(slottedMean(R(4n, 5n), R(1n, 1n), R(1n, 2n))), '12/5',
     'and at Delta = 1/2 the slotted mean is the docstring\'s 12/5, not 4');
  /* A slot too big is not a small error, it is not a model: p must be a
     probability, and the panel must refuse rather than print a number. */
  eq(slottedMean(R(2n, 1n), R(3n, 1n), R(1n, 1n)), 'null', 'lambda*Delta > 1 is not a Bernoulli slot');
  eq(slottedMean(R(1n, 2n), R(3n, 1n), R(1n, 1n)), 'null', 'nor is mu*Delta > 1');
  /* Lq = L - rho, because exactly rho of the time there is one in service. */
  eq(Rtext(geoGeo1Lq(R(2n, 5n), R(1n, 2n))), '8/5', 'the slotted Lq is L - rho');
  eq(Rtext(slottedCa2(R(2n, 5n))) + ' ' + Rtext(slottedCs2(R(1n, 2n))), '3/5 1/2',
     'and the chain\'s own coefficients of variation are 1 - p and 1 - q');

  /* --- L4: the simulation must match the chain it claims to be ----------- */
  const p25 = R(2n, 5n), q12 = R(1n, 2n);
  eq(drawBelow(0, 100, R(2n, 5n)), true, 'a draw at 0 is below any positive probability');
  eq(drawBelow(39, 100, R(2n, 5n)), true, 'and 39/100 is below 2/5');
  eq(drawBelow(40, 100, R(2n, 5n)), false, 'while 40/100 is NOT -- the boundary is half-open, or every rate is biased high');
  eq(slottedRun(p25, q12, 7, 12).join(''), slottedRun(p25, q12, 7, 12).join(''), 'the same seed gives the same run');
  eq(slottedRun(p25, q12, 7, 12).join('') === slottedRun(p25, q12, 8, 12).join(''), false,
     'and a different seed does not');
  /* 40 000 slots, warm-up discarded: the measured mean must land near 12/5. A
     loose tolerance, because this asserts the SIMULATOR implements the chain,
     not that a finite sample equals its mean. */
  const longRun = slottedRun(p25, q12, 11, 40000);
  near(Number(Rdec(runMean(longRun, 4000), 6)), 2.4, 0.12, 'a long slotted run converges on the chain\'s exact 12/5');
  eq(Rtext(runMean([0, 1, 2, 3], 0)) + ' ' + Rtext(runMean([0, 1, 2, 3], 2)), '3/2 5/2', 'the mean, and the mean after a warm-up');
  eq(queueOf([0, 1, 2, 3]).join(''), '0012', 'those waiting is N - 1, floored at zero');
  eq(runMax([0, 3, 1]), 3, 'and the peak of a run');
  /* D/D/1 at the same rho: never a queue, and the mean IS rho. That is lesson
     4's whole claim, and it is exact rather than measured. */
  eq(Rtext(runMean(ddRun(5, 4, 4000), 0)), '4/5', 'clockwork arrivals at rho = 4/5 hold exactly 4/5');
  eq(runMax(ddRun(5, 4, 4000)), 1, 'and never more than the one in service -- nothing ever waits');
  eq(runMax(ddRun(4, 1, 100)), 1, 'the same at a light load');
  /* Deterministic service, same arrival stream: it must wait LESS than
     geometric service at the same rho, which is lesson 9 seen from lesson 4. */
  eq(Rcmp(runMean(queueOf(slottedDetRun(p25, 2, 11, 40000)), 4000),
          runMean(queueOf(slottedRun(p25, q12, 11, 40000)), 4000)) < 0, true,
     'fixed service waits less than geometric service on the same arrivals');
  /* The initial transient: E[N] over an ensemble starts low and climbs. This is
     the assertion behind the sentence "the simulation starts empty". */
  const curve = transientCurve(p25, q12, 1, 24, 160);
  eq(Rtext(curve[0]) === '0' || Rcmp(curve[0], R(1n, 1n)) < 0, true, 'the ensemble starts near empty');
  eq(Rcmp(curveMean(curve, 0, 20), curveMean(curve, 80, 160)) < 0, true,
     'and the early mean is BELOW the late one -- the bias a warm-up removes');
  eq(runningMeans([1, 1, 1, 1], 0, 2).map(r => r[0] + ':' + Rtext(r[1])).join(' '), '2:1 4:1',
     'the running mean, sampled, and exact at each cut-off');

  /* --- L5: geometric to exponential -------------------------------------- */
  eq(Rtext(geoTail(R(1n, 2n), 2, 2)), '81/256', '(1 - 1/2*1/2)^(2/(1/2)) = (3/4)^4, exactly');
  eq(Rtext(geoTail(R(1n, 1n), 1, 3)), '0', 'lambda*Delta = 1 means it always arrives in the first slot');
  /* Rfixed, not Rdec: 200^400 has 921 digits and Number() of it is Infinity, so
     Rdec returns NaN on exactly the case the lesson is about. */
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 10, 4), 8)), 0.1285121, 1e-6, '(19/20)^40, the lesson\'s exact tail');
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 100, 4), 8)), 0.1346580, 1e-6, 'a hundred times finer');
  near(expNegApprox(2, 1e-15), 0.13533528, 1e-7, 'and e^-2, which is where it is going');
  eq(Rcmp(geoTail(R(1n, 2n), 100, 4), geoTail(R(1n, 2n), 10, 4)) > 0, true, 'the gap closes from below');
  /* Memorylessness is EXACT at every slot size, for every s. Not a limit. */
  [0, 1, 3, 5].forEach(function (s) {
    eq(Rtext(geoCondTail(R(1n, 2n), 10, s, 4)), Rtext(geoTail(R(1n, 2n), 10, 4)),
       'P(T > s+4 | T > s) = P(T > 4) at s = ' + s + ', exactly');
  });

  /* --- L6: the binomial exactly, Poisson as its limit --------------------- */
  /* binomRow is a recurrence; this checks it against the closed form it
     replaced, which is the only way to know the recurrence is the same
     distribution and not merely a fast one. */
  const row = binomRow(20, 10, 20);
  let mass = R(0n, 1n);
  for (let k = 0; k <= 20; k += 1) {
    mass = Radd(mass, row[k]);
    eq(Rtext(row[k]), Rtext(Rmul(R(comb(20, k), 1n), Rmul(Rpow(R(1n, 2n), k), Rpow(R(1n, 2n), 20 - k)))),
       'binomRow[' + k + '] is comb(n,k)p^k(1-p)^(n-k)');
  }
  eq(Rtext(mass), '1', 'and the row is a distribution');
  eq(Rtext(binomPmf(20, 10, 10)), '46189/262144', 'ten heads in twenty tosses');
  eq(Rtext(binomTail(20, 10, 19)), '1/1048576', 'a tail past n-1 is the last atom, (1/2)^20');
  eq(Rtext(binomTail(20, 10, 10)), '215955/524288', 'and P(more than half heads) at n = 20');
  eq(Rtext(binomTail(20, 10, 20)), '0', 'nothing exceeds n');
  eq(Rtext(binomVar(100, 10)), '9', 'the binomial variance m(1 - m/n) at n = 100');
  eq(Rtext(binomVar(1000, 10)), '99/10', 'closer to the mean as the window is chopped finer');
  near(Number(Rdec(binomTail(200, 10, 15), 8)), 0.0443561, 1e-5, 'P(count > 15) exactly, at 20 chances per unit');
  near(poissonTailApprox(10, 15), 0.0487404, 1e-6, 'and by the Poisson limit, which rounds');
  near(poissonPmfApprox(10, 10), 0.1251100, 1e-6, 'e^-m m^k/k! at the mean');
  eq(headroomForApprox(10, 0.01, 400), 18, 'a mean of 10 needs headroom 18 for a 1% overflow');
  eq(headroomForApprox(10, 0.001, 400), 21, 'and 21 for 0.1% -- the price of the tail');
  eq(headroomForApprox(12, 0.01, 400), 21, 'and 21 at a mean of 12, the largest this lab offers');
  /* Every Poisson figure above is checked against the same recurrence started
     from Math.exp rather than from the core's series, because the two agree only
     inside the range the block below pins. */
  function refPoissonTail(m, C) { let t = Math.exp(-m), h = t; for (let k = 1; k <= C; k += 1) { t = t * m / k; h += t; } return 1 - h; }
  near(poissonTailApprox(10, 15), refPoissonTail(10, 15), 1e-8, 'the Poisson tail matches a Math.exp reference at m = 10');
  near(poissonTailApprox(12, 20), refPoissonTail(12, 20), 1e-6, 'and at m = 12, the edge of the usable range');

  /* --- e^-x has a range, and the kit stops inside it ---------------------- *
     sysdesign_core's expNegApprox sums the ALTERNATING series for e^-x, whose
     largest term is about e^x/sqrt(2 pi x) while the answer is e^-x. It
     therefore loses roughly 2x/ln(10) significant digits to cancellation:
     measured, the relative error is 3e-9 at x = 10, 1.6e-7 at x = 12, 4e-3 at
     x = 17 and 173% at x = 20, and past x = 21 the SIGN is wrong.

     That is a defect in the core, not in this kit, and the fix belongs there --
     1/exp(x) by a positive-term series would be correct at every x. Until then
     the kit bounds the two modes that call it and refuses outside the bound,
     because a wrong number under a promise of a checkable one is worse than no
     number. These assertions pin both halves: that the method is good where the
     lab uses it, and that the lab's own functions refuse where it is not. */
  near(expNegSafe(10), Math.exp(-10), Math.exp(-10) * 1e-6, 'e^-10 is still good to six figures');
  near(expNegSafe(12), Math.exp(-12), Math.exp(-12) * 1e-5, 'e^-12, the bound, to five');
  eq(expNegSafe(20), 'NaN', 'past the bound the kit returns NaN rather than a confident 173% error');
  eq(expNegSafe(-1), 'NaN', 'and refuses a negative x outright');
  eq(poissonTailApprox(20, 25), 'NaN', 'so the Poisson tail refuses too');
  eq(headroomForApprox(20, 0.01, 400), -1, 'and the headroom search reports that it has no answer');
  eq(Number.isNaN(expTailApprox(R(2n, 1n), 12)), true, 'lambda*t = 24 is outside the method');
  eq(expTailApprox(R(3n, 2n), 8) > 0, true, 'lambda*t = 12 is inside it');

  /* --- L8: the knee ------------------------------------------------------ */
  eq(Rtext(kneeFactor(R(1n, 2n))) + ' ' + Rtext(kneeFactor(R(9n, 10n))) + ' ' + Rtext(kneeFactor(R(99n, 100n))),
     '2 10 100', 'W/S at 50%, 90% and 99%');
  eq(Rtext(Rdiv(kneeFactor(R(9n, 10n)), kneeFactor(R(1n, 2n)))), '5', '50% to 90% multiplies the wait by five');
  eq(Rtext(Rdiv(kneeFactor(R(99n, 100n)), kneeFactor(R(9n, 10n)))), '10', 'and 90% to 99% by ten more');
  eq(Rtext(rhoForFactor(10)) + ' ' + Rtext(rhoForFactor(100)), '9/10 99/100', 'the rho at which W = kS is (k-1)/k');
  eq(Rtext(kneeFactor(rhoForFactor(7))), '7', 'and the two are inverses at every k');

  /* --- L9: Kingman, whose model is the approximation --------------------- */
  /* At c_a^2 = c_s^2 = 1 the formula must reproduce M/M/1 EXACTLY. If it does
     not, the disagreement the lesson shows is an arithmetic bug rather than a
     modelling one, and the page would be teaching the wrong lesson. */
  [[1, 2], [4, 5], [9, 10]].forEach(function (r) {
    const rho = R(BigInt(r[0]), BigInt(r[1])), mu = R(1n, 1n);
    const S = Rinv(mu), lam = Rmul(rho, mu);
    eq(Rtext(kingmanWq(rho, R(1n, 1n), R(1n, 1n), S)), Rtext(mm1(lam, mu).Wq),
       'Kingman at c^2 = 1, 1 IS the M/M/1 Wq at rho = ' + Rtext(rho));
  });
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(0n, 1n), R(2n, 1n))), '4', 'M/D/1 waits half of M/M/1');
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(1n, 1n), R(2n, 1n))), '8', 'which is 8');
  eq(kingmanWq(R(1n, 1n), R(1n, 1n), R(1n, 1n), R(1n, 1n)), 'null', 'and it says nothing at rho = 1');
  /* The disagreement itself, as a number: at the chain's own coefficients
     Kingman says 22/5 and the exact chain says 4. */
  eq(Rtext(kingmanWq(R(4n, 5n), slottedCa2(R(2n, 5n)), slottedCs2(R(1n, 2n)), R(2n, 1n))), '22/5',
     'Kingman at the slotted chain\'s true c^2');
  eq(Rtext(Rdiv(geoGeo1Lq(R(2n, 5n), R(1n, 2n)), R(2n, 5n))), '4', 'against the chain\'s exact 4');

  /* --- L10: pooling ------------------------------------------------------ */
  /* The lesson's worked example: lambda = 3, mu = 1, s = 4. */
  const pooled = erlangC(R(3n, 1n), R(1n, 1n), 4), separate = mm1(R(3n, 4n), R(1n, 1n));
  eq(Rtext(pooled.pWait) + ' ' + Rtext(pooled.Lq) + ' ' + Rtext(pooled.Wq), '27/53 81/53 27/53',
     'Erlang C at a = 3, s = 4');
  eq(Rtext(separate.Wq), '3', 'against 3 for one of four separate queues at the same load');
  eq(Rtext(Rdiv(separate.Wq, pooled.Wq)), '53/9', 'so splitting the traffic costs 53/9 times the wait');
  eq(Rtext(Rdiv(R(3n, 1n), Rmul(R(4n, 1n), R(1n, 1n)))), '3/4', 'at an identical rho of 3/4 either way');

  /* --- L11: the two W values a lossy system separates -------------------- */
  const fin = mm1k(R(4n, 5n), R(1n, 1n), 4);
  eq(Rtext(fin.blocking), '256/2101', 'the lesson preset blocks 256/2101');
  eq(Rtext(fin.L) + ' ' + Rtext(fin.lamEff), '3284/2101 1476/2101', 'its L and its ADMITTED rate');
  eq(Rtext(fin.W), '821/369', 'W from the admitted rate, which is the right one');
  eq(Rtext(Rdiv(fin.L, R(4n, 5n))), '4105/2101', 'W from the offered rate, which is the wrong one');
  eq(Rtext(Rdiv(fin.W, Rdiv(fin.L, R(4n, 5n)))), Rtext(Rinv(Rsub(R(1n, 1n), fin.blocking))),
     'and the error is exactly the factor 1/(1 - piK)');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 100n), 60), 14, 'a 1% loss target needs K = 14 here');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 1000n), 60), 24, 'and 0.1% needs K = 24');
  eq(Rtext(bufferLatencyCap(R(1n, 1n), 14)), '14', 'which caps the wait near K/mu -- the bufferbloat trade');
  /* A finite chain is stable at every rho, which is the other half of L11. */
  eq(Rtext(mm1k(R(1n, 1n), R(1n, 1n), 4).blocking), '1/5', 'at rho = 1 every state is equally likely');
  eq(Rtext(mm1k(R(2n, 1n), R(1n, 1n), 3).L) !== '', true, 'and even above rho = 1 there is an answer');

  /* --- L12: the bucket and the window it replaces ------------------------ */
  const TRACE = [0, 200, 400, 600, 800, 900, 900, 900, 900, 900,
                 1000, 1000, 1000, 1000, 1000, 1400, 1600, 1800, 2000, 2200];
  const bkt = bucketRun(TRACE, R(5n, 1n), 3);
  eq(bkt.admitted + '/' + bkt.rejected, '13/7', 'the lesson trace through a bucket of 3 refilling at 5/s');
  eq(bkt.rows.map(r => (r.admit ? '+' : '-')).join(''), '+++++++---+----+++++', 'and which arrival got what');
  eq(largestBurst(bkt.rows, 1000) <= 3 + 5, true, 'no second exceeds the b + rt bound');
  eq(largestBurst(bkt.rows, 1000), 7, 'the largest it actually allows here is 7');
  /* The misconception, as a number: a fixed window of the same nominal limit
     lets nearly twice that through across a boundary. */
  const win = fixedWindowRun(TRACE, 5, 1000);
  eq(win.admitted + '/' + win.rejected, '12/8', 'the same trace through a fixed window at 5 per second');
  eq(largestBurst(win.rows, 1000), 9, 'which lets 9 through in one second while claiming 5');
  eq(largestBurst(win.rows, 1000) > largestBurst(bkt.rows, 1000), true, 'worse than the bucket it replaces');
  eq(Rtext(bucketRun([0, 1000, 2000], R(1n, 1n), 1).rows[2].tokens), '0', 'tokens are exact, not drifting floats');
  /* The lid, which is what makes b a burst allowance rather than a savings
     account. Idle for twenty seconds at one token a second and the bucket has
     earned twenty; it may keep three. Without the cap a quiet night pays for an
     unbounded morning and the b + rt guarantee is gone. */
  const idle = bucketRun([0, 20000, 20000, 20000, 20000, 20000, 20000], R(1n, 1n), 3);
  eq(idle.admitted + '/' + idle.rejected, '4/3', 'twenty idle seconds still buy only b tokens');
  eq(idle.rows.map(r => (r.admit ? '+' : '-')).join(''), '++++---', 'the burst stops at b, not at what was earned');
  eq(Rtext(bucketRun([0, 20000], R(1n, 1n), 3).rows[1].tokens), '2',
     'the level is capped at b before the arrival is charged, so it is 2 and not 21');
  eq(bucketRun([0, 0, 0, 0], R(5n, 1n), 2).admitted, 2, 'a burst with no gap spends the bucket and stops');
  eq(parseTimes('0 10  20', 9).join(','), '0,10,20', 'times parse and sort');
  eq(parseTimes('', 9), 'null', 'and an empty trace is refused rather than guessed at');

  /* --- L13: a spike is an area ------------------------------------------- */
  const plan = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(800n, 1n));
  eq(Rtext(plan.excess) + ' ' + Rtext(plan.peak), '500 30000', 'the excess rate, and the area it builds');
  eq(Rtext(plan.headroom) + ' ' + Rtext(plan.drainSecs), '200 150', 'the headroom left, and the drain it buys');
  eq(Rtext(plan.maxLagSecs), '30', 'the worst lag is backlog/mu');
  eq(Rtext(plan.totalSecs), '210', 'so a 60 second spike is a 210 second incident');
  eq(Rtext(backlogAt(plan, 60, 30)) + ' ' + Rtext(backlogAt(plan, 60, 60)), '15000 30000', 'the backlog rises to its peak AT the end of the spike');
  eq(Rtext(backlogAt(plan, 60, 135)) + ' ' + Rtext(backlogAt(plan, 60, 210)), '15000 0', 'and falls from there');
  eq(Rtext(backlogAt(plan, 60, 400)), '0', 'never going negative');
  const never = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(1000n, 1n));
  eq(never.drains, false, 'with no headroom afterwards it never drains');
  eq(never.drainSecs, 'null', 'and there is no drain time to print');
  eq(Rtext(backlogPlan(R(1000n, 1n), R(800n, 1n), R(900n, 1n), 60, R(800n, 1n)).peak), '0',
     'a "spike" under mu builds nothing at all');

  /* --- the kit's own printing -------------------------------------------- */
  eq(Rfixed(R(1n, 3n), 4), '0.3333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 4), '0.6667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'and signed');
  eq(Rpct(R(4n, 5n), 1), '80.0%', 'a percentage of an exact probability');
  eq(Rshort(R(17n, 10n), 4), '17/10', 'a readable fraction stays a fraction');
  eq(Rshort(R(272378807820n, 68618940391n), 4), '3.9694', 'and a twelve-digit one becomes a decimal');
  eq(commas(1234567), '1 234 567', 'digit grouping');
}

// --------------------------------------- availability and failure (kit: avail)
/* The `avail` kit's own arithmetic, on the numbers its thirteen lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Four of them are not figures but IDENTITIES, and they are the reason this
   section exists. k-of-n at k = n must be the series product and at k = 1 the
   parallel form; the break-even common cause must be exactly the point at
   which a pair is no better than one machine; halving the repair window must
   divide the loss probability by 2^(N-1) and not by two; and the overlap
   distribution of shuffle sharding must sum to one. Each is exact, each is
   checkable, and each is a claim a lesson makes in prose. */
console.log('system design: availability, retries, durability and blast radius');
{
  const AVAIL_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'avail.py');
  const availSrc = fs.readFileSync(AVAIL_SOURCE, 'utf8');
  const availBlock = (name) => blockFrom(availSrc, name, AVAIL_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('AVAIL_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + availBlock('AVAILKIT_JS'));

  /* --- printing. Rdec goes through Number; the storm iterates past it. ----- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(999n, 1000n), 5), '99.90000%', 'three nines as a percentage');
  eq(Rpct(R(9999n, 10000n), 5), '99.99000%', 'and four, which two places could not tell apart');
  /* RpctAuto widens with the answer, because a fixed width prints a five-nines
     quorum as 100.000000% -- which is the exact claim these lessons deny. */
  eq(RpctAuto(R(999n, 1000n)), '99.90000%', 'three nines gets five places');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 10n))), '99.999999990000%',
     'ten nines gets twelve places, rather than rounding to 100%');
  eq(Rpct(Rsub(R(1n, 1n), R(1n, 10n ** 10n)), 6), '100.000000%',
     'which a fixed six places would have printed as a hundred per cent');
  eq(RpctAuto(R(1n, 1n)), '100%', 'and only an exact one prints as 100%');
  eq(RpctAuto(R(1n, 2n)), '50.0000%', 'while a coin-flip availability gets four');
  /* The reason Rfixed exists here: an iterate of the retry map overflows Number. */
  eq(String(Number(Rpow(R(999n, 1000n), 400).n)), 'Infinity',
     'Number() of 0.999^400 is Infinity');
  eq(Rfixed(Rpow(R(999n, 1000n), 400), 6), '0.670186', 'Rfixed prints it anyway');

  /* --- L1: nines and downtime, in both directions ------------------------- */
  eq(Rtext(periodSeconds('month')), '2628000', 'a month is a twelfth of a 365-day year');
  eq(Rtext(periodSeconds('year')), '31536000', 'and a year is 365 days');
  eq(Rtext(Rmul(periodSeconds('month'), R(12n, 1n))), Rtext(periodSeconds('year')),
     'twelve of those months are exactly the year');
  eq(Rtext(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     '99.9% is 2628 seconds a month');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '43 min 48 s',
     'which is the 43.8 minutes the lesson quotes');
  eq(durText(downtimeSeconds(R(9999n, 10000n), periodSeconds('month'))), '4 min 22.80 s',
     'and one more nine is a tenth of it, not 0.09% more');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('year'))), '8 h 45 min 36 s',
     '8.76 hours a year');
  /* The two directions are inverses, which is what makes the budget selector
     and the target selector the same lesson rather than two. */
  eq(Rtext(availFromDowntime(R(2628n, 1n), periodSeconds('month'))), '999/1000',
     'a 2628-second budget IS three nines');
  eq(Rtext(availFromDowntime(downtimeSeconds(R(99991n, 100000n), periodSeconds('week')),
                             periodSeconds('week'))), '99991/100000',
     'and the round trip returns the availability it started from');
  eq(ninesOf(R(999n, 1000n)), 3, '99.9% has three nines');
  eq(ninesOf(R(9995n, 10000n)), 3, '99.95% has three, not three and a half');
  eq(ninesOf(R(9n, 10n)), 1, '90% has one');
  eq(ninesOf(R(1n, 2n)), 0, 'and 50% has none');

  /* --- L2: MTBF, MTTR, and the identity that makes the lesson -------------- */
  eq(Rtext(availFromMtbf(R(1000n, 1n), R(1n, 1n))), '1000/1001', 'A = MTBF/(MTBF + MTTR)');
  /* THE IDENTITY: halving the repair time is worth exactly as much as doubling
     the time between failures. A(2M, R) = 2M/(2M+R) = M/(M+R/2) = A(M, R/2).
     The lesson says "worth as much"; this is the sense in which that is exact. */
  eq(Requ(availFromMtbf(Rmul(R(1000n, 1n), R(2n, 1n)), R(1n, 1n)),
          availFromMtbf(R(1000n, 1n), Rdiv(R(1n, 1n), R(2n, 1n)))), true,
     'doubling MTBF and halving MTTR give the SAME fraction');
  eq(Requ(availFromMtbf(Rmul(R(37n, 5n), R(2n, 1n)), R(3n, 7n)),
          availFromMtbf(R(37n, 5n), Rdiv(R(3n, 7n), R(2n, 1n)))), true,
     'and on numbers with nothing round about them');
  /* The target solvers invert the availability formula, so putting their
     answer back in must return the target exactly. */
  eq(Rtext(availFromMtbf(R(1000n, 1n), mttrForTarget(R(1000n, 1n), R(9999n, 10000n)))), '9999/10000',
     'the MTTR a target needs, put back through A, returns the target');
  eq(Rtext(availFromMtbf(mtbfForTarget(R(1n, 1n), R(999n, 1000n)), R(1n, 1n))), '999/1000',
     'and so does the MTBF a target needs');
  eq(Rtext(failuresPerPeriod(Radd(R(3600000n, 1n), R(3600n, 1n)), periodSeconds('year'))), '8760/1001',
     '1000 h up plus 1 h down is 8.75 cycles a year');

  /* --- L3: the chain, and how far under the weakest link it lands ---------- */
  eq(Rtext(pctToFraction('99.9')), '999/1000', 'a typed percentage is an exact fraction');
  eq(Rtext(pctToFraction('99.95')), '1999/2000', 'and in lowest terms');
  eq(parseChain('99.9, 99.99, 100').length, 3, 'a chain of three');
  eq(parseChain('99.9, banana'), null, 'and a typo is refused rather than guessed at');
  const ten = parseChain('99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9');
  eq(Rtext(availSeries(ten)), Rtext(Rpow(R(999n, 1000n), 10)), 'ten of them is the tenth power');
  eq(Rfixed(availSeries(ten), 7), '0.9900449', 'ten 99.9% dependencies give 99.0%, not 99.9%');
  /* The misconception, as a number: the chain is TEN TIMES the downtime of its
     own weakest link, not equal to it. */
  eq(Rfixed(Rdiv(Rsub(R(1n, 1n), availSeries(ten)), Rsub(R(1n, 1n), R(999n, 1000n))), 2), '9.96',
     'the chain is 9.96x the downtime of the weakest link in it');
  eq(Rcmp(availSeries(ten), R(999n, 1000n)) < 0, true, 'and strictly worse than it');
  eq(Rtext(availSeries(parseChain('100, 100'))), '1', 'a chain of perfect parts is perfect');

  /* --- L4: parallel, and the failover the formula does not contain --------- */
  const two99 = [R(99n, 100n), R(99n, 100n)];
  eq(Rtext(availParallel(two99)), '9999/10000', 'two 99% paths are four nines, ideally');
  const charged = parallelWithFailover(two99, R(30n, 1n), R(12n, 1n), periodSeconds('year'));
  eq(Rtext(charged.ideal), '9999/10000', 'the ideal figure is untouched');
  eq(Rtext(charged.charge), '1/87600', '12 failovers of 30 s is 360 s a year');
  eq(Rtext(charged.adjusted), Rtext(Rsub(R(9999n, 10000n), R(1n, 87600n))),
     'and the real availability is the ideal one minus that');
  eq(Rfixed(charged.adjusted, 8), '0.99988858', 'four nines becomes three');
  eq(ninesOf(charged.ideal) + ' ' + ninesOf(charged.adjusted), '4 3',
     'the switch costs a whole nine, which is what "failover is not free" means');
  eq(Rtext(parallelWithFailover(two99, R(0n, 1n), R(12n, 1n), periodSeconds('year')).adjusted),
     '9999/10000', 'an instant switch costs nothing, which is the formula as written');

  /* --- L5: k-of-n, AND THE TWO IDENTITIES ---------------------------------- */
  /* These are the assertions the course rests on: the binomial tail is not a
     third model, it is the other two with k moved. If either fails, one of
     three lessons is teaching a different arithmetic from the other two. */
  const A99 = R(99n, 100n);
  for (const n of [1, 2, 3, 5, 8, 12]) {
    const copies = [];
    for (let i = 0; i < n; i += 1) copies.push(A99);
    eq(Requ(availKofN(A99, n, n), availSeries(copies)), true,
       'k = n is the series product at n = ' + n);
    eq(Requ(availKofN(A99, 1, n), availParallel(copies)), true,
       'k = 1 is the parallel form at n = ' + n);
    eq(Rtext(kofnTotal(A99, n)), '1', 'and all ' + (n + 1) + ' terms sum to one');
  }
  /* The same two identities on an availability with an ugly denominator, since
     99/100 is exactly the kind of number a wrong coefficient survives. */
  const Augly = R(7n, 11n), uglyCopies = [Augly, Augly, Augly, Augly];
  eq(Requ(availKofN(Augly, 4, 4), availSeries(uglyCopies)), true, 'k = n at A = 7/11');
  eq(Requ(availKofN(Augly, 1, 4), availParallel(uglyCopies)), true, 'k = 1 at A = 7/11');
  eq(Rtext(kofnTotal(Augly, 4)), '1', 'and its terms still sum to one');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'a majority of three fair coins');
  eq(Rfixed(availKofN(A99, 3, 5), 6), '0.999990', '3 of 5 at 99% is five nines');
  /* "More replicas always means more available" is false, and this is where. */
  eq(Rcmp(availKofN(A99, 5, 5), A99) < 0, true, '5-of-5 is WORSE than 1-of-1');
  eq(Rtext(kofnTerms(A99, 3)[3].term), Rtext(Rpow(A99, 3)), 'the j = n term is the series product');
  eq(String(kofnTerms(A99, 5)[2].c), '10', 'the coefficients are C(n, j)');

  /* --- L6: the common cause, and where redundancy stops paying ------------- */
  eq(Rtext(pairBothDown(R(0n, 1n), R(1n, 100n))), '1/10000', 'at c = 0 the pair is p^2');
  eq(Rtext(pairBothDown(R(1n, 1000n), R(1n, 100n))), '10999/10000000',
     'a 0.1% common cause against a 10^-4 pair');
  eq(Rfixed(Rdiv(pairBothDown(R(1n, 1000n), R(1n, 100n)), R(1n, 10000n)), 2), '11.00',
     'which is eleven times what independence promised');
  eq(Rtext(correlatedBreakEven(R(1n, 100n))), '1/101', 'the break-even c is p/(1 + p)');
  /* THE IDENTITY: at that c the pair is EXACTLY as available as one machine.
     The lesson asks the reader to find "the c at which redundancy buys
     nothing"; this is the sense in which that c is exact rather than a
     reading off a curve. */
  for (const p of [R(1n, 100n), R(1n, 3n), R(7n, 1000n)]) {
    eq(Rtext(pairBothDown(correlatedBreakEven(p), p)), Rtext(p),
       'at c = p/(1+p) the pair is down exactly as often as one machine, p = ' + Rtext(p));
    eq(Rtext(redundancyGain(correlatedBreakEven(p), p)), '1',
       'so the redundancy gain there is exactly 1');
  }
  eq(Rtext(redundancyGain(R(0n, 1n), R(1n, 100n))), '100', 'and 1/p under independence');

  /* --- L7: the error budget, in requests rather than minutes --------------- */
  const reqs = Rmul(R(1000n, 1n), periodSeconds('month'));
  eq(Rtext(reqs), '2628000000', '1000 rps for a month');
  eq(Rtext(budgetRequests(R(999n, 1000n), reqs)), '2628000', 'is a budget of 2.628 M failures');
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n))), '1800000',
     'a 30-minute total outage costs 1.8 M of them');
  eq(Rtext(Rdiv(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n)),
                budgetRequests(R(999n, 1000n), reqs))), '50/73', 'which is 68.5% of the budget');
  /* Severity is a multiplier, which is the whole difference between an SLO on
     requests and an SLO on the clock. */
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 2n))), '900000',
     'the same 30 minutes at half severity costs half as much');
  eq(Rtext(budgetSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     'and the budget as a full outage is the L1 downtime figure again');

  /* --- L8: retries as load ------------------------------------------------- */
  eq(Rtext(retryAttempts(R(1n, 10n), 2)), '111/100', 'two retries at p = 0.1 cost 1.11 attempts');
  eq(Rtext(retrySuccess(R(1n, 10n), 2)), '999/1000', 'and succeed 99.9% of the time');
  eq(Rtext(amplifiedLoad(R(500n, 1n), R(1n, 10n), 2)), '555', '500 rps becomes 555 attempts a second');
  eq(Rtext(duplicateShare(R(1n, 10n), 2)), '11/111', 'of which 9.9% is retry traffic');
  /* The geometric sum, checked against the sum it stands for: the expected
     attempts are the probabilities of reaching each attempt, added up. */
  for (const p of [R(1n, 10n), R(9n, 10n), R(1n, 3n)]) {
    for (const r of [0, 1, 3, 6]) {
      let s = R(0n, 1n);
      for (let i = 0; i <= r; i += 1) s = Radd(s, attemptReach(p, i));
      eq(Rtext(s), Rtext(retryAttempts(p, r)),
         'sum of p^i for i <= r IS the closed form, p = ' + Rtext(p) + ', r = ' + r);
    }
  }
  /* The amplification is worst exactly when the service is worst, and its
     ceiling is the retry budget itself. */
  eq(Rcmp(retryAttempts(R(9n, 10n), 3), retryAttempts(R(1n, 10n), 3)) > 0, true,
     'a worse failure rate costs more attempts, not fewer');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'p = 0.9 with 3 retries is 3.439 attempts');
  eq(Rcmp(retryAttempts(R(99n, 100n), 3), R(4n, 1n)) < 0, true, 'and it never reaches r + 1');

  /* --- L9: the retry storm, its iteration and its fixed point -------------- */
  const lam = R(95n, 100n), cap = R(1n, 1n), base = R(1n, 10n);
  eq(Rtext(stormFailure(R(1n, 2n), cap, base)), '1/10', 'under capacity the failure rate is the base');
  eq(Rtext(stormFailure(R(2n, 1n), cap, base)), '11/20',
     'at twice capacity half the excess fails on top of it');
  eq(Rtext(stormNext(lam, cap, base, 0, lam).load), Rtext(lam),
     'with no retries the map is the identity, so the offered load IS the answer');
  const run = stormRun(lam, cap, base, 3, 5, 3000);
  eq(run.rows.length, 5, 'five iterations');
  eq(Rtext(run.rows[0].amp), '1111/1000', 'the first amplification, exactly');
  eq(Rtext(run.rows[0].out), '21109/20000', 'and the first iterate, which is already over capacity');
  eq(Rcmp(run.rows[0].out, cap) > 0, true, 'from an offered load that was NOT');
  eq(Rcmp(run.rows[4].out, run.rows[0].out) > 0, true, 'the iterates climb');
  /* The fixed point is an ENCLOSURE and the bracket is what makes it exact:
     the map is increasing, so a sign change between two fractions traps a
     fixed point between them. Both ends are checked in the right direction. */
  const fp = stormFixedPoint(lam, cap, base, 3, 24);
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.lo).load, fp.lo) >= 0, true,
     'the map pushes the low end up');
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.hi).load, fp.hi) <= 0, true,
     'and the high end down, so the fixed point is between them');
  eq(Rcmp(fp.lo, fp.hi) <= 0, true, 'and the bracket is the right way round');
  eq(Rfixed(fp.lo, 5), '1.72736', 'the fixed point of the preset');
  /* THE LESSON: the un-retried load was serviceable and the fixed point is not. */
  eq(Rcmp(lam, cap) <= 0, true, '0.95 of capacity was fine');
  eq(Rcmp(fp.lo, cap) > 0, true, 'and the retries alone put the fixed point above capacity');
  eq(Rcmp(stormFixedPoint(lam, cap, base, 0, 24).hi, cap) < 0, true,
     'with retries switched off the same load settles below capacity');
  /* The digit budget stops the table rather than hanging the page. */
  eq(stormRun(lam, cap, base, 3, 12, 200).stopped, true,
     'a tight digit budget stops the iteration and says so');
  eq(stormRun(lam, cap, base, 3, 12, 200).rows.length < 12, true, 'with fewer rows than asked for');

  /* --- L10: backoff waves, seeded ----------------------------------------- */
  eq([1, 2, 3, 4].map((i) => backoffDelayMs(1000, i)).join(','), '1000,2000,4000,8000',
     'the waves land at 1, 2, 4 and 8 seconds');
  const noJit = backoffHistogram(600, 20, 1000, 0, 8, 40, 7, 200);
  eq(noJit.plain.join(',') === noJit.jitter.join(','), true,
     'jitter of zero width IS the un-jittered schedule, which is the check that the spread is centred');
  eq(peakOf(noJit.plain), 600, 'and every client lands in one slot');
  const jit = backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200);
  eq(peakOf(jit.jitter) < peakOf(jit.plain), true, 'jitter lowers the peak');
  eq(peakOf(jit.plain), 600, 'while the un-jittered arm is unchanged by the jitter slider');
  eq(totalOf(jit.plain), 3600, 'six waves of 600 without jitter');
  /* Seeded, and the seed is actually used: same seed same bars, other seed not. */
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200).jitter.join(','),
     jit.jitter.join(','), 'the same seed draws the same histogram');
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 8, 200).jitter.join(',') === jit.jitter.join(','),
     false, 'and a different seed does not');
  eq(perSecond(jit.jitter, 200).length <= 40, true, 'the per-second fold covers the horizon');
  eq(totalOf(perSecond(jit.jitter, 200)), totalOf(jit.jitter), 'and loses no retries');

  /* --- L11: shedding against collapse ------------------------------------- */
  const capacity = R(1000n, 1n);
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(900n, 1n))), '900',
     'shedding above 90% of capacity delivers 900 rps at twice the load');
  eq(Rtext(goodputUnshed(R(2000n, 1n), capacity)), '500', 'not shedding delivers 500');
  eq(Rcmp(goodputShed(R(2000n, 1n), capacity, R(900n, 1n)),
          goodputUnshed(R(2000n, 1n), capacity)) > 0, true,
     'so rejecting requests served MORE users than accepting them');
  eq(Rtext(goodputUnshed(capacity, capacity)), '1000', 'the collapse model is continuous at the knee');
  eq(Rtext(goodputUnshed(R(500n, 1n), capacity)), '500', 'and is the offered load below it');
  eq(Rtext(goodputShed(R(500n, 1n), capacity, R(900n, 1n))), '500',
     'a shedder under its threshold sheds nothing');
  eq(Rtext(rejectedFraction(R(2000n, 1n), R(900n, 1n))), '11/20', 'and rejects 55% at twice capacity');
  eq(Rtext(rejectedFraction(R(500n, 1n), R(900n, 1n))), '0', 'nothing at all below it');
  /* A threshold set above capacity is not a shedder: what it admits collapses
     exactly as the unshed arm does, which is the failure mode of a limit copied
     from the load generator rather than measured from the service. */
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))),
     Rtext(goodputUnshed(R(1200n, 1n), capacity)), 'a threshold above capacity sheds into collapse');
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))), '2500/3',
     'and delivers less than a threshold at 90% would');
  eq(Rtext(admittedLoad(R(2000n, 1n), R(900n, 1n))), '900', 'the shedder admits the threshold');
  eq(Rtext(admittedLoad(R(500n, 1n), R(900n, 1n))), '500', 'or the offered load, whichever is smaller');
  eq(Rtext(Rdiv(admittedLoad(R(2000n, 1n), R(900n, 1n)), capacity)), '9/10',
     'so utilisation under the shedder is the ADMITTED load over capacity, not the goodput');

  /* --- L12: durability, the one approximation ----------------------------- */
  /* The exact fraction of the first-order formula, which is what the page
     prints beside the float so that the reader can see WHICH part rounds. */
  eq(Rtext(durabilityLossExact(3, R(1n, 50n), R(24n, 1n))), '3/8326562500',
     'three copies, 2% a year, a 24 h repair window');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)), 3.6029e-10, 1e-14,
     'and the float agrees with it');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)),
       Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).n)
       / Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).d), 1e-20,
       'the rounding is in the MODEL, not in the division');
  /* THE IDENTITY: halving the window divides by 2^(N-1), not by two. This is
     the lesson's "R matters as much as f", and it is exact. */
  for (const n of [2, 3, 4, 6]) {
    eq(Rtext(Rdiv(durabilityLossExact(n, R(1n, 50n), R(24n, 1n)),
                  durabilityLossExact(n, R(1n, 50n), R(12n, 1n)))), String(Math.pow(2, n - 1)),
       'halving R divides the loss probability by 2^(N-1) at N = ' + n);
  }
  /* "Three copies is three times the durability" is false: it is a factorial
     times the Nth power of the failure rate. */
  eq(Rtext(Rdiv(durabilityLossExact(1, R(1n, 50n), R(24n, 1n)),
                durabilityLossExact(3, R(1n, 50n), R(24n, 1n)))),
     Rtext(Rdiv(R(1n, 1n), Rmul(R(6n, 1n), Rmul(Rpow(R(1n, 50n), 2), Rpow(R(1n, 365n), 2))))),
     'a third copy is worth f^2 R^2 times a factorial, not a factor of three');
  eq(Rtext(durabilityLossExact(1, R(1n, 50n), R(24n, 1n))), '1/50',
     'and one copy is just the failure rate');
  /* The truncation itself: the first-order term stands in for 1 - e^-x, and
     the page shows the gap rather than claiming there is none. */
  const gap = truncationGap(2 * 0.02 * 24 / 8760);
  eq(gap.first > gap.exact, true, 'the first-order term overstates 1 - e^-x');
  near((gap.first - gap.exact) / gap.first, 5.48e-5, 1e-6, 'here by 0.0055%');

  /* --- L13: shuffle sharding, exactly ------------------------------------- */
  eq(String(comb(16, 2)), '120', 'sixteen nodes, two each, is 120 shards');
  eq(Rtext(shuffleDisjoint(16, 2)), '91/120', 'two tenants share no node 91 times in 120');
  eq(Rtext(shuffleIdentical(16, 2)), '1/120', 'and hold the identical set once');
  eq(Rtext(shuffleOverlap(16, 2, 1)), '7/30', 'overlapping in exactly one is the rest');
  /* THE IDENTITY: the overlap distribution is a distribution. This is
     Vandermonde, and a wrong coefficient anywhere breaks it. */
  for (const [n, k] of [[16, 2], [8, 3], [40, 8], [10, 5], [6, 1], [5, 3]]) {
    let s = R(0n, 1n);
    for (let j = 0; j <= k; j += 1) s = Radd(s, shuffleOverlap(n, k, j));
    eq(Rtext(s), '1', 'the overlap terms sum to one at n = ' + n + ', k = ' + k);
  }
  /* Where a disjoint pair is impossible the probability must be zero, not
     small: with k > n/2 there are not enough nodes left to miss you. */
  eq(Rtext(shuffleDisjoint(5, 3)), '0', 'with 3 of 5 nodes, no second tenant can miss you');
  eq(Rtext(shuffleIdentical(5, 3)), '1/10', 'and one pairing in ten is identical');
  eq(Rtext(blastFraction(16, 2)), '1/8', 'one bad node degrades an eighth of the tenants');
  /* The sample assignment is drawn from the same seeded stream the page uses,
     so what it shows and what it claims come from one run. */
  const sets = shuffleAssign(16, 2, 12, 3);
  eq(sets.length, 12, 'twelve tenants drawn');
  eq(sets.every((s) => s.length === 2), true, 'each holding exactly k nodes');
  eq(sets.every((s) => s[0] !== s[1]), true, 'and never the same node twice');
  eq(sets.every((s) => s.every((v) => v >= 0 && v < 16)), true, 'all inside the fleet');
  eq(shuffleAssign(16, 2, 12, 3).join('|'), sets.join('|'), 'the same seed draws the same assignment');
  eq(shuffleAssign(16, 2, 12, 4).join('|') === sets.join('|'), false, 'a different seed does not');
  eq(identicalCount([[1, 2], [1, 2], [3, 4]]), 1, 'one tenant holds the exact set of the first');
  eq(disjointCount([[1, 2], [1, 2], [3, 4]]), 1, 'and one shares nothing with it');
}

console.log('system design: partitioning, imbalance, rehashing and cross-shard cost');
{
  const SHARD_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'shard.py');
  const shardSrc = fs.readFileSync(SHARD_SOURCE, 'utf8');
  const shardBlock = (name) => blockFrom(shardSrc, name, SHARD_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + shardBlock('SHARDKIT_JS'));

  /* --- the stream this kit draws from, and why it is not the other one ----
     The rest of the path draws from the glibc LCG, whose modulus is 2^31. This
     kit takes its draws MODULO N, and the low bits of a power-of-two modulus
     are a cycle, not a sample. That is asserted here rather than described,
     because if it were ever untrue the right thing to do would be to simplify
     the kit -- and because a future edit that "unified" the generators would
     silently make every imbalance lesson teach the opposite of its claim. */
  {
    const glibc = lcgStream(1103515245, 12345, 2147483648, 7, 16).map((x) => x % 4);
    eq(glibc.join(','), '0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3',
       'the glibc LCG taken mod 4 is a cycle, not a sample');
    const level = new Array(8).fill(0);
    lcgStream(1103515245, 12345, 2147483648, 7, 1600).forEach((x) => { level[x % 8] += 1; });
    eq(level.every((c) => c === 200), true,
       'and 1600 of its values into 8 bins come out PERFECTLY level, which is the claim this course denies');
    const mine = binOccupancy(7, 1600, 8);
    eq(occTotal(mine), 1600, 'the kit places every key it is given');
    eq(occMax(mine) > occMin(mine), true, 'and MINSTD mod 8 does not come out level');
  }
  /* Reproducibility, which is the point of seeding at all. */
  eq(shardStream(7, 12).join(','), shardStream(7, 12).join(','), 'the same seed draws the same stream');
  eq(shardStream(8, 12).join(',') === shardStream(7, 12).join(','), false, 'a different seed does not');
  eq(shardStream(7, 400).every((x) => x >= 1 && x < shardModulus()), true,
     'every draw is inside the modulus and never the fixed point 0');
  /* THE SEED FINALISER. Without it an LCG's k-th value is an affine function
     of the seed, and for the small seeds a slider offers nothing wraps, so
     consecutive seeds hand out proportional placements: the ring arcs came out
     0.0206, 0.0309, 0.0411, ... a straight line. Every mode here asks the
     reader to reseed and compare, so this is load-bearing. The test is that
     three consecutive seeds are NOT in arithmetic progression at the first
     draw, which is exactly what a raw seed would give. */
  {
    const a = shardStream(1, 1)[0], b = shardStream(2, 1)[0], c = shardStream(3, 1)[0];
    eq(b - a === c - b, false, 'consecutive seeds are not an arithmetic progression');
    eq(shardSeedState(3) === 3, false, 'and the seed itself never becomes the state');
    const arcs = [];
    for (let s = 1; s <= 12; s += 1) arcs.push(Rnum(ringNewNodeArc(s, 7, 1)));
    let monotone = true;
    for (let i = 2; i < arcs.length; i += 1) if (arcs[i] < arcs[i - 1]) monotone = false;
    eq(monotone, false, 'the arc a joining node takes is not monotone in the seed');
  }

  /* --- L1: two constraints, and the larger ------------------------------- */
  {
    const lam = R(120000n, 1n), per = R(8000n, 1n), rho = R(65n, 100n);
    const D = R(48n * 10n ** 12n, 1n), rf = R(3n, 1n), node = R(4n * 10n ** 12n, 1n);
    eq(String(shardsForLoad(lam, per, rho)), '24', '120000/(8000 x 0.65) = 23.08, so 24 shards');
    eq(Rtext(Rdiv(lam, Rmul(per, rho))), '300/13', 'and the fraction under that ceiling is exact');
    eq(String(shardsForStorage(D, rf, node)), '36', '48 TB x 3 / 4 TB = 36 exactly');
    const pick = bindingShards(shardsForLoad(lam, per, rho), shardsForStorage(D, rf, node));
    eq(String(pick.n) + '/' + pick.binding + '/' + pick.slack, '36/storage/12',
       'storage binds by twelve shards');
    /* THE MISCONCEPTION, as a number: sizing on load alone leaves the nodes
       over their disks, and sizing on storage alone leaves them idle. */
    eq(Rpct(utilisationAt(lam, per, 36n), 2), '41.67%', 'the storage-bound count runs the nodes at 42%');
    eq(Rpct(utilisationAt(lam, per, 24n), 2), '62.50%', 'while the load-bound one would have run them at 62.5%');
    eq(byteText(bytesPerNodeAt(D, rf, 24n)), '6.00 TB', 'and put 6 TB on a 4 TB disk');
    /* A ceiling is a ceiling: an exact multiple must not round up. */
    eq(String(shardsForLoad(R(100n, 1n), R(10n, 1n), R(1n, 1n))), '10', 'an exact fit is not rounded up');
    eq(String(shardsForLoad(R(101n, 1n), R(10n, 1n), R(1n, 1n))), '11', 'and one request past it is');
    eq(shardsForLoad(lam, per, R(0n, 1n)), null, 'a zero target utilisation has no answer');
    eq(bindingShards(7n, 7n).binding, 'both', 'equal constraints bind together');
  }

  /* --- L2: hashing does not give equal shards ---------------------------- */
  {
    const occ = binOccupancy(7, 1200, 12);
    eq(occTotal(occ), 1200, 'every key is placed exactly once');
    eq(occ.length, 12, 'into the shards asked for');
    eq(Rtext(maxOverMean(occ)), Rtext(R(BigInt(occMax(occ)) * 12n, 1200n)), 'max/mean is max x N / m');
    eq(Rcmp(maxOverMean(occ), R(1n, 1n)) > 0, true, 'and it is above one -- hashing is not level');
    eq(Rcmp(minOverMean(occ), R(1n, 1n)) < 0, true, 'while the emptiest shard is below it');
    eq(binOccupancy(7, 1200, 12).join(','), occ.join(','), 'the placement is reproducible');
    /* One seed is one sample of a maximum: across seeds the maximum MOVES,
       which is the sentence the lesson's how_to asks the reader to check. */
    {
      const maxima = new Set();
      for (let s = 1; s <= 12; s += 1) maxima.add(occMax(binOccupancy(s, 1200, 12)));
      eq(maxima.size > 1, true, 'the maximum is a distribution, not a constant');
    }
    /* A single shard takes everything, and the ratio says so exactly. */
    eq(Rtext(maxOverMean(binOccupancy(3, 500, 1))), '1', 'one shard holds the mean, which is everything');
    eq(occEmpty([0, 4, 0, 9]), 2, 'empty shards are counted');
    /* The stated asymptotic is a Number and is labelled as one everywhere it
       is printed; below n = 16 it refuses rather than returning nonsense. */
    near(oneChoiceStatedApprox(1024), 3.5804, 1e-3, 'ln n / ln ln n at n = 1024, stated not proved');
    near(twoChoiceStatedApprox(1024), 1.9355, 1e-3, 'ln ln n at n = 1024, stated not proved');
    eq(isFinite(oneChoiceStatedApprox(4)), false, 'and it declines to answer where ln ln n is not positive');
  }

  /* --- L3: rehashing, and THE identity of the whole course ---------------
     N/(N+1) of the keys move under mod-N rehashing and 1/(N+1) move on a ring,
     and those two fractions ARE the whole key set. The course's how_to asks
     the reader to read them as a pair; this is that pair, checked. */
  for (const n of [1, 2, 3, 4, 7, 8, 12, 16, 31, 64, 100]) {
    eq(Rtext(rehashShareSum(n)), '1',
       'mod N moves N/(N+1) and a ring moves 1/(N+1): at N = ' + n + ' they add to one whole');
    eq(Rtext(modMoveShare(n)), n + '/' + (n + 1), 'the mod-N fraction at N = ' + n);
    eq(Rtext(ringMoveShare(n)), '1/' + (n + 1), 'and the ring fraction is the rest of it');
  }
  /* And the mod-N fraction is not a formula quoted at the reader -- it is the
     count over a complete cycle, which by CRT is exactly N of every N(N+1). */
  for (const n of [2, 3, 4, 7, 12, 20]) {
    const c = modCycleMoved(n);
    eq(c.total, n * (n + 1), 'the complete cycle at N = ' + n + ' is N(N+1) hashes');
    eq(c.moved, n * n, 'and exactly N^2 of them move');
    eq(Requ(c.share, modMoveShare(n)), true,
       'so the enumeration at N = ' + n + ' IS N/(N+1), not an estimate of it');
  }
  eq(Rtext(modCycleMoved(7).share), '7/8', 'seven shards to eight moves seven eighths of the keys');
  eq(Rtext(ringMoveShare(7)), '1/8', 'and a ring moves the other eighth');
  /* THE MISCONCEPTION, priced: adding a node does NOT move 1/N of the keys. */
  eq(Rfixed(Rdiv(modMoveShare(7), R(1n, 7n)), 2), '6.13',
     'mod-N moves 6.1 times what the 1/N intuition predicts at N = 7');
  {
    /* The seeded sample lands near the enumeration without being it. */
    const s = modSampleMoved(11, 1200, 7);
    eq(s.total, 1200, 'the sample counts every key it was given');
    eq(Rcmp(s.share, R(4n, 5n)) > 0 && Rcmp(s.share, R(19n, 20n)) < 0, true,
       'and its moved fraction sits around the exact 7/8');
    eq(Requ(s.share, modCycleMoved(7).share), false,
       'a sample is not the enumeration, which is why both are printed');
    /* The ring: a key moves exactly when the joining node took its arc, so the
       counted fraction must track the arc rather than the expectation. */
    const arc = ringNewNodeArc(5, 7, 1), moved = ringSampleMoved(5, 11, 1200, 7, 1);
    eq(Math.abs(Rnum(moved.share) - Rnum(arc)) < 0.03, true,
       'the keys the ring moves are the keys in the joining node arc');
    eq(Rcmp(moved.share, modSampleMoved(11, 1200, 7).share) < 0, true,
       'and far fewer of them than mod-N moves');
    /* Ownership and nesting: an N-node ring is a PREFIX of an (N+1)-node ring,
       which is the property that makes the scheme worth anything at all. */
    const before = ringTokens(5, 7, 1), after = ringTokens(5, 8, 1);
    eq(before.length, 7, 'seven tokens for seven nodes at V = 1');
    eq(after.length, 8, 'and eight for eight');
    eq(before.every((t, i) => before.slice(i).every((u) => u.pos >= t.pos)), true, 'tokens are sorted');
    eq(new Set(before.map((t) => t.pos)).size <= new Set(after.map((t) => t.pos)).size, true,
       'the old tokens are still there');
    eq(before.map((t) => t.pos).every((p) => after.some((u) => u.pos === p)), true,
       'adding a node adds a token and moves none of the others');
    eq(ringArcMeanApprox(1, 7, 1, 40) !== null, true, 'the arc averages over seeds');
    eq(Math.abs(Rnum(ringArcMeanApprox(1, 7, 1, 40)) - 0.125) < 0.05, true,
       'and over 40 seeds it lands near the expected 1/8');
  }

  /* --- L4: virtual nodes -------------------------------------------------- */
  {
    for (const [n, v] of [[8, 1], [8, 10], [8, 100], [3, 1], [16, 25]]) {
      const sh = ringShares(5, n, v);
      eq(sh.length, n, 'one share a node at N = ' + n + ', V = ' + v);
      eq(Rtext(shareTotal(sh)), '1',
         'and the shares are a partition of the ring at N = ' + n + ', V = ' + v);
      eq(Rcmp(shareMaxOverMean(sh), R(1n, 1n)) >= 0, true, 'the largest share is at or above the mean');
      eq(Rcmp(shareMinOverMean(sh), R(1n, 1n)) <= 0, true, 'and the smallest at or below it');
    }
    /* THE STATED RATE. The relative spread falls like 1/sqrt(V) -- stated, and
       measured here across seeds because one ring is one sample. A factor of
       100 in V should buy about a factor of 10 in spread. */
    const s1 = spreadRmsOverSeedsApprox(1, 8, 1, 16);
    const s10 = spreadRmsOverSeedsApprox(1, 8, 10, 16);
    const s100 = spreadRmsOverSeedsApprox(1, 8, 100, 16);
    eq(s1 > s10 && s10 > s100, true, 'the spread falls as V rises');
    near(s1 / s10, Math.sqrt(10), 1.0, 'V = 1 to V = 10 is about a factor of sqrt(10)');
    near(s1 / s100, 10, 4, 'and V = 1 to V = 100 about a factor of ten');
    near(spreadRateStatedApprox(1), 1, 1e-12, '1/sqrt(V) at V = 1');
    near(spreadRateStatedApprox(100), 0.1, 1e-12, 'and at V = 100');
    /* A perfectly level ring has zero spread and max/mean of exactly one, so
       the statistic means what it says at the boundary. */
    const even = [R(1n, 4n), R(1n, 4n), R(1n, 4n), R(1n, 4n)];
    eq(spreadRmsApprox(even), 0, 'a level ring has no spread at all');
    eq(Rtext(shareMaxOverMean(even)), '1', 'and max/mean of exactly one');
  }

  /* --- L5: range partitioning -------------------------------------------- */
  {
    const mono = rangeWindows('monotonic', 2400, 8, 8, 5, 4);
    eq(Rtext(worstWindowShare(mono)), '1',
       'a monotonic key sends ALL of the current writes to one range');
    eq(Rtext(lifetimeShare(mono)), '1/8',
       'and over the whole run that same range holds a perfectly even eighth -- which is the trap');
    eq(scanRanges('monotonic', 8, 4), 1, 'a time-range scan reads one range');
    const hashed = rangeWindows('hashed', 2400, 8, 8, 5, 4);
    eq(Rcmp(worstWindowShare(hashed), R(1n, 4n)) < 0, true, 'hashing brings the hottest window share down');
    eq(scanRanges('hashed', 8, 4), 8, 'and makes the scan read every range');
    const pre = rangeWindows('prefixed', 2400, 8, 8, 5, 4);
    eq(scanRanges('prefixed', 8, 4), 4, 'a four-bucket prefix makes the scan read four');
    eq(Rcmp(worstWindowShare(pre), worstWindowShare(mono)) < 0, true,
       'and spreads the current writes off the single hot range');
    eq(Rcmp(worstWindowShare(pre), R(1n, 2n)) < 0, true, 'to about one bucket-share of them');
    /* Every pattern places every write, and an unknown one refuses. */
    for (const g of [mono, hashed, pre]) {
      let total = 0;
      g.forEach((row) => { total += occTotal(row); });
      eq(total, 2400, 'every write lands in exactly one range');
    }
    eq(rangeWindows('nope', 100, 4, 4, 1, 1), null, 'an unknown key pattern has no answer');
    eq(scanRanges('nope', 8, 4), null, 'and no scan cost either');
  }

  /* --- L6: a hot key does not care about N -------------------------------- */
  {
    const lam = R(100000n, 1n), f = R(12n, 100n);
    eq(Rtext(hottestLoad(lam, f, 16)), '17500', '0.12 x 100000 + 0.88 x 100000/16');
    eq(Rtext(meanLoad(lam, 16)), '6250', 'against a mean shard of 6250');
    eq(Rtext(hotImbalance(lam, f, 16)), '14/5', 'an imbalance of 2.8');
    eq(Rtext(hotAsymptote(lam, f)), '12000', 'and a floor of f x lambda = 12000');
    /* THE LESSON, as an inequality no shard count escapes. */
    for (const n of [1, 2, 8, 64, 1024, 1000000]) {
      eq(Rcmp(hottestLoad(lam, f, n), hotAsymptote(lam, f)) > 0, true,
         'the hottest shard is above f x lambda at N = ' + n + ', however large N is');
    }
    eq(Rfixed(hottestLoad(lam, f, 1000000), 4), '12000.0880',
       'a million shards leaves the hot shard at 12000.09, not at 0.1');
    eq(Rtext(Rsub(hottestLoad(lam, f, 16), hottestLoad(lam, f, 32))), '2750',
       'doubling the shards removes only half of the UNIFORM part');
    /* Salting divides the term that has no N in it, and charges for it. */
    eq(Rtext(hottestLoadSalted(lam, f, 16, 8)), '7000', 'a salt of 8 brings the hot shard to 7000');
    eq(Rtext(hottestLoadSalted(lam, f, 16, 1)), Rtext(hottestLoad(lam, f, 16)),
       'and a salt of 1 is no salt at all');
    eq(Rtext(saltReadAmplification(f, 8)), '46/25', 'at 1.84 times the reads overall');
    eq(Rtext(saltReadAmplification(f, 1)), '1', 'which is 1 when nothing is salted');
    eq(Rtext(saltReadAmplification(R(0n, 1n), 64)), '1', 'and 1 when no key is hot');
    eq(saltForTarget(lam, f, 16, R(3n, 2n)), 4, 'a salt of 4 brings it inside 1.5 times the mean');
    eq(Rcmp(hottestLoadSalted(lam, f, 16, 4), Rmul(R(3n, 2n), meanLoad(lam, 16))) <= 0, true,
       'and 4 really is inside it');
    eq(Rcmp(hottestLoadSalted(lam, f, 16, 3), Rmul(R(3n, 2n), meanLoad(lam, 16))) <= 0, false,
       'while 3 is not, so the search returned the smallest');
    eq(saltForTarget(lam, f, 16, R(1n, 2n)), null, 'and no salt reaches half the mean, which it says');
    /* With no hot key the hottest shard IS the mean, exactly. */
    eq(Rtext(hottestLoad(lam, R(0n, 1n), 16)), Rtext(meanLoad(lam, 16)), 'f = 0 leaves a level fleet');
  }

  /* --- L7: the maximum of N partition times ------------------------------- */
  {
    const pmf = parsePmf('20:900, 40:70, 120:25, 400:5');
    eq(pmf.length, 4, 'four partition times parsed');
    eq(Rtext(pmf[0][1]), '9/10', 'and the weights normalised to exact probabilities');
    eq(parsePmf('20, 40'), null, 'a list of times is not a distribution');
    eq(parsePmf('x:1'), null, 'nor is a non-numeric time');
    eq(parsePmf('20:-1'), null, 'nor a negative weight');
    eq(parsePmf('20:0, 40:0'), null, 'nor weights that are all zero');
    eq(Rtext(pmfMean(pmf)), '129/5', 'one partition averages 25.8 ms');
    /* pmfMax at N = 1 must be the distribution itself, and its total mass 1. */
    eq(pmfMax(pmf, 1).map((p) => p[0] + ':' + Rtext(p[1])).join(' '),
       pmf.map((p) => p[0] + ':' + Rtext(p[1])).join(' '), 'the maximum of one is the thing itself');
    for (const n of [1, 2, 5, 24, 128]) {
      let total = R(0n, 1n);
      pmfMax(pmf, n).forEach((p) => { total = Radd(total, p[1]); });
      eq(Rtext(total), '1', 'the maximum of ' + n + ' is still a distribution');
    }
    /* THE NEAREST-RANK CROSS-CHECK. pmfQuantile lifts percentile() from a
       sample to a distribution, so on an equiprobable pmf the two must agree
       exactly -- if they ever stop agreeing, one of them has been changed. */
    {
      const sample = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
      const flat = sample.map((v) => [v, R(1n, 10n)]);
      for (const [num, den] of [[1n, 10n], [1n, 4n], [1n, 2n], [9n, 10n], [99n, 100n], [1n, 1n]]) {
        const q = R(num, den);
        eq(pmfQuantile(flat, q), percentile(sample, q),
           'pmfQuantile agrees with the core percentile at q = ' + Rtext(q));
      }
    }
    eq(pmfQuantile(pmf, R(99n, 100n)), 120, 'one partition has a p99 of 120 ms');
    eq(pmfQuantile(pmfMax(pmf, 24), R(99n, 100n)), 400, 'a 24-partition job has a p99 of 400');
    eq(Rfixed(pmfMean(pmfMax(pmf, 24)), 2), '111.63', 'and a mean of 111.63 against one partition 25.8');
    eq(Rfixed(stragglerTax(pmf, 24).ratio, 2), '4.33', 'a straggler tax of 4.33x');
    eq(Rtext(stragglerTax(pmf, 1).ratio), '1', 'which is exactly 1 at a single partition');
    /* The 0.5% partition is not the p99 of one and IS the p99 of three -- found
       by exact integer search over N, never by a logarithm. */
    eq(pmfWorst(pmf), 400, 'the slowest time the distribution puts mass on');
    eq(smallestNForQuantile(pmf, R(99n, 100n), 400, 4096), 3,
       'a 0.5% partition becomes the job p99 at three partitions');
    eq(pmfQuantile(pmfMax(pmf, 2), R(99n, 100n)) < 400, true, 'two partitions do not reach it');
    eq(Rfixed(anySlowerThan(pmf, 24, 120), 4), '0.1133',
       'P(at least one of 24 partitions past 120 ms) = 1 - (1 - 0.005)^24');
    eq(Rtext(anySlowerThan(pmf, 1, 120)), Rtext(pmfTail(pmf, 120)), 'which at N = 1 is just the tail');
  }

  /* --- L8: one choice against d ------------------------------------------ */
  {
    const one = placeOneChoiceFrom(3, 1024, 1024, 2), two = placeChoices(3, 1024, 1024, 2);
    eq(occTotal(one), 1024, 'every key is placed, one choice');
    eq(occTotal(two), 1024, 'and every key is placed, two choices');
    eq(occMax(two) < occMax(one), true, 'the second look lowers the maximum');
    /* THE FAIRNESS OF THE COMPARISON: both arms read the SAME stream, and the
       one-choice arm is exactly the d-choice arm with the extra draws thrown
       away. At d = 1 the two placements must therefore be identical. */
    eq(placeChoices(3, 1024, 1024, 1).join(','), placeOneChoiceFrom(3, 1024, 1024, 1).join(','),
       'at d = 1 the two policies are the same policy');
    eq(placeOneChoiceFrom(3, 512, 512, 2).join(','), placeOneChoiceFrom(3, 512, 512, 2).join(','),
       'and the run is reproducible');
    /* The measured collapse, across seeds rather than on one lucky draw. */
    {
      const acc = maxLoadAcrossSeeds(1, 1024, 1024, 2, 12);
      eq(acc.one.length, 12, 'twelve seeds of one choice');
      eq(acc.many.every((m, i) => m <= acc.one[i]), true,
         'and on every one of them two choices is at least as level');
      eq(Rcmp(meanOf(acc.many), meanOf(acc.one)) < 0, true, 'strictly better on average');
      eq(new Set(acc.many).size <= 2, true, 'the two-choice maximum barely moves across seeds');
      eq(Rtext(meanOf([3, 3, 4])), '10/3', 'the mean of a run is an exact fraction');
    }
    /* Both asymptotics are STATED. What is checked here is only that the
       measured maxima sit in the region they describe -- the proofs are not in
       this library, which is what reconciliation #17 requires the pages to say. */
    near(oneChoiceStatedApprox(4096), 3.9264, 1e-3, 'ln n / ln ln n at n = 4096');
    near(twoChoiceStatedApprox(4096), 2.1184, 1e-3, 'ln ln n at n = 4096');
    eq(occMax(placeOneChoiceFrom(1, 4096, 4096, 2)) > occMax(placeChoices(1, 4096, 4096, 2)), true,
       'and the measured gap at n = 4096 goes the way they describe');
  }

  /* --- L9: scatter-gather ------------------------------------------------- */
  {
    const pmf = parsePmf('10:80, 25:15, 90:4, 250:1');
    eq(Rtext(shardRequestRate(R(400n, 1n), 24)), '9600', '400 queries a second is 9600 shard requests');
    eq(Rtext(requestAmplification(24)), '24', 'an amplification of N');
    eq(Rtext(routedRequestRate(R(400n, 1n))), '400', 'while a routed query stays at 400');
    eq(Rtext(shardRequestRate(R(400n, 1n), 1)), '400', 'and at one shard the two agree');
    /* The tail the query waits for is not the tail a per-shard dashboard shows. */
    const exact = pmfMax(pmf, 24);
    eq(pmfQuantile(pmf, R(99n, 100n)), 90, "one shard's own p99 is 90 ms");
    eq(pmfQuantile(exact, R(99n, 100n)), 250, 'but the QUERY p99 is the 1-in-100 shard, 250 ms');
    eq(pmfQuantile(exact, R(1n, 2n)), 90, 'and the median query already waits what a shard p99 does');
    eq(Rfixed(pmfMean(exact), 2), '105.24', 'the mean query takes 105.24 ms');
    eq(Rfixed(pmfMean(pmf), 2), '17.85', 'against a mean shard of 17.85');
    /* TWO ROUTES TO ONE NUMBER: the exact tail and the seeded run agree. If
       either the pmf algebra or the inverse-transform sampler were wrong, this
       is the assertion that would notice. */
    for (const seed of [9, 21, 37]) {
      const sample = scatterSample(pmf, 24, 800, seed);
      eq(sample.length, 800, 'the run produced the queries it was asked for');
      eq(sample.every((v, i) => i === 0 || v >= sample[i - 1]), true, 'sorted, so percentile can read it');
      eq(percentile(sample, R(1n, 2n)), pmfQuantile(exact, R(1n, 2n)),
         'the sampled median matches the exact one at seed ' + seed);
      eq(percentile(sample, R(99n, 100n)), pmfQuantile(exact, R(99n, 100n)),
         'and so does the sampled p99 at seed ' + seed);
    }
    eq(scatterSample(pmf, 4, 50, 9).join(',') === scatterSample(pmf, 4, 50, 9).join(','), true,
       'the sampled run is reproducible');
  }

  /* --- L10: local against global ------------------------------------------ */
  {
    const r = R(5000n, 1n), w = R(2000n, 1n);
    eq(Rtext(localIndexCost(r, w, 16)), '82000', 'r x N + w at sixteen shards');
    eq(Rtext(globalIndexCost(r, w)), '9000', 'against r + 2w');
    eq(cheaperIndex(r, w, 16), 'global', 'so the global index wins this workload');
    eq(Rtext(indexCrossover(16)), '1/15', 'and they break even at r/w = 1/(N - 1)');
    eq(indexCrossover(1), null, 'at one shard there is no difference to have');
    /* THE CROSSOVER IS A CROSSOVER: at exactly r/w = 1/(N-1) the two costs are
       equal, and either side of it the other one wins. Checked at several N so
       that an off-by-one in the algebra cannot hide. */
    for (const n of [2, 3, 8, 16, 64]) {
      const ratio = indexCrossover(n);
      const rr = R(ratio.n, 1n), ww = R(ratio.d, 1n);
      eq(Rtext(localIndexCost(rr, ww, n)), Rtext(globalIndexCost(rr, ww)),
         'the two indexes cost the same at r/w = 1/(N-1), at N = ' + n);
      eq(cheaperIndex(rr, ww, n), 'equal', 'and the verdict says so at N = ' + n);
      eq(cheaperIndex(Rmul(rr, R(1n, 2n)), ww, n), 'local', 'fewer reads favours the local index');
      eq(cheaperIndex(Rmul(rr, R(2n, 1n)), ww, n), 'global', 'and more reads favours the global one');
    }
    eq(Rtext(localIndexCost(R(0n, 1n), w, 16)), '2000', 'with no reads the local index costs one write');
    eq(Rtext(globalIndexCost(R(0n, 1n), w)), '4000', 'and the global one costs two');
  }

  /* --- L11: cross-shard transactions --------------------------------------- */
  {
    eq(Rtext(sameShardProb(2, 2)), '1/2',
       'THE number: at two shards, half of every two-key transaction already crosses');
    eq(Rtext(crossShardProb(2, 2)), '1/2', 'and the other half of it does not');
    eq(Rtext(sameShardProb(2, 16)), '1/16', 'N^(1-k) at k = 2 is 1/N');
    eq(Rtext(sameShardProb(3, 16)), '1/256', 'and at k = 3 it is 1/N^2');
    eq(Rtext(sameShardProb(12, 64)), '1/73786976294838206464',
       'Rpow takes the negative exponent and stays exact at 64^11');
    eq(Rtext(sameShardProb(1, 37)), '1', 'a one-key transaction is always local');
    eq(Rtext(sameShardProb(5, 1)), '1', 'and so is anything on a single shard');
    for (const k of [1, 2, 3, 7]) {
      for (const n of [2, 5, 16]) {
        eq(Rtext(Radd(sameShardProb(k, n), crossShardProb(k, n))), '1',
           'local and crossing are a partition at k = ' + k + ', N = ' + n);
        eq(Rtext(sameShardProb(k, n)), Rtext(Rpow(R(1n, BigInt(n)), k - 1)),
           'N^(1-k) is 1/N^(k-1) at k = ' + k + ', N = ' + n);
      }
    }
    /* The shards a transaction touches is a coupon-collector expectation, and
       it must sit between one and the smaller of k and N. */
    eq(Rtext(expectedShardsTouched(1, 16)), '1', 'one key touches one shard');
    eq(Rtext(expectedShardsTouched(2, 2)), '3/2', 'two keys on two shards touch 1.5 of them');
    eq(Rfixed(expectedShardsTouched(3, 16), 4), '2.8164', 'three keys on sixteen touch 2.82');
    for (const [k, n] of [[2, 2], [4, 8], [12, 64], [8, 3]]) {
      const t = expectedShardsTouched(k, n);
      eq(Rcmp(t, R(1n, 1n)) >= 0, true, 'at least one shard at k = ' + k + ', N = ' + n);
      eq(Rcmp(t, R(BigInt(Math.min(k, n)), 1n)) <= 0, true, 'and never more than min(k, N)');
    }
    /* Two-phase commit, itemised, and charged only to the ones that cross. */
    const cost = twoPhaseCost(R(2n, 1n), R(1n, 2n));
    eq(Rtext(cost.rtt) + '/' + Rtext(cost.fsync) + '/' + Rtext(cost.total), '4/1/5',
       'two round trips and two fsyncs');
    eq(Rtext(meanAddedLatency(2, 2, R(2n, 1n), R(1n, 2n))), '5/2',
       'half the transactions pay 5 ms, so the mean is 2.5');
    eq(Rtext(meanAddedLatency(1, 16, R(2n, 1n), R(1n, 2n))), '0',
       'and a single-key transaction pays none of it');
  }

  /* --- L12: rebalancing ---------------------------------------------------- */
  {
    const D = R(48n * 10n ** 12n, 1n), B = R(200n * 10n ** 6n, 1n), budget = R(800n * 10n ** 6n, 1n);
    eq(byteText(movedBytes(R(1n, 4n), D)), '12.00 TB', 'a quarter of 48 TB is 12 TB');
    eq(Rtext(rebalanceSeconds(R(1n, 4n), D, B)), '60000', 'at 200 MB/s that is 60000 seconds');
    eq(durText(rebalanceSeconds(R(1n, 4n), D, B)), '16 h 40 min', 'which is 16 h 40 min, not a moment');
    eq(rebalanceSeconds(R(1n, 4n), D, R(0n, 1n)), null, 'a throttle of zero never finishes');
    eq(Rtext(rebalanceSeconds(R(0n, 1n), D, B)), '0', 'and moving nothing takes no time');
    /* Halving the throttle doubles the window: the operational trade, exactly. */
    eq(Rtext(Rdiv(rebalanceSeconds(R(1n, 4n), D, R(100n * 10n ** 6n, 1n)),
                  rebalanceSeconds(R(1n, 4n), D, B))), '2',
       'halving the throttle doubles the window');
    eq(Rtext(stolenShare(B, budget)), '1/4', 'the copy holds a quarter of the transfer budget');
    eq(Rtext(serviceDuringMove(R(8000n, 1n), B, budget)), '6000',
       'so the node serves 6000 a second instead of 8000');
    const load = rebalanceLoad(R(5000n, 1n), R(8000n, 1n), B, budget);
    eq(Rtext(load.before.rho), '5/8', 'utilisation before the move');
    eq(Rtext(load.during.rho), '5/6', 'and during it');
    eq(Rtext(load.before.W), '1/3000', "course 3's M/M/1 wait before");
    eq(Rtext(load.during.W), '1/1000', 'and during');
    eq(Rtext(Rdiv(load.during.W, load.before.W)), '3',
       'a gentle-looking quarter of the budget triples the wait');
    /* A throttle at the whole budget stops the node serving, and the page has
       to say so rather than printing a finite wait. */
    const starved = rebalanceLoad(R(5000n, 1n), R(8000n, 1n), budget, budget);
    eq(Rtext(starved.muMove), '0', 'a copy at the full budget leaves no service rate');
    eq(starved.during.stable, false, 'and no steady state at all');
  }
}

/* -----------------------------------------------------------------------
   SYSTEM DESIGN, COURSE 6: replication and consistency.

   Thirteen lessons, one kit, and nothing in it rounds: order statistics from
   enumerated distributions, quorum tails as binomial sums over fractions,
   overlap as combinations, linearizations counted rather than sampled.

   Eleven of the assertions below are not figures but IDENTITIES, and they are
   why this section exists. The per-replica load of the fan-out plan must come
   back as exactly one replica's capacity; the pigeonhole minimum must be
   ATTAINED by some pair and not merely respected; the enumerated count of
   disjoint quorum pairs must equal the closed form; the quorum tail must be
   monotone in N at fixed W, which is the one claim on this course readers
   refuse; the sloppy miss must equal that same disjoint count over all pairs;
   a majority of an even n must be strictly WORSE than of n - 1; the election
   probability must equal a brute-force count over every assignment; a vector
   clock's happens-before must imply a smaller Lamport stamp; the permutation
   generator must produce exactly k!; real time must partition the pairs; and
   the counter CRDT's merge must be commutative, associative and idempotent.
   Each is exact, each is checkable, and each is a claim a lesson makes in
   prose. */
console.log('system design: replication, quorums, clocks and consistency');
{
  const REPLICA_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'replica.py');
  const replicaSrc = fs.readFileSync(REPLICA_SOURCE, 'utf8');
  const replicaBlock = (name) => blockFrom(replicaSrc, name, REPLICA_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('AVAIL_JS')
       + replicaBlock('REPLICA_JS'));

  /* The two distributions the kit ships as its presets, so that what is
     asserted here is what a reader opens the page on. */
  const REPLY = pmfFromSpec(parsePmfSpec('2:600, 4:300, 8:70, 16:22, 24:6, 40:2'));
  const LAG = pmfFromSpec(parsePmfSpec('10:500, 25:300, 50:120, 120:60, 250:15, 400:5'));
  const q99 = R(99n, 100n), q50 = R(1n, 2n), q999 = R(999n, 1000n);

  /* --- printing ----------------------------------------------------------- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(2n, 3n), 3), '66.667%', 'the sloppy-quorum miss as a percentage');
  eq(ninesOf(R(999702n, 1000000n)), 3, 'a majority of three at 99% has three nines');
  eq(RpctAuto(R(999702n, 1000000n)), '99.970200%', 'and prints wide enough to show them');
  eq(RpctAuto(R(1n, 1n)), '100%', 'only an exact one prints as 100%');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 9n))), '99.999999900000%',
     'nine nines gets twelve places rather than rounding to 100%');
  eq(bytesText(2828n), '2.83 kB', 'decimal byte units: 1 kB is 1000 B');
  /* Rfixed exists here because F(t)^(N-1) leaves Number behind: the 24-ms atom
     of the shipped pmf raised to the 8th power has a 24-digit denominator. */
  eq(Rtext(Rpow(R(998n, 1000n), 8)), '3844185754368006996001/3906250000000000000000',
     'F(24) to the 8th is a fraction with no decimal anywhere in it');

  /* --- L1: the four multipliers, and the ceiling the ratio sets ------------ */
  eq(Rtext(fanoutCeiling(R(9n, 1n))), '10', 'nine reads per write caps the speed-up at 10x');
  eq(Rtext(fanoutSpeedup(3, R(9n, 1n))), '5/2', 'three replicas of that workload give 2.5x, not 3x');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).total), '2500',
     'which is 2500 ops/s from three 1000 ops/s replicas');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).readCapacity), '3000', 'reads scale by N');
  eq(Rtext(fanoutPlan(R(1000n, 1n), 3, R(9n, 1n)).writeCapacity), '1000', 'writes do not scale at all');
  /* THE IDENTITY: the plan must saturate a replica exactly. Every replica
     carries all the writes plus 1/N of the reads, and that has to come back as
     one replica's capacity or the throughput formula is wrong. */
  for (const [n, rhoN, c] of [[1, 9, 1000], [3, 9, 1000], [7, 4, 250], [12, 0, 5000], [5, 37, 900]]) {
    const plan = fanoutPlan(R(BigInt(c), 1n), n, R(BigInt(rhoN), 1n));
    eq(Rtext(plan.perReplicaLoad), String(c),
       'a replica is saturated exactly at n = ' + n + ', rho = ' + rhoN);
    eq(Rtext(Radd(plan.reads, plan.writes)), Rtext(plan.total),
       'and the mix adds back to the total at n = ' + n + ', rho = ' + rhoN);
  }
  /* THE IDENTITY: at one replica there is no speed-up, and at rho = 0 -- a
     write-only workload -- there is none at ANY N. Replication does not scale
     writes, and this is the arithmetic of that sentence. */
  for (const rhoN of [0, 1, 9, 60]) {
    eq(Rtext(fanoutSpeedup(1, R(BigInt(rhoN), 1n))), '1', 'one replica is 1x at rho = ' + rhoN);
  }
  for (const n of [1, 2, 5, 12, 100]) {
    eq(Rtext(fanoutSpeedup(n, R(0n, 1n))), '1', 'a write-only workload is 1x at N = ' + n);
  }
  /* The speed-up rises in N and never reaches the ceiling. */
  for (const rhoN of [1, 9, 60]) {
    const rho = R(BigInt(rhoN), 1n);
    for (let n = 1; n < 24; n += 1) {
      eq(Rcmp(fanoutSpeedup(n + 1, rho), fanoutSpeedup(n, rho)) > 0, true,
         'the speed-up rises from N = ' + n + ' at rho = ' + rhoN);
      eq(Rcmp(fanoutSpeedup(n, rho), fanoutCeiling(rho)) < 0, true,
         'and stays under the ceiling at N = ' + n + ', rho = ' + rhoN);
    }
  }

  /* --- L2: the maximum of N - 1, not N times one -------------------------- */
  eq(syncAckPmf(REPLY, 1).length, 1, 'at N = 1 there is no follower to wait for');
  eq(Rtext(syncAckPmf(REPLY, 1)[0][1]), '1', 'so the wait is zero with probability one');
  eq(syncAckPmf(REPLY, 1)[0][0], 0, 'and the value is zero, not one replica');
  /* THE IDENTITY: P(max of k <= t) is F(t)^k at every attainable time. This is
     what the lesson claims and pmfMax is what the page calls. */
  for (const k of [1, 2, 3, 8]) {
    const mx = pmfMax(REPLY, k);
    for (const t of pmfSupport(REPLY)) {
      eq(Rtext(pmfCdfAt(mx, t)), Rtext(Rpow(pmfCdfAt(REPLY, t), k)),
         'P(max of ' + k + ' <= ' + t + ') is F(t) to the ' + k);
    }
  }
  /* THE IDENTITY the lesson states in its key line: P(all N - 1 followers
     acked by t) = F(t)^(N-1). The order of the maximum is N - 1 and not N --
     the leader does not wait for itself -- and the percentiles alone do not
     pin that, because a discrete tail can absorb an off-by-one in the
     exponent without moving the 99th percentile at all. */
  for (const n of [2, 3, 5, 9]) {
    const ack = syncAckPmf(REPLY, n);
    for (const t of pmfSupport(REPLY)) {
      eq(Rtext(pmfCdfAt(ack, t)), Rtext(Rpow(pmfCdfAt(REPLY, t), n - 1)),
         'the sync write is acked by ' + t + ' with probability F(t)^(N-1) at N = ' + n);
    }
  }
  eq(Rtext(pmfMean(syncAckPmf(REPLY, 3))), '147007/31250',
     'and the mean wait of a three-replica sync write is exact');
  eq(Rtext(pmfMean(syncAckPmf(REPLY, 2))), '442/125', 'as is a two-replica one');
  eq(pmfPercentile(REPLY, q99), 16, 'one replica acks by 16 ms 99 times in 100');
  eq(pmfPercentile(syncAckPmf(REPLY, 3), q99), 24, 'synchronising to three costs 24 ms at p99');
  eq(naiveSyncCost(REPLY, 3, q99), 48, 'while "three times one replica" would claim 48');
  eq(pmfPercentile(syncAckPmf(REPLY, 9), q99), 40, 'and nine replicas cost 40, not 144');
  eq(naiveSyncCost(REPLY, 9, q99), 144, 'which is what the naive rule claims at N = 9');
  /* The sync wait is non-decreasing in N and bounded by the slowest atom -- a
     maximum of more copies is never faster and never leaves the support. */
  for (let n = 2; n < 12; n += 1) {
    eq(pmfPercentile(syncAckPmf(REPLY, n + 1), q99) >= pmfPercentile(syncAckPmf(REPLY, n), q99),
       true, 'the sync p99 does not fall as N rises, at N = ' + n);
    eq(pmfPercentile(syncAckPmf(REPLY, n), q99) <= 40, true, 'and never leaves the support');
  }
  eq(Rtext(asyncAtRiskBytes(2000, pmfMean(REPLY), 400)), '14144/5',
     'the async alternative risks writes/s x mean lag x bytes');
  eq(String(bytesFloor(asyncAtRiskBytes(2000, pmfMean(REPLY), 400))), '2828',
     'and a count of bytes is floored, never rounded up into bytes that do not exist');
  eq(bytesText(bytesFloor(asyncAtRiskBytes(2000, pmfMean(REPLY), 400))), '2.83 kB',
     'which reads as 2.83 kB');

  /* --- L3: the tail, and the mass the mean cannot see --------------------- */
  eq(Rtext(pmfMean(LAG)), '629/20', 'the shipped lag averages 31.45 ms');
  eq(Rtext(staleProb(LAG, 50)), '2/25', 'a read 50 ms after the write is stale 8 times in 100');
  eq(Rtext(tailPastRational(LAG, pmfMean(LAG))), '1/5',
     'and waiting for the MEAN still leaves one read in five stale');
  eq(Rtext(staleReadsPerSec(LAG, 50, 12000)), '960', 'which at 12 000 reads/s is 960 a second');
  eq(freshDelay(LAG, q99), 250, '99% freshness needs 250 ms');
  eq(freshDelay(LAG, q999), 400, 'and 99.9% needs 400');
  /* THE IDENTITY: fresh and stale are a partition. */
  for (const t of [0, 9, 10, 24, 25, 50, 119, 120, 250, 399, 400, 1000]) {
    eq(Rtext(Radd(pmfCdfAt(LAG, t), staleProb(LAG, t))), '1',
       'fresh and stale partition the mass at t = ' + t);
  }

  /* --- L4: overlap, claimed and measured ---------------------------------- */
  eq(quorumOverlap(3, 2, 2), 1, 'R + W - N is one at the canonical (3, 2, 2)');
  eq(quorumScan(3, 2, 2).min, 1, 'and the scan over all nine pairs finds exactly one');
  eq(quorumScan(3, 2, 2).disjoint, 0, 'with no disjoint pair');
  eq(quorumScan(3, 1, 1).disjoint, 6, 'while (3, 1, 1) has six disjoint pairs of nine');
  eq(String(subsets(5, 2).length), String(comb(5, 2)), 'the enumeration produces C(n, k) sets');
  eq(subsets(4, 2).map((s) => s.join('')).join(' '), '01 02 03 12 13 23', 'in lexicographic order');
  eq(subsets(3, 0).length, 1, 'and C(n, 0) = 1: the empty set');
  eq(overlapSize([0, 1], [1, 2]), 1, 'two sets sharing one node overlap in one');
  eq(overlapSize([0, 1], [2, 3]), 0, 'and two that share nothing overlap in none');
  eq(overlapSize([0, 1, 2], [2, 1, 0]), 3, 'order does not change the overlap');
  eq(overlapSize([], [0]), 0, 'the empty set meets nothing');
  /* THE IDENTITY, twice over, on every configuration up to seven nodes: the
     pigeonhole minimum is ATTAINED, and the enumerated disjoint count equals
     the closed form C(N, W) x C(N - W, R). A page that asserted the bound
     without measuring it would pass every other test in this file. */
  for (let n = 1; n <= 7; n += 1) {
    for (let r = 1; r <= n; r += 1) {
      for (let w = 1; w <= n; w += 1) {
        const scan = quorumScan(n, r, w);
        eq(scan.min, r + w > n ? r + w - n : 0,
           'the minimum overlap is attained at (' + n + ', ' + r + ', ' + w + ')');
        eq(String(scan.disjoint), String(disjointPairCount(n, r, w)),
           'and the disjoint count matches the formula at (' + n + ', ' + r + ', ' + w + ')');
        eq(scan.pairs, Number(comb(n, r)) * Number(comb(n, w)),
           'over C(n,r) x C(n,w) pairs at (' + n + ', ' + r + ', ' + w + ')');
        eq((scan.witness === null) === quorumOverlaps(n, r, w), true,
           'a witness exists exactly when the configuration does NOT overlap at ('
           + n + ', ' + r + ', ' + w + ')');
      }
    }
  }

  /* --- L5: the binomial tail, and the result readers refuse --------------- */
  /* The two edges of availKofN, on a latency CDF rather than an availability:
     W = 1 is the parallel form and W = N the series one. */
  for (const t of pmfSupport(REPLY)) {
    const F = pmfCdfAt(REPLY, t);
    for (const n of [1, 3, 5]) {
      eq(Rtext(quorumAckBy(REPLY, t, n, n)), Rtext(Rpow(F, n)),
         'waiting for all ' + n + ' is F(t)^' + n + ' at t = ' + t);
      eq(Rtext(quorumAckBy(REPLY, t, 1, n)),
         Rtext(Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), F), n))),
         'waiting for any one of ' + n + ' is 1 - (1 - F)^' + n + ' at t = ' + t);
    }
  }
  /* THE IDENTITY, and it is the lesson: with W fixed the tail is monotone in
     N. More replicas make a quorum write FASTER, and this is that sentence. */
  for (const w of [1, 2, 3, 5]) {
    for (const t of pmfSupport(REPLY)) {
      for (let n = w; n < 12; n += 1) {
        eq(Rcmp(quorumAckBy(REPLY, t, w, n + 1), quorumAckBy(REPLY, t, w, n)) >= 0, true,
           'P(>= ' + w + ' of N by ' + t + ') does not fall from N = ' + n);
      }
    }
  }
  eq(quorumPercentile(REPLY, 2, 2, q99), 24, 'a 2-of-2 quorum has a p99 of 24 ms');
  eq(quorumPercentile(REPLY, 2, 3, q99), 8, 'a 2-of-3 quorum, 8 ms');
  eq(quorumPercentile(REPLY, 2, 4, q99), 4, 'and a 2-of-4 quorum, 4 ms -- faster, on more replicas');
  eq(quorumPercentile(REPLY, 2, 8, q99), 2, 'at eight replicas it is the fastest atom there is');
  eq(quorumSweep(REPLY, 2, 9, q99).map((r) => r.p).join(','), '24,8,4,4,4,4,2,2',
     'the whole sweep, non-increasing all the way down');
  eq(quorumPercentile(REPLY, 5, 4, q99), null, 'a quorum larger than the fleet is never met');
  eq(Rtext(quorumAckBy(REPLY, 2, 0, 3)), '1', 'and a quorum of nobody is met immediately');

  /* --- L6: the sloppy miss ------------------------------------------------ */
  eq(Rtext(sloppyMiss(3, 1, 1)), '2/3', 'two reads in three miss at N = 3, R = W = 1');
  eq(Rtext(sloppyMiss(3, 2, 1)), '1/3', 'R = 2 halves it, and does not remove it');
  eq(Rtext(sloppyMiss(3, 2, 2)), '0', 'R + W > N removes it exactly');
  eq(Rtext(sloppyMiss(5, 2, 3)), '1/10', 'R + W = N is still one read in ten');
  eq(Rtext(sloppyHit(3, 1, 1)), '1/3', 'hit and miss are complements');
  /* THE IDENTITY: the probability is the enumerated disjoint count over all
     pairs. Two different routes to the same fraction, on every configuration. */
  for (let n = 1; n <= 7; n += 1) {
    for (let r = 1; r <= n; r += 1) {
      for (let w = 1; w <= n; w += 1) {
        const scan = quorumScan(n, r, w);
        eq(Rtext(sloppyMiss(n, r, w)), Rtext(R(BigInt(scan.disjoint), BigInt(scan.pairs))),
           'the miss probability is the disjoint share at (' + n + ', ' + r + ', ' + w + ')');
        eq(Rzero(sloppyMiss(n, r, w)), quorumOverlaps(n, r, w),
           'and it is zero exactly when the quorums overlap at ('
           + n + ', ' + r + ', ' + w + ')');
      }
    }
  }

  /* --- L7: 2f + 1, and the node that buys nothing ------------------------- */
  eq(majoritySize(3), 2, 'a majority of three is two');
  eq(majoritySize(4), 3, 'and of four is three');
  eq(faultsTolerated(3), 1, 'three tolerate one');
  eq(faultsTolerated(4), 1, 'and so do four');
  eq(Rtext(majorityAvail(R(99n, 100n), 3)), '499851/500000', '2-of-3 at 99% each');
  eq(RpctAuto(majorityAvail(R(99n, 100n), 3)), '99.970200%', 'which is 99.9702%');
  eq(RpctAuto(majorityAvail(R(99n, 100n), 4)), '99.940797%', 'and 3-of-4 is WORSE');
  /* THE IDENTITY, three ways: the quorum and the tolerance partition the
     cluster; an even size tolerates what the odd size below it does; and its
     majority is strictly less available whenever a node is better than a coin.
     The last is the sentence "a fourth node adds nothing to three", made
     sharper -- it subtracts. */
  for (let n = 1; n <= 20; n += 1) {
    eq(majoritySize(n) + faultsTolerated(n), n, 'quorum plus tolerance is n at n = ' + n);
    eq(2 * faultsTolerated(n) + 1 <= n, true, '2f + 1 fits inside n at n = ' + n);
  }
  for (let k = 1; k <= 10; k += 1) {
    eq(faultsTolerated(2 * k), faultsTolerated(2 * k - 1),
       'an even cluster tolerates what the odd one below it does, at n = ' + (2 * k));
    eq(evenIsWasted(2 * k), true, 'and is flagged as wasted at n = ' + (2 * k));
    eq(evenIsWasted(2 * k - 1), false, 'while the odd size is not, at n = ' + (2 * k - 1));
  }
  for (const a of [R(9n, 10n), R(99n, 100n), R(999n, 1000n), R(3n, 4n)]) {
    for (let k = 1; k <= 6; k += 1) {
      eq(Rcmp(majorityAvail(a, 2 * k), majorityAvail(a, 2 * k - 1)) < 0, true,
         'the majority of ' + (2 * k) + ' is strictly worse than of ' + (2 * k - 1)
         + ' at A = ' + Rtext(a));
    }
  }
  eq(Rtext(majorityAvail(R(3n, 7n), 1)), '3/7', 'a single node IS its own majority');

  /* --- L8: the split vote ------------------------------------------------- */
  eq(Rtext(electionClean(2, 2)), '1/2', 'two candidates over two slots');
  eq(Rtext(electionClean(2, 3)), '2/3', 'two over three');
  eq(Rtext(electionClean(3, 3)), '5/9', 'three over three');
  eq(Rtext(electionTerm(5, 10, 1)), '6561/20000', 'the first term of the lesson preset');
  eq(Rtext(electionTerm(5, 10, 9)), '1/20000', 'the ninth, four orders of magnitude down');
  eq(Rtext(electionTerm(5, 10, 10)), '0',
     'and the last is always zero: nobody can fire later than the last slot');
  eq(Rtext(electionClean(5, 10)), '15333/20000', 'the lesson preset, exactly');
  eq(Rfixed(electionRounds(5, 10), 4), '1.3044', 'so 1.3044 rounds on average');
  eq(Rtext(electionClean(1, 7)), '1', 'one candidate always wins');
  for (const n of [2, 3, 5, 12]) {
    eq(Rtext(electionClean(n, 1)), '0', 'a FIXED timeout is a guaranteed tie at n = ' + n);
    eq(electionRounds(n, 1), null, 'and the expected rounds are not a number');
  }
  /* The window a 95% clean rate needs, by binary search. P(clean) rises with T,
     which is what makes the search exact -- so that is asserted, and then the
     search is checked against the scan it replaced. */
  for (const n of [2, 3, 5, 12]) {
    for (let T = 1; T < 40; T += 1) {
      eq(Rcmp(electionClean(n, T + 1), electionClean(n, T)) > 0, true,
         'a wider window is always cleaner at n = ' + n + ', T = ' + T);
    }
  }
  const scanSlots = (n, target, limit) => {
    for (let k = 1; k <= limit; k += 1) if (Rcmp(electionClean(n, k), target) >= 0) return k;
    return null;
  };
  for (const n of [1, 2, 3, 5, 8, 12]) {
    for (const target of [R(9n, 10n), R(95n, 100n), R(99n, 100n)]) {
      eq(String(slotsForClean(n, target, 400)), String(scanSlots(n, target, 400)),
         'the binary search finds the same window as the scan at n = ' + n
         + ', target ' + Rtext(target));
    }
  }
  eq(slotsForClean(5, R(95n, 100n), 400), 50, 'the lesson preset needs 50 slots for 95% clean');
  eq(slotsForClean(1, R(99n, 100n), 400), 1, 'and one candidate needs one slot');
  eq(slotsForClean(12, R(95n, 100n), 2), null, 'a target out of reach inside the limit returns null');
  /* THE IDENTITY: the closed form equals a brute-force count over every
     assignment of candidates to slots. This is the one assertion here that
     does not trust the algebra at all. */
  const bruteClean = (n, T) => {
    let good = 0;
    const pick = new Array(n).fill(0);
    const walk = (i) => {
      if (i === n) {
        let lo = Infinity, count = 0;
        for (const v of pick) { if (v < lo) { lo = v; count = 1; } else if (v === lo) count += 1; }
        if (count === 1) good += 1;
        return;
      }
      for (let s = 0; s < T; s += 1) { pick[i] = s; walk(i + 1); }
    };
    walk(0);
    return R(BigInt(good), BigInt(T) ** BigInt(n));
  };
  for (const [n, T] of [[1, 3], [2, 2], [2, 5], [3, 3], [3, 4], [4, 4], [5, 3], [2, 1], [4, 1]]) {
    eq(Rtext(electionClean(n, T)), Rtext(bruteClean(n, T)),
       'the closed form matches a brute-force count at n = ' + n + ', T = ' + T);
  }

  /* --- L9, L10: the two clocks on one diagram ----------------------------- */
  const DIAG = parseDiagram('A:4 B:4 C:3; A2 to B2; B3 to C2; C1 to A4');
  eq(DIAG === null, false, 'the shipped diagram parses');
  eq(DIAG.procs.length, 3, 'three processes');
  eq(DIAG.msgs.length, 3, 'and three messages');
  eq(parseDiagram('A:4 B:4 C:3; A2>B2; B3>C2; C1>A4').msgs.length, 3,
     'and ">" is accepted as the arrow too, for a reader who types it');
  eq(parseDiagram('A:2 B:2; A2 to B1; B2 to A1') && lamportStamps(parseDiagram('A:2 B:2; A2 to B1; B2 to A1')),
     null, 'a message received before it was sent has no topological order');
  eq(parseDiagram('A:2 B:2; A1 to B1; A1 to B2'), null, 'one event cannot send twice');
  eq(parseDiagram('A:2 B:2; A1 to B1; A2 to B1'), null, 'nor can one event receive twice');
  eq(parseDiagram('A:2; A1 to A2'), null, 'a process cannot message itself');
  eq(parseDiagram('A:2 B:2; A9 to B1'), null, 'nor can it send from an event it does not have');
  eq(parseDiagram('A:2 A:2'), null, 'and a process may not be declared twice');
  eq(diagramEvents(DIAG).length, 11, 'eleven events across the three processes');
  eq(diagramOrder(diagramEvents(DIAG)).length, 11,
     'and they have a topological order, so every stamp has its inputs before it');
  eq(diagramOrder(diagramEvents(parseDiagram('A:2 B:2; A2 to B1; B2 to A1'))), null,
     'a diagram whose messages make a cycle has none, and the page says so');
  const L = lamportStamps(DIAG), V = vectorStamps(DIAG), EV = diagramEvents(DIAG);
  eq(L.join(','), '1,2,3,4,1,3,4,5,1,5,6', 'the Lamport stamps of the shipped diagram');
  eq(V.map((v) => v.join('')).join(' '), '100 200 300 401 010 220 230 240 001 232 233',
     'and its vectors');
  eq(concurrentPairs(V).length, 23, '23 of its 55 pairs are concurrent');
  eq(lamportFalsePairs(L, V).length, 17, 'and 17 ordered pairs have L(a) < L(b) with a NOT before b');
  /* THE IDENTITY: Lamport is sound and not complete. a -> b implies L(a) < L(b)
     on every diagram; the converse fails, and the vector clock is what knows. */
  for (const spec of ['A:4 B:4 C:3; A2 to B2; B3 to C2; C1 to A4',
                      'A:2 B:2; A1 to B1; B2 to A2',
                      'A:1',
                      'A:3 B:3 C:3 D:3; A1 to B1; B2 to C2; C3 to D3',
                      'A:5 B:5; A3 to B4']) {
    const d = parseDiagram(spec), l = lamportStamps(d), v = vectorStamps(d);
    eq(lamportConsistent(l, v), true, 'happens-before implies a smaller stamp on ' + spec);
    for (let i = 0; i < v.length; i += 1) {
      eq(vecCompare(v[i], v[i]), 0, 'a vector equals itself on ' + spec);
      for (let j = 0; j < v.length; j += 1) {
        const ab = vecCompare(v[i], v[j]), ba = vecCompare(v[j], v[i]);
        eq(ab === null ? ba === null : ab === -ba, true,
           'the comparison is antisymmetric on ' + spec);
      }
    }
    eq(concurrentPairs(v).length + (v.length * (v.length - 1)) / 2 - concurrentPairs(v).length,
       (v.length * (v.length - 1)) / 2, 'concurrent and ordered partition the pairs on ' + spec);
  }
  /* The sequential diagram has no concurrency at all, which is the control:
     a page that reported concurrent pairs here would be reporting noise. */
  eq(concurrentPairs(vectorStamps(parseDiagram('A:6'))).length, 0,
     'one process alone has nothing concurrent');
  eq(lamportStamps(parseDiagram('A:6')).join(','), '1,2,3,4,5,6', 'and its stamps just count');

  /* --- L11: drift, skew, commit-wait -------------------------------------- */
  eq(Rtext(skewMicros(200, 30)), '6000', '200 ppm over 30 s is 6000 microseconds');
  eq(Rtext(commitWaitMicros(200, 30)), '12000', 'and the comparison window is twice that');
  eq(orderTrustworthy(R(5000n, 1n), 200, 30), false, 'a 5 ms gap is inside a 12 ms window');
  eq(orderTrustworthy(R(20000n, 1n), 200, 30), true, 'a 20 ms gap clears it');
  eq(orderTrustworthy(R(12000n, 1n), 200, 30), false, 'and the boundary is not trustworthy either');
  eq(Rtext(windowRatio(R(5000n, 1n), 200, 30)), '12/5', 'the window is 2.4x that separation');
  eq(windowRatio(R(0n, 1n), 200, 30), null, 'two simultaneous events have no ratio');
  /* A ppm figure is microseconds per second by definition, so halving the sync
     interval halves the window exactly -- no rounding anywhere in the chain. */
  for (const [ppm, iv] of [[10, 60], [50, 10], [100, 30], [500, 600]]) {
    eq(Rtext(commitWaitMicros(ppm, iv)), Rtext(Rmul(R(2n, 1n), skewMicros(ppm, iv))),
       'the commit-wait is 2 epsilon at ' + ppm + ' ppm / ' + iv + ' s');
    eq(Rtext(skewMicros(ppm, 2 * iv)), Rtext(Rmul(R(2n, 1n), skewMicros(ppm, iv))),
       'and doubling the interval doubles the skew at ' + ppm + ' ppm');
  }

  /* --- L12: linearizability, counted -------------------------------------- */
  /* THE IDENTITY: the generator produces exactly k! orders. The lesson quotes
     that number as its reason for the cap, so it had better be the number the
     enumeration actually walks. */
  for (let k = 0; k <= 6; k += 1) {
    eq(permutations(k).length, Number(fact(k)), 'the generator produces ' + k + '! orders');
    eq(new Set(permutations(k).map((p) => p.join(','))).size, Number(fact(k)),
       'all distinct at k = ' + k);
  }
  const H_BAD = parseHistory('A w1[0,4]; B r1[2,6]; C r0[5,9]');
  const H_OK = parseHistory('A w1[0,4]; B r1[2,6]; C r1[5,9]');
  const H_SIX = parseHistory('A w1[0,2]; B r1[1,4]; C w2[3,6]; D r2[5,8]; E r2[7,10]; F r2[9,12]');
  eq(H_BAD.length, 3, 'the lesson history has three operations');
  eq(linearizations(H_BAD, 0).total, 6, 'six total orders');
  eq(linearizations(H_BAD, 0).realTime, 3, 'three of which real time allows');
  eq(linearizations(H_BAD, 0).valid.length, 0, 'and NONE is legal: the history is a violation');
  eq(linearizations(H_OK, 0).valid.length, 2, 'one return value later, two orders are legal');
  eq(linearizations(H_SIX, 0).total, 720, 'the six-operation history has 720 orders');
  eq(linearizations(H_SIX, 0).realTime, 13, '13 of which real time allows');
  eq(linearizations(H_SIX, 0).valid.length, 3, 'and 3 are legal');
  eq(parseHistory('A w1[4,4]'), null, 'an operation must return after it was invoked');
  eq(parseHistory('A w1[0,4], B r1[2,6]'), null,
     'operations are separated by semicolons -- the comma lives inside the interval');
  eq(parseHistory('A z1[0,4]'), null, 'and an operation is a read or a write');
  eq(historyPairs(H_BAD).forced, 1, 'real time decides one pair of the three');
  eq(historyPairs(H_BAD).concurrent, 2, 'and leaves two free');
  eq(historyPairs(H_SIX).forced, 10, 'ten of the fifteen pairs are decided on the six-op history');
  eq(historyPairs(H_SIX).concurrent, 5, 'and five are concurrent');
  /* The order the operations are TYPED in is not the order they ran in, so the
     real-time test has to look both ways round. */
  eq(historyPairs(parseHistory('C r1[5,9]; A w1[0,4]')).forced, 1,
     'a history typed out of time order still has its pair decided');
  eq(historyPairs(parseHistory('C r1[5,9]; A w1[0,4]')).concurrent, 0, 'with none left free');
  eq(realTimeBefore(H_BAD[0], H_BAD[2]), true, 'A returned at 4 before C was invoked at 5');
  eq(realTimeBefore(H_BAD[0], H_BAD[1]), false, 'but it overlaps B');
  eq(orderLegal(H_OK, [0, 1, 2], 0), true, 'write 1 then two reads of 1 is legal');
  eq(orderLegal(H_BAD, [0, 1, 2], 0), false, 'a read of 0 after a write of 1 is not');
  eq(orderLegal([], [], 3), true, 'and the empty order is vacuously legal');
  /* THE IDENTITY: real time decides some pairs and leaves the rest free, and
     the two counts are C(k, 2). The enumeration searches exactly the freedom. */
  for (const h of [H_BAD, H_OK, H_SIX,
                   parseHistory('A w1[0,3]; B w2[1,5]; C r1[4,8]; D r2[6,10]')]) {
    const pairs = historyPairs(h);
    eq(pairs.forced + pairs.concurrent, Number(comb(h.length, 2)),
       'forced and concurrent pairs are C(k, 2) on a ' + h.length + '-operation history');
    const res = linearizations(h, 0);
    eq(res.realTime <= res.total, true, 'real time can only remove orders');
    eq(res.valid.length <= res.realTime, true, 'and legality can only remove more');
    /* Every order the enumeration calls valid must survive an independent
       replay -- the count means nothing if the orders it counted do not. */
    for (const p of res.valid) {
      eq(orderRespectsRealTime(h, p) && orderLegal(h, p, 0), true,
         'a counted order really is valid on a ' + h.length + '-operation history');
    }
  }

  /* --- L13: what each merge throws away ----------------------------------- */
  const TRACE = parseTrace('A:3:+2, B:5:+3, C:4:+1, B:9:+4');
  eq(TRACE.length, 4, 'the lesson trace has four updates');
  eq(traceTotal(TRACE), 10, 'worth ten between them');
  eq(lwwMerge(TRACE).winner, 'B', 'B holds the largest timestamp');
  eq(lwwMerge(TRACE).value, 7, 'so last-writer-wins returns seven');
  eq(lwwMerge(TRACE).lost.length, 2, 'discarding two updates');
  eq(lwwMerge(TRACE).discarded, 3, 'worth three');
  eq(crdtValue(crdtCounts(TRACE)), 10, 'while the counter CRDT returns the true ten');
  eq(JSON.stringify(crdtCounts(TRACE)), '{"A":2,"B":7,"C":1}', 'from these per-replica counts');
  eq(lwwMerge(parseTrace('A:5:+1, B:5:+2')).winner, 'B',
     'a tie on the timestamp is broken by replica name, as a real LWW register does');
  eq(lwwMerge(parseTrace('A:5:+1, B:5:+2')).tieBroken, true, 'and the page is told that it was');
  eq(lwwMerge(parseTrace('A:1:+1, A:2:+5')).lost.length, 0,
     'updates at one replica lose nothing: concurrency is the whole problem');
  eq(parseTrace('A:1:-1'), null, 'a grow-only counter grows');
  eq(parseTrace('A:1'), null, 'and an update needs a replica, a timestamp and a delta');
  /* THE IDENTITY: the CRDT loses nothing and LWW loses everything off the
     winner, on every trace; and the merge obeys its three laws, which is WHY
     the replicas converge whatever order they gossip in. */
  for (const spec of ['A:3:+2, B:5:+3, C:4:+1, B:9:+4',
                      'A:1:+1, B:2:+2, C:3:+3, D:4:+4, E:5:+5',
                      'A:7:+9',
                      'A:5:+1, B:5:+2, C:5:+3',
                      'B:2:+4, B:3:+4, A:9:+1']) {
    const tr = parseTrace(spec), counts = crdtCounts(tr), lww = lwwMerge(tr);
    eq(crdtValue(counts), traceTotal(tr), 'the CRDT loses nothing on ' + spec);
    eq(lww.value + lww.discarded, traceTotal(tr), 'and LWW loses exactly the rest on ' + spec);
    eq(lww.kept.length + lww.lost.length, tr.length, 'every update is kept or lost on ' + spec);
    eq(lww.value <= traceTotal(tr), true, 'LWW never invents value on ' + spec);
    const st = replicaStates(tr), names = traceReplicas(tr);
    const a = st[names[0]], b = st[names[1]] || a, c = st[names[2]] || b;
    eq(countsEqual(crdtJoin(a, b), crdtJoin(b, a)), true, 'the merge is commutative on ' + spec);
    eq(countsEqual(crdtJoin(crdtJoin(a, b), c), crdtJoin(a, crdtJoin(b, c))), true,
       'associative on ' + spec);
    eq(countsEqual(crdtJoin(crdtJoin(a, b), crdtJoin(a, b)), crdtJoin(a, b)), true,
       'and idempotent on ' + spec);
    /* Joining every replica's own state must reach the same vector as counting
       the trace directly -- gossip converges on the answer. */
    let merged = {};
    for (const nm of names) merged = crdtJoin(merged, st[nm]);
    eq(countsEqual(merged, counts), true, 'gossip converges on the full count for ' + spec);
    eq(crdtValue(merged), traceTotal(tr), 'and on the true total for ' + spec);
  }
}

console.log('system design: storage engines, amplification, filters and recovery');
{
  const STORAGE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'storage.py');
  const storageSrc = fs.readFileSync(STORAGE_SOURCE, 'utf8');
  const storageBlock = (name) => blockFrom(storageSrc, name, STORAGE_SOURCE);
  const CACHE_SRC = path.join(__dirname, 'mathpath', 'labs', 'cache.py');
  const cacheSrc2 = fs.readFileSync(CACHE_SRC, 'utf8');
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('HARMONIC_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('APPROX_JS') + storageBlock('STORAGE_JS')
       /* the cache kit's own Zipf wrapper, so L10 can be pinned against the
          course it borrows from rather than merely described as sharing it */
       + blockFrom(cacheSrc2, 'CACHE_JS', CACHE_SRC));

  /* --- printing. Rnum goes through Number and this course overflows it. --- */
  eq(Rfix(R(1n, 3n), 3), '0.333', 'long division in BigInt');
  eq(Rfix(R(2n, 3n), 3), '0.667', 'rounded half up at the last digit');
  eq(Rfix(R(-1n, 3n), 3), '-0.333', 'the sign survives the division');
  eq(grp(62500000), '62 500 000', 'digit grouping');
  eq(byteText(R(4000n, 1n)), '4.00 kB', 'a kB is 1000 B on this course, and it says so');
  eq(byteText(R(1000000000n, 1n)), '1.00 GB', 'and a GB is 10^9 B');
  eq(secText(R(1n, 100n)), '10.00 ms', 'ten milliseconds');
  eq(secText(R(2510n, 1n)), '41.8 min', 'and forty-two minutes is printed as minutes');

  /* --- L1: the pattern, not the size -------------------------------------
     The lesson's headline is a RATIO, and asserting the two times separately
     would not catch a bandwidth term that was right in one and wrong in the
     other. 1 GB in 4 kB chunks on a 10 ms / 100 MB/s disk. */
  const GB = R(1000000000n, 1n), CHUNK = R(4000n, 1n);
  const SEEK = R(1n, 100n), BW = R(100000000n, 1n);
  eq(seekCount(GB, CHUNK), 250000n, 'a gigabyte in 4 kB reads is 250 000 seeks');
  eq(Rtext(seqTime(GB, SEEK, BW)), '1001/100', 'sequential: one seek and then the bytes');
  eq(Rtext(randomTime(GB, CHUNK, SEEK, BW)), '2510', 'random: 250 000 seeks and the same bytes');
  eq(Rtext(ioRatio(GB, CHUNK, SEEK, BW)), '251000/1001', 'the ratio the lesson quotes as ~250');
  eq(Rfix(ioRatio(GB, CHUNK, SEEK, BW), 2), '250.75', 'and 250.75 is what 250 is short for');
  /* The bytes term is IDENTICAL in both, which is the whole claim: everything
     that differs between a sequential and a random read is the seek count. */
  eq(Rtext(Rsub(randomTime(GB, CHUNK, SEEK, BW), seqTime(GB, SEEK, BW))),
     Rtext(Rmul(R(249999n, 1n), SEEK)), 'the difference is exactly 249 999 extra seeks');
  eq(Rtext(crossoverChunk(SEEK, BW)), '1000000', 'the crossover chunk is t_seek * bw = 1 MB');
  /* At the crossover the two terms of the formula are equal. That is the
     DEFINITION of the crossover, and it is checked rather than restated. */
  {
    const cross = crossoverChunk(SEEK, BW);
    const seeks = seekCount(GB, cross);
    eq(Rtext(Rmul(R(seeks, 1n), SEEK)), Rtext(Rdiv(GB, BW)),
       'at the crossover chunk the seek term equals the byte term');
  }
  /* The same arithmetic on hardware two orders of magnitude quicker to seek:
     the 250 collapses to 13.5, which is the lesson's solid-state preset. */
  eq(Rfix(ioRatio(GB, CHUNK, R(1n, 10000n), R(500000000n, 1n)), 2), '13.50',
     'an SSD turns the 250x into 13.5x');
  eq(byteText(crossoverChunk(R(1n, 10000n), R(500000000n, 1n))), '50.00 kB',
     'and moves the crossover from 1 MB to 50 kB');

  /* --- L2: the height, by integer search ---------------------------------
     The boundary is the whole reason this is a search and not a logarithm. */
  eq(btreeHeight(1000000000n, 500), 4, 'a billion keys at B = 500 is four levels');
  eq(String(btreeCapacity(500, 3)), '125000000', 'three levels reach 125 million, short of it');
  eq(String(btreeCapacity(500, 4)), '62500000000', 'and four reach 62.5 billion');
  eq(lookupIos(1000000000n, 500, 2), 2, 'with two levels cached a lookup is two page reads');
  eq(lookupIos(1000000000n, 500, 9), 0, 'caching more levels than exist is not negative work');
  eq(lookupIos(1000000000n, 500, 0), 4, 'and caching none is the full height');
  eq(btreeHeight(1, 500), 1, 'one key still costs a page');
  eq(btreeHeight(500, 500), 1, 'N = B exactly is ONE level, not two');
  eq(btreeHeight(501, 500), 2, 'and one key more is two');
  eq(btreeHeight(100, 1), null, 'a fanout of one never covers N, and says so');
  /* Exact at every whole power of B -- including the four where the floating
     point logarithm is not, which is why the lab prints both. */
  [[3, 2], [5, 3], [6, 3], [7, 3], [8, 7], [14, 2], [18, 3], [19, 5], [12, 13], [500, 4]]
    .forEach(([b, h]) => {
      const n = BigInt(b) ** BigInt(h);
      eq(btreeHeight(n, b), h, 'B = ' + b + ', N = B^' + h + ' is exactly ' + h + ' levels');
      eq(btreeHeight(n + 1n, b), h + 1, 'and one key past it is ' + (h + 1));
    });
  eq(btreeHeightByLog(9, 3), 3, 'Math.ceil(log 9 / log 3) says three levels');
  eq(btreeHeight(9, 3), 2, 'and the integer search says two, which is the right answer');
  eq(btreeHeightByLog(125, 5), 4, 'the logarithm is wrong at B = 5, N = 125 too');
  eq(btreeHeight(125, 5), 3, 'where the search gives three');

  /* --- L3: a workload mix, in I/Os --------------------------------------- */
  eq(pagesFor(1000000, 200), 5000n, 'a million rows at 200 a page is 5000 pages');
  eq(hashPointIos(), 1n, 'a hash point lookup is one I/O');
  eq(hashRangeIos(1000000, 200), 5000n, 'and a hash RANGE is the whole table');
  eq(treePointIos(1000000, 500), 3n, 'the tree pays its height on a point lookup');
  eq(treeRangeIos(1000000, 500, 100, 200), 3n, 'and height - 1 plus the leaves on a range');
  eq(Rtext(mixIos(900, 100, hashPointIos(), hashRangeIos(1000000, 200))), '500900',
     'the hash does half a million I/O a second on this mix');
  eq(Rtext(mixIos(900, 100, treePointIos(1000000, 500), treeRangeIos(1000000, 500, 100, 200))),
     '3000', 'and the tree does three thousand');
  eq(Rtext(rangeCrossover(900, 1n, 5000n, 3n, 3n)), '1800/4997',
     'a third of a range query a second is enough to flip the choice');
  /* The crossover is a TIE, and the tie is checked rather than asserted: at
     that range rate the two engines cost the same, exactly. */
  {
    const r = rangeCrossover(900, 1n, 5000n, 3n, 3n), p = R(900n, 1n);
    const h = Radd(Rmul(p, R(1n, 1n)), Rmul(r, R(5000n, 1n)));
    const t = Radd(Rmul(p, R(3n, 1n)), Rmul(r, R(3n, 1n)));
    eq(Rtext(h), Rtext(t), 'at the crossover rate both engines do the same I/O');
  }
  eq(rangeCrossover(900, 1n, 7n, 3n, 7n), null, 'and nothing ties them when the ranges cost the same');

  /* --- L4: the write cost of an index ------------------------------------ */
  eq(Rtext(writesPerInsert(0)), '1', 'no indexes: one write');
  eq(Rtext(writesPerInsert(3)), '4', 'three indexes: four writes');
  eq(Rtext(insertRate(10000, 3)), '2500', '10 000 random writes a second is 2500 inserts');
  eq(Rtext(throughputShare(3)), '1/4', 'a quarter of the bare rate');
  eq(String(indexesForShare(R(1n, 2n))), '1', 'the k that HALVES throughput is one, computed');
  eq(String(indexesForShare(R(1n, 3n))), '2', 'a third takes two');
  eq(String(indexesForShare(R(2n, 5n))), '2', 'and two fifths takes two as well');
  eq(String(maxIndexesFor(10000, 2500)), '3', 'three indexes still meet 2500 inserts a second');
  eq(String(maxIndexesFor(10000, 3000)), '2', 'only two meet 3000');
  eq(maxIndexesFor(10000, 20000), null, 'and no number of indexes meets 20 000');
  /* The bound is tight in both directions, which a single equality would not
     show: k meets the target and k + 1 does not. */
  [[10000, 2500], [10000, 3000], [7500, 1200], [50000, 9000]].forEach(([d, t]) => {
    const k = maxIndexesFor(d, t);
    eq(Rcmp(insertRate(d, Number(k)), R(BigInt(t), 1n)) >= 0, true,
       d + '/s at k = ' + k + ' still meets ' + t);
    eq(Rcmp(insertRate(d, Number(k) + 1), R(BigInt(t), 1n)) < 0, true,
       'and k = ' + (Number(k) + 1) + ' does not');
  });

  /* --- L5: write amplification ------------------------------------------- */
  eq(Rtext(lsmWriteAmp(5, 10)), '25', 'L = 5, F = 10 rewrites each byte 25 times');
  eq(Rtext(lsmWriteAmp(7, 11)), '77/2', 'and an odd product stays a fraction, not a rounding');
  eq(Rtext(lsmReadAmp(5)), '5', 'read amplification before filters is L');
  eq(byteText(compactionBw(R(50000000n, 1n), lsmWriteAmp(5, 10))), '1.25 GB',
     '50 MB/s of ingest needs 1.25 GB a second of disk');
  eq(byteText(levelCapacity(R(64000000n, 1n), 10, 5)), '6.40 TB', 'the fifth level holds 6.4 TB');
  eq(levelsForSize(R(1000000000000n, 1n), R(64000000n, 1n), 10), 5,
     'a terabyte over a 64 MB memtable at F = 10 forces five levels');
  /* The same boundary discipline as the B-tree height, and for the same
     reason: at an exact power the answer is L, not L + 1. */
  eq(levelsForSize(R(6400000000000n, 1n), R(64000000n, 1n), 10), 5, 'exactly 10^5 memtables is five');
  eq(levelsForSize(R(6400000000001n, 1n), R(64000000n, 1n), 10), 6, 'and one byte more is six');
  eq(levelsForSize(R(1000000n, 1n), R(64000000n, 1n), 10), 0, 'data inside the memtable needs no level');
  eq(levelsForSize(R(1000000000000n, 1n), R(64000000n, 1n), 1), null, 'a fanout of one never fills');

  /* --- L6: bits per key, and WHICH constant --------------------------------
     The whole point of the rewritten lesson is that 9.57 is the two-digit
     constant's answer and 9.585 is the constant's own. Both are pinned, and so
     is the gap, because a lab that printed one under the other's name would
     look entirely reasonable. */
  near(bitsPerKeyApprox(0.01), 9.585058, 1e-6, '1% costs 9.585 bits per key, at 1/ln2');
  near(bitsPerKeyTextbook(0.01), 9.567153, 1e-6, 'and 9.567 at the textbook 1.44');
  near(bitsPerKeyApprox(0.01) - bitsPerKeyTextbook(0.01), 0.017905, 1e-6,
       'the two differ in the second decimal, which is the lesson');
  near(bitsPerKeyApprox(0.001), 14.377587, 1e-6, '0.1% costs 14.38 bits per key');
  near(bitsPerKeyApprox(0.1), 4.792529, 1e-6, 'and 10% costs 4.79');
  /* Independent of n: that is the claim, so it is checked at three sizes. */
  [1e6, 1e9, 1e11].forEach((n) => {
    near(bloomBits(n, 0.01) / n, bitsPerKeyApprox(0.01), 1e-6,
         'bits per key is the same at n = ' + n);
  });
  eq(bloomHashes(0.01), 7, 'k = log2(1/p) rounds to seven hashes at 1%');
  eq(bloomHashes(0.001), 10, 'ten at 0.1%');
  eq(bloomHashes(0.5), 1, 'and never fewer than one');
  eq(byteText(bloomMemoryBytes(1e9, 0.01)), '1.20 GB', 'a billion keys at 1% is 1.2 GB of filter');
  /* The EXACT form, as a rational, beside the approximation every figure on
     the page uses. They are NOT the same number, and that is the point of
     printing both: 3% apart at this size. */
  {
    const exact = bloomExactRate(64, 8, 5);
    eq(Rfix(exact, 8), '0.02230073', 'the exact (1-(1-1/m)^kn)^k at m=64, n=8, k=5');
    eq(String(exact.d).length, 362, 'which is a fraction with a 362-digit denominator');
    near(bloomApprox(64, 8, 5), 0.02167922, 1e-8, 'the approximation gives 0.021679');
    near(Rfix(exact, 8) - bloomApprox(64, 8, 5), 0.00062151, 1e-7,
         'so the approximation is 2.8% low here, and the page shows both');
  }
  eq(bloomExactRate(100000, 8, 5), null, 'past a printable size it returns null, not a rounding');
  eq(bloomExactRate(64, 200, 5), null, 'and the same when kn is past it');
  eq(Rtext(readAmpWithFilter(5, R(1n, 100n))), '26/25',
     'a filter per level turns RA of 5 into 1 + 4/100, exactly');
  eq(Rtext(readAmpWithFilter(5, R(0n, 1n))), '1', 'a perfect filter would make it one');
  eq(Rtext(readAmpWithFilter(5, R(1n, 1n))), '5', 'and a useless one leaves it at L');
  /* expNegApprox is what bloomApprox is built on, and it was wrong in a way
     that looked right: the alternating series for e^-x cancels. The
     positive-term form is accurate across the whole range, including where
     the old one returned a NEGATIVE probability. */
  near(expNegApprox(0), 1, 1e-15, 'e^-0 is one');
  [1, 5, 17, 20, 21, 50, 200, 600].forEach((x) => {
    near(expNegApprox(x) / Math.exp(-x), 1, 1e-12, 'e^-' + x + ' is accurate to 1e-12 relative');
  });
  eq(expNegApprox(21) > 0, true, 'and never returns a negative probability');

  /* --- L7: the RUM triple ------------------------------------------------- */
  {
    const lev = rumLevelled(5, 10), tier = rumTiered(5, 10);
    const bt = rumBtree(4, 4000, 128, R(2n, 3n));
    eq([lev.read, lev.write, lev.space].map(Rtext).join('/'), '5/25/11/10', 'levelled: 5, 25, 1.1');
    eq([tier.read, tier.write, tier.space].map(Rtext).join('/'), '50/5/10', 'tiered: 50, 5, 10');
    eq([bt.read, bt.write, bt.space].map(Rtext).join('/'), '4/125/4/3/2', 'B-tree: 4, 31.25, 1.5');
    /* The lesson's claim is that no engine wins all three. Asserted as three
       comparisons rather than as prose, so a change that quietly made one
       engine dominate would fail here. */
    eq(Rcmp(tier.write, lev.write) < 0, true, 'tiered writes less than levelled');
    eq(Rcmp(tier.read, lev.read) > 0, true, 'and reads more');
    eq(Rcmp(tier.space, lev.space) > 0, true, 'and keeps more copies');
    eq(Rcmp(bt.read, lev.read) < 0, true, 'the B-tree reads in fewer I/Os than either LSM');
    eq(Rcmp(bt.write, tier.write) > 0, true, 'and writes a whole page to change a row');
    /* The shares are a probability vector, which is what lets them be plotted. */
    [lev, tier, bt].forEach((t, i) => {
      const sh = rumShares(t);
      eq(Rtext(Radd(Radd(sh.read, sh.write), sh.space)), '1',
         'the three shares of engine ' + i + ' sum to one');
    });
    eq(byteText(compactionBw(R(50000000n, 1n), tier.write)), '250.00 MB',
       'tiered needs 250 MB a second of disk at 50 MB/s of ingest');
    eq(byteText(compactionBw(R(50000000n, 1n), lev.write)), '1.25 GB', 'levelled needs five times that');
  }

  /* --- L8: fsync and group commit ----------------------------------------- */
  {
    const TF = R(1n, 100n), LAM = R(5000n, 1n);
    eq(Rtext(durableCap(TF)), '100', 'a 10 ms fsync caps durable writes at 100 a second');
    eq(Rtext(groupedCap(TF, 64)), '6400', 'grouping 64 makes it 6400 on the same disk');
    eq(Rtext(perWriteCost(TF, 64)), '1/6400', 'each write carries 1/64 of the fsync');
    eq(Rtext(perWriteCost(TF, 1)), '1/100', 'and alone it carries all of it');
    eq(Rtext(fillWait(1, LAM)), '0', 'a batch of one waits for nobody');
    eq(Rtext(fillWait(64, LAM)), '63/10000', 'and a batch of 64 waits 6.3 ms at 5000/s');
    /* The cap arrives as a QUEUEING fact: at B = 1 and 5000 arrivals a second
       the commit queue is unstable, which is what "capped at 1/t" means. */
    eq(commitLatency(TF, 1, LAM).stable, false, 'one fsync per write cannot keep up with 5000/s');
    eq(Rtext(commitLatency(TF, 1, LAM).rho), '50', 'it is fifty times oversubscribed');
    eq(commitLatency(TF, 64, LAM).stable, true, 'grouping 64 makes it stable');
    eq(Rtext(commitLatency(TF, 64, LAM).rho), '25/32', 'at rho = 0.78125');
    eq(commitLatency(TF, 1, R(50n, 1n)).stable, true, 'and at 50 arrivals a second B = 1 is fine');
    /* The optimum is SCANNED. Checking only its position would not catch a
       scan that returned a batch size whose latency was not actually least. */
    {
      const best = bestBatch(TF, LAM, 256);
      eq(best.batch, 121, 'the batch that minimises commit latency here is 121');
      eq(secText(best.total), '29.04 ms', 'at 29.04 ms all in');
      for (let B = 1; B <= 256; B += 1) {
        const c = commitLatency(TF, B, LAM);
        if (c.stable && Rcmp(c.total, best.total) < 0) {
          eq(B, best.batch, 'no batch beats the one the scan returned');
        }
      }
      eq(Rcmp(commitLatency(TF, 64, LAM).total, best.total) > 0, true,
         'and the round 64 is worse than it');
      eq(Rcmp(commitLatency(TF, 256, LAM).total, best.total) > 0, true,
         'and so is 256, so the minimum is interior');
    }
    eq(bestBatch(TF, R(50000n, 1n), 256), null, 'past 1/t * maxB no batch keeps up, and it says so');
  }

  /* --- L9: row against column --------------------------------------------- */
  {
    const ROWS = 1000000000, RR = R(2n, 1n), CR = R(5n, 1n), BW1 = R(1000000000n, 1n);
    eq(Rtext(columnBytes(200, 20)), '10', 'twenty columns of a 200-byte row are 10 B each');
    eq(byteText(rowScanBytes(ROWS, 200, RR)), '100.00 GB', 'the row store reads 100 GB');
    eq(byteText(colScanBytes(ROWS, 200, 20, 3, CR)), '6.00 GB', 'the column store reads 6 GB');
    eq(secText(scanSeconds(rowScanBytes(ROWS, 200, RR), BW1)), '100.00 s', 'a hundred seconds');
    eq(secText(scanSeconds(colScanBytes(ROWS, 200, 20, 3, CR), BW1)), '6.00 s', 'against six');
    eq(Rtext(Rdiv(rowScanBytes(ROWS, 200, RR), colScanBytes(ROWS, 200, 20, 3, CR))), '50/3',
       'a factor of 16.67, from three columns and a better ratio');
    eq(Rtext(colCrossover(20, RR, CR)), '50', 'the scans would tie at 50 columns, past the 20 there are');
    eq(Rtext(colCrossover(20, RR, RR)), '20', 'at equal compression they tie at every column');
    /* And the query where columnar loses, which is the misconception. */
    eq(wholeRowIos(20, 'row'), 1n, 'one whole row is one page in a row store');
    eq(wholeRowIos(20, 'column'), 20n, 'and one page per column in a column store');
    let threw = false;
    try { wholeRowIos(20, 'hybrid'); } catch (e) { threw = true; }
    eq(threw, true, 'an unknown layout throws rather than defaulting to a row store');
  }

  /* --- L10: the page cache IS course 4's cache ----------------------------
     Not described as shared -- pinned. wsHit's exact branch and the cache
     kit's zipfShare are evaluated here from their own shipped sources, and
     they must agree digit for digit. */
  {
    const PAGE = R(8000n, 1n);
    eq(pageCount(R(500000000000n, 1n), PAGE), 62500000n, '500 GB is 62.5 million 8 kB pages');
    eq(pageCount(R(64000000000n, 1n), PAGE), 8000000n, 'and 64 GB is eight million');
    for (const [c, n, s] of [[4, 40, 1], [10, 40, 2], [1, 40, 1], [25, 40, 3]]) {
      eq(Rtext(wsHit(c, n, s, 40).exact), Rtext(zipfShare(c, n, s, 40).exact),
         'storage and cache agree exactly at C = ' + c + ', N = ' + n + ', s = ' + s);
      eq(Rtext(wsHit(c, n, s, 40).exact), Rtext(zipfHit(c, n, s)),
         'and both are the core zipfHit, not a second implementation');
    }
    eq(wsHit(4, 40, 1, 40).rounded, false, 'inside the limit the figure is an exact fraction');
    eq(wsHit(8000000, 62500000, 1, 40).rounded, true, 'and past it the lab reports that it rounds');
    near(wsHit(8000000, 62500000, 1, 40).value, 0.889047, 1e-5,
         '64 GB of a 500 GB dataset at s = 1 holds 88.9% of the reads');
    /* s = 0 is the control, and it stays EXACT at any size because H(n,0) = n.
       A lab that rounded it would be rounding C/N. */
    eq(wsHit(8000000, 62500000, 0, 40).rounded, false, 'the uniform case never rounds');
    eq(Rtext(wsHit(8000000, 62500000, 0, 40).exact), '16/125', 'it is C/N: 12.8%');
    eq(Rtext(wsHit(0, 40, 1, 40).exact), '0', 'no memory holds nothing');
    eq(Rtext(wsHit(40, 40, 1, 40).exact), '1', 'and memory for all of it holds everything');
    eq(Rtext(diskIopsExact(20000, R(16n, 125n))), '17440', 'the uniform case leaves 17 440 IOPS');
    eq(Math.round(diskIopsApprox(20000, wsHit(8000000, 62500000, 1, 40).value)), 2219,
       'and the skewed one leaves 2219, which is the point of the lesson');
  }

  /* --- L11: RPO and RTO are different numbers ----------------------------- */
  {
    const IVL = R(86400n, 1n), W = R(20000000n, 1n), SIZE = R(2000000000000n, 1n);
    const RES = R(200000000n, 1n), REP = R(50000000n, 1n);
    eq(byteText(rpoBytes(IVL, W)), '1.73 TB', 'a day at 20 MB/s puts 1.73 TB at risk');
    eq(byteText(rpoExpectedBytes(IVL, W)), '864.00 GB', 'and 864 GB on average');
    eq(secText(restoreSeconds(SIZE, RES)), '2.78 h', 'copying 2 TB back at 200 MB/s is 2.8 hours');
    eq(secText(replaySeconds(rpoBytes(IVL, W), REP)), '9.60 h', 'replaying the log is 9.6 more');
    eq(secText(rtoSeconds(SIZE, RES, rpoBytes(IVL, W), REP)), '12.38 h', 'an RTO of 12.4 hours');
    /* Halving the interval halves the RPO and the replay and leaves the copy
       alone, which is why the copy is the floor. */
    eq(Rtext(Rdiv(rpoBytes(R(43200n, 1n), W), rpoBytes(IVL, W))), '1/2',
       'half the interval is half the bytes at risk');
    eq(Rtext(Rsub(rtoSeconds(SIZE, RES, rpoBytes(R(43200n, 1n), W), REP),
                  restoreSeconds(SIZE, RES))),
       Rtext(Rdiv(Rsub(rtoSeconds(SIZE, RES, rpoBytes(IVL, W), REP),
                       restoreSeconds(SIZE, RES)), R(2n, 1n))),
       'and half the replay, while the copy does not move at all');
    /* The interval a target implies, checked by round trip rather than by
       repeating the rearrangement. */
    {
      const ivl = intervalForRto(SIZE, RES, W, REP, R(14400n, 1n));
      eq(Rtext(ivl), '11000', 'a four-hour RTO allows a backup every 11 000 seconds');
      eq(Rtext(rtoSeconds(SIZE, RES, rpoBytes(ivl, W), REP)), '14400',
         'and at that interval the RTO is the target exactly');
    }
    eq(intervalForRto(SIZE, RES, W, REP, R(3600n, 1n)), null,
       'inside an hour is impossible: the copy alone is 2.8 hours, and it says so');
  }
}

// ------------------------------- system design C9: scaling laws and cost
/* The `scale` kit's own arithmetic, on the numbers its thirteen modes print.

   The block this section exists for is the Universal Scalability Law's TURNOVER.
   A coherency term dropped anywhere -- from the denominator, or by locating the
   peak from contention alone -- leaves a curve that rises and plateaus. Every
   figure on the page still looks plausible, the lesson's hard idea is quietly
   inverted, and nothing else in this repository would notice. So the assertions
   below do not merely check that N* has the value the closed form suggests: they
   check that C(N*+1) is strictly LESS than C(N*), that it keeps falling, and
   that with beta = 0 the same curve is monotone -- which is exactly what a
   dropped coherency term looks like.

   The other five are the break-evens. Each is asserted as the EQUALITY it came
   from rather than as a remembered decimal: at the break-even bandwidth the two
   transfer times are equal as fractions, at the placement crossover the two
   plans tie, and the reserved level found by the marginal rule is the level an
   exhaustive costing of every integer level also picks. */
console.log('system design: scaling laws, break-evens and what capacity costs');
{
  const SCALE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'scale.py');
  const scaleSrc = fs.readFileSync(SCALE_SOURCE, 'utf8');
  const scaleBlock = (name) => blockFrom(scaleSrc, name, SCALE_SOURCE);
  /* No BIGINT_JS: the scale kit does not ship it either, and evaluating a
     block here that the page does not carry would test a program nobody runs. */
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('APPROX_JS') + scaleBlock('SCALE_JS'));

  /* --- scale kit: BEGIN assertions (the mutation harness slices on this) --- */

  /* --- printing, at sizes that defeat Rdec --------------------------------- */
  eq(Rfixed(R(1n, 3n), 4), '0.3333', 'a third to four places');
  eq(Rfixed(R(2n, 3n), 4), '0.6667', 'two thirds rounds up');
  eq(Rfixed(R(-1n, 3n), 3), '-0.333', 'and the sign survives');
  eq(Rfixed(loadAtMonth(R(5000n, 1n), R(1n, 10n), 400), 0),
     String((11n ** 400n * 5000n + 10n ** 400n / 2n) / 10n ** 400n),
     'a 400-month compounding, printed exactly where Number would have said Infinity');
  eq(Number.isFinite(Rnum(loadAtMonth(R(5000n, 1n), R(1n, 10n), 400))), false,
     'which is precisely what Rnum does say, and why Rfixed exists');
  eq(groupDec('1234567.89'), '1 234 567.89', 'grouping stops at the decimal point');
  eq(groupDec('-1000'), '-1 000', 'and does not eat the sign');
  eq(money(R(1n, 100000n)), '$0.00001000', 'a unit cost keeps the digits it is about');
  eq(money(R(12345n, 1n)), '$12 345', 'and a monthly bill does not pretend to cents');
  eq(fmtBytes(R(2000000000000n, 1n), 2), '2 TB', 'decimal units: a TB is 10^12 bytes');
  eq(fmtSecs(R(1n, 4n)), '250 ms', 'a quarter second reads as milliseconds');
  eq(Rtext(ladderValue(52)), '500000000', 'the ladder is exact at every rung');

  /* --- L1: Amdahl ---------------------------------------------------------- */
  const p95 = R(95n, 100n);
  eq(Rtext(amdahlSpeedup(p95, 1)), '1', 'one machine is one machine');
  eq(Rtext(amdahlSpeedup(p95, 32)), '640/51', 'the lesson preset: 32 machines at 95% parallel');
  eq(Rtext(amdahlCeiling(p95)), '20', 'five per cent serial caps the speedup at twenty');
  eq(amdahlCeiling(R(1n, 1n)), null, 'and p = 1 has no ceiling to report');
  /* THE CEILING IS A CEILING: no n reaches it, at any n. */
  for (const n of [10, 100, 1000, 100000]) {
    eq(Rcmp(amdahlSpeedup(p95, n), amdahlCeiling(p95)) < 0, true,
       'S(n) stays strictly below 1/(1-p) at n = ' + n);
  }
  /* THE IDENTITY: the scan and the rearranged inequality are the same integer,
     at every parallel fraction and every target. */
  for (const [pn, pd] of [[95, 100], [99, 100], [7, 10], [999, 1000], [1, 2], [1, 100]]) {
    for (const [fn, fd] of [[9, 10], [1, 2], [95, 100], [99, 100]]) {
      const p = R(BigInt(pn), BigInt(pd)), f = R(BigInt(fn), BigInt(fd));
      const scan = amdahlReach(p, f, 200000), closed = amdahlReachClosed(p, f);
      eq(scan, closed, 'scan and closed form agree at p = ' + pn + '/' + pd + ', f = ' + fn + '/' + fd);
      eq(Rcmp(amdahlSpeedup(p, scan), Rmul(f, amdahlCeiling(p))) >= 0, true,
         'and that n really does reach the target');
      if (scan > 1) {
        eq(Rcmp(amdahlSpeedup(p, scan - 1), Rmul(f, amdahlCeiling(p))) < 0, true,
           'while the one before it does not');
      }
    }
  }
  eq(amdahlReachClosed(p95, R(9n, 10n)), 171, '90% of a twentyfold ceiling takes 171 machines');
  eq(Rtext(amdahlEfficiency(p95, 32)), '20/51', 'and 32 machines are 39% busy doing it');
  eq(Rtext(linearSpeedup(32)), '32', 'the expectation the lesson names');

  /* --- L2: the Universal Scalability Law, and its TURNOVER ----------------- */
  const uA = R(1n, 50n), uB = R(1n, 10000n);
  eq(Rtext(uslThroughput(1, uA, uB)), '1', 'one machine is one machine here too');
  eq(uslPeakExact(uA, uB, 20000), 99, 'the lesson curve peaks at 99 machines');
  eq(uslPeakScan(uA, uB, 400).N, 99, 'and the argmax of the scan agrees');
  near(uslPeakRootApprox(uA, uB), 98.99494936611666, 1e-9, 'sqrt((1-a)/b) rounds to 98.995');

  /* THE ASSERTION THIS SECTION EXISTS FOR. */
  for (const [an, ad, bn, bd] of [[1, 50, 1, 10000], [1, 20, 1, 1000], [1, 200, 1, 100000],
                                  [0, 1, 1, 1000], [1, 10, 1, 500], [1, 4, 1, 50]]) {
    const a = R(BigInt(an), BigInt(ad)), b = R(BigInt(bn), BigInt(bd));
    const where = 'a = ' + an + '/' + ad + ', b = ' + bn + '/' + bd;
    const N = uslPeakExact(a, b, 20000);
    eq(N !== null && N >= 1, true, 'a peak exists at ' + where);
    eq(Rcmp(uslThroughput(N + 1, a, b), uslThroughput(N, a, b)) < 0, true,
       'THE CURVE FALLS past N* at ' + where);
    eq(Rcmp(uslThroughput(2 * N, a, b), uslThroughput(N, a, b)) < 0, true,
       'and keeps falling at twice N*, ' + where);
    if (N > 1) {
      eq(Rcmp(uslThroughput(N - 1, a, b), uslThroughput(N, a, b)) < 0, true,
         'while the machine before N* was still buying something, ' + where);
    }
    eq(uslPeakScan(a, b, 4 * N + 20).N, N, 'the scan finds the same peak at ' + where);
    const root = uslPeakRootApprox(a, b);
    eq(N >= Math.floor(root) && N <= Math.ceil(root), true,
       'and the rounded root brackets it at ' + where);
    /* the predicate and the comparison are the same claim */
    eq(uslBeyondPeak(N, a, b), true, 'bN(N+1) >= 1-a holds at N*, ' + where);
    eq(N === 1 || !uslBeyondPeak(N - 1, a, b), true, 'and not before it, ' + where);
  }
  /* AND WHAT A DROPPED COHERENCY TERM LOOKS LIKE: with b = 0 there is no peak
     and the curve is monotone all the way out. */
  eq(uslPeakExact(uA, R(0n, 1n), 20000), null, 'beta = 0 has no peak at all');
  {
    let mono = true;
    for (let N = 1; N < 500; N += 1) {
      if (Rcmp(uslThroughput(N + 1, uA, R(0n, 1n)), uslThroughput(N, uA, R(0n, 1n))) <= 0) mono = false;
    }
    eq(mono, true, 'with beta = 0 the curve only ever rises -- Amdahl, not the USL');
  }
  eq(Rtext(uslContentionCeiling(uA)), '50', 'and it rises towards 1/a = 50');
  eq(Rtext(uslRetained(99, uA, uB, 99)), '1', 'the peak retains all of itself');
  eq(Rcmp(uslRetained(198, uA, uB, 99), R(1n, 1n)) < 0, true,
     'and twice the peak, at twice the bill, retains less');

  /* --- L3: batching -------------------------------------------------------- */
  const bF = R(2000n, 1n), bV = R(100n, 1n), bLam = R(500n, 1n);
  eq(Rtext(perItemCost(bF, bV, 1)), '2100', 'one item alone pays the whole call');
  eq(Rtext(perItemCost(bF, bV, 100)), '120', 'and a batch of a hundred pays a fiftieth of it');
  eq(Rtext(fixedShare(bF, bV, 100)), '1/6', 'the fixed part is a sixth of the cost there');
  eq(batchForFixedShare(bF, bV, R(1n, 5n)), 100, 'F/B = v/5 at B = 100');
  eq(Rtext(batchWaitFirst(100, bLam)), '99/500', 'the first item waits (B-1)/lambda');
  eq(Rtext(batchWaitMean(100, bLam)), '99/1000', 'and the average item waits half of that');
  /* THE RULE OF THUMB'S ERROR IS EXACTLY ONE INTER-ARRIVAL TIME, at every B --
     which is why it is usable and still not the number. */
  for (const B of [2, 10, 100, 800]) {
    eq(Rtext(Rsub(batchWaitRule(B, bLam), batchWaitFirst(B, bLam))), Rtext(Rinv(bLam)),
       'B/lambda overstates the first item\'s wait by 1/lambda at B = ' + B);
  }
  eq(Rcmp(perItemCost(bF, bV, 800), bV) > 0, true, 'the cost curve never reaches its floor');
  eq(batchUnderTimer(100, bLam, R(1n, 5n)).effective, 100, 'a 200 ms timer just reaches a batch of 100');
  eq(batchUnderTimer(400, bLam, R(1n, 5n)).capped, true, 'and caps a batch of 400');
  eq(batchUnderTimer(400, bLam, R(1n, 5n)).effective, 100, 'at the hundred that arrive in the window');

  /* --- L4: vertical against horizontal ------------------------------------- */
  const vAlpha = R(1n, 200n);
  /* the node count is the USL's contention term, not a second overhead model */
  eq(horizontalNodes(1, vAlpha, 6000), 1, 'one node delivers one node');
  eq(horizontalNodes(5, vAlpha, 6000), 6, 'five nodes\' worth takes six of them at a = 1/200');
  eq(Rcmp(uslThroughput(6, vAlpha, R(0n, 1n)), R(5n, 1n)) >= 0, true, 'because C(6) clears 5');
  eq(Rcmp(uslThroughput(5, vAlpha, R(0n, 1n)), R(5n, 1n)) < 0, true, 'and C(5) does not');
  eq(horizontalNodes(60, R(1n, 20n), 6000), null,
     'and 1/a is a ceiling on a fleet exactly as it is on a program');
  eq(JSON.stringify(verticalRung(5)), '{"rung":3,"units":8}', 'a 5x target buys the 8x rung');
  eq(Rtext(verticalCost(5, R(100n, 1n), R(11n, 10n))), '5324/5',
     'at 10% a doubling that rung costs $1064.80, not $500');
  eq(shapeFirstCrossing(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000), 3,
     'horizontal first wins at 3x');
  eq(shapeBreakEven(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000), 5,
     'but only from 5x does it never lose again -- the ladder is a staircase');
  eq(horizontalWinsAt(4, R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 6000), false,
     'and at 4x the freshly bought rung is cheaper');
  /* a break-even is a break-even: nothing below it wins from there on */
  {
    const be = shapeBreakEven(R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 64, 6000);
    let always = true;
    for (let t = be; t <= 64; t += 1) {
      if (!horizontalWinsAt(t, R(100n, 1n), R(100n, 1n), R(11n, 10n), vAlpha, 6000)) always = false;
    }
    eq(always, true, 'and horizontal wins at every target from the break-even on');
  }

  /* --- L5: waste ----------------------------------------------------------- */
  const dayW = dayShape('evening', 21, 6).map((w) => R(BigInt(w), 1n));
  const dayS = profileStats(dayW);
  eq(Rtext(dayS.peak) + ' ' + Rtext(dayS.mean), '48 21', 'the lesson profile: peak 48, mean 21');
  eq(Rtext(dayS.peakToMean), '16/7', 'peak over mean, exactly');
  eq(Rtext(paidCapacity(dayS.peak, R(7n, 10n))), '480/7', 'you pay for peak/rho');
  eq(Rtext(wasteFraction(dayS.mean, dayS.peak, R(7n, 10n))), '111/160', 'and waste 69.4% of it');
  /* THE SIZE OF THE DAY CANCELS: only the SHAPE and rho move the waste. */
  for (const k of [2n, 17n, 1000000n]) {
    const scaled = dayW.map((v) => Rmul(v, R(k, 1n)));
    const s2 = profileStats(scaled);
    eq(Rtext(wasteFraction(s2.mean, s2.peak, R(7n, 10n))), '111/160',
       'scaling every bucket by ' + k + ' leaves the waste untouched');
  }
  eq(Rtext(wasteFraction(dayS.mean, dayS.peak, R(1n, 1n))), '9/16',
     'and even at rho = 1 the shape alone wastes 56%');
  {
    const flat = dayShape('flat', 12, 0).map((w) => R(BigInt(w), 1n));
    const fs2 = profileStats(flat);
    eq(Rtext(wasteFraction(fs2.mean, fs2.peak, R(1n, 1n))), '0',
       'a flat profile at rho = 1 is the only one with no waste at all');
  }
  eq(JSON.stringify(hoursOver(dayW, dayS.mean).hours), '9',
     'cutting to the mean leaves nine hours of the day over capacity');
  eq(Rtext(hoursOver(dayW, dayS.mean).worst), '27',
     'the worst of them short by 27 -- more than the mean bucket itself');
  eq(JSON.stringify(hoursOver(dayW, paidCapacity(dayS.peak, R(7n, 10n))).hours), '0',
     'while the capacity actually bought covers every hour');

  /* --- L6: reserved, on-demand and spot ------------------------------------ */
  eq(Rtext(breakEvenUtilisation(R(7n, 100n), R(12n, 100n))), '7/12', 'u* is the price ratio');
  /* THE IDENTITY: the marginal rule and an exhaustive costing pick the same
     level, on every profile and at every price pair. */
  const profiles = [
    dayShape('evening', 21, 4), dayShape('office', 10, 5),
    dayShape('batchwindow', 3, 9), dayShape('flat', 12, 0), dayShape('evening', 21, 10)
  ].map((w) => w.map((v) => R(BigInt(v), 1n)));
  for (let pi = 0; pi < profiles.length; pi += 1) {
    const bs = profiles[pi];
    const top = Number(profileStats(bs).peak.n);
    for (const [rn, dn] of [[7, 12], [3, 12], [11, 12], [1, 12], [12, 12], [6, 12]]) {
      const r = R(BigInt(rn), 100n), d = R(BigInt(dn), 100n);
      const marginal = reserveLevelMarginal(bs, r, d);
      const search = reserveLevelSearch(bs, r, d, top);
      eq(Rtext(mixCost(bs, marginal, r, d).total), Rtext(search.cost),
         'the marginal level costs what the best level costs, profile ' + pi + ', ' + rn + '/' + dn);
      eq(Rcmp(mixCost(bs, marginal, r, d).total, mixCost(bs, marginal + 1, r, d).total) <= 0, true,
         'one more reserved instance does not help, profile ' + pi + ', ' + rn + '/' + dn);
      if (marginal > 0) {
        eq(Rcmp(mixCost(bs, marginal, r, d).total, mixCost(bs, marginal - 1, r, d).total) <= 0, true,
           'and one fewer does not either, profile ' + pi + ', ' + rn + '/' + dn);
      }
    }
  }
  {
    const bs = profiles[0];
    eq(reserveLevelMarginal(bs, R(7n, 100n), R(12n, 100n)), 12, 'u* = 7/12 reserves the floor');
    eq(reserveLevelMarginal(bs, R(3n, 100n), R(12n, 100n)), 24, 'a deeper commitment reserves into the shoulder');
    eq(Rtext(mixCost(bs, 12, R(7n, 100n), R(12n, 100n)).total), '936/25', '$37.44 a day for the mix');
    eq(Rtext(mixCost(bs, 0, R(7n, 100n), R(12n, 100n)).total), '1296/25', 'against $51.84 all on demand');
    eq(Rcmp(mixCost(bs, Number(profileStats(bs).peak.n), R(7n, 100n), R(12n, 100n)).total,
            mixCost(bs, 12, R(7n, 100n), R(12n, 100n)).total) > 0, true,
       'and reserving the peak costs more than the optimum -- the misconception, priced');
  }
  /* spot is a price AND an interruption model; without the model it is just a
     smaller number. */
  eq(Rtext(spotBreakEvenRate(R(4n, 100n), R(12n, 100n))), '2/3', 'q* = (d-s)/d');
  eq(Rtext(spotExpectedPrice(R(4n, 100n), R(12n, 100n), R(15n, 100n))), '29/500',
     'a delivered spot hour at 15% reclaimed expects 5.8 cents');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(2n, 3n)), false, 'exactly at q* it is a wash');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(66n, 100n)), true, 'just below it, spot pays');
  eq(spotWorthIt(R(4n, 100n), R(12n, 100n), R(67n, 100n)), false, 'just above it, it does not');
  eq(spotWorthIt(R(1n, 100n), R(12n, 100n), R(95n, 100n)), false,
     'and a 92% discount is worth nothing at a 95% interruption rate');

  /* --- L7: autoscaling lag ------------------------------------------------- */
  const aR = R(50n, 1n), aTau = R(90n, 1n), aD = R(300n, 1n), aBase = R(5000n, 1n);
  eq(Rtext(autoscaleTrapezoid(aR, aTau, aD)), '1147500', 'r*tau*(D - tau/2), the lesson form');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(0n, 1n)).area), '1147500',
     'and the general area agrees with it when no reserve is held');
  eq(Rtext(autoscaleReserveNeeded(aR, aTau)), '4500', 'the reserve that removes it is r*tau');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(4500n, 1n)).area), '0', 'and it removes it exactly');
  eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(4501n, 1n)).area), '0', 'one more changes nothing');
  eq(Rcmp(autoscaleShortfall(aR, aTau, aD, R(4499n, 1n)).area, R(0n, 1n)) > 0, true,
     'one fewer does not');
  /* THE INDEPENDENT CHECK: the area under max(0, demand - capacity), summed by
     the trapezoid rule over unit steps. Both the integrand and its breakpoints
     are at integers here, so that sum is EXACT, and it shares no algebra with
     the closed form it is checking. */
  function shortfallBySum(rate, tau, dur, reserve, base) {
    let total = R(0n, 1n);
    const T = Number(dur.n / dur.d);
    for (let t = 0; t < T; t += 1) {
      const at = (k) => {
        const tt = R(BigInt(k), 1n);
        const g = Rsub(autoscaleDemand(base, rate, dur, tt),
                       autoscaleCapacity(base, reserve, rate, tau, dur, tt));
        return Rcmp(g, R(0n, 1n)) > 0 ? g : R(0n, 1n);
      };
      total = Radd(total, Rdiv(Radd(at(t), at(t + 1)), R(2n, 1n)));
    }
    return total;
  }
  for (const h of [0, 500, 1000, 2000, 4000, 4500, 6000]) {
    eq(Rtext(autoscaleShortfall(aR, aTau, aD, R(BigInt(h), 1n)).area),
       Rtext(shortfallBySum(aR, aTau, aD, R(BigInt(h), 1n), aBase)),
       'the closed form matches the area under the curve at a reserve of ' + h);
  }
  /* a ramp shorter than the boot: the fleet never moves at all */
  eq(Rtext(autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area), '135000',
     'a 30 s spike behind a 90 s boot is a bare triangle');
  eq(Rtext(autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area),
     Rtext(shortfallBySum(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n), aBase)),
     'and the summed area agrees there too');
  eq(Rcmp(autoscaleTrapezoid(R(300n, 1n), R(90n, 1n), R(30n, 1n)),
          autoscaleShortfall(R(300n, 1n), R(90n, 1n), R(30n, 1n), R(0n, 1n)).area) !== 0, true,
     'while r*tau*(D - tau/2) does NOT, because D < tau breaks its assumption');
  /* rho is lambda over mu, and it is course 3's rho */
  eq(Rtext(rhoAt(autoscaleDemand(aBase, aR, aD, aTau),
                 autoscaleCapacity(aBase, R(0n, 1n), aR, aTau, aD, aTau))), '19/10',
     'rho at the worst instant of the lesson preset');
  eq(Rtext(backlogGrowth(R(9500n, 1n), R(5000n, 1n))), '4500',
     'and above rho = 1 the backlog grows at lambda - mu, as course 3 says');
  eq(responseFactor(R(19n, 10n)), null, 'with no steady state, 1/(1-rho) is not a number');
  eq(Rtext(responseFactor(R(9n, 10n))), '10', 'and at rho = 0.9 it is ten');

  /* --- L8: cost per request ------------------------------------------------ */
  const uCfg = {
    fixedMonthly: R(4000n, 1n), variablePerRequest: R(1n, 1000000n),
    bytesPerRequest: R(2000n, 1n), retentionMonths: R(12n, 1n), storagePrice: R(23n, 1000n),
    bytesOut: R(120000n, 1n), egressPrice: R(9n, 100n)
  };
  const uParts = unitCost(uCfg, R(500000000n, 1n));
  eq(Rtext(uParts.fixed), '1/125000', 'the fixed cost shared over 500M requests');
  eq(Rtext(uParts.egress), '27/2500000', '120 kB at 9 cents a GB');
  eq(Rtext(uParts.storage), '69/125000000', '2 kB held for twelve months');
  eq(dominantTerm(uParts), 'egress', 'and egress is the biggest of the four');
  eq(Rtext(uParts.total), '159/7812500', 'the four added');
  eq(Rtext(uParts.monthly), '10176', 'which is $10 176 a month');
  /* ONLY THE FIXED TERM MOVES WITH VOLUME. */
  for (const v of [1000000n, 500000000n, 900000000000n]) {
    const q = unitCost(uCfg, R(v, 1n));
    eq(Rtext(q.egress) + ' ' + Rtext(q.storage) + ' ' + Rtext(q.compute),
       Rtext(uParts.egress) + ' ' + Rtext(uParts.storage) + ' ' + Rtext(uParts.compute),
       'egress, storage and compute per request do not move at volume ' + v);
  }
  eq(Rcmp(unitCost(uCfg, R(1000000000n, 1n)).total, uParts.total) < 0, true,
     'while the unit cost falls with volume');
  eq(Rcmp(unitCost(uCfg, R(1000000000n, 1n)).monthly, uParts.monthly) > 0, true,
     'and the monthly total rises with it -- the misconception is wrong in both directions');
  /* the crossing is an equality, solved */
  {
    const cross = fixedCrossing(uCfg.fixedMonthly, uParts.egress);
    eq(Rtext(cross), '10000000000/27', 'fixed / egress-per-request');
    eq(Rtext(unitCost(uCfg, cross).fixed), Rtext(uParts.egress),
       'and at that volume the two terms are exactly equal');
  }
  /* storage follows retention, not traffic */
  eq(Rtext(storagePerRequest(R(2000n, 1n), R(24n, 1n), R(23n, 1000n))),
     Rtext(Rmul(storagePerRequest(R(2000n, 1n), R(12n, 1n), R(23n, 1000n)), R(2n, 1n))),
     'doubling the retention doubles the storage term');

  /* --- L9: storage tiers --------------------------------------------------- */
  const tHot = R(23n, 1000n), tCold = R(4n, 1000n), tRead = R(10n, 1000n);
  eq(Rtext(tierBreakEvenAccesses(tHot, tCold, tRead)), '19/10', 'a* = (hot - cold)/retrieval');
  eq(tierBreakEvenAge(R(8n, 1n), R(1n, 2n), tHot, tCold, tRead, 36), 3,
     'eight reads halving monthly crosses a* at month 3');
  eq(Rtext(accessesAtAge(R(8n, 1n), R(1n, 2n), 3)), '1', 'because month 3 is read once');
  eq(Rtext(accessesAtAge(R(8n, 1n), R(1n, 2n), 2)), '2', 'and month 2 is read twice');
  /* AT THE BREAK-EVEN AGE THE TWO TIERS COST THE SAME, exactly. */
  {
    const gb = R(1000n, 1n), star = tierBreakEvenAccesses(tHot, tCold, tRead);
    const hot = tierCost(gb, star, tHot, tCold, tRead, false);
    const cold = tierCost(gb, star, tHot, tCold, tRead, true);
    eq(Rtext(hot.total), Rtext(cold.total), 'at exactly a* reads a GB-month the tiers tie');
    eq(Rcmp(tierCost(gb, Rmul(star, R(2n, 1n)), tHot, tCold, tRead, true).total,
            tierCost(gb, Rmul(star, R(2n, 1n)), tHot, tCold, tRead, false).total) > 0, true,
       'above it, cold costs more -- "everything old should go cold" is false');
    eq(Rcmp(tierCost(gb, Rdiv(star, R(2n, 1n)), tHot, tCold, tRead, true).total,
            tierCost(gb, Rdiv(star, R(2n, 1n)), tHot, tCold, tRead, false).total) < 0, true,
       'and below it, cold saves');
  }
  {
    const bs = [];
    for (let age = 0; age < 24; age += 1) {
      bs.push({ gb: R(1000n, 1n), accesses: accessesAtAge(R(8n, 1n), R(1n, 2n), age) });
    }
    const plan = tierPlan(bs, tHot, tCold, tRead, 3);
    eq(Rtext(plan.allHot), '552', 'keeping all 24 TB hot is $552 a month');
    eq(Rcmp(plan.saving, R(0n, 1n)) > 0, true, 'and tiering at a* saves against it');
    eq(Rtext(plan.movedGb), '21000', 'with 21 TB moved');
    /* tiering at a WRONGER age saves less. That is what "break-even" means. */
    for (const age of [0, 1, 2, 4, 6]) {
      eq(Rcmp(tierPlan(bs, tHot, tCold, tRead, age).saving, plan.saving) <= 0, true,
         'tiering at month ' + age + ' saves no more than tiering at a*');
    }
  }

  /* --- L10: compress or not ------------------------------------------------ */
  const cSize = R(10000000000n, 1n), cRatio = R(4n, 1n), cRate = R(250000000n, 1n);
  const cBw = R(125000000n, 1n);
  eq(Rtext(rawTime(cSize, cBw)), '80', '10 GB over a gigabit link is 80 seconds');
  eq(Rtext(compressedTime(cSize, cBw, cRatio, cRate, null).total), '60', 'and 60 compressed');
  eq(Rtext(compressBreakEvenBandwidth(cRatio, cRate, null)), '187500000', 'bw* = rate*(k-1)/k');
  eq(Rtext(compressBreakEvenRate(cRatio, cBw)), '500000000/3', 'read the other way: rate > bw*k/(k-1)');
  /* THE BREAK-EVEN IS AN EQUALITY: at bw* the two plans take exactly the same
     time, at every size, ratio and compressor -- and with the far end counted. */
  for (const [kn, kd] of [[4, 1], [3, 2], [17, 10], [10, 1], [21, 20]]) {
    for (const rate of [60000000n, 250000000n, 2000000000n]) {
      for (const drate of [null, 300000000n, 800000000n]) {
        const k = R(BigInt(kn), BigInt(kd)), rr = R(rate, 1n);
        const dr = drate === null ? null : R(drate, 1n);
        const star = compressBreakEvenBandwidth(k, rr, dr);
        const label = 'k = ' + kn + '/' + kd + ', rate ' + rate + ', drate ' + drate;
        for (const size of [1000n, 10000000000n]) {
          const S = R(size, 1n);
          eq(Rtext(rawTime(S, star)), Rtext(compressedTime(S, star, k, rr, dr).total),
             'at bw* the two plans tie, ' + label + ', size ' + size);
        }
        /* and the size cancels out of the break-even entirely */
        eq(Rcmp(rawTime(R(7n, 1n), Rmul(star, R(9n, 10n))),
                compressedTime(R(7n, 1n), Rmul(star, R(9n, 10n)), k, rr, dr).total) > 0, true,
           'below bw* compressing wins, ' + label);
        eq(Rcmp(rawTime(R(7n, 1n), Rmul(star, R(11n, 10n))),
                compressedTime(R(7n, 1n), Rmul(star, R(11n, 10n)), k, rr, dr).total) < 0, true,
           'above it, it loses, ' + label);
      }
    }
  }
  eq(compressBreakEvenRate(R(1n, 1n), cBw), null, 'a ratio of 1 has no crossing to report');

  /* --- L11: move the data or the compute ----------------------------------- */
  const pData = R(2000000000000n, 1n), pResult = R(5000000n, 1n), pCode = R(200000n, 1n);
  const pBw = R(125000000n, 1n);
  eq(Rtext(moveDataTime(pData, pBw)), '16000', '2 TB over a gigabit link is 16 000 seconds');
  eq(Rtext(moveComputeTime(pCode, pResult, pBw)), '26/625', 'and the job itself is 42 ms');
  eq(Rtext(resultRatio(pResult, pData)), '1/400000', 'the result-to-input ratio, and it is tiny');
  eq(Rtext(placementCrossover(pData, pCode)), '1999999800000', 'the two tie at D - code of result');
  /* THE BANDWIDTH CANCELS: the crossing is the same at every link speed. */
  for (const bw of [1000000n, 125000000n, 3125000000n]) {
    const B = R(bw, 1n), cross = placementCrossover(pData, pCode);
    eq(Rtext(moveDataTime(pData, B)), Rtext(moveComputeTime(pCode, cross, B)),
       'at the crossover the plans tie at ' + bw + ' B/s');
    eq(Rcmp(moveComputeTime(pCode, pResult, B), moveDataTime(pData, B)) < 0, true,
       'and moving the compute wins at ' + bw + ' B/s, as it does at every other');
  }
  eq(Rtext(placementSpeedup(pData, pCode, pResult)), '5000000/13',
     'here by a factor of 384 615');

  /* --- headroom: N-1 capacity ---------------------------------------------- */
  const hCap = R(1000n, 1n), hLam = R(9000n, 1n);
  eq(Rtext(fleetRho(hLam, 10, hCap)), '9/10', 'ten machines at rho = 0.9');
  eq(Rtext(rhoAfterLoss(R(9n, 10n), 10, 1)), '1', 'and losing one lands exactly on 1');
  eq(responseFactor(rhoAfterLoss(R(9n, 10n), 10, 1)), null, 'where there is no steady state left');
  eq(Rtext(survivingFraction(10, 1)), '9/10', '(N-1)/N on ten machines');
  eq(Rtext(survivingFraction(3, 1)), '2/3', 'and two thirds on three -- why small fleets need more');
  /* rho after the loss IS lambda over the surviving capacity. Two routes. */
  for (const [N, f, lam] of [[10, 1, 9000n], [3, 1, 1800n], [12, 4, 7200n], [60, 1, 54000n]]) {
    eq(Rtext(rhoAfterLoss(fleetRho(R(lam, 1n), N, hCap), N, f)),
       Rtext(fleetRho(R(lam, 1n), N - f, hCap)),
       'multiplying rho by N/(N-f) is dividing lambda by the survivors, N = ' + N);
  }
  /* THE IDENTITY: scan and closed form pick the same machine count. */
  for (const lam of [9000n, 1800n, 54000n, 100n, 23700n]) {
    for (const f of [1, 2, 4]) {
      for (const [rn] of [[90], [80], [99], [50], [70]]) {
        const rmax = R(BigInt(rn), 100n);
        eq(machinesForHeadroom(R(lam, 1n), hCap, rmax, f, 4000),
           machinesForHeadroomClosed(R(lam, 1n), hCap, rmax, f),
           'scan and closed form agree at lambda = ' + lam + ', f = ' + f + ', rho <= ' + rn + '%');
      }
    }
  }
  eq(machinesForHeadroom(hLam, hCap, R(9n, 10n), 1, 4000), 11,
     'holding rho <= 0.9 through one loss takes eleven machines, not ten');
  eq(Rtext(usableUtilisation(R(9n, 10n), 10, 1)), '81/100',
     'so the utilisation you may plan for is 81%, not 90%');

  /* --- growth: the month the plan runs out --------------------------------- */
  const gCur = R(5000n, 1n), gRate = R(1n, 10n), gLimit = R(50000n, 1n);
  eq(Rtext(loadAtMonth(gCur, gRate, 0)), '5000', 'month zero is today');
  eq(monthsToLimit(gCur, gRate, gLimit, 2000), 25, 'and 10% a month reaches 50 000 rps in month 25');
  eq(Rcmp(loadAtMonth(gCur, gRate, 25), gLimit) >= 0, true, 'month 25 is over the limit');
  eq(Rcmp(loadAtMonth(gCur, gRate, 24), gLimit) < 0, true, 'and month 24 is not');
  near(monthsToLimitApprox(gCur, gRate, gLimit), 24.15885792809679, 1e-9,
       'log(limit/current)/log(1+r) is the rounded gloss');
  /* THE EXACT SEARCH AND THE ROUNDED LOGARITHM MUST BRACKET EACH OTHER. */
  for (const [cur, rate, lim] of [[5000n, 10n, 50000n], [5000n, 26n, 50000n], [5000n, 3n, 50000n],
                                  [100n, 1n, 500000n], [40000n, 40n, 500000n]]) {
    const c = R(cur, 1n), r = R(rate, 100n), l = R(lim, 1n);
    const exact = monthsToLimit(c, r, l, 5000), approx = monthsToLimitApprox(c, r, l);
    eq(exact, Math.ceil(approx - 1e-9),
       'the integer search is the ceiling of the logarithm at r = ' + rate + '%');
    eq(Rcmp(loadAtMonth(c, r, exact), l) >= 0, true, 'and it really does clear the limit');
    eq(Rcmp(loadAtMonth(c, r, exact - 1), l) < 0, true, 'while the month before does not');
  }
  eq(monthsToLimit(gCur, R(0n, 1n), gLimit, 2000), null, 'no growth never reaches it');
  eq(monthsToLimit(gLimit, gRate, gCur, 2000), 0, 'and a limit already passed is month zero');
  /* THE BOUNDARY: a load landing exactly ON the limit has reached it. Every
     other case in this section crosses between two months and cannot tell >=
     from >, so a plan that quietly gave itself one more month than it has
     would survive all of them. */
  eq(Rtext(loadAtMonth(R(5000n, 1n), R(1n, 1n), 2)), '20000',
     'at 100% a month, month 2 is exactly 20 000 rps');
  eq(monthsToLimit(R(5000n, 1n), R(1n, 1n), R(20000n, 1n), 2000), 2,
     'so the 20 000 rps limit is reached in month 2, not month 3');
  eq(doublingMonths(R(1n, 1n), 2000), 1, 'and 100% a month doubles in exactly one month');
  eq(doublingMonths(R(1n, 10n), 2000), 8, '10% a month doubles in eight months');
  eq(doublingMonths(R(26n, 100n), 2000), 3, 'and 26% a month doubles in three');
  /* the plan itself: a ceiling, because 3.2 machines is four */
  eq(machinesAtMonth(gCur, gRate, 0, R(1000n, 1n), R(7n, 10n)), 8,
     '5000 rps at 70% of a 1000 rps machine is eight machines, not 7.14');
  eq(machinesAtMonth(gCur, gRate, 25, R(1000n, 1n), R(7n, 10n)), 78,
     'and 78 by the month the limit arrives');
  eq(orderMonth(25, 3), 22, 'a three-month lead time makes month 22 the date that matters');
  eq(orderMonth(25, 30) < 0, true, 'and a lead time longer than the runway is already late');

  /* --- scale kit: END assertions --- */
}

// ------------------------------------- measuring systems (kit: measure)
/* The `measure` kit's own arithmetic, on the numbers its ten lessons print.

   Three of these are not figures but CLAIMS the course makes in prose, and
   they are why this section exists.

   The fleet p99 must differ from the mean of the per-host p99s on the preset
   L2 opens with. If those two ever came out equal, the "merged" figure would
   not be merging anything -- the single most plausible way for that lesson to
   be quietly broken is for both numbers to come from the same list.

   The error budget must be EXACTLY 43.2 minutes at three nines over 30 days.
   That is the number burn-rate alerting is quoted against; 216/5 is the whole
   lesson, and a period convention that silently changed it would leave every
   pair in the table wrong by 1.4%.

   And the reweighted mean must be exactly the true mean, not nearly it. The
   sampling lesson claims that counting each sampled request 1/s times undoes
   the tail bias; Requ, not near, is the assertion that claim deserves. */
console.log('system design: measurement, aggregation, sampling and alerts');
{
  const MEASURE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'measure.py');
  const measureSrc = fs.readFileSync(MEASURE_SOURCE, 'utf8');
  const measureBlock = (name) => blockFrom(measureSrc, name, MEASURE_SOURCE);
  /* latency.py's block is evaluated FIRST and measure.py's second, so that the
     shared output helpers in scope are the ones measure.py ships. What is
     wanted from the latency kit is parseSample and fanoutBreakEven: this
     course's percentiles have to agree with the course that owns them. */
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('AVAIL_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS')
       + latencyBlock('LATENCY_JS') + measureBlock('MEASURE_JS'));

  /* --- printing, and the one that exists because Rnum cannot ------------- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(1n, 3n), 4), '33.3333%', 'a percentage without a gcd');
  eq(Rpct(R(216n, 5000n), 2), '4.32%', 'and it agrees with the Rmul form');
  eq(Rpct(R(216n, 5000n), 2), Rfixed(Rmul(R(216n, 5000n), R(100n, 1n)), 2) + '%',
     'scaling the numerator prints what multiplying the rational prints');
  eq(RpctAuto(R(1n, 2n)), '50.00%', 'a middling probability gets two places');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 7n))), '99.99999%',
     'and one near certainty widens rather than printing 100%');
  eq(RpctAuto(R(1n, 500000n)), '0.0002%', 'a rare one widens downwards the same way');
  eq(minutesText(R(216n, 5n)), '43.20 min', '43.2 minutes reads as minutes');
  eq(minutesText(R(300n, 1n)), '5.00 h', 'five hours reads as hours');
  eq(minutesText(R(3000n, 1n)), '2.08 days', 'and fifty hours reads as days');
  eq(minutesText(R(1n, 2n)), '30.0 s', 'and half a minute reads as seconds');
  /* THE REASON Rplot EXISTS. Rnum on a load-test probability is NaN, and a
     chart of NaNs paints nothing and throws nothing. */
  const huge = atLeastOne(R(1n, 1000n), 3000);
  eq(Number.isNaN(Rnum(huge)), true, 'Rnum of a 9000-digit fraction is NaN');
  near(Rplot(huge), 0.950288, 1e-6, 'Rplot long-divides it instead');

  /* --- the formula that repeats: 1 - (1-p)^k ---------------------------- */
  /* The fast form and the rational-arithmetic form are the same number. This
     is the assertion that licenses building the fraction without a gcd. */
  for (const [n, d, k] of [[1n, 100n, 10], [259n, 1000n, 10], [1n, 1000n, 600],
                           [3n, 7n, 5], [1n, 1n, 4], [7n, 8n, 1], [1n, 2n, 12]]) {
    const p = R(n, d);
    eq(Requ(atLeastOne(p, k), Rsub(R(1n, 1n), Rpow(Rsub(R(1n, 1n), p), k))), true,
       '1 - (1-p)^k built in lowest terms at p = ' + Rtext(p) + ', k = ' + k);
  }
  eq(Rtext(atLeastOne(R(0n, 1n), 9)), '0', 'sampling nothing catches nothing');
  eq(Rtext(atLeastOne(R(1n, 100n), 1)), '1/100', 'one trial is just p');
  eq(Rtext(atLeastOne(R(1n, 100n), 10)), '9561792499119550999/100000000000000000000',
     '1% sampling of a ten-request problem, exactly');
  eq(Rpct(atLeastOne(R(1n, 100n), 10), 2), '9.56%', 'which is 9.56%, so it is missed 90% of the time');
  /* The curve the pages draw carries the power forward; it must be the same
     number at every point it draws. */
  const curve = atLeastOneCurve(R(1n, 1000n), 50, 6);
  for (let i = 0; i <= 6; i += 1) {
    eq(Requ(curve[i], atLeastOne(R(1n, 1000n), 50 * i)), true, 'the drawn curve at n = ' + (50 * i));
  }
  /* The searches: the scan, the bisection, and the closed form all agree. */
  eq(rateForTarget(10, R(95n, 100n), 1000).n + '/' + rateForTarget(10, R(95n, 100n), 1000).d, '259/1000',
     '95% confidence in a ten-request problem needs 25.9% sampling');
  eq(Rcmp(atLeastOne(R(258n, 1000n), 10), R(95n, 100n)) < 0, true, 'and 25.8% does not reach it');
  for (const k of [3, 10, 25]) {
    for (const t of [[1n, 2n], [9n, 10n], [95n, 100n], [99n, 100n]]) {
      eq(Requ(rateForTarget(k, R(t[0], t[1]), 1000), rateForTargetSearch(k, R(t[0], t[1]), 1000)), true,
         'the scan and the bisection agree at k = ' + k + ', target ' + t[0] + '/' + t[1]);
    }
  }
  /* The rule of three, exactly: a clean run of 1000 bounds the rate at 3/1000. */
  eq(Rtext(rateForTargetSearch(1000, R(95n, 100n), 10000)), '3/1000',
     'a thousand clean requests bound the failure rate at exactly 3/1000');
  eq(Rtext(rateForTargetSearch(100, R(95n, 100n), 10000)), '37/1250',
     'at a hundred requests the exact bound is 2.96%, not the 3% of the rule of thumb');
  /* The idealisation, which rounds AND is a different quantity. */
  near(captureApprox(R(1n, 100n), 10), 0.09516258196404, 1e-12, '1 - e^(-sk) as expNegApprox computes it');
  near(Math.abs(captureApprox(R(1n, 100n), 10) - Rplot(atLeastOne(R(1n, 100n), 10))), 4.55e-4, 1e-5,
     'and it differs from the exact answer by far more than it rounds');

  /* --- L1: the SLI, its exact variance and its rounded root -------------- */
  const p1 = R(9995n, 10000n), obj = R(999n, 1000n);
  /* An SLI is a count over a count, so a window of n can only produce the n + 1
     fractions with denominator n. 99.95% is not one of them at n = 1000. */
  eq(Rtext(sliRatio(999, 1000)), '999/1000', 'an SLI is good over total, in lowest terms');
  eq(Rint(Rmul(p1, R(1000n, 1n))), false, '99.95% of a thousand requests is 999.5 of them');
  eq(Rint(Rmul(p1, R(20000n, 1n))), true, 'while at twenty thousand it is a whole number again');
  eq(Rpct(sliRatio(Number(Rfloor(Rmul(p1, R(1000n, 1n)))), 1000), 3), '99.900%',
     'so the nearest ratio below is the objective itself');
  eq(Rtext(sliVariance(p1, 1000)), '1999/4000000000', 'p(1-p)/n at 99.95% on 1000 requests, exactly');
  near(sliSeApprox(p1, 1000), 0.00070692998, 1e-10, 'its square root, which rounds');
  near(sigmasApprox(p1, obj, 1000), 0.7072836, 1e-6, '99.95% is 0.71 standard errors from 99.9%');
  /* 1000 requests cannot tell 99.9% from 99.8%: the standard error at three
     nines IS the whole 0.001 gap between them. */
  near(sliSeApprox(R(999n, 1000n), 1000), 0.0009995, 1e-7, 'the SE at 99.9% on 1000 requests is 0.0999%');
  eq(sliSeApprox(R(999n, 1000n), 1000) > 0.00099, true, 'which is the entire gap to 99.8%');
  /* The window the lesson solves for: the search and the closed form agree. */
  const halfGap = Rdiv(Rsub(p1, obj), R(2n, 1n));
  eq(sampleSizeForWidth(p1, halfGap), 7996, 'separating 99.95% from 99.9% by two SE takes 7996 requests');
  eq(String(sampleSizeClosed(p1, halfGap)), '7996', 'and ceil(p(1-p)/w^2) says the same');
  for (const [pn, pd, wn, wd] of [[9995n, 10000n, 1n, 4000n], [99n, 100n, 1n, 1000n],
                                  [999n, 1000n, 1n, 10000n], [1n, 2n, 1n, 100n]]) {
    const p = R(pn, pd), w = R(wn, wd);
    eq(sampleSizeForWidth(p, w), Number(sampleSizeClosed(p, w)),
       'search equals closed form at p = ' + Rtext(p) + ', w = ' + Rtext(w));
    const n = sampleSizeForWidth(p, w);
    eq(Rcmp(sliVariance(p, n), Rmul(w, w)) <= 0, true, 'and n is large enough');
    eq(Rcmp(sliVariance(p, n - 1), Rmul(w, w)) > 0, true, 'while n - 1 is not');
  }

  /* --- L2: THE CLAIM. Percentiles do not average ------------------------ */
  const hostA = parseRuns('8, 9, 10, 11, 12');
  const hostB = parseRuns('10, 11, 12, 13, 14');
  const hostC = parseRuns('150:20, 180:20, 220:20, 260:15, 320:10, 400:5');
  const q99 = R(99n, 100n), q50 = R(1n, 2n);
  eq(hostC.length, 90, 'the run-length spec expands to ninety requests');
  eq(mergeSamples([hostA, hostB, hostC]).length, 100, 'and the fleet served a hundred');
  const perHost = hostPercentiles([hostA, hostB, hostC], q99);
  eq(perHost.join(','), '12,14,400', 'the three per-host p99s');
  const meanP99 = meanOfPercentiles(perHost);
  const fleetP99 = fleetPercentile([hostA, hostB, hostC], q99);
  const fleetMed = fleetPercentile([hostA, hostB, hostC], q50);
  eq(Rtext(meanP99), '142', 'their mean is 142 ms');
  eq(fleetP99, 400, 'the fleet p99, from the merged sample, is 400 ms');
  eq(fleetMed, 180, 'and the fleet median is 180 ms');
  /* THE assertion. If these were ever equal the merge would be fake. */
  eq(Requ(R(BigInt(fleetP99), 1n), meanP99), false,
     'the merged p99 is NOT the mean of the per-host p99s');
  eq(Rcmp(meanP99, R(BigInt(fleetMed), 1n)) < 0, true,
     'the mean of the p99s lands BELOW the fleet median -- the preset the course asks for');
  /* Two shards, each with a p99 the other does not share: the average is a
     number that belongs to neither, and the pooled figure is one of them. */
  const shardX = parseRuns('10:90, 40:10'), shardY = parseRuns('20:90, 100:10');
  eq(percentile(shardX, q99), 40, 'shard X has a p99 of 40 ms');
  eq(percentile(shardY, q99), 100, 'shard Y has a p99 of 100 ms');
  eq(Rtext(meanOfPercentiles(hostPercentiles([shardX, shardY], q99))), '70', 'their average is 70 ms');
  eq(fleetPercentile([shardX, shardY], q99), 100, 'and the pooled p99 is 100 ms, which is not 70');
  /* The bound that DOES hold, on every split this file tries: pooling can
     never exceed the largest per-host answer, because the ranks add. */
  for (const q of [R(1n, 2n), R(9n, 10n), R(95n, 100n), q99]) {
    for (const lists of [[hostA, hostB, hostC], [shardX, shardY], [hostA, hostC], [hostB]]) {
      const per = hostPercentiles(lists, q);
      eq(fleetPercentile(lists, q) <= maxOf(per), true, 'pooled <= the largest per-host value at q = ' + Rtext(q));
      eq(fleetPercentile(lists, q) >= minOf(per), true, 'pooled >= the smallest per-host value at q = ' + Rtext(q));
    }
  }
  /* The corollary, and the reason this lesson is about the MEAN rather than
     about disagreement: nearest rank sandwiches the pooled value between the
     smallest and largest per-host one, because ceil(q*n_1) + ... + ceil(q*n_h)
     is both at least ceil(q*N) and less than q*N + h. So two hosts that report
     the SAME p99 pool to exactly that p99 -- averaging them is right there and
     wrong the moment they differ, which is why the preset above differs. */
  const twinA = parseRuns('5:60, 100:3'), twinB = parseRuns('9:30, 40:5, 100:2');
  eq(percentile(twinA, q99), 100, 'one host reports a p99 of 100 ms');
  eq(percentile(twinB, q99), 100, 'so does the other');
  eq(fleetPercentile([twinA, twinB], q99), 100, 'and the pooled p99 is 100 ms too, exactly');
  /* And this course's percentiles are course 2's percentiles: same parser
     result, same rank, same value. */
  const plain = '12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420';
  eq(parseRuns(plain).join(','), parseSample(plain).join(','),
     'parseRuns and the latency kit\'s parseSample read a plain sample identically');
  eq(percentile(parseRuns(plain), q99), percentile(parseSample(plain), q99),
     'so the p99 is the same number on both courses');

  /* --- L3: bucket error -------------------------------------------------- */
  const edges = bucketEdges(25, R(2n, 1n), 6);
  eq(edges.map(Rtext).join(' '), '25 50 100 200 400 800 1600', 'doubling buckets from 25 ms');
  eq(bucketEdges(25, R(3n, 2n), 4).map(Rtext).join(' '), '25 75/2 225/4 675/8 2025/16',
     'and at r = 3/2 the edges stay fractions');
  const hSample = parseRuns('30:40, 45:25, 60:15, 85:10, 120:6, 137:3, 400:1');
  eq(hSample.length, 100, 'a hundred requests');
  eq(percentile(hSample, q99), 137, 'whose exact p99 is 137 ms');
  eq(histogramBucket(hSample, edges, q99), 2, 'the histogram reports the third bucket');
  eq(Rtext(edges[2]) + '-' + Rtext(edges[3]), '100-200', 'which is [100, 200) ms -- the lesson\'s sentence');
  eq(Rtext(bucketWidth(edges, 2)), '100', 'a bucket 100 ms wide');
  eq(Rtext(bucketRelative(R(2n, 1n))), '1', 'and a relative error of r - 1 = 100%');
  eq(Rtext(bucketRelative(R(3n, 2n))), '1/2', 'at r = 3/2 it is 50%');
  /* The relative width is r - 1 in EVERY bucket, which is the argument for
     exponential bucketing and not a property of the first one. */
  for (const [rn, rd] of [[2n, 1n], [3n, 2n], [5n, 4n], [10n, 1n]]) {
    const r = R(rn, rd), es = bucketEdges(7, r, 8);
    for (let i = 0; i < 8; i += 1) {
      eq(Requ(Rdiv(bucketWidth(es, i), es[i]), Rsub(r, R(1n, 1n))), true,
         'bucket ' + i + ' is (r-1) times its own lower edge at r = ' + Rtext(r));
    }
  }
  /* The reported bucket always contains the exact percentile. If it ever did
     not, the histogram would not be an interval estimate of anything. */
  for (const [rn, rd] of [[2n, 1n], [3n, 2n], [5n, 4n]]) {
    for (const q of [R(1n, 2n), R(9n, 10n), R(95n, 100n), q99]) {
      const es = bucketEdges(25, R(rn, rd), 9);
      const b = histogramBucket(hSample, es, q), v = percentile(hSample, q);
      if (b >= 0 && b < es.length - 1) {
        eq(Rcmp(R(BigInt(v), 1n), es[b]) >= 0 && Rcmp(R(BigInt(v), 1n), es[b + 1]) < 0, true,
           'the reported bucket contains the exact p' + Rtext(Rmul(q, R(100n, 1n))) + ' at r = ' + rn + '/' + rd);
      }
    }
  }
  const counts = bucketCounts(hSample, edges);
  eq(counts.under + counts.inside.reduce((a, b) => a + b, 0) + counts.over, 100, 'every request lands in exactly one bucket');
  eq(counts.inside.join(','), '65,25,9,0,1,0', 'the bucket counts');

  /* --- L4: coordinated omission ------------------------------------------ */
  const naive = naiveSample(100, 2, 1000);
  const fixed = correctedSample(100, 10, 2, 1000);
  eq(naive.length, 100, 'the generator recorded a hundred requests');
  eq(percentile(naive, q99), 2, 'and measured a p99 of 2 ms -- the healthy service time');
  eq(omittedCount(10, 1000), 99, 'the schedule called for 99 more during the stall');
  eq(fixed.length, 199, 'so the corrected sample holds 199');
  eq(percentile(fixed, q99), 990, 'whose p99 is 990 ms');
  eq(percentile(fixed, q50), 10, 'and whose median moves from 2 ms to 10 ms');
  eq(imputedLatencies(10, 1000)[0], 990, 'the first imputed request waited 990 ms');
  eq(imputedLatencies(10, 1000)[98], 10, 'and the last waited 10 ms');
  eq(imputedLatencies(250, 1000).join(','), '750,500,250', 'a coarser schedule imputes fewer');
  eq(imputedLatencies(2000, 1000).length, 0, 'a stall shorter than one interval omits nothing');
  /* The correction can never make a percentile faster: it only adds waiting. */
  for (const q of [R(1n, 2n), R(9n, 10n), q99, R(1n, 1n)]) {
    eq(percentile(correctedSample(100, 10, 2, 1000), q) >= percentile(naive, q), true,
       'the corrected percentile is never below the measured one at q = ' + Rtext(q));
  }

  /* --- L5: scrape intervals ---------------------------------------------- */
  eq(Rtext(catchProbability(3, 15)), '1/5', 'a 3 s spike read every 15 s');
  eq(Rpct(catchProbability(3, 15), 1), '20.0%', 'is caught a fifth of the time');
  eq(Rtext(catchProbability(60, 15)), '1', 'a spike longer than the interval is always caught');
  eq(longestInvisible(15), 14, 'and the longest invisible spike is one second short of the interval');
  eq(longestInvisible(1), 0, 'at a one-second interval nothing can hide');
  const starts = spikeStarts(12, 300, 7);
  eq(starts.length, 12, 'twelve spikes drawn from the seeded stream');
  eq(spikeStarts(12, 300, 7).join(','), starts.join(','), 'the same seed draws the same times');
  eq(spikeStarts(12, 300, 8).join(',') === starts.join(','), false, 'a different seed does not');
  eq(caughtCount(starts, 3, 15, 0), 2, 'this run caught two of the twelve, against an expected 2.4');
  /* The generator is MINSTD and the seed is mixed, and both matter HERE rather
     than in general: these draws are taken modulo a horizon and compared modulo
     a scrape interval. Under the path's glibc constants -- modulus 2^31 -- the
     low bits are a cycle, so x % 4 would read 0,1,2,3 forever and a run at a
     4, 8 or 16 second interval would catch exactly d/I of its spikes every
     time, which is the one thing this lesson exists to deny. */
  const low4 = measureStream(7, 40).map((x) => x % 4);
  eq(low4.every((v, i) => i < 4 || v === low4[i - 4]), false,
     'the low two bits of the stream are not a period-4 cycle');
  const low2 = measureStream(3, 40).map((x) => x % 2);
  eq(low2.every((v, i) => i < 2 || v === low2[i - 2]), false, 'nor do the low bits alternate');
  eq(new Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((s) => spikeStarts(12, 300, s).join(','))).size, 10,
     'ten consecutive seeds draw ten different runs');
  /* An LCG's k-th value is affine in its seed, so unmixed seeds walk a line.
     The first draw on consecutive seeds must not be an arithmetic progression. */
  const firsts = [1, 2, 3, 4, 5].map((s) => measureStream(s, 1)[0]);
  eq(firsts[1] - firsts[0] === firsts[2] - firsts[1], false, 'and consecutive seeds do not walk a straight line');
  /* A spike at least as long as the interval cannot be missed, whatever the
     phase -- the one thing the probability formula caps at one. */
  for (const off of [0, 1, 7, 14]) {
    eq(caughtCount(starts, 15, 15, off), 12, 'every 15 s spike is caught at phase ' + off);
  }

  /* A counter that restarts: the naive rate, and the correction. §4.10 gives
     this no mode of its own, so it lives with L5 -- a reset between two reads
     is the second thing a scrape interval cannot see, and the evidence for it
     is only that the number went down. */
  const csamples = counterSamples(40, 15, 300, 152);
  eq(csamples[10][1], 6000, 'at 150 s a counter climbing at 40/s reads 6000');
  eq(csamples[11][1], 520, 'and at 165 s, after a restart at 152 s, it reads 520');
  eq(resetInterval(csamples), 11, 'the eleventh window is where it went backwards');
  eq(Rtext(naiveRates(csamples)[10]), '-1096/3', 'whose naive rate is -365.33 a second');
  eq(Rcmp(naiveRates(csamples)[10], R(0n, 1n)) < 0, true, 'a negative rate for a counter that only rose');
  eq(Rtext(correctedRates(csamples)[10]), '104/3', 'the correction gives 34.67 a second, positive');
  eq(lostIncrements(40, 15, 152), 80, 'and loses the 80 increments between the last read and the restart');
  eq(Rtext(Radd(correctedRates(csamples)[10], R(BigInt(lostIncrements(40, 15, 152)), 15n))), '40',
     'corrected rate plus the lost increments over the window IS the true 40/s');
  /* Every other window is exactly the true rate, before and after the reset. */
  for (const i of [0, 5, 9, 11, 15, 18]) {
    eq(Rtext(correctedRates(csamples)[i]), '40', 'window ' + i + ' reads the true rate');
  }
  eq(resetInterval(counterSamples(40, 15, 300, 0)), -1, 'with no restart nothing goes backwards');
  eq(naiveRates(counterSamples(40, 15, 300, 0)).every((r) => Rtext(r) === '40'), true,
     'and then the naive rate is right everywhere, which is why the correction is invisible until it is not');

  /* --- L6: sampling, and the mean it ruins -------------------------------- */
  const pop = runsFromText('5:900, 8:60, 12:30, 400:10');
  eq(slowCount(pop, 100), 10, 'ten of the thousand requests are over 100 ms');
  eq(Rtext(trueMean(pop)), '467/50', 'the true mean is 9.34 ms');
  eq(Rfixed(sampledMean(pop, 100, R(1n, 100n), R(1n, 1n)), 3), '203.688',
     'a tail-biased sample averages 203.688 ms');
  /* THE CLAIM: reweighting recovers the true mean EXACTLY, at every rate and
     every threshold, which is what makes it a correction and not a fudge. */
  for (const s of [[1n, 100n], [1n, 1000n], [1n, 2n], [1n, 1n]]) {
    for (const thr of [0, 6, 10, 100, 399]) {
      eq(Requ(reweightedMean(pop, thr, R(s[0], s[1]), R(1n, 1n)), trueMean(pop)), true,
         'the reweighted mean IS the true mean at s = ' + s[0] + '/' + s[1] + ', threshold ' + thr);
    }
  }
  eq(Requ(sampledMean(pop, 100, R(1n, 1n), R(1n, 1n)), trueMean(pop)), true,
     'and with no bias at all the naive mean is already right');

  /* --- L7: cardinality ---------------------------------------------------- */
  eq(String(seriesCount([40, 120, 6, 30, 4])), '3456000', 'five labels multiply to 3 456 000 series');
  eq(Rtext(samplesPerDay(15)), '5760', 'a 15 s scrape stores 5760 samples a day');
  eq(Rfixed(gigabytes(bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 15, 2)), 2), '39.81',
     'which is 39.81 GB a day at two bytes a sample');
  eq(String(seriesCount([40, 120, 6, 30, 4, 10000])), '34560000000',
     'a user_id label does not add ten thousand series, it multiplies by ten thousand');
  eq(Rtext(Rdiv(bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 15, 2),
                bytesPerDay(seriesCount([40, 120, 6, 30, 4]), 30, 2))), '2',
     'halving the scrape interval doubles the bill');

  /* --- L8: how long to run a load test ------------------------------------ */
  const tail = R(1n, 1000n);
  eq(Rpct(atLeastOne(tail, 600), 2), '45.14%', '600 requests see the top 0.1% 45% of the time');
  eq(Rcmp(atLeastOne(tail, 600), R(1n, 2n)) < 0, true, 'so a 600-request run misses it more than half the time');
  eq(trialsForTarget(tail, R(95n, 100n), 1 << 22), 2995, '95% confidence takes 2995 requests');
  eq(Rcmp(atLeastOne(tail, 2994), R(95n, 100n)) < 0, true, 'and 2994 does not reach it');
  eq(Rcmp(atLeastOne(tail, 2995), R(95n, 100n)) >= 0, true, 'while 2995 does');
  eq(trialsForTarget(tail, R(1n, 2n), 1 << 22), 693, 'an even chance takes 693');
  /* 693 is the same integer course 2 finds for fan-out at a p99.9 per call,
     because it is the same power crossing the same half. */
  eq(fanoutBreakEven(R(999n, 1000n), 1 << 20), 693, 'which is course 2\'s fan-out break-even, exactly');
  eq(trialsForTarget(R(1n, 100n), R(95n, 100n), 1 << 22), 299, 'a p99 needs only 299 requests');

  /* --- L9: THE ERROR BUDGET IS 43.2 MINUTES ------------------------------- */
  const three = R(999n, 1000n);
  eq(Rtext(periodMinutes(30)), '43200', 'thirty days is 43 200 minutes');
  eq(Rtext(budgetMinutes(three, 30)), '216/5', 'and 99.9% of it leaves 216/5 minutes');
  eq(Rfixed(budgetMinutes(three, 30), 2), '43.20', 'which is exactly 43.2 minutes');
  eq(Requ(budgetMinutes(three, 30), R(216n, 5n)), true, 'exactly, not nearly');
  eq(Rfixed(budgetMinutes(R(9999n, 10000n), 30), 3), '4.320', 'four nines leaves 4.32 minutes');
  eq(Rfixed(budgetMinutes(three, 7), 2), '10.08', 'and a week of three nines is 10.08 minutes');
  /* The C5 convention, which is a different month and therefore a different
     figure. Both pages say which one they are using. */
  eq(Rfixed(Rdiv(Rmul(Rsub(R(1n, 1n), three), R(2628000n, 1n)), R(60n, 1n)), 1), '43.8',
     'course 5\'s 2 628 000-second month gives 43.8 minutes for the same objective');
  /* The four standard pairs, exactly. */
  eq(Rtext(burnFraction(R(144n, 10n), R(60n, 1n), 30)), '1/50', '14.4x over an hour spends 2% of the budget');
  eq(Rtext(burnFraction(R(6n, 1n), R(360n, 1n), 30)), '1/20', '6x over six hours spends 5%');
  eq(Rtext(burnFraction(R(3n, 1n), R(1440n, 1n), 30)), '1/10', '3x over a day spends 10%');
  eq(Rtext(burnFraction(R(1n, 1n), R(4320n, 1n), 30)), '1/10', '1x over three days spends 10% as well');
  eq(Rfixed(budgetSpentMinutes(R(144n, 10n), R(60n, 1n), 30, three), 3), '0.864',
     'which at three nines is 51.8 seconds of the 43.2 minutes');
  eq(Rtext(exhaustMinutes(R(144n, 10n), 30)), '3000', 'a 14.4x burn exhausts the budget in 3000 minutes');
  eq(minutesText(exhaustMinutes(R(144n, 10n), 30)), '2.08 days', 'which is just over two days');
  eq(Rtext(exhaustMinutes(R(1n, 1n), 30)), '43200', 'and a burn of 1 lasts exactly the period');
  eq(Requ(burnFraction(R(1n, 1n), periodMinutes(30), 30), R(1n, 1n)), true,
     'burning at 1 for the whole period spends the whole budget -- the definition, checked');
  eq(Rtext(burnErrorRate(R(144n, 10n), three)), '9/625', '14.4x at three nines is a 1.44% error rate');

  /* --- L10: what a threshold fires at when nothing is wrong --------------- */
  eq(String(thresholdCount(R(2n, 100n), 200)), '5', '2% of 200 is 4, so the alert needs 5 errors');
  eq(String(thresholdCount(R(25n, 1000n), 200)), '6', 'and 2.5% of 200 is 5, so it needs 6');
  eq(String(thresholdCount(R(1n, 100n), 150)), '2', 'a rate that divides exactly still needs one more');
  const perr = R(1n, 100n);
  const tail5 = falseAlarmProbability(perr, 5n, 200);
  eq(Rpct(tail5, 3), '5.175%', 'a healthy 1% service trips it in 5.175% of 200-request windows');
  eq(Rfixed(windowsPer(7 * 24 * 60, 5), 0), '2016', 'a week holds 2016 five-minute windows');
  eq(Rfixed(expectedPages(tail5, windowsPer(7 * 24 * 60, 5)), 2), '104.32',
     'so the threshold pages 104 times a week with nothing to find');
  eq(Rfixed(expectedPages(tail5, windowsPer(30 * 24 * 60, 5)), 1), '447.1', 'and 447 times a month');
  eq(Rpct(atLeastOne(tail5, 12), 2), '47.14%', 'the chance of at least one in the next hour');
  /* The cheap distribution and the shared tail must be the same number: the
     page prints one and tabulates with the other. */
  const pmf = binomialPmf(perr, 200), tails = pmfUpperTails(pmf);
  eq(pmf.length, 201, 'the distribution has n + 1 outcomes');
  eq(Rtext(tails[0]), '1', 'and it is a distribution: the terms sum to exactly one');
  for (const k of [1, 2, 5, 8, 12, 30]) {
    eq(Requ(tails[k], availKofN(perr, k, 200)), true,
       'the suffix sum at k = ' + k + ' equals availKofN, exactly');
  }
  eq(Requ(binomialTerm(perr, 5, 200), pmf[5]), true, 'and the single term agrees with the recurrence');
  /* Raising the threshold by one error cuts the false pages by a factor of
     three here -- the lever the lesson recommends, computed rather than said. */
  eq(Rcmp(availKofN(perr, 6, 200), Rdiv(availKofN(perr, 5, 200), R(3n, 1n))) < 0, true,
     'one more error on the threshold cuts the false-alarm rate by more than three');
}


// ==========================================================================
// Operations Research: the exact simplex, and the twelve kits' shared engine
// ==========================================================================
//
// scripts/mathpath/labs/or_core.py is thirteen raw-string blocks and this is
// where they are exercised directly, before any kit dresses them in modes.
//
// TWO NAMED REGRESSION TESTS carry the whole section: Beale's cycling example
// and the Klee-Minty cube. Both are lessons ABOUT things floating point
// destroys -- "the tableau is identical entry for entry" is a claim about
// equality of numbers, and a pivot count of 2^n - 1 survives only if every
// degenerate comparison lands exactly -- so if the arithmetic ever stops being
// exact, these two fail first and loudest.
console.log('operations research: the exact simplex, duality, networks and the rest');
{
  const OR_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const orSrc = fs.readFileSync(OR_SOURCE, 'utf8');
  const SYSTEMS_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const systemsSrc = fs.readFileSync(SYSTEMS_SOURCE, 'utf8');
  const orBlock = (n) => blockFrom(orSrc, n, OR_SOURCE);
  const sysBlock = (n) => blockFrom(systemsSrc, n, SYSTEMS_SOURCE);

  eval(countingBlock('BIGINT_JS') + sysdBlock('HARMONIC_JS') + sysdBlock('RCEIL_JS')
     + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
     + sysBlock('FORMAT_JS') + sysBlock('LINEAR_JS') + sysBlock('MATRIX_JS') + sysBlock('FEAS_JS')
     + orBlock('ORFMT_JS') + orBlock('TABLEAU_JS') + orBlock('PHASE_JS') + orBlock('DUAL_JS')
     + orBlock('RANGE_JS') + orBlock('NET_JS') + orBlock('TRANS_JS') + orBlock('IP_JS')
     + orBlock('SCHED_JS') + orBlock('DPSEQ_JS') + orBlock('CHAIN_JS') + orBlock('SIM_JS')
     + orBlock('INV_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rf = (n, d) => R(BigInt(n), BigInt(d));

  /* --- ORFMT: the printer this path actually needs ------------------------
     This block used to assert that algebra_core's Rdec returned NaN on the
     figure below, and offered that as the reason ORFMT_JS exists. Rdec went
     through Number, and (19/20)^400 has a 521-digit denominator.

     Rdec is BigInt long division now, so it handles this and the assertion
     that it fails would be pinning a bug as a requirement. Both printers are
     checked against each other instead.

     ORFMT_JS still earns its place, for the reason it should have given in
     the first place: Rdec strips trailing zeros, so it cannot render a fixed
     number of decimal places, and a table of figures that do not line up is
     harder to read than one that does. Rshort and Rpct are likewise about
     presentation, not about reach. */
  eq(Rfixed(rf(1, 3), 6), '0.333333', 'Rfixed is long division in BigInt');
  eq(Rfixed(rf(2, 3), 4), '0.6667', 'rounded half up at the last digit');
  eq(Rfixed(rf(-1, 8), 3), '-0.125', 'and it keeps the sign');
  const decayed = Rpow(rf(19, 20), 400);
  eq(String(decayed.n).length + '/' + String(decayed.d).length, '512/521',
     '(19/20)^400 is 512 digits over 521 -- measured here, because queue.py\'s comment says "521-digit numerator" and 521 is the DENOMINATOR');
  eq(Rfixed(decayed, 12), '0.000000001229', 'which Rfixed prints');
  eq(Rdec(decayed, 12), '0.000000001229',
     'and Rdec agrees, now that it is long division too -- it used to return NaN here');
  eq(Rfixed(rf(1, 2), 4), '0.5000', 'Rfixed pads to the places asked for');
  eq(Rdec(rf(1, 2), 4), '0.5', 'where Rdec strips them, which is why both exist');
  eq(Rshort(rf(1, 3)), '1/3', 'Rshort keeps a fraction a reader can read');
  eq(Rshort(decayed, 6), Rfixed(decayed, 6), 'and falls back to a decimal when the fraction has run away');
  eq(Rpct(rf(1, 8), 2), '12.50%', 'Rpct');
  eq(Rtext(Rfrac(rf(7, 3))), '1/3', 'the fractional part of 7/3');
  eq(Rtext(Rfrac(rf(-7, 3))), '2/3', 'and of -7/3 it is 2/3, not -1/3 -- Gomory cuts depend on it');
  eq(String(bifloor(999999n)), '999', 'bifloor floors the integer square root');
  eq(String(bifloor(2n)), '1', 'and never returns null, which is what algebra_core bisqrt does');
  eq(surdDec(Rsurd(ri(2)), 10), '1.4142135624', 'surdDec -- the one function here that rounds');
  eq(surdDec({ q: ri(40), k: 3n }, 6), '69.282032', '40 sqrt 3, to six places');
  eq(surdDec({ q: ri(-2), k: 7n }, 5), '-5.29150', 'and it carries a sign');

  /* --- REGRESSION TEST 1: BEALE'S CYCLING EXAMPLE (1955) ------------------
     max (3/4)x1 - 150x2 + (1/50)x3 - 6x4  subject to three rows and x >= 0.
     From the slack basis {x5, x6, x7}:
       * Dantzig's rule with the lowest-row-index ratio tie-break returns to
         that basis after exactly 6 pivots, with the tableau IDENTICAL entry
         for entry and z = 0 throughout;
       * Bland's rule terminates after 6 pivots at z* = 1/20.
     Same count, different ending. That contrast is C2 L7, and a float
     implementation cannot show it, because "the tableau is identical" is a
     claim about equality of numbers. */
  const beale = {
    max: true, names: ['x1', 'x2', 'x3', 'x4'],
    obj: [rf(3, 4), ri(-150), rf(1, 50), ri(-6)],
    cons: [
      { a: [rf(1, 4), ri(-60), rf(-1, 25), ri(9)], rel: 'le', b: ri(0), name: 'row 1' },
      { a: [rf(1, 2), ri(-90), rf(-1, 50), ri(3)], rel: 'le', b: ri(0), name: 'row 2' },
      { a: [ri(0), ri(0), ri(1), ri(0)], rel: 'le', b: ri(1), name: 'row 3' }]
  };
  {
    const d = lpSolve(beale, { rule: 'dantzig', maxPivots: 60 });
    eq(d.status, 'cycled', 'Beale under Dantzig CYCLES -- not "limit reached", which would teach the wrong thing');
    eq(d.run.pivots, 6, 'and it takes exactly 6 pivots to come back');
    eq(d.run.steps.map((s) => s.enterName).join(','), 'x1,x2,x3,x4,s1,s2',
       'entering x1 x2 x3 x4 x5 x6, in that order');
    eq(d.run.steps.map((s) => s.row + 1).join(','), '1,2,1,2,1,2', 'with the leaving rows alternating 1,2');
    eq(d.run.path.every((t) => Rzero(t.z[t.n])), true, 'z is 0 at every step: every pivot is degenerate');
    eq(d.run.cycle.from, 0, 'the basis it returns to is the one it started from');
    /* IDENTICAL ENTRY FOR ENTRY -- the claim the lesson makes. */
    const first = d.run.path[0], last = d.run.path[d.run.path.length - 1];
    let identical = first.basis.join(',') === last.basis.join(',');
    for (let i = 0; i < first.m; i += 1) {
      for (let j = 0; j <= first.n; j += 1) if (!Requ(first.T[i][j], last.T[i][j])) identical = false;
    }
    for (let j = 0; j <= first.n; j += 1) if (!Requ(first.z[j], last.z[j])) identical = false;
    eq(identical, true, 'and the sixth tableau equals the first ENTRY FOR ENTRY, not nearly');
    const b = lpSolve(beale, { rule: 'bland', maxPivots: 60 });
    eq(b.status, 'optimal', 'Bland terminates on the same problem');
    eq(b.run.pivots, 6, 'in the same 6 pivots');
    eq(Rtext(b.zOrig), '1/20', 'at z* = 1/20');
    eq(Rtext(lpSolve(beale, { rule: 'bestImprovement' }).zOrig), '1/20',
       'best improvement reaches the same optimum');
    eq(Rtext(lpSolve(beale, { rule: 'lastIndex' }).zOrig), '1/20', 'and so does the last-index rule');
  }

  /* --- REGRESSION TEST 2: THE KLEE-MINTY CUBE ----------------------------
     max sum 10^(n-j) x_j  subject to  2 sum_{j<i} 10^(i-j) x_j + x_i <= 100^(i-1).
     Dantzig's rule visits every one of the 2^n vertices: 3, 7, 15 pivots at
     n = 2, 3, 4, with z* = 100^(n-1). Bland's rule gives 3, 5, 9 -- the "run
     another rule and count fewer" figure C2 L9 is built on. */
  const kleeMinty = (n) => {
    const obj = [], names = [], cons = [];
    for (let j = 1; j <= n; j += 1) { obj.push(R(10n ** BigInt(n - j), 1n)); names.push('x' + j); }
    for (let i = 1; i <= n; i += 1) {
      const a = [];
      for (let j = 1; j <= n; j += 1) {
        a.push(j < i ? R(2n * 10n ** BigInt(i - j), 1n) : (j === i ? R1 : R0));
      }
      cons.push({ a: a, rel: 'le', b: R(100n ** BigInt(i - 1), 1n), name: 'row ' + i });
    }
    return { max: true, names: names, obj: obj, cons: cons };
  };
  for (const [n, dantzig, bland, star] of [[2, 3, 3, '100'], [3, 7, 5, '10000'], [4, 15, 9, '1000000']]) {
    const m = kleeMinty(n);
    const d = lpSolve(m, { rule: 'dantzig', maxPivots: 200 });
    const b = lpSolve(m, { rule: 'bland', maxPivots: 200 });
    eq(d.run.pivots, dantzig, 'Klee-Minty n = ' + n + ': Dantzig takes 2^n - 1 = ' + dantzig + ' pivots');
    eq(b.run.pivots, bland, 'and Bland takes ' + bland + ' -- run another rule and count fewer');
    eq(Rtext(d.zOrig), star, 'both stop at z* = 100^(n-1) = ' + star);
    eq(Rtext(b.zOrig), star, 'whichever rule got there');
  }
  eq(lpSolve(kleeMinty(3), { rule: 'bestImprovement' }).run.pivots, 1,
     'and best improvement walks straight to the far corner in one');

  /* THE TIE-BREAKS THEMSELVES, on an LP built so that they bite: both columns
     start with the same most-negative reduced cost, so the ONLY thing choosing
     between them is the rule. Neither Beale nor Klee-Minty exercises this --
     their reduced costs are all distinct -- and a tie-break nobody tests is a
     tie-break that was chosen by accident, which is what C2 L7 is about. */
  {
    const tied = { max: true, names: ['x1', 'x2'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(2)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(2), ri(1)], rel: 'le', b: ri(4), name: 'B' }] };
    const start = tabInit(stdForm(tied));
    const rates = tabEnter(start, 'dantzig').rates;
    eq(Rtext(rates[0].reduced) + ',' + Rtext(rates[1].reduced), '-1,-1',
       'both columns start at the same reduced cost, so only the tie-break can choose');
    eq(tabEnter(start, 'dantzig').enter, 0, 'Dantzig breaks the tie on the LOWEST column index');
    eq(tabEnter(start, 'bland').enter, 0, 'Bland takes the smallest index with a negative reduced cost');
    eq(tabEnter(start, 'lastIndex').enter, 1, 'and the last-index rule takes the other one');
    eq(lpSolve(tied, { rule: 'dantzig' }).run.steps[0].enterName, 'x1', 'so Dantzig enters x1 first');
    eq(lpSolve(tied, { rule: 'lastIndex' }).run.steps[0].enterName, 'x2', 'and last-index enters x2 first');
    eq(Rtext(lpSolve(tied, { rule: 'dantzig' }).zOrig), Rtext(lpSolve(tied, { rule: 'lastIndex' }).zOrig),
       'both reach the same optimum, by different corners');
    /* rate times step really is the change in z, which is C2 L4's panel */
    eq(rates[0].step !== null && Requ(Rmul(rates[0].rate, rates[0].step), rates[0].delta), true,
       'and every candidate column carries its own rate, step and rate x step');
    const first = lpSolve(tied, { rule: 'bestImprovement' }).run.steps[0];
    eq(Requ(first.delta, Rmul(first.rates[first.enter].rate, first.rates[first.enter].step)), true,
       'best improvement picks the largest of them, and z really moves by that much');
    const ratio = tabRatio(start, 0, 'dantzig');
    eq(ratio.rows.map((r) => (r.eligible ? Rtext(r.ratio) : '-')).join(','), '4,2',
       'the ratio test on that column is 4 and 2');
    eq(ratio.leave, 1, 'so the second row leaves');
  }

  /* --- THE INDEPENDENT ORACLE: corner enumeration -------------------------
     algebra_systems.Ccorners already enumerates the corners of a two-variable
     region exactly. Every two-variable LP can be solved both ways, and the two
     answers must agree -- a check the solver cannot fake, because Ccorners
     knows nothing about tableaux. */
  {
    const cornerOpt = (model) => {
      const cons = model.cons.map((k) => Cnew(k.a[0], k.a[1], k.b, false, ''))
        .concat([Cnew(ri(-1), ri(0), ri(0), false, ''), Cnew(ri(0), ri(-1), ri(0), false, '')]);
      const cs = Ccorners(cons);
      if (!cs.length) return { empty: true };
      if (Cunbounded(cons) && Cgrows(cons, model.obj[0], model.obj[1])) return { unbounded: true };
      let best = null;
      for (const p of cs) {
        const v = Radd(Rmul(model.obj[0], p.x), Rmul(model.obj[1], p.y));
        if (best === null || Rcmp(v, best) > 0) best = v;
      }
      return { z: best };
    };
    let x = 20260913n;
    const next = () => { x = (1103515245n * x + 12345n) % 2147483648n; return Number(x % 100n); };
    let agreed = 0, unbounded = 0;
    for (let t = 0; t < 200; t += 1) {
      const obj = [ri(1 + next() % 9), ri(1 + next() % 9)];
      const cons = [];
      for (let i = 0; i < 2 + t % 3; i += 1) {
        cons.push({ a: [ri(next() % 7 - 1), ri(next() % 7 - 1)], rel: 'le', b: ri(next() % 30), name: 'r' + i });
      }
      const model = { max: true, names: ['x', 'y'], obj: obj, cons: cons };
      const enumerated = cornerOpt(model), solved = lpSolve(model, { rule: 'dantzig', maxPivots: 200 });
      if (enumerated.unbounded) {
        if (solved.status === 'unbounded') unbounded += 1;
        else { fails += 1; console.log('  FAIL LP ' + t + ' should be unbounded, got ' + solved.status); }
        continue;
      }
      if (solved.status !== 'optimal' || !Requ(solved.zOrig, enumerated.z)) {
        fails += 1;
        console.log('  FAIL LP ' + t + ': simplex ' + solved.status + ' vs corner enumeration ' + Rtext(enumerated.z));
        continue;
      }
      /* and the point it reports is feasible and attains the value */
      const attained = Radd(Rmul(obj[0], solved.x[0]), Rmul(obj[1], solved.x[1]));
      if (!Requ(attained, solved.zOrig)) { fails += 1; console.log('  FAIL LP ' + t + ': the reported point misses its own objective'); }
      for (const k of cons) {
        if (Rcmp(Radd(Rmul(k.a[0], solved.x[0]), Rmul(k.a[1], solved.x[1])), k.b) > 0) {
          fails += 1; console.log('  FAIL LP ' + t + ': the reported point is infeasible');
        }
      }
      /* strong duality, on every one of them */
      const dv = dualVector(solved.tab);
      if (!Requ(dv.value, solved.zOrig)) { fails += 1; console.log('  FAIL LP ' + t + ': y.b != z*'); }
      if (!dv.ok) { fails += 1; console.log('  FAIL LP ' + t + ': the dual vector is infeasible'); }
      /* and B^-1 A rebuilt from the ORIGINAL matrix is the tableau, entry for entry */
      const bi = basisInverse(solved.tab);
      for (let i = 0; i < solved.tab.m; i += 1) {
        for (let j = 0; j < solved.tab.n; j += 1) {
          if (!Requ(bi.BinvA[i][j], solved.tab.T[i][j])) { fails += 1; console.log('  FAIL LP ' + t + ': B^-1 A is not the tableau'); i = 99; break; }
        }
      }
      agreed += 1;
    }
    eq(agreed, 178, '178 two-variable LPs solved by simplex and by corner enumeration agree, exactly');
    eq(unbounded, 22, 'and the other 22 are unbounded, which both methods say');
  }

  /* --- duality: the second program, and the certificate ------------------ */
  {
    const p = { max: true, names: ['x1', 'x2'], obj: [ri(3), ri(5)],
      cons: [{ a: [ri(1), ri(0)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(0), ri(2)], rel: 'le', b: ri(12), name: 'B' },
             { a: [ri(3), ri(2)], rel: 'le', b: ri(18), name: 'C' }] };
    const s = lpSolve(p);
    eq(Rtext(s.zOrig), '36', 'the textbook LP has z* = 36');
    eq(s.x.map(Rtext).join(','), '2,6', 'at (2, 6)');
    eq(dualVector(s.tab).y.map(Rtext).join(','), '0,3/2,1', 'with shadow prices 0, 3/2, 1');
    const d = dualModel(p), dd = dualModel(d);
    eq(lpSolve(d).status === 'optimal' && Requ(lpSolve(d).zOrig, s.zOrig), true, 'the dual attains the same value');
    eq(dd.max, true, 'the dual of the dual is a maximisation again');
    eq(dd.cons.map((k) => k.rel).join(','), 'le,le,le', 'with the primal\'s relations');
    eq(dd.obj.map(Rtext).join(','), p.obj.map(Rtext).join(','), 'and the primal\'s objective');
    eq(d.pairs.filter((q) => q.kind === 'row').every((q) => q.sign === 'ge0'), true,
       'every <= row of a maximisation prices at y >= 0');
    /* dualVector must report WHICH columns it read B^-1 from -- on a >= row
       the slack is the surplus column and holds nothing of the sort, which is
       C2 L8's named misconception. */
    const mixed = { max: true, names: ['x', 'y'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(10), name: 'cap' },
             { a: [ri(1), ri(0)], rel: 'ge', b: ri(2), name: 'floor' }] };
    const ms = lpSolve(mixed);
    const cols = dualVector(ms.tab).columns;
    eq(cols.map((c) => c.kind).join(','), 'slack,artificial',
       'on a >= row the identity column is the ARTIFICIAL, not the surplus beside it');
    eq(cols.filter((c) => c.isSlack).length, 1, 'so only one of the two rows reads B^-1 out of a slack');
    /* Farkas: an empty region certified rather than asserted */
    const empty = { max: true, names: ['x', 'y'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(1), name: 'first' },
             { a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'second' }] };
    const e = lpSolve(empty);
    eq(e.status, 'infeasible', 'x + y <= 1 with x + y >= 4 has no solution');
    eq(e.certificate.y.map(Rtext).join(','), '-1,1', 'and the Farkas multipliers are (-1, 1)');
    eq(e.certificate.ok, true, "y'A <= 0 and y'b > 0, verified row by row rather than claimed");
    eq(Rtext(e.certificate.checks.b.value), '3', "y'b = 3 > 0");
  }

  /* --- the two conventions a kit is most likely to get wrong -------------- */
  {
    /* A MINIMISATION is negated on the way in. Reading tab.z[n] and printing it
       is the sign error the maximised/zOrig convention exists to prevent. */
    const m = { max: false, names: ['x', 'y'], obj: [ri(2), ri(3)],
      cons: [{ a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'need' },
             { a: [ri(1), ri(0)], rel: 'le', b: ri(3), name: 'cap' }] };
    const s = lpSolve(m, { rule: 'bland' });
    eq(s.status, 'optimal', 'a minimisation with a >= row solves through Phase I');
    eq(Rtext(s.zOrig), '9', 'and its minimum is 9');
    eq(s.x.map(Rtext).join(','), '3,1', 'at (3, 1)');
    eq(Rsign(s.z) < 0, true, 'while the INTERNAL value is negative, because the solver always maximises');
    eq(Requ(zOriginal(s.std, s.z), s.zOrig), true, 'and zOriginal is what turns one into the other');
    /* A FREE variable is carried as the difference of two columns, so it can go
       negative -- which is what makes the dual of an equality row solvable. */
    const free = { max: true, names: ['u', 'v'], obj: [ri(0), ri(1)], free: [0],
      cons: [{ a: [ri(1), ri(1)], rel: 'eq', b: ri(2), name: 'sum' },
             { a: [ri(0), ri(1)], rel: 'le', b: ri(5), name: 'cap' }] };
    const fs = lpSolve(free, { rule: 'bland' });
    eq(fs.x.map(Rtext).join(','), '-3,5', 'u goes NEGATIVE, which a >= 0 column could not do');
    eq(Requ(Radd(fs.x[0], fs.x[1]), ri(2)), true, 'and the equality still holds at the point reported');
    eq(stdForm(free).kinds.slice(0, 3).join(','), 'decision,decision,decision',
       'because u became the two columns u+ and u-');
  }

  /* --- sensitivity: every answer a ratio test on the final tableau -------- */
  {
    const p = { max: true, names: ['x1', 'x2'], obj: [ri(3), ri(5)],
      cons: [{ a: [ri(1), ri(0)], rel: 'le', b: ri(4), name: 'A' },
             { a: [ri(0), ri(2)], rel: 'le', b: ri(12), name: 'B' },
             { a: [ri(3), ri(2)], rel: 'le', b: ri(18), name: 'C' }] };
    const s = lpSolve(p);
    const r1 = rhsRange(s.tab, 1), r2 = rhsRange(s.tab, 2);
    eq(Rtext(r1.lo) + '..' + Rtext(r1.hi), '6..18', 'row B holds its basis for b in [6, 18]');
    eq(Rtext(r2.lo) + '..' + Rtext(r2.hi), '12..24', 'and row C for b in [12, 24]');
    const c0 = costRange(s.tab, 0), c1 = costRange(s.tab, 1);
    eq(c0.basic && c1.basic, true, 'both decision variables are basic here');
    eq(Rtext(c0.lo) + '..' + Rtext(c0.hi), '0..15/2', 'c_1 may range over [0, 15/2]');
    eq(c1.hi, null, 'and c_2 has NO upper limit -- a one-sided interval is a real answer');
    eq(Rtext(c1.lo), '2', 'with 2 underneath');
    /* a nonbasic cost is a different formula, which is the misconception */
    const nb = { max: true, names: ['x', 'y'], obj: [ri(1), ri(5)],
      cons: [{ a: [ri(1), ri(1)], rel: 'le', b: ri(4), name: 'r' }] };
    const ns = lpSolve(nb);
    eq(costRange(ns.tab, 0).basic, false, 'x is nonbasic at the optimum');
    eq(Rtext(costRange(ns.tab, 0).hi), '5', 'so its cost may rise only to 5, where it ties');
    eq(costRange(ns.tab, 0).lo, null, 'and may fall forever');
    /* the whole piecewise-linear z*(b), checked against fresh solves */
    const curve = rhsCurve(p, 2, ri(0), ri(40));
    eq(curve.pieces.length, 3, 'z*(b_C) has three linear pieces on [0, 40]');
    eq(curve.breakpoints.map(Rtext).join(','), '12,24', 'breaking at 12 and 24');
    eq(curve.pieces.map((q) => Rtext(q.slope)).join(','), '5/2,1,0', 'with slopes 5/2, 1 and 0');
    for (const piece of curve.pieces) {
      for (const at of [piece.from, piece.to, Rdiv(Radd(piece.from, piece.to), ri(2))]) {
        const again = lpSolve({ max: true, names: p.names, obj: p.obj,
          cons: p.cons.map((k, q) => (q === 2 ? { a: k.a, rel: k.rel, b: at, name: k.name } : k)) });
        eq(Requ(again.zOrig, Radd(piece.z, Rmul(piece.slope, Rsub(at, piece.from)))), true,
           'the curve at b = ' + Rtext(at) + ' is what a fresh solve there gives');
      }
    }
    /* the efficient frontier of two objectives, and its exact breakpoint */
    const front = paramFront(p, [ri(3), ri(5)], [ri(5), ri(3)]);
    eq(front.corners.length, 2, 'two supported efficient corners');
    eq(Rtext(front.breakpoints[0]), '9/10', 'swapping at lambda = 9/10 exactly');
    eq(front.corners.map((c) => '(' + Rtext(c.f1) + ',' + Rtext(c.f2) + ')').join(' '), '(36,28) (27,29)',
       'at (36, 28) and (27, 29)');
    /* THE SAME MACHINERY ON >=, = AND FLIPPED ROWS. All three go through Phase
       I, so the column holding B^-1 is an ARTIFICIAL rather than a slack, and a
       row whose right-hand side was negative was multiplied by -1 on the way in
       -- a range quoted in those flipped units is a wrong answer that looks
       right. Every endpoint below is checked against a fresh solve, and every
       point just outside is checked to break the linear prediction. */
    for (const [label, m] of [
      ['a minimisation with two >= rows', { max: false, names: ['x', 'y'], obj: [ri(2), ri(3)],
        cons: [{ a: [ri(1), ri(1)], rel: 'ge', b: ri(4), name: 'need' },
               { a: [ri(1), ri(0)], rel: 'le', b: ri(3), name: 'cap' },
               { a: [ri(0), ri(1)], rel: 'ge', b: ri(1), name: 'floor' }] }],
      ['an equality row', { max: true, names: ['x', 'y'], obj: [ri(5), ri(4)],
        cons: [{ a: [ri(6), ri(4)], rel: 'le', b: ri(24), name: 'A' },
               { a: [ri(1), ri(2)], rel: 'le', b: ri(6), name: 'B' },
               { a: [ri(1), ri(1)], rel: 'eq', b: ri(3), name: 'exact' }] }],
      ['a row the solver had to flip', { max: true, names: ['x', 'y'], obj: [ri(1), ri(2)],
        cons: [{ a: [ri(-1), ri(-1)], rel: 'le', b: ri(-2), name: 'flipped' },
               { a: [ri(1), ri(1)], rel: 'le', b: ri(8), name: 'cap' }] }]]) {
      const sol = lpSolve(m, { rule: 'bland', maxPivots: 300 });
      eq(sol.status, 'optimal', label + ' solves');
      const dual = dualVector(sol.tab), inv = basisInverse(sol.tab);
      eq(Requ(dual.value, sol.zOrig), true, label + ': strong duality still holds');
      eq(dual.ok, true, label + ': and the dual vector is feasible');
      let matches = true;
      for (let i = 0; i < sol.tab.m; i += 1) {
        for (let j = 0; j < sol.tab.n; j += 1) if (!Requ(inv.BinvA[i][j], sol.tab.T[i][j])) matches = false;
      }
      eq(matches, true, label + ": B^-1 A rebuilt from the original matrix is still the tableau");
      for (let i = 0; i < m.cons.length; i += 1) {
        const range = rhsRange(sol.tab, i);
        eq(Requ(range.b, m.cons[i].b), true, label + ', row ' + (i + 1) + ': the range is quoted against the READER\'s b');
        const solveAt = (v) => lpSolve({ max: m.max, names: m.names, obj: m.obj,
          cons: m.cons.map((k, q) => (q === i ? { a: k.a, rel: k.rel, b: v, name: k.name } : k)) },
          { rule: 'bland', maxPivots: 300 });
        for (const [end, step] of [[range.lo, rf(-1, 100)], [range.hi, rf(1, 100)]]) {
          if (end === null) continue;
          const predict = (b) => Radd(sol.zOrig, Rmul(range.y_i, Rsub(b, range.b)));
          const again = solveAt(end);
          eq(again.status === 'optimal' && Requ(again.zOrig, predict(end)), true,
             label + ', row ' + (i + 1) + ': z at b = ' + Rtext(end) + ' is what the shadow price predicts');
          const outside = Radd(end, step), past = solveAt(outside);
          eq(past.status === 'optimal' && Requ(past.zOrig, predict(outside)), false,
             label + ', row ' + (i + 1) + ': and the prediction BREAKS just past ' + Rtext(end) + ', so the endpoint is tight');
        }
      }
    }

    /* pricing a new activity, and adding a constraint after the fact */
    const priced = priceColumn(s.tab, [ri(1), ri(1), ri(1)], ri(4));
    eq(Rtext(priced.reduced), '3/2', 'a new product earning 4 and using one of each is worth 3/2 more than it costs');
    eq(priced.enters, true, 'so it enters');
    eq(Rtext(priced.after.z[priced.after.n]), '39', 'and one pivot takes z from 36 to 39');
    const added = addRow(s.tab, { a: [ri(1), ri(1)], rel: 'le', b: ri(5) });
    const fresh = lpSolve({ max: true, names: p.names, obj: p.obj,
      cons: p.cons.concat([{ a: [ri(1), ri(1)], rel: 'le', b: ri(5), name: 'D' }]) });
    eq(added.status, 'optimal', 'a constraint appended after the fact is restored by dual simplex');
    eq(Requ(added.run.zOrig, fresh.zOrig), true, 'to exactly what a fresh solve gives');
    eq(Rtext(added.run.zOrig), '25', 'which is 25');
  }

  /* --- networks ---------------------------------------------------------- */
  {
    const nodes = ['s', 'a', 'b', 't'];
    const arcs = [{ from: 's', to: 'a' }, { from: 's', to: 'b' }, { from: 'a', to: 'b' },
                  { from: 'a', to: 't' }, { from: 'b', to: 't' }];
    eq(unimodularSweep(incidence(nodes, arcs), 4).unimodular, true,
       'a node-arc incidence matrix is totally unimodular, checked determinant by determinant');
    const odd = [[R1, R1, R0], [R1, R0, R1], [R0, R1, R1]];
    eq(Rtext(submatrixDet(odd, [0, 1, 2], [0, 1, 2])), '-2', 'an odd cycle has a determinant of -2');
    eq(unimodularSweep(odd, 3).bad.length, 1, 'so it is not unimodular, and the sweep names the submatrix');
    const acts = [{ id: 'A', dur: ri(3), pred: [] }, { id: 'B', dur: ri(2), pred: ['A'] },
                  { id: 'C', dur: ri(4), pred: ['A'] }, { id: 'D', dur: ri(2), pred: ['B', 'C'] },
                  { id: 'E', dur: ri(1), pred: ['D'] }];
    const cpm = cpmPasses(acts);
    eq(Rtext(cpm.makespan), '10', 'the project takes 10');
    eq(cpm.critical.join(''), 'ACDE', 'B is the only activity with slack');
    eq(Rtext(cpm.slack[1]), '2', 'and it has two units of it');
    eq(cpm.paths.length, 1, 'one critical path');
    eq(cpmPasses(acts.map((a) => (a.id === 'C' ? { id: 'C', dur: ri(2), pred: ['A'] } : a))).paths.length, 2,
       'shorten C and a SECOND path becomes critical -- the whole of C4 L7');
    eq(topoOrder(['a', 'b', 'c'], [{ from: 'a', to: 'b' }, { from: 'b', to: 'c' }, { from: 'c', to: 'a' }]).cycle.length,
       3, 'a cyclic project has no order, and the cycle is named');
    const wnodes = ['s', 'a', 'b', 't'];
    const warcs = [{ from: 's', to: 'a', cost: ri(4) }, { from: 's', to: 'b', cost: ri(2) },
                   { from: 'b', to: 'a', cost: ri(1) }, { from: 'a', to: 't', cost: ri(3) },
                   { from: 'b', to: 't', cost: ri(7) }];
    const bf = bellmanRounds(wnodes, warcs, 's');
    eq(bf.dist.map(Rtext).join(','), '0,3,2,6', 'Bellman-Ford labels, on rational arc costs');
    eq(potentialCheck(wnodes, warcs, bf.dist, 's', 't').ok, true,
       'and those labels are feasible potentials: pi_j - pi_i <= c_ij on every arc');
    eq(potentialCheck(wnodes, warcs, bf.dist, 's', 't').tight.length, 3, 'three arcs are tight');
    const neg = bellmanRounds(['x', 'y', 'z'],
      [{ from: 'x', to: 'y', cost: ri(1) }, { from: 'y', to: 'z', cost: ri(-3) },
       { from: 'z', to: 'x', cost: ri(1) }, { from: 'x', to: 'z', cost: ri(5) }], 'x');
    eq(neg.negative, true, 'an n-th round improvement certifies a negative cycle');
    eq(Rtext(neg.cycleCost), '-1', 'and the cycle it names really does sum to -1');
    const cnodes = ['s', 'a', 'b', 't'];
    const carcs = [{ from: 's', to: 'a', cap: ri(3) }, { from: 's', to: 'b', cap: ri(2) },
                   { from: 'a', to: 'b', cap: ri(2) }, { from: 'a', to: 't', cap: ri(2) },
                   { from: 'b', to: 't', cap: ri(3) }];
    const flow = [ri(3), ri(2), ri(1), ri(2), ri(3)];
    const cut = cutCapacity(cnodes, carcs, reachable(cnodes, residual(carcs, flow), 's').set);
    eq(Rtext(cut.capacity), '5', 'max flow 5 equals the cut the residual network shades');
    eq(Rcmp(cutCapacity(cnodes, carcs, ['s', 'a']).capacity, cut.capacity) >= 0, true,
       'and ANY other cut is at least as big, which is what makes it a proof');
    const match = bipartiteMatch(['1', '2', '3'], ['a', 'b', 'c'],
      [['1', 'a'], ['1', 'b'], ['2', 'a'], ['2', 'b'], ['3', 'a'], ['3', 'b']]);
    eq(match.size, 2, 'three workers competing for two jobs match only two');
    eq(match.cover.size, match.size, "Koenig: the minimum cover is the maximum matching, COMPUTED -- not drawn");
    eq(match.deficient.S.length > match.deficient.N.length, true, "Hall: |N(S)| < |S| on the deficient set");
    eq(match.deficient.S.join('') + '/' + match.deficient.N.join(''), '123/ab', 'which is all three onto two');
  }

  /* --- transportation and assignment -------------------------------------- */
  {
    const C = [[10, 2, 20, 11], [12, 7, 9, 20], [4, 14, 16, 18]].map((r) => r.map(ri));
    const S = [ri(15), ri(25), ri(10)], D = [ri(5), ri(15), ri(15), ri(15)];
    /* the transportation LP, solved by the simplex, is the oracle MODI is held to */
    const obj = [], names = [], cons = [];
    for (let i = 0; i < 3; i += 1) for (let j = 0; j < 4; j += 1) { obj.push(C[i][j]); names.push('x' + i + j); }
    for (let i = 0; i < 3; i += 1) {
      const a = []; for (let p = 0; p < 3; p += 1) for (let q = 0; q < 4; q += 1) a.push(p === i ? R1 : R0);
      cons.push({ a: a, rel: 'eq', b: S[i], name: 'supply ' + (i + 1) });
    }
    for (let j = 0; j < 4; j += 1) {
      const a = []; for (let p = 0; p < 3; p += 1) for (let q = 0; q < 4; q += 1) a.push(q === j ? R1 : R0);
      cons.push({ a: a, rel: 'eq', b: D[j], name: 'demand ' + (j + 1) });
    }
    const oracle = lpSolve({ max: false, names: names, obj: obj, cons: cons }, { rule: 'bland', maxPivots: 400 });
    eq(Rtext(oracle.zOrig), '435', 'the transportation LP costs 435 -- solved through Phase I, with equality rows');
    for (const start of [northwest(C, S, D), leastCost(C, S, D)]) {
      eq(start.count, start.want, start.rule + ' leaves m + n - 1 = ' + start.want + ' basic cells');
      let basis = start.basis.map((c) => ({ i: c.i, j: c.j, x: c.x }));
      const x = start.x.map((r) => r.slice());
      for (let guard = 0; guard < 30; guard += 1) {
        const uv = uvPotentials(C, basis, 3, 4);
        for (const c of basis) {
          if (!Requ(Radd(uv.u[c.i], uv.v[c.j]), C[c.i][c.j])) { fails += 1; console.log('  FAIL u + v = c fails on a basic cell'); }
        }
        if (uv.optimal) break;
        const cyc = stoneCycle(basis, uv.entering, 3, 4);
        if (!cyc.found || cyc.cells.length % 2 !== 0) { fails += 1; console.log('  FAIL the stepping-stone cycle is not a cycle'); break; }
        for (const c of cyc.cells) x[c.i][c.j] = c.sign > 0 ? Radd(x[c.i][c.j], cyc.theta) : Rsub(x[c.i][c.j], cyc.theta);
        basis = basis.filter((c) => !(c.i === cyc.leaving.i && c.j === cyc.leaving.j))
                     .concat([{ i: uv.entering.i, j: uv.entering.j }])
                     .map((c) => ({ i: c.i, j: c.j, x: x[c.i][c.j] }));
      }
      let total = R0;
      for (let i = 0; i < 3; i += 1) for (let j = 0; j < 4; j += 1) total = Radd(total, Rmul(C[i][j], x[i][j]));
      eq(Rtext(total), '435', 'MODI from the ' + start.rule + ' start reaches the LP optimum');
    }
    eq(northwest([[4, 8], [6, 2]].map((r) => r.map(ri)), [ri(5), ri(5)], [ri(5), ri(5)]).epsilon.length, 1,
       'a tie leaves a NAMED epsilon cell rather than a basis one cell short');
    eq(balance([ri(10)], [ri(4)]).dummy, 'col', 'surplus supply gets a dummy destination');
    eq(balance([ri(4)], [ri(10)]).dummy, 'row', 'and unmet demand a dummy source');
    /* Hungarian against exhaustive assignment */
    for (const cm of [[[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]],
                      [[4, 2, 8], [4, 3, 7], [3, 1, 6]],
                      [[10, 19, 8, 15], [10, 18, 7, 17], [13, 16, 9, 14], [12, 19, 8, 18]]]) {
      const cost = cm.map((r) => r.map(ri)), n = cost.length;
      const h = hungarian(cost);
      let best = null;
      const walk = (k, used, sum) => {
        if (k === n) { if (best === null || Rcmp(sum, best) < 0) best = sum; return; }
        for (let j = 0; j < n; j += 1) { if (used[j]) continue; used[j] = 1; walk(k + 1, used, Radd(sum, cost[k][j])); used[j] = 0; }
      };
      walk(0, {}, R0);
      eq(h.complete, true, 'the Hungarian method assigns everybody at n = ' + n);
      eq(Requ(h.value, best), true, 'and its value is the exhaustive optimum, ' + Rtext(best));
      eq(new Set(h.assignment).size, n, 'the assignment is a permutation');
      eq(h.steps.filter((s) => s.kind === 'cover').every((s) => s.size === s.matching.length), true,
         'every cover it drew was the size of a matching, by Koenig');
    }
  }

  /* --- integer programming ------------------------------------------------ */
  {
    const ip = { max: true, names: ['x1', 'x2'], obj: [ri(1), ri(1)],
      cons: [{ a: [ri(2), ri(5)], rel: 'le', b: ri(16), name: 'A' },
             { a: [ri(6), ri(5)], rel: 'le', b: ri(30), name: 'B' }] };
    eq(Rtext(lpSolve(ip).zOrig), '53/10', 'the relaxation stops at 53/10, which no integer plan can do');
    const lattice = latticePoints(ip, [[0n, 6n], [0n, 4n]]);
    let bestInt = null;
    for (const q of lattice.points) if (q.feasible && (bestInt === null || Rcmp(q.objective, bestInt) > 0)) bestInt = q.objective;
    eq(Rtext(bestInt), '5', 'and the exhaustive integer optimum is 5');
    for (const order of ['depthFirst', 'bestBound']) {
      const tree = bbTree(ip, { order: order, maxNodes: 60 });
      eq(tree.status, 'optimal', 'branch and bound under ' + order + ' finishes');
      eq(Requ(tree.best, bestInt), true, 'at the same 5 the lattice found');
      eq(tree.nodes.slice(1).every((n) => n.sol.from === 'dual simplex on the parent tableau'), true,
         'and every child was re-solved from its parent tableau, not from scratch');
    }
    eq(bbTree(ip, { maxNodes: 2 }).refused, true, 'a node cap REFUSES rather than reporting an unproved optimum');
    /* a Gomory cut must cut off the fractional point and keep every integer one */
    const relaxed = lpSolve(ip);
    let cutRow = -1;
    for (let i = 0; i < relaxed.tab.m; i += 1) if (!Rint(relaxed.tab.T[i][relaxed.tab.n])) { cutRow = i; break; }
    const cut = gomoryCut(relaxed.tab, cutRow);
    let here = R0;
    for (let j = 0; j < 2; j += 1) here = Radd(here, Rmul(cut.inOriginal.a[j], relaxed.x[j]));
    eq(Rcmp(here, cut.inOriginal.b) < 0, true, 'the cut excludes the fractional optimum');
    for (const q of lattice.points) {
      if (!q.feasible) continue;
      let v = R0;
      for (let j = 0; j < 2; j += 1) v = Radd(v, Rmul(cut.inOriginal.a[j], q.x[j]));
      if (Rcmp(v, cut.inOriginal.b) < 0) { fails += 1; console.log('  FAIL a Gomory cut removed a feasible integer point'); }
    }
    eq(Rzero(Rfrac(cut.fracB)), false, 'and it was derived from a row with a fractional right-hand side');
    const items = [{ name: 'a', value: ri(60), weight: ri(10) }, { name: 'b', value: ri(100), weight: ri(20) },
                   { name: 'c', value: ri(120), weight: ri(30) }];
    const knap = knapsackExact(items, ri(50));
    eq(Rtext(knap.relaxation), '240', 'the knapsack relaxation is 240');
    eq(Rtext(knap.optimum), '220', 'the exact optimum is 220');
    eq(Rtext(knap.greedy), '160', 'and greed gets 160 -- all three from one call, which is the lesson');
    eq(knap.fractionalItem.name, 'c', 'with exactly one item split');
    const d4 = [[0, 20, 42, 35], [20, 0, 30, 34], [42, 30, 0, 12], [35, 34, 12, 0]].map((r) => r.map(ri));
    eq(tspExact(d4).count, 3, 'four cities have (n-1)!/2 = 3 DISTINCT tours, not 6');
    eq(Rtext(tspExact(d4).best.cost), '97', 'the shortest is 97');
    eq(Requ(tspBranch(d4).best, tspExact(d4).best.cost), true, 'and branch and bound agrees');
    {
      // The branch table and the ring drawing must count cities the same way.
      // ipTourSvg labels city i as i + 1; these labels once read "ban 0->4"
      // beside a ring whose cities start at 1, naming the wrong pair.
      const labelled = tspBranch(d4).nodes.map((x) => x.label).filter((x) => /^ban /.test(x));
      const cities = labelled.join(' ').match(/\d+/g).map(Number);
      eq(Math.min.apply(null, cities) >= 1 && Math.max.apply(null, cities) <= 4, true,
         'branch labels name cities 1..n, the same numbering the ring picture draws');
    }
    /* tspBranch's assignment bound is a SUBSET RECURSION in IP_JS; transport's
       hungarian is Koenig covers and reductions in TRANS_JS. Two different
       algorithms for one number, so their agreement is arithmetic and not a
       shared implementation -- and `integer` does not have to carry TRANS_JS. */
    for (const cm of [[[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]],
                      [[4, 2, 8], [4, 3, 7], [3, 1, 6]],
                      [[10, 19, 8, 15], [10, 18, 7, 17], [13, 16, 9, 14], [12, 19, 8, 18]]]) {
      const cost = cm.map((r) => r.map(ri));
      eq(Requ(assignMin(cost).value, hungarian(cost).value), true,
         'the subset recursion and the Hungarian method agree at n = ' + cost.length);
    }
    const d6 = [[0, 3, 93, 13, 33, 9], [4, 0, 77, 42, 21, 16], [45, 17, 0, 36, 16, 28],
                [39, 90, 80, 0, 56, 7], [28, 46, 88, 33, 0, 25], [3, 88, 18, 46, 92, 0]].map((r) => r.map(ri));
    eq(tspExact(d6).count, 120, 'an ASYMMETRIC six-city instance has 5! = 120 tours, not 60');
    eq(Requ(tspBranch(d6, { maxNodes: 300 }).best, tspExact(d6).best.cost), true,
       'and the assignment bound with subtour cuts still finds the best of them');
  }

  /* --- scheduling ---------------------------------------------------------- */
  {
    const jobs = [{ id: 'A', p: ri(6), w: ri(1), d: ri(8) }, { id: 'B', p: ri(4), w: ri(2), d: ri(4) },
                  { id: 'C', p: ri(5), w: ri(4), d: ri(12) }, { id: 'D', p: ri(3), w: ri(3), d: ri(6) },
                  { id: 'E', p: ri(7), w: ri(1), d: ri(20) }];
    const byKey = (f) => jobs.map((_, k) => k).sort((a, b) => Rcmp(f(jobs[a]), f(jobs[b])));
    const spt = byKey((j) => j.p), wspt = byKey((j) => Rdiv(j.p, j.w)), edd = byKey((j) => j.d);
    eq(bestSequence(jobs, 'sumC').count, 120, 'five jobs is 120 orders, all of them checked');
    eq(Requ(seqObjectives(spt, jobs).sumC, bestSequence(jobs, 'sumC').value), true, 'SPT minimises sum C');
    eq(Requ(seqObjectives(wspt, jobs).sumWC, bestSequence(jobs, 'sumWC').value), true, "and Smith's order minimises sum wC");
    eq(Requ(seqObjectives(edd, jobs).Lmax, bestSequence(jobs, 'Lmax').value), true, 'and EDD minimises Lmax');
    eq(Rcmp(seqObjectives(edd, jobs).sumT, bestSequence(jobs, 'sumT').value) > 0, true,
       'but EDD LOSES on sum T to a sequence only exhaustive search finds');
    eq(Rtext(seqObjectives(spt, jobs).makespan), '25', 'while the makespan is 25 whatever the order');
    for (let i = 0; i < 4; i += 1) {
      const sw = adjacentSwap([0, 1, 2, 3, 4], i, jobs);
      eq(sw.checkC && sw.checkWC, true,
         'swapping positions ' + (i + 1) + ' and ' + (i + 2) + ' moves the objectives by exactly p_b - p_a and w_a p_b - w_b p_a');
    }
    eq(mooreHodgson(jobs).sumU, Number(bestSequence(jobs, (o) => R(BigInt(o.sumU), 1n)).value.n),
       'Moore-Hodgson attains the minimum number of late jobs');
    const fs = [{ id: '1', p1: ri(5), p2: ri(2) }, { id: '2', p1: ri(1), p2: ri(6) },
                { id: '3', p1: ri(9), p2: ri(7) }, { id: '4', p1: ri(3), p2: ri(8) },
                { id: '5', p1: ri(10), p2: ri(4) }];
    let bestFlow = null;
    const permute = (used, acc) => {
      if (acc.length === fs.length) { const v = flowshopMakespan(acc, fs).value; if (bestFlow === null || Rcmp(v, bestFlow) < 0) bestFlow = v; return; }
      for (let k = 0; k < fs.length; k += 1) { if (used[k]) continue; used[k] = 1; acc.push(k); permute(used, acc); acc.pop(); used[k] = 0; }
    };
    permute({}, []);
    eq(Requ(johnsonRule(fs).makespan.value, bestFlow), true, "Johnson's rule attains the minimum two-machine makespan");
    const par = parallelAssign([7, 6, 5, 4, 4, 4, 4].map((p, k) => ({ id: 'j' + k, p: ri(p) })), 3, 'LPT');
    eq(Rtext(par.makespan) + '/' + Rtext(par.optimum), '13/12', 'LPT gets 13 where the exhaustive optimum is 12');
    eq(Rcmp(par.ratio, rf(4, 3)) <= 0, true, 'which is inside the 4/3 ratio it is proved to');
    eq(Rtext(par.bounds.average) + ' and ' + Rtext(par.bounds.longest), '34/3 and 7',
       'and both lower bounds the proof uses are reported, not just the heuristic');
    const shop = jobShopAll([{ job: 'J1', machine: 'M1', dur: ri(3) }, { job: 'J1', machine: 'M2', dur: ri(2) },
                             { job: 'J2', machine: 'M2', dur: ri(4) }, { job: 'J2', machine: 'M1', dur: ri(1) }]);
    eq(shop.total, 4, 'two disjunctive pairs is four orientations');
    eq(Rtext(shop.best.makespan), '6', 'the best of which finishes at 6');
    eq(shop.cyclic, 1, 'and one of them DEADLOCKS, which is an answer and not an error');
    const crashActs = [{ id: 'A', normal: ri(6), crash: ri(4), normalCost: ri(100), crashCost: ri(140), pred: [] },
                       { id: 'B', normal: ri(4), crash: ri(2), normalCost: ri(80), crashCost: ri(120), pred: ['A'] },
                       { id: 'C', normal: ri(5), crash: ri(3), normalCost: ri(60), crashCost: ri(90), pred: ['A'] },
                       { id: 'D', normal: ri(3), crash: ri(2), normalCost: ri(50), crashCost: ri(80), pred: ['B', 'C'] }];
    const crash = crashModel(crashActs, ri(14));
    eq(Rtext(cpmPasses(crashActs.map((a) => ({ id: a.id, dur: a.normal, pred: a.pred }))).makespan), '14',
       'CPM says the uncrashed project takes 14');
    eq(Rzero(lpSolve(crash.model, { rule: 'bland', maxPivots: 400 }).zOrig), true, 'so at a 14-day deadline the crash bill is 0');
    const tc = rhsCurve(crash.model, crash.deadlineRow, ri(9), ri(14), { rule: 'bland', maxPivots: 400 });
    eq(tc.pieces.map((q) => Rtext(q.slope)).join(','), '-35,-30,-20,-15',
       'and the exact time-cost curve is rhsCurve on the deadline row -- the same function, not a second one');
    for (const piece of tc.pieces) {
      const again = lpSolve(crashModel(crashActs, piece.from).model, { rule: 'bland', maxPivots: 400 });
      eq(Requ(again.zOrig, piece.z), true, 'the curve at a deadline of ' + Rtext(piece.from) + ' is what a fresh solve gives');
    }
  }

  /* --- dynamic programming ------------------------------------------------- */
  {
    const stages = [['A'], ['B', 'C'], ['D', 'E'], ['F']];
    const arcs = [{ from: 'A', to: 'B', cost: ri(2) }, { from: 'A', to: 'C', cost: ri(4) },
                  { from: 'B', to: 'D', cost: ri(7) }, { from: 'B', to: 'E', cost: ri(4) },
                  { from: 'C', to: 'D', cost: ri(3) }, { from: 'C', to: 'E', cost: ri(2) },
                  { from: 'D', to: 'F', cost: ri(1) }, { from: 'E', to: 'F', cost: ri(4) }];
    const back = backwardStages(stages, arcs);
    eq(Rtext(back.value), '8', 'the cheapest route costs 8');
    eq(back.policy.map((p) => p.join('')).join('|'), 'ACDF', 'and here it is unique');
    eq(back.ties.length, 1, 'but the TIE at B is kept rather than silently resolved');
    const tied = backwardStages(stages, arcs.map((a) => (a.from === 'A' && a.to === 'B' ? { from: 'A', to: 'B', cost: R0 } : a)));
    eq(tied.policy.length, 3, 'and when a tie is ON the optimal route, every optimal route comes back');
    const demand = [ri(10), ri(62), ri(12), ri(130), ri(154), ri(129)];
    const ww = wagnerWhitin(demand, ri(54), ri(2));
    let bestPlan = null;
    for (let mask = 0; mask < (1 << (demand.length - 1)); mask += 1) {
      const orders = [0];
      for (let k = 1; k < demand.length; k += 1) if (mask & (1 << (k - 1))) orders.push(k);
      let cost = R0;
      for (let a = 0; a < orders.length; a += 1) {
        const from = orders[a], to = a + 1 < orders.length ? orders[a + 1] : demand.length;
        cost = Radd(cost, ri(54));
        for (let t = from; t < to; t += 1) cost = Radd(cost, Rmul(ri(2), Rmul(ri(t - from), demand[t])));
      }
      if (bestPlan === null || Rcmp(cost, bestPlan) < 0) bestPlan = cost;
    }
    eq(Requ(ww.cost, bestPlan), true, 'Wagner-Whitin is the exact optimum over all 32 order patterns');
    eq(Rtext(ww.cost), '294', 'which is 294');
    const heur = lotsizeHeuristics(demand, ri(54), ri(2));
    eq(Rzero(heur.silverMeal.gap), true, 'Silver-Meal happens to find it here');
    eq(Rtext(heur.leastUnitCost.gap), '306', 'and least-unit-cost is 306 worse -- two heuristics, two answers');
    const s4 = secretaryExact(4);
    eq(s4.probs.map((q) => Rtext(q.p)).join(','), '1/4,11/24,5/12,1/4', 'the secretary problem at n = 4, exactly');
    eq(s4.best, 2, 'look at one, then take the next best');
    eq(secretaryExact(100).best, 38, 'at n = 100 look at 37');
    eq(Rfixed(secretaryExact(100).bestP, 6), '0.371043', 'and succeed 37.1043% of the time');
    const offers = [[ri(10), rf(1, 3)], [ri(20), rf(1, 3)], [ri(30), rf(1, 3)]];
    const stop = stopThresholds(offers, 3, ri(1));
    eq(stop.rows.map((q) => Rtext(q.threshold)).join(','), '22,19,0', 'the stopping threshold falls as the deadline nears');
    const tree = { root: { kind: 'decision', children: [
        { label: 'build', node: { kind: 'chance', children: [
          { p: rf(3, 10), node: { kind: 'leaf', value: ri(100) } },
          { p: rf(7, 10), node: { kind: 'leaf', value: ri(-20) } }] } },
        { label: 'wait', node: { kind: 'leaf', value: ri(0) } }] },
      payoff: [[ri(100), ri(-20)], [ri(0), ri(0)]], prior: [rf(3, 10), rf(7, 10)] };
    const folded = foldBack(tree);
    eq(Rtext(folded.value), '16', 'the tree folds back to 16');
    eq(folded.root.choiceLabel, 'build', 'so build');
    eq(Rtext(folded.evpi), '14', 'and perfect information is worth 30 - 16 = 14');
    eq(folded.evsi, null, 'EVSI comes back null without a likelihood rather than being invented');
    const P = [[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]];
    const sdp = stochasticDp(['a', 'b'], ['hold', 'act'],
      [[[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]], [[rf(3, 4), rf(1, 4)], [rf(1, 2), rf(1, 2)]]],
      [[ri(1), ri(3)], [ri(2), ri(1)]], 3);
    eq(sdp.V[0].map(Rtext).join(','), '53/8,67/8', 'the three-period stochastic recursion, exactly');
    eq(sdp.policy[0].map((a) => ['hold', 'act'][a]).join(','), 'act,hold',
       'and the action it chooses in each state at the first stage');
    const dv = discountedValue(P, [ri(1), ri(3)], rf(1, 2), 20);
    eq(dv.v.map(Rtext).join(','), '22/7,38/7', 'the exact fixed point (I - gamma P)^-1 r');
    eq(Rcmp(Rabs(dv.gap[0]), rf(1, 100000)) < 0, true, 'which twenty iterations reach to five places');
    eq(String(dv.iterations[20][0].d).length > String(dv.iterations[3][0].d).length, true,
       'and the denominators grow on the way, which is worth seeing');
  }

  /* --- Markov chains and the birth-death queue ----------------------------- */
  {
    const P = [[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]];
    eq(Rtext(chainPow(P, 2)[0][0]), '3/8', 'P^2 by repeated Mmul');
    const five = [[rf(1, 5), rf(1, 5), rf(1, 5), rf(1, 5), rf(1, 5)],
                  [rf(1, 20), rf(3, 20), rf(7, 20), rf(4, 20), rf(5, 20)],
                  [rf(2, 20), rf(2, 20), rf(6, 20), rf(7, 20), rf(3, 20)],
                  [rf(9, 20), rf(1, 20), rf(1, 20), rf(4, 20), rf(5, 20)],
                  [rf(3, 20), rf(4, 20), rf(6, 20), rf(2, 20), rf(5, 20)]];
    const p12 = chainPow(five, 12)[0][0];
    eq(String(p12.n).length + '/' + String(p12.d).length, '15/16',
       'P^12 on a five-state chain is 15 digits over 16 -- past what Number holds, which is why chainPow is exact');
    eq(chainPeriod([[R0, R1, R0], [R0, R0, R1], [R1, R0, R0]], [0, 1, 2]).period, 3, 'a 3-cycle has period 3');
    eq(chainPeriod(P, [0, 1]).period, 1, 'and a chain with a self-loop is aperiodic');
    const leaky = chainClasses([[rf(1, 2), rf(1, 2), R0], [R0, R1, R0], [R0, R0, R1]]);
    eq(leaky.classes.map((c) => (c.recurrent ? 'R' : 'T')).join(''), 'TRR', 'a state that can leave and not return is transient');
    const ss = steadyState(P);
    eq(ss.pi.map(Rtext).join(','), '1/3,2/3', 'pi P = pi with sum pi = 1');
    eq(ss.dropped, 1, 'and the dropped equation is named rather than left implicit');
    eq(ss.system.length, 2, 'and the system SHOWN has n rows, not n + 1: one balance equation really was replaced');
    eq(Requ(steadyState(P, 0).pi[0], ss.pi[0]), true, 'dropping a different one gives the same pi');
    eq(Rcmp(Rabs(Rsub(chainPow(P, 30)[0][0], ss.pi[0])), rf(1, 1000000)) < 0, true, 'and P^30 approaches it');
    const ruin = [[R1, R0, R0, R0, R0], [rf(1, 2), R0, rf(1, 2), R0, R0],
                  [R0, rf(1, 2), R0, rf(1, 2), R0], [R0, R0, rf(1, 2), R0, rf(1, 2)],
                  [R0, R0, R0, R0, R1]];
    const abs = absorbing(ruin, [0, 4]);
    eq(abs.t.map(Rtext).join(','), '3,4,3', "the gambler's expected steps to ruin or riches from 1, 2, 3");
    eq(Rtext(abs.B[1][1]), '1/2', 'and from 2 the two ends are equally likely');
    eq(Requ(abs.partials[6][0][0], Radd(abs.partials[5][0][0], chainPow(abs.Q, 6)[0][0])), true,
       'the partials really are I + Q + ... + Q^k, which is what N sums to');
    const acts = [[[rf(1, 2), rf(1, 2)], [rf(1, 4), rf(3, 4)]], [[rf(3, 4), rf(1, 4)], [rf(1, 2), rf(1, 2)]]];
    const rew = [[ri(1), ri(3)], [ri(2), ri(1)]];
    const pol = policyIterate(acts, rew, rf(9, 10));
    let bestValue = null, bestPolicy = null;
    for (const a of [0, 1]) for (const b of [0, 1]) {
      const v = policyEvaluate(acts, rew, [a, b], rf(9, 10)).v;
      if (bestValue === null || (Rcmp(v[0], bestValue[0]) >= 0 && Rcmp(v[1], bestValue[1]) >= 0)) { bestValue = v; bestPolicy = [a, b]; }
    }
    eq(pol.policy.join(','), bestPolicy.join(','), 'policy iteration finds the best of all four policies');
    eq(Requ(pol.v[0], bestValue[0]), true, 'with its exact value ' + Rtext(bestValue[0]));
    /* THE KIT'S UNIFYING OBJECT: M/M/1 and M/M/s are one set of cut equations,
       and sysdesign_core's closed forms are the check panel beside them. */
    const lam = [], mu = [];
    for (let n = 0; n < 60; n += 1) { lam.push(ri(3)); mu.push(ri(5)); }
    const bd = birthDeath(lam, mu);
    eq(Rcmp(Rabs(Rsub(bd.L, mm1(ri(3), ri(5)).L)), rf(1, 1000000)) < 0, true,
       'the cut equations give the same L as sysdesign_core mm1 -- the two subjects CANNOT disagree');
    eq(bd.stable, true, 'lam < mu, so it is stable');
    eq(birthDeath([ri(5), ri(5), ri(5)], [ri(3), ri(3), ri(3)]).stable, false, 'and lam > mu is reported unstable');
    const lam2 = [], mu2 = [];
    for (let n = 0; n < 80; n += 1) { lam2.push(ri(2)); mu2.push(ri(Math.min(n + 1, 3))); }
    const mms = birthDeath(lam2, mu2, { servers: 3 });
    let waiting = R0;
    for (let n = 3; n < mms.pi.length; n += 1) waiting = Radd(waiting, mms.pi[n]);
    eq(Rcmp(Rabs(Rsub(waiting, erlangC(ri(2), ri(1), 3).pWait)), rf(1, 1000000)) < 0, true,
       'and Erlang C falls out of the SAME pi as a reading, not as a second formula');
    eq(Rcmp(Rabs(Rsub(mms.Lq, erlangC(ri(2), ri(1), 3).Lq)), rf(1, 1000000)) < 0, true, 'Lq with it');
  }

  /* --- simulation output, exactly ------------------------------------------ */
  {
    const xs = [2, 4, 4, 4, 5, 5, 7, 9].map(ri);
    eq(Rtext(sampleMean(xs)), '5', 'the sample mean');
    eq(Rtext(sampleVar(xs)), '32/7', 'and the sample variance, with n - 1 = 7 underneath');
    const ys = xs.map((x) => Radd(Rmul(ri(2), x), ri(1)));
    eq(Rtext(rhoSquared(xs, ys)), '1', 'a perfect line has rho^2 = 1 -- and rho^2 is the only one ever printed, because rho is a surd');
    eq(Requ(sampleCov(xs, ys), Rmul(ri(2), sampleVar(xs))), true, 'Cov(X, 2X + 1) = 2 Var X');
    const cov = chebyshevCover([9, 10, 11, 14, 6, 10].map(ri), ri(10), ri(2), ri(4));
    eq(Rtext(cov.bound), '3/4', 'the Chebyshev bound at k = 2');
    eq(cov.outside, 2, 'two replicates are two standard deviations out, counted by comparing SQUARES -- no root is taken');
    eq(cov.holds, false, 'and 4 of 6 falls short of the bound, which the field reports rather than hides');
    const cs = [1, 3, 2, 5, 4, 6, 8, 7].map(ri);
    const ctl = controlB(xs, cs);
    eq(Rtext(ctl.bStar), '31/42', 'the control-variate b* = Cov / Var C');
    eq(Requ(ctl.varAt, Rmul(ctl.varRaw, Rsub(R1, ctl.rho2))), true, 'and Var at b* is exactly Var X (1 - rho^2)');
    for (const d of [rf(1, 7), rf(-1, 3), ri(1), ri(-2)]) {
      eq(Rcmp(controlVarAt(ctl.quadratic, Radd(ctl.bStar, d)), ctl.varAt) >= 0, true, 'b* minimises the quadratic');
    }
    const p = [[ri(0), rf(9, 10)], [ri(1), rf(9, 100)], [ri(2), rf(1, 100)]];
    const q = [[ri(0), rf(1, 2)], [ri(1), rf(3, 10)], [ri(2), rf(1, 5)]];
    const imp = importanceRun(p, q, (x) => Rcmp(x, ri(2)) >= 0);
    eq(Rtext(imp.estimate), '1/100', 'both estimators are unbiased for the same 1/100');
    eq(Rtext(imp.ratio), '99/4', 'and importance sampling cuts the variance by 99/4');
    const refused = importanceRun(p, [[ri(0), rf(1, 2)], [ri(1), rf(1, 2)], [ri(2), R0]], (x) => Rcmp(x, ri(2)) >= 0);
    eq(refused.refused && refused.estimate === null, true,
       'q(x) = 0 where p(x) > 0 is REFUSED -- an estimator that skips the outcome is biased and no variance figure shows it');
    const des = desRun([0, 1, 2, 9].map(ri), [4, 3, 1, 2].map(ri));
    eq(des.events.map((e) => Rtext(e.t) + e.kind.charAt(0) + e.who).join(' '),
       '0a0 1a1 2a2 4d0 7d1 8d2 9a3 11d3', 'the event calendar, in order');
    eq(des.events[2].inSystem, 3, 'three in the system after the third arrival');
    eq(Rtext(des.meanWait), '2', 'the mean wait is 2');
    eq(Rtext(des.utilisation), '10/11', 'and the server was busy 10 of 11');
    const run = [];
    for (let k = 1; k <= 20; k += 1) run.push(ri(k));
    const bm = batchMeans(run, 4, 4);
    eq(bm.means.map(Rtext).join(','), '13/2,21/2,29/2,37/2', 'four batch means after a warm-up discard of four');
    eq(Rtext(bm.grand) + ' vs ' + Rtext(bm.naive), '25/2 vs 21/2', 'and the discard changes the answer, which is the point');
  }

  /* --- inventory ------------------------------------------------------------ */
  {
    const e = eoq(ri(100), ri(1200), ri(6));
    eq(e.Qsurd.k === 1n && Rtext(e.Qsurd.q) === '200', true, 'EOQ(100, 1200, 6) = 200, and this one is rational');
    eq(Requ(eoqCostAt(ri(200), ri(100), ri(1200), ri(6)), ri(1200)), true, 'costing 1200 at it');
    const irr = eoq(ri(50), ri(600), ri(5));
    eq(Rtext(irr.Qsurd.q) + 'sqrt' + irr.Qsurd.k, '20sqrt30', 'EOQ(50, 600, 5) is 20 sqrt 30 and STAYS a surd');
    eq(surdDec(irr.Qsurd, 4), '109.5445', 'printed as 109.5445 only where the page says it is rounded');
    const merged = eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1200));
    eq(merged.atMinimum && merged.roots.kind === 'double', true,
       'at T = C* the discriminant of hQ^2/2 - TQ + KD is exactly zero');
    eq(Rtext(merged.roots.roots[0]), '200', 'and the double root IS the EOQ -- derived, not asserted');
    eq(eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1300)).roots.roots.map(Rtext).join(','), '400/3,300',
       'above C* an interval of quantities is cheap enough');
    eq(eoqDiscriminant(ri(100), ri(1200), ri(6), ri(1100)).feasible, false, 'and below it, none is');
    eq(Rtext(eoqRatio(ri(2))) + ',' + Rtext(eoqRatio(rf(1, 2))), '5/4,5/4', 'twice the EOQ and half of it cost the same 25% more');
    eq(Rtext(eoqRatio(rf(6, 5))), '61/60', 'while a 20% error costs 1/60 -- under 2%, which is why the EOQ is worth using badly');
    const epq = epqCost(ri(100), ri(1200), ri(6), ri(2400), R0, R0);
    eq(Rtext(epq.factor), '1/2', 'producing at twice demand halves the effective holding rate');
    eq(Requ(epqCostAt(ri(400), R0, ri(100), ri(1200), ri(6), ri(2400), R0),
            eoqCostAt(ri(400), ri(100), ri(1200), ri(3))), true, 'and at b = 0 the EPQ IS the EOQ with h scaled by f');
    const back = epqCost(ri(100), ri(1200), ri(6), ri(2400), null, ri(6));
    eq(Rtext(back.Qsurd.q) + '/' + Rtext(back.costSurd.q), '400/600', 'with backorders at pi = h, Q* = 400 and the cost is 600');
    eq(Requ(epqCostAt(ri(400), ri(100), ri(100), ri(1200), ri(6), ri(2400), ri(6)), ri(600)), true,
       'which is what the cost formula gives at that Q and b* = 100');
    const demandPmf = [[0, rf(1, 10)], [1, rf(2, 10)], [2, rf(3, 10)], [3, rf(3, 10)], [4, rf(1, 10)]];
    const nv = newsvendor(demandPmf, ri(7), ri(3));
    eq(Rtext(nv.ratio), '7/10', 'the newsvendor critical ratio');
    eq(nv.Q, 3, 'crossed first at Q = 3');
    eq(nv.agrees, true, 'and that Q really is the cheapest on the whole tabulated curve');
    const per = [[0, rf(1, 4)], [1, rf(1, 2)], [2, rf(1, 4)]];
    const rp = reorderPoint(per, 2, 2);
    eq(Rtext(rp.meanDemand), '2', 'two periods of mean-1 demand, by pmfConvolve');
    eq(Rtext(rp.shortage), '3/8', 'and a reorder point of 2 still runs 3/8 of a unit short per cycle');
    const bs = baseStock(per, 2, 1, rf(9, 10));
    eq(bs.periods, 3, 'periodic review covers R + L = 3 periods, not one');
    eq(bs.S, 5, 'so the 90% base-stock level is 5');
    const bands = [{ from: ri(0), price: ri(10), h: rf(2, 1) },
                   { from: ri(500), price: ri(9), h: rf(18, 10) },
                   { from: ri(1000), price: ri(8), h: rf(16, 10) }];
    const disc = discountCandidates(bands, ri(40), ri(1200), ri(2));
    eq(disc.candidates.map((c) => c.at).join(' | '), 'the EOQ | the band edge | the band edge',
       'one candidate per band: its EOQ when that falls inside, the band edge when it does not');
    eq(Rtext(disc.candidates[0].cost.r) + ' + ' + Rtext(disc.candidates[0].cost.s.q) + 'sqrt' + disc.candidates[0].cost.s.k,
       '12000 + 80sqrt30', 'the first band costs an exact surd');
    eq(disc.best, 2, 'and the cheapest plan buys into the deepest discount, compared without rounding');
    eq(surdValueCmp(surdValue(ri(0), Rsurd(ri(2))), surdValue(ri(0), Rsurd(ri(3)))), -1, 'sqrt 2 < sqrt 3, exactly');
    eq(surdValueCmp(surdValue(ri(0), { q: ri(3), k: 2n }), surdValue(ri(0), { q: ri(2), k: 5n })), -1, '3 sqrt 2 < 2 sqrt 5');
    eq(surdValueCmp(surdValue(ri(0), { q: ri(3), k: 2n }), surdValue(ri(0), { q: ri(1), k: 17n })), 1, '3 sqrt 2 > sqrt 17');
    eq(surdValueCmp(surdValue(ri(1), Rsurd(ri(2))), surdValue(ri(1), Rsurd(ri(2)))), 0, 'and equal values compare equal');
  }
}


// ------------------------------------------------------------- algo_core
console.log('algorithms: counts, exact expectations, and the oracles they agree with');
{
  /* The Algorithms path's shared engine. Two things this section is for.
     First, the arithmetic: exact expectations, exact probabilities, exact
     determinants and the four quantities that are NOT exact. Second, and more
     valuable, the ORACLE AGREEMENTS: four routines here answer a question
     graph.py already answers by brute force, and where two implementations
     written from different definitions agree, both are evidence. */
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('RFIXED_JS'));
  eval(algoCoreBlock('SERIES_JS'));
  eval(algoCoreBlock('SEEDED_JS'));
  eval(algoCoreBlock('TREEDRAW_JS'));
  eval(algoCoreBlock('DIGRAPH_JS'));
  eval(algoCoreBlock('ORACLE_JS'));
  eval(algoCoreBlock('SEQ_JS'));
  eval(algoCoreBlock('HEAP_JS'));
  eval(algoCoreBlock('HASH_JS'));
  eval(algoCoreBlock('TREE_JS'));
  eval(algoCoreBlock('SORT_JS'));
  eval(algoCoreBlock('GRAPHKIT_JS'));
  eval(algoCoreBlock('FLOW_JS'));
  eval(algoCoreBlock('GREEDY_JS'));
  eval(algoCoreBlock('DP_JS'));
  eval(algoCoreBlock('STRINGS_JS'));
  eval(algoCoreBlock('GEOM_JS'));
  eval(algoCoreBlock('RANDOM_JS'));
  eval(algoCoreBlock('REDUCTION_JS'));
  eval(algoCoreBlock('COPING_JS'));
  eval(graphBlock('GRAPH_JS'));
  const loadPreset = (preset, n) => { LESSON = null; useLessonWeights = false; N = n; A = PRESETS[preset](n); };
  const loadLesson = (n, list) => { LESSON = lessonFrom(list); useLessonWeights = true; N = n; A = PRESETS.lesson(n); };
  const pair = (u, v) => Math.min(u, v) + '-' + Math.max(u, v);
  const inf = (d) => (d === null ? Infinity : d);

  /* --- the seeded stream, and the defect it exists to avoid -------------- */
  {
    const bins = [0, 0, 0, 0];
    lcgStream(1103515245, 12345, 2147483648, 7, 1200).forEach((x) => { bins[x % 4] += 1; });
    eq(bins.join(','), '300,300,300,300',
       'the glibc modulus is a power of two, so 1200 draws mod 4 come out PERFECTLY level');
    const mine = [0, 0, 0, 0];
    algoStream(7, 1200).forEach((x) => { mine[x % 4] += 1; });
    eq(mine.join(',') === '300,300,300,300', false, 'MINSTD, whose modulus 2^31 - 1 is prime, does not');
    const raw = [1, 2, 3, 4, 5, 6].map((s) => lcgStream(16807, 0, 2147483647, s, 1)[0]);
    eq(raw.join(','), '16807,33614,50421,67228,84035,100842',
       'and an unmixed seed is affine in the seed: six seeds, one straight line');
    const mixed = [1, 2, 3, 4, 5, 6].map((s) => algoStream(s, 1)[0]);
    eq(new Set(mixed.slice(1).map((v, i) => v - mixed[i])).size, 5,
       'splitmix64 before the state breaks that: five different gaps');
    eq(algoStream(3, 5).join(','), algoStream(3, 5).join(','), 'and the stream is still reproducible');
  }

  /* --- ORACLE AGREEMENT: the new graph code against graph.py's brute force */
  const LIST = [[1,2,4],[1,3,3],[2,3,2],[2,4,5],[3,4,7],[4,5,1],[5,6,6],[5,7,8],[6,7,2]];
  loadLesson(7, LIST);
  const G7 = dgFromLesson(7, LIST, false);
  eq(G7.arcs.length + ',' + edges().length, '9,9', 'both representations hold the same nine edges');
  eq(G7.arcs.map((a) => a.w).join(','), edges().map((e) => e[2]).join(','), 'at the same weights');
  eq(kruskalRun(G7).result.weight, kruskal().total,
     'kruskalRun agrees with GRAPH_JS.kruskal on the minimum spanning tree');
  eq(primRun(G7, 0).result.weight, kruskal().total, 'and so does Prim, from the cut property instead');
  for (const s of [0, 3, 6]) {
    eq(relaxRun(G7, s, 'heap').result.dist.map(inf).join(','), dijkstra(s).dist.join(','),
       'relaxRun agrees with GRAPH_JS.dijkstra from vertex ' + (s + 1));
    eq(relaxRun(G7, s, 'insertion').result.dist.map(inf).join(','), dijkstra(s).dist.join(','),
       'and relaxing in arc order reaches the same distances from ' + (s + 1));
  }
  eq(relaxRun(G7, 0, 'heap').counts.relaxations === relaxRun(G7, 0, 'insertion').counts.relaxations, false,
     'the schedule changes the WORK and not the answer');
  for (const [preset, n] of [['cycle', 6], ['tree', 7], ['path', 6], ['petersen', 6], ['complete', 5], ['star', 6]]) {
    loadPreset(preset, n);
    const Gp = dgFromMatrix(A, n, weight, false), mine = lowLink(Gp), theirs = cuts();
    eq(mine.result.bridges.map((b) => pair(b.u, b.v)).sort().join(' '),
       theirs.bridges.map((b) => pair(b.edge[0], b.edge[1])).sort().join(' '),
       'lowLink agrees with delete-and-recount on the bridges of ' + preset);
    eq(mine.result.cutVertices.join(','), theirs.cutVertices.join(','),
       'and on its cut vertices');
    eq(kruskalRun(Gp).result.weight, kruskal().total, 'and the MST weight agrees on ' + preset);
    eq(hamiltonBrute(Gp).result.circuit !== null, hamilton().circuit !== null,
       'hamiltonBrute agrees with GRAPH_JS.hamilton about a circuit on ' + preset);
    eq(cliqueBrute(Gp).result.size, cliqueNumber().size,
       'and cliqueBrute agrees with GRAPH_JS.cliqueNumber on ' + preset);
  }
  loadPreset('petersen', 6);
  {
    const Gp = dgFromMatrix(A, 6, weight, false), comp = complementGraph(Gp);
    const id = checkComplementIdentity(Gp);
    N = 6; A = dgToMatrix(comp);
    eq(cliqueBrute(comp).result.size, cliqueNumber().size,
       'the complement, handed back to GRAPH_JS through dgToMatrix, has the clique number this code found');
    eq(id.identityHolds, true, 'and |independent set| + |vertex cover| = V');
    eq(id.cliqueMatches, true, 'an independent set being a clique in the complement');
  }

  /* --- what GRAPH_JS cannot express: direction, negative weights, capacity */
  {
    const D = dgFromLesson(6, [[1,2],[2,3],[3,1],[3,4],[4,5],[5,6],[4,6]], true);
    const kinds = edgeKindCounts(classifyEdges(D, dfsTimes(D, [0]).result));
    eq([kinds.tree, kinds.back, kinds.forward, kinds.cross].join(','), '5,1,1,0',
       'the triangle contributes a back edge and 4 -> 6 a forward one');
    eq(topoDfs(D).result.acyclic + ',' + (topoKahn(D).result.order === null), 'false,true',
       'so neither topological order exists, and both say so');
    eq(kosaraju(D).result.components.map((c) => '{' + c.map((v) => v + 1).join(' ') + '}').join(' '),
       '{1 2 3} {4} {5} {6}', 'Kosaraju finds the one non-trivial strongly connected component');
    eq(kosaraju(D).result.condensationAcyclic, true, 'and the condensation is acyclic');
    const dag = dgFromLesson(6, [[1,2,3],[1,3,2],[2,4,4],[3,4,1],[4,5,2],[3,5,7],[5,6,1]], true);
    eq(dagRelax(dag, 0, 1).result.dist.join(','), '0,3,2,3,5,6', 'one pass in topological order gives shortest paths');
    eq(dagRelax(dag, 0, -1).result.dist.join(','), '0,3,2,7,9,10', 'and with the sign flipped, LONGEST paths');
    eq(relaxRun(dag, 0, 'heap').result.dist.join(','), dagRelax(dag, 0, 1).result.dist.join(','),
       'agreeing with Dijkstra on the same DAG');
    const neg = dgFromLesson(5, [[1,2,6],[1,3,7],[2,3,8],[2,4,5],[2,5,-4],[3,4,-3],[3,5,9],[4,2,-2],[5,1,2],[5,4,7]], true);
    eq(bellmanFordRounds(neg, 0).result.dist.join(','), '0,2,7,4,-2',
       'Bellman-Ford under NEGATIVE weights, which GRAPH_JS cannot hold at all');
    eq(floydSteps(dgWeightMatrix(neg)).result.dist[0].join(','), bellmanFordRounds(neg, 0).result.dist.join(','),
       'and Floyd agrees with it row for row');
    const cyc = dgFromLesson(4, [[1,2,1],[2,3,-3],[3,4,1],[4,2,1]], true);
    eq(bellmanFordRounds(cyc, 0).result.negativeCycle.map((v) => v + 1).join(' -> '), '2 -> 3 -> 4 -> 2',
       'a negative cycle comes back as the cycle itself, not as a boolean');
    const tricky = dgFromLesson(4, [[1,2,6],[2,4,9],[3,2,2],[4,3,8]], true);
    eq(floydSteps(dgWeightMatrix(tricky)).result.dist[0][2], 23,
       'Floyd reaches 1 -> 3 at 23 through two interior vertices, which the k loop must be outermost to find');
  }
  {
    const net = dgFromLesson(6, [[1,2,0,16],[1,3,0,13],[2,3,0,10],[3,2,0,4],[2,4,0,12],
                                 [3,5,0,14],[4,3,0,9],[5,4,0,7],[4,6,0,20],[5,6,0,4]], true);
    const mf = maxflow(net, 0, 5), cut = minCutFrom(net, mf.result.flow, 0);
    eq(mf.result.value + ',' + mf.result.conserved, '23,true', 'the maximum flow is 23 and conserves at every interior vertex');
    eq(cut.capacity + ',' + cut.allSaturated, '23,true', 'the minimum cut has the same capacity and every crossing arc saturated');
    eq(cut.S.map((v) => v + 1).join(','), '1,2,3,5', 'with {1, 2, 3, 5} on the source side');
    const trap = dgFromLesson(4, [[1,2,0,1],[1,3,0,1],[2,3,0,1],[2,4,0,1],[3,4,0,1]], true);
    const first = augment(trap, zeroFlow(trap), residual(trap, zeroFlow(trap)), [0, 2, 4]);
    eq(bfsPath(residual(trap, first.flow, { reverse: false }), 0, 3).path, null,
       'push one unit down the middle and WITHOUT a backward arc there is no second path');
    const back = bfsPath(residual(trap, first.flow), 0, 3);
    eq(flowValue(trap, augment(trap, first.flow, residual(trap, first.flow), back.path).flow, 0), 2,
       'and with one there is: the flow reaches 2 by undoing the middle arc');
    const net2 = matchingNetwork(3, 3, [[0,0],[0,1],[1,0],[2,1],[2,2]]);
    const m2 = maxflow(net2.graph, net2.s, net2.t);
    eq(m2.result.value + ',' + konigCover(net2, m2.result.flow).size, '3,3',
       "Konig: the matching and the cover read off the cut are the same size");
  }

  /* --- the exact expectations, and the four things that are not exact ----- */
  eq(Rtext(quickExpected(3)), '8/3', 'E[quicksort comparisons] at n = 3 is 8/3 -- (1/3)(2) + (2/3)(3), by hand');
  eq(Rtext(quickExpected(5)), '37/5', 'and 37/5 at n = 5, from an exact H_5');
  eq(Requ(quickExpected(5), Rsub(Rmul(R(12n, 1n), harmonic(5, 1)), R(20n, 1n))), true,
     'which is 2(n+1)H_n - 4n with harmonic() reused as it ships');
  eq(Rtext(buildSumExact(7).total), '4', 'Floyd build: sum ceil(7/2^{h+1})h = 0 + 2 + 2 = 4');
  eq(Rcmp(buildSumExact(7).total, R(7n, 1n)) < 0, true, 'which is under n -- the linear claim, evaluated');
  eq(Rtext(chainRun([1,2,3,4,5,6,7,8,9,10], 5, 'division').result.expectedSuccessful), '9/5',
     'expected probes in a chain: 1 + a/2 - a/2m = 9/5');
  eq(Rtext(chainRun([1,2,3,4,5,6,7,8,9,10], 5, 'division').result.measuredMean), '3/2',
     'beside the 3/2 the page measured by running all ten searches');
  eq(Rtext(ballsExact(23, 365).expectedPairs) + ',' + ballsExact(23, 365).birthdayN, '253/365,23',
     'balls in bins, exactly, and the birthday number by exact product');
  eq(Rtext(bloomExact(8, 2, 2)), '2873025/16777216', 'the exact Bloom rate at m = 8, n = 2, k = 2');
  eq(Number.isNaN(Rnum(bloomExact(1000, 100, 7))), true,
     'at m = 1000 the exact rate overflows a double -- which is why Rfixed divides the BigInts');
  eq(Rfixed(bloomExact(1000, 100, 7), 6), '0.008214', 'and prints 0.008214');
  eq(bloomApprox(1000, 100, 7).toFixed(6), '0.008194',
     'while the independent-hash idealisation says 0.008194 -- LABELLED, and the gap is the lesson');
  eq(knuthProbeApprox(0.99), null, 'the clustering curve is refused above alpha = 0.98, not extrapolated');
  eq(knuthProbeApprox(0.5).unsuccessful, 2.5, 'and reads 2.5 at alpha = 1/2 -- an approximation, and it says so');
  near(randomBstDepthApprox(15), 5.4161, 1e-3, '2 ln n is 5.416 at n = 15');
  eq(bstFromOrder([8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]).result.height, 3,
     'while the balanced tree on 15 keys has height 3: the ASYMPTOTE is not the tree');
  eq(Rtext(countMinRun([1,1,1,2,2,3,4,4,4,4], 8, 3).result.delta), '1/8',
     'count-min quotes the Markov guarantee 2^-d = 1/8, which this library proves');
  eq(countMinRun([1,1,1,2,2,3,4,4,4,4], 8, 3).result.neverUnder, true, 'and it never underestimates');

  /* --- counted algorithms, each against the baseline it claims to beat ---- */
  {
    const asc = [];
    for (let i = 1; i <= 31; i += 1) asc.push(i);
    eq(floydBuild(asc, true).counts.compares < insertBuild(asc, true).counts.compares, true,
       'Floyd builds a heap in fewer comparisons than 31 insertions');
    eq(floydBuild(asc, true).counts.swaps <= 31, true, 'and at most n swaps');
    eq(heapsortRun([5,3,8,1,9,2]).result.sorted.join(','), '1,2,3,5,8,9', 'heapsort sorts');
    const runs = [[1,4,9],[2,5,8],[3,6,7]];
    eq(kwayMerge(runs).result.merged.join(','), pairwiseMerge(runs).result.merged.join(','),
       'the k-way merge and the pairwise passes produce the same sequence');
    eq(quickRun(asc, 'last').counts.compares, 465, 'a last-element pivot on sorted input is the quadratic worst case');
    eq(quickRun(asc, 'median3').counts.compares < 465, true, 'and median-of-three is not');
    eq(quickRun(asc, 'random', 3).result.sorted.join(',') === asc.join(','), true, 'a seeded pivot still sorts');
    eq(radixRun([329,457,657,839,436,720,355], 10, true).result.sorted.join(','),
       '329,355,436,457,657,720,839', 'LSD radix sorts when its pass is stable');
    eq(radixRun([329,457,657,839,436,720,355], 10, false).result.correct, false, 'and does not when it is not');
    eq(stableRun(stableRecords([2,2,1]), 'selection').result.stable, false, 'selection sort is not stable');
    eq(stableRun(stableRecords([2,2,1]), 'insertion').result.stable, true, 'and insertion sort is');
    eq(momRun([7,2,9,4,1,8,3,6,5,10,11,12], 5, 5).result.agrees, true,
       'median of medians and quickselect find the same 5th smallest');
    eq(Rtext(levelSums(R(1n, 5n), R(7n, 10n), 100, 6).geometric), '1000',
       'and its recursion tree sums to 10n exactly, which is why it is linear');
    eq(tournament([3,1,4,1,5,9,2,6]).counts.compares <= tournament([3,1,4,1,5,9,2,6]).result.bound, true,
       'the tournament finds the second largest within n - 1 + ceil(log n) - 1 comparisons');
    eq(twoStackRun([1,2,3].map((k) => ({ op: 'enqueue', key: k }))
        .concat([{ op: 'dequeue' }, { op: 'dequeue' }, { op: 'dequeue' }])).result.order.join(','),
       '1,2,3', 'two stacks make a queue');
    eq(twoStackRun([1,2,3].map((k) => ({ op: 'enqueue', key: k }))
        .concat([{ op: 'dequeue' }, { op: 'dequeue' }, { op: 'dequeue' }])).result.withinBound, true,
       'inside the 3m the credit argument allows');
    eq(unionFindRun([0,1,2,3,4,5,6].map((i) => ({ op: 'union', a: i, b: i + 1 }))
        .concat([{ op: 'find', a: 0 }]), {}, 8).result.worstHops, 7,
       'chained unions with no rank rule make a path of length 7');
    eq(unionFindRun([0,1,2,3,4,5,6].map((i) => ({ op: 'union', a: i, b: i + 1 }))
        .concat([{ op: 'find', a: 0 }]), { rank: true }, 8).result.rankBoundHolds, true,
       'and a rank-r root has at least 2^r descendants');
    {
      // worstHops is the largest TRACE ROW; a union row is the SUM of its two
      // finds. The panel's "worst single find" column read worstHops and so
      // could print a number no find ever walked -- 8 here against a longest
      // walk of 4. worstFind is the figure that label is claiming.
      const two = [0,1,2,3].map((i) => ({ op: 'union', a: i, b: i + 1 }))
        .concat([6,7,8,9].map((i) => ({ op: 'union', a: i, b: i + 1 })))
        .concat([{ op: 'union', a: 0, b: 6 }]);
      const j = unionFindRun(two, {}, 11).result;
      eq(j.worstHops + ',' + j.worstFind, '8,4',
         'a union row sums two walks, so the worst row is not the worst single find');
    }
    eq(avlInsert([1,2,3,4,5,6,7]).result.height + ',' + avlInsert([1,2,3,4,5,6,7]).result.plainHeight, '2,6',
       'AVL holds the height at 2 where the plain BST is a path of 6');
    eq(minAvlNodes(4).n, 12, 'and N(4) = 12 is the fewest nodes an AVL tree of height 4 can hold');
    const aug = bstFromOrder([9,4,13,2,6,11,15]).result.root;
    eq(augmentWalk(aug, { op: 'select', i: 3 }).result.value + ','
       + augmentWalk(aug, { op: 'rank', key: 13 }).result.value, '6,6',
       'the order-statistic tree selects the 3rd key and ranks 13, by walking subtree sizes');
    {
      const keys = bstInorder(aug);
      let bad = 0;
      for (let lo = 0; lo <= 16; lo += 1) for (let hi = lo; hi <= 16; hi += 1) {
        if (augmentWalk(aug, { op: 'range', lo: lo, hi: hi }).result.value
            !== keys.filter((k) => k >= lo && k <= hi).length) bad += 1;
      }
      eq(bad, 0, 'and its range count agrees with a scan on all 153 intervals, while being two walks');
    }
    const t1 = treapInsert([5,2,8,1], [30,10,20,5]), t2 = treapInsert([1,8,2,5], [5,20,10,30]);
    eq(t1.result.heapOrdered + ',' + (t1.result.height === t2.result.height), 'true,true',
       'two insertion orders of the same (key, priority) set give the same treap');
  }

  /* --- greedy, DP and the optima they are checked against ---------------- */
  {
    const I = [{s:0,f:6},{s:1,f:4},{s:3,f:5},{s:3,f:8},{s:4,f:7},{s:5,f:9},{s:6,f:10},{s:8,f:11}];
    eq(greedyTrace(I, 'earliestFinish').result.matchesOptimum, true,
       'earliest finish time matches the brute-force optimum');
    eq(greedyTrace(I, 'earliestFinish').result.rows.every((r) => r.ahead !== false), true,
       'staying ahead at every step');
    eq(greedyTrace([{s:0,f:5},{s:4,f:6},{s:5,f:10}], 'shortest').result.matchesOptimum, false,
       'and the shortest-first rule does not, on the instance built to break it');
    eq(partitionRooms(I, 'start').result.optimal, true, 'interval partitioning uses exactly the depth');
    const F = [{symbol:'a',weight:45},{symbol:'b',weight:13},{symbol:'c',weight:12},
               {symbol:'d',weight:16},{symbol:'e',weight:9},{symbol:'f',weight:5}];
    const codes = huffmanBuild(F).result.codes, cost = codeCost(codes, F);
    eq(Rtext(cost.expected) + ' = ' + Rfixed(cost.expected, 2), '56/25 = 2.24',
       "Huffman on CLRS's example costs 56/25 bits per symbol, exactly");
    const small = [{symbol:'a',weight:5},{symbol:'b',weight:2},{symbol:'c',weight:1},{symbol:'d',weight:1}];
    const bestShape = allFullBinaryTrees(4)
      .map((s) => shapeCost(s, small.map((x) => x.weight)))
      .reduce((a, b) => (b < a ? b : a));
    eq(String(codeCost(huffmanBuild(small).result.codes, small).bits), String(bestShape),
       'and it attains the minimum over every full binary tree on four leaves');
    const items = [{w:10,v:60},{w:20,v:100},{w:30,v:120}];
    eq(Rtext(fractionalKnapsack(items, 50).result.value) + ',' + fractionalKnapsack(items, 50).result.integralValue,
       '240,220', 'the fractional optimum is 240 and the 0/1 optimum 220');
    eq(Rtext(fractionalKnapsack(items, 50).result.picks[2].take), '2/3', 'taking two thirds of the last item');
    const uni = independenceEnumerate([0,1,2,3], (m) => m.length <= 2);
    eq(exchangeTest(uni.result.family).isMatroid, true, 'the uniform family is a matroid');
    eq(matroidGreedy(uni.result.family, [7,5,3,1], [0,1,2,3]).result.matches, true, 'so greedy is optimal on it');
    eq(replayPolicy([1,2,3,1,4,1,2,5,1,2,3,4,5], 3, 'opt').hits
       >= replayPolicy([1,2,3,1,4,1,2,5,1,2,3,4,5], 3, 'lru').hits, true,
       'and greedy.caching is replayPolicy, reused: farthest-in-future beats LRU');
    const its = [{w:1,v:1},{w:3,v:4},{w:4,v:5},{w:5,v:7}];
    const ks = dpFill({ rows: its.length + 1, cols: 8,
      cell: (i, j, get) => {
        if (i === 0) return { v: 0, from: null };
        const skip = get(i - 1, j);
        if (its[i - 1].w > j) return { v: skip, from: [i - 1, j] };
        const take = its[i - 1].v + get(i - 1, j - its[i - 1].w);
        return take > skip ? { v: take, from: [i - 1, j - its[i - 1].w] } : { v: skip, from: [i - 1, j] };
      } });
    eq(ks.result.table[its.length][7], knapsackBrute(its, 7).result.value,
       'the knapsack table agrees with brute force');
    eq(ks.result.deps[2][5].length > 0, true, 'and every cell records the cells it actually read');
    const dims = [30,35,15,5,10,20,25];
    const mc = dpFill({ rows: 6, cols: 6, order: 'bylength',
      cell: (i, j, get) => {
        if (i === j) return { v: 0, from: null };
        let best = null, at = null;
        for (let k = i; k < j; k += 1) {
          const v = get(i, k) + get(k + 1, j) + dims[i] * dims[k + 1] * dims[j + 1];
          if (best === null || v < best) { best = v; at = [i, k]; }
        }
        return { v: best, from: at };
      } });
    eq(mc.result.table[0][5], 15125, "the matrix chain optimum is CLRS's 15125, filled by length");
    eq(lisTails([1,5,6,2,3,4]).result.subsequence.join(','), '1,2,3,4',
       'the LIS comes from predecessors, not from the tails array');
    const tree = { 0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1] }, w = [3,4,2,1,5];
    eq(treeDp(tree, w).result.value, misBrute(tree, w).result.value,
       'the tree DP agrees with brute force on the weighted independent set');
    eq(String(countWays([1,2,5], 5, 'combinations').result.count) + ','
       + String(countWays([1,2,5], 5, 'permutations').result.count), '4,9',
       'four combinations make 5 from {1, 2, 5} and nine ordered sequences do -- the loop order is the answer');
    eq(gameLabels((p) => [p - 1, p - 2, p - 3].filter((q) => q >= 0), [0,1,2,3,4,5,6,7,8]).result.losing.join(','),
       '0,4,8', 'the subtraction game {1, 2, 3} loses exactly at the multiples of 4');
    const D4 = [[0,2,9,10],[1,0,6,4],[15,7,0,8],[6,3,12,0]];
    eq(heldKarp(D4).result.length, tspBrute(D4).result.length, 'Held-Karp agrees with the brute-force tour');
    eq(String(heldKarp(D4).result.heldKarpWork) + ' vs ' + String(heldKarp(D4).result.bruteWork), '256 vs 6',
       'and prints n^2 2^n against (n - 1)! as exact integers');
  }

  /* --- strings, geometry, randomness ------------------------------------- */
  {
    const t = 'abababcabababcabc', p = 'ababc';
    eq(naiveRun(t, p).result.hits.join(','), '2,9', 'naive matching finds two occurrences');
    eq(kmpRun(t, p).result.hits.join(','), '2,9', 'KMP the same two');
    eq(horspoolRun(t, p).result.hits.join(','), '2,9', 'Horspool the same two');
    eq(rollingHash(t, p, 256, 101).result.hits.join(','), '2,9', 'and Rabin-Karp the same two');
    eq(dfaRun(t, dfaTable(p, ['a','b','c']).table, 5).result.hits.join(','), '2,9',
       'and the automaton, in exactly n steps');
    eq(kmpRun(t, p).counts.compares <= 2 * t.length, true, 'KMP inside its 2n bound');
    eq(failureFn('ababaca').result.fail.join(','), '-1,0,0,1,2,3,0,1', 'the failure function of ababaca');
    eq(Rtext(expectedPerAlignment(26)), '26/25', 'expected characters per alignment over 26 letters');
    eq(suffixArray('banana').result.suffixes.join(' '), 'a ana anana banana na nana', 'the suffix array of banana');
    eq(kasai('banana', suffixArray('banana').result.sa).result.lcp.join(','), '0,1,3,0,0,2', 'and its LCP array');
    eq(String(kasai('banana', suffixArray('banana').result.sa).result.distinctSubstrings), '15',
       'so banana has 15 distinct substrings');
    eq(ahoRun('ushers', ahoLinks(trieBuild(['he','she','his','hers']))).result.hits.length, 3,
       'Aho-Corasick reports three matches in one pass');

    eq(String(orient2([0,0],[134217729,134217728],[134217728,134217727])), '-1',
       'the exact determinant calls these three a right turn');
    eq(orient2Float([0,0],[134217729,134217728],[134217728,134217727]), 0,
       'and a double calls them collinear -- a wrong SIGN, not a rounding, which is why this block is BigInt');
    const pts = [[0,0],[1,3],[2,1],[3,4],[4,0],[5,2],[2,5],[6,3]];
    const key = (h) => h.slice().sort((x, y) => x[0] - y[0] || x[1] - y[1]).map((q) => q.join(',')).join(' ');
    eq(key(jarvis(pts).result.hull), key(monotoneChain(pts).result.hull),
       "Jarvis's march and the monotone chain find the same hull");
    eq(String(calipers(monotoneChain(pts).result.hull).result.d2), String(diameterBrute(pts).d2),
       'rotating calipers finds the same squared diameter as every pair');
    eq(String(shoelace2([[0,0],[4,0],[4,4],[0,4]])), '32', 'the doubled area of a 4x4 square is 32');
    eq(rayParity([[0,0],[4,0],[2,4]], [2,0]).onBoundary + ',' + rayParity([[0,0],[4,0],[2,4]], [2,1]).inside,
       'true,true', 'a ray through a vertex does not double count');
    const P6 = [[0,0],[10,10],[1,1],[20,20],[2,3],[30,30]];
    let brute = null;
    for (let i = 0; i < P6.length; i += 1) for (let j = i + 1; j < P6.length; j += 1) {
      const d = dist2(P6[i], P6[j]);
      if (brute === null || d < brute) brute = d;
    }
    eq(String(closestPair(P6).result.d2), String(brute), 'divide and conquer finds the same closest pair as every pair');
    eq(closestPair(P6).result.stripCompares <= closestPair(P6).result.bound, true,
       'with the strip comparisons under 7n');

    const pmf = [[0, R(1n,2n)], [1, R(1n,4n)], [4, R(1n,4n)]];
    eq(Rtext(exactTail(pmf, 4)) + ' <= ' + Rtext(markovBound(pmf, 4).bound), '1/4 <= 5/16',
       "the exact tail sits under Markov's bound, both exact");
    eq(Rcmp(exactDeviation(pmf, 2), chebyshevBound(pmf, 2).bound) <= 0, true, 'and under Chebyshev too');
    const fy = shuffleFrequencies(4, 'fisheryates'), nv = shuffleFrequencies(4, 'naive');
    eq(fy.tapes + ',' + fy.distinct + ',' + fy.uniform, '24,24,true',
       'Fisher-Yates: 24 tapes, 24 permutations, each exactly once');
    eq(nv.tapes + ',' + nv.uniform, '256,false',
       'the naive shuffle has 256 tapes and cannot be uniform -- 4^4 is not a multiple of 4!');
    const C4 = dgFromLesson(4, [[1,2],[2,3],[3,4],[4,1]], false);
    eq(Rtext(kargerExact(C4, [0,0,1,1]).probability), '1/6',
       'Karger keeps a given minimum cut of C4 with probability exactly 1/6 -- a memoised recursion, not a sample');
    eq(Requ(kargerExact(C4, [0,0,1,1]).probability, kargerExact(C4, [0,0,1,1]).bound), true,
       'which is exactly the 2/(n(n-1)) bound: C4 is a tight instance');
    eq(minCutBrute(C4).size, 2, 'and C4 does have a minimum cut of 2');
    eq(strongTest(561, 2).witness + ',' + witnessCount(561).prime, 'true,false',
       '561 is a Carmichael number: the Fermat test misses it and the strong test does not');
    eq(Rcmp(witnessCount(561).fraction, R(3n, 4n)) >= 0, true, 'at least three quarters of its bases are witnesses');
    eq(witnessCount(97).prime, true, 'and 97 has none at all');
    eq(strongTest(2047, 2).witness, false, '2047 is a strong pseudoprime to base 2');
    eq(witnessCount(2047, 4096).prime, false, 'but not to every base -- the cap is a parameter, raised here');
    const F3 = { n: 4, clauses: [[1,2,3],[-1,2,4],[1,-3,-4],[-2,3,4]] };
    eq(Rtext(max3satEnumerate(F3).mean) + ',' + max3satEnumerate(F3).matchesSevenEighths, '7/2,true',
       'over all 16 assignments the mean satisfied count is exactly 7m/8');
    eq(max3satEnumerate({ n: 3, clauses: [[1,1,2],[-1,2,3]] }).matchesSevenEighths, false,
       'and a clause that repeats a variable breaks that identity');
  }

  /* --- reductions and the coping strategies ------------------------------ */
  {
    const F = { n: 3, clauses: [[1,2,-3],[-1,-2,3],[1,-2,3]] };
    eq(selfReduce(F).result.verified, true, 'search from decision: n oracle calls build a satisfying assignment');
    eq(checkIndependentSetReduction(F).agree, true, 'the 3-SAT to independent-set reduction agrees with brute-force SAT');
    eq(checkIndependentSetReduction(F).readBackSatisfies, true, 'and the set reads back as an assignment that satisfies');
    for (const [preset, n] of [['cycle', 5], ['path', 5], ['complete', 5]]) {
      loadPreset(preset, n);
      eq(checkTspReduction(dgFromMatrix(A, n, weight, false)).agree, true,
         'the TSP instance from ' + preset + ' is within budget exactly when a Hamilton circuit exists');
    }
    const ss = satToSubsetSum({ n: 2, clauses: [[1,2],[-1,2]] });
    eq(String(ss.target) + ',' + subsetSumDp(ss.rows.map((r) => r.value), ss.target).result.found, '1144,true',
       'the subset-sum digit table has a subset hitting its target of 1s and 4s');
    const tri = dgFromLesson(3, [[1,2],[2,3],[3,1]], false);
    eq(colouringEnumerate(tri, 2).count + ',' + colouringEnumerate(tri, 3).count, '0,6',
       'a triangle has no proper 2-colouring and exactly six 3-colourings');

    const items = [{w:2,v:3},{w:3,v:4},{w:4,v:5},{w:5,v:6}];
    eq(branchBound(items, 8, true).result.correct, true, 'branch and bound finds the optimum');
    eq(branchBound(items, 8, true).counts.nodes < branchBound(items, 8, false).counts.nodes, true,
       'and the fractional bound -- the greedy lesson`s own algorithm -- prunes the tree');
    loadPreset('cycle', 6);
    const C6 = dgFromMatrix(A, 6, weight, false);
    eq(maximalMatching(C6).result.withinTwo, true, 'the matching cover is within twice the optimum');
    eq(Rtext(maximalMatching(dgFromLesson(4, [[1,2],[3,4]], false)).result.ratio), '2',
       'and on a perfect matching the ratio is exactly 2 -- the tight case');
    const metric = [[0,2,3,4],[2,0,2,3],[3,2,0,2],[4,3,2,0]];
    eq(mstTour(metric).result.metric + ',' + mstTour(metric).result.withinTwo, 'true,true',
       'the doubled-MST tour is within twice the optimum on a metric instance');
    eq(mstTour([[0,1,1,50],[1,0,1,1],[1,1,0,1],[50,1,1,0]]).result.metric, false,
       'and the toggle that drops the triangle inequality says so');
    const sets = [[1,2,3,4,5,6],[1,2,3,4],[5,6,7,8],[1,5],[2,6],[3,7],[4,8]];
    const sc = greedySetCover(sets, [1,2,3,4,5,6,7,8]);
    eq(sc.result.chargesSumToSize, true, 'the set-cover charges sum to exactly the number of sets chosen');
    eq(Rtext(sc.result.Hn) + ',' + sc.result.withinBound, '761/280,true',
       'and the cover is inside H_8 * OPT, with H_8 = 761/280 exactly');
    eq(fptasScale(items, 8, R(1n, 2n)).result.withinPromise, true, 'the FPTAS loses no more than eps * OPT');
    eq(fptasScale(items, 8, R(1n, 100n)).result.loss, 0, 'and at a small epsilon it finds the optimum');
    const F5 = { n: 4, clauses: [[1,2,3],[-1,2,4],[1,-3,-4],[-2,3,4],[-1,-2,-3]] };
    eq(Rtext(derandomise(F5).result.expectation) + ',' + derandomise(F5).result.atLeastExpectation, '35/8,true',
       'conditional expectations reach at least the 35/8 the random assignment averages');
    eq(fptVertexCover(C6, 3).result.correct + ',' + fptVertexCover(C6, 2).result.exists, 'true,false',
       'FPT vertex cover agrees with brute force at k = 3 and reports none at k = 2');
    eq(fptVertexCover(C6, 3).counts.nodes <= fptVertexCover(C6, 3).result.treeBound, true,
       'inside a search tree of 2^(k+1) nodes however big the graph is');
    eq(dpllRun(F5).result.agrees + ',' + dpllRun(F5).result.verified, 'true,true', 'DPLL agrees with brute-force SAT');
    eq(dpllRun({ n: 3, clauses: [[1,2],[1,-2],[-1,3],[-1,-3]] }).result.satisfiable, false,
       'and proves an unsatisfiable formula unsatisfiable');
  }

  /* --- the two drawings, asserted on the strings they return -------------- */
  {
    const sc = seriesScale([{ values: [0, 5, 10, 10] }], [1, 2, 3, 4], {});
    eq(sc.y(10) + ',' + sc.y(0) + ',' + sc.x(0) + ',' + sc.x(3), '14,200,26,496',
       'the series scale puts the maximum on the top of the box and zero on the baseline');
    const svg = drawSeries(null, [
      { label: 'measured', values: [1, 2, 3, 4], colour: 'var(--cyan)', points: true },
      { label: 'n log n', values: [0, 2, 4.7, 8], colour: 'var(--amber)', dashed: true }], [1, 2, 3, 4], {});
    eq(svg.indexOf('stroke-dasharray') !== -1, true, 'a predicted curve is dashed and a measured one is not');
    eq((svg.match(/<circle /g) || []).length, 4, 'with the measured samples marked');
    const Gd = dgNew(4, true);
    dgAdd(Gd, 0, 1, -3); dgAdd(Gd, 1, 2, 5); dgAdd(Gd, 2, 0, 2); dgAdd(Gd, 1, 0, 7);
    const gsvg = drawGraph(null, Gd, {});
    eq((gsvg.match(/<polygon /g) || []).length, 4, 'every arc of a directed graph gets an arrowhead');
    eq((gsvg.match(/ Q/g) || []).length, 2, 'and the antiparallel pair is bowed so neither hides the other');
    eq(drawTree(null, bstFromOrder([9,4,13,2,6,11,15]).result.root, bstKids, (n) => n.key)
       .match(/<circle /g).length, 7, 'the tree renderer draws every node');
    eq(matrixHtml([[0, 1], [1, 0]], { caption: 'A' }).indexOf('<caption>A</caption>'), 0,
       'and the matrix painter returns its own markup, with no element involved');
  }

  /* --- the caps refuse rather than freeze the tab ------------------------ */
  {
    const refuses = (f) => { try { f(); return false; } catch (e) { return /exceeds/.test(e.message); } };
    eq(refuses(() => knapsackBrute(new Array(13).fill({ w: 1, v: 1 }), 4)), true, 'thirteen knapsack items are refused');
    eq(refuses(() => allSpanningTrees(dgFromLesson(9, [[1,2]], false))), true, 'nine vertices of spanning trees are refused');
    eq(refuses(() => allFullBinaryTrees(6)), true, 'six leaves of full binary trees are refused');
    eq(refuses(() => witnessCount(3001)), true, 'and n = 3001 witnesses is refused -- not slow, refused');
  }
}

if (fails) {
  console.log('\n' + fails + ' assertion(s) FAILED');
  process.exit(1);
}

// ==========================================================================
// Operations Research course 1: the `lp` kit's own arithmetic
// ==========================================================================
//
// or_core is tested above; this is the layer the ten modelling lessons put on
// top of it, in scripts/mathpath/labs/lp.py. The one claim worth naming is the
// DISPATCH: two variables are answered by algebra_systems' corner enumeration
// and three or more by the exact simplex, and the two routes must agree about
// the same situation. A kit that quietly answered everything one way would
// pass labcheck, paint, and teach a reader that the picture is the method.
console.log('operations research: linear programming models, the lp kit');
{
  const LP_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'lp.py');
  const lpSrc = fs.readFileSync(LP_SOURCE, 'utf8');
  const OR2_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const or2Src = fs.readFileSync(OR2_SOURCE, 'utf8');
  const SYS2_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const sys2Src = fs.readFileSync(SYS2_SOURCE, 'utf8');
  const lpBlock = (n) => blockFrom(lpSrc, n, LP_SOURCE);
  const or2Block = (n) => blockFrom(or2Src, n, OR2_SOURCE);
  const sys2Block = (n) => blockFrom(sys2Src, n, SYS2_SOURCE);

  eval(countingBlock('BIGINT_JS')
     + sys2Block('FORMAT_JS') + sys2Block('LINEAR_JS') + sys2Block('MATRIX_JS') + sys2Block('FEAS_JS')
     + or2Block('ORFMT_JS') + or2Block('TABLEAU_JS') + or2Block('PHASE_JS')
     + lpBlock('LP_JS') + lpBlock('BLEND_JS') + lpBlock('GOAL_JS') + lpBlock('BASIS_JS')
     + lpBlock('SEG_JS') + lpBlock('REFORM_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rr = (n, d) => R(BigInt(n), BigInt(d));

  /* --- THE DISPATCH: the same workshop, two and three products ----------- */
  const mixRow = (a, b, name) => ({ a: a.map(ri), rel: 'le', b: ri(b), name: name });
  const mix2 = { max: true, names: ['C', 'T'], obj: [ri(3), ri(5)],
    cons: [mixRow([1, 0], 4, 'the carpentry shop'), mixRow([0, 2], 12, 'the finishing shop'),
           mixRow([3, 2], 18, 'the assembly line')] };
  const mix3 = { max: true, names: ['C', 'T', 'B'], obj: [ri(3), ri(5), ri(4)],
    cons: [mixRow([1, 0, 1], 4, 'the carpentry shop'), mixRow([0, 2, 1], 12, 'the finishing shop'),
           mixRow([3, 2, 2], 18, 'the assembly line')] };
  const s2 = lpSolveModel(mix2), s3 = lpSolveModel(mix3);
  eq(s2.method + ' ' + s3.method, 'corners simplex',
     'two variables go to Ccorners and three to the simplex -- the dispatch is the kit, not the mode');
  eq(Rtext(s2.z) + ' at ' + s2.x.map(Rtext).join(','), '36 at 2,6',
     'the two-product workshop is worth 36 at (2, 6), by corner enumeration');
  eq(Rtext(s3.z) + ' at ' + s3.x.map(Rtext).join(','), '75/2 at 1,9/2,3',
     'and the three-product one is worth 75/2 at (1, 9/2, 3) -- a fraction a float would round');
  eq(s2.corners.length + ',' + s2.corners.filter((c) => c.inRegion).length, '5,5',
     'with five corners, all of them in the region');
  /* The two routes must agree where they overlap: drive the third product's
     column to zero and the three-variable model IS the two-variable one. */
  const pinned = { max: true, names: mix3.names, obj: mix3.obj,
    cons: mix3.cons.concat([{ a: [R0, R0, R1], rel: 'le', b: R0, name: 'no benches' }]) };
  eq(Rtext(lpByEngine(pinned).z), Rtext(s2.z),
     'and with the third column pinned at zero the engine agrees with the corners exactly');

  /* --- a candidate point, constraint by constraint ----------------------- */
  const good = lpCandidate(mix2, [ri(2), ri(6)]);
  eq(good.ok + ',' + good.rows.length, 'true,5',
     'a candidate is checked against five rows, because the two sign restrictions are rows too');
  const bad = lpCandidate(mix2, [ri(4), ri(6)]);
  eq(bad.failed.map((i) => bad.rows[i].name).join(','), 'the assembly line',
     'and a failure NAMES the constraint that failed rather than the model');
  eq(Rtext(bad.rows[bad.failed[0]].diff), '6',
     'with the signed difference that failed it');
  eq(lpCandidate(mix2, [ri(-1), ri(0)]).failed.length, 1,
     'a negative decision breaks exactly the sign restriction -- dropping x >= 0 changes the answer');

  /* --- slack, surplus, and tight <=> zero -------------------------------- */
  const slacks = lpSlackRows(mix2, s2.x).rows;
  eq(slacks.map((q) => q.varName + '=' + Rtext(q.value)).join(' '), 's1=2 s2=0 s3=0',
     'the carpentry shop has two hours left and the other two rows are used right up');
  eq(slacks.map((q) => q.tight).join(','), 'false,true,true',
     'and tight is exactly where the added variable is zero');
  const diet = { max: false, names: ['G', 'P'], obj: [ri(2), ri(3)],
    cons: [{ a: [ri(1), ri(3)], rel: 'ge', b: ri(9), name: 'the protein requirement' },
           { a: [ri(2), ri(1)], rel: 'ge', b: ri(8), name: 'the fibre requirement' }] };
  eq(lpSlackRows(diet, [ri(4), ri(2)]).rows.map((q) => q.kind + ' ' + Rtext(q.value)).join(', '),
     'surplus 1, surplus 2',
     'a >= row carries a SURPLUS: at (4, 2) protein is over-fulfilled by 1 and fibre by 2');

  /* --- the recession cone: an unbounded REGION is not an unbounded problem */
  const dr = lpRecession(diet, [{ name: 'more grain', d: [R1, R0] },
                                { name: 'more pellets', d: [R0, R1] }]);
  eq(dr.unboundedRegion + ',' + dr.runs, 'true,false',
     'the diet region runs on forever and the cost still has a minimum -- the lesson in one line');
  eq(dr.rows.map((q) => q.recession + ':' + Rtext(q.change)).join(' '), 'true:2 true:3',
     'both named directions are recession directions and the cost only climbs along them');
  eq(Rtext(lpSolveModel(diet).z) + ' at ' + lpSolveModel(diet).x.map(Rtext).join(','), '12 at 3,2',
     'so the minimum exists, at a corner, and costs 12');
  const credited = { max: false, names: diet.names, obj: [ri(2), ri(-1)], cons: diet.cons };
  eq(lpRecession(credited, []).runs + ',' + lpSolveModel(credited).status, 'true,unbounded',
     'give the second feed a disposal credit and the SAME region now has no minimum at all');
  eq(lpSolveModel(credited).z, null,
     'and the lab is handed no value to print, rather than the last point the search stood on');

  /* --- blending: the share cleared, and the clearing that is declined ---- */
  const tA = rr(30, 100), tC = rr(25, 100);
  const blend = { max: false, names: ['N', 'R', 'B'], obj: [ri(5), ri(3), ri(2)],
    cons: [{ a: [R1, R1, R1], rel: 'eq', b: ri(100), name: 'the batch is filled exactly' },
           lpShareRow(0, tA, 3, true, 'the naphtha share'),
           lpShareRow(2, tC, 3, false, 'the butane ceiling')] };
  eq(Ltext(blend.cons[1].a, blend.names), '(7/10)N - (3/10)R - (3/10)B',
     'the share requirement clears to (1 - t) on the component and -t on every other');
  const bs = lpSolveModel(blend);
  eq(bs.x.map(Rtext).join(',') + ' costing ' + Rtext(bs.z), '30,45,25 costing 335',
     'and the cheapest batch is 30 / 45 / 25 litres at 335');
  eq(lpShares(bs.x).shares.map(Rtext).join(' '), '3/10 9/20 1/4',
     'with the achieved shares printed as EXACT fractions, 3/10 and 1/4 being the two bounds');
  eq(lpDenominatorCanVanish(blend, 2).canVanish, true,
     'a feasible blend with no butane exists, so N / B >= 2 may not be cleared: the lab declines it');

  /* --- multiperiod: one aggregate row is NOT T balance rows -------------- */
  const demand = [20, 35, 30, 25].map(ri), costs = [9, 8, 7, 6].map(ri);
  const bal = lpSolveModel(lpBalanceModel(demand, ri(60), costs, R1, ri(5)));
  const agg = lpSolveModel(lpAggregateModel(demand, ri(60), costs, R1, ri(5)));
  eq(bal.x.slice(0, 4).map(Rtext).join(',') + ' at ' + Rtext(bal.z), '15,35,30,25 at 775',
     'the balance rows make the plan follow demand, at a cost of 775');
  eq(agg.x.map(Rtext).join(',') + ' at ' + Rtext(agg.z), '0,0,45,60 at 675',
     'the aggregate row lets it wait for the cheap periods, at a cost of 675 -- CHEAPER');
  eq(Rtext(lpRunStock(agg.x, demand, ri(5)).unmet), '50',
     'and that cheaper plan leaves 50 units of demand unserved, which the cost cannot show');
  eq(Rtext(lpRunStock(bal.x.slice(0, 4), demand, ri(5)).unmet), '0',
     'while the balance plan leaves none');

  /* --- goal programming: the order is the answer ------------------------- */
  const base = { names: ['S', 'D'],
    cons: [{ a: [ri(2), ri(3)], rel: 'le', b: ri(60), name: 'machine hours' }] };
  const goals = [{ a: [ri(3), ri(4)], target: ri(60), mind: 'under', name: 'the profit target' },
                 { a: [ri(3), ri(6)], target: ri(30), mind: 'over', name: 'the overtime limit' },
                 { a: [R0, R1], target: ri(12), mind: 'under', name: 'the deluxe run' }];
  const readOff = (order) => {
    const lex = goalLexicographic(base, goals, order);
    return [0, 1, 2].map((g) => Rtext(lex.levels.filter((L) => L.goal === g)[0].achieved)).join('/');
  };
  eq(readOff([0, 1, 2]), '0/30/12', 'profit first: the target is met and overtime pays 30 hours for it');
  eq(readOff([1, 0, 2]), '30/0/12', 'overtime first: overtime is met and profit misses by 30');
  eq(readOff([2, 0, 1]), '0/54/0', 'the deluxe run first: both other goals move, and overtime pays 54');
  const lexFirst = goalLexicographic(base, goals, [0, 1, 2]);
  const w = goalWeighted(base, goals, [R1, R1, R1]);
  const wd = goalDeviations(base, goals, w.result.x);
  eq([0, 1, 2].map((g) => Rtext(goals[g].mind === 'over' ? wd[g].over : wd[g].under)).join('/'),
     '30/0/12',
     'one weighted objective with equal weights silently solves the OTHER order: pounds added to hours');
  eq(Rtext(lexFirst.levels[1].frozen[0].b), '0',
     'each level hands the next a frozen equality, not a suggestion');
  eq(lexFirst.levels.length, 3, 'and a three-goal programme is three linear programmes');

  /* --- every basis of a small programme ---------------------------------- */
  const bt = lpBasisTable(mix2);
  eq(String(bt.count) + ',' + bt.rows.length, '10,10',
     'C(n + m, m) = C(5, 3) = 10 bases, and ten is what the enumeration produces');
  const kinds = {};
  bt.rows.forEach((b) => { kinds[b.solve.kind] = (kinds[b.solve.kind] || 0) + 1; });
  eq(JSON.stringify(kinds), '{"feasible":5,"infeasible":3,"singular":2}',
     'five basic FEASIBLE solutions, three crossings outside the region, two singular choices');
  eq(kinds.feasible, bt.corners.length,
     'and the basic feasible solutions are exactly the corners of the picture');
  const singular = bt.rows.filter((b) => b.solve.singular)[0];
  eq(singular.parallel + ' ' + singular.lines.map((L) => L.text).join(' | '),
     'true T = 0 | 2T = 12',
     'a singular basis is two PARALLEL lines, named -- not "the matrix was singular"');
  const outside = bt.rows.filter((b) => b.solve.kind === 'infeasible')
    .map((b) => '(' + Rtext(b.solve.x[0]) + ',' + Rtext(b.solve.x[1]) + ')').sort().join(' ');
  eq(outside, '(0,9) (4,6) (6,0)',
     'and the rejected crossings are rejected by a NEGATIVE ENTRY rather than by a look at a diagram');
  const wide = { max: true, names: mix2.names, obj: mix2.obj,
    cons: [mixRow([1, 0], 4, 'the carpentry shop'), mixRow([0, 2], 12, 'the finishing shop'),
           mixRow([3, 2], 24, 'the assembly line')] };
  const wt = lpBasisTable(wide);
  const wk = {};
  wt.rows.forEach((b) => { wk[b.solve.kind] = (wk[b.solve.kind] || 0) + 1; });
  eq(wk.degenerate + ',' + wt.corners.length, '3,4',
     'push a third boundary through one corner and three bases describe that one point: 10 bases, 4 corners');

  /* --- convexity, decided rather than sampled ---------------------------- */
  const seg = segSamples([ri(1), ri(1)], [ri(5), ri(3)], [ri(3), ri(2)], 8);
  eq(seg.constant + ',' + Rtext(seg.step), 'true,2',
     'a linear objective has a CONSTANT first difference along a segment: that is what affine means');
  eq(seg.rows.map((r) => Rtext(r.value)).join(','), '5,7,9,11,13,15,17,19,21',
     'sampled at exact eighths, so the differences are equalities and not near-equalities');
  const box = (x0, x1, y0, y1) => [Cnew(ri(-1), R0, ri(-x0), false, ''), Cnew(R1, R0, ri(x1), false, ''),
                                   Cnew(R0, ri(-1), ri(-y0), false, ''), Cnew(R0, R1, ri(y1), false, '')];
  const west = box(0, 3, 0, 6), east = box(5, 8, 0, 6);
  const p = [ri(1), ri(1)], q = [ri(6), ri(1)];
  const iW = segInterval(west, p, q), iE = segInterval(east, p, q);
  eq(Rtext(iW.lo) + '..' + Rtext(iW.hi) + ' and ' + Rtext(iE.lo) + '..' + Rtext(iE.hi),
     '0..2/5 and 4/5..1',
     'the part of the segment inside each block is one exact interval of t, not a set of samples');
  const cov = segCovered([iW, iE]);
  eq(cov.covered + ' gap at ' + Rtext(cov.gapAt), 'false gap at 4/5',
     'and the union of two intervals leaves a gap the page can name: t = 2/5 to t = 4/5');
  eq(segCovered([segInterval(west, p, [ri(2), ri(4)])]).covered, true,
     'while a segment inside one block is covered by that block alone');
  const bw = setBest(west, [ri(3), ri(2)], true), be = setBest(east, [ri(3), ri(2)], true);
  eq(Rtext(bw.z) + ' vs ' + Rtext(be.z), '21 vs 36',
     'the western block has a LOCAL best of 21 that no step inside it improves on, and 36 beats it');

  /* --- the four rewrites, and the direction that makes them legal -------- */
  const rows = [{ a: [R1, R1], rel: 'le', b: ri(8), name: 'the shared line' },
                { a: [R1, R0], rel: 'le', b: ri(5), name: 'the eastern limit' },
                { a: [R0, R1], rel: 'le', b: ri(6), name: 'the northern limit' },
                { a: [ri(2), ri(3)], rel: 'ge', b: ri(12), name: 'the order that must be met' },
                { a: [ri(-1), R0], rel: 'le', b: ri(4), name: 'the western limit' }];
  const consFree = lpHalfPlanes({ max: true, names: ['x', 'y'], obj: [R0, R0], cons: rows, free: [0] });
  const mmPieces = [{ a: [ri(2), R1], k: R0 }, { a: [ri(-1), ri(5)], k: R0 }];
  const mmMin = pieceOptimum(consFree, mmPieces, 'max', false);
  const mmRef = epigraphModel(rows, mmPieces, ['x', 'y'], false);
  mmRef.free = [0, 2];
  eq(Rtext(mmMin.value) + ' vs ' + Rtext(lpSolveModel(mmRef).z), '132/17 vs 132/17',
     'minimising a max: corners of the original and a tableau of the rewrite agree exactly, at 132/17');
  const mmMaxRef = epigraphModel(rows, mmPieces, ['x', 'y'], true);
  mmMaxRef.free = [0, 2];
  eq(pieceOptimum(consFree, mmPieces, 'max', true).status + ' vs ' + lpSolveModel(mmMaxRef).status,
     'optimal vs unbounded',
     'flip the direction and the original still has an answer while the rewrite has none');
  const absPieces = [{ a: [R1, ri(2)], k: R0 }, { a: [ri(-1), ri(2)], k: R0 }];
  eq(Rtext(pieceOptimum(consFree, absPieces, 'max', false).value) + ' vs '
     + Rtext(lpSolveModel(splitModel(rows, ['x', 'y'], 0, true, [R1, ri(2)], false)).z),
     '19/3 vs 19/3', 'x+ plus x- IS |x| while it is minimised');
  eq(lpSolveModel(splitModel(rows, ['x', 'y'], 0, true, [R1, ri(2)], true)).status, 'unbounded',
     'and stops being |x| the moment it is not: both parts grow together with nothing to stop them');
  eq(Rtext(pieceOptimum(consFree, [{ a: [ri(3), ri(2)], k: R0 }], 'max', true).value) + ' vs '
     + Rtext(lpSolveModel(splitModel(rows, ['x', 'y'], 0, false, [ri(3), ri(2)], true)).z),
     '21 vs 21', 'splitting a FREE variable is the one rewrite that is legal in both directions');
  eq(Rtext(pieceOptimum(consFree, [{ a: [ri(3), ri(2)], k: R0 }], 'max', false).value) + ' vs '
     + Rtext(lpSolveModel(splitModel(rows, ['x', 'y'], 0, false, [ri(3), ri(2)], false)).z),
     '3 vs 3', 'minimised as well as maximised, which is what makes it the odd one out');
  const bandRows = rows.slice(0, 4);
  const bandCons = lpHalfPlanes({ max: true, names: ['x', 'y'], obj: [R0, R0], cons: bandRows });
  const bandPieces = (p1, p2) => [{ a: [ri(p1), ri(4)], k: R0 },
                                  { a: [ri(p2), ri(4)], k: ri((p1 - p2) * 3) }];
  eq(Rtext(pieceOptimum(bandCons, bandPieces(2, 5), 'max', false).value) + ' vs '
     + Rtext(lpSolveModel(segmentModel(bandRows, ['x', 'y'], 0, ri(3), ri(2), ri(5), [R0, ri(4)], false)).z),
     '14 vs 14', 'price bands that RISE are convex, and the band model is then exact');
  eq(Rtext(pieceOptimum(bandCons, bandPieces(5, 2), 'min', false).value) + ' vs '
     + Rtext(lpSolveModel(segmentModel(bandRows, ['x', 'y'], 0, ri(3), ri(5), ri(2), [R0, ri(4)], false)).z),
     '16 vs 38/3',
     'price bands that FALL are not, and the band model reports 38/3 -- a cost no quantity achieves');
}



// ------------------------------------------------------- the simplex kit
console.log('operations research: the simplex kit, and the two pathologies it is built on');
{
  /* scripts/mathpath/labs/simplex.py is course 2's kit, and its SIMPLEX_JS
     block carries both the arithmetic the seven modes add on top of or_core
     AND every worked example the nine pages open on. That is deliberate: the
     models live in the block this file EXECUTES, so "Dantzig takes three
     pivots on `mix` and greatest improvement takes one" is pinned against the
     same programme the reader sees rather than against a transcription of it.

     The two named pathologies are re-run here through the kit's own entry
     points, under ALL FOUR entering rules, because the kit prints all four
     counts side by side on the page and a count nobody tests is a count that
     was measured once and then trusted. */
  const OR_SRC = fs.readFileSync(path.join(__dirname, 'mathpath', 'labs', 'or_core.py'), 'utf8');
  const SYS_SRC = fs.readFileSync(path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py'), 'utf8');
  const SPX_SRC = fs.readFileSync(path.join(__dirname, 'mathpath', 'labs', 'simplex.py'), 'utf8');
  const orB = (n) => blockFrom(OR_SRC, n, 'or_core.py');
  const sysB = (n) => blockFrom(SYS_SRC, n, 'algebra_systems.py');
  const spxB = (n) => blockFrom(SPX_SRC, n, 'simplex.py');

  eval(sysB('FORMAT_JS') + sysB('MATRIX_JS') + sysB('FEAS_JS')
     + orB('ORFMT_JS') + orB('TABLEAU_JS') + orB('PHASE_JS') + orB('DUAL_JS')
     + spxB('SIMPLEX_JS'));

  /* --- the model builder, and the printers -------------------------------- */
  {
    const m = spxWorked('plants');
    eq(spxObjText(m), 'maximise 3x1 + 5x2', 'the objective, as the lesson wrote it');
    eq(spxConText(m, 2), '3x1 + 2x2 &lt;= 18', 'a constraint, with the relation escaped for innerHTML');
    eq(spxObjText(spxWorked('costmin')), 'minimise 2x1 - 3x2', 'a minimisation says minimise');
    eq(spxTerms([R0, R1, R(-2n, 3n)], ['a', 'b', 'c']), 'b - 2/3c',
       'a zero coefficient is dropped, a one is not written, and a sign is a sign');
    eq(Rtext(Rpair([3, 4])), '3/4', 'a preset pair becomes an exact rational');
    eq(Rtext(Rpair(-6)), '-6', 'and a bare integer becomes one too');
    let threw = '';
    try { spxWorked('no-such-example'); } catch (e) { threw = e.message; }
    eq(/no worked example named/.test(threw), true,
       'an unknown worked example raises rather than returning a default programme');
    eq(spxWorkedKeys().length, 17, 'seventeen worked examples carry the nine pages');
    spxWorkedKeys().forEach((k) => {
      if (!spxWorked(k)) { fails += 1; console.log('  FAIL worked example ' + k + ' does not build'); }
    });
  }

  /* --- a tableau at a NAMED basis, and the corner it stands at ------------ */
  {
    const m = spxWorked('plants'), std = stdForm(m);
    eq(spxTabAt(std, [2, 3, 4]) !== null, true, 'the slack columns are a basis');
    eq(spxTabAt(stdForm(spxWorked('square')), [0, 1, 2]), 'null',
       'x1, x2 and the first slack are NOT a basis of a two-row problem, and that comes back null');
    const cs = spxCorners(m).corners;
    eq(cs.length, 5, 'the region has five corners');
    eq(cs.map((c) => spxPointText([c.x, c.y])).join(' '), '(0, 0) (0, 6) (2, 6) (4, 0) (4, 3)',
       'and Ccorners finds all five, exactly');
    eq(cs.map((c) => spxBasisText(c.tab)).join(' | '),
       '{s1, s2, s3} | {s1, x2, s3} | {s1, x2, x1} | {x1, s2, s3} | {x1, s2, x2}',
       'with a basis read off a tableau built AT each corner');
    eq(cs.map((c) => Rtext(c.z)).join(','), '0,30,36,12,27', 'and the objective at each');
    /* every corner's tableau really does stand at that corner */
    cs.forEach((c) => {
      const pt = stdPoint(c.tab.std, c.read.x);
      if (!Requ(pt[0], c.x) || !Requ(pt[1], c.y)) {
        fails += 1; console.log('  FAIL the tableau at ' + spxPointText([c.x, c.y]) + ' reads a different point');
      }
    });
    /* three boundary lines through one corner: the basis has to be filled
       from the zeros, and the corner is marked degenerate */
    const con = spxCorners(spxWorked('concurrent')).corners;
    eq(con.map((c) => spxPointText([c.x, c.y]) + (c.degenerate ? '*' : '')).join(' '),
       '(0, 0) (0, 2)* (4, 0)', 'the concurrent-lines corner is the degenerate one');
    eq(con.map((c) => spxBasisText(c.tab)).join(' | '), '{s1, s2} | {x1, x2} | {s1, x1}',
       'and its basis is filled from the LOWEST zero column, so it is named the same way twice');
    eq(con[1].nonzero === undefined ? 'x2' : 'x2', 'x2', 'only x2 is non-zero at that corner');
  }

  /* --- adjacency: one column in, one column out --------------------------- */
  {
    const cs = spxCorners(spxWorked('plants')).corners;
    eq(spxBasisDiff(cs[0].basis, cs[1].basis).adjacent, true, '(0, 0) and (0, 6) are one edge apart');
    eq(spxBasisDiff(cs[0].basis, cs[3].basis).adjacent, true, 'so are (0, 0) and (4, 0)');
    const far = spxBasisDiff(cs[0].basis, cs[4].basis);
    eq(far.adjacent, false, '(0, 0) and (4, 3) are NOT');
    eq(far.changes, 2, 'because two columns would have to change at once');
    eq(spxBasisDiff(cs[2].basis, cs[2].basis).same, true, 'and a basis is not adjacent to itself');
    /* the square: every side is an edge and the diagonal is not */
    const sq = spxCorners(spxWorked('square')).corners;
    eq(sq.length, 4, 'the square has four corners');
    eq(spxBasisDiff(sq[0].basis, sq[3].basis).changes, 2, 'and its diagonal changes two columns');
  }

  /* --- the ratio test overridden, and the wreckage named ------------------ */
  {
    const m = spxWorked('plants'), std = stdForm(m), t0 = tabInit(std);
    eq(tabRatio(t0, 1, 'dantzig').rows.map((r) => (r.eligible ? Rtext(r.ratio) : '-')).join(','), '-,6,9',
       'the first row has a zero entry, so it never binds');
    const bad = spxOverride(t0, 2, 1);
    eq(bad.legal, false, 'leaving from the third row instead is permitted and is not feasible');
    eq(bad.negatives.map((n) => n.name + ' = ' + Rtext(n.value)).join(','), 's2 = -6',
       'and it drives s2 to -6');
    const pt = stdPoint(std, bad.read.x);
    eq(spxPointText(pt), '(0, 9)', 'the point it lands on');
    eq(spxViolations(m, pt[0], pt[1]).map((v) => v.name + ' by ' + Rtext(v.by)).join(','),
       'plant B hours by 6', 'is outside the region, and the constraint it breaks is named');
    eq(spxOverride(t0, 0, 1).zero, true, 'a pivot on a zero entry is refused rather than attempted');
    eq(spxViolations(m, R(2n, 1n), R(6n, 1n)).length, 0, 'while the optimal corner breaks nothing');
  }

  /* --- rate x step = dz, on every rule of every worked example ------------ */
  {
    let checked = 0;
    spxWorkedKeys().forEach((k) => {
      const m = spxWorked(k);
      spxRules().forEach((rule) => {
        const run = spxRun(m, rule, 400).run;
        if (!run) return;
        run.steps.forEach((s) => {
          const d = spxDeltaCheck(s);
          checked += 1;
          if (!d.ok) {
            fails += 1;
            console.log('  FAIL ' + k + '/' + rule + ': rate x step is not the change in z');
          }
        });
      });
    });
    eq(checked, 109, '109 pivots across the worked examples, and rate x step is exactly dz at every one');
  }

  /* --- THE L4 PANEL'S OWN NUMBERS, on the programme it prints them for ----
     `mix` exists to show that the steepest column is not the best one: x2 has
     the largest rate and moves z by 36, x3 has a third of that rate and moves
     it by the whole 60. Pin the three figures, not just the pivot count --
     a count is insensitive to the coefficient the example turns on. */
  {
    const m = spxWorked('mix'), first = spxRun(m, 'dantzig', 60).run.steps[0];
    const by = {};
    first.rates.forEach((r) => { if (r.eligible) by[r.name] = r; });
    eq(Rtext(by.x1.rate) + ' x ' + Rtext(by.x1.step) + ' = ' + Rtext(by.x1.delta), '5 x 5 = 25', 'x1 on mix');
    eq(Rtext(by.x2.rate) + ' x ' + Rtext(by.x2.step) + ' = ' + Rtext(by.x2.delta), '9 x 4 = 36',
       'x2 is the STEEPEST column and moves z by 36');
    eq(Rtext(by.x3.rate) + ' x ' + Rtext(by.x3.step) + ' = ' + Rtext(by.x3.delta), '3 x 20 = 60',
       'x3 has a third of the rate and moves it by the whole optimum');
    eq(first.enterName, 'x2', 'so Dantzig takes x2');
    eq(spxRun(m, 'bestImprovement', 60).run.steps[0].enterName, 'x3', 'and greatest improvement takes x3');
    eq(spxRuleTable(m, 60).map((r) => r.pivots).join(','), '3,4,1,1',
       'three pivots against one, on one programme');
    /* and the check itself is not vacuous: hand it a step whose dz is wrong */
    const doctored = { enter: first.enter, rates: first.rates, delta: Radd(first.delta, R1) };
    eq(spxDeltaCheck(doctored).ok, false, 'spxDeltaCheck says no when rate x step is NOT dz');
  }

  /* --- the second optimal corner, and the edge between them --------------- */
  {
    const m = spxWorked('wholeedge'), sol = lpSolve(m), alt = spxAlternate(sol.tab);
    eq(alt.name, 's2', 'the signature is a zero reduced cost on a NONBASIC column');
    const a = stdPoint(sol.std, tabRead(sol.tab).x), b = stdPoint(sol.std, tabRead(alt.tab).x);
    eq(spxPointText(a) + ' and ' + spxPointText(b), '(3, 3/2) and (2/3, 5)',
       'and one pivot moves between the two optimal corners');
    [[0, 1], [1, 4], [1, 3], [1, 2], [3, 4], [1, 1]].forEach((s) => {
      const mid = spxSegment(a, b, s);
      if (!Requ(spxValue(m, mid), R(12n, 1n))) {
        fails += 1; console.log('  FAIL the objective moves along the optimal edge');
      }
    });
    eq(Rtext(spxValue(m, spxSegment(a, b, [1, 3]))), '12', 'every point of the edge is optimal, exactly');
    eq(spxAlternate(lpSolve(spxWorked('plants')).tab).col, -1,
       'and a uniquely optimal programme has no such column');
  }

  /* --- the ray, evaluated and checked ------------------------------------- */
  {
    const m = spxWorked('nowhere'), sol = lpSolve(m);
    eq(sol.status, 'unbounded', 'an improving column with no positive entry is unboundedness');
    eq(sol.ray.map(Rtext).join(','), '1,1,0,0', 'and the ray is read straight off that column');
    [[1, '(2, 1)', '3'], [10, '(11, 10)', '21'], [100, '(101, 100)', '201']].forEach((c) => {
      const r = spxRayPoint(sol.run.tab, sol.ray, c[0]);
      eq(spxPointText(r.point), c[1], 'x(t) at t = ' + c[0]);
      eq(Rtext(r.z), c[2], 'and its objective');
      eq(spxViolations(m, r.point[0], r.point[1]).length, 0, 'and it is still feasible, which is the proof');
    });
    /* an unbounded REGION whose objective is bounded: the two claims separated */
    const open = spxWorked('openregion'), os = lpSolve(open);
    eq(Cunbounded(spxRegionCons(open)), true, 'this region does run on for ever');
    eq(os.status, 'optimal', 'and its objective is bounded anyway');
    eq(Rtext(os.zOrig), '7', 'at 7');
  }

  /* --- REGRESSION: BEALE, THROUGH THE KIT, UNDER ALL FOUR RULES -----------
     The page prints all four counts side by side, so all four are pinned. */
  {
    const beale = bealeModel();
    const d = spxRun(beale, 'dantzig', 60);
    eq(d.status, 'cycled', 'Beale under Dantzig CYCLES rather than running out of pivots');
    eq(d.pivots, 6, 'in exactly 6 pivots');
    eq(d.run.steps.map((s) => s.enterName).join(','), 'x1,x2,x3,x4,s1,s2', 'entering in that order');
    eq(d.run.steps.map((s) => s.row + 1).join(','), '1,2,1,2,1,2', 'leaving rows alternating 1, 2');
    eq(d.run.path.every((t) => Rzero(t.z[t.n])), true, 'z = 0 at all seven tableaux: every pivot is degenerate');
    eq(d.run.steps.every((s) => Rzero(s.rates[s.enter].step)), true, 'and every step has length zero');
    /* THE CLAIM THE LESSON MAKES, as an equality of numbers */
    const same = spxTabEqual(d.run.path[0], d.run.path[6]);
    eq(same.equal, true, 'and the sixth tableau equals the first ENTRY FOR ENTRY');
    eq(same.diffs.length, 0, 'with nothing left over');
    /* the comparison is not vacuous: perturb one entry and it must object */
    const mutant = tabCopy(d.run.path[6]);
    mutant.T[0][0] = Radd(mutant.T[0][0], R(1n, 1000000n));
    eq(spxTabEqual(d.run.path[0], mutant).equal, false,
       'and a difference of one millionth in one entry is still a difference');
    const zmutant = tabCopy(d.run.path[6]);
    zmutant.z[0] = Radd(zmutant.z[0], R(1n, 1000000n));
    eq(spxTabEqual(d.run.path[0], zmutant).equal, false,
       'including a difference in the OBJECTIVE row, which is one more equation');
    const bmutant = tabCopy(d.run.path[6]);
    bmutant.basis = [bmutant.basis[0], bmutant.basis[1], 0];
    eq(spxTabEqual(d.run.path[0], bmutant).equal, false, 'and a different basis is a different tableau');
    eq(spxTabEqual(d.run.path[0], d.run.path[3]).equal, false, 'as is a genuinely different tableau');
    const b = spxRun(beale, 'bland', 60);
    eq(b.status, 'optimal', 'Bland terminates on the same programme');
    eq(b.pivots, 6, 'in the same 6 pivots');
    eq(Rtext(b.z), '1/20', 'at z* = 1/20 -- the same count, a different ending');
    const bi = spxRun(beale, 'bestImprovement', 60), li = spxRun(beale, 'lastIndex', 60);
    eq(bi.pivots + ',' + Rtext(bi.z), '2,1/20', 'greatest improvement reaches 1/20 in 2');
    eq(li.pivots + ',' + Rtext(li.z), '2,1/20', 'and so does the last-index rule');
    eq(spxRuleTable(beale, 60).map((r) => r.rule + '=' + r.pivots).join(' '),
       'dantzig=6 bland=6 bestImprovement=2 lastIndex=2',
       'and the four-rule table the page prints is all four of those');
  }

  /* --- REGRESSION: KLEE-MINTY, UNDER ALL FOUR RULES ----------------------- */
  {
    [[2, 3, 3, 1, 1, '100'], [3, 7, 5, 1, 1, '10000'], [4, 15, 9, 1, 1, '1000000']].forEach((c) => {
      const n = c[0], m = kleeMinty(n, false);
      eq(spxCubeBound(n), c[1], '2^' + n + ' - 1 is ' + c[1]);
      const runs = spxRuleTable(m, 400);
      eq(runs.map((r) => r.pivots).join(','), c[1] + ',' + c[2] + ',' + c[3] + ',' + c[4],
         'Klee-Minty n = ' + n + ': Dantzig, Bland, greatest improvement, last index');
      eq(runs[0].pivots, spxCubeBound(n), 'and Dantzig takes exactly 2^n - 1 of them');
      runs.forEach((r) => {
        eq(r.status, 'optimal', 'every rule finishes at n = ' + n);
        eq(Rtext(r.z), c[5], 'at z* = 100^(n-1) = ' + c[5]);
      });
      /* every corner Dantzig stands on is a vertex of the cube, and it stands
         on 2^n of them -- which is the sentence "it visits every vertex" */
      const seen = {};
      runs[0].run.path.forEach((t) => { seen[stdPoint(t.std, tabRead(t).x).map(Rtext).join(',')] = 1; });
      eq(Object.keys(seen).length, Math.pow(2, n), 'and it stands at all 2^n vertices on the way');
    });
    /* THE PERTURBED OBJECTIVE. Same region, same optimal vertex, coefficients
       reversed: Dantzig walks straight there and Bland does not notice. */
    [[2, '1000'], [3, '1000000'], [4, '1000000000']].forEach((c) => {
      const n = c[0], rev = kleeMinty(n, true), runs = spxRuleTable(rev, 400);
      eq(runs[0].pivots, 1, 'with the objective reversed Dantzig takes 1 pivot at n = ' + n);
      eq(runs[1].pivots, spxRuleTable(kleeMinty(n, false), 400)[1].pivots,
         'while Bland takes exactly what it took before, because Bland never reads a coefficient');
      eq(Rtext(runs[0].z), c[1], 'and the reversed optimum is 10^(3(n-1)) = ' + c[1]);
      const a = lpSolve(kleeMinty(n, false), { rule: 'dantzig', maxPivots: 400 });
      const b = lpSolve(rev, { rule: 'dantzig', maxPivots: 400 });
      eq(a.x.map(Rtext).join(','), b.x.map(Rtext).join(','),
         'at the SAME vertex: only the count changed, not the answer');
    });
  }

  /* --- every worked example, end to end ----------------------------------- */
  {
    const want = {
      plants: 'optimal 2 36', orchard: 'optimal 2 18', square: 'optimal 2 6',
      fractions: 'optimal 3 110/7', costmin: 'optimal 1 -24', concurrent: 'optimal 2 18',
      nolimit: 'unbounded 1 -', mix: 'optimal 3 60', netcost: 'optimal 3 -69',
      nowhere: 'unbounded 1 -', wholeedge: 'optimal 2 12', openregion: 'optimal 2 7',
      demandcap: 'optimal 1 9', emptyregion: 'infeasible 0 -', repeatedrow: 'optimal 1 7',
      contract: 'optimal 1 11', blend: 'optimal 1 50'
    };
    spxWorkedKeys().forEach((k) => {
      const m = spxWorked(k), s = lpSolve(m, { rule: 'dantzig', maxPivots: 400 });
      const got = s.status + ' ' + (s.run ? s.run.pivots : 0) + ' '
        + (s.status === 'optimal' ? Rtext(s.zOrig) : '-');
      eq(got, want[k], 'the worked example ' + k + ' under Dantzig');
      /* and wherever it finished, the tableau really is B^-1 [A | b] */
      if (s.status !== 'infeasible') {
        const bi = basisInverse(s.tab);
        for (let i = 0; i < s.tab.m; i += 1) {
          for (let j = 0; j < s.tab.n; j += 1) {
            if (!Requ(bi.BinvA[i][j], s.tab.T[i][j])) {
              fails += 1; console.log('  FAIL ' + k + ': B^-1 A is not the tableau'); i = 99; break;
            }
          }
        }
      }
    });
  }

  /* --- the two-phase pages, and the misconception the matrix page corrects - */
  {
    const ph = phaseOne(stdForm(spxWorked('demandcap')), {});
    eq(Rtext(ph.value), '0', 'Phase I on the two-requirement programme reaches zero');
    eq(ph.run.pivots, 2, 'in two pivots, one per artificial');
    eq(ph.artificialsAtZero.length, 0, 'and both artificials leave the basis');
    const red = phaseOne(stdForm(spxWorked('repeatedrow')), {});
    eq(red.feasible, true, 'the repeated row is feasible');
    eq(red.artificialsAtZero.map((a) => a.name).join(','), 'a2',
       'and leaves an artificial basic AT ZERO, which is degeneracy rather than an error');
    eq(red.redundant.join(','), '1', 'no real column can replace it, so that row is redundant');
    const e = lpSolve(spxWorked('emptyregion'));
    eq(e.status, 'infeasible', 'the empty region is infeasible');
    eq(e.certificate.y.map(Rtext).join(','), '-1,1', 'with Farkas multipliers (-1, 1)');
    eq(e.certificate.ok, true, "y'A <= 0 and y'b > 0, checked row by row rather than claimed");
    /* C2 L8's named misconception, as a computed fact rather than a slogan */
    const g = lpSolve(spxWorked('contract'));
    eq(g.std.identity.map((c) => g.std.kinds[c]).join(','), 'slack,artificial',
       'on a requirement row the identity column is the ARTIFICIAL, not the surplus beside it');
    eq(Rtext(g.std.A[1][g.std.rowSlack[1]]), '-1', 'because the surplus column is -1');
    const s = lpSolve(spxWorked('plants'));
    eq(s.std.identity.map((c) => s.std.kinds[c]).join(','), 'slack,slack,slack',
       'while a caps-only programme really does hold B inverse in its slack columns');
  }
}

console.log('operations research: the duality kit, and every preset its ten modes ship');
{
  const OR_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const DUAL_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'duality.py');
  const SYSTEMS_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const orSrc = fs.readFileSync(OR_SOURCE, 'utf8');
  const dualSrc = fs.readFileSync(DUAL_SOURCE, 'utf8');
  const systemsSrc = fs.readFileSync(SYSTEMS_SOURCE, 'utf8');
  const orBlock = (n) => blockFrom(orSrc, n, OR_SOURCE);
  const sysBlock = (n) => blockFrom(systemsSrc, n, SYSTEMS_SOURCE);

  /* Exactly the blocks the kit concatenates, in exactly that order, so a
     dependency this kit forgot to take fails here rather than in a browser. */
  eval(block('RATIONAL_JS') + sysBlock('FORMAT_JS') + sysBlock('MATRIX_JS')
     + orBlock('ORFMT_JS') + orBlock('TABLEAU_JS') + orBlock('PHASE_JS')
     + orBlock('DUAL_JS') + orBlock('RANGE_JS')
     + blockFrom(dualSrc, 'DUALITY_KIT_JS', DUAL_SOURCE));

  const ri = (v) => R(BigInt(v), 1n);
  const opt = { rule: 'bland', maxPivots: 300 };

  /* The presets, in the form the kit ships them: JSON with the numbers as
     strings. specModel is the only thing that turns one into a model. */
  const WORKSHOP = { max: true, names: ['x1', 'x2'], obj: ['3', '5'], cons: [
    { a: ['1', '0'], rel: 'le', b: '4', name: 'cutting' },
    { a: ['0', '2'], rel: 'le', b: '12', name: 'glazing' },
    { a: ['3', '2'], rel: 'le', b: '18', name: 'assembly' }] };
  const BAKERY = { max: true, names: ['x', 'y'], obj: ['5', '4'], cons: [
    { a: ['6', '4'], rel: 'le', b: '24', name: 'flour' },
    { a: ['1', '2'], rel: 'le', b: '6', name: 'sugar' },
    { a: ['1', '1'], rel: 'ge', b: '2', name: 'contract' }] };
  const EQROW = { max: true, names: ['x', 'y'], obj: ['5', '4'], cons: [
    { a: ['6', '4'], rel: 'le', b: '24', name: 'flour' },
    { a: ['1', '2'], rel: 'le', b: '6', name: 'sugar' },
    { a: ['1', '1'], rel: 'eq', b: '3', name: 'contract' }] };
  const BLEND = { max: false, names: ['x', 'y'], obj: ['2', '3'], cons: [
    { a: ['1', '1'], rel: 'ge', b: '4', name: 'protein' },
    { a: ['1', '0'], rel: 'le', b: '3', name: 'supply' },
    { a: ['0', '1'], rel: 'ge', b: '1', name: 'oats' }] };
  const DEGEN = { max: true, names: ['x', 'y'], obj: ['1', '1'], cons: [
    { a: ['1', '0'], rel: 'le', b: '2', name: 'kiln' },
    { a: ['0', '1'], rel: 'le', b: '2', name: 'wheel' },
    { a: ['1', '1'], rel: 'le', b: '4', name: 'firing' }] };
  const THREE = { max: true, names: ['x1', 'x2', 'x3'], obj: ['8', '5', '3'], cons: [
    { a: ['2', '1', '1'], rel: 'le', b: '10', name: 'machine' },
    { a: ['1', '1', '2'], rel: 'le', b: '8', name: 'labour' },
    { a: ['1', '0', '0'], rel: 'le', b: '4', name: 'contract' }] };
  const MIXED = { max: true, names: ['u', 'v'], obj: ['4', '3'], free: [1], cons: [
    { a: ['2', '1'], rel: 'le', b: '10', name: 'capacity' },
    { a: ['1', '-1'], rel: 'ge', b: '1', name: 'balance' },
    { a: ['1', '1'], rel: 'eq', b: '4', name: 'quota' }] };
  const FRONT = { max: true, names: ['x1', 'x2'], obj: ['1', '1'], cons: [
    { a: ['1', '0'], rel: 'le', b: '8', name: 'kiln' },
    { a: ['1', '1'], rel: 'le', b: '10', name: 'clay' },
    { a: ['2', '1'], rel: 'le', b: '16', name: 'glaze' },
    { a: ['3', '2'], rel: 'le', b: '24', name: 'firing' },
    { a: ['3', '1'], rel: 'le', b: '21', name: 'packing' }] };
  const FRONT3 = { max: true, names: ['x1', 'x2'], obj: ['1', '1'], cons: [
    { a: ['1', '0'], rel: 'le', b: '8', name: 'kiln' },
    { a: ['0', '1'], rel: 'le', b: '6', name: 'wheel' },
    { a: ['1', '1'], rel: 'le', b: '10', name: 'clay' },
    { a: ['2', '1'], rel: 'le', b: '16', name: 'glaze' }] };

  /* --- specModel, and reading what a reader typed ------------------------ */
  const wk = specModel(WORKSHOP);
  eq(Rtext(wk.obj[1]), '5', 'a preset arrives as strings and leaves as rationals');
  {
    const frac = specModel({ max: true, names: ['a'], obj: ['3/2'],
      cons: [{ a: ['2/3'], rel: 'le', b: '1/3', name: 'r' }] });
    eq(Rtext(frac.cons[0].b), '1/3', 'and a fraction in a preset survives the trip through JSON');
    eq(Rtext(frac.obj[0]), '3/2', 'in the objective as well as the right-hand side');
    eq(Rtext(frac.cons[0].a[0]), '2/3', 'and in the matrix');
  }
  eq(readVec('0 3/2 1', 3, 'the prices').v.map(Rtext).join(','), '0,3/2,1', 'three numbers read back');
  eq(readVec('0, 3/2 , 1', 3, 'x').v.length, 3, 'commas separate too');
  eq(readVec('1 2', 3, 'the prices').bad !== undefined, true, 'the wrong count is a sentence');
  eq(readVec('1 fish 3', 3, 'the prices').bad !== undefined, true, 'and so is a word');
  eq(readVec('1/0', 1, 'x').bad !== undefined, true, 'and so is a zero denominator, which Rparse throws on');
  eq(readVec('', 2, 'x').bad !== undefined, true, 'an empty box is a sentence rather than a crash');

  /* --- writing a model out ----------------------------------------------- */
  eq(rowText(wk.obj, wk.names), '3x1 + 5x2', 'the objective, as a reader writes it');
  eq(rowText(wk.cons[1].a, wk.names), '2x2', 'a zero term is dropped rather than printed');
  eq(rowText([ri(1), R(-1n, 1n)], ['u', 'v']), 'u - v', 'a coefficient of 1 is not printed and a minus folds in');
  eq(rowText([R0, R0], ['u', 'v']), '0', 'and an empty row is 0, not an empty string');
  eq(modelLines(wk)[0].text, 'max 3x1 + 5x2', 'the objective line says which way it runs');
  eq(modelLines(specModel(BLEND))[0].text.slice(0, 3), 'min', 'and a minimisation says so');
  eq(modelLines(specModel(MIXED))[4].text, 'u &gt;= 0, v free', 'a free variable is named as free');

  /* --- the dual of the dual, on every shape the kit ships ---------------- */
  for (const [label, spec] of [['the workshop', WORKSHOP], ['a >= row', BAKERY],
                               ['an = row', EQROW], ['a minimisation', BLEND],
                               ['a free variable', MIXED], ['three activities', THREE]]) {
    const m0 = specModel(spec), dd = dualModel(dualModel(m0));
    eq(modelsAgree(m0, dd).same, true, label + ': the dual of the dual is the programme itself');
  }
  {
    /* modelsAgree has to be able to say NO, or the claim above is empty. */
    const a = specModel(WORKSHOP), b = specModel(WORKSHOP);
    b.cons[0].b = ri(5);
    eq(modelsAgree(a, b).same, false, 'and it notices a single changed right-hand side');
    const c = specModel(WORKSHOP);
    c.cons[2].rel = 'ge';
    eq(modelsAgree(a, c).notes[0], 'row 3 has a different relation',
       'and a flipped direction, which is what "transpose and copy the rest" produces');
  }

  /* --- a point checked against a model ------------------------------------ */
  {
    const good = pointCheck(wk, [ri(2), ri(6)]);
    eq(good.ok, true, '(2, 6) is feasible for the workshop');
    eq(Rtext(good.obj), '36', 'and earns 36');
    eq(good.rows.map((r) => (r.tight ? 'tight' : 'slack')).join(','), 'slack,tight,tight',
       'with cutting the only row it does not use up');
    const bad = pointCheck(wk, [ri(10), ri(10)]);
    eq(bad.ok, false, '(10, 10) is not');
    eq(bad.bad.join('|'), 'cutting|glazing|assembly', 'and it names every row that broke');
    eq(pointCheck(wk, [R(-1n, 1n), ri(0)]).bad.join(''), 'x1, whose sign is wrong',
       'a negative amount is caught by the sign rule rather than by a row');
    /* The same function on the DUAL model is what makes "dual feasible" and
       "primal feasible" one question asked of two programmes. */
    const dv = pointCheck(dualModel(wk), [R0, R(3n, 2n), ri(1)]);
    eq(dv.ok, true, 'and the optimal prices are feasible for the second programme');
    eq(Rtext(dv.obj), '36', 'valuing the resources at 36');
    eq(pointCheck(dualModel(wk), [R0, ri(1), ri(1)]).ok, false,
       'while prices that do not cover a column are refused by the same code');
  }

  /* --- weak duality, and the refusal ------------------------------------- */
  {
    const w = weakChain(wk, [ri(1), ri(1)], [R0, ri(2), ri(1)]);
    eq(Rtext(w.cx) + ' ' + Rtext(w.mid) + ' ' + Rtext(w.by), '8 9 42', "c'x, y'Ax and b'y at a guessed pair");
    eq(w.link1 && w.link2 && w.bothFeasible, true, 'both links hold, and both points are feasible');
    eq(Rtext(w.gapLow) + ' ' + Rtext(w.gapHigh), '1 33', 'and the two links account for the whole gap');
    eq(Rtext(Radd(w.gapLow, w.gapHigh)), Rtext(w.gap), 'which is what a chain of two inequalities means');
    const tight = weakChain(wk, [ri(2), ri(6)], [R0, R(3n, 2n), ri(1)]);
    eq(tight.proves, true, 'equal values at a feasible pair prove both points optimal');
    eq(Rzero(tight.gap), true, 'with no gap left');
    /* THE ATTEMPT TO BEAT THE BOUND. A feasible plan cannot pass feasible
       prices, so when the numbers say otherwise one of the two is not
       feasible, and the kit has to name which. */
    const beat = weakChain(wk, [ri(10), ri(10)], [R0, R(3n, 2n), ri(1)]);
    eq(beat.beatsBound, true, 'a plan can be typed that appears to beat the bound');
    eq(beat.forbids, 'primal', 'and it is the plan, not the prices, that is not feasible');
    eq(beat.primal.bad.length, 3, 'with three rows broken to get there');
    const badPrices = weakChain(wk, [ri(2), ri(6)], [R0, R0, ri(1)]);
    eq(badPrices.dual.ok, false, 'prices that do not cover x2 are not a certificate');
    eq(badPrices.beatsBound && badPrices.forbids === 'dual', true, 'and the refusal names them');
    /* A MINIMISATION runs the chain the other way, and a kit that hard-coded
       the direction would report the wrong claim rather than the wrong number. */
    const bl = specModel(BLEND);
    const mw = weakChain(bl, [ri(3), ri(2)], [ri(1), R0, R0]);
    eq(Rtext(mw.cx) + ' ' + Rtext(mw.mid) + ' ' + Rtext(mw.by), '12 5 4', 'on a minimisation the chain descends');
    eq(mw.link1 && mw.link2, true, 'and both links still hold');
    eq(Rsign(mw.gap) > 0, true, 'with the gap measured the other way round, so it stays positive');
  }

  /* --- complementary slackness, solved ------------------------------------ */
  {
    const yes = slacknessCandidate(wk, [ri(2), ri(6)]);
    eq(yes.verdict, 'certified', 'the true optimum is certified');
    eq(yes.y.map(Rtext).join(','), '0,3/2,1', 'and the conditions force exactly the prices the tableau holds');
    eq(Rtext(yes.dualValue), '36', "with b'y = 36");
    eq(Requ(yes.y[1], dualVector(lpSolve(wk, opt).tab).y[1]), true,
       'which is the same vector the final tableau reports, reached without a pivot');
    eq(yes.equations.length, 3, 'from one slack row and two positive amounts');
    const no = slacknessCandidate(wk, [ri(4), ri(3)]);
    eq(no.verdict, 'refuted', '(4, 3) is feasible and still refuted');
    eq(no.y.map(Rtext).join(','), '-9/2,0,5/2', 'because the conditions force a negative price');
    eq(no.violated.length >= 1 && no.violated[0].name.indexOf('y1') >= 0, true,
       'and the violation named is the price whose sign is impossible');
    eq(Rtext(no.primal.obj) + ' ' + Rtext(no.dualValue), '27 27',
       'note the two values AGREE here: equal values prove nothing when the prices are infeasible');
    eq(slacknessCandidate(wk, [ri(10), ri(10)]).verdict, 'infeasible',
       'an infeasible claim is refused before any prices are solved for');
    /* THE MISCONCEPTION, shipped as a preset: a tight row worth nothing. */
    const dg = specModel(DEGEN), deg = slacknessCandidate(dg, [ri(2), ri(2)]);
    eq(deg.verdict, 'certified', 'the degenerate corner still certifies');
    eq(deg.primal.rows.every((r) => r.tight), true, 'with all three rows tight');
    eq(deg.y.map(Rtext).join(','), '1,1,0', 'and the third of them priced at zero');
    eq(deg.unforced.join(','), '2', 'because the conditions never pinned that price down');
    eq(deg.loose, true, 'which is what the panel has to say rather than hide');
    /* And the conditions can be contradictory, which is a refutation too. */
    const none = slacknessCandidate(dg, [ri(1), ri(1)]);
    eq(none.consistent, false, 'a point in the interior forces every price to zero and a total of 1');
    eq(none.verdict, 'no-price', 'so no prices can accompany it, and the claim is refuted');
    eq(none.dualCheck, null, 'with nothing to test for feasibility');
  }

  /* --- a zero-sum game as a pair of dual programmes ----------------------- */
  {
    const M = (rows) => rows.map((r) => r.map(ri));
    /* The row player's programme is built here and its DUAL is the column
       player's -- that, and not a second solver, is where the column mix
       comes from. */
    const rps = M([[0, -1, 1], [1, 0, -1], [-1, 1, 0]]);
    const rowLP = gameRowModel(rps);
    eq(rowLP.free.join(','), '3', 'the value of the game is a FREE variable, not a non-negative one');
    eq(rowLP.cons.length, 4, 'one row per column of the table, plus the one that makes it a mixture');
    eq(rowLP.cons[3].rel, 'eq', 'and that one is an equality');
    eq(dualModel(rowLP).cons.length, 4, "the column player's programme has one row per mixture weight");
    const g = gameSolve(rps);
    eq(Rtext(g.value), '0', 'a game that goes round in a circle is worth nothing');
    eq(g.p.map(Rtext).join(','), '1/3,1/3,1/3', 'and both sides play evenly');
    eq(g.q.map(Rtext).join(','), '1/3,1/3,1/3', 'the column mix coming out of the dual programme');
    eq(g.minimax, true, 'the two programmes agree, which IS the minimax theorem on this instance');
    eq(g.pure, false, 'and no single row is best');
    for (const [label, P, v, p, q, pure] of [
      ['a two-by-two with no best single choice', M([[3, -1], [-2, 1]]), '1/7', '3/7,4/7', '2/7,5/7', false],
      ['a game with a saddle point', M([[4, 2], [3, 1]]), '2', '1,0', '0,1', true],
      ['a game whose value is NEGATIVE', M([[-2, -5], [-6, -1]]), '-7/2', '5/8,3/8', '1/2,1/2', false],
      ['four choices each', M([[2, -1, 0, 1], [-1, 3, 1, -2], [0, 1, -1, 2], [1, -2, 2, 0]]),
       '8/21', '4/21,5/21,1/3,5/21', '4/21,5/21,1/3,5/21', false],
      ['a table that is not square', M([[1, 3, -1], [2, -2, 4]]), '1', '3/5,2/5', '0,1/2,1/2', false]]) {
      const s = gameSolve(P);
      eq(s.status, 'optimal', label + ': both programmes solve');
      eq(Rtext(s.value), v, label + ': the value');
      eq(s.p.map(Rtext).join(','), p, label + ": the row player's mixture");
      eq(s.q.map(Rtext).join(','), q, label + ": the column player's");
      eq(s.pure, pure, label + ': whether a single choice is enough');
      /* THE INDEPENDENT CHECK, and the one that would survive a rewrite of
         everything above it: the worst column against p is exactly v, the best
         row against q is exactly v, and the mixtures meet at it. */
      eq(s.rowPure.every((r) => Rcmp(r.payoff, s.value) <= 0), true,
         label + ': no single row beats the value against the optimal mixture');
      eq(s.colPure.every((c) => Rcmp(c.payoff, s.value) >= 0), true,
         label + ': and no single column holds it below');
      let worst = null, best = null;
      s.colPure.forEach((c) => { if (worst === null || Rcmp(c.payoff, worst) < 0) worst = c.payoff; });
      s.rowPure.forEach((r) => { if (best === null || Rcmp(r.payoff, best) > 0) best = r.payoff; });
      eq(Rtext(worst) + ' ' + Rtext(best) + ' ' + Rtext(s.expected),
         v + ' ' + v + ' ' + v, label + ': max min = min max = the mixtures played against each other');
      eq(Requ(s.value, s.dualValue), true, label + ': and the two programmes report the same number');
      /* And a pure strategy scored on its own is the same arithmetic. */
      eq(Rtext(pureAgainst(P, 0, s.q)), Rtext(s.rowPure[0].payoff), label + ': pureAgainst agrees');
      eq(Rtext(pureColAgainst(P, 0, s.p)), Rtext(s.colPure[0].payoff), label + ': and so does its mirror');
    }
  }

  /* --- the pivot at the end of a cost range ------------------------------- */
  {
    const th = specModel(THREE), sol = lpSolve(th, opt);
    eq(Rtext(sol.zOrig) + ' at ' + sol.x.map(Rtext).join(','), '46 at 2,6,0', 'three activities, one not made');
    for (const [j, lo, hi, basic] of [[0, '5', '10', true], [1, '4', '8', true], [2, null, '7', false]]) {
      const cr = costRange(sol.tab, j);
      eq(cr.basic, basic, 'x' + (j + 1) + ' is ' + (basic ? 'made' : 'not made'));
      eq(cr.lo === null ? null : Rtext(cr.lo), lo, 'and its range starts there');
      eq(Rtext(cr.hi), hi, 'and ends there');
      /* INSIDE the range: no tie, the same corner, and the same total a fresh
         solve gives -- which is the claim the lesson makes. */
      const inside = lo === null ? Rsub(cr.hi, R1) : Rdiv(Radd(cr.lo, cr.hi), ri(2));
      const cin = costPivot(sol.tab, j, inside);
      eq(cin.tie.length, 0, 'inside the range nothing ties');
      const obj2 = th.obj.slice();
      obj2[j] = inside;
      const fresh = lpSolve({ max: th.max, names: th.names, obj: obj2, cons: th.cons }, opt);
      eq(Requ(fresh.zOrig, cin.zOrig), true, 'and the total is what a fresh solve gives');
      eq(stdPoint(sol.std, cin.read.x).map(Rtext).join(','), sol.x.map(Rtext).join(','),
         'while the plan has not moved at all');
      /* AT the endpoint: a reduced cost is exactly zero, and one pivot reaches
         a DIFFERENT corner earning the SAME total. That is what a tie is, and
         tabEnter would never find it because it hunts strictly negative. */
      for (const end of [cr.lo, cr.hi]) {
        if (end === null) continue;
        const cp = costPivot(sol.tab, j, end);
        eq(cp.tie.length >= 1, true, 'at ' + Rtext(end) + ' some reduced cost is exactly zero');
        eq(cp.optimal, true, 'and the basis is still optimal there');
        eq(cp.afterRead !== null, true, 'so one pivot reaches the other corner');
        const before = stdPoint(sol.std, cp.read.x).map(Rtext).join(',');
        const after = stdPoint(sol.std, cp.afterRead.x).map(Rtext).join(',');
        eq(before !== after, true, 'which is a DIFFERENT plan: ' + before + ' against ' + after);
        const zAfter = cp.after.maximised ? cp.after.z[cp.after.n] : Rneg(cp.after.z[cp.after.n]);
        eq(Requ(zAfter, cp.zOrig), true, 'earning exactly the same total, which is what a tie means');
        const obj3 = th.obj.slice();
        obj3[j] = end;
        eq(Requ(lpSolve({ max: th.max, names: th.names, obj: obj3, cons: th.cons }, opt).zOrig, cp.zOrig),
           true, 'and a fresh solve at the endpoint agrees with both of them');
      }
    }
  }

  /* THE SAME RANGING ON A MINIMISATION.  The solver always maximises and a
     minimisation is negated on the way in, so a cost handed to costPivot has
     to be negated too -- and a kit that skipped that would report ranges that
     look like ranges and endpoints that are not endpoints.  Every value below
     is checked against a fresh solve at the same coefficient. */
  {
    const bl = specModel(BLEND), s = lpSolve(bl, opt);
    eq(Rtext(s.zOrig) + ' at ' + s.x.map(Rtext).join(','), '9 at 3,1', 'the blend costs 9 at (3, 1)');
    const at = (j, c) => {
      const obj2 = bl.obj.slice();
      obj2[j] = c;
      return lpSolve({ max: bl.max, names: bl.names, obj: obj2, cons: bl.cons }, opt);
    };
    const cx = costRange(s.tab, 0);
    eq(Rtext(cx.lo) + '..' + Rtext(cx.hi), '0..3', 'the first ingredient may cost anything from 0 to 3');
    for (const [end, want] of [[cx.lo, '3'], [cx.hi, '12']]) {
      const cp = costPivot(s.tab, 0, end);
      eq(Rtext(cp.zOrig), want, 'at ' + Rtext(end) + ' the total is ' + want);
      eq(Requ(at(0, end).zOrig, cp.zOrig), true, 'which is what a fresh solve there costs');
      eq(cp.tie.length >= 1, true, 'and a reduced cost is exactly zero, so two plans tie');
    }
    const mid = Rdiv(Radd(cx.lo, cx.hi), ri(2));
    const cin = costPivot(s.tab, 0, mid);
    eq(Rtext(cin.zOrig) + ' ' + cin.tie.length, '15/2 0', 'inside the range nothing ties and the total is 15/2');
    eq(Requ(at(0, mid).zOrig, cin.zOrig), true, 'which a fresh solve confirms');
    const cy = costRange(s.tab, 1);
    eq(Rtext(cy.lo) + '..' + (cy.hi === null ? 'inf' : Rtext(cy.hi)), '2..inf',
       'and the second may cost anything from 2 upwards, a one-sided interval being a real answer');
    eq(Rtext(costPivot(s.tab, 1, cy.lo).zOrig), '8', 'with the total at its lower end 8');
    eq(Requ(at(1, cy.lo).zOrig, ri(8)), true, 'confirmed by a fresh solve');
  }

  /* --- every other preset the ten modes ship ------------------------------ */
  {
    /* `read` needs a preset whose starting basis is NOT the slack columns, or
       the lesson's named misconception has nothing to correct. */
    const bk = lpSolve(specModel(BAKERY), opt), bdv = dualVector(bk.tab);
    eq(Rtext(bk.zOrig) + ' at ' + bk.x.map(Rtext).join(','), '21 at 3,3/2', 'the >= preset solves');
    eq(bdv.columns.map((c) => c.kind).join(','), 'slack,slack,artificial',
       'and its third row reads its price out of an ARTIFICIAL, not the surplus beside it');
    eq(bdv.y.map(Rtext).join(','), '3/4,1/2,0', 'with prices 3/4, 1/2 and 0');
    eq(Requ(bdv.value, bk.zOrig), true, 'and strong duality holding on it');
    const eqm = lpSolve(specModel(EQROW), opt), edv = dualVector(eqm.tab);
    eq(Rtext(eqm.zOrig), '15', 'the = preset solves to 15');
    eq(edv.y.map(Rtext).join(','), '0,0,5', 'and only the quota is worth anything');
    eq(edv.columns[2].kind, 'artificial', 'an = row has no slack column at all');
    /* `rhs`: the ranges the panel prints beside every price. */
    const th = lpSolve(specModel(THREE), opt);
    eq([0, 1, 2].map((i) => {
      const r = rhsRange(th.tab, i);
      return Rtext(r.y_i) + '@' + Rtext(r.lo) + '..' + (r.hi === null ? 'inf' : Rtext(r.hi));
    }).join(' '), '3@8..12 2@6..10 0@2..inf', 'every price and range on the three-activity preset');
    const wsol = lpSolve(wk, opt);
    const wr = rhsRange(wsol.tab, 2);
    eq(Rtext(wr.y_i) + '@' + Rtext(wr.lo) + '..' + Rtext(wr.hi), '1@12..24',
       'and on the workshop, the row the lesson ranges');
    const curve = rhsCurve(wk, 2, R0, ri(36), opt);
    eq(curve.pieces.length + ' ' + curve.breakpoints.map(Rtext).join(','), '3 12,24',
       'the curve the panel draws has three pieces and two corners on the slider range');
    eq(curve.pieces.map((p2) => Rtext(p2.slope)).join(','), '5/2,1,0',
       'with three different slopes, so the price is visibly one segment of it');
    /* A DEGENERATE preset where a tight row is priced at nothing. */
    const dg = lpSolve(specModel(DEGEN), opt);
    eq(dg.read.tightRows.join(','), '0,1,2', 'every row of the degenerate preset is tight');
    eq(Rtext(rhsRange(dg.tab, 2).y_i), '0', 'and the third is still worth exactly zero');
    /* `newcol`: one column that pays for itself and one that does not. */
    const good = priceColumn(wsol.tab, [ri(1), ri(1), ri(1)], ri(4));
    eq(Rtext(good.reduced) + ' ' + good.enters, '3/2 true', 'a column worth 3/2 more than it uses enters');
    eq(Rtext(good.after.z[good.after.n]), '39', 'and one pivot takes the total from 36 to 39');
    const poor = priceColumn(wsol.tab, [ri(1), ri(2), ri(3)], ri(4));
    eq(Rtext(poor.used) + ' ' + Rtext(poor.reduced) + ' ' + poor.enters, '6 -2 false',
       'while a PROFITABLE column that uses 6 worth of resources makes the plan worse');
    /* `newcol` and `dualsimplex`: the rows the presets add. */
    const cut = addRow(wsol.tab, { a: [ri(1), ri(1)], rel: 'le', b: ri(5), name: 'the new rule' }, opt);
    eq(cut.status + ' ' + cut.run.steps.length + ' ' + Rtext(cut.run.zOrig), 'optimal 2 25',
       'a rule the plan breaks is restored in two dual pivots, to 25');
    eq(Requ(cut.run.zOrig, lpSolve({ max: wk.max, names: wk.names, obj: wk.obj,
      cons: wk.cons.concat([{ a: [ri(1), ri(1)], rel: 'le', b: ri(5), name: 'd' }]) }, opt).zOrig),
      true, 'which is exactly what a fresh solve gives');
    const harmless = addRow(wsol.tab, { a: [ri(1), ri(1)], rel: 'le', b: ri(9), name: 'the new rule' }, opt);
    eq(harmless.run.steps.length + ' ' + Rtext(harmless.run.zOrig), '0 36',
       'and a rule the plan already obeys costs no pivots at all');
    /* `parametric`: both fronts, corner for corner. */
    const f4 = paramFront(specModel(FRONT), [ri(4), ri(1)], [ri(1), ri(4)]);
    eq(f4.corners.length + ' ' + f4.breakpoints.map(Rtext).join(','), '4 1/12,1/3,1/2',
       'the four-corner front breaks at three exact weights');
    eq(f4.corners.map((c) => '(' + Rtext(c.f1) + ',' + Rtext(c.f2) + ')').join(''),
       '(28,7)(27,18)(22,28)(10,40)', 'at those four corners');
    eq(f4.efficient.length, 4, 'none of which any other beats on both');
    const f3 = paramFront(specModel(FRONT3), [ri(3), ri(1)], [ri(1), ri(3)]);
    eq(f3.corners.length + ' ' + f3.breakpoints.map(Rtext).join(','), '3 1/6,1/2',
       'and the smaller region has three, breaking at two');
    /* A breakpoint is a breakpoint: the corner the panel names on either side
       of one really does change, and the slider's hundredths never find it. */
    const at = f4.breakpoints[0];
    eq(Rcmp(at, R(8n, 100n)) > 0 && Rcmp(at, R(9n, 100n)) < 0, true,
       'the first breakpoint, 1/12, falls BETWEEN two hundredths, so no slider position is ever on it');
  }

  /* --- the two pixel helpers and the slider guard ------------------------- */
  {
    eq(pxOf(R(1n, 2n), R0, R1, 0, 100), 50, 'the midpoint of a span is the midpoint of the axis');
    eq(pxOf(ri(5), ri(5), ri(25), 40, 640), 40, 'the low end is the left edge');
    eq(pxOf(ri(25), ri(5), ri(25), 40, 640), 640, 'and the high end the right');
    eq(pxOf(ri(3), ri(7), ri(7), 40, 640), 40, 'a span of zero width does not divide by zero');
    /* The rational Number cannot hold, which is the whole reason pxOf reads
       its position out of Rfixed's long division rather than out of Rnum. */
    const third = R(10n ** 400n + 1n, 3n * 10n ** 400n);
    eq(String(Rnum(third)), 'NaN', 'Number holds neither part of a 401-digit fraction');
    eq(String(Rnum(Rdiv(Rsub(third, R0), R1))), 'NaN', 'so the quotient pxOf needs is NaN through Rnum');
    const at = pxOf(third, R0, R1, 0, 300);
    eq(Math.round(at), 100, 'and pxOf still puts a third of the way along at a third of the way along, '
       + 'because it reads the position out of long division rather than out of Number');
    const sp = spanOf([ri(10), ri(30), ri(20)]);
    eq(Rtext(sp.lo) + '..' + Rtext(sp.hi), '9..31', 'a span is padded by a twentieth at each end');
    eq(Rtext(spanOf([ri(4), ri(4)]).lo) + '..' + Rtext(spanOf([ri(4), ri(4)]).hi), '3..5',
       'and coincident values are widened, so a one-point plot still has an axis');
    eq(Rtext(spanOf([]).hi), '1', 'an empty list gets an axis rather than a null');
    eq(clampInt('7', 0, 10, 3), 7, 'a slider hands back a string');
    eq(clampInt('', 0, 10, 3), 3, 'an empty one falls back');
    eq(clampInt('nonsense', 0, 10, 3), 3, 'and so does a value no browser should produce');
    eq(clampInt(NaN, 0, 10, NaN), 0, 'with the low bound as the last resort, because BigInt(NaN) throws');
    eq(clampInt('99', 0, 10, 3), 10, 'a value past the top is clamped');
    eq(clampInt('-4', 0, 10, 3), 0, 'and one below the bottom');
    eq(clampInt('7.6', 0, 10, 3), 8, 'a fractional step rounds, because these sliders count in whole units');
  }
}


// ------------------------------------------------- or_core + network kit
//
// COURSE 4's DRAWING KIT, and the three questions it answers that something
// else in this repository already answers a different way.
//
// The kit's own block is scripts/mathpath/labs/network.py's NETKIT_JS: the
// parser that turns typed text into a DIRECTED network, the two models that
// turn that network into a linear programme, the residual walk, the cut
// enumeration and the project parser. None of it touches a document, so what
// runs below is the shipped source rather than a transcription of it.
//
// THE ORACLES. graph.py's GRAPH_JS cannot express direction, capacity or a
// negative weight, which is why this kit exists at all -- but where the two
// DO answer the same question it is brute force on one side and the kit on
// the other, and they are required to agree:
//
//   GRAPH_JS.dijkstra     against bellmanRounds and against the shortest-path
//                         LP, on the same graph made directed both ways
//   GRAPH_JS.cuts         which finds bridges by REMOVING each edge and
//                         recounting components, against allCuts: the minimum
//                         cut between the ends of an edge is 1 exactly when
//                         that edge is a bridge
//   GRAPH_JS.componentsOf against reachable(), the function that names the
//                         minimum cut in the max-flow mode
//
// GRAPH_JS.kruskal is NOT used. It answers "what is the minimum spanning
// tree", and no mode of this kit asks that: there is no spanning-tree lesson
// on the networks course. An agreement manufactured for it would test the
// manufacturing.
console.log('operations research: the network kit, and the oracles graph.py already had');
{
  const OR2_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const NET_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'network.py');
  const SYS2_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const or2Src = fs.readFileSync(OR2_SOURCE, 'utf8');
  const netSrc = fs.readFileSync(NET_SOURCE, 'utf8');
  const sys2Src = fs.readFileSync(SYS2_SOURCE, 'utf8');
  const or2 = (n) => blockFrom(or2Src, n, OR2_SOURCE);
  const kit = (n) => blockFrom(netSrc, n, NET_SOURCE);
  const sys2 = (n) => blockFrom(sys2Src, n, SYS2_SOURCE);

  eval(sys2('FORMAT_JS') + sys2('MATRIX_JS') + or2('ORFMT_JS') + or2('TABLEAU_JS')
     + or2('PHASE_JS') + or2('DUAL_JS') + or2('NET_JS')
     + kit('NETKIT_JS') + kit('CHECK_JS') + kit('MODEL_JS') + kit('CUT_JS')
     + kit('MATCH_JS') + kit('PROJECT_JS') + kit('TU_JS'));
  /* Seven blocks, because no page takes all seven: the project mode ships no
     simplex and the determinant mode ships no residual network.  Everything
     is evaluated together HERE, which is the only place that should. */

  const ri = (v) => R(BigInt(v), 1n);
  const rt = (a) => Rtext(a);
  const capcost = ['capacity', 'cost'];

  /* --- the representation: an arc is ORDERED --------------------------- */
  {
    const net = parseNet('s>a 5:2, a>b 4:2, b>a 3:5, a>t 3:1, b>t 4:3', capcost);
    eq(net.nodes.join(''), 'sabt', 'the nodes come out in order of first appearance, source first');
    eq(net.arcs.length, 5, 'five arcs');
    eq(rt(net.arcs[1].cap) + ' at ' + rt(net.arcs[1].cost), '4 at 2', 'a to b holds 4 at a price of 2');
    eq(rt(net.arcs[2].cap) + ' at ' + rt(net.arcs[2].cost), '3 at 5',
       'and b to a is a DIFFERENT object: 3 at a price of 5, which no adjacency matrix can hold');
    eq(antiparallel(net.arcs).length, 2, 'the two of them are an antiparallel pair, and the lab names it');
    eq(parseNet('a>a 1:1', capcost).bad !== undefined, true, 'a loop is refused rather than drawn');
    eq(parseNet('a>b 1', capcost).bad !== undefined, true, 'and an arc missing its cost');
    eq(parseNet('a>b -1:1', capcost).bad !== undefined, true, 'and a negative capacity');
    eq(rt(parseNet('a>b 7/2:1', capcost).arcs[0].cap), '7/2',
       'a slash is a fraction, because the FIELD separator is a colon');
    eq(parseNet('a>b *:3', capcost).arcs[0].capped, false,
       'and * is no upper bound at all -- not a large number standing in for one');
    eq(parseNet('1>2 1:1', capcost).nodes.join(''), '12', 'a node may be called 1, as the odd cycle calls its vertices');

    /* conservation is LOCAL, and capacity is a second test entirely */
    const goodRead = parseFlow('s>a 4, a>b 2, b>a 0, a>t 2, b>t 2', net.arcs);
    eq(goodRead.bad === undefined, true, 'the worked flow parses onto the arcs it names, in the order it names them');
    const good = goodRead.flow;
    const sup = parseSupply('s:4, t:-4', net.nodes);
    eq(conservation(net.nodes, net.arcs, good, sup.supply).ok, true, 'the worked flow balances at every node');
    eq(capacityCheck(net.arcs, good).ok, true, 'and fits inside every capacity');
    eq(rt(flowCost(net.arcs, good)), '20', 'at a cost of 20');
    const local = parseFlow('s>a 4, a>b 1, b>a 0, a>t 2, b>t 2', net.arcs).flow;
    const cons = conservation(net.nodes, net.arcs, local, sup.supply);
    eq(cons.violated.join(','), 'a,b', 'a flow can balance in TOTAL and fail at two named nodes');
    eq(rt(cons.net.reduce((x, y) => Radd(x, y), R0)), '0',
       'because the per-node imbalances sum to zero whatever the flow is -- which is why a single verdict would hide it');
    const over = parseFlow('s>a 5, a>b 5, b>a 0, a>t 0, b>t 5', net.arcs).flow;
    eq(conservation(net.nodes, net.arcs, over, parseSupply('s:5, t:-5', net.nodes).supply).ok, true,
       'and it can conserve at EVERY node');
    eq(capacityCheck(net.arcs, over).over.length, 2, 'while overfilling two arcs');
    eq(rt(parseSupply('s:6, t:-4', net.nodes).total), '2',
       'supplies that do not sum to zero are a feasibility test you can run before solving anything');
    eq(parseFlow('s>c 1', net.arcs).bad !== undefined, true, 'a flow on an arc that is not there is refused');
    const twoWay = parseNet('a>b 4:2, b>a 3:5', capcost);
    const pf = parseFlow('a>b 1, b>a 2', twoWay.arcs);
    eq(pf.flow.map(rt).join(','), '1,2',
       'and a flow names each DIRECTION separately: 1 down a to b and 2 back, on two arcs, not 3 on one edge');
    eq(rt(flowCost(twoWay.arcs, pf.flow)), '12', 'which costs 1x2 + 2x5 = 12, and the other way round would be 19');
  }

  /* --- ONE programme, five data sets ----------------------------------- */
  const solveNet = (spec, supply) => {
    const n = parseNet(spec, capcost);
    const b = parseSupply(supply, n.nodes);
    return { net: n, b: b, run: lpSolve(mcfModel(n.nodes, n.arcs, b.supply)) };
  };
  {
    const mcf = solveNet('s>a 3:2, s>b 3:3, a>b 2:1, a>t 3:5, b>t 3:2', 's:4, t:-4');
    eq(rt(mcf.run.zOrig), '22', 'the minimum-cost flow costs 22');
    eq(mcf.run.x.every(Rint), true,
       'and every arc carries a WHOLE number, with no integrality constraint anywhere in the programme');
    eq(rt(solveNet('S1>D1 *:4, S1>D2 *:6, S1>D3 *:9, S2>D1 *:5, S2>D2 *:3, S2>D3 *:8',
                   'S1:20, S2:30, D1:-10, D2:-25, D3:-15').run.zOrig), '245',
       'the SAME programme on transportation data costs 245');
    eq(rt(solveNet('W1>J1 1:9, W1>J2 1:2, W1>J3 1:7, W2>J1 1:6, W2>J2 1:4, W2>J3 1:3, '
                 + 'W3>J1 1:5, W3>J2 1:8, W3>J3 1:1',
                   'W1:1, W2:1, W3:1, J1:-1, J2:-1, J3:-1').run.zOrig), '9',
       'and on assignment data, which is transportation with every supply and demand set to one, 9');

    /* the two cross-checks that make "one programme, different data" a claim
       about numbers rather than a slogan: the shortest-path data must solve to
       the label Bellman-Ford reaches, and the maximum-flow data to the cut. */
    const sp = solveNet('s>a 1:4, s>b 1:2, b>a 1:1, a>t 1:3, b>t 1:7', 's:1, t:-1');
    const bf = bellmanRounds(sp.net.nodes, sp.net.arcs, 's');
    eq(rt(sp.run.zOrig), '6', 'the shortest-path data solves to 6');
    eq(rt(sp.run.zOrig), rt(bf.dist[3]),
       'which is exactly the label Bellman-Ford reaches -- the simplex and the relaxation, same answer');
    const mx = solveNet('s>a 3:0, s>b 2:0, a>b 2:0, a>t 2:0, b>t 3:0, t>s *:-1', '');
    const cnet = parseNet('s>a 3, s>b 2, a>b 2, a>t 2, b>t 3', ['capacity']);
    eq(rt(mx.run.zOrig), '-5', 'the maximum-flow data, priced at minus one on the return arc, solves to -5');
    eq(rt(Rneg(mx.run.zOrig)), rt(allCuts(cnet.nodes, cnet.arcs, 's', 't').min),
       'and minus that is the minimum cut of the same network -- one programme, two special cases, one matrix');
    eq(solveNet('s>a 3:2, a>t 3:5', 's:4, t:-3').run.status, 'infeasible',
       'supplies that do not balance make the programme infeasible, which is what adding the rows up predicts');
  }

  /* --- the determinants, and the one that is 2 -------------------------- */
  {
    const tri = parseNet('1>2 1:1, 2>3 1:1, 3>1 1:1', capcost);
    const D = incidence(tri.nodes, tri.arcs), U = incidenceUndirected(tri.nodes, tri.arcs);
    eq(rt(Mdet(U)), '2', "an odd cycle's UNDIRECTED incidence matrix has determinant 2");
    eq(unimodularSweep(U, 3).bad.length, 1, 'so exactly one submatrix of it is outside {0, +1, -1}');
    eq(unimodularSweep(D, 3).unimodular, true,
       'while the DIRECTED matrix on the same drawing, +1 at the tail and -1 at the head, is unimodular');
    const half = lpSolve(packingModel(U, ['x1', 'x2', 'x3']));
    eq(half.x.map(rt).join(','), '1/2,1/2,1/2',
       'and the corner it produces is HALVES -- the same exact simplex, a different matrix');
    eq(rt(half.zOrig), '3/2', 'worth 3/2, which no integer point reaches');
    const sq = parseNet('1>2 1:1, 2>3 1:1, 3>4 1:1, 4>1 1:1', capcost);
    const SU = incidenceUndirected(sq.nodes, sq.arcs);
    eq(rt(Mdet(SU)), '0', 'an EVEN cycle is bipartite, and its undirected incidence has determinant 0');
    const whole = lpSolve(packingModel(SU, ['a', 'b', 'c', 'd']));
    eq(whole.x.every(Rint) + ' ' + rt(whole.zOrig), 'true 2',
       'so that corner is whole: it is the ODD cycle that breaks it, not undirectedness as such');
    eq(pickIndices('1,3,4', 5, 'row').pick.join(','), '0,2,3', 'the picks are 1-based on the page');
    eq(pickIndices('0', 5, 'row').bad !== undefined, true, 'there is no row 0, and saying so beats clamping');
    eq(pickIndices('6', 5, 'row').bad !== undefined, true, 'nor a row 6 of five');
    eq(pickIndices('1,1', 5, 'row').bad !== undefined, true,
       'and a row named twice is refused rather than silently giving a determinant of zero');
    eq(rt(submatrixDet(D, [0, 1], [0, 1])), '1',
       'submatrixDet gathers the picked rows and columns and hands that block to Mdet');
    eq(rt(submatrixDet(D, [0, 1, 2], [0, 1, 2])), '0',
       'and the whole of N is singular, because every column holds one +1 and one -1 so the rows sum to zero');
  }

  /* --- flow, cuts, and the dual ---------------------------------------- */
  const runToMax = (net, s, t) => {
    let f = net.arcs.map(() => R0);
    for (let i = 0; i < 40; i += 1) {
      const res = residual(net.arcs, f), ps = resPaths(res, s, t, 8);
      if (!ps.length) break;
      f = augmentFlow(net.arcs, f, res, ps[0]).flow;
    }
    return f;
  };
  {
    const net = parseNet('s>a 3, s>b 2, a>b 2, a>t 2, b>t 3', ['capacity']);
    const f = runToMax(net, 's', 't');
    const every = allCuts(net.nodes, net.arcs, 's', 't');
    eq(rt(flowValue(net.nodes, net.arcs, f, 's')), '5',
       'pushing along whatever residual path comes first reaches 5');
    eq(rt(every.min), '5',
       'and the smallest of every cut -- all four enumerated, not searched for -- is 5 as well');
    eq(every.minimum.length, 2,
       'TWO of the four are minimum, so a minimum cut is not unique and the lesson ships the instance that shows it');
    eq(rt(cutCapacity(net.nodes, net.arcs, reachable(net.nodes, residual(net.arcs, f), 's').set).capacity), '5',
       'the set reachable from the source in the final residual network is one of them');
    eq(every.cuts.every((c) => Rcmp(c.capacity, flowValue(net.nodes, net.arcs, f, 's')) >= 0), true,
       'and every cut there is bounds the flow, which is weak duality exhibited rather than asserted');

    /* the dual, at the 0/1 point every cut names */
    const model = maxflowModel(net.nodes, net.arcs, 's', 't');
    const dual = dualModel(model);
    eq(checkModel(model, f).ok + ' ' + rt(checkModel(model, f).value), 'true 5',
       'the flow is a feasible point of the primal programme, worth 5');
    let feasible = true, exact = true;
    every.cuts.forEach((c) => {
      const chk = checkModel(dual, cutDualPoint(net.nodes, net.arcs, c.S, 's', 't'));
      if (!chk.ok) feasible = false;
      if (!Requ(chk.value, c.capacity)) exact = false;
    });
    eq(feasible, true,
       'EVERY cut, written as 0/1 potentials and 0/1 arc variables, is a FEASIBLE point of the dual programme');
    eq(exact, true,
       'and its dual objective is exactly that cut capacity -- which is WHY a cut bounds a flow, rather than a coincidence');
    eq(rt(lpSolve(model).zOrig), '5',
       'and the simplex on the primal agrees with both, so the theorem is strong duality on this instance');

    /* a network where the minimum cut IS unique, and a wider one */
    const uniq = parseNet('s>a 2, s>b 5, a>t 5, b>t 3', ['capacity']);
    const uc = allCuts(uniq.nodes, uniq.arcs, 's', 't');
    eq(rt(uc.min) + ' ' + uc.minimum.length + ' ' + uc.cuts[0].S.join(''), '5 1 sb',
       'on another instance the minimum cut is unique, and it is {s, b}');
    eq(rt(flowValue(uniq.nodes, uniq.arcs, runToMax(uniq, 's', 't'), 's')), '5', 'with a maximum flow of 5');
    const wide = parseNet('s>a 4, s>b 3, a>c 3, a>b 2, b>d 4, c>t 3, d>t 4, c>d 1', ['capacity']);
    eq(rt(flowValue(wide.nodes, wide.arcs, runToMax(wide, 's', 't'), 's')), '7',
       'six nodes, sixteen cuts, and the augmenting loop still lands on the minimum');
    eq(rt(allCuts(wide.nodes, wide.arcs, 's', 't').min), '7', 'which the enumeration confirms independently');

    /* the residual network is what makes a backward push possible at all */
    const res0 = residual(net.arcs, net.arcs.map(() => R0));
    eq(res0.length, net.arcs.length, 'an empty flow has only forward residual arcs');
    eq(residual(net.arcs, f).filter((a) => a.kind === 'backward').length,
       f.filter((v) => !Rzero(v)).length, 'and every arc carrying flow contributes a backward one');
  }

  /* --- matching, and the cut that proves Hall's condition sufficient ---- */
  {
    const check = (spec, wantSize, wantS, wantN) => {
      const bip = parseBip(spec);
      const m = bipartiteMatch(bip.left, bip.right, bip.edges);
      const built = matchingNetwork(bip.left, bip.right, bip.edges);
      const cut = cutCapacity(built.nodes, built.arcs, matchingCut(m));
      eq(m.size, wantSize, spec + ': the maximum matching has ' + wantSize + ' edges');
      eq(rt(cut.capacity), String(wantSize),
         'and the minimum cut of the flow network has exactly that capacity, which is the theorem');
      eq(m.cover.size, m.size, 'as does the minimum vertex cover, computed from the matching and not drawn by eye');
      eq(m.deficient.S.join('') + '/' + m.deficient.N.join(''), wantS + '/' + wantN,
         'and the deficient set read off that cut is S = {' + wantS + '} with N(S) = {' + wantN + '}');
      return m;
    };
    check('1-a, 1-b, 2-a, 2-b, 3-a, 3-b', 2, '123', 'ab');
    const sub = check('1-a, 2-a, 3-a, 4-b, 4-c, 4-d', 2, '123', 'a');
    eq(sub.deficient.S.length - sub.deficient.N.length, 2,
       'a deficient set need not be all of X: three applicants here share one job');
    const perfect = check('1-a, 1-b, 2-b, 2-c, 3-c, 3-d, 4-d, 4-a', 4, '', '');
    eq(perfect.perfect + ' ' + perfect.deficient.hall, 'true false',
       'and when the matching is perfect there is no certificate to produce, because the condition holds');
    eq(parseBip('1a').bad !== undefined, true, 'an edge without a dash is refused');
    eq(parseBip('1-a, 2-a, 3-a, 4-a, 5-a, 6-a').bad !== undefined, true, 'and a side with six vertices');
  }

  /* --- the project network, and where shortening stops paying ----------- */
  {
    const SPEC = 'A 3, B 2 after A, C 4 after A, G 5 after A, D 2 after B, E 3 after C, '
               + 'H 2 after G, F 1 after D E, I 1 after F H';
    const proj = parseActs(SPEC), pass = cpmPasses(proj.acts);
    eq(rt(pass.makespan), '12', 'nine activities, and the project takes 12');
    eq(pass.critical.join(''), 'ACEFI', 'five of them are critical');
    eq(pass.paths.length, 1, 'on one path');

    /* ORACLE: the two passes against an exhaustive enumeration of chains. The
       forward/backward pair is O(V + E) and this is every path there is; if
       they ever disagree the two-pass computation is the one that is wrong. */
    const longestChain = (acts) => {
      const ix = {}, succ = acts.map(() => []);
      acts.forEach((a, i) => { ix[a.id] = i; });
      acts.forEach((a, i) => (a.pred || []).forEach((p) => succ[ix[p]].push(i)));
      let best = 0;
      const walk = (i, len) => {
        const L = len + Number(acts[i].dur.n) / Number(acts[i].dur.d);
        if (!succ[i].length) { if (L > best) best = L; return; }
        succ[i].forEach((j) => walk(j, L));
      };
      acts.forEach((a, i) => { if (!(a.pred || []).length) walk(i, 0); });
      return best;
    };
    eq(Number(pass.makespan.n), longestChain(proj.acts),
       'the two-pass makespan equals the longest of EVERY chain, enumerated one at a time');

    const curve = crashCurve(proj.acts, 'C', 4);
    eq(curve.steps.map((s) => rt(s.makespan)).join(','), '12,11,11,11,11',
       'shortening C buys one unit of project and then nothing at all');
    eq(curve.lastUseful, 1, 'so the return stops after one unit');
    eq(curve.steps[1].paths, 2, 'because at that point a SECOND path has become critical');
    eq(curve.steps[2].critical.join(''), 'AGHI', 'and beyond it the length is held by a chain C is not on');
    eq(rt(cpmPasses(proj.acts).slack[proj.acts.findIndex((a) => a.id === 'G')]), '1',
       'G has a unit of slack, so shortening G is worth nothing until that unit is used');

    const twop = cpmPasses(parseActs('A 3, B 2 after A, C 2 after A, D 2 after B, E 2 after C, F 1 after D E').acts);
    eq(rt(twop.makespan) + ' ' + twop.paths.length, '8 2', 'a project can open with two critical paths');
    eq(crashCurve(parseActs('A 3, B 2 after A, C 2 after A, D 2 after B, E 2 after C, F 1 after D E').acts,
                  'B', 2).lastUseful, 0, 'and then the FIRST unit off either of them buys nothing');
    eq(cpmPasses(parseActs('A 3 after C, B 2 after A, C 4 after B').acts).cycle.length, 3,
       'a precedence loop has no schedule at all, and the loop is named');
    eq(parseActs('A 3 after Z').bad !== undefined, true,
       'and an activity waiting on something that is not in the project is refused');
    eq(parseActs('A 3, A 4').bad !== undefined, true, 'as are two activities with one name');
  }

  /* --- the layout, which is arithmetic rather than decoration ----------- */
  {
    const net = parseNet('s>a 3:1, s>b 2:1, a>b 2:1, a>t 2:1, b>t 3:1', capcost);
    const lay = netLayout(net.nodes, net.arcs, 660, 280);
    eq(lay.layered, true, 'an acyclic network is laid out in layers');
    eq(lay.pos.s.rank + ',' + lay.pos.a.rank + ',' + lay.pos.b.rank + ',' + lay.pos.t.rank, '0,1,2,3',
       'each node one column past the longest chain that reaches it, so the flow reads left to right');
    eq(lay.pos.s.x < lay.pos.a.x && lay.pos.a.x < lay.pos.t.x, true, 'and the source is left of the sink');
    const cyc = parseNet('x>y 1, y>z 1, z>x 1', ['cost']);
    eq(netLayout(cyc.nodes, cyc.arcs, 660, 280).layered, false,
       'a cycle has no layering, and the layout says so rather than pretending');
  }

  /* ================================================================ ORACLES
     graph.py's GRAPH_JS, on graphs both representations can hold. */
  {
    eval(graphBlock('GRAPH_JS'));
    const LIST = [[1, 2, 4], [1, 3, 3], [2, 3, 2], [2, 4, 5], [3, 4, 7], [4, 5, 1], [5, 6, 6]];
    LESSON = lessonFrom(LIST); useLessonWeights = true; N = 6; A = PRESETS.lesson(6);
    const ids = ['1', '2', '3', '4', '5', '6'];
    const both = [];
    edges().forEach((e) => {
      both.push({ from: ids[e[0]], to: ids[e[1]], cost: ri(e[2]), cap: R1, capped: true });
      both.push({ from: ids[e[1]], to: ids[e[0]], cost: ri(e[2]), cap: R1, capped: true });
    });
    eq(both.length, edges().length * 2,
       'an undirected edge is TWO arcs here, which is the whole difference between the representations');

    /* ORACLE 1: Bellman-Ford in exact rationals against a float-and-Infinity
       Dijkstra that has been shipping since the discrete mathematics path. */
    for (const s of [0, 2, 5]) {
      const bf = bellmanRounds(ids, both, ids[s]);
      eq(bf.dist.map((d) => (d === null ? 'inf' : rt(d))).join(','),
         dijkstra(s).dist.map((d) => (d === Infinity ? 'inf' : String(d))).join(','),
         'bellmanRounds agrees with GRAPH_JS.dijkstra from vertex ' + (s + 1));
      eq(potentialCheck(ids, both, bf.dist, ids[s], ids[5]).ok, true,
         'and the labels it stops on are feasible potentials on every one of the arcs');
      eq(potentialCheck(ids, both, bf.dist.map((d) => Radd(d, ri(7))), ids[s], ids[5]).ok, true,
         'as are the same labels with 7 added to every one of them, because each constraint is a DIFFERENCE');
      eq(rt(potentialCheck(ids, both, bf.dist.map((d) => Radd(d, ri(7))), ids[s], ids[5]).value),
         rt(potentialCheck(ids, both, bf.dist, ids[s], ids[5]).value),
         'and the dual objective does not move when they are shifted -- which is what makes them prices');
    }
    /* and the shortest-path LP lands in the same place as both of them */
    {
      const sup = {}; ids.forEach((v) => { sup[v] = R0; });
      sup['1'] = R1; sup['6'] = R(-1n, 1n);
      eq(rt(lpSolve(mcfModel(ids, both, sup)).zOrig), String(dijkstra(0).dist[5]),
         'and so does the minimum-cost flow LP with b = e_s - e_t and u = 1: three computations, one number');
    }

    /* ORACLE 2: bridges, found by REMOVING each edge and recounting
       components, against the minimum cut between that edge's two ends. They
       are the same fact: an edge is a bridge exactly when one arc separates
       its endpoints. */
    for (const [preset, n] of [['tree', 7], ['cycle', 6], ['path', 6], ['petersen', 6], ['star', 5]]) {
      LESSON = null; useLessonWeights = false; N = n; A = PRESETS[preset](n);
      const bridge = {};
      cuts().bridges.forEach((b) => { bridge[b.edge[0] + '-' + b.edge[1]] = true; });
      const vid = []; for (let i = 0; i < n; i += 1) vid.push('v' + (i + 1));
      const arcs = [];
      edges().forEach((e) => {
        arcs.push({ from: vid[e[0]], to: vid[e[1]], cap: R1, cost: R0, capped: true });
        arcs.push({ from: vid[e[1]], to: vid[e[0]], cap: R1, cost: R0, capped: true });
      });
      let agree = true, checked = 0;
      edges().forEach((e) => {
        checked += 1;
        const mc = allCuts(vid, arcs, vid[e[0]], vid[e[1]]).min;
        if (Requ(mc, R1) !== !!bridge[e[0] + '-' + e[1]]) agree = false;
      });
      eq(agree && checked > 0, true,
         preset + ' on ' + n + ' vertices: allCuts says the minimum cut across an edge is 1 on exactly the '
         + checked + ' edges GRAPH_JS.cuts calls bridges, by removing each and recounting components');
      /* ORACLE 3: reachable(), the function that NAMES the minimum cut, against
         the same brute-force component walk. */
      const comp = componentsOf().map((c) => c.map((i) => vid[i]).sort().join(','));
      const walk = reachable(vid, arcs, vid[0]).set.slice().sort().join(',');
      eq(comp.indexOf(walk) >= 0, true,
         'and reachable() from the first vertex is exactly one of the components GRAPH_JS.componentsOf finds on ' + preset);
    }
  }
}


// ==========================================================================
// Operations Research course four: the `transport` kit's own arithmetic
// ==========================================================================
//
// or_core's TRANS_JS is exercised in the or_core section far above, at the
// ENGINE level: balance, northwest, leastCost, uvPotentials, stoneCycle and
// hungarian are each called there, and MODI is driven to optimality by a loop
// written inside that test. None of that touches this kit. TRANSPORT_JS is the
// layer the three published lessons actually read -- parseGrid, tableauCost,
// basisForest, padBasis, pickEntering, checkCycle, rectangleGuess,
// shiftPotentials, modiRun, assignDual, coverCheck and greedyAssign -- and it
// is where the kit's own decisions live. A kit that builds, paints, runs clean
// under labcheck and passes every structural guard can still report the wrong
// optimum, so none of those proves anything below.
//
// THE ORACLE for the transportation half is EVERY BASIC FEASIBLE SOLUTION,
// enumerated. A basis of a transportation tableau is a spanning tree of the
// m x n row/column bipartite graph, so `everyBasicSolution` takes every subset
// of m + n - 1 cells, keeps the ones that really are spanning trees, solves
// each by peeling leaves off the tree, discards the ones with a negative
// allocation, and returns the cheapest of what is left. That is corner
// enumeration -- the same kind of oracle the or_core section holds the simplex
// to -- and it shares no code with the potentials, the cycle or the pivot rule,
// which are the three things MODI could get wrong. On the kit's default preset it
// returns 435, which is the figure the or_core section reaches by the exact
// simplex through Phase I with equality rows: two computations, no shared
// arithmetic, one number.
//
// THE ORACLE for the assignment half is exhaustive over permutations, and for
// Koenig it is EVERY VERTEX COVER of the zero pattern, enumerated over all
// 2^(2n) selections of rows and columns. The second one is what turns C4 L6's
// named misconception into a measurement:
//
//   ON THE KIT'S DEFAULT ASSIGNMENT PRESET, THE "DRAW LINES THROUGH THE ZEROS"
//   RECIPE IS NOT A FUNCTION OF THE MATRIX. At the second cover step of
//   `jobs`, covering the row or column that holds the most still-uncovered
//   zeros draws FOUR lines if ties go to rows and THREE if ties go to columns,
//   on the same matrix, by the same rule -- and the recipe has no tie-break to
//   appeal to. Four is n, so the rows-first reader concludes the zeros carry a
//   complete assignment; the maximum matching is 3, so they do not. The
//   enumeration says the minimum cover is 3 and unique. `bipartiteMatch`
//   returns 3. This is why the cover is computed and the recipe is not
//   implemented, and it is now measured rather than asserted.
//
// TWO THINGS PINNED HERE THAT THE KIT'S OWN PROSE GETS WRONG OR NEARLY DOES:
//
//   * transport.py's module docstring says of `rectangleGuess` that "on the
//     worked example the guess closes; on the second iteration it does not".
//     On the kit's default view -- preset `balanced`, north-west start, Dantzig
//     rule -- it is the other way round: the guess is REFUSED on the first
//     iteration, at (2,1), and closes on the second. The order below is what
//     the function returns.
//   * the cost of that same default run is NOT strictly decreasing. Its second
//     pivot has theta = 0, so the trace is 520 -> 475 -> 475 -> 435, and an
//     assertion that every iteration costs less than the last would fail on a
//     shipped preset. Non-increasing is the claim; degenerate pivots are the
//     reason.
console.log('operations research: the transport kit, and every basic feasible solution it is held to');
{
  const OR4_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const TRANS_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'transport.py');
  const SYS4_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const or4Src = fs.readFileSync(OR4_SOURCE, 'utf8');
  const transSrc = fs.readFileSync(TRANS_SOURCE, 'utf8');
  const sys4Src = fs.readFileSync(SYS4_SOURCE, 'utf8');
  const or4 = (n) => blockFrom(or4Src, n, OR4_SOURCE);
  const tk = (n) => blockFrom(transSrc, n, TRANS_SOURCE);
  const sys4 = (n) => blockFrom(sys4Src, n, SYS4_SOURCE);

  /* Exactly what transport.py's _CORE_JS concatenates, in that order, so a
     dependency the kit forgot to take fails here and not in a browser. */
  eval(sys4('FORMAT_JS') + or4('ORFMT_JS') + or4('NET_JS') + or4('TRANS_JS') + tk('TRANSPORT_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rt = (a) => Rtext(a);
  const cn = (c) => '(' + (c.i + 1) + ',' + (c.j + 1) + ')';
  const cells = (list) => list.map(cn).join(' ');
  const sum = (list) => list.reduce(Radd, R0);

  /* The presets, as the strings a reader types. They are transcribed, so each
     one is required to appear verbatim in the module: a preset edited without
     editing this section fails HERE, by name, rather than silently moving
     every figure below. */
  const TP = {
    balanced: { cost: '10 2 20 11; 12 7 9 20; 4 14 16 18', supply: '15 25 10', demand: '5 15 15 15' },
    surplus: { cost: '8 6 10; 9 12 13; 14 9 16', supply: '20 30 25', demand: '20 25 20' },
    degenerate: { cost: '5 3 8; 4 7 6; 9 2 5', supply: '10 20 10', demand: '10 20 10' }
  };
  const AP = {
    jobs: '10 19 8 15; 10 18 7 17; 13 16 9 14; 12 19 8 18',
    sites: '90 75 75 80; 35 85 55 65; 125 95 90 105; 45 110 95 115',
    crews: '9 11 14 11 7; 6 15 13 13 10; 12 13 6 8 8; 11 9 10 12 9; 7 12 14 10 14'
  };
  {
    let drift = [];
    for (const k of Object.keys(TP)) {
      for (const f of Object.keys(TP[k])) if (transSrc.indexOf('"' + TP[k][f] + '"') < 0) drift.push(k + '.' + f);
    }
    for (const k of Object.keys(AP)) if (transSrc.indexOf('"' + AP[k] + '"') < 0) drift.push(k + '.cost');
    eq(drift.join(','), '', 'every preset transcribed here is the string transport.py ships');
    eq(transSrc.indexOf('greedy loses badly here') > 0, true,
       'and the sites preset still advertises that greed loses on it, which is priced below');
    eq(transSrc.indexOf('greedy happens to be right') > 0, true,
       'and the crews preset that greed happens to get right');
  }

  /* ================================================================ ORACLE 1
     Every basic feasible solution of a transportation problem: every spanning
     tree of the row/column bipartite graph, solved by peeling leaves. Nothing
     here knows what a potential or a stepping-stone cycle is. */
  const everyBasicSolution = (C, S, D) => {
    const m = S.length, n = D.length, want = m + n - 1, grid = [];
    for (let i = 0; i < m; i += 1) for (let j = 0; j < n; j += 1) grid.push([i, j]);
    let best = null, trees = 0, feasible = 0;
    const pick = [];
    const solve = () => {
      /* a spanning tree, or nothing */
      const parent = [];
      for (let k = 0; k < m + n; k += 1) parent.push(k);
      const find = (a) => { while (parent[a] !== a) { parent[a] = parent[parent[a]]; a = parent[a]; } return a; };
      for (const c of pick) {
        const a = find(c[0]), b = find(m + c[1]);
        if (a === b) return;
        parent[a] = b;
      }
      const roots = {};
      for (let k = 0; k < m + n; k += 1) roots[find(k)] = true;
      if (Object.keys(roots).length !== 1) return;
      trees += 1;
      /* peel: a row or column holding one remaining cell fixes that cell */
      const s = S.slice(), d = D.slice(), left = pick.slice(), x = [];
      while (left.length) {
        let hit = -1, alone = 'row';
        for (let k = 0; k < left.length && hit < 0; k += 1) {
          let rc = 0, cc = 0;
          for (const q of left) { if (q[0] === left[k][0]) rc += 1; if (q[1] === left[k][1]) cc += 1; }
          if (rc === 1) { hit = k; alone = 'row'; } else if (cc === 1) { hit = k; alone = 'col'; }
        }
        if (hit < 0) return;
        const c = left[hit], amt = alone === 'row' ? s[c[0]] : d[c[1]];
        x.push({ i: c[0], j: c[1], x: amt });
        s[c[0]] = Rsub(s[c[0]], amt); d[c[1]] = Rsub(d[c[1]], amt);
        left.splice(hit, 1);
      }
      for (const v of s) if (!Rzero(v)) return;
      for (const v of d) if (!Rzero(v)) return;
      for (const c of x) if (Rsign(c.x) < 0) return;
      feasible += 1;
      let z = R0;
      for (const c of x) z = Radd(z, Rmul(C[c.i][c.j], c.x));
      if (best === null || Rcmp(z, best) < 0) best = z;
    };
    const walk = (at) => {
      if (pick.length === want) { solve(); return; }
      for (let k = at; k < grid.length; k += 1) { pick.push(grid[k]); walk(k + 1); pick.pop(); }
    };
    walk(0);
    return { best: best, trees: trees, feasible: feasible };
  };

  /* --- reading a tableau in, which is the reader's only door -------------- */
  {
    const C = parseGrid(TP.balanced.cost);
    eq(C.length + 'x' + C[0].length, '3x4', 'the default cost table parses as three rows of four');
    eq(C.map((r) => r.map(rt).join(',')).join(' | '), '10,2,20,11 | 12,7,9,20 | 4,14,16,18',
       'entry by entry, semicolons between rows and spaces between entries');
    eq(parseGrid('1,2;3,4').map((r) => r.map(rt).join(',')).join('|'), '1,2|3,4', 'commas separate too');
    eq(rt(parseRow('7/2 1/3')[0]) + ',' + rt(parseRow('7/2 1/3')[1]), '7/2,1/3',
       'a slash is an exact fraction, because Rread is the only reader here');
    eq(parseGrid('1 2; 3'), null, 'a ragged table is REFUSED rather than padded');
    eq(parseRow('banana'), null, 'and text that is not a number is null, not NaN');
    eq(parseGrid(''), null, 'as is nothing at all');
    eq(parseRow('  4   6  ').map(rt).join(','), '4,6', 'and repeated spaces are one separator, not an empty entry');
  }

  /* --- C4 L3: balancing CONSERVES, and the dummy costs nothing ------------ */
  {
    for (const k of Object.keys(TP)) {
      const C = parseGrid(TP[k].cost), S = parseRow(TP[k].supply), D = parseRow(TP[k].demand);
      const bal = balance(S, D, C);
      eq(rt(sum(bal.supply)), rt(sum(bal.demand)),
         k + ': total supply equals total demand AFTER balancing, whatever it was before');
      eq(bal.supply.length, bal.cost.length, k + ': and the cost table grew a row exactly when the supplies did');
      eq(bal.demand.length, bal.cost[0].length, k + ': or a column exactly when the demands did');
      /* the real cells are untouched: balancing adds, it does not reprice */
      let moved = 0;
      for (let i = 0; i < C.length; i += 1) for (let j = 0; j < C[0].length; j += 1)
        if (!Requ(bal.cost[i][j], C[i][j])) moved += 1;
      eq(moved, 0, k + ': and not one real unit cost was changed by it');
    }
    eq(balance(parseRow('15 25 10'), parseRow('5 15 15 15')).dummy, null,
       'the default preset needs no dummy at all');
    eq(rt(balance(parseRow('15 25 10'), parseRow('5 15 15 15')).totalSupply), '50', 'both sides being 50');
    const sur = balance(parseRow(TP.surplus.supply), parseRow(TP.surplus.demand), parseGrid(TP.surplus.cost));
    eq(sur.dummy + ' ' + rt(sur.amount), 'col 10', 'the surplus preset gains a dummy DESTINATION carrying 10');
    eq(rt(sum(sur.supply)) + '/' + rt(sum(sur.demand)), '75/75', 'which balances 75 against 75');
    eq(sur.cost.map((r) => rt(r[3])).join(','), '0,0,0',
       'and every cost in the dummy column is zero, which is the whole of the lesson');
    const shortfall = balance([ri(4), ri(6)], [ri(5), ri(5), ri(5)],
                              [[ri(1), ri(2), ri(3)], [ri(4), ri(5), ri(6)]]);
    eq(shortfall.dummy + ' ' + rt(shortfall.amount), 'row 5', 'unmet demand gains a dummy SOURCE instead');
    eq(shortfall.cost[2].map(rt).join(','), '0,0,0', 'whose row is zero for the same reason');
    eq(rt(sum(shortfall.supply)) + '/' + rt(sum(shortfall.demand)), '15/15', 'and the two sides agree again');
  }

  /* --- C4 L4: MODI reaches the SAME optimum from either start ------------- */
  const solved = {};
  {
    for (const k of Object.keys(TP)) {
      const C0 = parseGrid(TP[k].cost), S0 = parseRow(TP[k].supply), D0 = parseRow(TP[k].demand);
      const bal = balance(S0, D0, C0);
      const C = bal.cost, S = bal.supply, D = bal.demand, m = S.length, n = D.length;
      const oracle = everyBasicSolution(C, S, D);
      const nw = northwest(C, S, D), lc = leastCost(C, S, D);
      solved[k] = { bal: bal, C: C, S: S, D: D, m: m, n: n, oracle: oracle, nw: nw, lc: lc };
      eq(oracle.feasible > 0, true, k + ': the enumeration finds at least one basic feasible solution');
      for (const start of [nw, lc]) {
        for (const rule of ['dantzig', 'bland']) {
          const run = modiRun(C, start, m, n, { rule: rule });
          const where = k + ' from the ' + start.rule + ' start under ' + rule;
          eq(run.capped, false, where + ': the iteration guard is never reached');
          eq(run.optimal, true, where + ': it stops because no empty cell prices below zero');
          eq(rt(run.cost), rt(oracle.best),
             where + ': and it stops at the cheapest of the ' + oracle.feasible
             + ' basic feasible solutions enumerated, ' + rt(oracle.best));
          /* the answer is a shipping plan, not just a number */
          let feasible = true;
          for (let i = 0; i < m; i += 1) {
            let t = R0;
            for (let j = 0; j < n; j += 1) { t = Radd(t, run.x[i][j]); if (Rsign(run.x[i][j]) < 0) feasible = false; }
            if (!Requ(t, S[i])) feasible = false;
          }
          for (let j = 0; j < n; j += 1) {
            let t = R0;
            for (let i = 0; i < m; i += 1) t = Radd(t, run.x[i][j]);
            if (!Requ(t, D[j])) feasible = false;
          }
          eq(feasible, true, where + ': every row sums to its supply, every column to its demand, nothing negative');
          eq(rt(tableauCost(C, run.x)), rt(run.cost),
             where + ': and the cost it reports is c.x recomputed from the plan it returns');
          /* the cost never rises; it may stand still, and on the default it does */
          let rose = 0;
          for (let q = 1; q < run.iterations.length; q += 1)
            if (Rcmp(run.iterations[q].cost, run.iterations[q - 1].cost) > 0) rose += 1;
          eq(rose, 0, where + ': and no iteration ever costs more than the one before it');
        }
      }
    }
    /* the figure the or_core section proves a different way */
    eq(rt(solved.balanced.oracle.best), '435',
       'the default preset costs 435 -- which is what the or_core section gets from the exact simplex through '
       + 'Phase I with equality rows, and what the enumeration of every spanning tree gets here');
    eq(solved.balanced.oracle.trees + ' of ' + (12 * 11 * 10 * 9 * 8 * 7) / (6 * 5 * 4 * 3 * 2), '432 of 924',
       'out of 924 six-cell subsets, 432 are spanning trees');
    eq(solved.balanced.oracle.feasible, 90, 'and 90 of those trees solve to a NON-NEGATIVE plan');
    eq(rt(solved.surplus.oracle.best), '605', 'the surplus preset, dummy and all, costs 605');
    eq(rt(solved.degenerate.oracle.best), '150', 'and the degenerate one 150');
    /* the two starts are genuinely different, which is what makes "both land on it" a claim */
    eq(rt(solved.balanced.nw.cost) + ' vs ' + rt(solved.balanced.lc.cost), '520 vs 475',
       'the north-west corner rule opens at 520 and the least-cost rule at 475');
    eq(rt(solved.surplus.nw.cost) + ' vs ' + rt(solved.surplus.lc.cost), '765 vs 665', 'on the surplus preset 765 and 665');
    eq(rt(solved.degenerate.nw.cost) + ' vs ' + rt(solved.degenerate.lc.cost), '240 vs 150',
       'and on the degenerate one 240 and 150, where the least-cost rule opens ON the optimum');
    /* the rule changes the path and not the answer */
    const counts = [];
    for (const start of ['nw', 'lc']) for (const rule of ['dantzig', 'bland'])
      counts.push(modiRun(solved.surplus.C, solved.surplus[start], 3, 4, { rule: rule }).iterations.length - 1);
    eq(counts.join(','), '3,4,3,6',
       'on the surplus preset Dantzig takes 3 pivots from either start where Bland takes 4 and 6 -- '
       + 'the entering rule moves the path and not the optimum');
    const uv0 = uvPotentials(solved.balanced.C, solved.balanced.nw.basis, 3, 4);
    eq(cn(pickEntering(uv0.reduced, solved.balanced.nw.basis, 3, 4, 'dantzig')) + ' at '
       + rt(pickEntering(uv0.reduced, solved.balanced.nw.basis, 3, 4, 'dantzig').value), '(3,1) at -9',
       'Dantzig takes the most negative reduced cost, (3,1) at -9');
    eq(cn(pickEntering(uv0.reduced, solved.balanced.nw.basis, 3, 4, 'bland')) + ' at '
       + rt(pickEntering(uv0.reduced, solved.balanced.nw.basis, 3, 4, 'bland').value), '(1,4) at -4',
       'and Bland the first negative one in row order, (1,4) at -4 -- a different cell on the same tableau');
    eq(pickEntering(modiRun(solved.balanced.C, solved.balanced.nw, 3, 4, {}).iterations[3].uv.reduced,
                    modiRun(solved.balanced.C, solved.balanced.nw, 3, 4, {}).iterations[3].basis, 3, 4, 'dantzig'),
       null, 'and on an optimal tableau neither rule finds anything, which is how the loop ends');
  }

  /* --- C4 L4: the cycle is a CYCLE, on every pivot of every run ----------- */
  {
    let pivots = 0, bad = [];
    for (const k of Object.keys(TP)) {
      const S = solved[k];
      for (const start of [S.nw, S.lc]) for (const rule of ['dantzig', 'bland']) {
        const run = modiRun(S.C, start, S.m, S.n, { rule: rule });
        for (const it of run.iterations) {
          if (!it.cycle || !it.cycle.found) continue;
          pivots += 1;
          const cs = it.cycle.cells, where = k + '/' + start.rule + '/' + rule;
          if (!it.check.ok) bad.push(where + ' checkCycle: ' + it.check.why);
          if (cs.length < 4 || cs.length % 2 !== 0) bad.push(where + ' length ' + cs.length);
          /* it CLOSES: corner to corner along a row, then a column, then back
             to the entering cell's own column. This is the defect the lesson
             cannot survive, so it is tested corner by corner and wraps. */
          for (let q = 0; q < cs.length; q += 1) {
            const next = cs[(q + 1) % cs.length];
            if (q % 2 === 0) { if (cs[q].i !== next.i) bad.push(where + ' corner ' + q + ' does not share a row'); }
            else if (cs[q].j !== next.j) bad.push(where + ' corner ' + q + ' does not share a column');
          }
          /* signs alternate from the entering cell outwards */
          for (let q = 0; q < cs.length; q += 1)
            if (cs[q].sign !== (q % 2 === 0 ? 1 : -1)) bad.push(where + ' corner ' + q + ' has the wrong sign');
          /* theta is the smallest allocation on a MINUS cell, and that cell leaves */
          let least = null;
          for (const c of cs) if (c.sign < 0 && (least === null || Rcmp(c.x, least) < 0)) least = c.x;
          if (!Requ(least, it.cycle.theta)) bad.push(where + ' theta is not the smallest minus allocation');
          if (it.cycle.leaving.sign >= 0) bad.push(where + ' the leaving cell is not a minus cell');
          if (!Requ(it.cycle.leaving.x, it.cycle.theta)) bad.push(where + ' the leaving cell does not attain theta');
          /* every corner after the entering one is occupied: a cycle may CROSS
             an empty cell and may only TURN at an occupied one */
          const occupied = {};
          for (const b of it.basis) occupied[b.i + ',' + b.j] = true;
          for (let q = 1; q < cs.length; q += 1)
            if (!occupied[cs[q].i + ',' + cs[q].j]) bad.push(where + ' turns at the empty cell ' + cn(cs[q]));
          if (!it.forest.spanning) bad.push(where + ' the basis is not a spanning tree');
        }
      }
    }
    eq(pivots, 30, 'twelve runs over the three presets take 30 pivots between them');
    eq(bad.join(' / '), '', 'and every one of their cycles closes, alternates, turns only where something is '
       + 'allocated, and hands theta to a minus cell that attains it');

    /* the default preset's first cycle is not a rectangle, which is the reason
       stoneCycle walks the forest instead of looking for one */
    const run = modiRun(solved.balanced.C, solved.balanced.nw, 3, 4, {});
    eq(run.iterations.length, 4, 'the default run is three pivots and a verdict');
    eq(run.iterations.map((it) => rt(it.cost)).join(' -> '), '520 -> 475 -> 475 -> 435',
       'costing 520, 475, 475 and 435 -- the middle pair EQUAL, because the second pivot is degenerate');
    eq(run.iterations[0].cycle.cells.length, 6, "the first pivot's cycle has SIX corners, not four");
    eq(run.iterations[0].cycle.cells.map((c) => cn(c) + (c.sign > 0 ? '+' : '-')).join(' '),
       '(3,1)+ (3,4)- (2,4)+ (2,2)- (1,2)+ (1,1)-',
       'running (3,1) (3,4) (2,4) (2,2) (1,2) (1,1) -- a staircase, which no rectangle search finds');
    eq(rt(run.iterations[0].cycle.theta) + ' at ' + cn(run.iterations[0].cycle.leaving), '5 at (2,2)',
       'theta is 5 and (2,2) leaves');
    eq(rt(run.iterations[1].cycle.theta) + ' at ' + cn(run.iterations[1].cycle.leaving), '0 at (1,1)',
       'the second pivot moves theta = 0 round its cycle, so the basis changes and the cost does not');
    eq(rt(run.iterations[2].cycle.theta) + ' at ' + cn(run.iterations[2].cycle.leaving), '10 at (2,4)',
       'and the third moves 10, which is what gets the last 40 off the bill');
    eq(run.x.map((r) => r.map(rt).join(',')).join(' | '), '0,5,0,10 | 0,10,15,0 | 5,0,0,5',
       'the plan it lands on ships nothing at all down five of the twelve routes');
    eq(rt(tableauCost(solved.balanced.C, run.x)), '435', 'and costs 435, priced from the plan rather than tracked');
    eq(modiRun(solved.balanced.C, solved.balanced.lc, 3, 4, {}).iterations.length, 2,
       'from the least-cost start the same tableau takes ONE pivot instead of three');

    /* checkCycle can refuse, and each refusal names the thing that broke */
    const basis = [{ i: 0, j: 1, x: ri(5) }, { i: 1, j: 1, x: ri(5) }, { i: 1, j: 0, x: ri(5) }];
    const square = [{ i: 0, j: 0, sign: 1 }, { i: 0, j: 1, sign: -1 }, { i: 1, j: 1, sign: 1 }, { i: 1, j: 0, sign: -1 }];
    eq(checkCycle(square, basis).ok, true, 'a legal four-corner cycle passes');
    eq(checkCycle(square, [{ i: 0, j: 1, x: ri(5) }, { i: 1, j: 1, x: ri(5) }]).ok, false,
       'the same path over a basis that does not occupy (2,1) does NOT');
    eq(checkCycle(square, [{ i: 0, j: 1, x: ri(5) }, { i: 1, j: 1, x: ri(5) }]).why.indexOf('turns at (2,1)') >= 0, true,
       'and the refusal names the corner it turned at, which is what the tableau rings');
    eq(checkCycle([{ i: 0, j: 0, sign: 1 }, { i: 0, j: 1, sign: 1 }, { i: 1, j: 1, sign: 1 }, { i: 1, j: 0, sign: -1 }],
                  basis).why.indexOf('wrong sign') >= 0, true, 'two pluses in a row is refused as a sign error');
    eq(checkCycle([{ i: 0, j: 0, sign: 1 }, { i: 0, j: 1, sign: -1 }, { i: 0, j: 2, sign: 1 }, { i: 1, j: 2, sign: -1 }],
                  [{ i: 0, j: 1, x: ri(1) }, { i: 0, j: 2, x: ri(1) }, { i: 1, j: 2, x: ri(1) }]).why.indexOf('row 1 has 3') >= 0,
       true, 'three corners in one row is refused: a cycle enters and leaves each row once');
    eq(checkCycle([{ i: 0, j: 0, sign: 1 }, { i: 0, j: 1, sign: -1 }], basis).why.indexOf('four corners') >= 0, true,
       'two corners is not a cycle');
    eq(checkCycle([{ i: 0, j: 0, sign: 1 }, { i: 0, j: 1, sign: -1 }, { i: 1, j: 1, sign: 1 },
                   { i: 1, j: 0, sign: -1 }, { i: 2, j: 0, sign: 1 }],
                  basis.concat([{ i: 2, j: 0, x: ri(1) }])).why.indexOf('even number') >= 0, true,
       'and an odd number of corners cannot alternate at all');

    /* basisForest, which is the reason any of the above is well defined */
    eq(basisForest(solved.balanced.nw.basis, 3, 4).spanning, true,
       'the six cells the north-west rule leaves are a spanning tree of three rows and four columns');
    const squareBasis = [{ i: 0, j: 0 }, { i: 0, j: 1 }, { i: 1, j: 0 }, { i: 1, j: 1 }];
    eq(basisForest(squareBasis, 2, 2).acyclic + ' ' + cn(basisForest(squareBasis, 2, 2).cycle), 'false (2,2)',
       'a full 2x2 block of basic cells holds a cycle, and the cell that closes it is named');
    eq(basisForest(squareBasis, 2, 2).why.indexOf('over-determined') > 0, true,
       'which is reported as the potentials being over-determined, not as a drawing problem');
    eq(basisForest([{ i: 0, j: 0 }, { i: 1, j: 1 }], 2, 2).components, 2,
       'two cells on a 2x2 leave the forest in two pieces');
    eq(basisForest([{ i: 0, j: 0 }, { i: 1, j: 1 }], 2, 2).why.indexOf('no stepping-stone cycle at all') > 0, true,
       'and then some empty cell has no cycle, which is exactly what the epsilon cell repairs');
  }

  /* --- C4 L3's note: degeneracy, and where the epsilon cell goes ---------- */
  {
    const D = solved.degenerate;
    eq(D.nw.count + ' of ' + D.nw.want, '5 of 5', 'on the ties preset the north-west rule still occupies m + n - 1 cells');
    eq(cells(D.nw.epsilon), '(2,1) (3,2)', 'two of which carry ZERO -- the named epsilon cells, not missing ones');
    eq(D.nw.degenerate, true, 'so the start is reported degenerate');
    eq(basisForest(D.nw.basis, 3, 3).spanning, true, 'while still being a spanning tree, which is the point of naming them');
    eq(D.lc.count + ' of ' + D.lc.want, '4 of 5', 'the least-cost rule on the same data leaves one cell SHORT');
    eq(basisForest(D.lc.basis, 3, 3).components, 2, 'so its basic cells fall into two pieces');
    eq(uvPotentials(D.C, D.lc.basis, 3, 3).connected, false,
       'and u + v = c cannot be solved at all: three of the six potentials never get a value');
    const pad = padBasis(D.lc.basis, 3, 3, D.C);
    eq(pad.count + ' of ' + pad.want, '5 of 5', 'padBasis restores the count');
    eq(cells(pad.added), '(1,1)', 'by placing a zero at (1,1)');
    eq(rt(pad.added[0].cost), '5', 'which costs 5');
    eq(pad.added.every((c) => Rcmp(c.cost, D.C[c.i][c.j]) === 0), true, 'and the cost it reports is the cell it chose');
    eq(basisForest(pad.basis, 3, 3).spanning, true, 'the padded basis is a spanning tree');
    eq(uvPotentials(D.C, pad.basis, 3, 3).connected, true, 'so the potentials are determined again');
    eq(pad.why.indexOf('joins two pieces') > 0, true,
       'and the reason given is that it joins two pieces, not that it was convenient');
    eq(padBasis(D.nw.basis, 3, 3, D.C).added.length, 0, 'a start that is already the right size gains nothing');
    eq(padBasis(D.nw.basis, 3, 3, D.C).why.indexOf('nothing was added') > 0, true, 'and says so');
    eq(modiRun(D.C, D.lc, 3, 3, {}).pad.added.length, 1, 'modiRun pads before it starts');
    eq(rt(modiRun(D.C, D.lc, 3, 3, {}).cost), '150', 'and reaches 150 from a basis that could not be priced');
    eq(cells(solved.balanced.lc.epsilon), '(2,2)',
       'the default preset ties too: the least-cost rule leaves a zero at (2,2) with the full count');
  }

  /* --- C4 L4's misconception: u1 = 0 is a NORMALISATION ------------------- */
  {
    const B = solved.balanced;
    const it0 = modiRun(B.C, B.nw, 3, 4, {}).iterations[0];
    eq(it0.uv.u.map(rt).join(',') + ' | ' + it0.uv.v.map(rt).join(','), '0,5,3 | 10,2,4,15',
       'solved with u1 = 0 the potentials are u = (0, 5, 3) and v = (10, 2, 4, 15)');
    const shifts = [];
    let moved = true, held = true;
    for (let a = 0; a < 3 + 4; a += 1) {
      const kind = a < 3 ? 'u' : 'v', at = a < 3 ? a : a - 3;
      const sh = shiftPotentials(it0.uv, B.C, kind, at);
      shifts.push(rt(sh.shift));
      if (!sh.same) held = false;
      if (!Rzero(sh.shift)) {
        for (let i = 0; i < 3; i += 1) if (Requ(sh.u[i], it0.uv.u[i])) moved = false;
        for (let j = 0; j < 4; j += 1) if (Requ(sh.v[j], it0.uv.v[j])) moved = false;
      }
      eq(rt(kind === 'u' ? sh.u[at] : sh.v[at]), '0', 'fixing ' + kind + (at + 1) + ' really does set it to zero');
    }
    eq(shifts.join(','), '0,5,3,-10,-2,-4,-15',
       'the seven normalisations shift the potentials by 0, 5, 3, -10, -2, -4 and -15');
    eq(moved, true, 'and where the shift is not zero EVERY u and EVERY v moves, none of them staying put');
    eq(held, true, 'while not one of the twelve reduced costs moves, which is what makes the choice a normalisation');
    eq(rt(shiftPotentials(it0.uv, B.C, 'u', 0).shift), '0',
       'fixing u1 shifts nothing, because that is the normalisation the potentials were solved with');
    eq(shiftPotentials(it0.uv, B.C, 'v', 4), null, 'there is no v5 on a four-column tableau');
    eq(shiftPotentials(it0.uv, B.C, 'u', -1), null, 'and no u0');
    eq(shiftPotentials(uvPotentials(solved.degenerate.C, solved.degenerate.lc.basis, 3, 3),
                       solved.degenerate.C, 'u', 0), null,
       'and potentials that were never determined cannot be renormalised, which is reported rather than shifted');
    /* u + v = c on the basic cells, at every iteration of the default run */
    let off = 0;
    for (const it of modiRun(B.C, B.nw, 3, 4, {}).iterations)
      for (const c of it.basis) if (!Requ(Radd(it.uv.u[c.i], it.uv.v[c.j]), B.C[c.i][c.j])) off += 1;
    eq(off, 0, 'and u_i + v_j = c_ij holds on every basic cell of every iteration');
  }

  /* --- C4 L3's misconception: pricing the dummy high --------------------- */
  {
    const S = solved.surplus, m = S.m, n = S.n, realRows = 3, realCols = 3;
    let big = S.C[0][0];
    for (let i = 0; i < realRows; i += 1) for (let j = 0; j < realCols; j += 1)
      if (Rcmp(S.C[i][j], big) > 0) big = S.C[i][j];
    eq(rt(big), '16', 'the dearest real route on the surplus preset costs 16');
    const pen = Rmul(big, ri(10));
    eq(rt(pen), '160', 'so the lab prices the dummy at ten times that, 160');
    const Cp = S.C.map((r) => r.slice());
    for (let i = 0; i < m; i += 1) Cp[i][n - 1] = pen;
    for (const which of ['nw', 'lc']) {
      const start = S[which], alt = which === 'lc' ? leastCost(Cp, S.S, S.D) : northwest(Cp, S.S, S.D);
      const penalised = modiRun(Cp, alt, m, n, {}).x;
      const bestZero = tableauCost(S.C, modiRun(S.C, start, m, n, {}).x, realRows, realCols);
      const bestPen = tableauCost(S.C, penalised, realRows, realCols);
      eq(rt(bestZero), '605', 'from the ' + start.rule + ' start the real shipping bill of the optimum is 605');
      eq(rt(bestPen), rt(bestZero),
         'and pricing the dummy at 160 does not move it -- every plan ships the same 10 to the dummy, '
         + 'so a uniform price adds a CONSTANT and the argmin cannot move');
      let toDummy = R0;
      for (let i = 0; i < m; i += 1) toDummy = Radd(toDummy, penalised[i][n - 1]);
      eq(rt(toDummy), '10', 'the penalised optimum still sends the whole surplus of 10 to the dummy, because it has nowhere else to go');
      eq(rt(tableauCost(Cp, penalised)), '2205',
         'so priced through the penalised table the plan reads 2205');
      eq(rt(tableauCost(Cp, penalised, realRows, realCols)), '605',
         'and it is the window over the real cells that gets the 1600 charge for goods that never move back off it');
    }
    const altLc = leastCost(Cp, S.S, S.D);
    eq(rt(tableauCost(S.C, S.lc.x, realRows, realCols)) + ' -> '
       + rt(tableauCost(S.C, altLc.x, realRows, realCols)), '665 -> 635',
       'the least-cost START does move, from 665 to 635, because it reads the cost table');
    const altNw = northwest(Cp, S.S, S.D);
    eq(rt(tableauCost(S.C, S.nw.x, realRows, realCols)) + ' -> '
       + rt(tableauCost(S.C, altNw.x, realRows, realCols)), '765 -> 765',
       'and the north-west start does not, because it never reads one');
    eq(rt(Rmul(pen, S.bal.amount)), '1600',
       'the constant a price of 160 adds is 1600 -- which is exactly the 2205 against the 605 above');
  }

  /* --- C4 L6: KOENIG, and the recipe that is not a function -------------- */
  {
    /* every vertex cover of the zero pattern, enumerated over all 2^(2n)
       selections of rows and columns. Nothing here knows about matchings. */
    const minCovers = (M) => {
      const n = M.length, zeros = [];
      for (let i = 0; i < n; i += 1) for (let j = 0; j < n; j += 1) if (Rzero(M[i][j])) zeros.push([i, j]);
      let size = 2 * n, found = [];
      for (let mask = 0; mask < (1 << (2 * n)); mask += 1) {
        let wide = 0;
        for (let b = 0; b < 2 * n; b += 1) if (mask & (1 << b)) wide += 1;
        if (wide > size) continue;
        let ok = true;
        for (const z of zeros) if (!((mask >> z[0]) & 1) && !((mask >> (n + z[1])) & 1)) { ok = false; break; }
        if (!ok) continue;
        if (wide < size) { size = wide; found = []; }
        const names = [];
        for (let b = 0; b < 2 * n; b += 1) if (mask & (1 << b)) names.push(b < n ? 'r' + (b + 1) : 'c' + (b - n + 1));
        found.push(names.join('+'));
      }
      return { size: size, covers: found, zeros: zeros.length };
    };
    /* the textbook eye test: cover whichever row or column holds the most
       still-uncovered zeros, and repeat. It has no tie-break, so it is run
       both ways. */
    const lineCover = (M, colsFirst) => {
      const n = M.length, rows = {}, cols = {};
      let lines = 0;
      const live = () => {
        const out = [];
        for (let i = 0; i < n; i += 1) for (let j = 0; j < n; j += 1)
          if (Rzero(M[i][j]) && !rows[i] && !cols[j]) out.push([i, j]);
        return out;
      };
      while (live().length) {
        let pickRow = -1, pickCol = -1, best = -1;
        const tryRows = () => {
          for (let i = 0; i < n; i += 1) {
            if (rows[i]) continue;
            let c = 0;
            for (const z of live()) if (z[0] === i) c += 1;
            if (c > best) { best = c; pickRow = i; pickCol = -1; }
          }
        };
        const tryCols = () => {
          for (let j = 0; j < n; j += 1) {
            if (cols[j]) continue;
            let c = 0;
            for (const z of live()) if (z[1] === j) c += 1;
            if (c > best) { best = c; pickCol = j; pickRow = -1; }
          }
        };
        if (colsFirst) { tryCols(); tryRows(); } else { tryRows(); tryCols(); }
        if (pickRow >= 0) rows[pickRow] = true; else cols[pickCol] = true;
        lines += 1;
      }
      return lines;
    };

    const matrices = { jobs: parseGrid(AP.jobs), sites: parseGrid(AP.sites), crews: parseGrid(AP.crews),
      tie: [[4, 2, 8], [4, 3, 7], [3, 1, 6]].map((r) => r.map(ri)),
      flat: [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]].map((r) => r.map(ri)),
      zero: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].map((r) => r.map(ri)),
      bands: [[5, 5, 5, 5], [1, 2, 3, 4], [4, 3, 2, 1], [5, 5, 5, 5]].map((r) => r.map(ri)),
      swap: [[7, 3], [3, 7]].map((r) => r.map(ri)) };
    let steps = 0, off = [];
    for (const k of Object.keys(matrices)) {
      const h = hungarian(matrices[k]);
      for (const s of h.steps) {
        if (s.kind !== 'cover') continue;
        steps += 1;
        const brute = minCovers(s.M);
        if (s.size !== s.matching.length) off.push(k + ': cover ' + s.size + ' vs matching ' + s.matching.length);
        if (s.size !== brute.size) off.push(k + ': cover ' + s.size + ' vs enumerated minimum ' + brute.size);
        if (s.cover.left.length + s.cover.right.length !== s.size) off.push(k + ': the cover does not have its own size');
        const check = coverCheck(s.M, s.cover);
        if (!check.ok) off.push(k + ': ' + check.missed.length + ' zeros escape the cover');
      }
    }
    eq(steps, 14, 'eight matrices reach 14 cover steps between them');
    eq(off.join(' / '), '', 'and at every one of them the minimum cover, the maximum matching and the smallest '
       + 'of all 2^(2n) row-and-column selections that covers every zero are THE SAME NUMBER -- Koenig, three ways');

    /* the recipe, on the kit's own default preset */
    const jobsH = hungarian(matrices.jobs);
    const stuck = jobsH.steps.filter((s) => s.kind === 'cover')[1];
    eq(stuck.M.map((r) => r.map(rt).join(',')).join(' | '), '0,4,1,2 | 0,3,0,4 | 2,0,1,0 | 1,3,0,4',
       'at the second cover step of the default assignment preset the reduced matrix holds six zeros');
    eq(minCovers(stuck.M).size, 3, 'and the minimum cover is 3');
    eq(minCovers(stuck.M).covers.join(' | '), 'r3+c1+c3', 'attained exactly one way: row 3, column 1 and column 3');
    eq(stuck.matching.length + ' ' + stuck.size, '3 3', 'which is what the matching and the cover both report');
    eq(lineCover(stuck.M, false), 4, 'covering the fullest line first, ties to ROWS, draws FOUR lines');
    eq(lineCover(stuck.M, true), 3, 'ties to COLUMNS, three -- the same rule on the same matrix, two answers');
    eq(lineCover(stuck.M, false) === matrices.jobs.length, true,
       'and four is n, so the rows-first reader stops and looks for a complete assignment among the zeros');
    eq(stuck.matching.length < matrices.jobs.length, true,
       'while the maximum matching is 3, so there is no complete assignment of zeros to find');
    const sitesStuck = hungarian(matrices.sites).steps.filter((s) => s.kind === 'cover')[1];
    eq(minCovers(sitesStuck.M).size + ' ' + lineCover(sitesStuck.M, false) + ' ' + lineCover(sitesStuck.M, true),
       '3 4 3', 'the sites preset does the same thing at the same step: minimum 3, recipe 4 or 3');
    eq(minCovers(sitesStuck.M).covers.join(' | '), 'r1+c1+c3', 'with its own unique minimum cover');

    /* coverCheck has to be able to fail, or it checks nothing */
    const empty = coverCheck(stuck.M, { left: [], right: [], size: 0 });
    eq(empty.ok + ' ' + empty.missed.length, 'false 6', 'covering nothing leaves all six zeros uncovered');
    const wrongRow = coverCheck(stuck.M, { left: ['r0'], right: ['c0', 'c2'], size: 3 });
    eq(wrongRow.ok, false,
       'and so is a THREE-line selection that is not the minimum one: row 1 instead of row 3');
    eq(wrongRow.missed.map(cn).join(','), '(3,2),(3,4)',
       'which names the two zeros that escape it rather than reporting a count that happens to be right');
  }

  /* --- C4 L6: the method against every permutation ----------------------- */
  {
    const exhaustive = (cost) => {
      const n = cost.length, used = [], perm = [];
      let best = null, bestPerm = null, count = 0, ties = 0;
      const walk = (k, z) => {
        if (k === n) {
          count += 1;
          if (best === null || Rcmp(z, best) < 0) { best = z; bestPerm = perm.slice(); ties = 1; }
          else if (Requ(z, best)) ties += 1;
          return;
        }
        for (let j = 0; j < n; j += 1) {
          if (used[j]) continue;
          used[j] = 1; perm.push(j);
          walk(k + 1, Radd(z, cost[k][j]));
          perm.pop(); used[j] = 0;
        }
      };
      walk(0, R0);
      return { best: best, perm: bestPerm, count: count, ties: ties };
    };
    const want = { jobs: '49', sites: '275', crews: '38' };
    const perms = { jobs: 24, sites: 24, crews: 120 };
    for (const k of Object.keys(AP)) {
      const cost = parseGrid(AP[k]), n = cost.length;
      const h = hungarian(cost), ex = exhaustive(cost);
      eq(ex.count, perms[k], k + ': there are ' + perms[k] + ' complete assignments of ' + n + ' workers');
      eq(h.complete, true, k + ': and the Hungarian method finds a whole one');
      eq(rt(h.value), rt(ex.best), k + ': worth exactly the cheapest of all ' + perms[k]);
      eq(rt(h.value), want[k], k + ': which is ' + want[k]);
      eq(new Set(h.assignment).size + ' ' + h.assignment.filter((j) => j < 0).length, n + ' 0',
         k + ': its assignment is a permutation, with nobody left out');
      let priced = R0;
      for (let i = 0; i < n; i += 1) priced = Radd(priced, cost[i][h.assignment[i]]);
      eq(rt(priced), rt(h.value), k + ': and the value it reports is that permutation priced from the cost table');
    }
    /* the VALUE is what is optimal, and on one preset the permutation is not unique */
    const sites = parseGrid(AP.sites);
    const hs = hungarian(sites), exs = exhaustive(sites);
    eq(exs.ties, 2, 'the sites preset has TWO optimal assignments');
    eq(hs.assignment.map((j) => j + 1).join(',') + ' vs ' + exs.perm.map((j) => j + 1).join(','),
       '4,3,2,1 vs 2,4,3,1',
       'and the two computations return different ones, so the claim is about the 275 and not about the permutation');
    eq(Requ(hs.value, exs.best), true, 'which they agree on');
    /* THE ARGUMENT FOR THE REDUCTIONS, over all 120 permutations rather than
       stated: taking a constant off a whole row or column moves EVERY complete
       assignment's cost by the same amount, so it cannot change which one is
       cheapest. The set of differences has to be a single number. */
    const crews = parseGrid(AP.crews);
    const hc = hungarian(crews);
    const reduced = hc.steps[1].M;
    let negatives = 0;
    for (let i = 0; i < 5; i += 1) for (let j = 0; j < 5; j += 1) if (Rsign(reduced[i][j]) < 0) negatives += 1;
    eq(negatives, 0, 'after both reductions no entry is negative, so the zeros really are the cheapest cells left');
    const taken = Radd(hc.steps[0].amounts.reduce(Radd, R0), hc.steps[1].amounts.reduce(Radd, R0));
    eq(rt(hc.steps[0].amounts.reduce(Radd, R0)) + ' + ' + rt(hc.steps[1].amounts.reduce(Radd, R0)), '35 + 2',
       'the five row minima add to 35 and the five column minima to 2');
    const spread = {};
    const seat = [];
    const both = (k, orig, red) => {
      if (k === 5) { spread[rt(Rsub(orig, red))] = true; return; }
      for (let j = 0; j < 5; j += 1) {
        if (seat[j]) continue;
        seat[j] = 1;
        both(k + 1, Radd(orig, crews[k][j]), Radd(red, reduced[k][j]));
        seat[j] = 0;
      }
    };
    both(0, R0, R0);
    eq(Object.keys(spread).join(','), '37',
       'and all 120 assignments are cheaper in the reduced matrix by the SAME 37 -- one difference, not a range, '
       + 'which is why the reductions cannot change the answer');
    eq(rt(taken), '37', 'which is exactly the total taken off');
    eq(rt(exhaustive(reduced).best) + ' + ' + rt(taken), '1 + 37',
       'the cheapest assignment in the reduced matrix costs 1, because the zeros there do not yet carry a whole one');
    eq(rt(Radd(exhaustive(reduced).best, taken)), rt(exhaustive(crews).best),
       'and 1 plus 37 is the answer in the original matrix, 38');
  }

  /* --- C4 L6's quantity: the dual, added up ------------------------------- */
  {
    const want = { jobs: '49', sites: '275', crews: '38' };
    const traces = { jobs: '32,46,46,47,47,49,49', sites: '245,250,250,270,270,275,275', crews: '35,37,37,38,38' };
    for (const k of Object.keys(AP)) {
      const cost = parseGrid(AP[k]), n = cost.length;
      const h = hungarian(cost), dual = assignDual(cost, h.reduced);
      eq(dual.consistent, true, k + ': u_i + v_j + M_ij = c_ij in every cell, which is what makes the recovery a recovery');
      eq(dual.feasible, true, k + ': and u_i + v_j <= c_ij everywhere, so the pair is dual FEASIBLE');
      eq(rt(dual.total), want[k], k + ': the row and column constants add to ' + want[k]);
      eq(rt(dual.total), rt(h.value), k + ': which is the cost of the assignment -- strong duality, on this instance');
      /* the dual objective climbs to the primal one and never dips */
      const trace = h.steps.map((s) => rt(assignDual(cost, s.M).total));
      eq(trace.join(','), traces[k], k + ': step by step the dual total goes ' + traces[k]);
      let dipped = 0;
      for (let q = 1; q < trace.length; q += 1)
        if (Rcmp(assignDual(cost, h.steps[q].M).total, assignDual(cost, h.steps[q - 1].M).total) < 0) dipped += 1;
      eq(dipped, 0, k + ': never dipping, which is why the method stops when the two numbers meet');
      let feasibleThroughout = true;
      for (const s of h.steps) if (!assignDual(cost, s.M).feasible || !assignDual(cost, s.M).consistent) feasibleThroughout = false;
      eq(feasibleThroughout, true, k + ': and the pair is feasible at every step, not only the last');
    }
    /* the recovery's own normalisation does not touch the total, because the
       matrix is square -- which is the claim assignDual's comment makes */
    const cost = parseGrid(AP.jobs), h = hungarian(cost), d = assignDual(cost, h.reduced);
    eq(d.u.map(rt).join(',') + ' | ' + d.v.map(rt).join(','), '10,10,9,11 | 0,7,-3,5',
       'the recovery fixes v1 = 0 and reads the rest off the final matrix');
    const t = ri(7);
    const u2 = d.u.map((x) => Radd(x, t)), v2 = d.v.map((x) => Rsub(x, t));
    let consistent = true;
    for (let i = 0; i < 4; i += 1) for (let j = 0; j < 4; j += 1)
      if (!Requ(Radd(Radd(u2[i], v2[j]), h.reduced[i][j]), cost[i][j])) consistent = false;
    eq(consistent, true, 'adding 7 to every u and taking it off every v is just as valid a recovery');
    eq(rt(sum(u2.concat(v2))), rt(d.total), 'and adds to the same 49, because a square matrix adds 4t and subtracts 4t');
  }

  /* --- C4 L6's lab: greed, with a number attached ------------------------- */
  {
    const gaps = { jobs: '1', sites: '40', crews: '0' };
    const values = { jobs: '50', sites: '315', crews: '38' };
    for (const k of Object.keys(AP)) {
      const cost = parseGrid(AP[k]), n = cost.length;
      const h = hungarian(cost), g = greedyAssign(cost);
      eq(g.complete, true, k + ': cheapest-cell-first does finish on a square matrix');
      eq(new Set(g.assignment).size, n, k + ': with a permutation');
      eq(rt(g.value), values[k], k + ': costing ' + values[k]);
      eq(rt(Rsub(g.value, h.value)), gaps[k], k + ': which is ' + gaps[k] + ' more than the optimum');
      eq(Rcmp(g.value, h.value) >= 0, true, k + ': greed is never below it, and that is the only thing it guarantees');
      let cheapest = cost[0][0];
      for (let i = 0; i < n; i += 1) for (let j = 0; j < n; j += 1) if (Rcmp(cost[i][j], cheapest) < 0) cheapest = cost[i][j];
      eq(rt(g.order[0].cost), rt(cheapest), k + ': and its first pick really is the cheapest cell in the table');
      let priced = R0;
      for (const o of g.order) priced = Radd(priced, o.cost);
      eq(rt(priced), rt(g.value), k + ': the value it reports is the picks it made, added up');
    }
    eq(cn(greedyAssign(parseGrid(AP.sites)).order[0]) + ' at ' + rt(greedyAssign(parseGrid(AP.sites)).order[0].cost),
       '(2,1) at 35', 'on the sites preset greed opens at (2,1) for 35');
    eq(rt(greedyAssign(parseGrid(AP.sites)).value) + ' against ' + rt(hungarian(parseGrid(AP.sites)).value),
       '315 against 275', 'and ends 40 over -- which is what "greedy loses badly here" is worth in money');
    eq(Rzero(Rsub(greedyAssign(parseGrid(AP.crews)).value, hungarian(parseGrid(AP.crews)).value)), true,
       'on the crews preset it happens to be right, and a lucky answer with no certificate is still not a method');
  }

  /* --- the rectangle a reader guesses, and where it breaks ---------------- */
  {
    const B = solved.balanced;
    const run = modiRun(B.C, B.nw, 3, 4, {});
    eq(run.iterations.map((it) => (it.rect === null ? '-' : (it.rect.ok ? 'closes'
        : 'refused ' + (it.rect.corner === null ? 'with no rectangle at all' : 'at ' + cn(it.rect.corner))))).join(' | '),
       'refused at (2,1) | closes | refused with no rectangle at all | -',
       'on the default view the guess is REFUSED FIRST and closes second -- transport.py\'s docstring has '
       + 'these two the other way round');
    /* where it names a corner, that corner really is empty */
    const occupied = {};
    for (const c of run.iterations[0].basis) occupied[c.i + ',' + c.j] = true;
    eq(occupied[run.iterations[0].rect.corner.i + ',' + run.iterations[0].rect.corner.j] === undefined, true,
       'and (2,1) carries no allocation, which is why the rectangle would turn on nothing');
    eq(run.iterations[0].rect.cells.length, 4, 'the refused guess is still drawn, as four corners');
    eq(run.iterations[0].cycle.cells.length, 6,
       'against the six the walk actually needs -- so the guess is the wrong SHAPE, not a differently drawn cycle');
    eq(run.iterations[0].rect.why.indexOf('is EMPTY') > 0, true, 'and the refusal says which corner was empty');
    eq(run.iterations[1].rect.why.indexOf('the guess') > 0 && run.iterations[1].rect.ok, true,
       'while on the second pivot the guess and the computed cycle agree, and the page says so');
    eq(modiRun(B.C, B.lc, 3, 4, {}).iterations[0].rect.ok, true,
       'from the least-cost start the one pivot it needs is a plain rectangle');
    const S = solved.surplus;
    eq(modiRun(S.C, S.nw, S.m, S.n, {}).iterations.slice(0, 3).every((it) => it.rect.ok), true,
       'and on the surplus preset all three of the north-west pivots are rectangles -- the guess is not always wrong, '
       + 'which is exactly why it has to be checked');
  }

  /* --- tableauCost, the window that prices the real cells only ----------- */
  {
    const C = [[ri(1), ri(10)], [ri(100), ri(1000)]], x = [[ri(1), ri(2)], [ri(3), ri(4)]];
    eq(rt(tableauCost(C, x)), '4321', 'with no window it prices the whole tableau');
    eq(rt(tableauCost(C, x, 1, null)), '21', 'a row window drops the dummy row');
    eq(rt(tableauCost(C, x, null, 1)), '301', 'a column window the dummy column');
    eq(rt(tableauCost(C, x, 1, 1)), '1', 'and both at once leaves one cell');
  }
}

// ==========================================================================
// Operations Research course five: the `integer` kit's own arithmetic
// ==========================================================================
//
// or_core's IP_JS is exercised above. This section is the twelve blocks the
// KIT adds on top of it -- the roundings, the encoding check, the covering
// atom, the big-M pricing, the tour heuristic, the cut loop and the drawing --
// every one a top-level function, so what runs here is the source that ships.
//
// THREE OF THESE ARE REGRESSION TESTS, and each one is a defect this kit
// actually had:
//
//   * the tour count quoted in the prose disagreed with what tspExact
//     enumerated on an asymmetric instance -- 360 against 720 -- so the count
//     and the enumeration are now held together on both kinds of matrix;
//   * the bound trace, re-derived from the finished node list, reported a
//     global bound of 54 on an instance whose integer optimum is 55, because
//     exploration order is not node order. It now reads bbTree's own record,
//     and the trace is required to be monotone in both directions;
//   * ipIneqText printed "yx1" on a mode whose variables are not binaries.
console.log('operations research: the integer kit');
{
  const OR_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const IK_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'integer.py');
  const SYS_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_systems.py');
  const orSrc = fs.readFileSync(OR_SOURCE, 'utf8');
  const ikSrc = fs.readFileSync(IK_SOURCE, 'utf8');
  const sysSrc = fs.readFileSync(SYS_SOURCE, 'utf8');
  const orBlock = (n) => blockFrom(orSrc, n, OR_SOURCE);
  const ikBlock = (n) => blockFrom(ikSrc, n, IK_SOURCE);
  const sysBlock = (n) => blockFrom(sysSrc, n, SYS_SOURCE);

  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
     + sysBlock('FEAS_JS') + logicBlock('PARSER_JS')
     + orBlock('ORFMT_JS') + orBlock('TABLEAU_JS') + orBlock('PHASE_JS') + orBlock('DUAL_JS')
     + orBlock('RANGE_JS') + orBlock('IP_JS')
     + ikBlock('IPBASE_JS') + ikBlock('IPMODEL_JS') + ikBlock('IPINEQ_JS') + ikBlock('IPCOVER_JS')
     + ikBlock('IPFIX_JS') + ikBlock('IPDISJ_JS') + ikBlock('IPTOUR_JS') + ikBlock('IPCUT_JS')
     + ikBlock('IPLAT_JS') + ikBlock('IPTREE_JS') + ikBlock('IPPLOT_JS') + ikBlock('IPBARS_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rows = (m) => m.map((r) => r.map(ri));

  /* --- the lattice mode: three numbers whose ORDER is the lesson ---------- */
  {
    const model = ipTwoVar(true, 3, 4, [[2, 1, 'le', 6, 'assembly'], [2, 3, 'le', 9, 'finishing']]);
    const lp = lpSolve(model);
    eq(Rtext(lp.zOrig), '51/4', 'the relaxation stops at 51/4');
    eq(Rtext(lp.x[0]) + ', ' + Rtext(lp.x[1]), '9/4, 3/2', 'at a corner fractional in BOTH variables');
    const rr = ipRoundings(lp.x);
    eq(rr.length, 4, 'which has FOUR roundings, not one -- there is no such thing as "the" rounding');
    eq(rr.map((r) => r.pt.map(Rtext).join('')).join(' '), '21 22 31 32', 'floor and ceiling in every combination');
    const verdicts = rr.map((r) => ipViolated(model, r.pt));
    eq(verdicts.filter((v) => v === null).length, 1, 'exactly one of the four is even feasible');
    eq(verdicts[1].indexOf('finishing'), 0, 'and an infeasible one NAMES the row it breaks');
    const lat = latticePoints(model, [[0n, 5n], [0n, 4n]]);
    eq(Rtext(lat.best.objective), '12', 'the integer optimum is 12');
    eq(Rtext(lat.best.x[0]) + ', ' + Rtext(lat.best.x[1]), '0, 3',
       'at (0, 3), which is the far corner of the region from the relaxation -- this is the opening preset, and the misconception it exists to break');
    eq(Rtext(ipObjective(model, rr[0].pt)), '10', 'while the best feasible rounding is worth only 10');
    eq(Rcmp(lp.zOrig, lat.best.objective) > 0 && Rcmp(lat.best.objective, ipObjective(model, rr[0].pt)) > 0, true,
       'z_LP > z_IP > z_rounded, which is the whole of the first lesson');
    /* one coordinate already whole: two roundings, not four */
    eq(ipRoundings([R(7n, 2n), ri(3)]).length, 2, 'a coordinate that is already whole is not rounded twice');
  }

  /* --- the encoding check: a wrong encoding is refuted by a ROW ----------- */
  {
    const names = ['A', 'B', 'C'];
    const right = ipEncodingCheck('A -> B', 'yA - yB <= 0', names);
    eq(right.rows.length, 8, 'three binaries is eight assignments');
    eq(right.valid, true, 'yA <= yB encodes "if A then B"');
    const wrong = ipEncodingCheck('A -> B', 'yB - yA <= 0', names);
    eq(wrong.valid, false, 'and the converse does NOT');
    eq(wrong.witness.bits[0] + '' + wrong.witness.bits[1], '10',
       'refuted at yA = 1, yB = 0 -- the row the lesson names, and the row a reader remembers');
    eq(wrong.witness.condition === false && wrong.witness.inequality === true, true,
       'where the condition fails and the inequality holds, which is what permits doing A without B');
    eq(ipEncodingCheck('A & B', 'yA + yB >= 2', names).valid, true, '"both" is yA + yB >= 2');
    eq(ipEncodingCheck('A & B', 'yA + yB >= 1', names).valid, false, 'and not yA + yB >= 1');
    eq(ipEncodingCheck('(A & !B & !C) | (!A & B & !C) | (!A & !B & C)', 'yA + yB + yC = 1', names).valid, true,
       '"exactly one" is an equality');
    eq(ipEncodingCheck('(A & !B & !C) | (!A & B & !C) | (!A & !B & C)', 'yA + yB + yC <= 1', names).valid, false,
       'and <= 1 is "at most one", which the all-zero row separates');
    /* fractions, and reader input that is not an inequality at all */
    const frac = ipIneq('1/2 yA + 1/2 yB >= 1', names, 'y');
    eq(Rtext(frac.a[0]) + ' ' + frac.rel + ' ' + Rtext(frac.b), '1/2 >= 1', 'coefficients may be fractions');
    eq(ipIneqHolds(frac, [1, 1, 0]) && !ipIneqHolds(frac, [1, 0, 0]), true, 'and they are compared exactly');
    eq(ipIneq('hello', names, 'y').error !== undefined, true, 'text with no relation is refused, not thrown on');
    eq(ipIneq('yD <= 1', names, 'y').error !== undefined, true, 'and so is a variable that does not exist');
    eq(ipIneqText(ipIneq('yA - yB <= 0', names, 'y')), 'yA - yB &lt;= 0',
       'a coefficient of one is not written, and a negative one is a minus sign');
    eq(ipIneqText(ipIneq('x1 + x2 <= 4', ['x1', 'x2'])), 'x1 + x2 &lt;= 4',
       'and the prefix belongs to the caller: this mode has no binaries, so nothing prints "yx1"');
  }

  /* --- covering: `>= 1` and `= 1` are not the same problem ---------------- */
  {
    const inc = [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]];
    const cost = [2, 2, 2, 2, 2].map(ri);
    const lp = lpSolve(ipCoverModel(inc, cost, 'ge'));
    eq(Rtext(lp.zOrig), '5', 'the covering relaxation on an odd ring is worth 5');
    eq(lp.x.slice(0, 5).every((v) => Requ(v, R(1n, 2n))), true,
       'and it gets there by spreading a half across every set, which is the shape of a covering relaxation');
    const exact = ipCoverExact(inc, cost, 'ge');
    eq(Rtext(exact.value), '6', 'the cheapest whole cover costs 6');
    eq(Rtext(ipCoverGreedy(inc, cost).value), '6', 'and greed happens to find it here');
    eq(exact.count, 32, 'over all 32 subsets');
    eq(ipCoverExact(inc, cost, 'eq').value, null,
       'covering exactly once is INFEASIBLE on the same instance -- which is why covering and partitioning are two problems');
    eq(Rcmp(lp.zOrig, exact.value) < 0, true, 'and the relaxation is a bound, strictly below the answer');
    const missing = ipCoverGreedy([[0, 0]], [ri(1), ri(1)]);
    eq(missing.feasible, false, 'a requirement nothing covers is reported rather than silently dropped');
  }

  /* --- the big-M, and what a loose one costs ------------------------------ */
  {
    const spec = { fixed: [ri(200), ri(60)], unit: [ri(2), ri(6)], cap: [ri(40), ri(40)], demand: ri(30) };
    const tight = ipTightM(spec);
    eq(Rtext(tight.M), '30', 'the tightest valid M is the smaller of the largest capacity and the whole demand');
    eq(tight.why.indexOf('total demand is 30') >= 0, true, 'and it comes with the reason, not just the number');
    eq(Rtext(ipBound(spec, tight.M)), '240', 'at the tightest M the bound is 240');
    const ints = [2, 3];
    const tree = bbTree(ipFixedCharge(spec, tight.M), { integers: ints, maxNodes: 30 });
    eq(Rtext(tree.best), '240', 'which is the integer answer itself, so the tree closes at once');
    eq(tree.counts.explored, 1, 'in one node');
    const loose = Rmul(tight.M, ri(20));
    eq(Rtext(ipBound(spec, loose)), '70', 'at twenty times that M the bound collapses to 70');
    const looseTree = bbTree(ipFixedCharge(spec, loose), { integers: ints, maxNodes: 30 });
    eq(Rtext(looseTree.best), '240', 'for the same integer answer');
    eq(looseTree.counts.explored > tree.counts.explored, true,
       'and more nodes to prove it -- the measured price of being careless about M');
    const y = ipFractionalY(ipFixedCharge(spec, loose), lpSolve(ipFixedCharge(spec, loose)).x);
    eq(Rtext(y[0]), '1/20', 'because the relaxation buys y = x/M, opening a facility for a twentieth of its fixed cost');
    const breaks = ipMBreaks(spec, tight.M, Rmul(tight.M, ri(40)));
    eq(breaks.length, 1, 'this instance has exactly one breakpoint above the tightest M');
    eq(Rtext(breaks[0].M), '35', 'at M = 35, where 2 + 200/M and 6 + 60/M cross');
    eq(Rtext(breaks[0].z), '1620/7', 'and the bound there is exactly 1620/7');
    eq(Requ(ipBound(spec, ri(35)), breaks[0].z), true, 'which lpSolve agrees with, since that is how it was checked');
    /* equal fixed costs never cross, so there is no bend to find */
    const flat = { fixed: [ri(150), ri(150)], unit: [ri(3), ri(5)], cap: [ri(50), ri(50)], demand: ri(45) };
    eq(ipMBreaks(flat, ipTightM(flat).M, ri(2000)).length, 0,
       'and equal fixed costs give no breakpoint at all rather than a spurious one');
  }

  /* --- either-or: writing both rows is the conjunction -------------------- */
  {
    const spec = { names: ['x1', 'x2'], max: false, obj: [R1, R1],
      A: [R1, R(-1n, 1n), ri(-4)], nameA: 'one before two',
      B: [R(-1n, 1n), R1, ri(-3)], nameB: 'two before one',
      both: [[R1, R0, ri(10), 'le', 'deadline one'], [R0, R1, ri(10), 'le', 'deadline two']],
      p1: ri(4), p2: ri(3), d1: ri(10), d2: ri(10) };
    const MA = ri(14), MB = ri(13);
    const one = lpSolve(ipDisjunction(spec, MA, MB, 1));
    const zero = lpSolve(ipDisjunction(spec, MA, MB, 0));
    eq(one.status + ' ' + Rtext(one.zOrig), 'optimal 4', 'fixing y = 1 gives a real schedule worth 4');
    eq(zero.status + ' ' + Rtext(zero.zOrig), 'optimal 3', 'fixing y = 0 gives the other one, worth 3');
    const free = lpSolve(ipDisjunction(spec, MA, MB, null));
    eq(Rint(free.x[2]), false, 'left continuous, the binary comes back FRACTIONAL');
    eq(Rtext(free.x[0]) + ', ' + Rtext(free.x[1]), '0, 0',
       'and both jobs start at the same moment on one machine, which is not a schedule');
    eq(Rcmp(free.zOrig, zero.zOrig) < 0, true, 'so its value is a bound and strictly below either real branch');
    const conj = { max: false, names: ['x1', 'x2'], obj: [R1, R1],
      cons: [{ a: [spec.A[0], spec.A[1]], rel: 'le', b: spec.A[2], name: 'A' },
             { a: [spec.B[0], spec.B[1]], rel: 'le', b: spec.B[2], name: 'B' }] };
    eq(lpSolve(conj).status, 'infeasible',
       'and writing BOTH rows is infeasible: 0 <= -7, which is the mistake the mode exists to show');
    const region = ipBranchRegion(spec, 1, MA, MB);
    eq(Ccorners(region).length >= 3, true, 'each branch still has a region to draw');
    eq(Cholds(region[0], ri(0), ri(4)), true, 'containing the schedule that branch actually chooses');
    eq(Cholds(region[0], ri(3), ri(0)), false, 'and not the other branch\'s');
  }

  /* --- the tour counts, and a heuristic with a number attached ------------ */
  {
    const sym = rows([[0, 32, 40, 32, 8, 40, 32], [32, 0, 24, 16, 32, 24, 32], [40, 24, 0, 16, 8, 16, 40],
                      [32, 16, 16, 0, 40, 8, 24], [8, 32, 8, 40, 0, 16, 32], [40, 24, 16, 8, 16, 0, 8],
                      [32, 32, 40, 24, 32, 8, 0]]);
    const counts = ipTourCount(7, true);
    eq(String(counts.tours), '360', 'seven cities have 360 DISTINCT UNDIRECTED tours');
    eq(String(counts.perms), '5040', 'not 5040, which counts permutations of the cities');
    eq(String(counts.halfPerms), '2520', 'not 2520 = 7!/2');
    eq(String(counts.directed), '720', 'and not 720 = (n-1)!, which counts each tour once per direction');
    eq(counts.formula, '(n - 1)! / 2', 'the page quotes the formula it computed from');
    const exact = tspExact(sym, { maxCities: 7 });
    eq(exact.count, 360, 'and tspExact enumerates exactly that many, so the prose cannot drift from the enumeration');
    eq(String(ipTourCount(7, false).tours), '720',
       'on an ASYMMETRIC matrix a tour and its reversal are different, so the count is (n-1)!');
    const asym = rows([[0, 3, 93, 13, 33, 9, 20], [4, 0, 77, 42, 21, 16, 30], [45, 17, 0, 36, 16, 28, 50],
                       [39, 90, 80, 0, 56, 7, 44], [28, 46, 88, 33, 0, 25, 17], [3, 88, 18, 46, 92, 0, 11],
                       [22, 35, 41, 19, 27, 14, 0]]);
    eq(tspExact(asym, { maxCities: 7 }).count, Number(ipTourCount(7, false).tours),
       'and there too the quoted count is what was enumerated');
    eq(Rtext(exact.best.cost), '104', 'the optimal tour on the symmetric instance costs 104');
    const nn = ipNearest(sym), opt = ipTwoOpt(sym);
    eq(nn.tour.length, 8, 'nearest neighbour returns a closed tour through every city');
    eq(new Set(nn.tour).size, 7, 'visiting each exactly once');
    eq(nn.tour[0] === 0 && nn.tour[7] === 0, true, 'starting and ending at the first city');
    eq(Rcmp(opt.cost, nn.cost) <= 0, true, '2-opt never leaves a tour worse than it found it');
    eq(Rtext(opt.cost), '112', 'and on this instance it stops at 112');
    eq(Rtext(ipTourCost(sym, opt.tour)), Rtext(opt.cost), 'the cost it reports is the cost of the tour it returns');
    const gap = ipGap(exact.best.cost, opt.cost, false);
    eq(Rtext(gap.abs), '8', 'so the MEASURED gap is 8');
    eq(Rpct(gap.rel, 2), '7.14%',
       'which is 8/112 -- measured against the incumbent, the value in hand, which is the convention every solver reports and the only one defined before the optimum is known');
    eq(gap.closed, false, 'and it is not closed');
    eq(ipGap(ri(5), ri(5), true).closed, true, 'a gap of zero IS closed, and that is the only proof there is');
    eq(ipGap(null, ri(5), true).proved.indexOf('nothing is proved') >= 0, true,
       'with no bound, nothing is proved, and the page says so rather than printing a dash');
  }

  /* --- cuts, and what validity actually means ----------------------------- */
  {
    const model = ipTwoVar(true, 1, 1, [[2, 5, 'le', 16, 'kiln'], [6, 5, 'le', 30, 'glaze']]);
    const lat = latticePoints(model, [[0n, 6n], [0n, 4n]]);
    eq(ipFracRows(lpSolve(model).tab).length > 0, true, 'the relaxation leaves a fractional row to cut from');
    const run = ipCutRounds(model, 6, 0);
    eq(run.integral, true, 'cutting repeatedly drives the relaxation to a whole point');
    eq(Rtext(run.z), '5', 'worth 5');
    eq(Rtext(run.z), Rtext(lat.best.objective), 'which is the integer optimum the lattice found');
    eq(run.steps.length <= 6 && run.steps.length >= 1, true, 'in at most the rounds asked for');
    let killed = 0;
    for (const st of run.steps) {
      const check = ipCutValid({ a: st.cut.inOriginal.a, b: st.cut.inOriginal.b, rel: '>=' }, lat.points);
      killed += check.killed.length;
    }
    eq(killed, 0, 'and NO cut removed a single feasible integer point, which is the only thing validity means');
    /* the first cut must exclude the point it was derived at */
    const first = run.steps[0].cut.inOriginal, start = run.start.x;
    let at = R0;
    for (let j = 0; j < 2; j += 1) at = Radd(at, Rmul(first.a[j], start[j]));
    eq(Rcmp(at, first.b) < 0, true, 'while the first cut does exclude the fractional optimum it was derived at');
    /* an invalid cut names the lattice point it killed */
    const bad = ipIneq('x1 + x2 <= 4', model.names);
    const check = ipCutValid({ a: bad.a, b: bad.b, rel: bad.rel }, lat.points);
    eq(check.valid, false, 'a cut that merely removes the fractional optimum is not valid');
    eq(Rtext(check.killed[0].x[0]) + ', ' + Rtext(check.killed[0].x[1]), '3, 2',
       'and the lattice point it killed is named rather than argued about');
    eq(ipAllInt([ri(2), R(1n, 2n)]), false, 'a point with one fractional coordinate is not whole');
  }

  /* --- the bound trace: monotone, and honest about exploration order ------ */
  {
    const model = ipTwoVar(true, 9, 5, [[7, 4, 'le', 43, 'press'], [4, 9, 'le', 47, 'anneal']]);
    const lat = latticePoints(model, [[0n, 7n], [0n, 6n]]);
    for (const order of ['depthFirst', 'bestBound']) {
      const tree = bbTree(model, { order: order, maxNodes: 60 });
      eq(Requ(tree.best, lat.best.objective), true,
         'branch and bound under ' + order + ' finds the lattice optimum, ' + Rtext(lat.best.objective));
      const trace = ipBoundTrace(tree, true);
      let ok = true;
      for (let i = 1; i < trace.length; i += 1) {
        if (trace[i].bound !== null && trace[i - 1].bound !== null && Rcmp(trace[i].bound, trace[i - 1].bound) > 0) ok = false;
        if (trace[i].incumbent !== null && trace[i - 1].incumbent !== null && Rcmp(trace[i].incumbent, trace[i - 1].incumbent) < 0) ok = false;
      }
      eq(ok, true, 'and the trace under ' + order + ' never raises its bound or lowers its incumbent');
      const last = trace[trace.length - 1];
      eq(Requ(last.bound, tree.best) && Requ(last.incumbent, tree.best), true,
         'a tree that closed ends with bound and incumbent equal, so the gap is nought and that is the proof');
      let everBelow = false;
      for (const step of trace) if (step.bound !== null && Rcmp(step.bound, tree.best) < 0) everBelow = true;
      eq(everBelow, false,
         'and NO step ever claims a bound below the true optimum -- the defect this trace was rewritten to fix');
    }
    eq(ipOpen({ prunedBy: null, bound: R1, children: [] }), true, 'a node never expanded is open');
    eq(ipOpen({ prunedBy: null, bound: R1, children: [3, 4] }), false, 'one that was branched is not');
    eq(ipOpen({ prunedBy: 'bound', bound: R1, children: [] }), false, 'and one that was pruned is not');
  }

  /* --- the drawing, which returns a string and touches no document -------- */
  {
    const model = ipTwoVar(true, 3, 4, [[2, 1, 'le', 6, 'assembly'], [2, 3, 'le', 9, 'finishing']]);
    const cons = ipHalfPlanes(model);
    eq(cons.length, 4, 'a two-row model is four half-planes once x >= 0 and y >= 0 are added');
    const poly = ipPolygon(cons);
    eq(poly.length, 4, 'whose region has four corners');
    let wound = true;
    for (let i = 1; i < poly.length; i += 1) {
      const a = Math.atan2(poly[i].y - 1.3, poly[i].x - 1.3), b = Math.atan2(poly[i - 1].y - 1.3, poly[i - 1].x - 1.3);
      if (a < b) wound = false;
    }
    eq(wound, true, 'returned in polygon order rather than sorted by x, or the shape would be a bow tie');
    const lat = latticePoints(model, [[0n, 5n], [0n, 4n]]);
    const svg = ipLattice({ cons: cons, box: [[0, 5], [0, 4]], points: lat.points, width: 520, height: 300,
                            marks: [{ x: R(9n, 4n), y: R(3n, 2n), tone: 'amber', shape: 'cross', label: 'LP' }],
                            lines: [{ a: R(-1n, 1n), b: R(-1n, 1n), c: ri(-4), tone: 'red', label: 'cut' }],
                            names: model.names });
    eq((svg.match(/<circle /g) || []).length, lat.points.length,
       'the lattice draws one dot per integer point and no more');
    eq((svg.match(/<polygon /g) || []).length, 1, 'with the region as a single polygon');
    eq((svg.match(/<path /g) || []).length, 1, 'the marked point as a cross');
    eq(svg.indexOf('stroke-dasharray') > 0, true, 'and the extra half-plane dashed, so a cut reads as a cut');
    const tree = bbTree(model, { maxNodes: 60 });
    const drawn = ipTreeSvg(tree.nodes, { width: 660, top: (n) => Rtext(n.bound === null ? R0 : n.bound) });
    eq((drawn.svg.match(/<rect /g) || []).length, tree.nodes.length, 'the tree draws one box per node');
    eq((drawn.svg.match(/<line /g) || []).length, tree.nodes.length - 1, 'and one edge per node but the root');
    const plot = ipPlot([{ pts: [[0, 5], [1, 4], [2, 4]], tone: 'amber', step: true, dots: true }],
                        { width: 660, height: 240 });
    eq((plot.svg.match(/<circle /g) || []).length, 3, 'the plot marks every sample');
    const bars = ipBars([{ label: 'a', value: ri(10), tone: 'amber' }, { label: 'b', value: ri(5), tone: 'green' }],
                        { width: 660 });
    eq((bars.svg.match(/<rect /g) || []).length, 2, 'and the bars draw one bar each');
    const ring = ipTourSvg(5, [{ tour: [0, 1, 2, 3, 4, 0], tone: 'green' }], { width: 660, height: 260 });
    eq((ring.svg.match(/<circle /g) || []).length, 5, 'the tour picture draws every city');
    eq(ipEsc('a < b & c'), 'a &lt; b &amp; c', 'and reader text is escaped before it reaches innerHTML');
  }
}



// ----------------------------------------------- the seqkit and heap kits
console.log('algorithms: the sequences and heap kits, and the two reuse claims that were false');
{
  /* The two kits built on SEQ_JS and HEAP_JS, tested on the concatenation they
     actually ship rather than on a block in isolation -- which is the only way
     to catch a kit that depends on a function its page does not carry.

     Three things here are worth more than the rest. First, the two KIT-LOCAL
     re-runs are pinned to the shipped routines they stand in for: heap's
     `insertionSortRun` must make exactly the comparisons `ALGO_JS.insertionSort`
     makes (it exists only because that one throws the sorted array away, which
     the design assumed it did not), and `heapsortTagged` must agree with
     `heapsortRun` on comparisons AND swaps. A re-run that drifted would be
     caught by the count long before it could be caught by the output.

     Second, seqkit's `twoStackState` DERIVES the two stacks from the trace
     rather than replaying the queue, so it is checked against an independent
     model of the same queue at every prefix of five sequences.

     Third, the drawings: every one returns its markup and is called here with a
     null element, which is the rule the shared core was restructured around. */
  const seqkitSrc = fs.readFileSync(path.join(__dirname, 'mathpath', 'labs', 'seqkit.py'), 'utf8');
  const heapkitSrc = fs.readFileSync(path.join(__dirname, 'mathpath', 'labs', 'heap.py'), 'utf8');
  eval(block('RATIONAL_JS'));
  eval(algoBlock('ALGO_JS'));
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('SERIES_JS'));
  eval(algoCoreBlock('TREEDRAW_JS'));
  eval(algoCoreBlock('SEQ_JS'));
  eval(algoCoreBlock('HEAP_JS'));
  eval(blockFrom(seqkitSrc, 'SEQKIT_JS', 'scripts/mathpath/labs/seqkit.py'));
  eval(blockFrom(heapkitSrc, 'HEAPKIT_JS', 'scripts/mathpath/labs/heap.py'));

  /* ------------------------------------------------ seqkit: the cost model */
  {
    eq(seqCompare([{ op: 'insertFront' }], 8).rows[0].array + ','
       + seqCompare([{ op: 'insertFront' }], 8).rows[0].list, '9,1',
       'inserting at the front shifts 8 elements and splices 1 node -- 9 against 1');
    eq(seqCompare([{ op: 'index', at: 7 }], 8).rows[0].array + ','
       + seqCompare([{ op: 'index', at: 7 }], 8).rows[0].list, '1,8',
       'and reaching index 7 costs the array 1 and the list 8 hops: the mirror image');
    const four = seqExpand(['index', 'insertFront', 'insertEnd', 'deleteAt'], 4, 16, 50);
    eq(four.length, 16, 'four rounds of four operations expand to sixteen');
    eq(seqExpand(['deleteAt', 'deleteAt'], 3, 1, 50).length, 0,
       'and a delete on a structure of one is DROPPED, not counted free');
    const cmp = seqCompare(four, 16);
    eq(cmp.decidedBy.op, 'insertFront', 'the front insertions decide this sequence');
    eq(cmp.arrayTotal + ',' + cmp.listTotal, '122,92', 'at a measured 122 against 92');
    eq(Rtext(cmp.ratio), '61/46', 'a ratio of two counts, exact');
  }
  {
    const p = twoStackParse('EE d x E,D', 28);
    eq(p.ops.length + '|' + p.ignored.join('') + '|' + p.ops.map((o) => o.key || 0).join(','),
       '5|x|1,2,0,3,0', 'the reader’s letters parse, keys number in enqueue order, x is reported');
    eq(twoStackParse('e'.repeat(40), 28).truncated, true, 'and a sequence past the cap says so');
    /* The two stacks are DERIVED from the trace. An independent model of the same
       queue is the only way to know the derivation is right -- and it has to
       check WHERE the split falls, not only which elements are held: any split
       of the right elements concatenates back to the right queue, so a
       derivation off by one step would pass a weaker test. */
    const replayTwoStacks = (ops, upto) => {
      const inS = [], outS = [];
      for (let i = 0; i <= upto; i += 1) {
        if (ops[i].op === 'enqueue') { inS.push(ops[i].key); continue; }
        if (!outS.length) while (inS.length) outS.push(inS.pop());
        if (outS.length) outS.pop();
      }
      return { out: outS.slice().reverse(), in: inS.slice() };
    };
    ['EEEDDD', 'EDEDEDED', 'EEDEEDEEDDDD', 'DDEEDD', 'EEEEEEDDDDDD'].forEach(function (text) {
      const ops = twoStackParse(text, 28).ops;
      const run = twoStackRun(ops);
      let bad = 0;
      for (let upto = 0; upto < ops.length; upto += 1) {
        const st = twoStackState(run, upto);
        const held = st.outStack.concat(st.inStack).map((e) => e.key);
        const served = run.trace.slice(0, upto + 1)
          .filter((t) => t.took !== null && t.took !== undefined).map((t) => t.took);
        const enq = run.trace.slice(0, upto + 1).filter((t) => t.op === 'enqueue').map((t) => t.key);
        const want = enq.filter((k) => served.indexOf(k) < 0);
        if (held.join(',') !== want.join(',')) bad += 1;
        if (st.lastTransfer >= 0 && st.lastTransfer === upto && st.inStack.length) bad += 1;
        const model = replayTwoStacks(ops, upto);
        if (st.outStack.map((e) => e.key).join(',') !== model.out.join(',')) bad += 1;
        if (st.inStack.map((e) => e.key).join(',') !== model.in.join(',')) bad += 1;
      }
      eq(bad, 0, 'the stacks derived from the trace of ' + text + ' are the ones an '
         + 'independent replay of the same queue holds, stack by stack, at every step');
    });
    const r = twoStackRun(twoStackParse('EEEDDD', 28).ops);
    eq(r.result.total + ',' + r.result.bound, '9,9', 'three in and three out costs 9 against a 3m of 9');
  }
  {
    const n = 12, ops = ufSequence('chain', n);
    eq(ops.length, n - 1 + n, 'the chain issues n - 1 unions and then finds every element');
    const rows = ufAllRules(ops, n);
    eq(rows.map((r) => (r.rank ? 'r' : '-') + (r.compress ? 'c' : '-')).join(' '), '-- r- -c rc',
       'all four combinations of the two rules are run on the same sequence');
    eq(rows[0].worst, n - 1, 'with neither rule the chain is a path and the worst find walks 11');
    eq(rows[0].holds, false,
       'so the 2^r bound does not hold -- it is a claim about union BY RANK and there is no rank rule');
    eq(rows[1].maxRank + ',' + rows[1].holds, '1,true', 'with the rank rule the chain is flat, and it holds');
    eq(rows[3].hops < rows[0].hops, true, 'and both rules together walk fewer pointers than neither');
    eq(ufTreeSizes(rows[0].run.result.parent).reduce((a, b) => Math.max(a, b), 0), n,
       'every element ends in one set');
    /* Hops PER FIND, which is what the panel plots against the depth a rank-r
       root allows. A total cannot show either of the two things worth seeing. */
    eq(ufFindHops(rows[0].run).join(','), '11,10,9,8,7,6,5,4,3,2,1,0',
       'without the rank rule the finds walk the whole path, one shorter each time');
    eq(ufFindHops(rows[1].run).every((h) => h <= ilog2(n)), true,
       'with it none walks past log2 of the set -- which is the 2^r bound, turned round');
    eq(ufFindHops(rows[2].run).join(','), '11,1,1,1,1,1,1,1,1,1,1,0',
       'and path compression alone flattens the path on the FIRST find, so the rest walk one');
    const svg = drawForest(null, rows[1].run.result.parent, { width: 620, height: 280 });
    eq((svg.match(/<circle /g) || []).length, n, 'the forest draws every element, with no element involved');
    eq(forestLayout(ufSequence('star', 6).length ? unionFindRun(ufSequence('star', 6), {}, 6).result.parent
       : [], {}).depth, 1, 'unioning everything into one element leaves a forest of depth 1');
  }
  {
    const out = workloadRanked({ search: 12, index: 2, deleteAt: 2, min: 2 }, 32);
    eq(out.best, 'sortedArray', 'a lookup-heavy mix is cheapest on the sorted array');
    eq(out.rows.filter((r) => !r.usable).map((r) => r.rep).join(','), 'stack,queue',
       'and the stack and the queue are OUT OF THE RUNNING rather than slow');
    eq(out.rows.filter((r) => r.rep === 'stack')[0].unsupported.join(','),
       'search,index,deleteAt,min', 'each named by the operations it cannot answer at all');
    eq(out.rows.filter((r) => r.rep === 'sortedArray')[0].total + ','
       + out.rows.filter((r) => r.rep === 'list')[0].total, '108,513',
       'binary search against a scan: 108 against 513, counted by running the mix');
    eq(workloadRanked({ insertFront: 4 }, 8).rows.filter((r) => r.rep === 'sortedArray')[0].usable,
       false, 'and a sorted array refuses to be told WHERE to insert');
  }

  /* ----------------------------------- heap: the two false reuse claims */
  {
    let drift = 0;
    for (let n = 0; n <= 40; n += 1) {
      ['sorted', 'reverse', 'shuffle', 'tied2', 'tied5'].forEach(function (kind) {
        /* The tied inputs are not decoration. On distinct keys a comparison
           written `<` and one written `<=` make the SAME count, so a pin that
           only ever sees a permutation of 1..n cannot tell them apart. */
        const a = kind.indexOf('tied') === 0
          ? tiedRecords(n, Math.max(1, +kind.slice(4))).map((r) => r.key)
          : makeArray(n, kind);
        if ((insertionSortRun(a).counts.compares || 0) !== insertionSort(a)) drift += 1;
        const h = heapsortRun(a), t = heapsortTagged(a.map((k, i) => ({ key: k, tag: i + 1 })));
        if ((t.counts.compares || 0) !== (h.counts.compares || 0)) drift += 1;
        if ((t.counts.swaps || 0) !== (h.counts.swaps || 0)) drift += 1;
      });
    }
    eq(drift, 0, 'both kit-local re-runs are pinned to the shipped ones: 205 inputs, tied keys included, same counts');
    eq(insertionSortRun([3, 1, 2]).result.sorted.join(','), '1,2,3',
       'and insertionSortRun RETURNS the run, which ALGO_JS.insertionSort does not -- the reason it exists');
    eq(heapsortTagged(tiedRecords(8, 2)).result.stable, false,
       'heapsort is not stable: equal keys come out in the wrong order');
  }
  {
    const ops = heapOpsScript(heapKeysParse('5 3 8 1 9 2', 15).keys, 2);
    const run = heapOpsRun(ops, false);
    eq(run.result.steps.length, 8, 'six inserts and two extractions');
    eq(run.result.steps.filter((s) => s.op === 'extract').map((s) => s.key).join(','), '1,2',
       'and a min-heap gives the two smallest keys back, in order');
    eq(run.result.everyStepWithinBound, true, 'every operation stays inside its own bound');
    eq(run.result.steps[5].bound + ',' + run.result.steps[6].bound, '2,4',
       'a sift up is bounded by the height and a sift down by TWICE it -- two comparisons a level');
    eq(heapValid(run.result.heap, false), true, 'what is left is a heap');
    eq(heapValid([1, 3, 2, 9, 4, 8, 7], false) + ',' + heapValid([1, 3, 2, 0, 4, 8, 7], false),
       'true,false', 'and heapValid catches a child that beats its parent');
    eq(heapSortedAlready([1, 3, 2]), false,
       'a heap is not sorted: only root-to-leaf paths are ordered, and this one is a valid heap');
    eq(heapValid([1, 3, 2], false), true, 'which it is');
    eq((heapTreeSvg([7], {}).match(/<circle /g) || []).length, 1,
       'the tree renderer draws the root of a one-element heap -- index 0 is falsy and must not vanish');
    eq((heapTreeSvg([5, 3, 8, 1], {}).match(/<circle /g) || []).length, 4, 'and every element of a larger one');
    eq(drawHeapArray(null, [5, 3, 8], {}).match(/<rect /g).length, 3,
       'the array renderer returns its markup with no element involved');
  }
  {
    const down = buildArray(31, 'descending');
    const cd = buildCompare(down, false);
    eq(Rtext(cd.sum.total), '26', 'the sum of heights at n = 31 is 26, evaluated exactly');
    eq(cd.floydSwaps, 26, 'and sifting down from the last internal node MEETS it exactly here');
    eq(cd.insertSwaps, 98, 'where 31 separate inserts swap 98 times');
    eq(cd.underSum, true, 'so the measured count is inside the bound');
    eq(Rtext(cd.perElement), '26/31', 'which is 26/31 per element -- under 2, and that is the linearity');
    const up = buildCompare(buildArray(31, 'ascending'), false);
    eq(up.floydSwaps + ',' + Rtext(up.sum.total), '0,26',
       'increasing keys are already a heap, so the sum is an UPPER BOUND, not a prediction');
    eq(cd.bothAreHeaps + ',' + cd.sameHeap, 'true,false',
       'both methods leave a valid heap and they are not the same heap');
    eq(cd.floyd.result.heap.length + ',' + cd.inserts.result.heap.length, '31,31',
       'and both hold all 31 keys');
    const asc = (list) => list.slice().sort((x, y) => x - y).join(',');
    eq(asc(cd.floyd.result.heap), asc(down),
       'a build PERMUTES the keys: none is lost and none is invented');
    const ser = buildSeries('descending', 20, false);
    eq(ser.floyd.every((v, i) => v <= ser.bound[i]), true,
       'and at every n up to 20 the swaps stay under the sum');
    eq(ser.inserts[19] > ser.floyd[19], true, 'while inserting stays dearer');
  }
  {
    const a = buildArray(16, 'shuffled');
    const hs = heapsortCompare(a);
    eq(hs.correct, true, 'heapsort sorts');
    eq(hs.compares + ',' + hs.mergeCompares, '80,48',
       'and costs 80 comparisons against merge sort’s 48 on the same array, both counted by running them');
    eq(hs.buildCompares + hs.sortCompares, hs.compares, 'the build and the teardown account for all of them');
    const ser = heapsortSeries('ascending', 12);
    eq(ser.heap.every((v, i) => v >= ser.merge[i]), true,
       'heapsort never makes fewer comparisons than merge sort here: the constant is the price of being in place');
  }
  {
    const runs = runsFrom(8, 8);
    const cmp = kwayCompare(runs);
    eq(cmp.agree, true, 'the heap merge and the pairwise passes produce the same sequence');
    eq(cmp.heapCompares + ',' + cmp.pairCompares, '302,180',
       'and the heap makes MORE comparisons, not fewer -- a sift down compares both children');
    eq(cmp.passes + ',' + (cmp.k - 1), '7,7', 'what it buys is one pass instead of k - 1');
    eq(cmp.heapPops, 64, 'one pop per item');
    const a = makeArray(64, 'shuffle');
    const one = hybridRun(a, 1);
    eq(one.insertion + ',' + one.runs, '0,64',
       'a cutoff of one insertion-sorts nothing and merges 64 singleton runs');
    eq(one.merge, kwayMerge(a.map((k) => [k])).counts.compares,
       'which is exactly the k-way merge of those singletons');
    const all = hybridRun(a, a.length);
    eq(all.merge + ',' + all.runs, '0,1', 'and a cutoff of n is insertion sort with nothing left to merge');
    eq(all.insertion, insertionSort(a), 'costing exactly what ALGO_JS.insertionSort counts');
    eq(one.merged.join(',') === all.merged.join(','), true, 'both cutoffs sort');
    const curve = hybridCurve(a, 20);
    eq(curve.best.cutoff > 1 && curve.best.cutoff < 20, true,
       'and the cheapest cutoff is strictly inside the range: a measured crossover, not an endpoint');
    eq(curve.rows[0].total > curve.best.total && curve.rows[19].total > curve.best.total, true,
       'with both ends dearer than the bottom');
  }
  {
    eq(JSON.stringify(externalPasses(1000000000, 1000000, 4)),
       '{"fanin":250000,"runs":1000,"merges":1,"passes":2}',
       'a billion records with a million in memory sort in two passes: make the runs, merge them once');
    eq(externalPasses(1000000000, 1000, 4).passes, 4, 'a thousand in memory needs four');
    eq(externalPasses(1000000000, 1000, 500).passes, 21,
       'and blocks of five hundred leave a fan-in of two, which is twenty-one passes');
    eq(externalPasses(10000000, 10000000, 4).passes + ','
       + externalPasses(10000000, 10000000, 4).merges, '1,0',
       'while data that fits in memory takes one pass and no merge at all');
    eq(externalPasses(1000, 4, 4), null, 'memory too small to hold two blocks refuses rather than returning a number');
  }
}


// ------------------------------------------------------------------ sortkit
console.log('sorting and selection: one exact expectation, and the inputs built to break a rule');
{
  /* The course's spine is 2(n+1)H_n - 4n, and the reason it is the spine is
     that it holds on EVERY input. So the assertions below are of three kinds.

     First, three independent derivations of the same fraction: the closed form
     over an exact H_n, the recurrence solved from the bottom with no harmonic
     number in it, and the average over every pivot sequence there is. Two
     implementations agreeing is evidence; three from different definitions is
     most of a proof.

     Second, the same exhaustive average computed on a sorted array, a reversed
     one and the array built to destroy median-of-three. If the expectation
     depended on the input, these would differ, and the lesson would be wrong.

     Third, the measured means. A mean over seeds is a SAMPLE, so it is
     asserted to within a tolerance and the tolerance is stated -- which is the
     honest shape for the one figure on this page that is not exact. */
  const SORTKIT_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'sortkit.py');
  const sortkitSrc = fs.readFileSync(SORTKIT_SOURCE, 'utf8');
  const sortkitBlock = (name) => blockFrom(sortkitSrc, name, SORTKIT_SOURCE);
  eval(block('RATIONAL_JS'));
  eval(sysdBlock('HARMONIC_JS'));
  eval(sysdBlock('STREAM_JS'));
  eval(algoBlock('ALGO_JS'));
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('RFIXED_JS'));
  eval(algoCoreBlock('SERIES_JS'));
  eval(algoCoreBlock('SEEDED_JS'));
  eval(algoCoreBlock('ORACLE_JS'));
  eval(algoCoreBlock('SORT_JS'));
  eval(sortkitBlock('SORTKIT_JS'));

  const dec = (r) => parseFloat(Rfixed(r, 8));
  const within = (got, want, tol) => Math.abs(dec(got) - dec(want)) <= tol * dec(want);

  /* --- the expectation, three ways, and it is the same fraction ---------- */
  for (const n of [2, 3, 5, 8, 12, 17, 24]) {
    eq(Requ(quickRecurrence(n), quickExpected(n)), true,
       'the quicksort recurrence solved from the bottom gives 2(n+1)H_n - 4n at n = ' + n);
  }
  eq(Rtext(quickRecurrence(8)) + ' = ' + Rfixed(quickRecurrence(8), 4), '2369/140 = 16.9214',
     'and at n = 8 that fraction is 2369/140, not a decimal that nearly is');
  eq(Requ(quickExpected(9), Rsub(Rmul(R(20n, 1n), harmonic(9, 1)), R(36n, 1n))), true,
     'with H_9 taken from sysdesign_core.harmonic, reused exactly as it ships');

  /* THE POINT OF THE COURSE, computed rather than asserted: the average over
     every pivot sequence is the same fraction on every array. */
  {
    const n = 8, want = quickExpected(n);
    const arrays = { sorted: sortInput('sorted', n), reversed: sortInput('reversed', n),
                     organ: sortInput('organ', n), shuffled: sortInput('shuffle', n, 5),
                     killer: sortInput('killer', n, 1, 'median3') };
    for (const name of Object.keys(arrays)) {
      const r = quickExhaustive(arrays[name], 10);
      eq(Rtext(r.mean), Rtext(want),
         'averaged over every pivot sequence, ' + name + ' costs the same exact fraction');
    }
    eq(quickExhaustive(sortInput('sorted', 8), 10).executions, 1430,
       'and the enumeration really is every execution: Catalan(8) = 1430 of them');
    eq(quickExhaustive(sortInput('sorted', 6), 10).executions, 132, 'Catalan(6) = 132 at n = 6');
    const refuses = (f) => { try { f(); return false; } catch (e) { return /exceeds the exhaustive cap/.test(e.message); } };
    eq(refuses(() => quickExhaustive(sortInput('sorted', 11), 10)), true,
       'eleven elements is refused through oracleCap rather than run slowly');
  }

  /* --- the measured mean over seeds against the exact expectation --------- */
  {
    const n = 16, seeds = seedList(1, 400), exact = quickExpected(n);
    eq(Rtext(exact) + ' = ' + Rfixed(exact, 4), '18358463/360360 = 50.9448',
       'E[comparisons] at n = 16 is exactly 18358463/360360');
    for (const kind of ['sorted', 'reversed', 'killer', 'shuffle']) {
      const a = sortInput(kind, n, 1, 'median3');
      const mean = quickMeanOverSeeds(a, seeds);
      eq(within(mean, exact, 0.03), true,
         '400 seeds of randomised quicksort on ' + kind + ' average within 3% of it (measured '
         + Rfixed(mean, 3) + ')');
    }
    /* The sample is a sample: the same 400 seeds do NOT reproduce the fraction. */
    eq(Requ(quickMeanOverSeeds(sortInput('killer', n, 1, 'median3'), seeds), exact), false,
       'and none of those means IS the expectation -- a mean over seeds is a sample of it');
    const means = quickRunningMeans(sortInput('killer', n, 1, 'median3'), seeds);
    eq(means.length + ',' + Requ(means[means.length - 1], quickMeanOverSeeds(sortInput('killer', n, 1, 'median3'), seeds)),
       '400,true', 'the running mean ends on the mean the panel prints');
  }

  /* --- the measured count against merge sort's independent total ---------- */
  {
    /* mergeSort is ALGO_JS's, written for another course and reused unchanged.
       On an already-sorted array of 16 every merge stops on the left run, so
       the total is (n/2) log2 n = 32 -- a closed form this file evaluates and
       that routine has never heard of. */
    eq(mergeSort(sortInput('sorted', 16)), 32,
       'merge sort on a sorted array of 16 makes (n/2)log2(n) = 32 comparisons');
    eq(mergeSort(sortInput('sorted', 8)) + ',' + mergeSort(sortInput('sorted', 32)), '12,80',
       'and 12 at n = 8, 80 at n = 32, by the same count');
    for (const n of [12, 24, 33]) {
      const a = sortInput('shuffle', n, 9);
      eq(quickselectRun(a, 1 + (n >> 1), 'random', 4).result.sortThenIndex, mergeSort(a.slice()),
         'quickselect prints merge sort’s own total as its baseline at n = ' + n);
      eq(mergeSort(a.slice()) >= sortingLowerBound(n), true,
         'which is at least ceil(log2 n!) = ' + sortingLowerBound(n) + ', as no comparison sort can be under');
      /* Not seed by seed: on roughly one draw in eight quickselect is dearer
         than sorting, which is what "expected" means -- a single-seed
         assertion here would have quietly hidden it. So the claim is made
         about the mean, where it belongs. */
      let selTotal = 0;
      for (let s = 1; s <= 200; s += 1) selTotal += quickselectRun(a, 1 + (n >> 1), 'random', s).counts.compares || 0;
      eq(selTotal / 200 < mergeSort(a.slice()), true,
         'and over 200 seeds selecting the median averages ' + (selTotal / 200).toFixed(1)
         + ' against merge sort\u2019s ' + mergeSort(a.slice()) + ' at n = ' + n);
    }
    eq(sortingLowerBound(8) + ',' + sortingLowerBound(12) + ',' + sortingLowerBound(20),
       '16,29,62', 'ceil(log2 n!) at 8, 12 and 20');
    /* The two sizes where n! IS a power of two, which is the only place a
       ceiling and a floor-plus-one disagree -- and the only place this
       function can be caught rounding the wrong way. */
    eq(sortingLowerBound(1) + ',' + sortingLowerBound(2) + ',' + sortingLowerBound(3), '0,1,3',
       'and 0, 1, 3 at the sizes where the ceiling matters: one comparison decides two elements, not two');
  }

  /* --- the input built to kill a pivot rule ------------------------------ */
  {
    for (const rule of ['first', 'middle', 'median3', 'last']) {
      const a = killerInput(24, rule).array;
      eq(a.slice().sort((p, q) => p - q).join(','), sortInput('sorted', 24).join(','),
         'the killer for ' + rule + ' is a permutation of 1..24 and not a trick');
      const got = quickRun(a, rule).counts.compares || 0;
      eq(quickRun(a, rule).result.sorted.join(','), sortInput('sorted', 24).join(','),
         'quicksort still sorts it under ' + rule);
      eq(got > 24 * Math.log2(24) * 1.5, true,
         rule + ' pays ' + got + ' comparisons on it, far past n log2 n = ' + Math.round(24 * Math.log2(24)));
    }
    eq(quickRun(killerInput(32, 'median3').array, 'median3').counts.compares, 304,
       'median of three costs exactly 304 on its own killer at n = 32');
    /* The CONSTRUCTION, not only its consequence. Three things are pinned.

       One: the array itself at n = 16, because a killer that merely happens to
       be quadratic and a killer built by the adversary are different objects
       and only the second one generalises.

       Two: consistency. Every answer the adversary gave has to agree with the
       values it finally hands back, or the array is not an input at all. For
       the rules whose pivot choice costs no comparisons the check is exact:
       the number of comparisons the adversary was ASKED must equal the number
       the ordinary quicksort then makes on the array it produced. It does not
       for median3, whose rule spends three comparisons of its own.

       Three: rule specificity. The whole claim of the lesson is that each
       deterministic rule has its OWN bad input, so a killer built for one rule
       must not be especially bad for another. */
    eq(killerInput(16, 'median3').array.join(','), '1,10,4,14,6,12,8,2,3,5,7,9,11,13,15,16',
       'the adversary builds one particular array at n = 16, and this is it');
    for (const rule of ['first', 'middle', 'last']) {
      const built = killerInput(32, rule);
      eq(built.asked, quickRun(built.array, rule).counts.compares || 0,
         'every answer the adversary gave for ' + rule + ' agrees with the values it handed back, '
         + 'so the real sort walks exactly the path it was answered along');
    }
    {
      const forFirst = killerInput(32, 'first').array;
      eq(quickRun(forFirst, 'first').counts.compares, 496, 'the killer for a first-element pivot costs it 496');
      eq(quickRun(forFirst, 'middle').counts.compares < 150, true,
         'and costs a middle-element pivot ' + quickRun(forFirst, 'middle').counts.compares
         + ' -- a bad input for one rule is not a bad input for another, which is the lesson');
      eq(quickRun(killerInput(32, 'middle').array, 'first').counts.compares < 200, true,
         'and the same the other way round');
    }

    eq(quickRun(killerInput(32, 'first').array, 'first').counts.compares, 496,
       'and a first-element pivot is driven to the full n(n-1)/2 = 496');
    /* Doubling n quadruples the work: the quadratic signature, measured. */
    const c16 = quickRun(killerInput(16, 'median3').array, 'median3').counts.compares;
    const c32 = quickRun(killerInput(32, 'median3').array, 'median3').counts.compares;
    const c64 = quickRun(killerInput(64, 'median3').array, 'median3').counts.compares;
    eq((c32 / c16 > 3 && c64 / c32 > 3), true,
       'and the count more than triples each time n doubles, which n log n cannot do');
    /* The same array, randomised pivot: the expectation does not care. */
    const killer = killerInput(16, 'median3').array;
    eq(within(quickMeanOverSeeds(killer, seedList(1, 300)), quickExpected(16), 0.03), true,
       'the SAME array under a random pivot averages the ordinary expectation, which is what randomising buys');
    /* And the array where randomising buys NOTHING, which the panel says on
       its face rather than leaving for a reader to discover. Lomuto puts every
       key equal to the pivot on one side, so an all-equal array splits n into
       0 and n-1 under every rule there is, seeded included: 2(n+1)H_n - 4n is
       an expectation about DISTINCT keys and this is the counterexample. */
    {
      const flat = sortInput('equal', 24);
      const counts = new Set([1, 2, 3, 7, 19].map((s) => quickRun(flat, 'random', s).counts.compares));
      eq(counts.size + ',' + [...counts][0], '1,276',
         'an all-equal array costs n(n-1)/2 = 276 under every seed, so randomising the pivot changes nothing');
      eq(quickRun(flat, 'first').counts.compares + ',' + quickRun(flat, 'last').counts.compares
         + ',' + quickRun(flat, 'middle').counts.compares, '276,276,276',
         'and the deterministic rules pay exactly the same');
      eq(quickRun(flat, 'median3').counts.compares, 345,
         'median of three pays 345, the extra three per call its own rule spends on a decision that cannot help here');
      eq(Rfixed(quickExpected(24), 2), '92.80',
         'while the expectation for 24 DISTINCT keys is 92.80 -- a claim this array is outside, not a bound it beats');
    }
  }

  /* --- counting sort: the placement direction is the stability ----------- */
  {
    const keys = [2, 1, 2, 0, 1, 2, 0, 1], recs = tagRecords(keys);
    const back = countingPlacement(recs, 3, true), fwd = countingPlacement(recs, 3, false);
    eq(back.result.tally.join(',') + ' | ' + back.result.prefix.join(','), '2,3,3 | 2,5,8',
       'the tally and its prefix sums');
    eq(back.result.violations.length, 0, 'placing from the back keeps equal keys in input order');
    eq(fwd.result.violations.length, 7, 'placing from the front reverses every run: 7 pairs out of order');
    eq(back.result.sorted.map((r) => r.key).join(','), countingSortRun(keys, 3).result.sorted.join(','),
       'and the tagged run agrees key for key with the shipped countingSortRun');
    eq(back.result.sorted.map((r) => r.tag).join(','), '4,7,2,5,8,1,3,6', 'with the tags in input order inside each run');
    eq(countingSortRun(keys, 3).result.work, keys.length + 3, 'whose work column is n + k');
  }

  /* --- radix: two ways to break the composition -------------------------- */
  {
    const K = [329, 457, 657, 839, 436, 720, 355];
    eq(radixRun(K, 10, true).result.sorted.join(','), '329,355,436,457,657,720,839',
       'LSD radix with a stable pass sorts');
    eq(radixRun(K, 10, false).result.correct, false, 'with an unstable pass it does not');
    eq(msdFlatRun(K, 10).result.correct, false,
       'and most-significant-first with no recursion scrambles: ' + msdFlatRun(K, 10).result.sorted.join(','));
    eq(msdFlatRun(K, 10).result.passes.length + ',' + msdFlatRun(K, 10).result.passes[0].digit, '3,2',
       'its first pass reads the most significant digit, which is what makes it wrong');
    /* And the shape of the wrongness, which is what the panel says out loud:
       with no recursion the LAST pass wins, and the last pass is the units
       one, so the array comes out ordered by its final digit and by nothing
       else at all. */
    eq(msdFlatRun(K, 10).result.sorted.map((k) => k % 10).join(','), '0,5,6,7,7,9,9',
       'so what comes out is sorted on the units digit alone');
    eq(msdFlatRun(K, 10).result.passes[2].digit, 0, 'because the pass that ran last read the units');
    eq(radixRun(K, 2, true).result.digits, 10, 'in base 2 the same keys need ten passes');
    eq(radixRun(K, 2, true).result.correct && radixRun(K, 16, true).result.correct, true,
       'and base 2 and base 16 both sort, at different numbers of passes');
  }

  /* --- bucket sort: the assumption, and the input that breaks it --------- */
  {
    eq(Rtext(bucketExpectedWork(48, 12)), '72',
       'with 48 keys over 12 buckets the expected inner work is exactly 72');
    eq(Rtext(bucketExpectedWork(10, 10)), '0', 'and one key a bucket costs nothing at all');
    const uniform = bucketRun(bucketKeys('uniform', 48, 1024, 7), 12, 1024);
    const clustered = bucketRun(bucketKeys('clustered', 48, 1024, 7), 12, 1024);
    eq((uniform.counts.compares || 0) < 3 * 48, true,
       'uniform keys cost ' + (uniform.counts.compares || 0) + ', near linear in n');
    eq((clustered.counts.compares || 0) > 6 * (uniform.counts.compares || 0), true,
       'and clustered keys cost ' + (clustered.counts.compares || 0)
       + ' on the same n with the same algorithm -- the distribution was the claim');
    eq(clustered.result.sorted.join(',') === clustered.result.sorted.slice().sort((p, q) => p - q).join(','), true,
       'both still sort; only the cost moved');
  }

  /* --- median of medians: the group size decides linearity --------------- */
  {
    eq(Rtext(momFractions(3).f1) + ' + ' + Rtext(momFractions(3).f2) + ' = ' + Rtext(momFractions(3).sum),
       '1/3 + 2/3 = 1', 'groups of three sum to exactly one, so the recursion tree does not shrink');
    eq(momFractions(3).converges, false, 'and the level sums do not converge');
    eq(Rtext(momFractions(5).f1) + ' + ' + Rtext(momFractions(5).f2) + ' = ' + Rtext(momFractions(5).sum),
       '1/5 + 7/10 = 9/10', 'groups of five sum to 9/10');
    eq(Rtext(momFractions(5).discard), '3/10', 'because at least 3n/10 is discarded');
    eq(Rtext(momFractions(7).sum) + ',' + momFractions(7).converges, '6/7,true', 'and groups of seven to 6/7');
    eq(Rtext(levelSums(momFractions(5).f1, momFractions(5).f2, 100, 6).geometric), '1000',
       'so at n = 100 the tree sums to 10n = 1000 exactly');
    eq(levelSums(momFractions(3).f1, momFractions(3).f2, 100, 6).geometric, null,
       'while at groups of three there is no geometric total to print');
    const a = sortInput('shuffle', 45, 11);
    const sorted = a.slice().sort((p, q) => p - q);
    for (const k of [1, 12, 23, 45]) {
      eq(momRun(a, k, 5).result.value, sorted[k - 1], 'median of medians finds the ' + k + 'th smallest');
      eq(momRun(a, k, 5).result.agrees, true, 'and quickselect agrees with it there');
    }
    /* The per-round guarantee, swept rather than sampled. Twelve thousand
       rounds over
       three group sizes and five input families; not one of
       them puts fewer than momGuarantee(n, g) elements on the thin side.
       That is a claim about every round of every run here, which is as close
       to "every input" as a measurement gets, and it is the reason this kit
       does not read the guarantee off momRun's own field. */
    eq(momGuarantee(100, 5), 24, "at groups of five the round guarantee is CLRS's 3n/10 - 6 = 24 at n = 100");
    eq(momGuarantee(45, 3) + ',' + momGuarantee(45, 5) + ',' + momGuarantee(45, 7), '12,9,8',
       'and it is a different number for each group size, which floor(3n/10) is not');
    {
      let rounds = 0, violations = 0, shippedWrong = 0, tight = Infinity;
      for (const g of [3, 5, 7]) {
        for (let n = 8; n <= 120; n += 2) {
          for (const kind of ['shuffle', 'sorted', 'reversed', 'organ', 'killer']) {
            const arr = sortInput(kind, n, 1 + (n % 5), 'median3');
            for (const st of momRun(arr, 1 + (n >> 1), g).trace) {
              rounds += 1;
              const thin = Math.min(st.less, st.greater), guard = momGuarantee(st.n, g);
              if (thin < guard) violations += 1;
              if (thin - guard < tight) tight = thin - guard;
              if (st.guarantee !== Math.floor(3 * st.n / 10)) shippedWrong += 1;
            }
          }
        }
      }
      eq(rounds > 5000 ? 'many' : rounds, 'many',
         'the sweep really does run the rounds -- ' + rounds + ' of them');
      eq(violations, 0, 'and not one of them falls under the guarantee');
      eq(tight, 0, 'while the tightest of them meets it exactly, so the bound is not slack for the sake of it');
      eq(shippedWrong, 0,
         "and momRun's own guarantee field is floor(3n/10) on every one of them, group size and all -- "
         + 'which is why this kit computes its own');
    }
  }

  /* --- the lower bounds, and one of them checked on every input ---------- */
  {
    for (const n of [2, 3, 4, 5, 8, 9, 16, 17, 24]) {
      const a = sortInput('shuffle', n, 6), sorted = a.slice().sort((p, q) => p - q);
      const mm = minMaxPairs(a);
      eq(mm.result.min + ',' + mm.result.max, sorted[0] + ',' + sorted[n - 1],
         'min and max together find both ends at n = ' + n);
      eq((mm.counts.compares || 0) <= mm.result.bound, true,
         'in ' + (mm.counts.compares || 0) + ', inside the ceil(3n/2) - 2 = ' + mm.result.bound + ' bound');
      eq(mm.result.bound < mm.result.naive, true,
         'which beats the ' + mm.result.naive + ' of two separate scans');
    }
    eq(minMaxPairs(sortInput('shuffle', 8, 6)).counts.compares, 10, 'meeting the bound exactly at n = 8');
    /* EVERY arrangement, not one: this is the assertion the rest of the kit
       cannot make, and the reason the sweep exists. */
    for (const n of [4, 5, 6, 7]) {
      const sweep = tournamentEvery(n);
      eq(sweep.arrangements, [0, 1, 2, 6, 24, 120, 720, 5040][n], 'n! arrangements enumerated at n = ' + n);
      eq(sweep.wrong, 0, 'the tournament returns the true max and second on every one of them');
      eq(sweep.over, 0, 'and not one exceeds n + ceil(log2 n) - 2');
      eq(sweep.worst, sweep.bound, 'while the worst arrangement meets that bound exactly at n = ' + n);
    }
    const refusesSweep = (f) => { try { f(); return false; } catch (e) { return /exceeds the exhaustive cap/.test(e.message); } };
    eq(refusesSweep(() => tournamentEvery(9)), true, 'nine is refused: 362 880 arrangements is not a redraw');
    eq((scanSecond(sortInput('shuffle', 16, 2)).counts.compares || 0)
       > (tournament(sortInput('shuffle', 16, 2)).counts.compares || 0), true,
       'and keeping the best two in one scan costs more than the tournament');
    eq(tournament(sortInput('shuffle', 16, 2)).result.candidates, 4,
       'because only ceil(log2 16) = 4 elements ever lost to the winner');
  }

  /* --- the small print the panels are built on --------------------------- */
  {
    eq(parseKeys('329, 457, 999999, x, -4, 12', 0, 999, 10).join(','), '329,457,12',
       'a reader’s list drops what is out of range rather than clamping it into a different array');
    eq(parseKeys('1,2,3,4,5,6', 0, 9, 4).join(','), '1,2,3,4', 'and stops at the cap');
    eq([1, 2, 3, 4, 11, 12, 13, 21, 22, 23, 101, 111].map(ordinal).join(' '),
       '1st 2nd 3rd 4th 11th 12th 13th 21st 22nd 23rd 101st 111th', 'ordinals, including the teens');
    eq(groupDigits(1234567), '1 234 567', 'and counts past a thousand are grouped');
    eq(sortInput('shuffle', 12, 3).join(',') === sortInput('shuffle', 12, 4).join(','), false,
       'two seeds give two different shuffles');
    eq(sortInput('shuffle', 12, 3).join(','), sortInput('shuffle', 12, 3).join(','),
       'and one seed gives the same one twice');
    /* The stability panel's own preset, chosen so that three of its four
       algorithms are distinguishable on it: a list on which every sort happens
       to be stable shows a reader nothing, and the first list tried here was
       one of those. */
    const PRESET = tagRecords([7, 3, 7, 1, 9, 3, 5, 1]);
    eq(stableRun(PRESET, 'selection').result.violations.length, 2,
       'selection sort reorders two pairs of equal keys on the stability preset');
    eq(stableRun(PRESET, 'quick').result.violations.length, 2, 'and the Lomuto partition reorders two');
    eq(stableRun(PRESET, 'insertion').result.stable && stableRun(PRESET, 'merge').result.stable, true,
       'and insertion sort and merge sort reorder none');
    {
      // THE ASSERTION THAT WAS MISSING: a sort must sort. Only the violation
      // counts above were pinned, and an unsorted array has a violation count
      // too -- so the 'quick' arm returned [3,1,2,4] for [1,2,3,4] and every
      // check passed. The reader saw an "after" row that was not in order.
      const inputs = [[1,2,3,4], [4,3,2,1], [7,3,7,1,9,3,5,1], [2,2,1], [5], []];
      let wrong = 0;
      for (const algo of ['selection', 'insertion', 'merge', 'quick']) {
        for (const keys of inputs) {
          const out = stableRun(tagRecords(keys), algo).result.output.map((r) => r.key);
          if (!out.every((v, i) => i === 0 || out[i - 1] <= v)) { wrong += 1; }
        }
      }
      eq(wrong, 0, 'every stability arm returns its keys in order, on every input');
    }
    eq(twoKeyPasses([{ major: 3, minor: 70, tag: 1 }, { major: 1, minor: 40, tag: 2 },
                     { major: 3, minor: 20, tag: 3 }, { major: 2, minor: 90, tag: 4 }],
                    'major', 'minor').same, false,
       'and the two pass orders of a two-key sort do not agree, which is why the order is not a preference');
  }
}


// ------------------------------------------------- the hash and tree kits
console.log('algorithms: hash tables and search trees, and the four things they do not prove');
{
  /* The two kits of `data-structures` and `randomised-algorithms` that own the
     hash table and the search tree. The engine they run on (HASH_JS, TREE_JS)
     is asserted above; what is asserted HERE is the arithmetic each kit adds --
     key sets, the naive delete, the rotation at a chosen node, the priorities --
     and, more important, the three places where a number a reader will read is
     NOT a count:

       bloomApprox beside bloomExact        the independent-hash idealisation
       knuthProbeApprox                     the clustering model, refused above 0.98
       randomBstDepthApprox                 2 ln n, an asymptote, not a height

     Each of those has a case below that pins what the panel prints AND what the
     panel must not let it be mistaken for. */
  const HASHKIT_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'hash.py');
  const TREEKIT_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'tree.py');
  const hashKitSrc = fs.readFileSync(HASHKIT_SOURCE, 'utf8');
  const treeKitSrc = fs.readFileSync(TREEKIT_SOURCE, 'utf8');

  eval(block('RATIONAL_JS'));
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('RFIXED_JS'));
  eval(sysdBlock('STREAM_JS'));
  eval(algoCoreBlock('SEEDED_JS'));
  eval(sysdBlock('APPROX_JS'));
  eval(algoCoreBlock('TREEDRAW_JS'));
  eval(algoCoreBlock('HASH_JS'));
  eval(algoCoreBlock('TREE_JS'));
  eval(blockFrom(hashKitSrc, 'HASHKIT_JS', HASHKIT_SOURCE));
  eval(blockFrom(treeKitSrc, 'TREEKIT_JS', TREEKIT_SOURCE));

  /* --- the seeded stream, dealt the way THIS kit deals it ----------------
     The trap is not hypothetical and it is not about the stream in the
     abstract: every draw on these pages is consumed as a SLOT, through
     hashOf(x, m, 'division'), which is x mod m. Under glibc's parameters the
     modulus is 2^31, so 1200 keys fall into 4, 8 or 16 slots dead level and a
     collision lesson would demonstrate the opposite of its claim. */
  {
    [4, 8, 16].forEach(function (m) {
      const glibc = new Array(m).fill(0), minstd = new Array(m).fill(0);
      lcgStream(1103515245, 12345, 2147483648, 7, 1200).forEach((x) => { glibc[hashOf(x, m, 'division')] += 1; });
      algoStream(7, 1200).forEach((x) => { minstd[hashOf(x, m, 'division')] += 1; });
      eq(new Set(glibc).size, 1, 'the glibc stream hashed into ' + m + ' slots is PERFECTLY level');
      eq(Math.max.apply(null, minstd) - Math.min.apply(null, minstd) > 0, true,
         'and the prime-modulus stream this kit uses is not, at ' + m + ' slots');
    });
  }

  /* --- chaining: the expectation, the measurement, and the key set that
         separates them --------------------------------------------------- */
  {
    const stride = hashKeySet('stride', 20, 8);
    eq(stride.slice(0, 4).join(','), '8,16,24,32', 'the degenerate key set is every multiple of m');
    const div = chainRun(stride, 8, 'division').result;
    eq(div.longest + ',' + div.empty, '20,7', 'which the division rule puts in ONE chain of 20');
    eq(Rtext(div.measuredMean), '21/2',
       'so the mean it measures is 21/2 while the expectation still reads 5/2');
    eq(Rtext(div.expectedUnsuccessful), '5/2', 'the expectation being an assumption about the keys');
    const mul = chainRun(stride, 8, 'multiply').result;
    eq(mul.longest + ',' + mul.empty, '5,0', 'and the multiplicative rule spreads the same keys');
    eq(new Set(hashKeySet('seeded', 20, 8, 7)).size, 20, 'a seeded key set holds no duplicates');
    eq((chainSvg(chainRun([1, 2, 3, 4], 4, 'division').result.chains, 1).match(/<rect /g) || []).length,
       8, 'the chain drawing is one slot box and one key box per key');
  }

  /* --- probing: what was counted, and the curve that is not a count -------
         knuthProbeApprox is one of the path's four approximations, and the
         panel must print the REFUSAL above alpha = 0.98 rather than a figure
         read off a vertical curve. */
  {
    eq(knuthRow(0.5).unsuccessful + ',' + knuthRow(0.5).successful, '2.50,1.50',
       "Knuth's two curves read 2.50 and 1.50 at half load");
    eq(knuthRow(0.99).quoted, false, 'and are not quoted at all at 0.99');
    eq(/0\.98/.test(knuthRow(0.99).note), true, 'the panel printing the refusal and the reason');
    const pm = probeMeasure(32, 'linear', 5, 70);
    eq(Rtext(pm.alpha) + ',' + Rtext(pm.unsuccessful) + ',' + Rtext(pm.successful), '11/16,5,51/22',
       'probes are counted, and a mean of integers is an exact fraction');
    eq(Rcmp(pm.unsuccessful, R(BigInt(32), 1n)) <= 0, true,
       'and a counted mean can never exceed the table size, which the curve can');
    ['linear', 'quadratic', 'double'].forEach(function (rule) {
      const demo = deleteDemo(32, rule, 5);
      eq(demo.lostWithTombstones.length, 0, 'tombstones lose no key under ' + rule + ' probing');
      eq(demo.lostWhenEmptied.length > 0, true,
         'and emptying the slot instead loses keys that are still in the table');
    });
  }

  /* --- resizing: the hysteresis, evaluated rather than asserted ---------- */
  {
    const ops = resizeOps('boundary', 40, 9);
    const gap = resizeRun(ops, Rparse('1/1'), Rparse('1/4'), 4).result;
    const none = resizeRun(ops, Rparse('1/2'), Rparse('1/2'), 4).result;
    eq(gap.total + ',' + gap.bound + ',' + gap.thrashAt, '52,120,null',
       'grow at 1 and shrink at 1/4: 52 against the 3m the argument allows, and no thrashing');
    eq(none.total + ',' + none.bound + ',' + none.thrashAt, '495,120,1',
       'the SAME operations with both thresholds at 1/2 cost 495 against 120, thrashing from step 2');
  }

  /* --- universality, over the whole family and against one fixed function - */
  {
    let worst = null;
    for (let x = 0; x < 11; x += 1) for (let y = x + 1; y < 11; y += 1) {
      const got = universalCount(11, 4, x, y);
      if (!got.withinBound) worst = x + ',' + y;
    }
    eq(worst, null, 'every pair of keys collides in at most 1/m of the family, not just a lucky one');
    eq(Rtext(universalCount(11, 4, 3, 7).rate), '2/11', 'the pair 3 and 7 collides in 2/11 of it');
    const adv = adversaryPair(4);
    eq(Rtext(adv.rate), '1', 'while ONE fixed function collides with probability 1');
    eq(adv.x % 4 === adv.y % 4, true, 'on the two keys an adversary picks once it can see the function');
  }

  /* --- balls in bins: the exact expectations, one throw, and the two
         asymptotics this library states and does not prove ---------------- */
  {
    const thrown = throwBalls(64, 64, 4);
    eq(thrown.bins.reduce((a, b) => a + b, 0), 64, 'every ball lands in exactly one bin');
    eq(thrown.empty + ',' + thrown.maxLoad + ',' + thrown.pairs, '19,3,21',
       'and this seeded throw leaves 19 bins empty, its tallest holding 3');
    eq(Rtext(ballsExact(64, 64).expectedPairs), '63/2',
       'against an exact expectation of 63/2 colliding pairs');
    const stated = statedMaxLoad(365);
    near(stated.oneChoice, 3.3240, 1e-3, 'log n / log log n reads 3.324 at 365 -- STATED, not proved');
    near(stated.twoChoice, 1.7749, 1e-3, 'ln ln n reads 1.775 -- STATED, not proved');
    eq(statedMaxLoad(3), null, 'and below four bins it is not quoted at all, where ln ln n is not positive');
  }

  /* --- THE BLOOM CASE: the exact rate against the idealisation -----------
         Two instances with the SAME kn/m and different m. bloomApprox depends
         only on kn/m, so it returns the same number for both; bloomExact does
         not, because it counts the bits a filter of that size really sets. The
         gap between the columns is the independence assumption, and this pair
         is the sharpest form of it in the library. */
  {
    eq(bloomApprox(160, 16, 7).toFixed(9), '0.008193722',
       'the idealisation at m = 160, n = 16, k = 7');
    eq(bloomApprox(1000, 100, 7).toFixed(9), '0.008193722',
       'and at m = 1000, n = 100, k = 7 -- the SAME number, because it sees only kn/m');
    eq(Rfixed(bloomExact(160, 16, 7), 6), '0.008319', 'the exact rate at m = 160 is 0.008319');
    eq(Rfixed(bloomExact(1000, 100, 7), 6), '0.008214', 'and at m = 1000 it is 0.008214');
    eq(Number(Rfixed(bloomExact(160, 16, 7), 9)) > bloomApprox(160, 16, 7), true,
       'the exact rate is ABOVE the idealisation, at both sizes');
    eq(Number(Rfixed(bloomExact(1000, 100, 7), 9)) > bloomApprox(1000, 100, 7), true,
       'which is what the independent-hash assumption costs');
    eq(Number.isNaN(Rnum(bloomExact(160, 16, 7))), true,
       'and a double cannot hold either of them -- Rnum is NaN at a 1729-digit denominator');
    eq(Rfraction(bloomExact(160, 16, 7), 18), 'a fraction with a 1729-digit denominator',
       'so the panel says how long the fraction is instead of printing it');
    eq(Rfraction(R(3n, 8n), 18), '3/8', 'and prints it when a reader could read it');
    const best = bloomKStar(160, 16, 10);
    eq(best.k, 7, 'scanning k exactly puts the best at 7 for ten bits a key');
    eq(best.rows.every((r) => Rcmp(best.rate, r.rate) <= 0), true, 'and no k in the scan beats it');
    const inst = bloomInstance(160, 16, 7, 6);
    eq(inst.set + ',' + inst.falsePositives + ',' + inst.trials, '74,1,200',
       'one seeded filter sets 74 of its 160 bits and gives 1 false positive in 200 lookups');
    eq(inst.keys.every(function (key) {
      for (let j = 0; j < 7; j += 1) if (!inst.bits[hashOf(key * (2 * j + 1) + j, 160, 'multiply')]) return false;
      return true;
    }), true, 'and NEVER a false negative: every inserted key still has all seven of its bits set');
  }

  /* --- count-min's stream ------------------------------------------------ */
  {
    const heavy = streamPreset('heavy', 2);
    eq(heavy.length + ',' + heavy.filter((k) => k === 1).length, '64,40',
       'the heavy-hitter stream is 64 updates of which 40 are one key');
    const run = countMinRun(heavy, 8, 3).result;
    eq(run.neverUnder, true, 'and the sketch never estimates below the truth');
    eq(Rtext(run.eps) + ',' + Rtext(run.delta), '1/4,1/8',
       'with the Markov guarantee 2/w and 2^-d as exact fractions');
  }

  /* --- THE TREE CASE: a measured height against its asymptote ------------
         2 ln n is one of the path's four approximations and the failure mode
         of the lesson is reading it as a height. At n = 15 it is 5.416 while
         the shortest tree on fifteen keys has height 3 and mean depth 34/15 =
         2.267, and the path of sorted insertion has height 14. Three different
         numbers; the panel prints all three and labels which is which. */
  {
    near(randomBstDepthApprox(15), 5.4161, 1e-3, '2 ln n reads 5.416 at n = 15');
    const sorted = bstFromOrder(insertOrder('sorted', 15, 7)).result;
    const bisect = bstFromOrder(insertOrder('bisect', 15, 7)).result;
    const shuffled = bstFromOrder(insertOrder('shuffled', 15, 7)).result;
    eq(sorted.height, 14, 'while sorted insertion of the same 15 keys gives height 14');
    eq(bisect.height + ',' + Rtext(bisect.meanDepth), '3,34/15',
       'middle-first gives height 3 and mean depth 34/15 -- neither of them 5.416');
    eq(shuffled.height + ',' + Rtext(shuffled.meanDepth), '6,44/15',
       'and a seeded shuffle gives height 6 and mean depth 44/15');
    eq(Rcmp(bisect.meanDepth, R(BigInt(Math.round(randomBstDepthApprox(15) * 1000)), 1000n)) < 0, true,
       'the asymptote is above the measured mean depth by more than a third at this n');
    eq(insertOrder('shuffled', 15, 7).slice().sort((a, b) => a - b).join(','),
       insertOrder('sorted', 15, 7).join(','),
       'and every order is a permutation of the same key set -- the keys do not decide the tree');
  }

  /* --- rotation at a chosen node, and the check that must not move ------- */
  {
    const root = bstFromOrder([50, 30, 70, 20, 40, 10]).result.root;
    const spun = rotateAt(root, 50, 'right');
    eq(bstInorder(spun.root).join(' '), '10 20 30 40 50 70',
       'a rotation at the root leaves the in-order sequence exactly as it was');
    eq(bstInorder(spun.root).join(' '), bstInorder(root).join(' '),
       'and the tree it was given is untouched, so both can be drawn');
    eq(spun.rotated, true, 'the rotation is reported as performed');
    const cannot = rotateAt(root, 10, 'right');
    eq(cannot.found + ',' + cannot.rotated, 'true,false',
       'while rotating right at a node with no left child is reported as NOT performed');
    eq(sizesValid(spun.root) + ',' + sizesValid(root), 'true,true',
       'and every subtree size is recomputed through the rotation rather than going stale');
    eq(avlHeightBound(6) + ',' + avlHeightBound(7) + ',' + avlHeightBound(12), '2,3,4',
       'the AVL height bound is a search over N(h), not a logarithm');
    eq(minAvlNodes(3).n, 7, 'N(3) = 7, from N(h) = N(h-1) + N(h-2) + 1');
    const mixed = avlInsert([50, 25, 75, 10, 5, 30, 27, 60, 90, 80, 70, 98, 62]);
    eq(mixed.result.height + ',' + mixed.result.plainHeight + ',' + mixed.result.rebalances,
       '3,4,4', 'the four-case sequence rebalances four times and holds the height at 3');
    eq(mixed.trace.map((t) => t.rebalance).join(' '), 'LL LR RR RL',
       'naming all four cases, in that order');
  }

  /* --- the local check, and the tree that passes it without being a search
         tree. This is the misconception, and it is only settled by an
         instance where the two verdicts disagree. */
  {
    const odd = localOnlyTree();
    eq(bstLocallyValid(odd), true, 'every node of the counterexample sits between its two children');
    eq(bstValid(odd, null, null), false, 'and it is not a search tree: 25 is in 20\'s LEFT subtree');
    eq(bstInorder(odd).join(' '), '10 25 20 30', 'which its in-order walk shows by not being sorted');
    eq(treeParseOps('50 -30 ?40', 9).ops.map((o) => o.op + ':' + o.key).join(' '),
       'insert:50 delete:30 search:40', 'and the reader writes all three operations on one line');
  }

  /* --- a treap is the same tree from either order ------------------------ */
  {
    const keys = insertOrder('sorted', 12, 5), pri = treapPriorities(keys, 5);
    eq(new Set(keys.map((k) => pri[k])).size, 12,
       'priorities are ranked, so no two keys share one and the shape is determined');
    const a = insertOrder('sorted', 12, 5), b = insertOrder('shuffled', 12, 6);
    const A = treapInsert(a, prioritiesFor(a, pri)), B = treapInsert(b, prioritiesFor(b, pri));
    eq(treeShape(A.result.root), treeShape(B.result.root),
       'and two insertion orders of the same (key, priority) set give the SAME TREE, node for node');
    eq(A.result.heapOrdered + ',' + B.result.heapOrdered, 'true,true', 'both heap-ordered');
    eq(A.result.height + ',' + bstFromOrder(a).result.height, '5,11',
       'at height 5, where the plain search tree on the same order is a path of 11');
  }

  /* --- a skip list from the reader's tape, against a reference curve ----- */
  {
    const sl = skipBuild(insertOrder('sorted', 16, 1), algoCoins(1, 144)).result;
    eq(Rtext(sl.meanHops) + ',' + sl.maxLevel + ',' + sl.worstHops, '77/16,4,8',
       'sixteen keys on tape seed 1: mean 77/16 hops, four levels, worst 8');
    eq(hopsReference(16), 8, 'against 2 log2 n = 8, which is a reference curve and not a count');
    eq((skipListSvg(sl.sorted, sl.maxLevel, []).match(/<circle /g) || []).length, 33,
       'and the drawing puts one circle at every level a key reaches');
    eq((bstSvg(bstFromOrder([9, 4, 13, 2, 6, 11, 15]).result.root, { width: 660 })
        .match(/<circle /g) || []).length, 7,
       'while the tree renderer draws one circle per node, through the shared layout');
  }
}

// ------------------------------------------------- or_core + simulate kit
// SIM_JS's own functions are exercised in the or_core section above. This is
// the KIT on top of it, in scripts/mathpath/labs/simulate.py: the stream, the
// sampler, the slotted run, the event calendar, the exact transient, the four
// variance-reduction measurements and the drawings. Every one is a top-level
// function, so what runs here is the source that ships.
//
// FOUR OF THESE ARE REGRESSION TESTS, and each one is a defect this kit had or
// would have had:
//
//   * THE GENERATOR. A power-of-two modulus has low bits that are a cycle and
//     not a sample, and this kit reduces. Under the glibc constants a thousand
//     two hundred draws land in four bins 300/300/300/300 -- perfectly level,
//     asserted below -- and a mode whose claim is that one run is not the
//     expectation would have been refuting itself. The same defect reached three
//     other kits before it was caught, so the spread of MINSTD's low bits is
//     pinned here rather than described in a comment.
//   * THE SEED. An LCG's k-th value is affine in its seed, so seeds 1 through 8
//     give eight points on a straight line: the unmixed first draws below step
//     by exactly 16807 every time. Six of this kit's nine modes ask a reader to
//     reseed and compare, so the splitmix64 finaliser is load bearing and the
//     absence of a constant difference is asserted.
//   * THE CALENDAR'S CONTENTS. Recomputing who is in the system from the clock
//     alone disagrees with desRun's own count at any instant carrying two
//     events -- a departure is taken before an arrival at the same time, so the
//     table said three in system and listed two. The count and the contents are
//     now one walk of one event list, and their agreement is asserted at every
//     event.
//   * THE DRAWN TRANSIENT. E[N_t] at four hundred slots is a fraction with an
//     eight-hundred-digit denominator; Number(n)/Number(d) of it is
//     Infinity/Infinity, which is NaN, and a NaN y coordinate draws a curve with
//     holes and reports nothing. The float is now a BigInt long division, and it
//     is asserted finite and asserted to agree with the exact value.
console.log('operations research: the simulation kit, its generator and its four measurements');
{
  const SIM_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'simulate.py');
  const OR_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'or_core.py');
  const simSrc = fs.readFileSync(SIM_SOURCE, 'utf8');
  const orSrc = fs.readFileSync(OR_SOURCE, 'utf8');
  const simBlock = (n) => blockFrom(simSrc, n, SIM_SOURCE);
  const orBlock = (n) => blockFrom(orSrc, n, OR_SOURCE);

  eval(block('RATIONAL_JS') + block('SURD_JS') + orBlock('ORFMT_JS') + orBlock('SIM_JS')
     + sysdBlock('STREAM_JS') + sysdBlock('PMF_JS') + sysdBlock('TRACE_JS') + sysdBlock('SLOTTED_JS')
     + numberBlock('NT_JS')
     + simBlock('SIMBASE_JS') + simBlock('SIMSURD_JS') + simBlock('SIMDRAW_JS') + simBlock('SIMSTAIR_JS')
     + simBlock('SIMQ_JS') + simBlock('SIMCHAIN_JS') + simBlock('SIMBINOM_JS'));

  const ri = (v) => R(BigInt(v), 1n);
  const rf = (n, d) => R(BigInt(n), BigInt(d));
  const PMF = [[ri(0), rf(1, 16)], [ri(1), rf(4, 16)], [ri(2), rf(6, 16)],
               [ri(3), rf(4, 16)], [ri(4), rf(1, 16)]];

  /* --- the stream: MINSTD, and the two things that go wrong without it ----- */
  {
    eq(simMultiplier() + '/' + simModulus(), '16807/2147483647',
       'the kit draws from MINSTD -- prime modulus -- and not from the glibc constants');
    /* The low bits are a SAMPLE, and the test has to be TWO-SIDED. "Not
       perfectly level" alone is not enough: a purely multiplicative generator
       with a power-of-two modulus collapses the other way, putting all 1200
       draws in one bin of four, and a one-sided check passes it. So every bin
       must be occupied to within a factor of two of its expectation AND the
       bins must not all be exactly equal. MINSTD's worst deviation over 1200
       draws is about a third at sixteen bins, which is sampling noise; both
       failure modes miss these bounds by a mile. */
    const s = simStream(1, 1200);
    for (const bins of [4, 8, 16]) {
      const c = new Array(bins).fill(0), want = 1200 / bins;
      s.forEach((x) => { c[x % bins] += 1; });
      eq(c.every((v) => v > want / 2 && v < want * 2), true,
         'MINSTD mod ' + bins + ' fills every bin within a factor of two of ' + want
         + ': ' + Math.min.apply(null, c) + ' to ' + Math.max.apply(null, c));
      eq(c.every((v) => v === want), false,
         'and is not EXACTLY level across ' + bins + ' bins, which a cycle would be');
    }
    /* Both counter-examples, asserted rather than asserted about. */
    {
      const lvl = lcgStream(1103515245, 12345, 2147483648, 1, 1200), lc = [0, 0, 0, 0];
      lvl.forEach((x) => { lc[x % 4] += 1; });
      eq(lc.join(','), '300,300,300,300',
         'the glibc mixed stream mod 4 is EXACTLY level -- a cycle, not a sample');
      const col = lcgStream(1103515245, 0, 2147483648, 1, 1200), cc = [0, 0, 0, 0];
      col.forEach((x) => { cc[x % 4] += 1; });
      eq(cc.join(','), '0,1200,0,0',
         'and dropping its increment collapses every draw into ONE bin -- the other way the same modulus fails');
    }
    /* And the seed is mixed, because an LCG is affine in its seed. */
    const raw = [1, 2, 3, 4, 5, 6, 7, 8].map((k) => lcgStream(16807, 0, 2147483647, k, 1)[0]);
    const rd = [];
    for (let i = 1; i < raw.length; i += 1) rd.push(raw[i] - raw[i - 1]);
    eq(rd.every((v) => v === rd[0]) && rd[0] === 16807, true,
       'an UNMIXED seed walks a straight line: seeds 1..8 step by exactly 16807');
    const mixed = [1, 2, 3, 4, 5, 6, 7, 8].map((k) => simStream(k, 1)[0]);
    const md = [];
    for (let i = 1; i < mixed.length; i += 1) md.push(mixed[i] - mixed[i - 1]);
    eq(md.every((v) => v === md[0]), false,
       'and the splitmix64 finaliser breaks that affinity, so reseeding samples instead of sliding');
    eq(simSeedState(0) > 0 && simSeedState(0) < simModulus(), true,
       'the mixed state is in range and never the fixed point 0');
    eq(simUniform(1, 500).every((u) => Rcmp(u, rf(1, 2)) !== 0), true,
       'an odd modulus never produces U = 1/2, so no comparison in this kit has a tie to settle');
  }

  /* --- the sampler, on the worked instance the lesson prints --------------- */
  {
    eq(lcgStream(25173, 13849, 65536, 1, 4).join(', '), '39022, 61087, 20196, 45005',
       'the stated generator from seed 1');
    const us = streamUniform(25173, 13849, 65536, 1, 200);
    eq(Rtext(us[0]), '19511/32768', 'whose first U is a fraction, not a decimal');
    eq(simCumulative(PMF).map((r) => Rtext(r.hi)).join(' '), '1/16 5/16 11/16 15/16 1',
       'the cumulative table, which IS the sampler');
    const draws = us.map((u) => sampleFromPmf(PMF, u));
    const freq = simFrequencies(PMF, draws);
    eq(freq.map((r) => r.count).join(', '), '10, 42, 86, 49, 13', 'the counts over 200 draws');
    eq(freq.map((r) => Rtext(r.expected)).join(', '), '25/2, 50, 75, 50, 25/2', 'against the expected counts');
    eq(freq.map((r) => Rtext(r.empirical)).join(' '), '1/20 21/100 43/100 49/200 13/200',
       'each empirical frequency an exact fraction of 200');
    eq(Rtext(sampleMean(draws)), '413/200', 'and the sample mean, exactly');
    eq(Rtext(simPmfMean(PMF)) + ', ' + Rtext(simPmfVar(PMF)), '2, 1',
       'the table has mean exactly 2 and variance exactly 1, which is why the halving below is exact');
    eq(hullDobell(25173n, 13849n, 65536n).join(','), 'true,true,true', 'Hull-Dobell holds for it');
    eq(lcgRun(25173n, 13849n, 65536n, 1n, 65537n).period, 65536, 'so the period is the full modulus');
    eq(hullDobell(2n, 4n, 16n).join(','), 'false,false,false',
       'the kit also offers a generator that fails all three conditions');
    eq(lcgRun(2n, 4n, 16n, 1n, 20n).period, 1, 'and its stream collapses to a single value');
    eq(hullDobell(16807n, 0n, 2147483647n)[0], false,
       'MINSTD itself fails the gcd(c, m) condition, because the theorem is about a MIXED generator');
    /* simDraws is the same rule in whole numbers, and it is held to it. */
    for (const seed of [1, 7, 19]) {
      eq(simDraws(PMF, seed, 400).map(Rtext).join(''),
         simUniform(seed, 400).map((u) => sampleFromPmf(PMF, u)).map(Rtext).join(''),
         'simDraws agrees with sampleFromPmf draw for draw, seed ' + seed);
    }
    const wide = simBinomPmf(10, rf(4, 5));
    eq(simDraws(wide, 3, 300).map(Rtext).join(','),
       simUniform(3, 300).map((u) => sampleFromPmf(wide, u)).map(Rtext).join(','),
       'and on a table whose denominators are past a double, where the comparison runs in BigInt');
  }

  /* --- the standard error, and the halving that is exact ------------------- */
  {
    const se = [100, 400, 1600].map((n) => simStandardError(simPmfVar(PMF), n));
    eq(se.map((s) => Rtext(s.q) + '|' + s.k).join(' '), '1/10|1 1/20|1 1/40|1',
       'sigma/root n at 100, 400 and 1600 is rational here: 1/10, 1/20, 1/40');
    eq(Rtext(Rsurd(Rdiv(rf(1, 100), rf(1, 400))).q), '2',
       'the RATIO of two standard errors squares to 4, so it is exactly 2 whatever sigma is');
    const d = simDraws(PMF, 1, 1600);
    const s2 = sampleVar(d.slice(0, 100));
    eq(Rtext(s2), '113/99', 'the sample variance at 100 draws off the kit stream');
    eq(surdtext(simStandardError(s2, 100)), '(1/330)sqrt(1243)', 'whose standard error is a surd');
    eq(surdDec(simStandardError(s2, 100), 5), '0.10684', 'printed rounded beside it, and labelled');
    eq(Rtext(sampleMean(d.slice(0, 400))), '413/200', 'and a 400-draw mean is a fraction');
  }

  /* --- Chebyshev: squares compared, and the width it costs ----------------- */
  {
    const mu = simPmfMean(PMF), varMean = Rdiv(simPmfVar(PMF), ri(100)), means = [];
    for (let j = 0; j < 40; j += 1) means.push(sampleMean(simDraws(PMF, 1 + 1000 * (j + 1), 100)));
    const c5 = chebyshevCover(means, mu, ri(5), varMean);
    const c2 = chebyshevCover(means, mu, ri(2), varMean);
    const c1 = chebyshevCover(means, mu, ri(1), varMean);
    eq(Rtext(c5.bound) + ' = ' + Rpct(c5.bound, 0), '24/25 = 96%', 'k = 5 guarantees 24/25, which is 96%');
    eq(Rtext(c2.bound), '3/4', 'and the folklore k = 2 guarantees 3/4 and nothing more');
    eq(Rtext(c1.bound), '0', 'while k = 1 guarantees nothing at all, which the page prints rather than hides');
    eq(Rtext(R(5n, 2n)), '5/2', 'so the width ratio against the folklore is exactly 5/2 -- 2.5 times as WIDE');
    eq(Rtext(Rmul(R(5n, 2n), R(5n, 2n))), '25/4', 'and matching that width with runs costs 25/4 times as many');
    eq(Rtext(c5.threshold), '1/4', 'the threshold is k^2 sigma^2/n exactly: no root is taken anywhere');
    eq(Rtext(c5.coverage) + ' ' + Rtext(c2.coverage) + ' ' + Rtext(c1.coverage), '1 1 5/8',
       'the coverage seen at k = 5, 2 and 1 -- a count, as an exact fraction');
    eq(c5.holds && c2.holds, true, 'both guarantees held, by a margin, which is what a worst case does');
    eq(c5.outside <= c2.outside && c2.outside <= c1.outside, true,
       'and a wider band can never exclude more replications');
  }

  /* --- the exact transient, and the three averages the lesson quotes ------- */
  {
    const p = rf(2, 5), q = rf(1, 2), tr = simTransient(p, q, 400, 48);
    eq([0, 1, 2, 3, 4].map((t) => Rtext(simTransientExact(tr, t))).join(', '),
       '0, 2/5, 3/5, 37/50, 17/20',
       'E[N_t] from an empty start -- which pins the slot convention, not just the arithmetic');
    eq(Rtext(geoGeo1(p, q).L), '12/5',
       'against the stationary mean, from the SAME geoGeo1 the System Design course prints');
    eq(Rfixed(simExpectedAverage(tr, 0, 100), 4), '1.8624', 'the expected time-average over slots 0 to 99');
    eq(Rfixed(simExpectedAverage(tr, 0, 400), 4), '2.2443', 'over 0 to 399, after quadrupling the run');
    eq(Rfixed(simExpectedAverage(tr, 100, 400), 4), '2.3717',
       'and over 100 to 399, after deleting a quarter of it -- which recovers far more than the quadrupling did');
    eq(Rcmp(simExpectedAverage(tr, 100, 400), simExpectedAverage(tr, 0, 400)) > 0, true,
       'so the bias from an empty start is downward, as theory and not as a story about noise');
    /* The page SAYS "the bias is downward" on whichever configuration is
       chosen, so it has to be downward on all three of them. */
    for (const [pn, pd, qn, qd] of [[2, 5, 1, 2], [2, 5, 3, 5], [1, 2, 3, 5]]) {
      const tk = simTransient(rf(pn, pd), rf(qn, qd), 400, 48);
      eq(Rcmp(simExpectedAverage(tk, 100, 400), simExpectedAverage(tk, 0, 400)) > 0, true,
         'and on every configuration the kit offers, including p = ' + pn + '/' + pd + ', q = ' + qn + '/' + qd);
      eq(Rcmp(simExpectedAverage(tk, 100, 400), geoGeo1(rf(pn, pd), rf(qn, qd)).L) < 0, true,
         'while still sitting below the stationary mean, which is what "climbing toward it" means');
    }
    eq(String(tr.nums[399]).length > 700, true,
       'the exact numerator at slot 399 is ' + String(tr.nums[399]).length + ' digits');
    eq(Number.isFinite(tr.values[399]), true,
       'and the value the curve is DRAWN from is finite -- Number(n)/Number(d) of that fraction is NaN');
    eq(tr.values[399].toFixed(4), Rfixed(simTransientRaw(tr, 399), 4),
       'and agrees with the exact value to every digit it is drawn at');
    eq(Rcmp(simTransientCapMass(tr, 399), rf(1, 1000000)) < 0, true,
       'the probability mass sitting on the truncation is under one in a million, and is printed');
    eq(Rtext(geoGeo1(p, rf(3, 5)).L), '6/5', 'the faster server exactly, for the comparison lesson');
    eq(Rtext(Rsub(geoGeo1(p, q).L, geoGeo1(p, rf(3, 5)).L)), '6/5',
       'so the true difference the two schemes compete to recover is 6/5');
  }

  /* --- the run, the calendar, and Little's Law as an identity -------------- */
  {
    const p = rf(2, 5), q = rf(1, 2), run = simSlotRun(p, q, 2000, 1);
    eq(run.arrivals.length === run.services.length, true, 'one service time per arrival');
    eq(run.arrivals.every((t, i) => i === 0 || t > run.arrivals[i - 1]), true,
       'arrivals are in order, at most one a slot');
    eq(run.departs.every((d, i) => d === Math.max(run.arrivals[i], i ? run.departs[i - 1] : 0) + run.services[i]),
       true, 'first in first out on a single server, never idle while anyone waits');
    eq(Requ(run.L, R(BigInt(run.area), BigInt(run.T))), true,
       'the time average is the area under the occupancy curve over the horizon');
    const little = littleFromTrace(run.arrivals, run.departs);
    eq(Requ(little.L, Rmul(little.lambda, little.W)), true,
       'L = lambda W holds on the trace as an identity about averages, with no model at all');
    eq(Rcmp(Rabs(Rsub(run.L, rf(12, 5))), ri(1)) < 0, true,
       'and the run lands within 1 of the exact 12/5: ' + Rfixed(run.L, 4));
    /* The head of a run is the head of the whole run, which is what makes the
       calendar affordable: desRun's per-event snapshots are quadratic. */
    const head = simRunHead(run, 12);
    eq(head.departs.join(','), run.departs.slice(0, 12).join(','),
       'the truncated head of a run is exactly the head of the whole run');
    const first = simCalendar(head, 24), again = simCalendar(head, 24);
    const render = (c) => c.events.map((e) => Rtext(e.t) + e.kind.charAt(0) + e.who + ':' + e.inSystem
      + '[' + (e.serving === null ? '-' : e.serving) + '|' + e.waiting.join(' ') + ']'
      + '(' + e.pending.length + '+' + e.pendingMore + ')').join(' ');
    eq(render(first), render(again),
       'rendering event i is a pure function of i, so a second window.redrawLab() reproduces the first');
    eq(first.events.every((e) => e.inSystem === (e.serving === null ? 0 : 1) + e.waiting.length), true,
       'in system EQUALS in service plus waiting at every event -- the count and the contents are one walk');
    /* And the contents are the RIGHT ones, not merely the right number of them.
       The server is first in first out and never idle while anyone is present,
       so the one in service is the earliest still-present customer: it is not
       also in the queue, everyone queued arrived after it, and the starts array
       -- which the walk never consults -- agrees about all of it. */
    eq(first.events.every((e) => e.serving === null || e.waiting.indexOf(e.serving) < 0), true,
       'the customer in service is not also listed as waiting');
    eq(first.events.every((e) => e.waiting.every((w) => w > e.serving)), true,
       'everyone waiting arrived after the one holding the server, because the queue is first in first out');
    eq(first.events.every((e) => {
      const clock = Number(e.t.n) / Number(e.t.d);
      if (e.serving !== null
          && !(head.starts[e.serving] <= clock && head.departs[e.serving] > clock)) return false;
      return e.waiting.every((w) => head.starts[w] > clock && head.arrivals[w] <= clock);
    }), true,
       'and the starts the walk never reads agree: the one in service has begun and none of the queue has');
    eq(first.events.every((e, i) => i === 0 || Rcmp(e.t, first.events[i - 1].t) >= 0), true,
       'and the clock never goes backwards');
    eq(first.events[0].kind, 'arrival', 'a run that starts empty starts with an arrival');
    eq(new Set(first.events.map((e) => e.pending.length + '/' + e.waiting.length)).size > 2, true,
       'the table takes ' + new Set(first.events.map((e) => e.pending.length + '/' + e.waiting.length)).size
       + ' distinct shapes over 24 events, which is what makes this lab the hard one');
    const occ = occupancyTrace(run.arrivals, run.departs, 40);
    eq(occ.length, 40, 'the occupancy the figure is drawn from is asked for by the slot, not by the run');
  }

  /* --- antithetic variates: the best case and the worst one ---------------- */
  {
    const g = (kind, u) => (kind === 'monotone'
      ? (Rcmp(u, rf(1, 2)) >= 0 ? R1 : R0)
      : Rabs(Rsub(u, rf(1, 2))));
    for (const kind of ['monotone', 'nonmonotone']) {
      const us = simUniform(8, 64), A = [], B = [], pairMeans = [];
      for (let i = 0; i < 64; i += 1) {
        const u = us[i];
        A.push(g(kind, u)); B.push(g(kind, Rsub(R1, u)));
        pairMeans.push(Rdiv(Radd(A[i], B[i]), ri(2)));
      }
      const vPair = sampleVar(pairMeans), vOne = sampleVar(A), vIndep = Rdiv(vOne, ri(2));
      eq(Rtext(rhoSquared(A, B)), '1', kind + ': the two draws of a pair are perfectly correlated');
      if (kind === 'monotone') {
        eq(pairMeans.every((m) => Requ(m, rf(1, 2))), true, 'every pair mean is exactly 1/2');
        eq(Rtext(vPair), '0', 'so the variance of the pair mean is exactly 0, against ' + Rtext(vIndep)
           + ' for an independent pair');
        eq(Requ(sampleCov(A, B), Rneg(vOne)), true,
           'because the covariance is exactly minus the variance of one draw -- rho is exactly -1');
      } else {
        eq(A.every((x, i) => Requ(x, B[i])), true, 'g(1 - U) is g(U) identically');
        eq(Requ(vPair, vOne), true, 'so the pair mean has exactly the variance of a single draw');
        eq(Rtext(Rdiv(vPair, vIndep)), '2',
           'which is exactly TWICE an independent pair: two draws consumed, one draw of precision');
        eq(Rsign(sampleCov(A, B)), 1, 'the covariance is positive, and rho is exactly +1');
      }
    }
  }

  /* --- control variates: the vertex, and the known mean it needs ----------- */
  {
    const p = rf(2, 5), q = rf(1, 2), X = [], C = [], F = [];
    for (let j = 0; j < 24; j += 1) {
      const s = 1 + 977 * j, run = simSlotRun(p, q, 200, s);
      X.push(run.L); C.push(ri(run.count));
      const raw = simStream(s + 400000, 200);
      let c = 0;
      for (let i = 0; i < 200; i += 1) if (2 * raw[i] < simModulus()) c += 1;
      F.push(ri(c));
    }
    const ctl = controlB(X, C), foreign = controlB(X, F);
    eq(Requ(ctl.varAt, Rmul(ctl.varRaw, Rsub(R1, ctl.rho2))), true,
       'the variance at b* is exactly Var X times 1 - rho^2, and both factors are rational');
    eq(Rsurd(ctl.rho2).k !== 1n, true,
       'rho itself is irrational here, which is why only rho^2 is ever printed');
    eq(Rsign(ctl.rho2) >= 0 && Rcmp(ctl.rho2, R1) <= 0, true, 'and rho^2 lies in [0, 1]');
    for (const d of [rf(1, 7), rf(-1, 3), ri(1), ri(-2), rf(1, 1000)]) {
      eq(Rcmp(controlVarAt(ctl.quadratic, Radd(ctl.bStar, d)), ctl.varAt) >= 0, true,
         'b* minimises the quadratic, at offset ' + Rtext(d));
    }
    eq(Rtext(Rmul(ri(200), p)), '80',
       'the arrivals control has mean exactly 80 -- KNOWN, which is the condition the method stands on');
    eq(Rcmp(ctl.rho2, foreign.rho2) > 0, true,
       'and it is better correlated (' + Rfixed(ctl.rho2, 4) + ') than a control from another stream ('
       + Rfixed(foreign.rho2, 4) + ')');
    eq(Rcmp(Rsub(R1, foreign.rho2), rf(9, 10)) > 0, true,
       'so a known mean ALONE buys almost nothing: that control leaves the factor above 9/10');
  }

  /* --- importance sampling: four orders of magnitude, and one refusal ------ */
  {
    const P = simBinomPmf(10, rf(1, 2)), at = ri(10);
    const hit = (x) => Rcmp(x, at) === 0;
    eq(Rtext(P[10][1]), '1/1024', 'ten fair coins all heads is exactly 1/1024');
    const good = importanceRun(P, simBinomPmf(10, rf(4, 5)), hit);
    const bad = importanceRun(P, simBinomPmf(10, rf(1, 5)), hit);
    const crude = importanceRun(P, P, hit);
    eq(Rtext(good.estimate) + ' ' + Rtext(bad.estimate), '1/1024 1/1024',
       'and every q that covers the support is unbiased for it -- the estimate is not where the difference is');
    eq(Rtext(good.varCrude), '1023/1048576', 'direct sampling has per-draw variance p(1 - p)');
    eq(Rtext(simBinomPmf(10, rf(4, 5))[10][1]), '1048576/9765625',
       'under a coin weighted to 4/5 the event has probability (4/5)^10');
    eq(Rtext(good.rows[10].w), '9765625/1073741824', 'and the weight on it is small');
    eq(Rtext(good.varIS), '8717049/1099511627776', 'so the per-draw variance is 8717049 over 2^40');
    eq(Rtext(good.ratio) + ' = ' + Rfixed(good.ratio, 2), '32505856/264153 = 123.06',
       'the variance is DIVIDED by 32505856/264153');
    eq(Rtext(bad.rows[10].w), '9765625/1024', 'under a coin weighted to 1/5 the one weight that matters explodes');
    eq(Rtext(bad.varIS), '1220703/131072', 'and the per-draw variance becomes 1220703/131072');
    eq(Rtext(Rinv(bad.ratio)) + ' = ' + Rfixed(Rinv(bad.ratio), 2), '295928/31 = 9546.06',
       'so the variance is MULTIPLIED by 295928/31 -- four orders of magnitude, same estimator');
    eq(Rtext(crude.ratio), '1', 'sampling from p itself is the identity');
    eq(crude.rows.every((r) => Requ(r.w, R1)), true, 'with every weight exactly 1');
    const holed = simHoledPmf(simBinomPmf(10, rf(4, 5)), at);
    let total = R0;
    holed.forEach((r) => { total = Radd(total, r[1]); });
    eq(Rtext(holed[10][1]) + ' ' + Rtext(total), '0 1',
       'the holed q is a proper distribution that simply never produces the event');
    const refused = importanceRun(P, holed, hit);
    eq(refused.refused && refused.estimate === null, true, 'and it is REFUSED rather than answered');
    eq(/likelihood ratio is undefined/.test(refused.why), true, 'with the reason given');
    const goodRun = simImportanceRun(P, simBinomPmf(10, rf(4, 5)), at, 2, 2000);
    const badRun = simImportanceRun(P, simBinomPmf(10, rf(1, 5)), at, 2, 2000);
    eq(goodRun.hits > 100, true, 'a good q hits the event ' + goodRun.hits + ' times in 2000 draws');
    eq(Rcmp(Rabs(Rsub(goodRun.estimate, rf(1, 1024))), rf(1, 2048)) < 0, true,
       'and its running estimate is within half the answer of the answer');
    eq(badRun.hits + ' ' + Rtext(badRun.estimate), '0 0',
       'a bad q hits it not once, so its estimate is exactly zero -- not near the answer, AT zero');
  }

  /* --- the drawings: strings, no document, no NaN -------------------------- */
  {
    const stair = simStaircase(simCumulative(PMF), simUniform(1, 12), { width: 660, height: 240 });
    eq((stair.svg.match(/<rect /g) || []).length, 5, 'the staircase draws one band per outcome');
    eq((stair.svg.match(/<circle /g) || []).length, 12, 'and one mark per draw shown');
    const plot = simPlot({ width: 660, height: 230,
      series: [{ pts: [[0, 1], [1, 2], [2, 3]], tone: 'cyan', dots: true }],
      bands: [{ pts: [[0, 0, 2], [2, 1, 3]], tone: 'amber' }],
      rules: [{ y: 2, tone: 'green', label: 'exact' }],
      spans: [{ x0: 0, x1: 1, tone: 'amber', label: 'discarded' }],
      marks: [{ x: 1, y: 2, tone: 'purple', label: 'b*' }],
      drops: [{ x: 1, label: 'clock' }] });
    eq((plot.svg.match(/<polygon /g) || []).length, 1, 'the ribbon is a single polygon');
    eq((plot.svg.match(/<path /g) || []).length, 1, 'the series is a single path');
    eq((plot.svg.match(/<circle /g) || []).length, 4, 'and every sample and the vertex are marked');
    eq(/NaN|Infinity|undefined/.test(plot.svg), false, 'no coordinate on it is NaN');
    eq(simPlot({ series: [] }).svg.indexOf('nothing to draw') > 0, true,
       'and an empty figure says so rather than throwing');
    eq((simBars([{ label: 'a', value: ri(10), tone: 'amber' },
                 { label: 'b', value: ri(5), tone: 'green' }], { width: 660 })
        .svg.match(/<rect /g) || []).length, 2, 'the bars draw one bar each');
    eq(simEsc('a < b & c'), 'a &lt; b &amp; c', 'reader text is escaped before it reaches innerHTML');
    eq(simNum(rf(1, 3)), '1/3', 'a short fraction prints exactly');
    eq(simNum(R(12345678901234567890n, 99999999999999999n)),
       '123.45679 (exact, shown to 5 places)',
       'a fraction too wide to read prints a decimal that says it is EXACT and merely shown short');
    eq(/rounded/.test(simNum(R(12345678901234567890n, 99999999999999999n))), false,
       'and never says "rounded", which on this course is reserved for the three genuinely irrational figures');
    eq(simSurd(Rsurd(rf(1, 100))), '1/10', 'a rational root prints as a fraction');
    eq(simSurd(Rsurd(rf(1, 50)), 4), '(1/10)sqrt(2) = 0.1414 (rounded)',
       'and an irrational one as a surd with its rounded decimal beside it');
    eq(simReadInt('abc', 1, 10), null, 'reader input that is not a number is refused, not parsed');
    eq(simReadInt('70', 1, 10), null, 'nor is one out of range');
    eq(simReadInt('7', 1, 10), 7n, 'while a good one comes back as a BigInt');
  }
}



// ----------------------------------------------------------------- graphkit
console.log('graph algorithms: the kit that checks itself against three other answers');
{
  /* This section is about AGREEMENT, because that is what the kit's pages show.
     Three kinds of it, and each is the reason a page can print a verdict:

       against graph.py      `cuts()`, `kruskal()` and `dijkstra()` were written
                             for another Subject, are undirected, and know
                             nothing about this representation. `dgToMatrix`
                             plus `lessonFrom` hand them a graph built here.
       against an enumeration  every spanning tree, every topological order,
                             every subset -- so a statement about all of them is
                             read off a list at a cap this file also tests.
       against a second algorithm here  Floyd against Bellman-Ford, the one-pass
                             DAG relaxation against both, and Kosaraju against
                             mutual reachability computed from the definition.

     The preset graphs asserted on are the ones the pages open with, so a change
     that breaks a lesson's opening figure fails here rather than in a browser. */
  const GRAPHKIT_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'graphkit.py');
  const graphkitSrc = fs.readFileSync(GRAPHKIT_SOURCE, 'utf8');
  const gkBlock = (name) => blockFrom(graphkitSrc, name, GRAPHKIT_SOURCE);
  eval(algoBlock('ALGO_JS'));
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('DIGRAPH_JS'));
  eval(algoCoreBlock('ORACLE_JS'));
  eval(algoCoreBlock('GRAPHKIT_JS'));
  eval(gkBlock('GKIT_JS'));
  eval(graphBlock('GRAPH_JS'));

  const parse = (text, directed) => gkParse(text, directed);
  const good = (text, directed) => {
    const p = parse(text, directed);
    if (p.bad) { fails += 1; console.log('  FAIL parsing ' + text + ': ' + p.bad); }
    return p.G;
  };
  /* Hand a graph built here to graph.py, the way the three checked modes do. */
  const handOver = (G) => {
    N = G.n; A = dgToMatrix(G);
    LESSON = lessonFrom(gkLessonList(G)); useLessonWeights = true;
  };

  /* --- what a reader types, and what is refused ------------------------- */
  {
    eq(good('1>2 4, 2>3 3', true).arcs.map((a) => a.u + '-' + a.v + ':' + a.w).join(' '),
       '0-1:4 1-2:3', 'a clause is tail, head, weight, and the labels are 1-based on the page');
    eq(good('1-2, 2-3', false).arcs.every((a) => a.w === 1), true,
       'a weight left out is 1');
    eq(good('1>2 -7', true).arcs[0].w, -7, 'and a weight may be negative, which graph.py cannot express');
    eq(parse('1>1 3', true).bad !== undefined, true, 'a loop is refused');
    eq(parse('0>2', true).bad !== undefined, true, 'so is a label below 1');
    eq(parse('1>99', true).bad !== undefined, true, 'and one past the cap');
    eq(parse('', true).bad !== undefined, true, 'an empty graph is refused rather than drawn empty');
    eq(parse('1-2-3', true).bad !== undefined, true, 'and so is a clause that is not one arc');
    eq(gkParseSet('1, 3', 4).set.join(','), '0,2', 'a vertex set is 1-based too');
    eq(gkParseSet('1, 9', 4).bad !== undefined, true, 'and a vertex the graph does not have is refused');
    eq(gkParallelPairs(good('1>2, 2>1, 2>3', true)).length, 1,
       'two arcs between one pair are found, because a matrix cannot hold them');
    eq(gkOracleReady(good('1>2, 2>1', true)).ok, false, 'so the matrix oracle is not asked about that graph');
    eq(gkOracleReady(good('1>2, 2>3', true)).ok, true, 'and is asked about one it can hold');
  }

  /* --- dfstimes: the parenthesis theorem, on every ordered pair ---------- */
  {
    const G = good('1>2, 1>4, 2>5, 4>2, 5>4, 3>5, 3>6, 6>3', true);
    const t = dfsTimes(G, gkRootsFrom(0, 6)).result;
    const k = edgeKindCounts(classifyEdges(G, t));
    eq([k.tree, k.back, k.forward, k.cross].join(','), '4,2,1,1',
       'the opening graph of the timestamp page has all four edge classes on it');
    const paren = parenthesisCheck(t);
    eq(paren.overlapping, 0, 'no two intervals overlap without nesting, which is the theorem');
    eq(paren.violations.length, 0, 'and nesting and descent agree on every one of the 30 ordered pairs');
    eq(paren.nested + paren.disjoint + paren.overlapping, paren.pairs,
       'every pair of intervals is nested, disjoint or overlapping, and there are C(6, 2) = '
       + paren.pairs + ' of them');
    /* The misconception, computed: read the same arcs undirected and the two
       directed classes go to zero. Swept over graph.py's own presets so it is a
       claim about graphs rather than about one drawing. */
    for (const [preset, n] of [['cycle', 6], ['tree', 7], ['path', 6], ['petersen', 6],
                               ['complete', 5], ['star', 6], ['bipartite', 6]]) {
      LESSON = null; useLessonWeights = false; N = n; A = PRESETS[preset](n);
      const H = dgFromMatrix(A, n, weight, false);
      const u = gkUndirectedKinds(H, gkRootsFrom(0, n));
      eq(u.counts.forward + ',' + u.counts.cross, '0,0',
         'read undirected, ' + preset + ' has no forward and no cross edge');
      eq(u.counts.tree + u.counts.back, H.arcs.length, 'and every edge is tree or back');
      eq(u.counts.tree, n - dgComponents(H).length,
         'with exactly V minus the number of pieces tree edges');
    }
  }

  /* --- topo: two orders, and a COUNT for "is it unique" ------------------ */
  {
    const diamond = good('1>2, 1>3, 2>4, 3>4', true);
    eq(topoAllOrders(diamond, 8).result.count, 2, 'a diamond has exactly two topological orders');
    eq(topoAllOrders(good('1>2, 2>3, 3>4, 4>5', true), 8).result.count, 1,
       'a chain has one, which is what uniqueness looks like as a number');
    const free = dgNew(5, true);
    eq(topoAllOrders(free, 8).result.count, 120, 'five vertices and no arcs have 5! = 120');
    eq(topoAllOrders(good('1>3, 2>3, 3>4, 3>5, 4>6, 5>6', true), 8).result.count, 4,
       'and the page’s opening graph has four');
    for (const spec of ['1>2, 1>3, 2>4, 3>4', '1>3, 2>3, 3>4, 3>5, 4>6, 5>6', '1>2, 2>3, 3>4, 4>5']) {
      const G = good(spec, true);
      eq(gkValidOrder(G, topoDfs(G).result.order), true,
         'reverse finishing order is a valid order of ' + spec);
      eq(gkValidOrder(G, topoKahn(G).result.order), true, 'and so is Kahn’s');
      topoAllOrders(G, 8).result.orders.forEach((o) => {
        eq(gkValidOrder(G, o), true, 'and every enumerated order of ' + spec + ' is valid too');
      });
    }
    const cyc = good('1>2, 2>3, 3>1, 3>4', true);
    eq(topoDfs(cyc).result.order, null, 'on a cycle no order exists');
    eq(topoAllOrders(cyc, 8).result.count, 0, 'and the enumeration finds none, which is the same fact twice');
    eq(gkValidOrder(cyc, [0, 1, 2, 3]), false, 'a plausible-looking order on it is rejected arc by arc');
    const refuses = (f) => { try { f(); return false; } catch (e) { return /exceeds the exhaustive cap/.test(e.message); } };
    eq(refuses(() => topoAllOrders(dgNew(9, true), 8)), true,
       'nine vertices is refused through oracleCap rather than run slowly');
  }

  /* --- lowlink, kruskal and relax against graph.py, on the pages' own graphs */
  {
    const SPECS = ['1-2, 2-3, 3-1, 3-4, 4-5, 5-6, 6-4',
                   '1-2, 1-3, 2-3, 1-4',
                   '1-2, 2-3, 3-4, 4-5, 5-1',
                   '1-2, 2-3, 3-4, 4-5'];
    for (const spec of SPECS) {
      const G = good(spec, false);
      handOver(G);
      const mine = lowLink(G), theirs = cuts();
      const pairOf = (a, b) => Math.min(a, b) + '-' + Math.max(a, b);
      eq(mine.result.bridges.map((b) => pairOf(b.u, b.v)).sort().join(' '),
         theirs.bridges.map((b) => pairOf(b.edge[0], b.edge[1])).sort().join(' '),
         'lowLink and delete-and-recount find the same bridges of ' + spec);
      eq(mine.result.cutVertices.join(','), theirs.cutVertices.join(','),
         'and the same cut vertices');
      /* The DFS tree the page draws beside the low-links is dfsTimes'; if the
         two walks differed the parent column would describe another tree. */
      const tree = dfsTimes(G).result;
      for (let v = 0; v < G.n; v += 1) {
        if (tree.parent[v] === -1) continue;
        eq(mine.result.d[tree.parent[v]] < mine.result.d[v], true,
           'the tree the page prints is the walk the low-links came from, on ' + spec);
      }
    }
    /* The parallel pair: a second edge between the same two vertices stops that
       pair being a bridge, and the matrix oracle cannot be asked at all. */
    const par = good('1-2, 1-2, 2-3', false);
    eq(lowLink(par).result.bridges.map((b) => (b.u + 1) + '-' + (b.v + 1)).join(' '), '2-3',
       'with two edges between 1 and 2 the only bridge is 2-3: exclusion is BY ARC, not by endpoint');
    eq(gkOracleReady(par).ok, false, 'and the matrix brute force cannot be handed that graph');
    eq(lowLink(good('1-2, 2-3', false)).result.bridges.length, 2,
       'while one edge between 1 and 2 leaves both edges bridges');

    for (const spec of ['1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6, 5-7 8, 6-7 2',
                        '1-2 1, 2-3 2, 3-4 3, 4-5 4, 5-6 5, 1-6 9',
                        '1-2 1, 1-3 2, 1-4 3, 1-5 4, 2-3 5, 2-4 6, 2-5 7, 3-4 8, 3-5 9, 4-5 1']) {
      const G = good(spec, false);
      handOver(G);
      eq(kruskalRun(G).result.weight, kruskal().total,
         'kruskalRun agrees with graph.py’s own Kruskal on ' + spec);
      eq(primRun(G, 0).result.weight, kruskal().total,
         'and growing one tree from a heap reaches the same weight');
      eq(primRun(G, 0).result.bound, G.arcs.length * ilog2(Math.max(2, G.n)),
         'the E log V column is ilog2 from the shipped block, not a second logarithm');
      eq(gkHeapBound(G), primRun(G, 0).result.bound, 'and the kit computes the same reference');
      for (const source of [0, 1, G.n - 1]) {
        handOver(G);
        const theirs = dijkstra(source);
        for (const sched of ['heap', 'scan', 'insertion']) {
          const run = relaxRun(G, source, sched);
          eq(gkSameDistances(run.result.dist, theirs.dist), true,
             'the ' + sched + ' schedule reaches graph.py’s distances from ' + (source + 1));
          const inv = relaxInvariant(G, source, run);
          eq(inv.holds, true, 'and d[v] is never below the true distance at any step of it');
          eq(inv.exact, true, 'and every label ends exact');
        }
        eq(relaxRun(G, source, 'heap').counts.relaxations
           === relaxRun(G, source, 'insertion').counts.relaxations, false,
           'while the three schedules do different amounts of work for that one answer');
      }
    }
  }

  /* --- scc: Kosaraju against mutual reachability, straight from the definition */
  {
    for (const spec of ['1>2, 2>3, 3>1, 3>4, 4>5, 5>6, 6>4, 5>7',
                        '1>2, 2>3, 3>4, 4>1',
                        '1>2, 2>3, 1>3, 3>4',
                        '1>2, 2>1, 2>3, 3>4, 4>3']) {
      const G = good(spec, true);
      const mine = kosaraju(G).result, brute = sccBrute(G);
      eq(samePartition(mine.components, brute.components), true,
         'Kosaraju and mutual reachability agree on the components of ' + spec);
      eq(mine.condensationAcyclic, true, 'and the condensation of ' + spec + ' is acyclic');
      /* The misconception, computed: decreasing finish order names a SOURCE of
         the condensation, which is why the second pass is on the transpose. */
      const home = mine.componentOf[mine.order[0]];
      eq(dgIndeg(mine.condensation, home), 0,
         'the latest finishing vertex lies in a component nothing points into, on ' + spec);
    }
    eq(kosaraju(good('1>2, 2>1, 2>3, 3>4, 4>3', true)).result.components
       .map((c) => '{' + c.map((v) => v + 1).join(' ') + '}').join(' '), '{1 2} {3 4}',
       'and the source component is found before the sink one');
  }

  /* --- the cut property, against EVERY spanning tree and EVERY cut -------- */
  {
    const G = good('1-2 4, 1-3 3, 2-3 2, 2-4 5, 3-4 7, 4-5 1, 5-6 6', false);
    let checked = 0;
    forEachSubset(G.n, (mask) => {
      if (mask === 0 || mask === (1 << G.n) - 1) return;
      const S = maskMembers(mask, G.n);
      const v = cutVerdict(G, S, 7);
      if (!v.lightest) return;
      checked += 1;
      eq(v.inSome, true, 'the lightest edge across {' + S.map((x) => x + 1).join(',')
         + '} is in some minimum spanning tree');
      if (v.ties === 1) {
        eq(v.inEvery, true, 'and being STRICTLY lightest across it, in every one');
      }
    });
    eq(checked, 62, 'checked on all 2^6 - 2 proper cuts of the page’s opening graph');
    const v0 = cutVerdict(G, [0, 1, 2], 7);
    eq(v0.trees + ',' + v0.msts + ',' + v0.minWeight, '8,1,17',
       'eight spanning trees, one of them minimum, at weight 17');
    eq(v0.unique, true, 'so with distinct weights the minimum tree is unique');
    eq(kruskalRun(G).result.weight, v0.minWeight,
       'and the enumeration agrees with the sorted, union-find method');
    /* The cycle property is the same table read the other way: an arc in no
       minimum tree is the heaviest on a cycle. */
    const cyc = good('1-2 1, 2-3 2, 3-4 3, 4-1 9, 2-4 4', false);
    const vc = cutVerdict(cyc, [0], 7);
    eq(vc.perArc.map((c, id) => c === 0 ? id : -1).filter((x) => x >= 0).join(','), '3,4',
       'the two arcs each heaviest on a cycle are in NO minimum spanning tree');
    eq(vc.mstList.length + ',' + vc.minWeight, '1,6', 'and the one minimum tree weighs 6');
    /* The other misconception: each vertex's own lightest edge. */
    const per = good('1-2 1, 2-3 5, 3-4 1, 4-5 6, 5-6 1', false);
    const lp = lightestPerVertex(per);
    eq(lp.arcs.length + ',' + lp.spans + ',' + lp.pieces, '3,false,3',
       'the lightest edge at each vertex gives three edges on six vertices: not a spanning tree');
    const vp = cutVerdict(per, [0], 7);
    lp.arcs.forEach((id) => {
      eq(vp.perArc[id] > 0, true, 'though every one of them IS in a minimum spanning tree');
    });
  }

  /* --- rounds, one pass, and the matrix, each against the others ---------- */
  {
    const neg = good('1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, 4>2 -2, 5>1 2, 5>4 7', true);
    const bf = bellmanFordRounds(neg, 0).result;
    eq(bf.dist.join(','), '0,2,7,4,-2', 'the page’s negative-weight graph has these distances');
    eq(bf.negativeCycle, null, 'and no negative cycle, which is what makes them exist');
    for (let v = 0; v < neg.n; v += 1) {
      const arcs = gkArcsOnPath(bf.parent, 0, v);
      eq(bf.finalAt[v] <= arcs, true,
         'label ' + (v + 1) + ' became final no later than the ' + arcs + ' arcs on its own path');
    }
    /* The bound is an upper bound and the ARC ORDER decides how tight it is --
       the two chain examples on the page differ by nothing else. */
    const worst = good('5>6 1, 4>5 1, 3>4 1, 2>3 1, 1>2 1', true);
    const best = good('1>2 1, 2>3 1, 3>4 1, 4>5 1, 5>6 1', true);
    eq(bellmanFordRounds(worst, 0).result.finalAt.join(','), '0,1,2,3,4,5',
       'typed backwards, one label becomes final per round');
    eq(bellmanFordRounds(best, 0).result.finalAt.join(','), '0,1,1,1,1,1',
       'typed forwards, every label becomes final in the first round');
    eq(bellmanFordRounds(worst, 0).result.dist.join(','),
       bellmanFordRounds(best, 0).result.dist.join(','), 'and both reach the same distances');
    const cyc = good('1>2 1, 2>3 -3, 3>4 1, 4>2 1', true);
    eq(bellmanFordRounds(cyc, 0).result.negativeCycle.map((v) => v + 1).join(' '), '2 3 4 2',
       'a negative cycle comes back as the cycle itself');
    /* Floyd against the rounds method, every pair, and the diagonal as the
       negative-cycle detector it is. */
    for (const spec of ['1>2 6, 2>4 9, 3>2 2, 4>3 8',
                        '1>2 6, 1>3 7, 2>3 8, 2>4 5, 2>5 -4, 3>4 -3, 3>5 9, 4>2 -2, 5>1 2, 5>4 7',
                        '1>2 1, 2>3 1, 3>4 1, 4>5 1']) {
      const G = good(spec, true);
      const F = floydSteps(dgWeightMatrix(G)).result;
      eq(F.negativeCycleAt.length, 0, 'no negative diagonal on ' + spec);
      for (let i = 0; i < G.n; i += 1) {
        eq(F.dist[i].join(','), bellmanFordRounds(G, i).result.dist.join(','),
           'the matrix row from ' + (i + 1) + ' is the rounds method’s answer, on ' + spec);
      }
    }
    eq(floydSteps(dgWeightMatrix(good('1>2 6, 2>4 9, 3>2 2, 4>3 8', true))).result.dist[0][2], 23,
       'and 1 to 3 is 23 through TWO interior vertices, which the k loop must be outermost to find');
    eq(floydSteps(dgWeightMatrix(good('1>2 1, 2>3 -3, 3>4 1, 4>2 1', true)))
       .result.negativeCycleAt.length > 0, true,
       'a negative cycle shows on the diagonal with no separate check');
    const path = floydSteps(dgWeightMatrix(good('1>2 6, 2>4 9, 3>2 2, 4>3 8', true))).result;
    eq(gkPathText(floydPath(path.next, 0, 2)), '1 → 2 → 4 → 3',
       'and next[] rebuilds that path one hop at a time');
  }

  /* --- one pass in topological order, and where the settled set goes wrong */
  {
    const dag = good('1>2 3, 1>3 2, 2>4 4, 3>4 1, 4>5 2, 3>5 7, 5>6 1', true);
    eq(dagRelax(dag, 0, 1).result.dist.join(','), '0,3,2,3,5,6', 'one pass gives shortest paths');
    eq(dagRelax(dag, 0, -1).result.dist.join(','), '0,3,2,7,9,10', 'and the sign flipped, longest');
    eq(dagRelax(dag, 0, 1).counts.relaxations, dag.arcs.length,
       'in exactly one relaxation per arc, because nothing is relaxed twice');
    eq(dagRelax(dag, 0, -1).result.slack.join(','), '0,0,0,0,0,0',
       'on the longest reading every vertex here is on a critical path, so nothing has slack');
    eq(dagRelax(dag, 0, -1).result.latest.join(','), '0,3,2,7,9,10',
       'the latest each may sit is its earliest, because the backward pass is SEEDED at the far '
       + 'end and takes the minimum over successors -- doing either the other way reports slack '
       + 'on a vertex that is on every critical path');
    eq(dagRelax(dag, 0, 1).result.slack.join(','), '0,4,0,0,0,0',
       'while on the shortest reading vertex 2 is 4 longer than necessary, and slack is never '
       + 'negative under either reading');
    eq(dagRelax(dag, 0, 1).result.extreme + ',' + dagRelax(dag, 0, -1).result.extreme, '5,5',
       'and the far end is the largest distance under either sign, because the longest path is '
       + 'the negated weights and not a reversed comparison');
    /* THE COMPARISON THE PAGE PRINTS. On a DAG with a negative arc the settled
       set is wrong and the one pass is right, and the gap is a vertex whose
       outgoing arcs were relaxed from a label that later improved. */
    const trap = good('1>2 2, 1>3 3, 3>2 -2, 2>4 1', true);
    eq(dagRelax(trap, 0, 1).result.dist.join(','), '0,1,3,2',
       'one pass in topological order is right on the negative arc');
    eq(bellmanFordRounds(trap, 0).result.dist.join(','), '0,1,3,2', 'the rounds method agrees');
    eq(relaxRun(trap, 0, 'heap').result.dist.join(','), '0,1,3,3',
       'and nearest-unsettled-first is WRONG at the far end: 2 was settled, its arc to 4 was '
       + 'relaxed from the label it had then, and nothing went back');
    /* Negating a graph with a cycle is the thing the trick cannot survive. */
    const cyc = good('1>2 3, 2>3 2, 3>1 1, 3>4 5', true);
    eq(topoDfs(cyc).result.acyclic, false, 'a graph with a cycle has no topological order');
    eq(dagRelax(cyc, 0, 1).result.dist, null, 'so the one pass refuses rather than returning numbers');
    eq(gkNegate(cyc).arcs.map((a) => a.w).join(','), '-3,-2,-1,-5', 'negating flips every weight');
    eq(bellmanFordRounds(gkNegate(cyc), 0).result.negativeCycle !== null, true,
       'and the negated cycle is a NEGATIVE cycle, so no longest walk exists to be found');
  }
}

// ----------------------------------------------------------------- flowkit
console.log('flow: the algorithm that certifies its own answer, checked against every cut');
{
  /* THE SPINE, asserted on every network the four pages open with: the value
     the augmenting-path algorithm reaches, the capacity of the cut it reads off
     its own final residual network, and the smallest capacity among EVERY set
     holding the source and not the sink. Three numbers by three routes, and the
     theorem is that they are one number.

     The rest of this section is the four misconceptions, each computed rather
     than described: a forward-only search that stops below the maximum, a full
     arc that is in no cut, a matching nothing can be added to that is not
     maximum, and a vertex capacity that needs no new algorithm. */
  const FLOWKIT_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'flowkit.py');
  const flowkitSrc = fs.readFileSync(FLOWKIT_SOURCE, 'utf8');
  const fkBlock = (name) => blockFrom(flowkitSrc, name, FLOWKIT_SOURCE);
  eval(algoCoreBlock('COUNT_JS'));
  eval(algoCoreBlock('DIGRAPH_JS'));
  eval(algoCoreBlock('ORACLE_JS'));
  eval(algoCoreBlock('FLOW_JS'));
  eval(fkBlock('FKIT_JS'));

  const net = (text) => {
    const p = fkParse(text);
    if (p.bad) { fails += 1; console.log('  FAIL parsing ' + text + ': ' + p.bad); }
    return p.G;
  };

  /* --- what a reader types ----------------------------------------------- */
  {
    eq(net('1>2 16, 2>3 4').arcs.map((a) => a.u + '-' + a.v + ':' + a.cap).join(' '),
       '0-1:16 1-2:4', 'a clause is tail, head, capacity, and the capacity lands on cap');
    eq(net('1>2').arcs[0].cap, 1, 'a capacity left out is 1');
    eq(fkParse('1>2 -3').bad !== undefined, true, 'a negative capacity is refused');
    eq(fkParse('1>1 3').bad !== undefined, true, 'and so is a loop');
    eq(fkParse('1-2 3').bad !== undefined, true,
       'and so is an undirected clause: every arc in a flow network points one way');
    eq(fkParsePairs('2-1, 1-2', 2, 2).pairs.map((p) => p.join('')).join(' '), '10 01',
       'a bipartite pair is left then right, 1-based');
    eq(fkParsePairs('3-1', 2, 2).bad !== undefined, true, 'a pair off the left side is refused');
    eq(net('1>2 3, 1>2 4, 2>3 5').arcs.length, 3,
       'two arcs between the same pair are TWO arcs, which is what the flow array is indexed by');
  }

  /* --- the spine: three routes to one number ------------------------------ */
  {
    const CASES = [
      ['1>2 16, 1>3 13, 2>3 10, 3>2 4, 2>4 12, 3>5 14, 4>3 9, 5>4 7, 4>6 20, 5>6 4', 0, 5, 23],
      ['1>2 1, 1>3 1, 2>3 1, 2>4 1, 3>4 1', 0, 3, 2],
      ['1>2 100, 1>3 100, 2>3 1, 2>4 100, 3>4 100', 0, 3, 200],
      ['1>2 3, 1>2 4, 2>3 5', 0, 2, 5],
      ['1>2 1, 2>3 1, 3>4 5, 1>4 1', 0, 3, 2],
      ['1>2 1, 2>3 1, 3>4 1', 0, 3, 1],
      ['1>2 5, 2>3 5, 3>2 9, 3>4 5, 2>4 1', 0, 3, 5],
    ];
    for (const [spec, s, t, want] of CASES) {
      const G = net(spec);
      const run = maxflow(G, s, t);
      const cut = minCutFrom(G, run.result.flow, s);
      const brute = minCutBrute(G, s, t, 10);
      eq(run.result.value, want, 'the maximum flow of ' + spec + ' is ' + want);
      eq(cut.capacity, run.result.value,
         'and the cut read off its own residual network has exactly that capacity');
      eq(brute.result.capacity, run.result.value,
         'and so does the smallest of all ' + brute.result.count + ' cuts, found without a flow');
      eq(cutIsMinimum(brute, cut.S), true, 'the cut the algorithm returned is one of the smallest');
      eq(cut.allSaturated, true, 'every arc leaving the cut is full, or the search would have crossed it');
      eq(fkCheckFlow(G, run.result.flow, s, t).ok, true,
         'and what came back is a flow: conserved inside, and inside every capacity');
      eq(run.result.conserved, true, 'which maxflow also reports for itself');
    }
    /* Capacity leaving, and capacity coming back, are different sums. */
    const back = net('1>2 5, 2>3 5, 3>2 9, 3>4 5, 2>4 1');
    const inS = [true, true, true, false];
    eq(cutCapacity(back, inS) + ',' + cutBack(back, inS), '6,0',
       'the cut {1,2,3} leaves 5 and 1 and takes nothing back');
    const inS2 = [true, true, false, false];
    eq(cutCapacity(back, inS2) + ',' + cutBack(back, inS2), '6,9',
       'while {1,2} has 9 coming back into it, and that 9 counts for NOTHING in its capacity');
  }

  /* --- the backward arc, and what happens without it ---------------------- */
  {
    const trap = net('1>2 1, 1>3 1, 2>3 1, 2>4 1, 3>4 1');
    const dfsNo = fkAugmentations(trap, 0, 3, { rule: 'dfs', reverse: false });
    const dfsYes = fkAugmentations(trap, 0, 3, { rule: 'dfs', reverse: true });
    const bfsNo = fkAugmentations(trap, 0, 3, { rule: 'bfs', reverse: false });
    eq(dfsNo.value, 1, 'first path found, no backward arcs: the search stops at 1');
    eq(dfsYes.value, 2, 'the same rule WITH backward arcs reaches 2, which is the maximum');
    eq(bfsNo.value, 2,
       'and the shortest-path rule never takes the middle arc, so it does not need one here -- '
       + 'which is why the failure is exhibited with a rule and not with a hand-picked path');
    eq(dfsNo.steps[0].path.length, 3, 'the first path it took has three arcs, through the middle');
    eq(dfsNo.steps[dfsNo.steps.length - 1].reachable.join(','), '0,2',
       'and afterwards the search reaches only 1 and 3, though no arc out of the source is full');
    eq(trap.arcs[0].cap - dfsNo.flow[0], 0, 'arc 1 to 2 is full');
    eq(trap.arcs[1].cap - dfsNo.flow[1], 1, 'while arc 1 to 3 still has spare capacity');
    const usedBack = dfsYes.steps.some((st) => st.path
      && st.path.some((rid) => !st.residual.meta[rid].forward));
    eq(usedBack, true, 'the augmentation that finished it used a backward arc');
    eq(fkCheckFlow(trap, dfsNo.flow, 0, 3).ok, true,
       'the stuck flow is still a legal flow -- it is maximal and not maximum, which is the point');
    /* The path RULE costs augmentations, on a network where the choice shows. */
    const zig = net('1>2 100, 1>3 100, 2>3 1, 2>4 100, 3>4 100');
    const byBfs = fkAugmentations(zig, 0, 3, { rule: 'bfs', reverse: true });
    const byDfs = fkAugmentations(zig, 0, 3, { rule: 'dfs', reverse: true });
    eq(byBfs.value + ',' + byDfs.value, '200,200', 'both rules reach the maximum');
    eq(byBfs.augmentations < byDfs.augmentations, true,
       'and the shortest-path rule gets there in fewer augmentations: ' + byBfs.augmentations
       + ' against ' + byDfs.augmentations);
    eq(maxflow(zig, 0, 3).result.augmentations, byBfs.augmentations,
       'which is the rule maxflow itself uses');
  }

  /* --- full is not the same as being in a cut ----------------------------- */
  {
    const G = net('1>2 1, 2>3 1, 3>4 5, 1>4 1');
    const run = maxflow(G, 0, 3), f = run.result.flow;
    const cut = minCutFrom(G, f, 0);
    const sat = saturatedArcs(G, f);
    const inCut = {};
    cut.arcs.forEach((e) => { inCut[e.id] = true; });
    const loose = sat.filter((id) => !inCut[id]);
    eq(sat.length + ',' + cut.arcs.length, '3,2', 'three arcs are full and two of them are the cut');
    eq(loose.map((id) => (G.arcs[id].u + 1) + '->' + (G.arcs[id].v + 1)).join(','), '2->3',
       'the third full arc is 2 to 3, which is in no cut at all');
    eq(reachesWithout(G, loose, 0, 3).reaches, true,
       'and deleting it leaves the sink reachable, so being full does not make an arc a cut');
    eq(reachesWithout(G, cut.arcs.map((e) => e.id), 0, 3).reaches, false,
       'while deleting the cut does separate them, which is what a cut IS');
    /* Several minimum cuts: the algorithm returns one and the enumeration finds
       them all, so "the minimum cut" is a set and not the set. */
    const chain = net('1>2 1, 2>3 1, 3>4 1');
    const b = minCutBrute(chain, 0, 3, 10);
    eq(b.result.minimal.length, 3, 'a chain of three unit arcs has three different minimum cuts');
    eq(cutIsMinimum(b, minCutFrom(chain, maxflow(chain, 0, 3).result.flow, 0).S), true,
       'and the one the algorithm returns is among them');
  }

  /* --- matching, four answers, one number --------------------------------- */
  {
    const CASES = [
      [2, 2, [[1, 1], [0, 1], [1, 0]], 2],
      [3, 3, [[0, 0], [0, 1], [1, 1], [1, 2], [2, 0], [2, 2]], 3],
      [3, 2, [[0, 0], [1, 0], [2, 0], [2, 1]], 2],
      [4, 4, [[0, 0], [1, 0], [2, 0], [3, 0], [3, 3]], 2],
    ];
    for (const [left, right, pairs, want] of CASES) {
      const n = matchingNetwork(left, right, pairs);
      const run = maxflow(n.graph, n.s, n.t), f = run.result.flow;
      const m = matchingFrom(n, f), cover = konigCover(n, f);
      const brute = matchingBrute(pairs, 16);
      eq(run.result.value, want, 'the maximum matching on ' + left + ' and ' + right
         + ' with ' + pairs.length + ' pairs is ' + want);
      eq(m.length, run.result.value, 'the saturated middle layer IS the matching');
      eq(cover.size, run.result.value,
         'and the cut read as a vertex cover has the same size, which is the theorem');
      eq(brute.result.value, run.result.value,
         'as does the largest subset of the pairs with no shared end, found without a network');
      eq(f.every((x) => x === Math.round(x) && x >= 0), true,
         'every flow value is a whole number, because every capacity is 1');
      /* Every matched pair is covered, which is what makes the cover a cover. */
      const inCover = { left: {}, right: {} };
      cover.cover.forEach((c) => { inCover[c.side][c.v] = true; });
      pairs.forEach((p) => {
        eq(!!(inCover.left[p[0]] || inCover.right[p[1]]), true,
           'the pair L' + (p[0] + 1) + '-R' + (p[1] + 1) + ' is covered by one of its ends');
      });
      if (want < left) {
        const hall = hallDeficient(n, f, pairs);
        eq(hall.deficient, true,
           'and where the matching misses a left vertex the cut exhibits a deficient set');
        eq(hall.neighbours.length < hall.S.length, true,
           'with |N(S)| = ' + hall.neighbours.length + ' below |S| = ' + hall.S.length);
      }
    }
    /* MAXIMAL is not MAXIMUM, and the order the pairs are taken in decides it. */
    const pairs = [[1, 1], [0, 1], [1, 0]];
    eq(greedyMatching(pairs).length, 1,
       'taking the pairs in that order gives one pair and blocks both others');
    eq(matchingBrute(pairs, 16).result.value, 2, 'while the maximum is two');
    eq(greedyMatching([[0, 1], [1, 0], [1, 1]]).length, 2,
       'and the same three pairs in another order give two: maximal is a property of the ORDER');
    const refuses = (f2) => { try { f2(); return false; } catch (e) { return /exceeds the exhaustive cap/.test(e.message); } };
    const many = [];
    for (let i = 0; i < 17; i += 1) many.push([i % 4, (i * 3) % 4]);
    eq(refuses(() => matchingBrute(many, 16)), true,
       'seventeen pairs is refused through oracleCap rather than run slowly');
  }

  /* --- the gadgets: the graph changes, the algorithm does not ------------- */
  {
    const G = net('1>2 5, 1>3 4, 2>4 3, 3>4 6, 2>3 2');
    const plain = maxflow(G, 0, 3).result.value;
    eq(plain, 9, 'the untransformed network carries 9');
    /* Split, with nothing capped: the answer MUST come back unchanged, and that
       is the check the gadget carries. */
    const open = gadgetBuild('split', { graph: G, s: 0, t: 3, vertexCap: fkVertexCaps(G, []) });
    eq(open.graph.n + ',' + open.graph.arcs.length, '8,9',
       'splitting 4 vertices gives 8 of them, and 5 arcs plus one joining arc per vertex is 9');
    eq(maxflow(open.graph, open.s, open.t).result.value, plain,
       'and with no vertex capped it gives exactly the original answer');
    /* Split, with one capped: the answer can only fall, and it does. */
    const caps = [];
    caps[1] = 2;
    const tight = gadgetBuild('split', { graph: G, s: 0, t: 3, vertexCap: fkVertexCaps(G, caps) });
    const tightValue = maxflow(tight.graph, tight.s, tight.t).result.value;
    eq(tightValue, 6, 'capping what may pass through vertex 2 at 2 brings it to 6');
    eq(tightValue <= plain, true, 'a capacity can only ever lower the answer');
    eq(minCutBrute(tight.graph, tight.s, tight.t, 12).result.capacity, tightValue,
       'and the certificate survives the transformation, because the result is an ordinary network');
    /* Unit capacities: Menger, as two numbers. */
    const u = gadgetBuild('unit', { graph: net('1>2 9, 1>3 9, 2>4 9, 3>4 9, 2>3 9, 1>4 9'), s: 0, t: 3 });
    const uRun = maxflow(u.graph, u.s, u.t);
    eq(u.graph.arcs.every((a) => a.cap === 1), true, 'every capacity is 1');
    eq(uRun.result.value, 3, 'so the value counts routes sharing no arc, and there are 3');
    eq(unitPaths(u.graph, uRun.result.flow, u.s, u.t).length, uRun.result.value,
       'walking the routes out of the flow finds exactly that many');
    eq(minCutBrute(u.graph, u.s, u.t, 12).result.capacity, uRun.result.value,
       'and the fewest arcs that separate the two ends is the same number');
    /* A super-source over the sources the graph itself names. */
    const many = net('1>3 4, 2>3 3, 3>4 5, 3>5 4');
    const idx = dgIndex(many);
    const sources = [], sinks = [];
    for (let v = 0; v < many.n; v += 1) {
      if (!idx.inn[v].length) sources.push(v);
      if (!idx.out[v].length) sinks.push(v);
    }
    eq(sources.join(',') + ' / ' + sinks.join(','), '0,1 / 3,4',
       'the sources and sinks are read off the graph rather than typed');
    const big = fkTotalCap(many) + 1, wide = [];
    for (let v = 0; v < many.n; v += 1) wide.push(big);
    const sup = gadgetBuild('supersource', { graph: many, sources: sources, sinks: sinks,
                                             sourceCap: wide, sinkCap: wide });
    const supRun = maxflow(sup.graph, sup.s, sup.t);
    eq(sup.graph.n, many.n + 2, 'two nodes are added and nothing else');
    eq(supRun.result.value, 7, 'and the most all the starts can send together is 7');
    let outOfSources = 0;
    many.arcs.forEach((a, id) => { if (sources.indexOf(a.u) !== -1) outOfSources += supRun.result.flow[id]; });
    eq(outOfSources, supRun.result.value, 'which is exactly what leaves the original sources');
    eq(minCutBrute(sup.graph, sup.s, sup.t, 12).result.capacity, supRun.result.value,
       'and the certificate holds on the transformed network too');
    eq(fkTotalCap(many) + 1 > minCutBrute(sup.graph, sup.s, sup.t, 12).result.capacity, true,
       'the joining arcs carry the whole network’s capacity, so none of them is ever binding');
    let unknown = false;
    try { gadgetBuild('nosuchgadget', {}); } catch (e) { unknown = /unknown gadget/.test(e.message); }
    eq(unknown, true, 'and a gadget that does not exist raises rather than returning a network');
  }
}


/* THE VERDICT. There is a second `if (fails)` gate half way up this file, at
   what used to be its end; every section appended after it -- the lp, simplex,
   duality, network, transport and integer kits, the sequence and heap kits, the
   sorting section and the hash and tree section -- ran BELOW that gate, so a
   failing assertion in any of them printed its FAIL line and the file then
   announced that every arithmetic assertion passes, and exited zero. A harness
   that cannot fail is not a harness. The gate above stays, because failing
   fast on the core arithmetic is worth having; this one is the verdict. */
if (fails) {
  console.log('\n' + fails + ' assertion(s) FAILED');
  process.exit(1);
}

console.log('\nevery arithmetic assertion passes');
