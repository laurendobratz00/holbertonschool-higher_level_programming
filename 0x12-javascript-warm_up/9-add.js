#!/usr/bin/node
// a script that prints the addition of 2 integers
const myArgs = process.argv.slice(2);

function add(a, b) {
  console.log(parseInt(myArgs[0]) + parseInt(myArgs[1]));
}

add();
