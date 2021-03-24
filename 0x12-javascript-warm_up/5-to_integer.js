#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs[0]) {
  console.log('My number: ' + myArgs[0]);
} else {
  console.log('Not a number');
}
