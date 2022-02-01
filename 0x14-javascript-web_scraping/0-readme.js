#!/usr/bin/node

// Including the fs module
const fs = require('fs')
const file = process.argv[2]
fs.open(file, 'r', function (err, contents) {
  if (err) {
    console.error(err);
  } else {
    console.log(contents);
  }
});
