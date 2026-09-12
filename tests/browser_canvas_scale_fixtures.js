'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const {canvasFinalRaster}=require(ROOT+'/tests/canvas_raster_contract'),{reconcileCanvasRaster}=require(ROOT+'/tests/canvas_raster_evidence');
const definition={id:'scale.label',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal',family:'fixture',mode:'scale',dependencies:['frame.width','frame.height','theme']};
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}body{margin:0;padding-top:950px}#owner{margin-left:10px;width:280px;height:170px;border:6px solid #4b6379;overflow:auto;transform-origin:top left}canvas{width:720px;height:650px}</style><div id=owner tabindex=0 aria-label="Scaled horizontal and vertical chart"><canvas id=chart></canvas></div>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-scale',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const scale of [.5,1.25,2]){
   await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(helper);
   await c.evaluate(`document.getElementById('owner').style.transform='scale(${scale})';window.__canvasFixtureRedraw=()=>CanvasText.frame(()=>{const ctx=CanvasText.begin(document.getElementById('chart'),720,650,2);ctx.font='600 28px monospace';const token=CanvasText.site(${JSON.stringify(definition)});for(const [x,y]of [[30,90],[500,90],[30,540],[500,540]])CanvasText.text(ctx,token,'Scale',x,y)});__learnCanvasNative.clear();__canvasFixtureRedraw();`);
   const live=await c.evaluate('CanvasText.inspect()'),native=await c.evaluate('__learnCanvasNative.snapshot()');reconcileRuntime({canvases:[{id:'chart'}],occurrences:[{siteID:definition.id,descriptor:definition}]},live,native);
   await c.evaluate(canvasFinalRaster.toString());
   const before=await c.evaluate('[scrollX,scrollY,owner.scrollLeft,owner.scrollTop]');
   const observed=await c.evaluate('canvasFinalRaster("chart").then(result=>({result})).catch(e=>({assertion:e.assertion,code:e.code,error:e.message,evidence:window.__learnCanvasRasterEvidence}))',900000);
   fs.writeFileSync(OUT+'/scale-'+scale+'.json',JSON.stringify(observed));assert.equal(observed.error,undefined,'complete scaled canvas scroll-owner capture '+scale);
   const proof=reconcileCanvasRaster(observed.result,live[0]);assert.equal(proof.labels,4);assert(proof.tiles>1);assert.deepEqual(await c.evaluate('[scrollX,scrollY,owner.scrollLeft,owner.scrollTop]'),before);
   rows.push({scale,proof,exceptions:c.events.exceptions,blocked:c.events.blocked});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);
  }
  for(const [name,style,expected]of [
   ['zero-scale','owner.style.transform="none";owner.style.scale="0"','unprovable canvas CSS transform'],
   ['negative-scale','owner.style.transform="none";owner.style.scale="-1"','unprovable canvas CSS transform'],
   ['unsupported-clip','owner.style.scale="none";owner.style.clipPath="inset(0 50% 0 0)"','unprovable canvas CSS clipping'],
  ]){
   await c.evaluate(style);const observed=await c.evaluate('canvasFinalRaster("chart").then(result=>({result})).catch(e=>({assertion:e.assertion,code:e.code,error:e.message}))');
   rows.push({name,expected,observed});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));assert.equal(observed.assertion,expected,'canvas CSS boundary: '+name);assert.equal(observed.code,'LEARN_CANVAS_SEMANTIC');
  }
  console.log('6/6 scaled canvas and CSS-boundary raster fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
