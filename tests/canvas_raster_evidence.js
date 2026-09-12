'use strict';
const crypto=require('node:crypto');
// Independent evidence reconciliation. The browser uses rectangle subtraction;
// this reader uses a sweep union and recomputes every accepted pixel ratio.
function reconcileCanvasRaster(result, expected){
 const fail=assertion=>{throw Object.assign(Error(assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion})};
 const finite=n=>typeof n==='number'&&Number.isFinite(n);
 const rect=r=>r&&['left','right','top','bottom'].every(k=>finite(r[k]))&&r.left<r.right&&r.top<r.bottom;
 const digest=s=>typeof s==='string'&&/^[0-9a-f]{64}$/.test(s);
 const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const contrast=(a,b)=>{const lum=c=>c.slice(0,3).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0);const x=lum(a),y=lum(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
 const pixel=p=>Array.isArray(p)&&p.length===4&&p.every(x=>Number.isInteger(x)&&x>=0&&x<=255)&&p[3]===255;
 if(!result||result.inactive!==false||!Array.isArray(result.labels)||!result.labels.length||!Array.isArray(result.tiles)||!result.tiles.length||!Array.isArray(result.scale)||result.scale.length!==2||!result.scale.every(s=>finite(s)&&s>0))fail('missing canvas raster metadata');
 if(!expected||result.canvas!==expected.canvas||result.width!==expected.width||result.height!==expected.height||result.labels.length!==expected.labels.length)fail('wrong canvas raster identity');
 const phases=new Map();
 const tokens=new Set(),hash=value=>crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex');
 for(const [index,t] of result.tiles.entries()){
  if(t.index!==index||!rect(t.coverage)||t.coverage.left<0||t.coverage.top<0||t.coverage.right>result.width||t.coverage.bottom>result.height||!t.metrics||!Array.isArray(t.metrics.viewport)||!Array.isArray(t.metrics.bitmap)||!Array.isArray(t.metrics.owners)||!Array.isArray(t.dimensions)||!Array.isArray(t.sites))fail('missing canvas raster metadata');
  const [vw,vh,dpr]=t.metrics.viewport,c=t.captureFrame;
  if(![vw,vh,dpr].every(n=>finite(n)&&n>0)||!c||!['left','top','width','height'].every(k=>Number.isInteger(c[k]))||c.left<0||c.top<0||c.width<=0||c.height<=0||c.left+c.width>vw||c.top+c.height>vh)fail('invalid canvas capture frame');
  const expectedPhases=['normal-1','normal-2',...t.sites.flatMap(s=>['suppressed:'+s.id,'isolated:'+s.id+':#000000','reachable:'+s.id+':#000000','isolated:'+s.id+':#ffffff','reachable:'+s.id+':#ffffff'])];
  if(!equal(t.dimensions.map(d=>d.phase),expectedPhases)||new Set(expectedPhases).size!==expectedPhases.length||!digest(t.metricsHash)||!digest(t.traceHash)||!digest(t.secondTraceHash)||t.traceHash!==t.secondTraceHash)fail('incomplete canvas capture phases');
  for(const d of t.dimensions){
   if(d.width!==Math.round(c.width*2*dpr)||d.height!==Math.round(c.height*2*dpr)||!digest(d.pixelHash)||d.metricsHash!==t.metricsHash)fail('canvas raster frame correspondence differs');
   if(typeof d.captureToken!=='string'||!/^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$/.test(d.captureToken)||tokens.has(d.captureToken))fail('missing or duplicate canvas capture identity');tokens.add(d.captureToken);
   if(!t.clipStyles||!Array.isArray(t.clipStyles.normal)||!t.clipStyles.normal.length||!Array.isArray(t.clipStyles.geometry))fail('missing canvas clipping evidence');
   const square=t.clipStyles.normal.map(row=>({...row,styles:{...row.styles,borderTopLeftRadius:'0px',borderTopRightRadius:'0px',borderBottomLeftRadius:'0px',borderBottomRightRadius:'0px'}}));
   if(!equal(square,t.clipStyles.geometry)||d.clipHash!==hash(d.phase.startsWith('isolated:')?t.clipStyles.geometry:t.clipStyles.normal))fail('canvas clipping evidence differs');
  }
  if(t.dimensions[0].pixelHash!==t.dimensions[1].pixelHash||t.rasterHash!==t.dimensions[1].pixelHash)fail('nondeterministic canvas final frame');
  if(!Array.isArray(t.bitmapRestores)||!equal(t.bitmapRestores.map(r=>[r.id,r.color]),t.sites.flatMap(s=>[[s.id,'#000000'],[s.id,'#ffffff']])))fail('missing canvas bitmap restoration evidence');
  if(t.bitmapRestores.some(r=>![r.before,r.after,r.trace,r.restoredTrace].every(digest)||r.before!==r.after||r.trace!==r.restoredTrace))fail('canvas redraw failed bitmap restoration');
  phases.set(index,new Set(t.sites.map(s=>s.id)));
 }
 function covered(target,covers){
  const cuts=[...new Set([target.left,target.right,...covers.flatMap(r=>[Math.max(target.left,Math.min(target.right,r.left)),Math.max(target.left,Math.min(target.right,r.right))])])].sort((a,b)=>a-b);
  for(let i=1;i<cuts.length;i++){
   const x=(cuts[i-1]+cuts[i])/2,spans=covers.filter(r=>r.left<=x&&r.right>=x).map(r=>[Math.max(target.top,r.top),Math.min(target.bottom,r.bottom)]).filter(([a,b])=>a<b).sort((a,b)=>a[0]-b[0]);
   let y=target.top;for(const [top,bottom]of spans){if(top>y+1e-7)return false;y=Math.max(y,bottom)}if(y<target.bottom-1e-7)return false;
  }
  return true;
 }
 let count=0;
 for(const [index,label]of result.labels.entries()){
  const source=expected.labels[index];
  for(const key of ['site','instance','text','font','align','baseline','matrix','maxWidth','ink','region','backing','descriptor','paint'])if(!equal(label[key],source[key]))fail('wrong canvas raster identity');
  if(!rect(label.backing)||!rect(label.ink)||!rect(label.region)||!covered(label.backing,result.tiles.filter(t=>phases.get(t.index).has(label.site)).map(t=>t.coverage)))fail('incomplete canvas target tile coverage');
  if(!Array.isArray(label.samples)||!label.samples.length||label.coreSamples!==label.samples.length)fail('missing canvas final pixel samples');
  let missing=0,worst=Infinity;const owned=new Set(),tileCounts=new Map();
  for(const s of label.samples){
   const tile=result.tiles[s.tile];
   if(!tile||!phases.get(s.tile).has(label.site)||!finite(s.x)||!finite(s.y)||s.x<label.backing.left||s.x>label.backing.right||s.y<label.backing.top||s.y>label.backing.bottom||!pixel(s.foreground)||!pixel(s.backdrop)||s.coverage!==1)fail('invalid canvas final pixel sample');
   const key=s.x+':'+s.y;
   if(owned.has(key))fail('duplicate canvas pixel ownership');owned.add(key);
   const ratio=contrast(s.foreground,s.backdrop);if(!finite(s.ratio)||Math.abs(ratio-s.ratio)>1e-12)fail('canvas pixel contrast reconciliation differs');
   if(s.foreground.slice(0,3).every((c,i)=>Math.abs(c-s.backdrop[i])<2))missing++;
   worst=Math.min(worst,ratio);tileCounts.set(s.tile,(tileCounts.get(s.tile)||0)+1);
  }
  if(!Array.isArray(label.expectedCores)||!label.expectedCores.length||label.expectedCores.some(p=>!finite(p.x)||!finite(p.y)))fail('missing canvas full-ink evidence');
  const expectedPixels=new Set(label.expectedCores.map(p=>p.x+':'+p.y));
  if(expectedPixels.size!==label.expectedCores.length||expectedPixels.size!==owned.size||[...expectedPixels].some(key=>!owned.has(key)))fail('incomplete canvas final glyph coverage');
  if(label.missingCore!==missing||label.worstRatio!==worst)fail('canvas pixel summary reconciliation differs');
  for(const [tile,count]of tileCounts){const records=result.tiles[tile].sites.find(s=>s.id===label.site).instances.filter(i=>i.instance===label.instance);if(records.length!==1||records[0].coreSamples!==count)fail('canvas occurrence sample reconciliation differs');}
  if(missing)fail('canvas final glyph core occluded');
  if(worst<label.descriptor.minimumContrast)fail('text contrast below threshold');
  count+=label.samples.length;
 }
 return {canvas:result.canvas,labels:result.labels.length,tiles:result.tiles.length,samples:count};
}
module.exports={reconcileCanvasRaster};
