'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require('./browser_cdp'),protocol=require('./mutation_protocol'),{canvasControls,refreshCanvasControls}=require('./canvas_state_controls');
const html='<!doctype html><link rel=icon href=data:,><section class=lab><canvas id=chart></canvas><select id=mode><option value=a>A</option><option value=b>B</option></select><input id=level type=range min=0 max=10 step=1 value=5><button id=action>Run</button></section>';
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end(html)});await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-control-refresh',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 const cases=[['normal','',false],['replaced-control',"document.getElementById('action').outerHTML='<button id=action>Run again</button>';",false],['missing-control',"document.getElementById('action').remove();",true],['omitted-option',"document.getElementById('mode').options[1].remove();",true],['changed-numeric-boundary',"document.getElementById('level').max='11';",true],['new-conditional-control',"document.querySelector('.lab').insertAdjacentHTML('beforeend','<button id=newAction>New</button>');",true],['wrong-control-kind',"document.getElementById('level').type='checkbox';",true],['wrong-control-identity',"document.getElementById('action').id='different';",true]];
 try{for(const [name,change,negative]of cases){
  await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(canvasControls.toString()+'\n'+refreshCanvasControls.toString());
  const value=await c.evaluate(`(()=>{const expected=canvasControls();${change}try{return {result:refreshCanvasControls(expected)}}catch(e){return {assertion:e.assertion,code:e.code,error:e.message}}})()`);rows.push({name,negative,...value});fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));
  if(negative){assert.equal(value.code,'LEARN_CANVAS_SEMANTIC','canvas control refresh rejects changed domain: '+name);assert.equal(value.assertion,'canvas control domain changed without witness',name);}else{assert(value.result,name);assert.equal(value.result.targets.some(t=>t.replaced),name==='replaced-control',name);}
  assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);
 }console.log(cases.length+'/'+cases.length+' canvas control refresh fixtures passed');}finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
