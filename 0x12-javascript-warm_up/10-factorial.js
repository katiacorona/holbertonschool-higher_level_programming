#!/usr/bin/node
'use strict';

const n = parseInt(process.argv.slice(2)[0]);
console.log(factorial(n));

function factorial (n) {
  if (n <= 1 || Number.isNaN(n)) {
    return 1;
  }
  const res = factorial(n - 1) * n;

  return res;
}
