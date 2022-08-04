#!/usr/bin/node
'use strict';

const args = process.argv.slice(2);

if (args[0] == null) {
  console.log('No arguments');
} else {
  console.log(args[0]);
}
