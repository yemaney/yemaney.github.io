/*
Your task is to write a function that will take in an array of objects 
containing switches. The function will change the value of the isOn 
property to true for every switch in the list, and then return the updated 
array.

You can use the previous switchToggle function from the fourth challenge, 
however be careful, since we want all of them on, not toggled!
*/

const switchToggle = (toggle) => {
  // Code here!

  // Remember to return a value!
  if (toggle.isOn === false) {
    toggle.isOn = !toggle.isOn;
  }
  return toggle;
};


const switchAllTogglesOn = (toggleList) => {
  // Code here!
  // Using Map
  return toggleList.map(toggle => switchToggle(toggle));
};

const switchAllTogglesOn = (toggleList) => {
  // Code here!
  // Using forEach
  toggleList.forEach(toggle => toggle.isOn = true);
  return toggleList;
};

const toggleList = [
  {
    name: "Air",
    isOn: true
  },
  {
    name: "Radio",
    isOn: false
  },
];


console.log(toggleList);
console.log(switchAllTogglesOn(toggleList));
