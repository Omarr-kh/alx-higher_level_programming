#!/usr/bin/node
let argc = 0;

exports.logMe = function (item) {
  console.log(argc + ': ' + item);
  argc++;
};
