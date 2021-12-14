#!/usr/bin/node

const arg = process.argv;
const numbr = parseInt(arg[2]);

if (Number.isInteger(numbr)) {
  console.log('My number: ' + Number(arg[2]));
} else {
  console.log('Not a number');
}
