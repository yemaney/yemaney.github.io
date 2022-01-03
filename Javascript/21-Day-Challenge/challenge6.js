/* Create a function that takes in a roster array and an
astronaut object  as inputs. The function will add the astronaut
to the roster and return the updated roster array.*/

const addAstronautToRoster = (roster, astronaut) => {
  // Code here!
  roster.push(astronaut);
  return roster;

};


const exampleRoster = []
const exampleAstronaut = {
  firstName: "Chris",
  lastName: "Hadfield",
  nickname: "Space Oddity",
  prefix: "Astronaut"
}

console.log(exampleRoster);
console.log(addAstronautToRoster(exampleRoster, exampleAstronaut));
