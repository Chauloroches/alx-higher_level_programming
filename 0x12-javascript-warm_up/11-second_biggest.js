#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments. */
const args = process.argv.slice(2).map(Number);

function secondLargest(arr) {
  const len = arr.length;
  
  if (len <= 1) {
    return 0;
  }

  let first = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < len; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }

  return second;
}

console.log(secondLargest(args));
