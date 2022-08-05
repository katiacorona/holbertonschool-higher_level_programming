#!/usr/bin/node
'use strict';

/*
Prints a square using the character 'X'.
@size: the first argument of the script and the size of the square.
*/
const size = process.argv.slice(2)[0];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
