'use strict';
const {reconcileTextTiles}=require('./text_tile_contract');
function reconcileSvgRaster(result){
 if(!result||!Array.isArray(result.rows)||!Array.isArray(result.failures))throw Error('raster setup failure: incomplete SVG result');
 for(const row of result.rows){
  if(!row.paint||row.paint.nodeIndex!==result.rows.indexOf(row))throw Error('raster setup failure: missing SVG raster identity');
  reconcileTextTiles(row.paint);
  if(!row.paint.error&&(!row.paint.sampleCount||row.paint.missingPixels||row.paint.expectedPixels!==row.paint.sampleCount))throw Error('raster setup failure: incomplete SVG visibility evidence');
 }
 return true;
}
module.exports={reconcileSvgRaster};
