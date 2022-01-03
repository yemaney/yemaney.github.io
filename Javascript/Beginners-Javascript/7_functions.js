// Example
function myFunction() {
    // do work here
    console.log('myFunction')
}

// call function
myFunction();

//  functions with parameters
function myFunctionWithParameters(a, b) {
    console.log(a - b);
}
myFunctionWithParameters(10, 5);

/* 
Scope (visibility of variable) 
Global variables can be seen anywhere
Local can be seen only by the function they are defined in
*/

// Global variables

var myGlobalVariable = 10

function fun1() {
    // with no var keyword it becomes global
    oopsGlobalVariable = 5;
}


function checkGlobalVariable() {
    var output = "";
    if (typeof myGlobalVariable != "undefined") {
        output += 'myGlobalVariable ' + myGlobalVariable;
    }
    if (typeof oopsGlobalVariable != "undefined") {
        output += ' oopsGlobalVariable ' + oopsGlobalVariable;
    }
    console.log(output);
}

fun1();
checkGlobalVariable();


// Local Variables
function myLocalVariable() {
    var myVar = 5;
    console.log(myVar);
}
myLocalVariable();

// console.log(myVar); // will raise error


// Local vs Global Variables
// local takes precedence

var outerWear = "T-shirt"

function myOutfit() {
    var outerWear = "Sweater"
    return outerWear
}

console.log(myOutfit());
console.log(outerWear);


// function with no return value returns undefined
var sum = 0;
function undefinedReturnValue() {
    sum += 1;
}

console.log(undefinedReturnValue());


// assign a return value to a variable
function processVariable(number) {
    return number / 2;
}

processed = processVariable(10);
console.log(processed);

// next in line function
function nextInLineFunction(array, item) {
    // push item into array and return first element
    array.push(item);
    return array.shift();
}

var array = [1, 2, 3, 4, 5];
console.log("Before: " + JSON.stringify(array));
console.log(nextInLineFunction(array, 6));
console.log("After: " + JSON.stringify(array));


// default parameters
const increment = (function() {
    return function increment(number, value = 1) {
        return number + value;
    };
})();
console.log(increment(5, 2));
console.log(increment(5));

// rest operator
const sumFunction = (function() {
    return function sumFunction(...args) {
        return args.reduce((a, b) => a + b, 0);
    };
})();
console.log(sumFunction(1,2,3))