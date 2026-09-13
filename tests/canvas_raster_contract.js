'use strict';
async function canvasFinalRaster(canvasID){
 'use strict';
 const semantic=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 const setup=message=>{throw Error('raster setup failure: '+message)};
 const canvas=document.getElementById(canvasID);
 if(!(canvas instanceof HTMLCanvasElement))semantic('missing canvas raster target');
 const lineage=[];for(let e=canvas;e;e=e.parentElement)lineage.push(e);
 const radii=['borderTopLeftRadius','borderTopRightRadius','borderBottomLeftRadius','borderBottomRightRadius'];
 const clipKeys=[...radii,'clip','clipPath','maskImage','overflowX','overflowY','transform','rotate','scale','translate','perspective','zoom','opacity','filter','mixBlendMode'];
 const clipStyles=()=>lineage.map((e,index)=>({index,id:e.id,tag:e.tagName,styles:Object.fromEntries(clipKeys.map(k=>[k,getComputedStyle(e)[k]]))}));
 for(const row of clipStyles()){
  const s=row.styles,m=new DOMMatrix(s.transform==='none'?undefined:s.transform);
  if(s.clip!=='auto'||s.clipPath!=='none'||s.maskImage!=='none')semantic('unprovable canvas CSS clipping');
  const scale=s.scale==='none'?[1,1]:s.scale.split(/\s+/).map(n=>n.endsWith('%')?parseFloat(n)/100:Number(n));
  if(!m.is2D||m.b!==0||m.c!==0||m.a<=0||m.d<=0||!scale.length||scale.length>2||scale.some(n=>!Number.isFinite(n)||n<=0)||!['none','0deg'].includes(s.rotate)||s.perspective!=='none')semantic('unprovable canvas CSS transform');
 }
 const initial=CanvasText.inspect().find(f=>f.canvas===canvasID);
 if(!initial||!initial.labels.length)semantic('empty canvas raster inventory');
 if(!canvas.getBoundingClientRect().width||!canvas.getBoundingClientRect().height){
  if(!lineage.some(e=>getComputedStyle(e).display==='none'))semantic('canvas active target has zero dimensions');
  return {canvas:canvasID,inactive:true,labels:[],reason:'display-none ancestor; requires another authored state witness'};
 }
 const owners=[];
 for(let e=canvas.parentElement;e;e=e.parentElement){const s=getComputedStyle(e);if(['auto','scroll'].some(x=>s.overflowX===x||s.overflowY===x))owners.push(e);}
 if(!owners.includes(document.scrollingElement))owners.push(document.scrollingElement);
 const saved=owners.map(e=>({e,x:e.scrollLeft,y:e.scrollTop}));
 const redraw=async()=>{
  if(typeof window.redrawLab==='function')window.redrawLab();
  else if(typeof window.redraw==='function')window.redraw();
  else if(typeof window.drawCurrent==='function')window.drawCurrent();
  else if(typeof window.__canvasFixtureRedraw==='function')window.__canvasFixtureRedraw();
  else semantic('missing canvas redraw owner');
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
 };
 const frame=()=>CanvasText.inspect().find(f=>f.canvas===canvasID);
 const metric=()=>({viewport:[innerWidth,innerHeight,devicePixelRatio,scrollX,scrollY],canvas:canvas.getBoundingClientRect().toJSON(),bitmap:[canvas.width,canvas.height],owners:owners.map(e=>({id:e.id,tag:e.tagName,scroll:[e.scrollLeft,e.scrollTop,e.scrollWidth,e.scrollHeight,e.clientWidth,e.clientHeight],rect:e.getBoundingClientRect().toJSON()}))});
 const decode=async data=>{
  const image=new Image();image.src='data:image/png;base64,'+data;await image.decode();const out=document.createElement('canvas');out.width=image.width;out.height=image.height;out.getContext('2d').drawImage(image,0,0);return {width:image.width,height:image.height,pixels:out.getContext('2d').getImageData(0,0,image.width,image.height).data};
 };
 const hash=async bytes=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(n=>n.toString(16).padStart(2,'0')).join('');
 const contrast=(a,b)=>{const lum=c=>c.slice(0,3).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0);const x=lum(a),y=lum(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
 const sourceWidth=initial.width,sourceHeight=initial.height;
 const captured=new Set(),expectedCores=new Map(initial.labels.map(l=>[l.instance,new Map()])),records=new Map(initial.labels.map(l=>[l.instance,{...l,coreSamples:0,missingCore:0,worstRatio:Infinity,samples:[],tiles:[]}])) ,tiles=[];
 let primaryFrameError=null;
 window.__learnCanvasRasterEvidence={canvas:canvasID,tiles,labels:[...records.values()]};
 const subtract=(rect,cover)=>{const l=Math.max(rect.left,cover.left),r=Math.min(rect.right,cover.right),t=Math.max(rect.top,cover.top),b=Math.min(rect.bottom,cover.bottom);if(l>=r||t>=b)return[rect];return[{left:rect.left,top:rect.top,right:rect.right,bottom:t},{left:rect.left,top:b,right:rect.right,bottom:rect.bottom},{left:rect.left,top:t,right:l,bottom:b},{left:r,top:t,right:rect.right,bottom:b}].filter(r=>r.right-r.left>1e-7&&r.bottom-r.top>1e-7);};
 const port=element=>{
  if(element===document.scrollingElement)return {left:0,top:0,right:innerWidth,bottom:innerHeight,sx:1,sy:1};
  const s=getComputedStyle(element),r=element.getBoundingClientRect();
  const width=parseFloat(s.width)+(s.boxSizing==='border-box'?0:parseFloat(s.paddingLeft)+parseFloat(s.paddingRight)+parseFloat(s.borderLeftWidth)+parseFloat(s.borderRightWidth));
  const height=parseFloat(s.height)+(s.boxSizing==='border-box'?0:parseFloat(s.paddingTop)+parseFloat(s.paddingBottom)+parseFloat(s.borderTopWidth)+parseFloat(s.borderBottomWidth));
  const sx=r.width/width,sy=r.height/height;
  if(![width,height,sx,sy].every(n=>Number.isFinite(n)&&n>0))setup('unresolved canvas scroll-owner scale');
  return {left:r.left+element.clientLeft*sx,top:r.top+element.clientTop*sy,right:r.left+(element.clientLeft+element.clientWidth)*sx,bottom:r.top+(element.clientTop+element.clientHeight)*sy,sx,sy};
 };
 const visibleBox=()=>{
  let box={left:0,top:0,right:innerWidth,bottom:innerHeight};
  for(let e=canvas.parentElement;e;e=e.parentElement){
   const s=getComputedStyle(e);
   if(e===document.body||e===document.documentElement)continue;
   if(['auto','scroll','hidden','clip'].includes(s.overflowX)){const p=port(e);box.left=Math.max(box.left,p.left);box.right=Math.min(box.right,p.right)}
   if(['auto','scroll','hidden','clip'].includes(s.overflowY)){const p=port(e);box.top=Math.max(box.top,p.top);box.bottom=Math.min(box.bottom,p.bottom)}
  }
  return box;
 };
 const place=async(x,y)=>{
  for(let pass=0;pass<2;pass++)for(const owner of owners){
   const r=canvas.getBoundingClientRect(),sx=r.width/sourceWidth,sy=r.height/sourceHeight;
   const v=port(owner);
   owner.scrollTo({left:owner.scrollLeft+(r.left+x*sx-(v.left+v.right)/2)/v.sx,top:owner.scrollTop+(r.top+y*sy-(v.top+v.bottom)/2)/v.sy,behavior:'instant'});
  }
  await new Promise(r=>requestAnimationFrame(r));
 };
 try{
  window.__learnCanvasRasterEvidence.capturePolicy='explicit instant scroll for tile movement and restoration';
  canvas.scrollIntoView({block:'center',inline:'center',behavior:'instant'});await new Promise(r=>requestAnimationFrame(r));
  let r=canvas.getBoundingClientRect(),v=visibleBox();
  if(r.width<=0||r.height<=0||v.right<=v.left||v.bottom<=v.top)semantic('canvas target has no reachable viewport');
  const sx=r.width/sourceWidth,sy=r.height/sourceHeight;
  const stepX=Math.max(1,(Math.min(innerWidth,v.right-v.left)-12)/sx),stepY=Math.max(1,(Math.min(innerHeight,v.bottom-v.top)-12)/sy);
  const xs=[],ys=[];for(let x=0;x<sourceWidth;x+=stepX)xs.push(Math.min(sourceWidth,x+stepX/2));for(let y=0;y<sourceHeight;y+=stepY)ys.push(Math.min(sourceHeight,y+stepY/2));
  if(xs.length*ys.length>4096)setup('unbounded canvas tile plan');
  for(const y of ys)for(const x of xs){
   await place(x,y);r=canvas.getBoundingClientRect();v=visibleBox();
   const extent={left:Math.max(0,Math.floor(Math.max(r.left,v.left))),top:Math.max(0,Math.floor(Math.max(r.top,v.top))),right:Math.min(innerWidth,Math.ceil(Math.min(r.right,v.right))),bottom:Math.min(innerHeight,Math.ceil(Math.min(r.bottom,v.bottom)))};
   if(extent.right<=extent.left||extent.bottom<=extent.top)continue;
   const captureFrame={left:extent.left,top:extent.top,width:extent.right-extent.left,height:extent.bottom-extent.top},tileIndex=tiles.length,guard=JSON.stringify(metric()),dimensions=[];
   const normalClips=clipStyles(),geometryClips=normalClips.map(row=>({...row,styles:{...row.styles,...Object.fromEntries(radii.map(k=>[k,'0px']))}}));
   const capture=async phase=>{
    const expectedClips=phase.startsWith('isolated:')?geometryClips:normalClips,clipGuard=JSON.stringify(expectedClips);
    if(JSON.stringify(clipStyles())!==clipGuard)setup('canvas clipping metrics changed before '+phase);
    if(JSON.stringify(metric())!==guard){window.__learnCanvasRasterEvidence.failure={phase:'before '+phase,expected:JSON.parse(guard),actual:metric(),captureFrame};setup('canvas capture metrics changed before '+phase);}
    const captureToken=crypto.randomUUID(),png=await learnCaptureRaster({mode:'canvas-final',captureToken,canvas:canvasID,tile:tileIndex,phase,captureFrame,metrics:metric(),clipStyles:expectedClips}),image=await decode(png);
    if(JSON.stringify(clipStyles())!==clipGuard)setup('canvas clipping metrics changed after '+phase);
    if(JSON.stringify(metric())!==guard){window.__learnCanvasRasterEvidence.failure={phase:'after '+phase,expected:JSON.parse(guard),actual:metric(),captureFrame};setup('canvas capture metrics changed after '+phase);}
    const expected=[Math.round(captureFrame.width*2*devicePixelRatio),Math.round(captureFrame.height*2*devicePixelRatio)];
    if(image.width!==expected[0]||image.height!==expected[1]||dimensions.some(d=>d.width!==image.width||d.height!==image.height)){
     window.__learnCanvasRasterEvidence.failure={phase,captureToken,captureFrame,expectedDimensions:expected,decodedDimensions:[image.width,image.height],metrics:metric(),clipStyles:clipStyles()};setup('dimensions changed');
    }
    dimensions.push({phase,captureToken,width:image.width,height:image.height,pixelHash:await hash(image.pixels),metricsHash:await hash(new TextEncoder().encode(guard)),clipHash:await hash(new TextEncoder().encode(clipGuard))});return image;
   };
   CanvasText.probe(null);await redraw();const firstTrace=JSON.stringify(frame()),first=await capture('normal-1');await redraw();const secondTrace=JSON.stringify(frame()),normal=await capture('normal-2');
   if(firstTrace!==secondTrace||await hash(first.pixels)!==await hash(normal.pixels)){
    const changed=[];let changedCount=0;for(let k=0;k<first.pixels.length;k+=4)if([0,1,2,3].some(i=>first.pixels[k+i]!==normal.pixels[k+i])){changedCount++;if(changed.length<100)changed.push({x:(k/4)%first.width,y:Math.floor(k/4/first.width),first:[...first.pixels.slice(k,k+4)],second:[...normal.pixels.slice(k,k+4)]});}
    window.__learnCanvasRasterEvidence.failure={assertion:'nondeterministic canvas final frame',firstTrace,secondTrace,firstHash:await hash(first.pixels),secondHash:await hash(normal.pixels),changedCount,changed,metrics:metric(),captureFrame};semantic('nondeterministic canvas final frame');
   }
   const current=frame();
   if(current.width!==sourceWidth||current.height!==sourceHeight||current.labels.length!==initial.labels.length||current.labels.some((l,i)=>JSON.stringify(l)!==JSON.stringify(initial.labels[i])))semantic('canvas state changed during tiling');
   const tile={index:tileIndex,captureFrame,visibleBox:v,clipStyles:{normal:normalClips,geometry:geometryClips},coverage:{left:Math.max(0,(Math.max(r.left,v.left)-r.left)/sx),top:Math.max(0,(Math.max(r.top,v.top)-r.top)/sy),right:Math.min(sourceWidth,(Math.min(r.right,v.right)-r.left)/sx),bottom:Math.min(sourceHeight,(Math.min(r.bottom,v.bottom)-r.top)/sy)},metrics:metric(),dimensions,bitmapRestores:[],metricsHash:await hash(new TextEncoder().encode(guard)),traceHash:await hash(new TextEncoder().encode(firstTrace)),secondTraceHash:await hash(new TextEncoder().encode(secondTrace)),rasterHash:await hash(normal.pixels),sites:[]};
   const ids=[...new Set(current.labels.filter(l=>r.left+l.backing.right*sx>extent.left&&r.left+l.backing.left*sx<extent.right&&r.top+l.backing.bottom*sy>extent.top&&r.top+l.backing.top*sy<extent.bottom).map(l=>l.site))];
   for(const id of ids){
    CanvasText.probe({suppress:id});await redraw();const suppressed=await capture('suppressed:'+id);
    // Diagnostic bitmaps replay isolated ink on the original canvas and CSS
    // composition chain. Accepted foreground is always normal.pixels.
    const masks=[],reachableMasks=[];
    for(const color of ['#000000','#ffffff']){
     const mask=CanvasText.isolated(canvas,id,color),decoded=await decode(mask.data.slice('data:image/png;base64,'.length));
     const priorTrace=JSON.stringify(frame()),previous=__learnCanvasNative.replaceBitmap(canvas,new ImageData(decoded.pixels,decoded.width,decoded.height));
     const styles=[];let primaryError=null;
     try{
      // Full-ink geometry uses the actual canvas and composition chain. Only
      // corner rounding is removed; native overflow, scrollbars, transforms,
      // canvas dimensions and viewport metrics remain unchanged. Rectangular
      // clipping is reconciled by complete target tiling, never exempted.
      for(let e=canvas;e;e=e.parentElement)if(radii.some(k=>getComputedStyle(e)[k]!=='0px')){styles.push({e,value:e.getAttribute('style')});e.style.setProperty('border-radius','0px','important');}
      try{masks.push(await capture('isolated:'+id+':'+color));}
      finally{for(const saved of styles){if(saved.value===null)saved.e.removeAttribute('style');else saved.e.setAttribute('style',saved.value);}styles.length=0;}
      reachableMasks.push(await capture('reachable:'+id+':'+color));
     }catch(error){primaryError=error;throw error;}finally{
      for(const saved of styles){if(saved.value===null)saved.e.removeAttribute('style');else saved.e.setAttribute('style',saved.value);}
      try{
       await redraw();
       const restored=canvas.getContext('2d').getImageData(0,0,canvas.width,canvas.height),restoredTrace=JSON.stringify(frame());
       const restoration={id,color,before:await hash(previous.data),after:await hash(restored.data),trace:await hash(new TextEncoder().encode(priorTrace)),restoredTrace:await hash(new TextEncoder().encode(restoredTrace))};tile.bitmapRestores.push(restoration);
       if(restoration.before!==restoration.after||restoration.trace!==restoration.restoredTrace)setup('canvas redraw failed bitmap restoration');
      }catch(restorationError){
       window.__learnCanvasRasterEvidence.restorationFailure={error:restorationError.message,assertion:restorationError.assertion||null,code:restorationError.code||null,primaryError:primaryError?.message||null};
       if(!primaryError||primaryError.code==='LEARN_CANVAS_SEMANTIC')setup('canvas restoration failed'+(primaryError?' after '+primaryError.message:'')+': '+restorationError.message);
      }
     }
    }
    const [black,white]=masks,[reachableBlack,reachableWhite]=reachableMasks,scale=normal.width/captureFrame.width,siteRecord={id,instances:[]};
    for(const label of current.labels.filter(l=>l.site===id)){
     const record=records.get(label.instance);let count=0,missing=0,minimum=Infinity;
     const left=Math.max(0,Math.floor((r.left+label.backing.left*sx-captureFrame.left)*scale)),right=Math.min(normal.width,Math.ceil((r.left+label.backing.right*sx-captureFrame.left)*scale)),top=Math.max(0,Math.floor((r.top+label.backing.top*sy-captureFrame.top)*scale)),bottom=Math.min(normal.height,Math.ceil((r.top+label.backing.bottom*sy-captureFrame.top)*scale));
     for(let py=top;py<bottom;py++)for(let px=left;px<right;px++){
      const screenX=captureFrame.left+(px+.5)/scale,screenY=captureFrame.top+(py+.5)/scale;
      if(screenX-.5/scale<v.left||screenX+.5/scale>v.right||screenY-.5/scale<v.top||screenY+.5/scale>v.bottom)continue;
      const cx=(screenX-r.left)/sx,cy=(screenY-r.top)/sy;
      if(cx<label.backing.left||cx>label.backing.right||cy<label.backing.top||cy>label.backing.bottom)continue;
      const k=(py*normal.width+px)*4,coverage=Math.min(...[0,1,2].map(c=>(white.pixels[k+c]-black.pixels[k+c])/255));
      if(coverage!==1)continue;
      const key=label.instance+':'+cx+':'+cy;
      expectedCores.get(label.instance).set(key,{tile:tileIndex,x:cx,y:cy,px,py});
      const reachable=Math.min(...[0,1,2].map(c=>(reachableWhite.pixels[k+c]-reachableBlack.pixels[k+c])/255));
      if(reachable!==1)continue;
      if(captured.has(key))continue;captured.add(key);
      const fg=[...normal.pixels.slice(k,k+4)],bg=[...suppressed.pixels.slice(k,k+4)],ratio=contrast(fg,bg);
      if(fg.slice(0,3).every((c,j)=>Math.abs(c-bg[j])<2)){missing++;record.missingCore++;}
      count++;record.coreSamples++;minimum=Math.min(minimum,ratio);record.worstRatio=Math.min(record.worstRatio,ratio);
      record.samples.push({tile:tileIndex,x:cx,y:cy,foreground:fg,backdrop:bg,coverage,ratio});
     }
     if(count){record.tiles.push(tileIndex);siteRecord.instances.push({instance:label.instance,coreSamples:count,missingCore:missing,worstRatio:minimum});}
    }
    tile.sites.push(siteRecord);CanvasText.probe(null);await redraw();
   }
   tiles.push(tile);
  }
  const labels=[...records.values()];for(const label of labels)label.expectedCores=[...expectedCores.get(label.instance).values()];
  for(const label of labels){
   let remaining=[label.backing];for(const tile of tiles)remaining=remaining.flatMap(r=>subtract(r,tile.coverage));label.coverageGaps=remaining;
   if(remaining.length)semantic('incomplete canvas target tile coverage');
   if(!label.coreSamples)semantic('zero final canvas glyph core samples');
   if([...expectedCores.get(label.instance).keys()].some(key=>!captured.has(key)))semantic('incomplete canvas final glyph coverage');
   if(label.missingCore)semantic('canvas final glyph core occluded');
   if(label.worstRatio<label.descriptor.minimumContrast)semantic('text contrast below threshold');
  }
  return {canvas:canvasID,inactive:false,width:sourceWidth,height:sourceHeight,scale:[sx,sy],tiles,labels};
 }catch(error){primaryFrameError=error;throw error;}finally{
  try{CanvasText.probe(null);await redraw();}
  catch(error){
   window.__learnCanvasRasterEvidence.finalRestorationFailure={error:error.message,primaryError:primaryFrameError?.message||null};
   if(!primaryFrameError||primaryFrameError.code==='LEARN_CANVAS_SEMANTIC')setup('canvas final restoration failed: '+error.message);
  }finally{for(const p of saved)p.e.scrollTo({left:p.x,top:p.y,behavior:'instant'});}
 }
}
module.exports={canvasFinalRaster};
