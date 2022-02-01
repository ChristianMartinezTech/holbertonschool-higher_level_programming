#!/usr/bin/node

// Including the fs module
var fs = require('fs');


file = process.argv[2]
fs.open(file, 'r', function (err, contents) {
    if (err) {
        return console.error(err);
    }
    console.log(contents);
});
