'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require('./browser_cdp'),protocol=require('./mutation_protocol'),{interceptCanvasText}=require('./canvas_runtime_contract'),{reconcileDocument}=require('./browser_canvas_inventory');
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><link rel=icon href=data:,><p>Canvas inventory fixture</p>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-document',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 const cases=[
  ['normal-empty','',[],null],
  ['added-live-canvas',"const canvas=document.createElement('canvas');canvas.id='unexpected';document.body.append(canvas);",[],'canvas source/live identities differ'],
  ['missing-source-canvas','',[{id:'missing'}],'canvas source/live identities differ'],
  ['wrong-canvas-identity',"const canvas=document.createElement('canvas');canvas.id='wrong';document.body.append(canvas);",[{id:'expected'}],'canvas source/live identities differ'],
  ['detached-native-bypass',"document.createElement('canvas').getContext('2d').fillText('Unbound',10,20);",[],'uncontracted runtime native text'],
  ['orphan-helper','window.CanvasText={};',[],'unexpected canvas runtime on noncanvas route'],
  ['missing-native-history','',[],'missing canvas native history']
 ];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const [name,script,canvases,expected]of cases){
   await c.navigate('/',{width:390,height:844,theme:'dark'});if(script)await c.evaluate('(()=>{'+script+'})()');
   const value=await c.evaluate(`({canvases:[...document.querySelectorAll('canvas')].map(c=>c.id),helper:!!window.CanvasText,pending:0,live:[],native:__learnCanvasNative.snapshot()})`);
   if(name==='missing-native-history')delete value.native.history;
   let observed=null;try{reconcileDocument({canvases,occurrences:[]},value)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;observed=e.assertion;}
   rows.push({name,expected,observed,source:{canvases,occurrences:[]},value});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
   assert.equal(observed,expected,'complete document canvas inventory: '+name);assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);
  }
  console.log(cases.length+'/'+cases.length+' document canvas inventory fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
