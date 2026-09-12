'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const {canvasFinalRaster}=require(ROOT+'/tests/canvas_raster_contract');
const {reconcileCanvasRaster}=require(ROOT+'/tests/canvas_raster_evidence');
const {reconcileCanvasArtifacts}=require(ROOT+'/tests/canvas_raster_artifacts');
const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
const artifacts=(result,expected)=>reconcileCanvasArtifacts(result,expected,{directory:OUT,frames:fs.readFileSync(path.join(OUT,'canvas-contract-fixtures-raster-frames.jsonl'),'utf8').trim().split('\n').map(JSON.parse)});
const definition={id:'fixture.value',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal-fixture',family:'fixture',mode:'fixed',dependencies:['frame.width','frame.height','theme']};
const cases=[
 ['high-contrast','CanvasText.text(ctx,token,"Semantic value",30,80);',null],
 ['context-method-override','ctx.reset=0;CanvasText.text(ctx,token,"Semantic value",30,80);','unsupported canvas state property reset'],
 ['context-own-property','ctx.globalAlpha=.1;Object.defineProperty(ctx,"globalAlpha",{configurable:true,get(){return 1},set(){}});CanvasText.text(ctx,token,"Semantic value",30,80);','canvas context reflection mutation'],
 ['unknown-paint-operation','ctx.drawFocusIfNeeded(canvas);CanvasText.text(ctx,token,"Semantic value",30,80);','unsupported canvas operation drawFocusIfNeeded'],
 ['faint-decorative-guide','ctx.globalAlpha=.1;ctx.fillStyle="#fff";ctx.fillRect(10,130,280,1);ctx.globalAlpha=1;CanvasText.text(ctx,token,"Semantic value",30,80);',null],
 ['transformed-ink','ctx.translate(80,30);ctx.rotate(.2);ctx.textAlign="right";ctx.textBaseline="bottom";CanvasText.text(ctx,token,"Transform",140,90,80);',null],
 ['compressed-italic-ink','ctx.font="italic 600 22px monospace";ctx.translate(50,0);ctx.rotate(.15);ctx.textAlign="center";ctx.textBaseline="middle";CanvasText.text(ctx,token,"Italic compressed",120,90,100);',null],
 ['opaque-token','CanvasText.text(ctx,{},"Unbound",30,80);','unbound site token'],
 ['low-alpha','ctx.globalAlpha=.2;CanvasText.text(ctx,token,"Faint",30,80);','semantic alpha below one'],
 ['raw-fill','ctx.fillText("Bypass",30,80);','uncontracted native text'],
 ['raw-stroke','ctx.strokeText("Bypass",30,80);','uncontracted native text'],
 ['native-alias','const alias=canvas.getContext("2d").fillText;alias.call(canvas.getContext("2d"),"Bypass",30,80);','uncontracted native text'],
 ['native-bracket','canvas.getContext("2d")["fill"+"Text"]("Bypass",30,80);','uncontracted native text'],
 ['native-reflection','Reflect.get(canvas.getContext("2d"),"fillText").call(canvas.getContext("2d"),"Bypass",30,80);','uncontracted native text'],
 ['offscreen-native','new OffscreenCanvas(50,50).getContext("2d").fillText("Bypass",1,20);','uncontracted native text'],
 ['arbitrary-semantic-color','CanvasText.text(ctx,token,"Paint argument",30,80,100,"#fff");','arbitrary semantic paint arguments'],
 ['missing-descriptor','CanvasText.site();','missing descriptor'],
 ['conflicting-descriptor','CanvasText.site({...definition,region:"annotation"});','conflicting descriptor fixture.value'],
 ['guide-text','CanvasText.site({...definition,id:"guide",role:"guide"});','decorative guide used as semantic text'],
 ['overlap','CanvasText.text(ctx,token,"First",30,80);CanvasText.text(ctx,token,"Second",30,80);','semantic bounds overlap'],
 ['unplaceable','CanvasText.text(ctx,token,"Too wide ".repeat(80),30,80);','unplaceable semantic text fixture.value'],
 ['transformed-corner-escape','ctx.scale(40,40);CanvasText.text(ctx,token,"Escape",30,80);','unplaceable semantic text fixture.value'],
 ['clipped','ctx.beginPath();ctx.rect(30,75,10,10);ctx.clip();CanvasText.text(ctx,token,"Clipped",30,80);','unprovable semantic clip'],
 ['late-clip','CanvasText.text(ctx,token,"Clipped later",30,80);ctx.beginPath();ctx.rect(30,75,10,10);ctx.clip();','unprovable semantic clip at finalization'],
 ['gradient','ctx.fillStyle=ctx.createLinearGradient(0,0,100,0);CanvasText.text(ctx,token,"Gradient",30,80);','gradient or pattern used for semantic text'],
 ['composite','ctx.globalCompositeOperation="destination-out";CanvasText.text(ctx,token,"Composite",30,80);','unsupported semantic composite'],
 ['filter','ctx.filter="blur(2px)";CanvasText.text(ctx,token,"Filtered",30,80);','unprovable semantic shadow or filter'],
 ['spacing','ctx.letterSpacing="2px";CanvasText.text(ctx,token,"Spaced",30,80);','unprovable semantic font spacing'],
 ['late-paint','CanvasText.text(ctx,token,"Final text",30,80);','paint after text finalization','ctx.fillRect(0,0,320,200);'],
 ['late-partial-paint','CanvasText.text(ctx,token,"Final text",30,80);','paint after text finalization','canvas.getContext("2d").fillRect(40,70,2,8);'],
 ['late-bitmap-reset','CanvasText.text(ctx,token,"Final text",30,80);','paint after text finalization','canvas.width=canvas.width;'],
 ['missing-frame','CanvasText.text(ctx,token,"Final text",30,80);','frame missing','CanvasText.begin(canvas,320,200,2);'],
];
async function main(){
 if(!OUT)throw Error('BROWSER_EVIDENCE required');fs.mkdirSync(OUT,{recursive:true});
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><title>Canvas fixtures</title><link rel=icon href=data:,>')});await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-contract-fixtures',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.navigate('/',{width:390,height:844,theme:'dark'});
  await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}body{margin:0}canvas{width:320px;height:200px}</style><canvas id="chart"></canvas>'});
  await c.evaluate(`window.__fixtureRawRect=CanvasRenderingContext2D.prototype.fillRect;`+'('+interceptCanvasText.toString()+')();'+`(()=>{const native=CanvasRenderingContext2D.prototype.fillText;CanvasRenderingContext2D.prototype.fillText=function(...args){const active=window.CanvasText?.nativeToken();if(window.__fixtureInkFault&&active&&!active.diagnostic){this.save();if(__fixtureInkFault==='same-color')this.fillStyle='#071019';if(__fixtureInkFault==='low-alpha')this.globalAlpha=.2;try{return native.apply(this,args)}finally{this.restore()}}return native.apply(this,args)}})();`+helper);
  for(const [name,body,expected,after='']of cases){
   const value=await c.evaluate(`(()=>{const definition=${JSON.stringify(definition)},canvas=document.getElementById('chart'),token=CanvasText.site(definition);let ctx;__learnCanvasNative.clear();try{CanvasText.frame(()=>{ctx=CanvasText.begin(canvas,320,200,2);ctx.font='14px monospace';${body}});${after};return {live:CanvasText.inspect(),native:__learnCanvasNative.snapshot(),pending:CanvasText.pending()}}catch(e){return {assertion:e.assertion||null,code:e.code||null,error:e.message,pending:CanvasText.pending()}}})()`);
   rows.push({name,expected,...value});fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
   if(expected){assert.equal(value.code,'LEARN_CANVAS_SEMANTIC',name);assert.equal(value.assertion,expected,name);assert.equal(value.pending,0,name+' leaked pending frame');}
   else{assert.equal(value.error,undefined,name);assert.equal(value.pending,0);const check=reconcileRuntime({canvases:[{id:'chart'}],occurrences:[{siteID:definition.id,descriptor:definition}]},value.live,value.native);assert.equal(check.labels,1);}
  }
  const good=rows.find(r=>r.name==='transformed-ink'),source={canvases:[{id:'chart'}],occurrences:[{siteID:definition.id,descriptor:definition}]};
  const runtimeCorruptions=[
   ['empty-native-inventory',n=>n.calls=[],'empty canvas runtime inventory'],
   ['wrong-native-identity',n=>n.calls[0].site='unrelated','wrong native semantic identity'],
   ['duplicate-native-call',n=>n.calls.push(structuredClone(n.calls[0])),'incomplete native canvas frame'],
   ['wrong-native-ordinal',n=>n.calls[0].ordinal++,'incomplete native canvas frame'],
   ['missing-native-metrics',n=>delete n.calls[0].metrics,'missing native canvas geometry'],
   ['native-transformed-escape',n=>n.calls[0].matrix[4]+=10000,'native transformed corner outside semantic region'],
  ];
  for(const [name,change,expected]of runtimeCorruptions){const native=structuredClone(good.native);change(native);assert.throws(()=>reconcileRuntime(source,good.live,native),e=>e.code==='LEARN_CANVAS_SEMANTIC'&&e.assertion===expected,name);rows.push({name,expected,observed:expected});}
  const reflected=await c.evaluate("(()=>{const a=CanvasText.inspect(),before=JSON.stringify(a);a[0].labels[0].text='tampered';a[0].labels[0].ink.left=-1000;a[0].trace.length=0;return {before,after:JSON.stringify(CanvasText.inspect())}})()");
  assert.equal(reflected.after,reflected.before,'reflection cannot mutate private canvas frame');rows.push({name:'private-frame-reflection',passed:true});
  // A tall and wide off-viewport canvas must retain full real samples.
  await c.evaluate(`document.body.style.paddingTop='1100px';const owner=document.createElement('div');owner.id='canvas-owner';owner.tabIndex=0;owner.setAttribute('aria-label','Scrollable fixture chart');owner.style.cssText='width:280px;height:150px;overflow:auto';const target=document.getElementById('chart');target.before(owner);owner.appendChild(target);target.style.width='720px';target.style.height='650px';window.__canvasFixtureRedraw=()=>CanvasText.frame(()=>{const ctx=CanvasText.begin(target,720,650,2);ctx.font='600 16px monospace';const token=CanvasText.site(${JSON.stringify(definition)});for(const [x,y]of [[30,80],[510,80],[30,540],[510,540]])CanvasText.text(ctx,token,'Tile value',x,y)});__canvasFixtureRedraw();`);
  await c.evaluate(canvasFinalRaster.toString());
  const initial=await c.evaluate('CanvasText.inspect()[0]'),before=await c.evaluate('[scrollX,scrollY,document.getElementById("canvas-owner").scrollLeft,document.getElementById("canvas-owner").scrollTop]');
  const raster=await c.evaluate('canvasFinalRaster("chart")',900000);fs.writeFileSync(path.join(OUT,'tiled-raster.json'),JSON.stringify(raster));
  const reconciled=reconcileCanvasRaster(raster,initial);assert.equal(reconciled.labels,4);assert(reconciled.tiles>1);assert.deepEqual(await c.evaluate('[scrollX,scrollY,document.getElementById("canvas-owner").scrollLeft,document.getElementById("canvas-owner").scrollTop]'),before);
  fs.writeFileSync(path.join(OUT,'tiled-raster-artifact-proof.json'),JSON.stringify(artifacts(raster,initial)));
  const corruptions=[
   ['missing-raster-metadata',r=>delete r.tiles,'missing canvas raster metadata'],
   ['wrong-raster-identity',r=>r.labels[0].text='Unrelated','wrong canvas raster identity'],
   ['missing-capture-phase',r=>r.tiles[0].dimensions.pop(),'incomplete canvas capture phases'],
   ['unequal-recorded-raster',r=>r.tiles[0].dimensions[1].width++,'canvas raster frame correspondence differs'],
   ['missing-pixels',r=>r.labels[0].samples=[],'missing canvas final pixel samples'],
   ['duplicate-pixel',r=>{r.labels[0].samples.push({...r.labels[0].samples[0]});r.labels[0].coreSamples++},'duplicate canvas pixel ownership'],
   ['missing-full-ink-metadata',r=>delete r.labels[0].expectedCores,'missing canvas full-ink evidence'],
   ['missing-bitmap-restoration',r=>delete r.tiles[0].bitmapRestores,'missing canvas bitmap restoration evidence'],
   ['missing-capture-token',r=>delete r.tiles[0].dimensions[0].captureToken,'missing or duplicate canvas capture identity'],
   ['wrong-clip-evidence',r=>{const s=r.tiles[0].clipStyles.geometry[0].styles;s.overflowX=s.overflowX==='clip'?'hidden':'clip';},'canvas clipping evidence differs'],
  ];
  for(const [name,change,expected]of corruptions){const copy=structuredClone(raster);change(copy);assert.throws(()=>reconcileCanvasRaster(copy,initial),e=>e.code==='LEARN_CANVAS_SEMANTIC'&&e.assertion===expected,name);rows.push({name,expected,observed:expected});}
  // Calibrate surviving final ink against the unchanged isolated mask. These
  // pre-helper fixture aliases deliberately bypass the product paint guard.
  await c.evaluate(`(()=>{document.body.style.paddingTop='0px';document.body.appendChild(document.getElementById('chart'));document.getElementById('canvas-owner').remove();const target=document.getElementById('chart');target.style.width='320px';target.style.height='200px';window.__canvasFixtureRedraw=()=>{CanvasText.frame(()=>{const ctx=CanvasText.begin(target,320,200,2);ctx.font='600 16px monospace';CanvasText.text(ctx,CanvasText.site(${JSON.stringify(definition)}),'Visible semantic ink',30,80)});if(window.__fixtureCover){const ctx=target.getContext('2d');ctx.save();ctx.setTransform(2,0,0,2,0,0);ctx.fillStyle='#071019';__fixtureRawRect.apply(ctx,__fixtureCover);ctx.restore()}};__canvasFixtureRedraw();})()`);
  const capture=async()=>{const result=await c.evaluate('canvasFinalRaster("chart").then(result=>({result})).catch(e=>({assertion:e.assertion,code:e.code,error:e.message}))',900000);if(result.result){const expected=await c.evaluate('CanvasText.inspect()[0]');reconcileCanvasRaster(result.result,expected);result.artifactProof=artifacts(result.result,expected);}return result};
  const baseline=await capture();assert(baseline.result);const first=baseline.result.labels[0],core=first.samples[0];
  fs.writeFileSync(path.join(OUT,'calibration-baseline.json'),JSON.stringify(baseline));
  for(const [name,mutation,expected]of [
   ['same-color-pixels',"window.__fixtureInkFault='same-color'",'canvas final glyph core occluded'],
   ['low-alpha-pixels',"window.__fixtureInkFault='low-alpha'",'text contrast below threshold'],
   ['late-shape-pixels',`window.__fixtureCover=${JSON.stringify([first.backing.left,first.backing.top,first.backing.right-first.backing.left,first.backing.bottom-first.backing.top])}`,'canvas final glyph core occluded'],
   ['partial-glyph-pixels',`window.__fixtureCover=${JSON.stringify([core.x-1,core.y-1,2,2])}`,'canvas final glyph core occluded'],
  ]){
   await c.evaluate(mutation+';__canvasFixtureRedraw()');const red=await capture();fs.writeFileSync(path.join(OUT,name+'-red.json'),JSON.stringify({red,evidence:await c.evaluate('window.__learnCanvasRasterEvidence')}));assert.equal(red.code,'LEARN_CANVAS_SEMANTIC',name);assert.equal(red.assertion,expected,name);
   await c.evaluate('window.__fixtureInkFault=null;window.__fixtureCover=null;__canvasFixtureRedraw()');const restored=await capture();assert(restored.result,name+' restored green');fs.writeFileSync(path.join(OUT,name+'-restored.json'),JSON.stringify(restored));rows.push({name,expected,observed:red.assertion,restored:true});
  }
  fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
  fs.writeFileSync(path.join(OUT,'events.json'),JSON.stringify(c.events,null,2));assert.equal(c.events.blocked.length,0,'canvas fixture network');assert.equal(c.events.exceptions.length,0,'uncaught canvas runtime errors');
  console.log(`${cases.length+6+corruptions.length+runtimeCorruptions.length}/${cases.length+6+corruptions.length+runtimeCorruptions.length} canvas structural/raster fixtures passed`);
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
if(require.main===module)main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
module.exports={cases};
