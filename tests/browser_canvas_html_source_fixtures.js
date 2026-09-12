'use strict';
const fs=require('fs'),http=require('http'),path=require('path');
const R=(process.env.SOURCE_ROOT||path.resolve(__dirname,'..')),OUT=process.env.BROWSER_EVIDENCE,{launch}=require(R+'/tests/browser_cdp'),protocol=require(R+'/tests/mutation_protocol'),{interceptCanvasText}=require(R+'/tests/canvas_runtime_contract');
const {htmlParts,attributeSourceErrors,accesses,SCRIPT_TYPES}=require('../scripts/canvas_sources');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const raw="document.querySelector('canvas').getContext('2d').fillText('Raw',10,20)",cases=[];
 for(const type of SCRIPT_TYPES)cases.push({name:type,html:'<script type="'+type+'">'+raw+'</script>',native:1});
 cases.push({name:'case-whitespace',html:'<script type=" TEXT/JAVASCRIPT ">'+raw+'</script>',native:1},{name:'legacy-language',html:'<script language="JavaScript1.2">'+raw+'</script>',native:1},
 {name:'inert-JSON',html:'<script type="application/json">{"text":"fillText"}</script>',native:0},
 {name:'inert-noscript',html:'<noscript><script>'+raw+'</script></noscript>',native:0});
 for(const [name,code]of [['raw-event',raw],['encoded-event',"const ctx=document.querySelector('canvas').getContext('2d');ctx[&quot;fillText&quot;]('Raw',10,20)"],['numeric-event',"document.querySelector('canvas').getContext('2d').&#102;illText('Raw',10,20)"],['alias-event',"const ctx=document.querySelector('canvas').getContext('2d'),p='fill'+'Text',f=ctx[p];f.call(ctx,'Raw',10,20)"],['reflect-event',"const ctx=document.querySelector('canvas').getContext('2d'),g=Reflect.get;g(ctx,'fillText').call(ctx,'Raw',10,20)"]])cases.push({name,html:'<button id=trigger onclick="'+code+'">Run</button>',click:true,native:1});
 cases.push({name:'encoded-URL',html:'<a id=trigger href="java&Tab;script&colon;'+raw+';void 0">Run</a>',click:true,native:1});
 let current=cases[0];const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><title>Executable source calibration</title><link rel=icon href=data:,><canvas id=chart></canvas>'+current.html)});await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'html-source',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(current of cases){await c.navigate('/',{width:390,height:844,theme:'dark'});if(current.click){await c.evaluate('document.getElementById("trigger").click()');await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');}
   const observed=await c.evaluate('__learnCanvasNative.snapshot()'),h=htmlParts(current.html),staticErrors=[...h.boundaryErrors,...h.attributesCode.flatMap(attributeSourceErrors),...h.scripts.filter(s=>s.executable).flatMap(s=>accesses(s.source).map(a=>({...a,assertion:'uncontracted native canvas text source'})))];
   rows.push({name:current.name,expected:current.native,observed,staticErrors});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
   if(observed.failures.length!==current.native||observed.failures.some(f=>f.assertion!=='uncontracted runtime native text'))fail('Chromium executable source boundary: '+current.name);
   if(current.native&&!staticErrors.some(e=>e.assertion==='uncontracted native canvas text source')||!current.native&&staticErrors.length)fail('source/Chromium executable owner correspondence: '+current.name);
   if(c.events.exceptions.length||c.events.blocked.length||c.events.responses.some(r=>r.status>=400))throw Error('HTML source fixture runtime/network setup failure');
  }
  console.log(cases.length+'/'+cases.length+' Chromium executable source boundary fixtures passed');
 }finally{fs.writeFileSync(OUT+'/events.json',JSON.stringify(c.events));await c.close();await new Promise(r=>server.close(r));}
})().catch(e=>{if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
