// ccrun.js: run the shipped cckit JS (code and deps modes) on JSON jobs from stdin; print tiles.
const fs = require('fs'), path = require('path'), vm = require('vm');
const L = path.join(__dirname, '..', '..', 'scripts', 'mathpath', 'labs') + path.sep;
const rd = (f) => fs.readFileSync(L + f, 'utf8');
const S = { alg: rd('algebra_core.py'), core: rd('cckit_core.py'), a: rd('cckit.py'), b: rd('cckit_b.py') };
const blk = (src, name) => { const m = new RegExp(name.replace(/[[\]]/g, '\\$&') + ' = r"""([\\s\\S]*?)"""', 'm').exec(S[src]); if (!m) throw new Error('no ' + name); return m[1]; };
const views = (src, d, l) => l.map((v) => blk(src, d + '["' + v + '"]')).join('');
const ctx = { console }; vm.createContext(ctx);
vm.runInContext(blk('alg', 'RATIONAL_JS') + blk('core', 'CC_CORE_JS') + blk('core', 'CC_LEX_JS') + blk('a', 'CO_JS') + blk('a', 'CO_DECIDE_JS')
  + views('a', 'CO_VIEW_JS', ['size', 'class', 'dupes', 'complexity', 'basis']), ctx);
const ctx2 = { console }; vm.createContext(ctx2);
vm.runInContext(blk('alg', 'RATIONAL_JS') + blk('core', 'CC_CORE_JS') + blk('b', 'DG_JS') + views('b', 'DG_VIEW_JS', ['coupling', 'ripple']), ctx2);
const jobs = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = jobs.map((j) => {
  try {
    if (j.mode === 'code') {
      ctx.J = j; const r = vm.runInContext("coCompute(J.view, Object.assign({code: ccSplitLines(J.code)}, J.extra || {}), J.opts || {})", ctx);
      return { id: j.id, tiles: r.tiles, refuse: r.refuse, status: r.status };
    } else {
      ctx2.J = j; const r = vm.runInContext("(function(){ var e = J.edges.split(';').map(function(s){ var p = s.split(',').map(function(x){return x.trim();}); return J.view==='coupling'? {user:p[0], used:p[1]} : {dependent:p[0], dependency:p[1]}; }); return dgCompute(J.view, {edges: e, changed: J.changed}, {}); })()", ctx2);
      return { id: j.id, tiles: r.tiles, refuse: r.refuse, status: r.status };
    }
  } catch (e) { return { id: j.id, error: e.message }; }
});
console.log(JSON.stringify(out, null, 1));
