#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle { // Square inheriting from Rectangle
  constructor (size) {
    super(size, size); // Bringing w and h as size
  }
};
