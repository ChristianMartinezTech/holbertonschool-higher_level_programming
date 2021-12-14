#!/usr/bin/node

const arg = process.argv;
const numbr = parseInt(arg[2]);
const message = 'X';

if (Number.isInteger(numbr) && numbr > 0) {
  for (let y = 0; y < numbr; y++) {
    console.log(message.repeat(numbr));
  }
} else {
  console.log('Missing size');
}
