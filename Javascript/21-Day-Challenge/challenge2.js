// make a function that takes an astronaut object as a parameter and returns
// a string using it's properties as the

const generateAstronautTag = (astronaut) => {
  return `${astronaut.prefix}: ${astronaut.firstName} "${astronaut.nickname}" ${astronaut.lastName}`;
};

const exampleAstronaut = {
  firstName: "Neil",
  lastName: "Armstrong",
  nickname: "Steps",
  prefix: "Astronaut"
}

console.log(exampleAstronaut);
console.log(generateAstronautTag(exampleAstronaut));