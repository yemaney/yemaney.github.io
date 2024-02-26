/* create a function that will take an astronaut object and 
job string as an argument and return an updated astronaut object
with the job as a new property
*/


const addJobToAstronaut = (astronaut, job) => {
  // Code here!

  // Remember to return a value!
  astronaut.job = job;
  return astronaut;
};



const exampleAstronaut = {
  firstName: "Chris",
  lastName: "Hadfield",
  nickname: "Space Oddity",
  prefix: "Astronaut"
};

console.log(exampleAstronaut);
console.log(addJobToAstronaut(exampleAstronaut, 'Shuttle DJ'));

