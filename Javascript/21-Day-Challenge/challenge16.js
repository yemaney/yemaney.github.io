/*
Write a function that takes in two arguments. Each argument represents a rocket
at a particular altitude and time. Calculate the average speed of the rocket.
*/



const getAverageSpeed = (firstPosition, secondPosition) => {
  // code here!

  return parseFloat(((secondPosition.altitude - firstPosition.altitude) / (secondPosition.time - firstPosition.time)).toFixed(1));
}


const firstPosition = {
  time: 1637074462,
  altitude: 1100
}
const secondPosition = {
  time: 1637074558,
  altitude: 2200
}

console.log(getAverageSpeed(firstPosition, secondPosition));
console.log(typeof getAverageSpeed(firstPosition, secondPosition));
