#!/usr/bin/node

function add (a, b) {
  const arg = process.argv;
  console.log(parseInt(arg[2]) + parseInt(arg[3]));
}
add(); // function call
