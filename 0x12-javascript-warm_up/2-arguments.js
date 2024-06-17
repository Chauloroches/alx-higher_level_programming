#!/usr/bin/node
/* Script that prints a message depending of the number of arguments passed */
const args = process.argv;

if (args.length <= 0) {
  console.log('No argument');
} else if (args.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
