/* Create a function that takes in a toggle object and will changes
the value of the isON property between true and false, and then 
return the updated object.*/


const switchToggle = (toggle) => {
  // Code here!

  // Remember to return a value!
  toggle.isOn = !toggle.isOn;
  return toggle;
};


const someToggle = {
  name: "toggleA",
  isOn: false
}

console.log(someToggle);
console.log(switchToggle(someToggle));
