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
    this.height = this.height * 2;
  }

  rotate () { // exchange width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
