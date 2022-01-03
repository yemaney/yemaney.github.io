// Examples
var ourDog = {
    "name": "kirby",
    "age": 5  
};

// Access properties of an object
var dogName = ourDog.name;
console.log(dogName)

var dogAge = ourDog['age']
console.log(dogAge)

var name = "name";
console.log(ourDog[name]);

// Updating an object
ourDog.name = "fido";
console.log(ourDog);

// add new properties to the object
ourDog.color = "brown";
console.log(ourDog);

// delete  properties from the object
delete ourDog.color;
console.log(ourDog);

// check if the object has a property
function checkProperty(obj, property) {
    if (obj.hasOwnProperty(property)) {
        return obj[property];
    } else {
        return "Not a property";
    }
}
console.log(checkProperty(ourDog, "color"));

// accessing nested object properties
var nestedObject = {
    "outside": {
        "inside": "data",
    }
}
console.log(nestedObject.outside.inside);

// destructuring object properties
var coordinates = {x: 1, y: 2, z: 3}
const {x: a, y: b, z: c} = coordinates // a= 1, b= 2, c= 3

console.log(a);
console.log(b);
console.log(c);

// destructuring nested object properties
const forecast = {
    today: {
        min: 72,
        max: 83
    },
    tomorrow: {
        min: 73.3,
        max: 84.
    }
};

function getMaxTomorrow(forecast) {
    "use strict";

    const { tomorrow : { max : maxTomorrow } } = forecast;
    
    return maxTomorrow;
};
console.log(getMaxTomorrow(forecast));

// destructuring objects to pass it as a parameter
const stats = {
    max : 55,
    standardDeviation : 5.84,
    median : 34,
    mode : 23.55,
    min : -0.01,
    average : 36
};
const half = (function() {

    return function half({max, min}) {
        return (max + min) / 2;
    };

})(); 

console.log(stats);
console.log(half(stats));


// object literal declarations
const createPerson = (name, age, gender) => ( {name, age, gender});

console.log(createPerson("John", 24, "Male"));

// object can contain a function
const bicycle = {
    gear: 2,
    setGear(newGear) {
        "use strict";
        this.gear = newGear;
    }
};
bicycle.setGear(3);
console.log(bicycle.gear);