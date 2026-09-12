'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {decodePNG}=require('./canvas_png'),{reconcileCanvasRaster}=require('./canvas_raster_evidence');
function reconcileCanvasArtifacts(result,expected,{directory,frames}){
 const fail=assertion=>{throw Object.assign(Error(assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion})};
 const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b),hash=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
 const structural=reconcileCanvasRaster(result,expected),requests=new Map();
 for(const request of frames){const token=request.metadata?.captureToken;if(!token)continue;if(requests.has(token))fail('duplicate canvas artifact capture identity');requests.set(token,request);}
 const expectedCores=new Map(result.labels.map(l=>[l.instance,new Map()])),samples=new Map(result.labels.map(l=>[l.instance,new Map()]));let artifacts=0;
 for(const tile of result.tiles){
  const images=new Map();
  for(const dimension of tile.dimensions){
   const request=requests.get(dimension.captureToken),metadata=request?.metadata;
   if(!request||metadata.mode!=='canvas-final'||metadata.canvas!==result.canvas||metadata.tile!==tile.index||metadata.phase!==dimension.phase||!equal(metadata.captureFrame,tile.captureFrame)||!equal(metadata.metrics,tile.metrics)||!equal(metadata.clipStyles,dimension.phase.startsWith('isolated:')?tile.clipStyles.geometry:tile.clipStyles.normal))fail('canvas raster artifact identity differs');
   if(typeof request.rasterFile!=='string'||path.basename(request.rasterFile)!==request.rasterFile||!request.rasterFile.endsWith('.png'))fail('missing owned canvas raster artifact');
   const file=path.join(directory,request.rasterFile);let stat;try{stat=fs.lstatSync(file);}catch{fail('missing owned canvas raster artifact');}
   if(!stat.isFile()||stat.isSymbolicLink())fail('canvas raster artifact is not an owned regular file');
   const image=decodePNG(fs.readFileSync(file));
   if(image.width!==dimension.width||image.height!==dimension.height||request.decoded.width!==image.width||request.decoded.height!==image.height)throw Error('raster setup failure: canvas artifact dimensions changed');
   if(hash(image.pixels)!==dimension.pixelHash)throw Error('raster setup failure: canvas artifact pixel hash differs');
   images.set(dimension.phase,image);artifacts++;
  }
  const normal=images.get('normal-2'),capture=tile.captureFrame,r=tile.metrics.canvas,[sx,sy]=result.scale,scale=normal.width/capture.width,v=tile.visibleBox;
  if(!v||!['left','right','top','bottom'].every(k=>Number.isFinite(v[k])))fail('missing canvas visible-frame evidence');
  for(const label of result.labels){
   if(!tile.sites.some(s=>s.id===label.site))continue;
   const suppressed=images.get('suppressed:'+label.site),black=images.get('isolated:'+label.site+':#000000'),white=images.get('isolated:'+label.site+':#ffffff'),reachBlack=images.get('reachable:'+label.site+':#000000'),reachWhite=images.get('reachable:'+label.site+':#ffffff');
   const left=Math.max(0,Math.floor((r.left+label.backing.left*sx-capture.left)*scale)),right=Math.min(normal.width,Math.ceil((r.left+label.backing.right*sx-capture.left)*scale)),top=Math.max(0,Math.floor((r.top+label.backing.top*sy-capture.top)*scale)),bottom=Math.min(normal.height,Math.ceil((r.top+label.backing.bottom*sy-capture.top)*scale));
   const expectedMap=expectedCores.get(label.instance),sampleMap=samples.get(label.instance);
   for(let py=top;py<bottom;py++)for(let px=left;px<right;px++){
    const screenX=capture.left+(px+.5)/scale,screenY=capture.top+(py+.5)/scale;
    if(screenX-.5/scale<v.left||screenX+.5/scale>v.right||screenY-.5/scale<v.top||screenY+.5/scale>v.bottom)continue;
    const x=(screenX-r.left)/sx,y=(screenY-r.top)/sy;if(x<label.backing.left||x>label.backing.right||y<label.backing.top||y>label.backing.bottom)continue;
    const at=(py*normal.width+px)*4,core=(a,b)=>[0,1,2].every(c=>b.pixels[at+c]-a.pixels[at+c]===255);if(!core(black,white))continue;
    const key=x+':'+y;expectedMap.set(key,{tile:tile.index,x,y,px,py});
    if(!core(reachBlack,reachWhite)||sampleMap.has(key))continue;
    sampleMap.set(key,{tile:tile.index,x,y,foreground:[...normal.pixels.subarray(at,at+4)],backdrop:[...suppressed.pixels.subarray(at,at+4)]});
   }
  }
 }
 for(const label of result.labels){
  const expectedMap=expectedCores.get(label.instance),sampleMap=samples.get(label.instance);
  if(!equal([...expectedMap.values()],label.expectedCores))fail('canvas full-ink artifact coverage differs');
  if(sampleMap.size!==label.samples.length)fail('canvas surviving-ink artifact coverage differs');
  for(const sample of label.samples){
   const actual=sampleMap.get(sample.x+':'+sample.y);
   if(!actual||sample.tile!==actual.tile||!equal(sample.foreground,actual.foreground)||!equal(sample.backdrop,actual.backdrop))fail('canvas final foreground/backdrop artifact mismatch');
  }
 }
 return {...structural,artifacts,independentPNG:true};
}
module.exports={reconcileCanvasArtifacts};
