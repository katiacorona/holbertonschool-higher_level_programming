#!/usr/bin/node
'use strict';

const n = parseInt(process.argv.slice(2)[0]);
console.log(factorial(n));

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  const res = n * factorial(n - 1);

  return res;
}
