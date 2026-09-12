"use strict";
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {inventory}=require(ROOT+'/scripts/canvas_sources'),{launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
function checkDepth(value){
 const frame=value.live.find(f=>f.labels.some(l=>l.descriptor.mode==='drawDepth'));if(!frame)return null;
 const labels=frame.labels.filter(l=>l.descriptor.mode==='drawDepth'&&l.descriptor.formatter==='fmt(x.p,2)'),calls=value.native.calls.filter(c=>c.canvas===frame.canvas&&labels.some(l=>l.site===c.site)),bars=frame.trace.filter(c=>c[0]==='fillRect').map(c=>c[1]);
 if(!labels.length||labels.length!==calls.length||bars.length!==labels.length)fail('depth axis inventory differs from bars');
 const base=Math.max(...bars.map(b=>b[1]+b[3]));
 const pairs=labels.map((label,i)=>({label:label.text,site:label.site,instance:label.instance,bar:bars[i],native:calls[i],ink:label.ink,region:label.region,barCenter:bars[i][0]+bars[i][2]/2}));
 if(pairs.some(p=>Math.abs(p.native.x-p.barCenter)>1e-6||p.ink.top<=base||Math.abs(p.native.y-(base+16))>1e-6))fail('depth price label remains attached to its bar');
 return {labels:labels.length,width:frame.width,height:frame.height,pairs};
}
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const data=inventory(ROOT),pages=data.pages.filter(p=>p.occurrences.some(o=>o.implementationOwner==='drawDepth'));if(!pages.length||data.errors.length)fail('depth source inventory missing');
 fs.writeFileSync(OUT+'/source.json',JSON.stringify(data));
 const server=http.createServer((req,res)=>{try{let p=path.resolve(ROOT,'site','.'+decodeURIComponent(req.url.split('?')[0]));if(!p.startsWith(ROOT+'/site/'))throw Error('path');if(fs.statSync(p).isDirectory())p=path.join(p,'index.html');res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(p));}catch{res.writeHead(404);res.end()}});await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-depth',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const page of pages){
   await c.navigate(page.route,{width:390,height:844,theme:'dark'});
   const value=await c.evaluate(`(()=>{__learnCanvasNative.clear();redrawLab();return {live:CanvasText.inspect(),native:__learnCanvasNative.snapshot()}})()`);
   let result=null,error=null;try{result=checkDepth(value)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;error=e.assertion;}
   const row={route:page.route,sourceHash:page.sha256,value,result,error,events:c.events};rows.push(row);fs.appendFileSync(OUT+'/observations.jsonl',JSON.stringify(row)+'\n');
   if(error)fail(error);if(result)reconcileRuntime(page,value.live,value.native);
   if(c.events.exceptions.length||c.events.blocked.length||c.events.responses.some(r=>r.status>=400))throw Error('depth runtime/network setup failure');
  }
 }finally{await c.close();await new Promise(r=>server.close(r));}
 const active=rows.filter(r=>r.result);if(!active.length)fail('depth active implementation witness missing');
 const summary={candidatePages:pages.length,activePages:active.length,labels:active.reduce((n,r)=>n+r.result.labels,0),failures:0,finiteProofComplete:false};fs.writeFileSync(OUT+'/summary.json',JSON.stringify(summary));console.log(JSON.stringify(summary));
}
module.exports={checkDepth};if(require.main===module)main().catch(e=>{if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
