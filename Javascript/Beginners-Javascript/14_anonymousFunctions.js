// anonymous function
var magic = function() {
    return new Date();
}

// arrow function
var magic2 = () => {
    return new Date();
}

// even shorter
var magic3 = () => new Date();

// arrow function with arguments
var myConcat = (arr1, arr2) => arr1.concat(arr2);
console.log(myConcat([1,3], [2,3]));

// can use anonymous functions with map and filter
const squareList = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredIntegers
}
var numArray = [-2, 5, 9]
console.log(squareList(numArray));