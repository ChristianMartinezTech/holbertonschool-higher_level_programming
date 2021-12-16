#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const i in list) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
