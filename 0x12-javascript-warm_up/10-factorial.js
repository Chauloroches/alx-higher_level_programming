#!/usr/bin/node
/* Script that computes and prints a factorial */
const args = process.argv.slice(2);
const n = parseInt(args[0], 10);

function factorial(n) {
  if (isNaN(n)) {
    return 1; 
  }
  if (n === 0 || n === 1) {
    return 1; 
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
