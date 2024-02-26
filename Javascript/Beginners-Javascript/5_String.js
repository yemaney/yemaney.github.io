// Example
var firstName = 'Yemane'

// Escaping literal quotes
var  myString = "I am \"Escaping\""
console.log(myString)

// or escaping using single and double quotes
var newString = 'I m "Escaping" ' 
console.log(newString)


// Concatenate strings together,
var concat = 'This is the start' + ' This is the end' 
console.log(concat)

// can also use  augmented operators
// can also concat using variable names
var adjective = 'Great'
var sentence = 'Javascript is '
sentence += adjective
console.log(sentence)


// length of strings
sentenceLength = sentence.length
console.log(sentenceLength)

// brackets for indexing
firstLetterIndex = sentence[0]
console.log(firstLetterIndex)

// indexing last character
var LastCharacter = sentence[sentence.length - 1]
console.log(LastCharacter)


// string immutability, can change using indexing
var wrongString = 'Jello World'
wrongString = 'Hello World'

// make word blanks game
function makeWordBlanks(myAdjective, myNoun, myVerb, myAdverb) {
    var result = ''
    result += 'The ' + myAdjective + ' ' + myNoun + ' ' + myVerb + ' ' + myAdverb

    return result
}

console.log(makeWordBlanks("red", "dog", "run", "quickly"))

/* template literal strings 
can be multiline
can hae '" characters without escaping them
can have variable in them
*/
const person = {
    name: 'John',
    age: 34
};

const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old`;

console.log(greeting);

// make a list from object, with template literal strings
const result = {
    success: ["max-length", "no-amd", "prefer-arrow-functions"],
    failure: ["no-var", "var-on-top", "line break"],
    skipped: ["id-blacklist", "no dup-keys"]
};
function makeList(arr) {
    const resultDisplayArray = [];
    for (let i = 0; i < arr.length; i++) {
        resultDisplayArray.push(`<li class="text-warning">${arr[i]}</li>`);
    };
    return resultDisplayArray;
};

console.log(makeList(result.failure));
