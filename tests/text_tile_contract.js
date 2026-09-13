'use strict';
/* Independently reconcile the complete target against disjoint owned tile
 * regions. The renderer uses rectangle subtraction; this check uses a sweep
 * over vertical strips, so dropping a tile or double-owning a region fails. */
function reconcileTextTiles(measurement){
 const fail=reason=>{throw Error('raster setup failure: '+reason)};
 const t=measurement.tiling;
 const rect=r=>r&&['left','right','top','bottom'].every(k=>Number.isFinite(r[k]))&&r.left<r.right&&r.top<r.bottom;
 if(!t||!Array.isArray(t.sourceRects)||!t.sourceRects.length||!t.sourceRects.every(rect)||!Array.isArray(t.tiles)||!t.tiles.length||!Number.isInteger(t.plannedTiles)||t.plannedTiles!==t.capturedTiles||t.capturedTiles!==t.tiles.length)fail('incomplete tile metadata');
 let samples=0,expected=0,missing=0;const owned=[];
 for(const [index,tile] of t.tiles.entries()){
  const stable=Number.isInteger(tile.settleCaptures)&&tile.settleCaptures>=1&&tile.settleCaptures<=5&&tile.untouchedCaptures===tile.settleCaptures+1&&tile.untouchedFramesEqual===true;
  if(tile.index!==index||tile.completeFrame!==true||!stable||!tile.frame||!Number.isFinite(tile.frame.innerWidth)||!Number.isFinite(tile.frame.innerHeight)||!Number.isInteger(tile.decoded?.width)||!Number.isInteger(tile.decoded?.height)||tile.decoded.width<=0||tile.decoded.height<=0||!Number.isFinite(tile.sourceTranslation?.dx)||!Number.isFinite(tile.sourceTranslation?.dy)||!Array.isArray(tile.coverage)||!tile.coverage.every(rect)||!Array.isArray(tile.viewportCoverage)||!tile.viewportCoverage.every(rect))fail('incomplete tile frame metadata');
  const camera=tile.captureFrame;
  if(!camera||!['left','top','width','height'].every(k=>Number.isFinite(camera[k]))||camera.left<0||camera.top<0||camera.width<=0||camera.height<=0||camera.left+camera.width>tile.frame.innerWidth||camera.top+camera.height>tile.frame.innerHeight||tile.decoded.width!==Math.round(camera.width*2*tile.frame.devicePixelRatio)||tile.decoded.height!==Math.round(camera.height*2*tile.frame.devicePixelRatio))fail('capture frame and decoded raster disagree');
  if(!['original,backdrop,black,white','original,halo,backdrop,black,white'].includes(tile.captures?.join(',')))fail('incomplete tile capture phases');
  for(const k of ['sampleCount','expectedPixels','missingPixels'])if(!Number.isInteger(tile[k])||tile[k]<0)fail('missing tile visibility samples');
  samples+=tile.sampleCount;expected+=tile.expectedPixels;missing+=tile.missingPixels;
  owned.push(...tile.coverage);
 }
 if(samples!==measurement.sampleCount||expected!==measurement.expectedPixels||missing!==measurement.missingPixels)fail('tile sample reconciliation mismatch');
 for(let i=0;i<owned.length;i++)for(let j=i+1;j<owned.length;j++){
  const a=owned[i],b=owned[j];if(Math.max(a.left,b.left)<Math.min(a.right,b.right)&&Math.max(a.top,b.top)<Math.min(a.bottom,b.bottom))fail('overlapping tile ownership');
 }
 function gapsFor(target,covers){
  const cuts=[...new Set([target.left,target.right,...covers.flatMap(r=>[Math.max(target.left,Math.min(target.right,r.left)),Math.max(target.left,Math.min(target.right,r.right))])])].sort((a,b)=>a-b),gaps=[];
  for(let i=1;i<cuts.length;i++){
   const left=cuts[i-1],right=cuts[i],mid=(left+right)/2;
   const spans=covers.filter(r=>r.left<=mid&&r.right>=mid).map(r=>[Math.max(target.top,r.top),Math.min(target.bottom,r.bottom)]).filter(([a,b])=>a<b).sort((a,b)=>a[0]-b[0]);
   let y=target.top;
   for(const [top,bottom] of spans){if(top>y)gaps.push({left,right,top:y,bottom:top});y=Math.max(y,bottom);}
   if(y<target.bottom)gaps.push({left,right,top:y,bottom:target.bottom});
  }
  return gaps;
 }
 for(const region of owned)if(gapsFor(region,t.sourceRects).length)fail('tile coverage outside semantic target');
 const gaps=t.sourceRects.flatMap(r=>gapsFor(r,owned));
 if(t.complete!==!gaps.length||!Array.isArray(t.gaps)||(!gaps.length)!==!t.gaps.length)fail('tile coverage reconciliation mismatch');
 if(gaps.length&&!measurement.error)fail('passing text has missing tiles');
 return true;
}
module.exports={reconcileTextTiles};
