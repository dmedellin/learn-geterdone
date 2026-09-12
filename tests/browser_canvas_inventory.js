'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {inventory}=require('../scripts/canvas_sources'),{launch}=require('./browser_cdp'),protocol=require('./mutation_protocol');
const {interceptCanvasText,reconcileRuntime,reconcileRuntimeHistory}=require('./canvas_runtime_contract');
const {reconcileImplementations}=require('./canvas_implementation_evidence');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
function reconcileDocument(source,value){
 if(!Array.isArray(value.canvases)||JSON.stringify(source.canvases.map(c=>c.id).sort())!==JSON.stringify(value.canvases.slice().sort()))fail('canvas source/live identities differ');
 const history=reconcileRuntimeHistory(source,value.native);
 if(!source.canvases.length){if(value.helper||value.live.length||value.native.calls.length||history.nativeCalls||history.diagnosticCalls)fail('unexpected canvas runtime on noncanvas route');return {canvases:0,labels:0,history};}
 if(!value.helper||value.pending!==0)fail('missing canvas finalization');
 return reconcileRuntime(source,value.live,value.native);
}
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const data=inventory(ROOT);fs.writeFileSync(OUT+'/source.json',JSON.stringify(data));
 if(data.errors.length)fail(data.errors[0].assertion);
 const server=http.createServer((req,res)=>{try{let file=path.resolve(ROOT,'site','.'+decodeURIComponent(req.url.split('?')[0]));if(file!==ROOT+'/site'&&!file.startsWith(ROOT+'/site/'))throw Error('path');if(fs.statSync(file).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));}catch{res.writeHead(404);res.end()}});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-inventory',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const page of data.pages){
   await c.navigate(page.route,{width:390,height:844,theme:'dark'});await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');
   const initial=await c.evaluate('__learnCanvasNative.snapshot()');
   const initialHistory=reconcileRuntimeHistory(page,initial);
   const value=await c.evaluate(`(()=>{const helper=!!window.CanvasText;__learnCanvasNative.clear();if(helper){const redraw=window.redrawLab||window.redraw||window.drawCurrent;if(typeof redraw!=='function')throw Error('canvas redraw entry missing');redraw();}return {helper,pending:helper?CanvasText.pending():0,live:helper?CanvasText.inspect():[],native:__learnCanvasNative.snapshot(),canvases:[...document.querySelectorAll('canvas')].map(c=>c.id)}})()`);
   let result=null,error=null;try{result=reconcileDocument(page,value)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;error=e.assertion;}
   const row={route:page.route,sourceHash:page.sha256,initialHistory,result,error,value,exceptions:[...c.events.exceptions],blocked:[...c.events.blocked],responses:[...c.events.responses]};rows.push(row);fs.appendFileSync(OUT+'/observations.jsonl',JSON.stringify(row)+'\n');
   if(error)fail(error);if(row.exceptions.length||row.blocked.length||row.responses.some(r=>r.status>=400))throw Error('browser runtime or network failure on '+page.route);
   console.log(JSON.stringify({route:page.route,canvases:result.canvases,labels:result.labels,initialFrames:initialHistory.frames}));
  }
 }finally{await c.close();await new Promise(r=>server.close(r));}
 const implementations=reconcileImplementations(data,rows);fs.writeFileSync(OUT+'/implementation-evidence.json',JSON.stringify(implementations,null,2));
 const summary={routes:rows.length,canvasRoutes:rows.filter(r=>r.result.canvases).length,canvases:rows.reduce((n,r)=>n+r.result.canvases,0),labels:rows.reduce((n,r)=>n+r.result.labels,0),historicFrames:rows.reduce((n,r)=>n+r.result.history.frames,0),nativeCalls:rows.reduce((n,r)=>n+r.result.history.nativeCalls,0),failures:rows.filter(r=>r.error).length,finiteProofComplete:false,scope:'All source-derived documents at 390x844 dark initial state and one synchronous redraw; not the full derived finite state space.'};
 fs.writeFileSync(OUT+'/summary.json',JSON.stringify(summary,null,2));if(summary.routes!==data.htmlRoutes||summary.canvasRoutes!==data.canvasRoutes||summary.canvases!==data.canvases||!summary.labels||!summary.historicFrames||summary.failures)fail('incomplete canvas document runtime inventory');console.log(JSON.stringify(summary));
}
module.exports={reconcileDocument};
if(require.main===module)main().catch(e=>{if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
