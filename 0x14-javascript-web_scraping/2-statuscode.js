#!/usr/bin/node
const process = require('process');

const request = require('request');

const myargs = process.argv[2];

request(myargs, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
