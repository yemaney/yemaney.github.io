/*
Your task is to write a function that will take in a launch date and 
a mission name as strings. Calculate the difference between two dates 
in days and return an object containing the name of the mission and a 
rounded day difference.
*/

const timeRemaining = (launchDate, missionName, fakeToday) => {
  const today = fakeToday || new Date(); // Do not alter this line!
  let newLaunchDate = new Date(launchDate);

  // convert from milliseconds to days,  then round
  daysRemaining = Math.round((newLaunchDate - today) / (1000 * 60 * 60 * 24));
  return { missionName, daysRemaining };
};


const launchDate = "2021-12-12"
const fakeToday = new Date("2021-12-01")
const missionName = "Moon visit"


console.log(timeRemaining(launchDate, missionName));
console.log(timeRemaining(launchDate, missionName, fakeToday));
