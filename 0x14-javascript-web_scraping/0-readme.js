#!/usr/bin/node

// Including the fs module
const fs = require('fs')

fs.open(process.argv[2], 'r', function (err, contents) {
  if (err) {
    return console.error(err)
  }
  console.log(contents)
})
