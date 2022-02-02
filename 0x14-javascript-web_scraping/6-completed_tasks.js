#!/usr/bin/node
// script that computes the number of tasks completed by user id
// You must use the https://jsonplaceholder.typicode.com/todos API

// Including the axios module
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const bodyData = JSON.parse(body);
  const finalResult = {};

  for (const key in bodyData) {
    if (finalResult[key.userId] && key.completed) {
      finalResult[key.userId] += 1;
    } else if (!finalResult[key.userId] && key.completed) {
      finalResult[key.userId] = 1;
    }
  }
  console.log(finalResult);
});
