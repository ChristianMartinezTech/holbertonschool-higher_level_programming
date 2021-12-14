#!/usr/bin/node

const message = 'C is fun';
const arg = process.argv;
const numbr = parseInt(arg[2]);

if (Number.isInteger(numbr)) {
  for (let i = 0; i < numbr; i++) {
    console.log(message);
  }
} else {
  console.log('Missing number of occurrences');
}
