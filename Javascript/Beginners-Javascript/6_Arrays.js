// Example
var myArray = ["John", 23, 3.15, null, false];

// multidimensional array
var myArrayMultidimensional = [["red"], ["green"], ["blue"]]

// indexing array
var first = myArray[0];

// indexing a multidimensional array
var red = myArrayMultidimensional[0][0]
console.log(red)

// array mutability
myArray[0] = "Dave"
console.log(myArray)

// appending to an array
var numArray = [1, 2, 3]
numArray.push(4)
console.log(numArray)

// removing last element from array with pop
var poppedFromArray = numArray.pop()
console.log(poppedFromArray)
console.log(numArray)

// remove first element from array with shift
var shiftedFromArray = numArray.shift()
console.log(shiftedFromArray)
console.log(numArray)

// add element to beginning of array with unshift
numArray.unshift(1)
console.log(numArray)


// Shopping List
var shoppingList = [["cereal", 3], ["milk", 2], ["egg", 1]]

// spread operator, let you copy an array
const arr1 = ["JAN", "FEB", "MAR"]
let arr2;
(function() {
    arr2 = [...arr1]
    arr2[0] = 'potato'
})();
console.log(arr1);
console.log(arr2);

// destructing an array
const [z, x, , y] = [1, 2, 3, 4]
console.log(z,x,y);

// using destructuring to swap variables
let a = 8, b = 6;
(() => {
    "use strict";
    [a, b] = [b, a];
})();
console.log(a,b);

// spread operator  to change array
const source = [1,2,3,4,5,6,7,8,9,10];
function removeFirstTwo(list) {

    const [ , , ...arr] = list;
    return arr;
};
console.log(source);
console.log(removeFirstTwo(source));