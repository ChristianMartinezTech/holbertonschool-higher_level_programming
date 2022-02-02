#!/usr/bin/node
// script that computes the number of tasks completed by user id
// You must use the https://jsonplaceholder.typicode.com/todos API

// Including the axios module
const request = require('request');
const url = process.argv[2];

request(url, function (error, header, body) {
  if (error) {
    console.log(error);
  }

  const user = 0;
  const completedAmount = 0;

  for (i in header) {
    if (header[i] == userId) {
      if (user != 'userId') {
      }
    }
  }
});
