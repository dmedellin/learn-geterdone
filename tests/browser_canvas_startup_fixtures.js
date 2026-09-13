'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const definition={id:'startup.label',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal',family:'fixture',mode:'startup',dependencies:['frame.width','frame.height','theme']};
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}canvas{width:320px;height:200px}</style><canvas id=chart></canvas>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-startup',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const [name,call]of [['normal',''],['startup-fill','document.getElementById("chart").getContext("2d").fillText("Unbound startup",10,20)'],['startup-stroke','document.getElementById("chart").getContext("2d").strokeText("Unbound startup",10,20)'],['startup-offscreen','new OffscreenCanvas(100,100).getContext("2d").fillText("Unbound startup",10,20)']]){
   await c.navigate('/',{width:390,height:844,theme:'dark'});if(call)await c.evaluate(call);
   await c.evaluate(helper);
   const value=await c.evaluate(`(()=>{__learnCanvasNative.clear();const canvas=document.getElementById('chart');CanvasText.frame(()=>{const ctx=CanvasText.begin(canvas,320,200,2);ctx.font='14px monospace';CanvasText.text(ctx,CanvasText.site(${JSON.stringify(definition)}),'Bound current frame',30,80)});return {live:CanvasText.inspect(),native:__learnCanvasNative.snapshot()}})()`);
   let observed=null;try{reconcileRuntime({canvases:[{id:'chart'}],occurrences:[{siteID:definition.id,descriptor:definition}]},value.live,value.native)}catch(e){observed=e.assertion||e.message;assert.equal(e.code,'LEARN_CANVAS_SEMANTIC');}
   rows.push({name,expected:call?'uncontracted runtime native text':null,observed,...value});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
   assert.equal(observed,call?'uncontracted runtime native text':null,'startup uncontracted call survives epoch reset: '+name);
   assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);
  }
  console.log('4/4 canvas startup interception fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
