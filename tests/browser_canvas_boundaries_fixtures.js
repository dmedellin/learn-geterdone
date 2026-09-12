'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {canvasControls}=require(ROOT+'/tests/canvas_state_controls'),{deriveNumericSource,affine}=require(ROOT+'/tests/canvas_state_sources');
const {lex}=require(ROOT+'/scripts/canvas_sources');
const program=`function fixture(){let fresh=3,confidence=78,hallucination=10;const MIN_CONF=65,MAX_AGE=5,MAX_HALL=20;
 const draw=()=>{const proposal=confidence>=MIN_CONF,freshOk=fresh<=MAX_AGE,hallOk=hallucination<=MAX_HALL;return proposal&&freshOk&&hallOk;};
 bindRange('iFresh',v=>{fresh=v;draw()});bindRange('iConf',v=>{confidence=v;draw()});bindRange('iHall',v=>{hallucination=v;draw()});}`;
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const source=deriveNumericSource(program,'fixture');assert.deepEqual(source.unresolved,[]);assert.deepEqual(source.comparisons.map(c=>[c.id,c.threshold]),[['iFresh',5],['iConf',65],['iHall',20]]);
 assert.deepEqual(affine(lex('v / 100'),new Map(),'v'),{a:.01,b:0});
 for(const expression of ['v*v','v/(1+v)','Math.random()'])assert.throws(()=>affine(lex(expression),new Map(),'v'));
 const unsafe=deriveNumericSource(program.replace('fresh<=MAX_AGE','fresh<=MAX_AGE+confidence'),'fixture');assert(unsafe.unresolved.some(e=>e.id==='iFresh'),'joint threshold must remain unresolved');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><section class=lab><canvas id=chart></canvas><input type=range id=iFresh min=0 max=30 value=3 step=1><input type=range id=iConf min=30 max=99 value=78 step=1><input type=range id=iHall min=0 max=60 value=10 step=5></section>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-boundaries',base:'http://127.0.0.1:'+server.address().port});
 try{
  await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(canvasControls.toString());
  const spec=await c.evaluate('canvasControls('+JSON.stringify(source)+')');fs.writeFileSync(OUT+'/observations.json',JSON.stringify({source,spec},null,2));
  for(const [id,values]of [['iFresh',[4,5,6]],['iConf',[64,65,66]],['iHall',[15,20,25]]])for(const value of values)assert(spec.controls.find(c=>c.key===id).values.includes(value),'source-derived numeric boundary omitted: '+id+'='+value);
  const bad=await c.evaluate('(()=>{try{canvasControls('+JSON.stringify(unsafe)+');return null}catch(e){return e.assertion||e.message}})()');assert.equal(bad,'unresolved source numeric boundary','unresolved boundary may not become finite acceptance');
  assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);console.log(JSON.stringify({fixture:'canvas numeric boundaries',controls:spec.controls.length,sourceComparisons:source.comparisons.length,passed:true}));
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
