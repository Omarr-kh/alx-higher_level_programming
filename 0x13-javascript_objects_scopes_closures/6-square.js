#!/usr/bin/node
const SquarePre = require('./5-square');

class Square extends SquarePre {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}

module.exports = Square;
