#!/usr/bin/node

const argc = process.argv;

if (argc.length <= 2) {
  console.log('No argument');
} else if (argc.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
