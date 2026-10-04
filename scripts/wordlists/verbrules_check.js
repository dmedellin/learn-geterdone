const fs = require('fs');
const core = fs.readFileSync('scripts/mathpath/labs/english_core.py','utf8');
const js = core.split('ENGLISH_VERB_JS = r"""')[1].split('"""')[0];
const R = (a,b) => ({n:a,d:b});                       // stub: only vbScore uses it
eval(js);
const fx = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
for (const [k,v] of Object.entries(fx.stress)) VB_FINAL_STRESS[k] = v;
const fns = {s: vbThird, ing: vbIng, ed: vbEd};
for (const tag of ['s','ing','ed']) {
  let hit = 0; const miss = [];
  for (const [base, attested] of fx.cases[tag]) {
    if (attested.includes(fns[tag](base))) hit++;
    else miss.push(base + '->' + fns[tag](base));
  }
  const n = fx.cases[tag].length;
  console.log(`-${tag.padEnd(3)} ${String(hit).padStart(5)}/${n} = ${(100*hit/n).toFixed(2)}%   residue: ${miss.slice(0,6).join(', ')}`);
}
