// Boolean are either true or false
function falseFunction() {
    return false;
}

// if statements 
function ourTrueOrFalse(isItTrueOrFalse) {
    if (isItTrueOrFalse) {
        return "That's true";
    }
    return "That's false";
}
console.log(ourTrueOrFalse(true));

// equality operator
function testEquality(value) {
    if (value == 12) {
        return "Equal to 12";
    }
    return "not equal to 12";
}
console.log(testEquality(12));

// strict equality operator
function testStrictEquality(value) {
    // strict equality does not convert types
    if (value === 12) {
        return "Equal to 12";
    }
    return "not equal to 12";
}
console.log(testStrictEquality(12));
console.log(testStrictEquality("12"));

// inequality operator
function testInequality(value) {
    if (value != 99) {
        return "Not equal to 99";
    }
    return "Equal to 99";
}
console.log(testInequality(33));

// strict inequality operator
function testStrictInequality(value) {
    if (value !== 99) {
        return "Not equal to 99";
    }
    return "Equal to 99";
}
console.log(testStrictInequality("99"));

// greater than operator
function testGreaterThan(value) {
    if (value > 999) {
        return "Greater than 999";
    }
    return "Not greater than 999";
}
console.log(testGreaterThan("99"));

// greater than or equal operator
function testGreaterOrEqual(value) {
    if (value >= 99) {
        return "Greater than or equal to 99";
    }
    return "Not greater than or equal to 99";
}
console.log(testGreaterOrEqual(88));

// similarly you can make less than or equal operators


// And operator
function testLogicalAnd(value) {
    // use and operator
    if (value <=50 && value >= 25) {
        return "Between 25 and 50";
    }
    return "Not between 25 and 50";
}

// Or operator
function testLogicalOr(value) {
    // use or operator
    if (value <=50 || value >= 25) {
        return "Outside of range of 25 and 50";
    }
    return "Inside range of 25 and 50";
}

// Else statements
function testElse(value) {
    // use else operator
    if (value > 5) {
        result = "Bigger than 5";
    } else {
        result = "Smaller than 5";
    }
}

// else if statements
function testElseIf(value) {
    // use else if operator
    if (value > 5) {
        result = "Greater than 5";
    } else if (value < 0) {
        result = "Less than 0";
    } else {
        return "Between 5 and 0";
    }
}

// order of if else statements matters
// because it returns on the first statement evaluated to be true


// Golf game logic
var names = ["Hole in One", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]

function golfScore(par, strokes) {
    if (strokes == 1) {
        return names[0]
    } else if (strokes <= par - 2) {
        return names[1]
    } else if (strokes == par - 1) {
        return names[2]
    } else if (strokes == par) {
        return names[3]
    } else if (strokes == par + 1) {
        return names[4]
    } else if (strokes == par + 2) {
        return names[5]
    } else if (strokes >= par + 3) {
        return names[6]
    }
}

console.log(golfScore(5, 4));


// switch statements
function testSwitchStatement(value) {
    var answer = ''
    switch (value) {
        // switch statement, checks case, break to leave loop
        case 1: answer = "alpha"; break;
        case 2: answer = "beta"; break;
        case 3: answer = "gama"; break;
        
        // two cases return the same answer
        case 4: 
        case 5: answer = "delta"; break;

        // default case
        default: answer = "no case"; break;
    }
    return answer;
    
}
console.log(testSwitchStatement(5));
