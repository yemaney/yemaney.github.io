// creat a class using class syntax
class SpaceShuttle {
    constructor(targetPlanet) {
        this.targetPlanet = targetPlanet;
    }
};

var zeus = new SpaceShuttle("Jupiter");
console.log(zeus);


// getters and setters
class Book {
    // constructor
    constructor(author) {
        this._author = author;
    }

    // getter
    get writer() {
        return this._author;
    }

    // setter
    set writer(updateAuthor) {
        this._author = updateAuthor;
    }
}

var gameOfThrones = new Book("Unknown");
console.log(gameOfThrones);
gameOfThrones.writer = "George R.R Martin";
console.log(gameOfThrones);
