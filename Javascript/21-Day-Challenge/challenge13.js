/*
Your task is to write a function that will take in an array of objects 
containing a gauge reading (min, max, current). The function will then 
check if the gauge current value is within spec (between min and max) 
and check the next gauge. If one of the values is outside the spec, return 
false, if they are all ok, return true.
*/

const checkGaugeStatus = (gauge) => {
  // Check if the current is between the minimum and maximum
  return (gauge.min < gauge.current && gauge.current < gauge.max);
};

const checkAllGauges = (gaugeList) => {
  // Code here!
  return Boolean(gaugeList.reduce((acc, gauge) => acc * checkGaugeStatus(gauge)));
};


const gaugeList = [
  {
    current: 0.4,
    min: 0.1,
    max: 0.9
  },
  {
    current: 1.2,
    min: 0.1,
    max: 0.6
  }
];


console.log(gaugeList);
console.log(checkAllGauges(gaugeList));
