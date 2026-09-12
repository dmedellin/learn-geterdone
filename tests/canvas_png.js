'use strict';
const zlib=require('node:zlib');
const table=Array.from({length:256},(_,n)=>{for(let i=0;i<8;i++)n=n&1?0xedb88320^(n>>>1):n>>>1;return n>>>0;});
function crc32(bytes){let n=0xffffffff;for(const byte of bytes)n=table[(n^byte)&255]^(n>>>8);return(n^0xffffffff)>>>0;}
function decodePNG(bytes){
 const fail=message=>{throw Error('raster setup failure: PNG '+message)};
 if(!Buffer.isBuffer(bytes)||!bytes.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])))fail('signature');
 let cursor=8,header=null,ended=false;const compressed=[];
 while(cursor<bytes.length){
  if(cursor+12>bytes.length)fail('truncated chunk');const length=bytes.readUInt32BE(cursor),end=cursor+12+length;
  if(end>bytes.length)fail('truncated chunk data');const type=bytes.toString('ascii',cursor+4,cursor+8),data=bytes.subarray(cursor+8,cursor+8+length);
  if(crc32(bytes.subarray(cursor+4,cursor+8+length))!==bytes.readUInt32BE(cursor+8+length))fail('CRC mismatch');
  if(!header&&type!=='IHDR')fail('header order');
  if(type==='IHDR'){
   if(header||length!==13)fail('header');header={width:data.readUInt32BE(0),height:data.readUInt32BE(4),depth:data[8],color:data[9],compression:data[10],filter:data[11],interlace:data[12]};
   if(!header.width||!header.height||header.width*header.height>64000000||header.depth!==8||![2,6].includes(header.color)||header.compression||header.filter||header.interlace)fail('unsupported raster format');
  }else if(type==='IDAT')compressed.push(data);
  else if(type==='IEND'){if(length)fail('end chunk');ended=true;cursor=end;break;}
  else if(['tRNS','iCCP'].includes(type)||type[0]===type[0].toUpperCase())fail('unsupported chunk '+type);
  cursor=end;
 }
 if(!ended||cursor!==bytes.length||!compressed.length)fail('incomplete stream');
 const {width,height}=header,channels=header.color===2?3:4,rowBytes=width*channels,total=(rowBytes+1)*height;
 let inflated;try{inflated=zlib.inflateSync(Buffer.concat(compressed),{maxOutputLength:total});}catch(e){fail('inflate: '+e.message);}
 if(inflated.length!==total)fail('decoded dimensions differ');
 const raw=Buffer.alloc(rowBytes*height),pixels=Buffer.alloc(width*height*4);
 const paeth=(a,b,c)=>{const p=a+b-c,x=Math.abs(p-a),y=Math.abs(p-b),z=Math.abs(p-c);return x<=y&&x<=z?a:y<=z?b:c;};
 for(let y=0;y<height;y++){
  const filter=inflated[y*(rowBytes+1)];if(filter>4)fail('unknown row filter');
  for(let x=0;x<rowBytes;x++){
   const at=y*rowBytes+x,left=x>=channels?raw[at-channels]:0,up=y?raw[at-rowBytes]:0,corner=y&&x>=channels?raw[at-rowBytes-channels]:0;
   const prediction=filter===0?0:filter===1?left:filter===2?up:filter===3?Math.floor((left+up)/2):paeth(left,up,corner);raw[at]=(inflated[y*(rowBytes+1)+x+1]+prediction)&255;
  }
 }
 for(let i=0;i<width*height;i++){for(let c=0;c<3;c++)pixels[i*4+c]=raw[i*channels+c];pixels[i*4+3]=channels===4?raw[i*channels+3]:255;}
 return {width,height,pixels};
}
module.exports={crc32,decodePNG};
