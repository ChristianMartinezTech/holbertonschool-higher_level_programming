#!/usr/bin/node
// display the status code of a GET request.

// Including the axios module
const request = require('request');
const url = process.argv[2];

request(url, function (err, response) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
