// ternary operator is like a one line if else operator
function ternary(a, b) {
    return a === b ? true : false;
}
console.log(ternary(1, 2));


// nesting ternary operators
function checkSign(num) {
    return num > 0 ? "positive" : num < 0 ? "negative" : "0";
}
console.log(checkSign(-2));