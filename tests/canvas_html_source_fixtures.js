'use strict';
const {htmlParts,attributeSourceErrors,accesses,closedSurface,SCRIPT_TYPES}=require('../scripts/canvas_sources'),protocol=require('./mutation_protocol');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
function errors(source){const h=htmlParts(source);return [...h.boundaryErrors,...h.attributesCode.flatMap(attributeSourceErrors),...h.scripts.filter(s=>s.executable).flatMap(s=>[...accesses(s.source).map(a=>({...a,assertion:'uncontracted native canvas text source'})),...closedSurface(s.source)])];}
const raw="document.querySelector('canvas').getContext('2d').fillText('Raw',10,20)";
const cases=[
 ['authored handler','<button onclick="window.initLab()">Run</button>',null],
 ['second authored handler','<button onclick="scrollToLab()">Run</button>',null],
 ['literal and comment','<button onclick="void \'ctx.fillText()\';/* x.strokeText() */">Run</button>',null],
 ['raw event','<button onclick="'+raw+'">Run</button>','uncontracted native canvas text source'],
 ['encoded member','<button onclick="ctx[&quot;fillText&quot;](\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['numeric identifier','<button onclick="ctx.&#102;illText(\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['hex identifier','<button onclick="ctx.&#x66;illText(\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['escaped access','<button onclick="ctx[\'\\x66illText\'](\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['constant alias','<button onclick="const p=\'fill\'+\'Text\';const f=ctx[p];f.call(ctx,\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['template interpolation','<button onclick="void `${ctx.fillText(\'Raw\',1,2)}`">Run</button>','uncontracted native canvas text source'],
 ['Reflect alias','<button onclick="const g=Reflect.get;g(ctx,\'fillText\').call(ctx,\'Raw\',1,2)">Run</button>','uncontracted native canvas text source'],
 ['URL','<a href="javascript:'+raw+'">Run</a>','uncontracted native canvas text source'],
 ['encoded URL','<a href="java&Tab;script&colon;'+raw+'">Run</a>','uncontracted native canvas text source'],
 ['unowned descriptor','<button onclick="CanvasText.text(ctx,token,\'A\',1,2)">Run</button>','canvas descriptor requires an owned script implementation'],
 ['unsupported entity','<button onclick="void \'&trade;\'">Run</button>','unsupported executable HTML character reference'],
 ['duplicate handler','<button onclick="window.initLab()" onclick="'+raw+'">Run</button>','duplicate HTML attribute in canvas source boundary'],
 ['nested source','<iframe srcdoc="&lt;script&gt;'+raw+';&lt;/script&gt;"></iframe>','unsupported nested executable HTML owner'],
 ['inert JSON','<script type="application/json">{"text":"fillText"}</script>',null],
 ['unknown type','<script type="application/unknown">'+raw+'</script>','unsupported script classification in canvas source boundary'],
 ['script src','<script src="/anything.js"></script>','external script in canvas source boundary'],
 ['inert noscript','<noscript><script>'+raw+'</script></noscript>',null],
 ['text raw owner','<textarea><button onclick="'+raw+'"></textarea>',null],
 ['comment owner','<!--<button onclick="'+raw+'">-->',null]
];
for(const type of SCRIPT_TYPES)cases.push(['MIME '+type,'<script type="'+type+'">'+raw+'</script>','uncontracted native canvas text source']);
cases.push(['case whitespace MIME','<script type=" TEXT/JAVASCRIPT ">'+raw+'</script>','uncontracted native canvas text source']);
cases.push(['legacy language','<script language="JavaScript1.2">'+raw+'</script>','uncontracted native canvas text source']);
try{for(const [name,source,expected] of cases){const observed=errors(source);if(expected?!observed.some(e=>e.assertion===expected):observed.length)fail('executable HTML source boundary: '+name);}
 const h=htmlParts('<p>é</p><button onclick="window.initLab()">Run</button>');if(h.attributesCode[0].offset!==Buffer.byteLength('<p>é</p><button '))fail('executable HTML source boundary: stable byte identity');
 console.log((cases.length+1)+'/'+(cases.length+1)+' executable HTML source boundary fixtures passed');
}catch(e){if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1;}
module.exports={cases,errors};
