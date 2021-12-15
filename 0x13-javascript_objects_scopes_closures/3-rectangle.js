#!/usr/bin/node

// Class Declaration
module.exports = class Rectangle {
  constructor (w, h) { // Constructor
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Dynamic method
  print () {
    for (let y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }
};
