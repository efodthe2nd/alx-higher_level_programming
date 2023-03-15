#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      const Rect = class Rectangle {};
	  return new Rect();
    }

    this.width = w;
    this.height = h;
  }
};
