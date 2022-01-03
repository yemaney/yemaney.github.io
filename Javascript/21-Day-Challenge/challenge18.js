/*
Your task is to write a function that will take in an array of lunch 
choices (strings) and return the choice as a string with the most votes.

There is always two lunch choices, and always an odd number of astronauts!
*/

const chooseLunchWinner = (listOfChoices) => {
  //Code here!

  let dinnerCounts = listOfChoices.reduce((acc, item) => {
      acc[item] = (acc[item] || 0) + 1;
      return acc
  }, {});
  return Object.keys(dinnerCounts).reduce((acc, item) => dinnerCounts[acc] > dinnerCounts[item] ? acc : item);

};


const listOfChoices = [
  "Chicken Dinner",
  "Chicken Dinner",
  "Chicken Dinner",
  "Ice Cream Sandwich",
  "Ice Cream Sandwich"
];

console.log(listOfChoices);
console.log(chooseLunchWinner(listOfChoices));
