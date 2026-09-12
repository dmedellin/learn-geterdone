'use strict';
// Test environment only. Hold authored interval transitions, leave RAF and
// all non-interval APIs native, and execute the original closure on demand.
function installCanvasIntervalClock(definitions){
 const nativeSource=Function.prototype.toString,scheduled=new Map(),history=[];let serial=0;
 const fail=assertion=>{throw Object.assign(Error(assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion})};
 if(!Array.isArray(definitions)||!definitions.length||definitions.some(d=>!d.id||typeof d.source!=='string')||new Set(definitions.map(d=>d.id)).size!==definitions.length||new Set(definitions.map(d=>d.source)).size!==definitions.length)fail('invalid canvas interval domain');
 Object.defineProperty(window,'setInterval',{value:function(callback,delay,...args){
  if(typeof callback!=='function'||args.length||!Number.isInteger(delay)||delay<=0)fail('unsupported canvas interval transition');
  const source=nativeSource.call(callback),definition=definitions.find(d=>d.source===source);if(!definition)fail('unregistered canvas interval transition');
  const id=++serial;scheduled.set(id,{callback,delay,definition});history.push({action:'register',id,delay,definition:definition.id});return id;
 },writable:false,configurable:false});
 Object.defineProperty(window,'clearInterval',{value:function(id){if(scheduled.has(id)){history.push({action:'clear',id});scheduled.delete(id);}},writable:false,configurable:false});
 Object.defineProperty(window,'__learnCanvasClock',{value:Object.freeze({
  snapshot:()=>({active:[...scheduled].map(([id,s])=>({id,delay:s.delay,definition:s.definition.id})),history:history.map(h=>({...h}))}),
  tick:id=>{const task=scheduled.get(id);if(!task)fail('missing canvas interval transition');history.push({action:'tick',id});task.callback.call(window);}
 }),writable:false,configurable:false});
}
module.exports={installCanvasIntervalClock};
