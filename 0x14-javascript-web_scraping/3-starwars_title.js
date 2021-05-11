#!/usr/bin/node
const request = require('request');
const process = require('process');
const myargs = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + myargs + '/', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
