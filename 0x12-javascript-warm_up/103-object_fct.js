#!/usr/bin/node

/*
Update this script by adding a new function incr 

not allowed to use var
*/
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
myObject.incr = function () {
  this.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
