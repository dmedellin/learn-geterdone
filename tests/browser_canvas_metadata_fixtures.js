'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const definition={id:'history.label',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal',family:'fixture',mode:'history',dependencies:['frame.width','frame.height','theme']};
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}canvas{width:320px;height:200px}</style><canvas id=chart></canvas>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-history',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(helper);
  const source={canvases:[{id:'chart'}],occurrences:[{siteID:definition.id,descriptor:definition}]};
  const healthy=await c.evaluate(`(()=>{const canvas=document.getElementById('chart');const draw=()=>CanvasText.frame(()=>{const ctx=CanvasText.begin(canvas,320,200,2);ctx.font='14px monospace';CanvasText.text(ctx,CanvasText.site(${JSON.stringify(definition)}),'Every frame',30,80)});draw();__learnCanvasNative.clear();draw();return {live:CanvasText.inspect(),native:__learnCanvasNative.snapshot()}})()`);
  const cases=[['normal',null,null]];
  for(const key of ['width','actualBoundingBoxLeft','actualBoundingBoxRight','actualBoundingBoxAscent','actualBoundingBoxDescent']){
   cases.push(['missing-historic-'+key,v=>delete v.native.history[0].metrics[key],'missing historic canvas geometry']);
   cases.push(['missing-current-'+key,v=>delete v.native.calls[0].metrics[key],'missing native canvas geometry']);
  }
  for(const kind of ['region','ink'])for(const key of ['left','right','top','bottom']){
   cases.push(['missing-historic-'+kind+'-'+key,v=>delete v.native.history[0].geometry[kind][key],'missing historic canvas geometry']);
   cases.push(['missing-current-'+kind+'-'+key,v=>delete v.live[0].labels[0][kind][key],'missing native canvas geometry']);
  }
  for(const [name,mutate,expected]of cases){
   const v=structuredClone(healthy);if(mutate)mutate(v);let observed=null;
   try{reconcileRuntime(source,v.live,v.native)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;observed=e.assertion}
   rows.push({name,expected,observed,...v});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
   assert.equal(observed,expected,'required canvas geometry metadata: '+name);
  }
  assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);
  console.log(cases.length+'/'+cases.length+' required canvas geometry metadata fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
