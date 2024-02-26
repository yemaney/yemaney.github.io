/* Create a function that takes in the temperature, weather conditions,
wind speed, and direction as parameters. Convert the temperature from 
fahrenheit to degrees Celsius, and the wind speed from miles/hour
to meters/second. Return an object with all the parameters as properties.*/

const storeWeatherConditions = (temperature, condition, windSpeed, windDirection) => {
  // Code here!

  // Remember to return an object!

  // method 1
  // let weather = {};
  // weather.temperature = Math.round((temperature - 32) * 5/9);
  // weather.condition = condition;
  // weather.windSpeed = Math.round(windSpeed * 1609 / 3600);
  // weather.windDirection = windDirection;

  // return weather;

  // method 2
  this.temperature = Math.round((temperature - 32) * 5 / 9);
  this.condition = condition;
  this.windSpeed = Math.round(windSpeed * 1609 / 3600);
  this.windDirection = windDirection;
  return this;

};

console.log(storeWeatherConditions(32, "Sunny with small clouds", 20, "NNE"));
