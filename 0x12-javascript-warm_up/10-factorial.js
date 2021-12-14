#!/usr/bin/node

function factorial (x) {
  if (x === 0 || !x) {
    return 1; // if number is 0
  } else {
    return x * factorial(x - 1); // if number is positive
  }
}

const arg = process.argv;
const num = parseInt(arg[2]);

console.log(factorial(num));
// if (Number.isInteger(num) && num > 1) {
//  const result = factorial(num);
//  console.log(result);
// } else {
//  console.log('NaN');
// }
