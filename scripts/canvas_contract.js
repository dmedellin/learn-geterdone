/* Learn canvas text contract v1. Inlined by the authored-page normalizer. */
(()=>{
 'use strict';
 const roles=Object.freeze({axis:4.5,annotation:4.5,value:4.5,status:4.5,date:4.5});
 const tokens=new WeakMap(),sites=new Map(),contexts=new WeakMap(),pending=new Map(),completed=new Map(),gutters=new WeakMap();
 const nativeFill=CanvasRenderingContext2D.prototype.fillText;
 const paintObjects=new WeakMap();
 let depth=0,active=null,probe=null,execution=0;
 const fail=message=>{throw Object.assign(Error('canvas contract: '+message),{code:'LEARN_CANVAS_SEMANTIC',assertion:message})};
 const finite=values=>values.every(Number.isFinite);
 const stable=value=>JSON.stringify(value,Object.keys(value).sort());
 function site(definition){
  if(!definition||typeof definition!=='object')fail('missing descriptor');
  if(['guide','decorative'].includes(definition.role))fail('decorative guide used as semantic text');
  const keys=['id','role','minimumContrast','region','collision','formatter','family','mode','dependencies'];
  if(Object.keys(definition).sort().join()!==keys.sort().join()||typeof definition.id!=='string'||!/^[a-zA-Z0-9_.:-]+$/.test(definition.id)||typeof definition.role!=='string'||!Object.hasOwn(roles,definition.role)||!Number.isFinite(definition.minimumContrast)||definition.minimumContrast!==roles[definition.role]||!['axis-right','axis-left','axis-bottom','title-top','annotation','date-left','date-bottom-left','date-bottom-right','label-left','value-right','status'].includes(definition.region)||!['separate','fixed'].includes(definition.collision)||['formatter','family','mode'].some(k=>typeof definition[k]!=='string'||!definition[k])||!Array.isArray(definition.dependencies)||definition.dependencies.some(d=>typeof d!=='string'||!d)||new Set(definition.dependencies).size!==definition.dependencies.length||['frame.width','frame.height','theme'].some(d=>!definition.dependencies.includes(d)))fail('invalid semantic descriptor');
  const key=stable(definition),prior=sites.get(definition.id);
  if(prior){if(prior.key!==key)fail('conflicting descriptor '+definition.id);return prior.token;}
  const descriptor=Object.freeze({...definition,dependencies:Object.freeze([...definition.dependencies])}),token=Object.freeze(Object.create(null));
  tokens.set(token,descriptor);sites.set(descriptor.id,{key,descriptor,token});return token;
 }
 function rolePaint(canvas,role){
  if(typeof role!=='string'||!Object.hasOwn(roles,role))fail('decorative guide used as semantic text');
  for(let e=canvas;e;e=e.parentElement){const s=getComputedStyle(e);if(Number(s.opacity)!==1||s.filter!=='none'||s.mixBlendMode!=='normal')fail('unprovable canvas ancestor paint');}
  const style=getComputedStyle(canvas),foreground=style.getPropertyValue('--text').trim(),background=style.getPropertyValue('--panel-2').trim();
  const pixel=document.createElement('canvas');pixel.width=pixel.height=1;const c=pixel.getContext('2d',{willReadFrequently:true});
  const resolve=color=>{if(!CSS.supports('color',color))fail('unresolved semantic paint');c.clearRect(0,0,1,1);c.fillStyle=color;c.fillRect(0,0,1,1);const rgba=[...c.getImageData(0,0,1,1).data];if(rgba[3]!==255)fail('semantic role paint must be opaque');return rgba.slice(0,3)};
  const fg=resolve(foreground),bg=resolve(background);
  const luminance=rgb=>rgb.map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
  const a=luminance(fg),b=luminance(bg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
  if(ratio<roles[role])fail('text contrast below threshold');
  return {foreground,background,fg,bg,ratio};
 }
 function traceValue(value){
  if(value===null||typeof value==='string'||typeof value==='boolean')return value;
  if(value===undefined)return {undefined:true};
  if(typeof value==='number'&&Number.isFinite(value))return value;
  if(Array.isArray(value)){const items=[];for(let i=0;i<value.length;i++){if(!Object.hasOwn(value,i))fail('unprovable canvas trace value');items.push(traceValue(value[i]));}return {array:items};}
  const paint=value&&typeof value==='object'?paintObjects.get(value):null;
  if(paint)return {gradient:paint.kind,id:paint.id,arguments:paint.args,stops:paint.stops.map(s=>s.slice())};
  fail('unprovable canvas trace value');
 }
 function trackedGradient(raw,kind,args,frame){
  const record={raw,kind,id:++frame.paintSequence,frame,args:args.map(traceValue),stops:[],proxy:null};
  const proxy=new Proxy(Object.create(null),{get(_target,key){const target=raw;
   if(key!=='addColorStop')fail('unprovable canvas gradient access');
   return (...args)=>{if(frame.status!=='geometry'||pending.get(frame.canvas)!==frame)fail('gradient mutation outside canvas frame');if(args.length!==2)fail('unprovable canvas gradient stop');const stop=args.map(traceValue);target.addColorStop(...args);record.stops.push(stop);frame.trace.push(['gradient-stop',record.id,record.kind,record.args,stop]);};
  },defineProperty(){fail('canvas gradient reflection mutation')},deleteProperty(){fail('canvas gradient reflection mutation')},setPrototypeOf(){fail('canvas gradient reflection mutation')},preventExtensions(){fail('canvas gradient reflection mutation')},set(){fail('canvas gradient reflection mutation')}});
  record.proxy=proxy;paintObjects.set(raw,record);paintObjects.set(proxy,record);return proxy;
 }
 const operationMethods=new Set(['save','restore','reset','setTransform','resetTransform','transform','translate','rotate','scale','setLineDash','getLineDash','beginPath','moveTo','lineTo','bezierCurveTo','quadraticCurveTo','arc','arcTo','ellipse','rect','roundRect','closePath','fill','stroke','fillRect','strokeRect','clearRect','clip','measureText','getTransform','getImageData','createImageData','putImageData','drawImage','createLinearGradient','createRadialGradient','createConicGradient','isPointInPath','isPointInStroke','getContextAttributes','isContextLost']);
 const stateProperties=new Set(['direction','fillStyle','filter','font','fontKerning','fontStretch','fontVariantCaps','globalAlpha','globalCompositeOperation','imageSmoothingEnabled','imageSmoothingQuality','lang','letterSpacing','lineCap','lineDashOffset','lineJoin','lineWidth','miterLimit','shadowBlur','shadowColor','shadowOffsetX','shadowOffsetY','strokeStyle','textAlign','textBaseline','textRendering','wordSpacing']);
 const paintMethods=new Set(['reset','clearRect','fillRect','strokeRect','fill','stroke','drawImage','putImageData','fillText','strokeText']);
 function begin(canvas,width,height,dpr){
  if(!depth)fail('frame missing');
  if(!(canvas instanceof HTMLCanvasElement)||!finite([width,height,dpr])||width<=0||height<=0||dpr<=0)fail('invalid canvas dimensions');
  if(pending.has(canvas))fail('canvas begun twice without finalization');
  const raw=canvas.getContext('2d');if(!raw)fail('2D context missing');
  const frame={canvas,raw,width,height,dpr,execution:++execution,status:'geometry',commands:[],trace:[],labels:[],paintSequence:0,clipDepth:0,clipStack:[]};
  pending.set(canvas,frame);
  if(canvas.width!==Math.round(width*dpr))canvas.width=Math.round(width*dpr);if(canvas.height!==Math.round(height*dpr))canvas.height=Math.round(height*dpr);
  raw.reset();raw.setTransform(dpr,0,0,dpr,0,0);
  const proxy=new Proxy(Object.create(null),{
   get(_target,key){const target=raw;
    const value=Reflect.get(target,key,target);
    if(typeof value!=='function')return paintObjects.get(value)?.proxy||value;
    return (...args)=>{
     if(key==='fillText'||key==='strokeText')fail('uncontracted native text');
     if(!operationMethods.has(key))fail('unsupported canvas operation '+String(key));
     if(paintMethods.has(key)&&frame.status!=='geometry')fail('paint after text finalization');
     frame.trace.push([String(key),args.map(traceValue)]);
     const result=value.apply(target,args);
     return ['createLinearGradient','createRadialGradient','createConicGradient'].includes(key)?trackedGradient(result,key,args,frame):result;
    };
   },
   defineProperty(){fail('canvas context reflection mutation')},deleteProperty(){fail('canvas context reflection mutation')},setPrototypeOf(){fail('canvas context reflection mutation')},preventExtensions(){fail('canvas context reflection mutation')},
   set(_target,key,value){if(!stateProperties.has(key))fail('unsupported canvas state property '+String(key));const target=raw;const paint=paintObjects.get(value);if(paint&&paint.frame!==frame)fail('gradient used outside canvas frame');frame.trace.push(['set',String(key),traceValue(value)]);return Reflect.set(target,key,paint?.raw||value,target)}
  });
  contexts.set(proxy,frame);pending.set(canvas,frame);return proxy;
 }
 function region(frame,name){
  const w=frame.width,h=frame.height,gutter=gutters.get(frame.canvas)||0;
  const regions={'axis-bottom':[6,h-29,w-6,h-2],'title-top':[6,4,w-6,44],'axis-right':[w-(gutter||68),4,w-4,h-4],'axis-left':[2,4,46,h-30],'date-bottom-left':[42,h-28,w/2,h-2],'date-bottom-right':[w/2,h-28,w-8,h-2],'label-left':[6,6,168,h-6],annotation:[6,44,w-Math.max(74,gutter+8),h-30],'date-left':[6,6,Math.min(116,w/3),h-6],'value-right':[w-116,6,w-6,h-6],status:[6,48,w-6,h-6]};
  const r=regions[name];if(!r||r[0]<0||r[1]<0||r[2]>w||r[3]>h||r[0]>=r[2]||r[1]>=r[3])fail('invalid descriptor region');
  return {left:r[0],top:r[1],right:r[2],bottom:r[3]};
 }
 function text(context,token,value,x,y,maxWidth){
  if(arguments.length<5||arguments.length>6)fail('arbitrary semantic paint arguments');
  const descriptor=tokens.get(token),frame=contexts.get(context);
  if(!descriptor)fail('unbound site token');if(!frame||frame.status!=='geometry'||!pending.has(frame.canvas))fail('semantic text outside frame');
  if(frame.clipDepth)fail('unprovable semantic clip');
  const raw=frame.raw,label=String(value);if(!label.trim())fail('empty semantic text');
  if(!finite([x,y])||maxWidth!==undefined&&(!Number.isFinite(maxWidth)||maxWidth<=0))fail('nonfinite semantic geometry');
  if(raw.globalAlpha!==1)fail('semantic alpha below one');
  if(raw.globalCompositeOperation!=='source-over')fail('unsupported semantic composite');
  if(typeof raw.fillStyle!=='string')fail('gradient or pattern used for semantic text');
  if(raw.filter!=='none'||raw.shadowBlur||raw.shadowOffsetX||raw.shadowOffsetY||!['rgba(0, 0, 0, 0)','transparent','#00000000'].includes(raw.shadowColor))fail('unprovable semantic shadow or filter');
  let matrix=raw.getTransform();if(!matrix.is2D||!finite([matrix.a,matrix.b,matrix.c,matrix.d,matrix.e,matrix.f])||Math.abs(matrix.a*matrix.d-matrix.b*matrix.c)<1e-12)fail('unprovable semantic transform');
  // Chromium normalizes a six-number setTransform differently from an
  // accumulated rotate/translate matrix. Measure the transform that the
  // final flush will actually apply, leaving graph drawing state intact.
  raw.save();raw.setTransform(matrix.a,matrix.b,matrix.c,matrix.d,matrix.e,matrix.f);matrix=raw.getTransform();raw.restore();
  for(const property of ['letterSpacing','wordSpacing'])if(raw[property]!==undefined){if(raw[property]!==''&&raw[property]!=='0px')fail('unprovable semantic font spacing');raw[property]='1px';raw[property]='0px';if(raw[property]!=='0px')fail('unresolved semantic font spacing');}
  raw.fontKerning='none';raw.direction=raw.direction==='inherit'?getComputedStyle(frame.canvas).direction:raw.direction;
  const font=/^(?:(italic|oblique) )?(?:(normal|bold|[1-9]00) )?([0-9.]+)px (.+)$/.exec(raw.font);if(!font)fail('unresolved semantic font');
  raw.font=(font[1]?font[1]+' ':'')+Math.max(600,font[2]==='bold'?700:Number(font[2])||400)+' '+Math.max(12,Number(font[3]))+'px '+font[4];
  const metrics=raw.measureText(label),required=['width','actualBoundingBoxLeft','actualBoundingBoxRight','actualBoundingBoxAscent','actualBoundingBoxDescent'];
  if(!finite(required.map(k=>metrics[k])))fail('incomplete text metrics');
  const command={descriptor,token,text:label,x,y,maxWidth,metrics:Object.fromEntries(required.map(k=>[k,metrics[k]])),matrix:[matrix.a,matrix.b,matrix.c,matrix.d,matrix.e,matrix.f],font:raw.font,align:raw.textAlign,baseline:raw.textBaseline,direction:raw.direction,paint:rolePaint(frame.canvas,descriptor.role),region:region(frame,descriptor.region)};
  frame.commands.push(command);
 }
 function bounds(command,frame,x=command.x,y=command.y){
  const m=command.metrics,compress=command.maxWidth===undefined||!m.width?1:Math.min(1,command.maxWidth/m.width),matrix=new DOMMatrix(command.matrix);
  const corners=[[x-m.actualBoundingBoxLeft*compress,y-m.actualBoundingBoxAscent],[x+m.actualBoundingBoxRight*compress,y-m.actualBoundingBoxAscent],[x+m.actualBoundingBoxRight*compress,y+m.actualBoundingBoxDescent],[x-m.actualBoundingBoxLeft*compress,y+m.actualBoundingBoxDescent]].map(([x,y])=>{const p=matrix.transformPoint({x,y});return {x:p.x/frame.dpr,y:p.y/frame.dpr}});
  return {left:Math.min(...corners.map(p=>p.x)),right:Math.max(...corners.map(p=>p.x)),top:Math.min(...corners.map(p=>p.y)),bottom:Math.max(...corners.map(p=>p.y)),corners};
 }
 const intersects=(a,b)=>a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom;
 const inside=(a,b)=>a.left>=b.left&&a.right<=b.right&&a.top>=b.top&&a.bottom<=b.bottom;
 function finish(frame){
  if(frame.status!=='geometry')fail('duplicate finalization');
  if(frame.clipDepth)fail('unprovable semantic clip at finalization');
  const placed=[];
  for(const command of frame.commands){
   const initial=bounds(command,frame),pad=2,inkWidth=initial.right-initial.left,inkHeight=initial.bottom-initial.top,r=command.region;
   if(inkWidth<=0||inkHeight<=0||inkWidth+2*pad>r.right-r.left||inkHeight+2*pad>r.bottom-r.top)fail('unplaceable semantic text '+command.descriptor.id);
   let left=Math.max(r.left+pad,Math.min(initial.left,r.right-pad-inkWidth)),top=Math.max(r.top+pad,Math.min(initial.top,r.bottom-pad-inkHeight));
   const candidate=(left,top)=>({left:left-pad,right:left+inkWidth+pad,top:top-pad,bottom:top+inkHeight+pad});
   let box=candidate(left,top);
   if(command.descriptor.collision==='separate'&&placed.some(p=>intersects(box,p.box))){
    const choices=[];
    for(let y=r.top+pad;y<=r.bottom-pad-inkHeight;y+=inkHeight+2*pad+1)for(let x=r.left+pad;x<=r.right-pad-inkWidth;x+=inkWidth+2*pad+1)choices.push({x,y,d:(x-left)**2+(y-top)**2});
    choices.sort((a,b)=>a.d-b.d||a.y-b.y||a.x-b.x);
    const spot=choices.find(p=>!placed.some(q=>intersects(candidate(p.x,p.y),q.box)));
    if(!spot)fail('unplaceable semantic collision '+command.descriptor.id);left=spot.x;top=spot.y;box=candidate(left,top);
   }
   if(placed.some(p=>intersects(box,p.box)))fail('semantic bounds overlap');
   const inverse=new DOMMatrix(command.matrix).inverse(),shift=inverse.transformPoint({x:(left-initial.left)*frame.dpr,y:(top-initial.top)*frame.dpr,w:0});
   const x=command.x+shift.x,y=command.y+shift.y,ink=bounds(command,frame,x,y);
   if(!inside(ink,r)||ink.corners.some(p=>p.x<0||p.y<0||p.x>frame.width||p.y>frame.height))fail('transformed semantic corner outside region');
   placed.push({command,x,y,ink,box});
  }
  frame.placed=placed;frame.status='text';const raw=frame.raw;
  for(const p of placed){
   const c=p.command;raw.save();raw.setTransform(frame.dpr,0,0,frame.dpr,0,0);raw.globalAlpha=1;raw.globalCompositeOperation='source-over';raw.filter='none';raw.shadowColor='transparent';raw.fillStyle=c.paint.background;raw.fillRect(p.box.left,p.box.top,p.box.right-p.box.left,p.box.bottom-p.box.top);raw.restore();
  }
  const expectedNativeCount=placed.filter(p=>probe?.suppress!==p.command.descriptor.id).length;let nativeOrdinal=0;
  for(const [instance,p] of placed.entries()){
   const c=p.command;
   const label={site:c.descriptor.id,descriptor:c.descriptor,instance,text:c.text,font:c.font,align:c.align,baseline:c.baseline,matrix:c.matrix,maxWidth:c.maxWidth??null,ink:p.ink,region:c.region,backing:p.box,paint:c.paint};frame.labels.push(label);
   if(probe?.suppress===c.descriptor.id)continue;
   raw.save();raw.setTransform(...c.matrix);raw.font=c.font;raw.fontKerning='none';raw.letterSpacing='0px';raw.wordSpacing='0px';raw.textAlign=c.align;raw.textBaseline=c.baseline;raw.direction=c.direction;raw.fillStyle=c.paint.foreground;raw.globalAlpha=1;raw.globalCompositeOperation='source-over';raw.filter='none';raw.shadowColor='transparent';
   const geometry=Object.freeze({width:frame.width,height:frame.height,dpr:frame.dpr,region:Object.freeze({...c.region}),ink:Object.freeze({left:p.ink.left,right:p.ink.right,top:p.ink.top,bottom:p.ink.bottom})});
   active=Object.freeze({token:c.token,descriptor:c.descriptor,canvas:frame.canvas,instance,execution:frame.execution,ordinal:nativeOrdinal++,count:expectedNativeCount,text:c.text,geometry});
   try{if(c.maxWidth===undefined)nativeFill.call(raw,c.text,p.x,p.y);else nativeFill.call(raw,c.text,p.x,p.y,c.maxWidth)}finally{active=null;raw.restore()}
  }
  frame.status='final';pending.delete(frame.canvas);completed.set(frame.canvas,frame);
 }
 function frame(callback){
  if(depth){depth++;try{const result=callback();if(result&&typeof result.then==='function')fail('asynchronous frame unsupported');return result}finally{depth--;}}
  const clear=()=>{for(const f of pending.values()){f.status='failed';completed.delete(f.canvas);}pending.clear()};
  for(let pass=0;pass<3;pass++){
   let result;depth=1;
   try{result=callback();if(result&&typeof result.then==='function')fail('asynchronous frame unsupported');}
   catch(error){clear();throw error}finally{depth=0}
   try{
    let reflow=false;
    for(const f of pending.values()){
     const axes=f.commands.filter(c=>c.descriptor.region==='axis-right');
     // Reserve the measured axis lane before graph geometry is finalized.
     const lane=axes.length?Math.max(68,...axes.map(c=>{const b=bounds(c,f);return Math.ceil(b.right-b.left+16)})):0;
     if(axes.length&&f.width-lane<160)fail('unplaceable semantic axis lane');
     if((gutters.get(f.canvas)||0)!==lane){gutters.set(f.canvas,lane);reflow=true;}
    }
    if(reflow){clear();continue;}
    for(const f of [...pending.values()])finish(f);
    return result;
   }finally{clear();}
  }
  fail('canvas lane allocation did not converge');
 }
 function isolated(canvas,siteID,color){
  const original=completed.get(canvas);
  if(!original||original.status!=='final'||!original.labels.some(l=>l.site===siteID)||!['#000000','#ffffff'].includes(color))fail('invalid isolated ink request');
  const mask=document.createElement('canvas');mask.width=canvas.width;mask.height=canvas.height;const raw=mask.getContext('2d');
  raw.fillStyle='#7f7f7f';raw.fillRect(0,0,mask.width,mask.height);
  for(const [instance,p] of original.placed.entries()){
   const c=p.command;if(c.descriptor.id!==siteID)continue;
   raw.save();raw.setTransform(...c.matrix);raw.font=c.font;raw.fontKerning='none';raw.letterSpacing='0px';raw.wordSpacing='0px';raw.textAlign=c.align;raw.textBaseline=c.baseline;raw.direction=c.direction;raw.fillStyle=color;
   active=Object.freeze({token:c.token,descriptor:c.descriptor,canvas:mask,owner:canvas,instance,execution:original.execution,text:c.text,diagnostic:true});
   try{if(c.maxWidth===undefined)nativeFill.call(raw,c.text,p.x,p.y);else nativeFill.call(raw,c.text,p.x,p.y,c.maxWidth)}finally{active=null;raw.restore()}
  }
  return {width:mask.width,height:mask.height,data:mask.toDataURL('image/png')};
 }
 const api=Object.freeze({site,text,begin,frame,isolated,plotWidth:(ctx,width,rightMargin)=>{const f=contexts.get(ctx);if(!f||!finite([width,rightMargin])||width<=0||rightMargin<0)fail('unprovable plot allocation');const result=width-Math.max(0,(gutters.get(f.canvas)||0)+4-rightMargin);if(result<=0)fail('unplaceable plot beside semantic lane');return result;},
  nativeToken:()=>active,
  phase:canvas=>(pending.get(canvas)||completed.get(canvas))?.status||null,
  inspect:()=>JSON.parse(JSON.stringify([...completed.values()].filter(f=>f.canvas.isConnected).map(f=>({canvas:f.canvas.id,width:f.width,height:f.height,dpr:f.dpr,status:f.status,trace:f.trace,labels:f.labels})))),
  descriptors:()=>[...sites.values()].map(s=>s.descriptor),
  probe:settings=>{if(settings!==null&&(!settings||Object.keys(settings).some(k=>k!=='suppress')||settings.suppress!==null&&typeof settings.suppress!=='string'))fail('invalid capture probe');probe=settings},
  pending:()=>pending.size
 });
 // Install before all authored scripts. Public native methods never receive
 // semantic authority; only the private captured nativeFill can paint text.
 const prototypes=[CanvasRenderingContext2D.prototype];if(window.OffscreenCanvasRenderingContext2D)prototypes.push(OffscreenCanvasRenderingContext2D.prototype);
 for(const prototype of prototypes){
  for(const method of ['fillText','strokeText'])Object.defineProperty(prototype,method,{configurable:false,writable:false,value:function(){fail('uncontracted native text')}});
  for(const method of ['save','restore','clip','clearRect','fillRect','strokeRect','fill','stroke','drawImage','putImageData','reset']){
   const original=prototype[method];
   Object.defineProperty(prototype,method,{configurable:false,writable:false,value:function(...args){
    const f=pending.get(this.canvas)||completed.get(this.canvas);
    if(f?.status==='final'&&!['save','restore'].includes(method))fail('paint after text finalization');
    if(f&&pending.has(this.canvas)){
     if(method==='save')f.clipStack.push(f.clipDepth);
     if(method==='restore')f.clipDepth=f.clipStack.pop()??f.clipDepth;
     if(method==='clip')f.clipDepth++;
     if(method==='reset'){f.clipDepth=0;f.clipStack=[];}
    }
    return original.apply(this,args);
   }});
  }
 }
 // Assigning either bitmap dimension clears the canvas, including assigning
 // its current value. Treat that reset as paint after a completed frame.
 for(const property of ['width','height']){
  const descriptor=Object.getOwnPropertyDescriptor(HTMLCanvasElement.prototype,property);
  Object.defineProperty(HTMLCanvasElement.prototype,property,{...descriptor,configurable:false,set(value){
   const current=pending.get(this)||completed.get(this);
   if(current?.status==='final')fail('paint after text finalization');
   return descriptor.set.call(this,value);
  }});
 }
 if(Object.prototype.hasOwnProperty.call(window,'CanvasText'))fail('duplicate helper');
 Object.defineProperty(window,'CanvasText',{value:api,writable:false,configurable:false});
})();
