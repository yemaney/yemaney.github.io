/* write a function called parseMessage that takes two string parameters origin and message
and returns a message in the form of stringOne: stringTwo */

const parseMessage = (origin, message) => {
    return origin + ': ' + message;
}

console.log(parseMessage("Mission Control", "Hello there!"))