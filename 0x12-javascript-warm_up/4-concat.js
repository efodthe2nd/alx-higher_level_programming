#!/usr/bin/node

const mem = process.argv.length;

if (mem === 2 || mem > 4) {
  console.log('undefined is undefined');
} else if (mem === 3) {
  console.log(process.argv[2] + ' is undefined');
} else if (mem === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
