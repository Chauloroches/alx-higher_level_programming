#!/usr/bin/node
/* A class Square that defines a square and inherits from Square of 5-square.js */
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();

console.log('Double:');
s1.double();
s1.print();
