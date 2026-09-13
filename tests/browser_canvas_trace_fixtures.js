'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require('./browser_cdp'),protocol=require('./mutation_protocol');
const definition={id:'trace.label',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal',family:'fixture',mode:'trace',dependencies:['frame.width','frame.height','theme']};
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}canvas{width:320px;height:200px}</style><canvas id=chart></canvas>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-trace',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(helper);
  for(const kind of ['dash','gradient','gradient-identity'].filter(kind=>!process.argv.some(a=>a.startsWith('--only='))||process.argv.includes('--only='+kind))){
   const values=await c.evaluate(`(()=>{const canvas=document.getElementById('chart'),values=[];for(const variant of [0,0,1]){CanvasText.frame(()=>{const ctx=CanvasText.begin(canvas,320,200,2);ctx.font='14px monospace';ctx.strokeStyle='#f0f';ctx.lineWidth=5;if(${JSON.stringify(kind)}==='dash'){ctx.setLineDash(variant?[15,20]:[5,2]);ctx.strokeRect(10,110,280,60);}else if(${JSON.stringify(kind)}==='gradient-identity'){const gradients=[ctx.createLinearGradient(0,0,320,0),ctx.createLinearGradient(0,0,320,0)];for(const g of gradients){g.addColorStop(0,'#00f');g.addColorStop(1,'#0f0');}ctx.fillStyle=gradients[0];gradients[variant].addColorStop(.5,'#f00');ctx.fillRect(10,110,280,60);ctx.fillStyle='#fff';}else{const gradient=ctx.createLinearGradient(0,0,320,0);gradient.addColorStop(0,variant?'#ff0000':'#0000ff');gradient.addColorStop(1,'#00ff00');ctx.fillStyle=gradient;ctx.fillRect(10,110,280,60);ctx.fillStyle='#fff';}CanvasText.text(ctx,CanvasText.site(${JSON.stringify(definition)}),'Complete paint trace',30,80)});values.push({trace:CanvasText.inspect()[0].trace,raster:canvas.toDataURL()});}return values})()`);
   rows.push({kind,values});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
   assert.deepEqual(values[0],values[1],'normal redraw deterministic: '+kind);
   assert.notEqual(values[0].raster,values[2].raster,'paint mutation changes real canvas pixels: '+kind);
   assert.notDeepEqual(values[0].trace,values[2].trace,'canvas trace records consequential paint input: '+kind);
  }
  assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);console.log(rows.length+'/'+rows.length+' complete canvas paint trace fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
