#!/usr/bin/node

exports.esrever = function (list) {
  const revArray = []; // New Reversed Array

  for (let i = list.length - 1; i >= 0; i--) {
    revArray.push(list[i]);
  }
  return revArray;
};
