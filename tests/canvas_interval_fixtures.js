'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const {intervalDomain,boundedIntervalDomain}=require('./canvas_interval_domain.js'),{installCanvasIntervalClock}=require('./canvas_interval_clock.js');
const protocol=require('./mutation_protocol');
const fixture=(before='')=>'<script>'+before+`function data(mode){let rows=[];for(let i=0;i<3;i++){rows.push({value:i});}return rows;}function init(){let mode='a',rows=data(mode),shown=1,timer=null,speed=10;const draw=()=>{};const stop=()=>{clearInterval(timer);timer=null};const step=()=>{shown=Math.min(rows.length,shown+1);draw();if(shown>=rows.length)stop()};const play=()=>{timer=setInterval(step,speed)};}`+'</script>';
const rows=[];const check=(name,fn)=>{try{fn();rows.push({name,passed:true})}catch(error){throw Object.assign(Error(name),{assertion:name,code:'LEARN_CANVAS_SEMANTIC',cause:error})}};
try{
 check('interval lexical Unicode identity',()=>{const d=boundedIntervalDomain(fixture('const title="交易 🙂";'));assert.equal(d[0].source,'()=>{shown=Math.min(rows.length,shown+1);draw();if(shown>=rows.length)stop()}');assert.deepEqual(d[0].states,[1,2,3]);});
 check('interval ignores inert text',()=>{const d=boundedIntervalDomain(fixture('/* setInterval(foo,delay); */const s="setInterval(foo,delay)";const t=`setInterval(foo,delay)`;'));assert.equal(d.length,1)});
 const mutations=[
  ['conditional insertion','rows.push({value:i})','if(i>0)rows.push({value:i})'],
  ['nested insertion','rows.push({value:i})','if(i>0){rows.push({value:i})}'],
  ['extra insertion','rows.push({value:i})','rows.push({value:i});rows.push({value:i})'],
  ['array alias','rows.push({value:i})','const alias=rows;alias.push({value:i})'],
  ['loop break','rows.push({value:i})','if(i>0)break;rows.push({value:i})'],
  ['loop continue','rows.push({value:i})','if(i>0)continue;rows.push({value:i})'],
  ['unbounded loop','i<3','true'],
  ['inexact loop','i++','i+=2'],
  ['changed increment','shown+1','shown+2'],
  ['missing clamp','Math.min(rows.length,shown+1)','shown+1'],
  ['missing terminal stop','if(shown>=rows.length)stop()',''],
  ['unbound initial','shown=1','shown=2'],
  ['string timer','setInterval(step,speed)','setInterval("step()",speed)'],
  ['timer arguments','setInterval(step,speed)','setInterval(step,speed,7)'],
  ['timer alias','setInterval(step,speed)','setInterval.call(window,step,speed)']
 ];
 for(const [name,from,to]of mutations)check('closed interval domain '+name,()=>assert.throws(()=>boundedIntervalDomain(fixture().replace(from,to))));
 const context=vm.createContext({});vm.runInContext('window=globalThis;count=0;cb=()=>{count++};',context);
 const source=vm.runInContext('cb.toString()',context);vm.runInContext('('+installCanvasIntervalClock.toString()+')('+JSON.stringify([{id:'fixture.step',source}])+')',context);
 check('held interval does not execute on registration',()=>{vm.runInContext('timer=setInterval(cb,10)',context);assert.equal(context.count,0);assert.equal(vm.runInContext('__learnCanvasClock.snapshot().active.length',context),1)});
 check('clock executes original closure once',()=>{vm.runInContext('__learnCanvasClock.tick(timer)',context);assert.equal(context.count,1)});
 for(const [name,expression,expected]of [
  ['unregistered callback','setInterval(()=>{},10)','unregistered canvas interval transition'],
  ['string callback','setInterval("count++",10)','unsupported canvas interval transition'],
  ['fractional delay','setInterval(cb,.5)','unsupported canvas interval transition'],
  ['negative delay','setInterval(cb,-1)','unsupported canvas interval transition'],
  ['extra argument','setInterval(cb,10,1)','unsupported canvas interval transition'],
  ['unknown tick','__learnCanvasClock.tick(999)','missing canvas interval transition']
 ])check('closed interval clock '+name,()=>{const error=vm.runInContext('(()=>{try{'+expression+';return null}catch(e){return {code:e.code,assertion:e.assertion}}})()',context);assert.equal(error?.code,'LEARN_CANVAS_SEMANTIC');assert.equal(error.assertion,expected)});
 check('interval cancellation removes original closure',()=>{vm.runInContext('clearInterval(timer)',context);assert.equal(vm.runInContext('__learnCanvasClock.snapshot().active.length',context),0);assert.equal(context.count,1)});
 if(process.env.BROWSER_EVIDENCE){fs.mkdirSync(process.env.BROWSER_EVIDENCE,{recursive:true});fs.writeFileSync(process.env.BROWSER_EVIDENCE+'/interval-fixtures.json',JSON.stringify(rows,null,2))}console.log(JSON.stringify({passed:rows.length,finiteApplicationProofComplete:false}));
}catch(e){if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1}
