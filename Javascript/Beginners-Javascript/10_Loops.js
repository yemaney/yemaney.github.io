// while looping, to push to myArray as long as i < 5
var myArray = [];
var i = 0;

while (i < 5) {
    myArray.push(i);
    i++;
}

console.log(myArray)

// for loop
var ourArray = [];

// initialize i, make condition i < 5 and increment i
for (var i = 0; i < 4; i++) {
    ourArray.push(i);
}
console.log(ourArray);

// for loop to calculate sum
var ourArr = [1,2,3,4,5,6,7,8,9,10];
var ourTotal = 0;

for (var i = 0; i < ourArr.length; i++) {
    ourTotal += ourArr[i];
}
console.log(ourTotal);

// do while loop
var Arr = [];
var i = 10;

do {
    Arr.push(i);
    i++;
} while (i < 5) 

console.log(Arr)