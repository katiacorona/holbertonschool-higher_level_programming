#!/usr/bin/node
'use strict';

const num1 = parseInt(process.argv.slice(2)[0]);
const num2 = parseInt(process.argv.slice(2)[1]);
console.log(add(num1, num2));

function add (a, b) {
  return a + b;
}
