'use strict';
const {accesses}=require('../scripts/canvas_sources'),protocol=require('./mutation_protocol');
const cases=[
 ["let key='unrelated';key='fillText';ctx[key]('x',1,2)",'reassigned canvas native property'],
 ["const first='fillText';let key='other';key=first;ctx[key]('x',1,2)",'reassigned canvas native alias'],
 ["const key=`fillText`;ctx[key]('x',1,2)",'template canvas native property'],
 [String.raw`const key=\`fi\u006clText\`;ctx[key]('x',1,2)`.replaceAll('\\`','`'),'escaped template canvas native property']
];
for(const [source,assertion] of cases)if(!accesses(source).length){protocol.semantic(assertion);process.exit(1)}
console.log(cases.length+'/'+cases.length+' canvas property-source fixtures passed');
