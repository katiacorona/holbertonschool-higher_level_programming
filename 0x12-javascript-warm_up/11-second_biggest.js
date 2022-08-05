#!/usr/bin/node
'use strict';

const intArray = process.argv.slice(2).map(Number);
console.log(second(intArray));

function second (nums) {
  const len = nums.length;

  // check if there is at least two elements
  if (len < 2) {
    return 0;
  }

  // sort the array
  nums.sort();

  // return the second largest number
  return nums[len - 2];
}
