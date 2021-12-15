#!/usr/bin/node

// Class Declaration
module.exports = class Rectangle {
  constructor (w, h) { // Constructor
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () { // print width and height with "X" character
    for (let y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () { // print width and height with "X" TIMES TWO
    this.width = this.width * 2;
    for (let y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () { // exchange width and height
    for (let y = 0; y < this.width; y++) {
      console.log('X'.repeat(this.height));
    }
  }
};
