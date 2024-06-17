#!/usr/bin/node
/* script that prints two arguments passed to it */
const args = process.argv.slice(2);

console.log(`${args[0] || 'undefined'} is ${args[1] || 'undefined'}`);
