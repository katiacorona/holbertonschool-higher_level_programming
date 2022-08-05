#!/usr/bin/node
'use strict';

/*
Prints 'x' times 'C is fun'.
@x: the first argument of the script.
*/
const x = process.argv.slice(2)[0];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
