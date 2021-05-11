#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/', function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let o = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        o = o + 1;
      }
    }
  }
  console.log(o);
});
