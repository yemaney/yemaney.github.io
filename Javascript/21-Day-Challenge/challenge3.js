/* gauge object has current, min and max as properties
Create a function that will take the gauge object as a parameter
and return true if its current value is between its
minimum and maximum */

const checkGaugeStatus = (gauge) => {
  // Check if the current is between the minimum and maximum
  return (gauge.min < gauge.current && gauge.current < gauge.max)
}

const exampleGauge = {
  current: 0.4,
  min: 0.1,
  max: 0.9
}

console.log(exampleGauge);
console.log(checkGaugeStatus(exampleGauge));
