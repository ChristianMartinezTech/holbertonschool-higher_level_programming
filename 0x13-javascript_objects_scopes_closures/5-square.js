#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle { // Square inheriting from Rectangle
  constructor (size) {
    super(size, size); // Bringing w and h as size
  }
}
module.exports = Square; // Exporting square to main
