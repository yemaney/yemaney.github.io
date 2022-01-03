/* Create a function that takes in a roster array
and return the amount of astronauts in the roster array */


const countActiveAstronauts = (roster) => {
  // Code here!
  return roster.length;
};


const exampleRoster = [
  {
    firstName: "Chris",
    lastName: "Hadfield",
    nickname: "Space Oddity",
    prefix: "Astronaut",
    job: "Shuttle DJ"
  }
];

console.log(countActiveAstronauts(exampleRoster));
