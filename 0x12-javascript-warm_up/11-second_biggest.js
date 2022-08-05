#!/usr/bin/node
'use strict';

// convert the string array into a array of numbers
const intArray = process.argv.slice(2).map(Number);

console.log(second(intArray));

function second (nums) {
  // check if the array has at least two numbers
  if (nums.length < 2) {
    return 0;
  }

  // sort the array in descending order
  const sortedArray = nums.sort(function (a, b) { return (b - a); });

  return sortedArray[1];
}
