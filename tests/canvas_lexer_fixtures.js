'use strict';
const assert=require('node:assert/strict'),{lex,accesses,htmlParts}=require('../scripts/canvas_sources');
const positive=[
 "ctx.fillText('a',1,2)","ctx.strokeText('a',1,2)","const f=ctx.fillText;f.call(ctx,'a',1,2)",
 "ctx['fillText']('a',1,2)",String.raw`ctx['fi\x6clText']('a',1,2)`,String.raw`ctx.fi\u006clText('a',1,2)`,
 "ctx['fill'+'Text']('a',1,2)","const key='fill'+'Text';ctx[key]('a',1,2)",
 "Reflect.get(ctx,'fillText').call(ctx,'a',1,2)","const key='fill'+'Text';Reflect.get(ctx,key).call(ctx,'a',1,2)",
 "const get=Reflect.get;get(ctx,'fillText').call(ctx,'a',1,2)","`ignored ${ctx.fillText('a',1,2)} ignored`",
 "`outer ${`inner ${ctx['strokeText']('a',1,2)}`} end`"
];
for(const source of positive)assert(accesses(source).length,'executable native access: '+source);
const negatives=["// ctx.fillText('ignored',1,2)\nlet x=1;","/* ctx.strokeText('ignored',1,2) */ let x=1;",'const text="ctx.fillText(ignored,1,2)";',"const text=`ctx.fillText(ignored,1,2)`;",String.raw`const re=/ctx\.fillText\(x\)/g;`,"console.log('fillText')"];
for(const source of negatives)assert.equal(accesses(source).length,0,'non-executable native spelling: '+source);
const html='<!-- <canvas id="ghost"></canvas> --><script type="application/json">{"x":"fillText"}</script><textarea><canvas id="text"></canvas></textarea><canvas id="real"></canvas><script>ctx.fillText("x",1,2)</script>';
assert.deepEqual(htmlParts(html).canvases.map(c=>c.id),['real']);assert.equal(htmlParts(html).scripts.filter(s=>s.executable).length,1);
assert.throws(()=>lex('`unterminated ${x'),/unterminated/);
console.log((positive.length+negatives.length+3)+' canvas lexical fixtures passed');
