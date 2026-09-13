'use strict';
const assert=require('node:assert/strict'),{closedSurface,accesses,functions}=require('../scripts/canvas_sources'),protocol=require('./mutation_protocol');
const rejected=[
 ['canvas.getContext("2d")','uncontracted canvas context or executable-code acquisition'],
 ['canvas["getContext"]("2d")','uncontracted canvas context or executable-code acquisition'],
 ['const native=CanvasRenderingContext2D.prototype.fillText','uncontracted canvas context or executable-code acquisition'],
 ['new OffscreenCanvas(10,10)','uncontracted canvas context or executable-code acquisition'],
 ['globalThis["OffscreenCanvasRenderingContext2D"].prototype','uncontracted canvas context or executable-code acquisition'],
 ['new Function("ctx.fillText()")()','uncontracted canvas context or executable-code acquisition'],
 ['eval("ctx.fillText()")','uncontracted canvas context or executable-code acquisition'],
 ['setTimeout("ctx.fillText()",1)','uncontracted scheduled executable source'],
 ['CanvasText.probe({suppress:"axis"})','diagnostic or unknown canvas API in product source'],
 ['const api=CanvasText;api.nativeToken()','diagnostic or unknown canvas API in product source'],
 ['CanvasText["text"]()','noncanonical canvas API access'],
 ['window.__learnCanvasNative.replaceBitmap(canvas,pixels)','diagnostic canvas oracle API in product source'],
];
try{
 for(const [source,expected] of rejected)assert(closedSurface(source).some(e=>e.assertion===expected),'closed canvas surface: '+source);
 for(const source of ['const text="getContext"','const text=`OffscreenCanvas`','// eval("x")\nlet x=1;','CanvasText.frame(()=>{});CanvasText.begin(canvas,520,310,2);'])assert.deepEqual(closedSurface(source),[],'nonexecutable spelling and canonical capability');
 for(const literal of ['[','(',')','}',';']){
  const source='function draw(ctx){const note='+JSON.stringify(literal)+';ctx.fillText("Visible",1,2)}';
  assert.equal(accesses(source).length,1,'literal delimiter does not change native inventory');
  const owner=functions(source)[0];assert.equal(source.slice(owner.start,owner.end),source,'literal delimiter does not truncate executable owner');
 }
 console.log((rejected.length+9)+'/'+(rejected.length+9)+' closed-surface and lexical-balance fixtures passed');
}catch(e){protocol.semantic(e.message.split('\n')[0]);process.exitCode=1}
