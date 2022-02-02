#!/usr/bin/node
//  script that prints the number of movies where
// the character “Wedge Antilles” is present.
// You must use the Star wars API https://swapi-api.hbtn.io/api/films/

// Including the axios module
const request = require('request');
const url = process.argv[2];

request(url, function (error, request, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).results;
  let presentIn = 0;

  for (const dataindex in data) {
    const filmCharacters = data[dataindex].characters;

    for (const charindex in filmCharacters) {
      if (filmCharacters[charindex].includes('18')) {
        presentIn++;
      }
    }
  }
  console.log(presentIn);
});
