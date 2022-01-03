// create random decimal number using Math.random
function randomDecimal() {
    return Math.random();
}
console.log(randomDecimal());

// create random whole number
function randomWholeNumber() {
    
    return Math.floor(Math.random() * 100);
}
console.log(randomWholeNumber());

// function of random number between a range
function randomRange(min, max) {

    return Math.floor(Math.random() * (max - min + 1) + min);
}
console.log(randomRange(1, 100));

// convert str to int using parseInt
function convertToInt(str) {
    return parseInt(str);
}
console.log(typeof convertToInt("22"))
console.log(convertToInt("22"));

// specify the base of the number 
function binaryToNumber(str) {
    return parseInt(str, 2);
}
console.log(binaryToNumber("101101"));