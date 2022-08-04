#!/usr/bin/node
'use strict';

const args = process.argv.slice(2);
const len = args.length;

if (len > 1) {
  console.log('Arguments found');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
