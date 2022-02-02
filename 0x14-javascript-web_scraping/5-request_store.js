#!/usr/bin/node
// Script that gets contents of a webpage into a file.
// The first argument is the URL to request
// The second argument the file path to store the body response

// Including the axios module
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (error, header, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, body, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
