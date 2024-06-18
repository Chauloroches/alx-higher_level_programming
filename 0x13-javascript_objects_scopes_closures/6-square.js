#!/usr/bin/node
/* A class Square that defines a square and inherits from Square of 5-square.js */


const OriginalSquare = require('./5-square');

class Square extends OriginalSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
