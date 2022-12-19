#!/usr/bin/node

/*
Write a function that executes x times a function.

function must be visible from outside
Prototype: function (x, theFunction)
not allowed to use var
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
