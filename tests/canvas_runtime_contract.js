'use strict';
// Installed before any document script, so capturing a native method early,
// using aliases, reflection or another wrapper cannot escape observation.
function interceptCanvasText(){
 'use strict';
 const calls=[],history=[],failures=[],tokens=new WeakMap();
 const context=HTMLCanvasElement.prototype.getContext,readPixels=CanvasRenderingContext2D.prototype.getImageData,writePixels=CanvasRenderingContext2D.prototype.putImageData;
 const fail=(assertion,detail)=>failures.push({assertion,...detail});
 const prototypes=[CanvasRenderingContext2D.prototype];if(window.OffscreenCanvasRenderingContext2D)prototypes.push(OffscreenCanvasRenderingContext2D.prototype);
 for(const prototype of prototypes)for(const method of ['fillText','strokeText']){
  const original=prototype[method],measure=prototype.measureText,transform=prototype.getTransform;
  Object.defineProperty(prototype,method,{configurable:true,writable:true,value:function(...args){
   const active=window.CanvasText?.nativeToken(),canvas=this.canvas;
   if(!active||!active.token||active.canvas!==canvas||!active.descriptor||!Object.isFrozen(active.token)){
    fail('uncontracted runtime native text',{method,canvas:canvas.id||null,text:String(args[0])});return original.apply(this,args);
   }
   const id=active.descriptor.id,definition=JSON.stringify(active.descriptor),prior=tokens.get(active.token);
   if(prior&&prior!==definition)fail('runtime token identity changed',{id});tokens.set(active.token,definition);
   if(active.text!==String(args[0]))fail('wrong native semantic identity',{id});
   if(!active.diagnostic&&(CanvasText.phase(canvas)!=='text'||!Number.isInteger(active.execution)||active.execution<1||!Number.isInteger(active.ordinal)||!Number.isInteger(active.count)||active.ordinal<0||active.ordinal>=active.count))fail('native text outside final flush',{id});
   const metrics=measure.call(this,String(args[0])),matrix=transform.call(this);
   const record={method,canvas:(active.owner||canvas).id,site:id,descriptor:active.descriptor,instance:active.instance,text:String(args[0]),diagnostic:!!active.diagnostic,execution:active.execution,ordinal:active.ordinal,count:active.count,geometry:active.geometry,
    x:args[1],y:args[2],maxWidth:args.length>3?args[3]:null,font:this.font,align:this.textAlign,baseline:this.textBaseline,matrix:[matrix.a,matrix.b,matrix.c,matrix.d,matrix.e,matrix.f],metrics:Object.fromEntries(['width','actualBoundingBoxLeft','actualBoundingBoxRight','actualBoundingBoxAscent','actualBoundingBoxDescent'].map(k=>[k,metrics[k]]))};
   calls.push(record);history.push(record);
   return original.apply(this,args);
  }});
 }
 for(const prototype of prototypes)for(const method of ['clearRect','fillRect','strokeRect','fill','stroke','drawImage','putImageData','reset']){
  const original=prototype[method];
  Object.defineProperty(prototype,method,{configurable:true,writable:true,value:function(...args){
   if(window.CanvasText?.phase(this.canvas)==='final')fail('paint after text finalization',{method,canvas:this.canvas.id});
   return original.apply(this,args);
  }});
 }
 // A redraw starts a new correspondence interval, never a new audit. A
 // native bypass during startup must still reject every subsequent frame.
 Object.defineProperty(window,'__learnCanvasNative',{value:Object.freeze({snapshot:()=>({calls:JSON.parse(JSON.stringify(calls)),history:JSON.parse(JSON.stringify(history)),failures:JSON.parse(JSON.stringify(failures))}),clear:()=>{calls.length=0;},
  // Test-only bitmap substitution retains the actual canvas element, CSS
  // clips, scroll owners and observation frame. It never supplies accepted
  // foreground pixels. Return the prior decoded bitmap so callers can verify
  // an ordinary suppressed redraw restores it without a pixel round trip.
  replaceBitmap:(canvas,pixels)=>{
   if(!(canvas instanceof HTMLCanvasElement)||!(pixels instanceof ImageData)||pixels.width!==canvas.width||pixels.height!==canvas.height)throw Error('raster setup failure: diagnostic bitmap dimensions differ');
   const raw=context.call(canvas,'2d'),prior=readPixels.call(raw,0,0,canvas.width,canvas.height);writePixels.call(raw,pixels,0,0);return prior;
  }
 }),writable:false,configurable:false});
}
const metricKeys=['width','actualBoundingBoxLeft','actualBoundingBoxRight','actualBoundingBoxAscent','actualBoundingBoxDescent'];
const boundKeys=['left','right','top','bottom'];
const finiteFields=(value,keys)=>value&&keys.every(key=>Number.isFinite(value[key]));
const validBounds=value=>finiteFields(value,boundKeys)&&value.left<value.right&&value.top<value.bottom;
const validMetrics=value=>finiteFields(value,metricKeys)&&value.width>0;
const validMaxWidth=value=>value===null||Number.isFinite(value)&&value>0;
function reconcileRuntimeHistory(source,native){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 if(!native||!Array.isArray(native.history)||!Array.isArray(native.failures))fail('missing canvas native history');
 if(native.failures.length)fail(native.failures[0].assertion);
 const canvases=new Set(source.canvases.map(c=>c.id)),descriptors=new Map(source.occurrences.map(s=>[s.siteID,JSON.stringify(s.descriptor)])),groups=new Map();
 for(const call of native.history.filter(c=>!c.diagnostic)){
  if(!canvases.has(call.canvas)||call.method!=='fillText'||descriptors.get(call.site)!==JSON.stringify(call.descriptor))fail('wrong historic canvas semantic identity');
  const key=call.canvas+':'+call.execution;if(!groups.has(key))groups.set(key,[]);groups.get(key).push(call);
  const g=call.geometry,m=call.metrics;
  if(!g||!validBounds(g.region)||!validBounds(g.ink)||!validMetrics(m)||!validMaxWidth(call.maxWidth)||!Array.isArray(call.matrix)||call.matrix.length!==6||![g.width,g.height,g.dpr,call.x,call.y,...call.matrix].every(Number.isFinite)||g.width<=0||g.height<=0||g.dpr<=0)fail('missing historic canvas geometry');
  const k=call.maxWidth===null||!m.width?1:Math.min(1,call.maxWidth/m.width),[a,b,c,d,e,f]=call.matrix;
  const corners=[];for(const x of [call.x-m.actualBoundingBoxLeft*k,call.x+m.actualBoundingBoxRight*k])for(const y of [call.y-m.actualBoundingBoxAscent,call.y+m.actualBoundingBoxDescent])corners.push({x:(a*x+c*y+e)/g.dpr,y:(b*x+d*y+f)/g.dpr});
  const ink={left:Math.min(...corners.map(p=>p.x)),right:Math.max(...corners.map(p=>p.x)),top:Math.min(...corners.map(p=>p.y)),bottom:Math.max(...corners.map(p=>p.y))};
  if(Object.keys(ink).some(k=>Math.abs(ink[k]-g.ink[k])>1e-7)||corners.some(p=>p.x<g.region.left||p.x>g.region.right||p.y<g.region.top||p.y>g.region.bottom||p.x<0||p.y<0||p.x>g.width||p.y>g.height))fail('historic native ink differs from semantic bounds');
 }
 for(const group of groups.values())if(group.some((c,i)=>!Number.isInteger(c.execution)||c.execution<1||c.count!==group.length||c.ordinal!==i))fail('incomplete historic native canvas frame');
 return {frames:groups.size,nativeCalls:native.history.filter(c=>!c.diagnostic).length,diagnosticCalls:native.history.filter(c=>c.diagnostic).length};
}
function reconcileRuntime(source,live,native){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 if(!source?.canvases?.length||!live?.length||!native?.calls?.length)fail('empty canvas runtime inventory');
 if(native.failures.length)fail(native.failures[0].assertion);
 if(JSON.stringify(source.canvases.map(c=>c.id).sort())!==JSON.stringify(live.map(c=>c.canvas).sort()))fail('canvas source/live identities differ');
 const descriptors=new Map(source.occurrences.map(s=>[s.siteID,JSON.stringify(s.descriptor)]));
 const expected=[];
 for(const frame of live){
  if(frame.status!=='final'||!frame.labels.length)fail('missing canvas finalization');
  for(const label of frame.labels){
   if(descriptors.get(label.site)!==JSON.stringify(label.descriptor))fail('wrong canvas semantic identity');
   expected.push(JSON.stringify([frame.canvas,label.site,label.instance,label.text]));
  }
 }
 const actual=native.calls.filter(c=>!c.diagnostic).map(c=>{
  if(c.method!=='fillText'||descriptors.get(c.site)!==JSON.stringify(c.descriptor))fail('wrong native semantic identity');
  return JSON.stringify([c.canvas,c.site,c.instance,c.text]);
 });
 const groups=new Map();for(const call of native.calls.filter(c=>!c.diagnostic)){const key=call.canvas+':'+call.execution;if(!groups.has(key))groups.set(key,[]);groups.get(key).push(call);}
 for(const group of groups.values())if(group.some((c,i)=>!Number.isInteger(c.execution)||c.execution<1||c.count!==group.length||c.ordinal!==i))fail('incomplete native canvas frame');
 if(JSON.stringify(actual.sort())!==JSON.stringify(expected.sort()))fail('source/live/native label occurrence mismatch');
 for(const call of native.calls.filter(c=>!c.diagnostic)){
  const frame=live.find(f=>f.canvas===call.canvas),label=frame.labels.find(l=>l.instance===call.instance);
  if(call.font!==label.font||call.align!==label.align||call.baseline!==label.baseline||call.maxWidth!==label.maxWidth||!validMetrics(call.metrics)||!validMaxWidth(call.maxWidth)||!validBounds(label.region)||!validBounds(label.ink)||!Array.isArray(call.matrix)||call.matrix.length!==6||![call.x,call.y,frame.width,frame.height,frame.dpr,...call.matrix].every(Number.isFinite)||frame.width<=0||frame.height<=0||frame.dpr<=0)fail('missing native canvas geometry');
  // Independently reconstruct all four actual native ink corners with scalar
  // affine arithmetic. The product places boxes through DOMMatrix instead.
  const m=call.metrics,k=call.maxWidth===null||!m.width?1:Math.min(1,call.maxWidth/m.width),[a,b,c,d,e,f]=call.matrix;
  const corners=[];for(const x of [call.x-m.actualBoundingBoxLeft*k,call.x+m.actualBoundingBoxRight*k])for(const y of [call.y-m.actualBoundingBoxAscent,call.y+m.actualBoundingBoxDescent])corners.push({x:(a*x+c*y+e)/frame.dpr,y:(b*x+d*y+f)/frame.dpr});
  const bounds={left:Math.min(...corners.map(p=>p.x)),right:Math.max(...corners.map(p=>p.x)),top:Math.min(...corners.map(p=>p.y)),bottom:Math.max(...corners.map(p=>p.y))};
  if(corners.some(p=>p.x<label.region.left||p.x>label.region.right||p.y<label.region.top||p.y>label.region.bottom||p.x<0||p.y<0||p.x>frame.width||p.y>frame.height))fail('native transformed corner outside semantic region');
  if(Object.keys(bounds).some(k=>Math.abs(bounds[k]-label.ink[k])>1e-7))fail('native ink differs from semantic bounds');
 }
 const history=reconcileRuntimeHistory(source,native);
 return {canvases:live.length,labels:expected.length,uncontracted:0,history};
}
module.exports={interceptCanvasText,reconcileRuntimeHistory,reconcileRuntime};
