#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  if (item) {
    const newArr = [];
    newArr.push(item);

    for (const i in newArr) {
      console.log(count + ': ' + newArr[i]);
      count += 1;
    }
  }
};
