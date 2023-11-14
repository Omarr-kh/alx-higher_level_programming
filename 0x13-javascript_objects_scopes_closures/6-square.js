#!/usr/bin/node
const SquarePre = require('./5-square');

class Square extends SquarePre {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += c;
      }
      console.log(rec);
    }
  }
}

module.exports = Square;
