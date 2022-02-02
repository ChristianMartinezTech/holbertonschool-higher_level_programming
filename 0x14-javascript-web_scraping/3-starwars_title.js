#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer
// You must use the Star wars API https://swapi-api.hbtn.io/api/films/:id

// Including the axios module
const request = require('request');
const id = (process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
