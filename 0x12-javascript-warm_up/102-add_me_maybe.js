#!/usr/bin/node
/*
Write a function to increments  a call function.

The function  visible from outside
Prototype: function (number, theFunction)
not allowed to use var
*/
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
