#!/usr/bin/node
// a script that prints the first argument passed to it
const myArgs = process.argv.slice(2);

if (myArgs[0]) {
  console.log(myArgs[0]);
} else {
  console.log('No argument');
}
