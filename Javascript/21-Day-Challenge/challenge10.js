/*Create a function that takes in array of weather objects and returns
the rounded average of wind speed*/

const averageWindSpeed1 = (weatherEntries) => {
  // Code here!
  // Method one using reduce
  return Math.round(weatherEntries.reduce((acc, weather) => acc + (weather.windSpeed / weatherEntries.length), 0));

};

const averageWindSpeed2 = (weatherEntries) => {
  // Code here!
  // Method two using loops
  let average = 0;
  for (let i = 0; i < weatherEntries.length; i++) {
    average += (weatherEntries[i].windSpeed / weatherEntries.length);
  }

  return Math.round(average);
};

const exampleEntries = [
  {
    temperature: 0,
    weather: "sunny",
    windDirection: "NNE",
    windSpeed: 24
  },
  {
    temperature: 10,
    weather: "cloudy",
    windDirection: "NNE",
    windSpeed: 9
  }
];

console.log(averageWindSpeed1(exampleEntries));
console.log(averageWindSpeed2(exampleEntries));
