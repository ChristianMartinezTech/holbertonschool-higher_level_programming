#!/usr/bin/node

// Including the fs module
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (err, content) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});