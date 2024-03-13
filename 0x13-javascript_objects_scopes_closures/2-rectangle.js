#!/usr/bin/node
/**
 *this will  Check the parameters provided is equal to 0 or not
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
