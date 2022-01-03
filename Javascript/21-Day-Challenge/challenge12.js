/*
Your task is to write a function that will take in an array of objects 
containing a sender and a message as a parameter. The function will then 
parse a message from each object, add it to an array then return the built array.
*/

const parseTranscripts = (messages) => {
  // Code here!
  return messages.map(message => `${message.origin}: ${message.message}`);
};


const messages = [
  { origin: "MC", message: "Hello!" },
  { origin: "Shuttle", message: "Hey!" },
]

console.log(messages);
console.log(parseTranscripts(messages));
